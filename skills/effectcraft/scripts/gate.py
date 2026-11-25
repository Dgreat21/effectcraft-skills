#!/usr/bin/env python3
"""Хук скилла effectcraft: не дать закончить работу с непроверенным проектом.

  gate.py record   PostToolUse: запомнить .ecproj, который сохранила команда (Bash или MCP save_project)
  gate.py stop     Stop: если у сохранённого в этой сессии проекта нет квитанции ec.py verify
                   для его текущего содержимого — вернуть decision=block с подсказкой
  gate.py readonly PreToolUse субагента-проверяющего: запретить команды, которые сохраняют проект

Квитанция пишется и при провале проверки: хук требует, чтобы проверка была, а не чтобы она прошла.
Провал агент обязан назвать в отчёте. Только стандартная библиотека; любая ошибка — тихий выход 0.
"""
from __future__ import annotations

import json
import re
import shlex
import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _common as C  # noqa: E402

CLI_HINT = re.compile(r"effectcraft-cli|ec\.py")


def saved_paths_from_bash(command: str, cwd: Path) -> list[Path]:
    if not CLI_HINT.search(command) or "--save" not in command:
        return []
    found = []
    for part in re.split(r"&&|\|\||;|\n", command):
        try:
            tokens = shlex.split(part)
        except ValueError:
            continue
        if tokens[:1] == ["cd"] and len(tokens) > 1:
            cwd = (cwd / tokens[1]).resolve()
            continue
        if not any(CLI_HINT.search(t) for t in tokens):
            continue
        for i, tok in enumerate(tokens):
            if tok == "--save-as" and i + 1 < len(tokens):
                found.append(tokens[i + 1])
            elif tok.startswith("--save-as="):
                found.append(tok.split("=", 1)[1])
            elif tok == "--save" and "--project" in tokens:
                j = tokens.index("--project")
                if j + 1 < len(tokens):
                    found.append(tokens[j + 1])
        found = [f for f in found if f.endswith(".ecproj")]
        result = [(cwd / f).resolve() if not Path(f).is_absolute() else Path(f) for f in found]
        if result:
            return result
    return []


def saved_paths_from_mcp(tool_input: dict, tool_response) -> list[Path]:
    path = tool_input.get("path")
    if not path:
        m = re.search(r"[^\s\"']+\.ecproj", json.dumps(tool_response, ensure_ascii=False))
        path = m.group(0) if m else None
    return [Path(path).expanduser()] if path and str(path).endswith(".ecproj") else []


def session_file(session_id: str) -> Path:
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", session_id or "unknown")
    return C.state_dir() / "sessions" / f"{safe}.json"


def record(event: dict) -> None:
    name = event.get("tool_name", "")
    tool_input = event.get("tool_input") or {}
    cwd = Path(event.get("cwd") or ".")
    if name == "Bash":
        paths = saved_paths_from_bash(tool_input.get("command", ""), cwd)
    elif name.endswith("__save_project"):
        paths = saved_paths_from_mcp(tool_input, event.get("tool_response"))
    else:
        return
    if not paths:
        return
    f = session_file(event.get("session_id", ""))
    known = json.loads(f.read_text(encoding="utf-8")) if f.exists() else []
    for p in paths:
        if str(p) not in known:
            known.append(str(p))
    f.write_text(json.dumps(known, ensure_ascii=False), encoding="utf-8")


def stop(event: dict) -> None:
    f = session_file(event.get("session_id", ""))
    if not f.exists():
        return
    unverified = []
    for p in json.loads(f.read_text(encoding="utf-8")):
        path = Path(p)
        if path.exists() and not C.receipt_path(C.sha256(path)).exists():
            unverified.append(str(path))
    if not unverified:
        return
    verify = Path(__file__).resolve().with_name("ec.py")
    lines = "\n".join(f"  python3 {verify} verify {shlex.quote(p)}" for p in unverified)
    print(json.dumps({
        "decision": "block",
        "reason": ("EC-07: проекты сохранены, но последняя версия не проверена. Запусти проверку "
                   "(добавь --alpha для прозрачного фона, --sequence для секвенции), посмотри кадры "
                   "и назови провалы в отчёте:\n" + lines),
    }, ensure_ascii=False))


WRITES = re.compile(r"--save(-as)?\b|\bec\.py\s+run\b|\bsave_project\b")


def readonly(event: dict) -> None:
    """PreToolUse для субагента-проверяющего: запретить сохранение проектов."""
    command = (event.get("tool_input") or {}).get("command", "")
    if CLI_HINT.search(command) and WRITES.search(command):
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": "Проверяющий только читает: сохранять и запускать планы нельзя. "
                                        "Рендер — в свою папку через ec.py verify --out.",
        }}, ensure_ascii=False))


def main() -> int:
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        event = json.load(sys.stdin)
        if mode == "record":
            record(event)
        elif mode == "stop":
            stop(event)
        elif mode == "readonly":
            readonly(event)
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
