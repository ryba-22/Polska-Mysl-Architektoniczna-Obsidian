#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
OUT = ROOT / "dist" / "peos"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)


def parse_scalar(value: str):
    value = value.strip()
    if not value:
        return ""
    if value in {"true", "false"}:
        return value == "true"
    if value.startswith("[") and value.endswith("]"):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            pass
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> dict:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data = {}
    for raw in match.group(1).splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = parse_scalar(value)
    return data


def first_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def wikilinks(text: str) -> list[str]:
    links = []
    for target in re.findall(r"\[\[([^\]]+)\]\]", text):
        links.append(target.split("|", 1)[0].strip())
    return sorted(set(links))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    entries = []
    for path in sorted(CONTENT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        if meta.get("publication_status") != "public":
            continue
        rel = path.relative_to(ROOT).as_posix()
        entries.append(
            {
                "id": meta.get("id"),
                "title": first_heading(text) or path.stem,
                "type": meta.get("type"),
                "lifecycle": meta.get("lifecycle"),
                "knowledge_status": meta.get("knowledge_status"),
                "peos_usable": bool(meta.get("peos_usable", False)),
                "tags": meta.get("tags", []),
                "source_ids": meta.get("source_ids", []),
                "path": rel,
                "wikilinks": wikilinks(text),
            }
        )

    registry = {
        "schema_version": "1.0.0",
        "source": "Polska-Mysl-Architektoniczna-Obsidian",
        "publication_boundary": "public-only",
        "entries": entries,
    }
    (OUT / "registry.json").write_text(
        json.dumps(registry, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    groups = {
        "concepts.json": {"concept", "comparison", "map", "glossary", "peos-model", "integration", "governance"},
        "heuristics.json": {"heuristic"},
        "archetypes.json": {"software-archetype"},
        "failure-patterns.json": {"failure-pattern"},
        "case-studies.json": {"case-study"},
        "ai-engineering.json": {"concept", "eval"},
    }
    for filename, types in groups.items():
        subset = [e for e in entries if e["type"] in types and e["peos_usable"]]
        if filename == "ai-engineering.json":
            subset = [e for e in subset if "ai" in e.get("tags", []) or e["type"] == "eval"]
        (OUT / filename).write_text(
            json.dumps({"schema_version": "1.0.0", "entries": subset}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print(f"Built PMA registry: {len(entries)} public notes")


if __name__ == "__main__":
    main()
