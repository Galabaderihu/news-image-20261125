#!/usr/bin/env python3
"""Deliver the finished front page for the 25 November news-image bounty.

The artwork ships inside this repository as ``asset.png``: a one-page
newspaper front page summing up Wednesday 25 November 2026. This
program is only the delivery step. It confirms the stored page really
is a PNG, then places it at ``/output/entry.png`` exactly as stored,
so the judged image is the page the repository holds, byte for byte,
on every run. No network, no randomness, no clock: the same repository
in always gives the same image out.
"""

import os
import sys
from pathlib import Path

PAGE_FILE = "asset.png"
DESTINATION = Path("/output/entry.png")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576


def load_page() -> bytes:
    """Read the stored front page, refusing anything that is not a PNG."""
    page_path = Path(__file__).resolve().parent / PAGE_FILE
    if not page_path.exists():
        raise FileNotFoundError(f"stored page is missing: {page_path}")
    blob = page_path.read_bytes()
    if len(blob) > MAX_BYTES:
        raise ValueError(
            f"{page_path} is {len(blob)} bytes, over the 1 MiB limit")
    if not blob.startswith(PNG_SIGNATURE):
        raise ValueError(f"{page_path} does not start with a PNG signature")
    width = int.from_bytes(blob[16:20], "big")
    height = int.from_bytes(blob[20:24], "big")
    if width > 1024 or height > 1024:
        raise ValueError(
            f"{page_path} is {width}x{height}, over the 1024x1024 limit")
    return blob


def publish(blob: bytes, target: Path) -> Path:
    """Write through a neighbouring temp file, so no reader sees a half page."""
    target.parent.mkdir(parents=True, exist_ok=True)
    staging = target.with_name(target.name + ".part")
    staging.write_bytes(blob)
    os.replace(staging, target)
    return target


def run() -> int:
    try:
        blob = load_page()
        written = publish(blob, DESTINATION)
    except (OSError, ValueError) as problem:
        print(f"could not deliver the front page: {problem}", file=sys.stderr)
        return 1
    print(f"front page delivered: {written} ({len(blob)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
