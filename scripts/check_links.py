#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
URL_RE = re.compile(r"https?://[^\s)\]]+")


def main() -> int:
    urls: set[str] = set()
    for directory in ("problems", "contributions", "templates", "index"):
        for path in (ROOT / directory).rglob("*.md"):
            urls.update(URL_RE.findall(path.read_text(encoding="utf-8")))
    if not urls:
        print("No external links found.")
        return 0
    failures = []
    for url in sorted(urls):
        try:
            request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "open-energy-problems-link-check"})
            with urllib.request.urlopen(request, timeout=15) as response:
                if response.status >= 400:
                    failures.append(f"{url}: HTTP {response.status}")
        except Exception as exc:  # noqa: BLE001 - CLI should report all link failures clearly.
            failures.append(f"{url}: {exc}")
    if failures:
        print("Link check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Checked {len(urls)} links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
