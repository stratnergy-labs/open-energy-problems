from __future__ import annotations

import re
from pathlib import Path
from typing import Any

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if value in {"", "null", "None"}:
        return None
    if value == "[]":
        return []
    if value in {"true", "false"}:
        return value == "true"
    if value.isdigit():
        return int(value)
    return value.strip('"').strip("'")


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the small YAML subset used by repository front matter."""
    data: dict[str, Any] = {}
    current_list: str | None = None
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if raw_line.startswith("  - "):
            if current_list is None:
                raise ValueError(f"line {line_number}: list item without list key")
            data[current_list].append(_parse_scalar(raw_line[4:]))
            continue
        if raw_line.startswith("  []"):
            if current_list is None:
                raise ValueError(f"line {line_number}: empty list without list key")
            data[current_list] = []
            continue
        current_list = None
        if ":" not in raw_line:
            raise ValueError(f"line {line_number}: expected `key: value`")
        key, raw_value = raw_line.split(":", 1)
        key = key.strip()
        if raw_value.strip() == "":
            data[key] = []
            current_list = key
        else:
            data[key] = _parse_scalar(raw_value)
    return data


def parse_markdown(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"{path}: missing YAML front matter")
    try:
        data = parse_simple_yaml(match.group(1))
    except ValueError as exc:
        raise ValueError(f"{path}: invalid front matter: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path}: front matter must be a mapping")
    return data, text[match.end():]


def iter_markdown(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def require_fields(path: Path, data: dict[str, Any], required: list[str]) -> list[str]:
    errors: list[str] = []
    for field in required:
        if field not in data:
            errors.append(f"{path}: missing required field `{field}`")
    return errors


def scalar_for_csv(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return ";".join(str(item) for item in value)
    return str(value)
