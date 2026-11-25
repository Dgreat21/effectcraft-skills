#!/usr/bin/env python3
"""Пересобрать справочники скилла из живого CLI.

  python3 build_refs.py            перегенерировать таблицы команд в references/topics/*.md и VERSION
  python3 build_refs.py --check    только сверить: совпадает ли версия и состав команд (код 1, если нет)

Ручная часть каждого файла (раздел «Как работать») не трогается: скрипт меняет только
блоки между метками toc и generated. Одна команда попадает ровно в одну тему.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _common as C  # noqa: E402

TOPICS = {
    "project": "Проект и файлы",
    "footage": "Материалы и импорт",
    "composition": "Композиции и время",
    "layers": "Слои, текст и шейпы",
    "animation": "Свойства, ключи и анимация",
    "effects": "Эффекты",
    "masks": "Маски, пути, ротоскоп",
    "expressions": "Выражения и родители",
    "camera": "Камера, свет, 3D",
    "export": "Рендер и экспорт",
    "tracking": "Трекинг и стабилизация",
    "puppet": "Куклы (Puppet)",
    "other": "Правка, интерфейс, шаблоны и прочее",
}

FAMILY = {
    "file": "project", "project": "project", "item": "project",
    "footage": "footage", "mediaBrowser": "footage",
    "comp": "composition", "time": "composition",
    "layer": "layers", "text": "layers", "shape": "layers",
    "prop": "animation", "keys": "animation", "anim": "animation",
    "effect": "effects", "effects": "effects",
    "mask": "masks", "path": "masks", "roto": "masks", "objectMatte": "masks",
    "expr": "expressions",
    "camera": "camera", "material": "camera", "light": "camera",
    "render": "export", "renderQueue": "export",
    "track": "tracking",
    "puppet": "puppet",
}

# Точные исключения из семейного правила (смысл важнее префикса).
EXACT = {
    "layer.setSwitch": "camera", "layer.newLight": "camera", "layer.newCamera": "camera",
    "layer.cameraSettings": "camera", "layer.new3dPrimitive": "camera", "layer.castsShadows": "camera",
    "view.set3DView": "camera", "view.reset3DView": "camera", "view.set3DViewCamera": "camera",
    "view.get3D": "camera",
    "prop.setExpression": "expressions", "prop.convertExpressionToKeyframes": "expressions",
    "layer.setParent": "expressions",
    "file.exportLottie": "export", "file.exportTimeline": "export", "file.checkOutput": "export",
    "file.relinkFootage": "footage", "layer.replaceSource": "footage",
}
PATTERNS = [
    (re.compile(r"^view\.3d\."), "camera"),
    (re.compile(r"^layer\.mask\."), "masks"),
    (re.compile(r"^timeline\.revealMask$"), "masks"),
]

TOC_START, TOC_END = "<!-- toc:start -->", "<!-- toc:end -->"
GEN_START, GEN_END = "<!-- generated:start -->", "<!-- generated:end -->"


def topic_of(cid: str) -> str:
    if cid in EXACT:
        return EXACT[cid]
    for rx, topic in PATTERNS:
        if rx.search(cid):
            return topic
    return FAMILY.get(cid.split(".")[0], "other")


def cell(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def render_generated(version: str, cmds: list[dict]) -> tuple[str, list[str]]:
    fams = defaultdict(list)
    for c in sorted(cmds, key=lambda c: c["id"]):
        fams[c["id"].split(".")[0]].append(c)
    lines, heads = [GEN_START, f"<!-- build_refs.py, EffectCraft CLI {version}; руками не править -->", ""], []
    for fam in sorted(fams):
        head = f"Команды {fam}.* ({len(fams[fam])})"
        heads.append(head)
        lines += [f"## {head}", "", "| id | что делает | параметры |", "| --- | --- | --- |"]
        for c in fams[fam]:
            menu = " › ".join(c.get("menu") or [])
            label = cell(c.get("label", "")) + (f" ({cell(menu)})" if menu else "")
            lines.append(f"| `{c['id']}` | {label} | {cell(c.get('params') or '{}')} |")
        lines.append("")
    lines.append(GEN_END)
    return "\n".join(lines), heads


def slug(head: str) -> str:
    s = re.sub(r"[^\w\s-]", "", head.lower(), flags=re.UNICODE)
    return re.sub(r"\s+", "-", s.strip())


def write_topic(path: Path, title: str, generated: str, heads: list[str]) -> None:
    text = path.read_text(encoding="utf-8") if path.exists() else (
        f"# {title}\n\n{TOC_START}\n{TOC_END}\n\n## Как работать\n\nПравила темы ещё не записаны.\n\n{GEN_START}\n{GEN_END}\n")
    manual = re.findall(r"^## (?!Команды )(.+)$", text.split(GEN_START)[0], flags=re.M)
    toc = [TOC_START, "Содержание:"] + [f"- [{h}](#{slug(h)})" for h in manual + heads] + [TOC_END]
    text = re.sub(re.escape(TOC_START) + r".*?" + re.escape(TOC_END), "\n".join(toc), text, flags=re.S)
    text = re.sub(re.escape(GEN_START) + r".*?" + re.escape(GEN_END), lambda _: generated, text, flags=re.S)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--check", action="store_true")
    a = p.parse_args()
    cli = C.find_cli()
    version = C.cli_version(cli)
    cmds = C.catalog(cli)
    by_topic = defaultdict(list)
    for c in cmds:
        by_topic[topic_of(c["id"])].append(c)
    topics_dir = C.SKILL_DIR / "references" / "topics"
    if a.check:
        listed = set()
        for f in topics_dir.glob("*.md"):
            listed.update(re.findall(r"^\| `([^`]+)` \|", f.read_text(encoding="utf-8"), flags=re.M))
        live = {c["id"] for c in cmds}
        res = {"cli": version, "references": C.refs_version(),
               "missingInReferences": sorted(live - listed), "goneFromCli": sorted(listed - live)}
        res["ok"] = res["cli"] == res["references"] and not res["missingInReferences"] and not res["goneFromCli"]
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return 0 if res["ok"] else 1
    topics_dir.mkdir(parents=True, exist_ok=True)
    for topic, title in TOPICS.items():
        generated, heads = render_generated(version, by_topic.get(topic, []))
        write_topic(topics_dir / f"{topic}.md", title, generated, heads)
    (C.SKILL_DIR / "references" / "VERSION").write_text(version + "\n", encoding="utf-8")
    print(json.dumps({"cli": version, "commands": len(cmds),
                      "topics": {t: len(by_topic.get(t, [])) for t in TOPICS}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
