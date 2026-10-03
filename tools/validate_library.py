from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "ai-ea-library"
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
PROHIBITED = {
    "registered AIEA mark": re.compile(r"\bAIEA®"),
    "unsupported official label": re.compile(r"\bofficial AIEA\b", re.IGNORECASE),
    "internal group acronym": re.compile(r"\bSIG\b"),
    "personal GitHub handle": re.compile(r"(?<![\w.])@[A-Za-z][A-Za-z0-9_-]+"),
    "unqualified source-list footer": re.compile(r"^\*Sources?:", re.MULTILINE),
}


def markdown_files() -> list[Path]:
    files = list(DOCS.rglob("*.md"))
    files.extend(path for path in (ROOT / "README.md", ROOT / "LEGAL-NOTICE.md") if path.exists())
    return sorted(files)


def validate_links(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for match in MARKDOWN_LINK.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue

        target = unquote(target.split("#", 1)[0].strip())
        if not target:
            continue

        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing link target {match.group(1)}")
    return errors


def main() -> int:
    errors: list[str] = []
    files = markdown_files()

    for path in files:
        text = path.read_text(encoding="utf-8")
        errors.extend(validate_links(path, text))

        for label, pattern in PROHIBITED.items():
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)}: contains {label}")

    if errors:
        print("Reference library validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(files)} Markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
