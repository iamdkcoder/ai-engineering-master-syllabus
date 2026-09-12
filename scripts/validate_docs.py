#!/usr/bin/env python3
"""Lightweight sanity checks for the docs/ tree before building the site.

Checks: duplicate filenames, missing section index files, broken local
Markdown links, missing H1 headings, and unexpectedly empty Markdown files.
"""

import re
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
LINK_RE = re.compile(r"\]\(([^)]+)\)")


def find_markdown_files():
    return sorted(DOCS_DIR.rglob("*.md"))


def check_duplicate_filenames(files):
    """Flag filenames repeated within the same directory (e.g. two READMEs)."""
    seen = {}
    errors = []
    for f in files:
        seen.setdefault((f.parent, f.name), []).append(f)
    for (parent, name), paths in seen.items():
        if len(paths) > 1:
            errors.append(f"Duplicate filename '{name}' in {parent}: {[str(p) for p in paths]}")
    return errors


def check_missing_indexes():
    errors = []
    for d in sorted(p for p in DOCS_DIR.iterdir() if p.is_dir()):
        if not (d / "index.md").exists():
            errors.append(f"Missing index.md in section folder: {d}")
    return errors


def check_missing_h1(files):
    errors = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        if not re.search(r"^#\s+\S", text, re.MULTILINE):
            errors.append(f"Missing H1 heading: {f}")
    return errors


def check_empty_files(files):
    errors = []
    for f in files:
        if len(f.read_text(encoding="utf-8").strip()) == 0:
            errors.append(f"Empty Markdown file: {f}")
    return errors


def check_broken_links(files):
    errors = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.split("#")[0].strip()
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            if not target.endswith(".md"):
                continue
            resolved = (f.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"Broken link in {f}: {target}")
    return errors


def main():
    files = find_markdown_files()
    all_errors = []
    all_errors += check_duplicate_filenames(files)
    all_errors += check_missing_indexes()
    all_errors += check_missing_h1(files)
    all_errors += check_empty_files(files)
    all_errors += check_broken_links(files)

    if all_errors:
        print(f"Found {len(all_errors)} issue(s):\n")
        for e in all_errors:
            print(f" - {e}")
        sys.exit(1)

    print(f"OK: {len(files)} Markdown files validated, no issues found.")
    sys.exit(0)


if __name__ == "__main__":
    main()
