#!/usr/bin/env python3
"""Вход скилла effectcraft: установленный CLI, живой каталог, проверка плана, запуск и проверка проекта.

  ec.py which                          путь и версия CLI, версия справочников
  ec.py search ТЕКСТ                   команды, у которых id или название содержит ТЕКСТ
  ec.py describe ID [ID…]              параметры команд из живого каталога
  ec.py check PLAN.json                есть ли команды в живом CLI и знает ли он ключи параметров
  ec.py run PLAN.json --save-as NEW.ecproj [--project SRC.ecproj]
                                       выполнить план одним процессом и сохранить в новый файл
  ec.py verify PROJECT.ecproj [--comp C] [--times 0,1.5] [--alpha] [--sequence 'dir/seq_*.png' --frames N]
                                       переоткрыть, отрендерить кадры, записать отчёт и квитанцию для хука
  ec.py -- АРГУМЕНТЫ                   передать аргументы CLI как есть

Скрипт ничего не устанавливает. Нет CLI — сообщает, как его поставить.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _common as C  # noqa: E402
import _png  # noqa: E402

PLAN_KEYS = ("command", "id")


def out(obj) -> None:
    print(json.dumps(obj, ensure_ascii=False, indent=1))


def load_steps(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    steps = data.get("steps") if isinstance(data, dict) else data
    if not isinstance(steps, list):
        raise SystemExit(f"{path}: нужен JSON-массив шагов или объект с ключом steps")
    norm = []
    for n, s in enumerate(steps, 1):
        cmd = next((s.get(k) for k in PLAN_KEYS if s.get(k)), None)
        if not cmd:
            raise SystemExit(f"{path}: шаг {n} без command")
        norm.append({"command": cmd, "params": s.get("params") or {}})
    return norm


def recipe_placeholders() -> set[str]:
    found = set()
    for f in (C.SKILL_DIR / "references" / "recipes").glob("*.json"):
        try:
            found.update(json.loads(f.read_text(encoding="utf-8")).get("placeholders", []))
        except (OSError, json.JSONDecodeError):
            pass
    return found


def cmd_which(_):
    cli = C.find_cli()
    ver = C.cli_version(cli)
    refs = C.refs_version()
    res = {"cli": cli, "version": ver, "referencesVersion": refs}
    if ver != refs:
        res["warning"] = (f"справочники собраны для {refs}, а CLI — {ver}: верь живому каталогу "
                          "(ec.py search/describe) и пересобери справочники: build_refs.py")
    out(res)


def cmd_search(a):
    items = C.catalog(C.find_cli(), a.text)
    out([{"id": c["id"], "label": c.get("label"), "params": c.get("params", "{}")} for c in items])


def cmd_describe(a):
    cli = C.find_cli()
    with C.Mcp(cli) as mcp:
        res = [mcp.tool("describe_command", {"command": cid}) for cid in a.ids]
    out(res if len(res) > 1 else res[0])


def check_steps(steps: list[dict], cat: list[dict]) -> list[str]:
    by_id = {c["id"]: c for c in cat}
    placeholders = recipe_placeholders()
    problems = []
    for n, s in enumerate(steps, 1):
        spec = by_id.get(s["command"])
        if not spec:
            problems.append(f"шаг {n}: команды {s['command']} нет в этой версии CLI")
            continue
        schema = spec.get("schema") or {}
        allowed = set((schema.get("properties") or {}).keys())
        if schema.get("additionalProperties") is False:
            extra = sorted(set(s["params"]) - allowed)
            if extra:
                problems.append(f"шаг {n} {s['command']}: неизвестные ключи {extra}; допустимы {sorted(allowed)}")
        for key in ("text", "name"):
            val = s["params"].get(key)
            if isinstance(val, str) and val in placeholders and key == "text":
                problems.append(f"шаг {n} {s['command']}: текст «{val}» — заглушка рецепта, замени на утверждённый")
    return problems


def cmd_check(a):
    steps = load_steps(Path(a.plan))
    problems = check_steps(steps, C.catalog(C.find_cli()))
    out({"plan": a.plan, "steps": len(steps), "ok": not problems, "problems": problems})
    return 0 if not problems else 1


def cmd_run(a):
    cli = C.find_cli()
    target = Path(a.save_as).resolve()
    src = Path(a.project).resolve() if a.project else None
    if src and src == target:
        raise SystemExit("EC-02: исходный проект не перезаписываем, укажи новый --save-as")
    if target.exists() and not a.overwrite:
        raise SystemExit(f"{target} уже есть; выбери новое имя или добавь --overwrite")
    steps = load_steps(Path(a.plan))
    problems = check_steps(steps, C.catalog(cli))
    real = [p for p in problems if "заглушка" not in p or not a.allow_placeholders]
    if real:
        out({"ok": False, "problems": real})
        return 1
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as tmp:
        json.dump(steps, tmp, ensure_ascii=False)
    argv = [cli, "run"]
    argv += ["--project", str(src)] if src else ["--empty"]
    argv += ["--commands", tmp.name, "--save-as", str(target), "--json"]
    try:
        r = subprocess.run(argv, capture_output=True, text=True, timeout=a.timeout)
    except subprocess.TimeoutExpired:
        out({"ok": False, "result": "unknown", "hint": "EC-08: сначала проверь, сохранился ли проект; правку вслепую не повторяй"})
        return 1
    finally:
        os.unlink(tmp.name)
    sys.stdout.write(r.stdout)
    sys.stderr.write(r.stderr)
    return r.returncode


def _render(cli, project, comp, t, path, transparent, max_side):
    argv = [cli, "render-frame", "--project", str(project), "--time", f"{t:g}",
            "--max-side", str(max_side), "--out", str(path), "--json"]
    if comp is not None:
        argv[2:2] = ["--comp", str(comp)]
    if transparent:
        argv.append("--transparent")
    r = subprocess.run(argv, capture_output=True, text=True, timeout=300)
    if r.returncode != 0 or not Path(path).exists():
        return {"ok": False, "error": (r.stderr or r.stdout).strip()[:400]}
    return _png.inspect(Path(path))


def cmd_verify(a):
    cli = C.find_cli()
    project = Path(a.project).resolve()
    if not project.exists():
        raise SystemExit(f"нет файла {project}")
    digest = C.sha256(project)
    outdir = Path(a.out).resolve() if a.out else project.with_suffix(".verify")
    outdir.mkdir(parents=True, exist_ok=True)
    checks, fails, warns = [], [], []

    r = subprocess.run([cli, "info", "--project", str(project), "--json"], capture_output=True, text=True, timeout=300)
    try:
        info = json.loads(r.stdout)
    except json.JSONDecodeError:
        info = None
    if r.returncode != 0 or not info:
        fails.append("проект не открылся заново: " + (r.stderr or r.stdout).strip()[:300])
        info = {}
    proj = info.get("project", {})
    items = proj.get("items", [])
    comps = [i for i in items if i.get("type") == "Composition"]
    missing = [i.get("name") for i in items if i.get("missing")]
    if missing:
        fails.append(f"нет файлов у элементов проекта: {missing}")
    comp = None
    if comps:
        if a.comp is None:
            comp = next((c for c in comps if c.get("id") == proj.get("activeComp")), comps[0])
        else:
            comp = next((c for c in comps if str(c.get("id")) == str(a.comp) or c.get("name") == a.comp), None)
            if not comp:
                fails.append(f"композиции {a.comp} нет; есть {[c.get('name') for c in comps]}")
    elif info:
        fails.append("в проекте нет композиций")
    checks.append({"reopen": bool(info), "cliVersion": info.get("version"), "comps": [
        {k: c.get(k) for k in ("id", "name", "size", "frameRate", "duration", "layers")} for c in comps]})

    frames = []
    if comp:
        fps, dur = float(comp.get("frameRate") or 25), float(comp.get("duration") or 0)
        last = max(0.0, dur - 1.0 / fps)
        times = [float(x) for x in a.times.split(",")] if a.times else sorted({0.0, round(dur / 2, 3), round(last, 3)})
        for t in times:
            if t > last + 0.5 / fps:
                warns.append(f"время {t} за последним кадром {last:.3f} (EC-05)")
            png = outdir / f"frame_{t:07.3f}.png"
            res = _render(cli, project, comp.get("name"), t, png, False, a.max_side)
            res.update(time=t, file=str(png))
            frames.append(res)
            if not res.get("ok"):
                fails.append(f"кадр {t}: {res.get('error')}")
            elif res.get("blank"):
                warns.append(f"кадр {t} одноцветный — проверь, что слои видны")
        digests = {f.get("digest") for f in frames if f.get("ok")}
        if len(frames) > 1 and len(digests) == 1:
            warns.append("все кадры одинаковые — анимации на этих временах нет")
        if a.alpha:
            t = times[len(times) // 2]
            png = outdir / f"alpha_{t:07.3f}.png"
            res = _render(cli, project, comp.get("name"), t, png, True, a.max_side)
            res.update(time=t, file=str(png), transparent=True)
            frames.append(res)
            lo, hi = (res.get("alpha") or [255, 255])
            if not res.get("ok") or lo == 255:
                fails.append("прозрачности нет: в кадре нет пикселей с альфой < 255 (EC-06)")
            elif hi == 0:
                fails.append("кадр полностью прозрачный")
    checks.append({"frames": frames})

    if a.sequence:
        files = sorted(glob.glob(a.sequence))
        seq = {"pattern": a.sequence, "count": len(files)}
        if not files:
            fails.append(f"секвенция {a.sequence}: файлов нет")
        else:
            if a.frames and len(files) != a.frames:
                fails.append(f"секвенция: {len(files)} кадров, ждали {a.frames}")
            sample = [files[0], files[len(files) // 2], files[-1]]
            seq["sample"] = [dict(_png.inspect(Path(f)), file=f) for f in sample]
            sizes = {(s.get("width"), s.get("height")) for s in seq["sample"]}
            if any(not s.get("ok") for s in seq["sample"]) or len(sizes) > 1:
                fails.append("секвенция: битые кадры или разный размер")
            if a.alpha and not any((s.get("alpha") or [255])[0] < 255 for s in seq["sample"]):
                fails.append("секвенция без прозрачности (EC-06)")
        checks.append({"sequence": seq})

    if a.video:
        v = Path(a.video)
        size = v.stat().st_size if v.exists() else 0
        checks.append({"video": str(v), "bytes": size, "decoded": False})
        if not size:
            fails.append(f"видео {v} не найдено или пустое")
        else:
            warns.append("видео не декодировалось скриптом — посмотри его глазами или кадрами")

    report = {"project": str(project), "sha256": digest, "ok": not fails, "fails": fails, "warnings": warns,
              "checks": checks, "verifiedAt": time.strftime("%Y-%m-%dT%H:%M:%S")}
    (outdir / "verify.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    C.receipt_path(digest).write_text(json.dumps(
        {"project": str(project), "sha256": digest, "ok": report["ok"], "report": str(outdir / "verify.json")},
        ensure_ascii=False), encoding="utf-8")
    out({"ok": report["ok"], "fails": fails, "warnings": warns, "frames": [f.get("file") for f in frames],
         "report": str(outdir / "verify.json")})
    return 0 if report["ok"] else 1


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv[:1] == ["--"]:
        cli = C.find_cli()
        os.execv(cli, [cli, *argv[1:]])
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("which").set_defaults(fn=cmd_which)
    s = sub.add_parser("search"); s.add_argument("text"); s.set_defaults(fn=cmd_search)
    s = sub.add_parser("describe"); s.add_argument("ids", nargs="+"); s.set_defaults(fn=cmd_describe)
    s = sub.add_parser("check"); s.add_argument("plan"); s.set_defaults(fn=cmd_check)
    s = sub.add_parser("run"); s.add_argument("plan"); s.add_argument("--save-as", required=True)
    s.add_argument("--project"); s.add_argument("--overwrite", action="store_true")
    s.add_argument("--allow-placeholders", action="store_true", help="для пробного прогона рецепта как есть")
    s.add_argument("--timeout", type=int, default=900); s.set_defaults(fn=cmd_run)
    s = sub.add_parser("verify"); s.add_argument("project"); s.add_argument("--comp")
    s.add_argument("--times", help="секунды через запятую; по умолчанию начало, середина, последний кадр")
    s.add_argument("--alpha", action="store_true", help="ждём прозрачный фон")
    s.add_argument("--sequence", help="glob секвенции PNG, например 'out/seq_*.png'")
    s.add_argument("--frames", type=int, help="сколько кадров должно быть в секвенции")
    s.add_argument("--video", help="путь к видеофайлу: проверяется наличие и размер")
    s.add_argument("--out", help="папка для кадров и отчёта; по умолчанию <проект>.verify/")
    s.add_argument("--max-side", type=int, default=480); s.set_defaults(fn=cmd_verify)
    a = p.parse_args(argv)
    try:
        return a.fn(a) or 0
    except C.CliNotFound as e:
        out({"ok": False, "error": str(e)})
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
