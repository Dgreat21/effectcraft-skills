"""Общие функции скилла effectcraft: поиск установленного CLI, MCP-клиент, состояние проверок.

Только стандартная библиотека. Ничего не устанавливает и не скачивает.
"""
from __future__ import annotations

import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REFS_VERSION_FILE = SKILL_DIR / "references" / "VERSION"


class CliNotFound(RuntimeError):
    pass


def _version_key(path: str) -> tuple:
    m = re.search(r"effectcraft-cli-(\d+)\.(\d+)\.(\d+)", path)
    return tuple(int(x) for x in m.groups()) if m else (0, 0, 0)


def find_cli() -> str:
    """Путь к установленному effectcraft-cli. Порядок: $EFFECTCRAFT_CLI, ArtCraft CLI, PATH."""
    env = os.environ.get("EFFECTCRAFT_CLI")
    if env:
        if os.access(env, os.X_OK):
            return env
        raise CliNotFound(f"EFFECTCRAFT_CLI={env} не исполняемый файл")
    home = Path.home() / ".local/share/artcraft-cli"
    candidates = sorted(glob.glob(str(home / "effectcraft/effectcraft-cli-*/effectcraft-cli")), key=_version_key)
    if candidates:
        return candidates[-1]
    link = home / "bin/effectcraft-cli"
    if os.access(link, os.X_OK):
        return str(link)
    on_path = shutil.which("effectcraft-cli")
    if on_path:
        return on_path
    raise CliNotFound(
        "effectcraft-cli не найден. Скилл ничего не ставит: установи CLI сам "
        "(ArtCraft Launcher или релиз github.com/storytold/effectcraft) "
        "либо укажи путь в EFFECTCRAFT_CLI."
    )


def cli_version(cli: str) -> str:
    out = subprocess.run([cli, "--version"], capture_output=True, text=True, timeout=60).stdout.strip()
    return out.split()[-1] if out else "unknown"


def refs_version() -> str:
    try:
        return REFS_VERSION_FILE.read_text(encoding="utf-8").strip()
    except OSError:
        return "unknown"


class Mcp:
    """Минимальный клиент MCP (JSON-RPC по stdio) к `effectcraft-cli mcp`."""

    def __init__(self, cli: str):
        self.proc = subprocess.Popen([cli, "mcp"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     stderr=subprocess.DEVNULL, text=True, encoding="utf-8")
        self._id = 0
        self._request("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                                     "clientInfo": {"name": "effectcraft-skill", "version": "1"}})
        self._send({"jsonrpc": "2.0", "method": "notifications/initialized"})

    def _send(self, msg: dict) -> None:
        self.proc.stdin.write(json.dumps(msg) + "\n")
        self.proc.stdin.flush()

    def _request(self, method: str, params: dict) -> dict:
        self._id += 1
        self._send({"jsonrpc": "2.0", "id": self._id, "method": method, "params": params})
        while True:
            line = self.proc.stdout.readline()
            if not line:
                raise RuntimeError(f"MCP закрылся на {method}")
            msg = json.loads(line)
            if msg.get("id") == self._id:
                if "error" in msg:
                    raise RuntimeError(f"MCP {method}: {msg['error']}")
                return msg["result"]

    def tool(self, name: str, arguments: dict):
        res = self._request("tools/call", {"name": name, "arguments": arguments})
        text = "".join(c.get("text", "") for c in res.get("content", []) if c.get("type") == "text")
        if res.get("isError"):
            raise RuntimeError(text)
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return text

    def close(self) -> None:
        try:
            self.proc.stdin.close()
            self.proc.terminate()
            self.proc.wait(timeout=5)
        except Exception:
            self.proc.kill()
        finally:
            self.proc.stdout.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()


def catalog(cli: str, text_filter: str | None = None) -> list[dict]:
    """Живой каталог команд со схемами параметров."""
    args = {"schemas": True}
    if text_filter:
        args["filter"] = text_filter
    with Mcp(cli) as mcp:
        data = mcp.tool("command_list", args)
    return data if isinstance(data, list) else data.get("commands", [])


# ---- состояние проверок (общее для ec.py verify и хука gate.py) ----

def state_dir() -> Path:
    base = os.environ.get("XDG_STATE_HOME") or str(Path.home() / ".local/state")
    d = Path(base) / "effectcraft-skill"
    (d / "receipts").mkdir(parents=True, exist_ok=True)
    (d / "sessions").mkdir(parents=True, exist_ok=True)
    return d


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def receipt_path(digest: str) -> Path:
    return state_dir() / "receipts" / f"{digest}.json"
