"""Чтение PNG без сторонних библиотек: размер, число цветов, альфа.

Поддержано 8 бит, RGB и RGBA, без чересстрочности (так пишет effectcraft-cli).
Остальные варианты проверяются только по структуре.
"""
from __future__ import annotations

import struct
import zlib
from pathlib import Path

SIGNATURE = b"\x89PNG\r\n\x1a\n"


def _paeth(a: int, b: int, c: int) -> int:
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    return b if pb <= pc else c


def inspect(path: Path, sample_step: int = 4) -> dict:
    data = Path(path).read_bytes()
    if not data.startswith(SIGNATURE):
        return {"ok": False, "error": "не PNG"}
    pos, ihdr, idat = 8, None, bytearray()
    while pos < len(data):
        length, kind = struct.unpack(">I4s", data[pos:pos + 8])
        body = data[pos + 8:pos + 8 + length]
        if kind == b"IHDR":
            ihdr = struct.unpack(">IIBBBBB", body)
        elif kind == b"IDAT":
            idat += body
        elif kind == b"IEND":
            break
        pos += 12 + length
    if not ihdr:
        return {"ok": False, "error": "нет IHDR"}
    width, height, depth, color, _, _, interlace = ihdr
    info = {"ok": True, "width": width, "height": height, "depth": depth, "colorType": color}
    if depth != 8 or color not in (2, 6) or interlace:
        info["pixels"] = "не разбирались"
        return info
    bpp = 4 if color == 6 else 3
    try:
        raw = zlib.decompress(bytes(idat))
    except zlib.error as e:
        return {"ok": False, "error": f"повреждённые данные: {e}"}
    stride = width * bpp
    prev = bytearray(stride)
    colors, alpha_min, alpha_max = set(), 255, 0
    i = 0
    for y in range(height):
        ftype = raw[i]
        line = bytearray(raw[i + 1:i + 1 + stride])
        i += 1 + stride
        if ftype == 1:
            for x in range(bpp, stride):
                line[x] = (line[x] + line[x - bpp]) & 255
        elif ftype == 2:
            for x in range(stride):
                line[x] = (line[x] + prev[x]) & 255
        elif ftype == 3:
            for x in range(stride):
                left = line[x - bpp] if x >= bpp else 0
                line[x] = (line[x] + ((left + prev[x]) >> 1)) & 255
        elif ftype == 4:
            for x in range(stride):
                left = line[x - bpp] if x >= bpp else 0
                up_left = prev[x - bpp] if x >= bpp else 0
                line[x] = (line[x] + _paeth(left, prev[x], up_left)) & 255
        if y % sample_step == 0:
            for x in range(0, stride, bpp * sample_step):
                px = bytes(line[x:x + bpp])
                if len(colors) < 4096:
                    colors.add(px[:3])
                if bpp == 4:
                    alpha_min = min(alpha_min, px[3])
                    alpha_max = max(alpha_max, px[3])
        prev = line
    info["colors"] = len(colors)
    info["blank"] = len(colors) <= 1 and (bpp == 3 or alpha_max == alpha_min)
    if bpp == 4:
        info["alpha"] = [alpha_min, alpha_max]
    info["digest"] = zlib.crc32(raw) & 0xFFFFFFFF
    return info
