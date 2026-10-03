#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"


def normalize(name: str) -> str:
    return name.strip().casefold()


def main() -> int:
    names = {}
    for path in CONTENT.rglob("*.md"):
        names.setdefault(normalize(path.stem), []).append(path)

    missing = []
    ambiguous = []
    for path in CONTENT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw in re.findall(r"\[\[([^\]]+)\]\]", text):
            target = raw.split("|", 1)[0].strip()
            leaf = Path(target).stem
            matches = names.get(normalize(leaf), [])
            if not matches:
                missing.append((path.relative_to(ROOT).as_posix(), target))
            elif len(matches) > 1:
                ambiguous.append((path.relative_to(ROOT).as_posix(), target))

    if missing:
        print("WIKILINK GATE: FAIL")
        for source, target in missing:
            print(f"- missing: {source} -> {target}")
        return 1

    print(f"WIKILINK GATE: PASS (ambiguous={len(ambiguous)})")
    for source, target in ambiguous[:20]:
        print(f"- ambiguous: {source} -> {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
