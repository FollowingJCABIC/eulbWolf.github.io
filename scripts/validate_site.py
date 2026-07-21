#!/usr/bin/env python3
"""Validate the modern portfolio subset without touching preserved legacy pages."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = (
    ROOT / "index.html",
    ROOT / "contact.html",
    ROOT / "coding.html",
    ROOT / "404.html",
    ROOT / "projects" / "index.html",
    ROOT / "projects" / "learning-app-analytics.html",
    ROOT / "projects" / "mindstate-signal-lab.html",
    ROOT / "projects" / "tutoring-ops-analytics.html",
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[tuple[str, str | None, str | None]] = []
        self.images: list[tuple[str | None, str | None]] = []
        self.lang: str | None = None
        self.title_count = 0
        self.viewport_count = 0
        self.h1_count = 0
        self.main_count = 0
        self._in_title = False
        self._title_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.lang = values.get("lang")
        if values.get("id"):
            self.ids.append(values["id"] or "")
        if tag == "a":
            self.links.append((values.get("href") or "", values.get("target"), values.get("rel")))
        elif tag == "img":
            self.images.append((values.get("src"), values.get("alt")))
        elif tag == "meta" and values.get("name", "").lower() == "viewport":
            self.viewport_count += 1
        elif tag == "title":
            self.title_count += 1
            self._in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "main":
            self.main_count += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_text.append(data)

    @property
    def title_text(self) -> str:
        return "".join(self._title_text).strip()


def validate_page(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"{path.relative_to(ROOT)}: file is missing"]

    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    rel = path.relative_to(ROOT)

    if parser.lang != "en":
        errors.append(f'{rel}: <html lang="en"> is required')
    if parser.title_count != 1 or not parser.title_text:
        errors.append(f"{rel}: exactly one non-empty <title> is required")
    if parser.viewport_count != 1:
        errors.append(f"{rel}: exactly one viewport meta tag is required")
    if parser.h1_count != 1:
        errors.append(f"{rel}: exactly one <h1> is required; found {parser.h1_count}")
    if parser.main_count != 1:
        errors.append(f"{rel}: exactly one <main> landmark is required; found {parser.main_count}")

    duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
    if duplicates:
        errors.append(f"{rel}: duplicate ids: {', '.join(duplicates)}")

    for src, alt in parser.images:
        if src and alt is None:
            errors.append(f"{rel}: image {src!r} is missing alt text")

    for href, target, rel_attr in parser.links:
        if not href:
            errors.append(f"{rel}: empty link href")
            continue
        parsed = urlsplit(href)
        if target == "_blank" and "noopener" not in (rel_attr or "").split():
            errors.append(f"{rel}: target=_blank link {href!r} requires rel=noopener")
        if parsed.scheme or href.startswith(("mailto:", "tel:", "javascript:")):
            continue

        target_path = parsed.path
        if not target_path:
            continue
        resolved = (path.parent / target_path).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{rel}: internal link escapes site root: {href!r}")
            continue
        if not resolved.exists():
            errors.append(f"{rel}: missing internal target {href!r}")

    return errors


def main() -> int:
    errors: list[str] = []
    for page in PAGES:
        errors.extend(validate_page(page))

    required_assets = (ROOT / "portfolio.css", ROOT / "favicon.svg", ROOT / "robots.txt")
    for asset in required_assets:
        if not asset.exists() or asset.stat().st_size == 0:
            errors.append(f"{asset.relative_to(ROOT)}: required asset is missing or empty")

    if errors:
        print("Site validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(PAGES)} modern HTML pages and {len(required_assets)} required assets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
