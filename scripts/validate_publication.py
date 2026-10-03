#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

FORBIDDEN_TRACKED_PREFIXES = ("private/", "assets-private/")
FORBIDDEN_PUBLIC_EXTENSIONS = {
    ".srt", ".vtt", ".epub", ".mobi", ".mp4", ".mkv", ".webm", ".mp3", ".wav", ".7z", ".rar"
}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)(api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*['\"][^'\"]{8,}"),
]


def tracked_files() -> list[str]:
    proc = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files"],
        check=True,
        text=True,
        capture_output=True,
    )
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def frontmatter_status(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    block = text[4:end]
    for line in block.splitlines():
        if line.startswith("publication_status:"):
            return line.split(":", 1)[1].strip().strip("'\"")
    return None


def main() -> int:
    errors = []
    tracked = tracked_files()

    for rel in tracked:
        if rel.startswith(FORBIDDEN_TRACKED_PREFIXES):
            errors.append(f"private path is tracked: {rel}")
        path = ROOT / rel
        if path.suffix.lower() in FORBIDDEN_PUBLIC_EXTENSIONS:
            errors.append(f"raw/source-like attachment is tracked publicly: {rel}")

    for path in sorted(CONTENT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        status = frontmatter_status(text)
        if status != "public":
            errors.append(f"content note is not explicit-public: {path.relative_to(ROOT)} ({status})")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"possible secret in public note: {path.relative_to(ROOT)}")

    for rel in tracked:
        path = ROOT / rel
        if path.is_file() and path.stat().st_size <= 2_000_000:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    errors.append(f"possible secret in tracked file: {rel}")

    if errors:
        print("PUBLICATION GATE: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PUBLICATION GATE: PASS ({len(tracked)} tracked files checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
