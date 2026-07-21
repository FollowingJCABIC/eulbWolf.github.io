#!/usr/bin/env python3
"""Render the modern portfolio at representative widths and check basic usability."""

from __future__ import annotations

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import threading
import sys

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "browser-artifacts"
PAGES = (
    "index.html",
    "contact.html",
    "coding.html",
    "404.html",
    "projects/index.html",
    "projects/learning-app-analytics.html",
    "projects/mindstate-signal-lab.html",
    "projects/tutoring-ops-analytics.html",
)
SCREENSHOT_PAGES = {
    "index.html",
    "projects/learning-app-analytics.html",
    "projects/mindstate-signal-lab.html",
    "projects/tutoring-ops-analytics.html",
}
VIEWPORTS = (
    {"name": "mobile", "width": 390, "height": 844},
    {"name": "tablet", "width": 768, "height": 1024},
    {"name": "desktop", "width": 1440, "height": 900},
)


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:  # noqa: A002
        return


def main() -> int:
    ARTIFACT_DIR.mkdir(exist_ok=True)
    previous_cwd = Path.cwd()
    os.chdir(ROOT)
    server = ThreadingHTTPServer(("127.0.0.1", 0), QuietHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base_url = f"http://127.0.0.1:{server.server_port}"

    failures: list[str] = []
    results: list[dict[str, object]] = []

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            for viewport in VIEWPORTS:
                for route in PAGES:
                    page = browser.new_page(
                        viewport={"width": viewport["width"], "height": viewport["height"]},
                        reduced_motion="reduce",
                    )
                    browser_errors: list[str] = []
                    page.on("pageerror", lambda error: browser_errors.append(f"pageerror: {error}"))
                    page.on(
                        "console",
                        lambda message: browser_errors.append(f"console: {message.text}")
                        if message.type == "error"
                        else None,
                    )

                    response = page.goto(f"{base_url}/{route}", wait_until="load")
                    status = response.status if response else None
                    metrics = page.evaluate(
                        """
                        () => ({
                          scrollWidth: document.documentElement.scrollWidth,
                          clientWidth: document.documentElement.clientWidth,
                          h1Count: document.querySelectorAll('h1').length,
                          mainCount: document.querySelectorAll('main').length,
                          skipLinkCount: document.querySelectorAll('a.skip-link[href="#main-content"]').length,
                        })
                        """
                    )
                    page.keyboard.press("Tab")
                    first_focus = page.evaluate(
                        """
                        () => ({
                          tag: document.activeElement?.tagName || '',
                          className: document.activeElement?.className || '',
                          href: document.activeElement?.getAttribute('href') || '',
                        })
                        """
                    )

                    prefix = f"{route} @ {viewport['width']}x{viewport['height']}"
                    if status is None or status >= 400:
                        failures.append(f"{prefix}: HTTP status {status}")
                    if metrics["scrollWidth"] > metrics["clientWidth"] + 1:
                        failures.append(
                            f"{prefix}: page-level horizontal overflow "
                            f"({metrics['scrollWidth']} > {metrics['clientWidth']})"
                        )
                    if metrics["h1Count"] != 1:
                        failures.append(f"{prefix}: expected one h1, found {metrics['h1Count']}")
                    if metrics["mainCount"] != 1:
                        failures.append(f"{prefix}: expected one main landmark, found {metrics['mainCount']}")
                    if metrics["skipLinkCount"] != 1:
                        failures.append(f"{prefix}: expected one skip link, found {metrics['skipLinkCount']}")
                    if "skip-link" not in str(first_focus["className"]).split():
                        failures.append(f"{prefix}: first keyboard focus is not the skip link: {first_focus}")
                    for error in browser_errors:
                        failures.append(f"{prefix}: {error}")

                    if route in SCREENSHOT_PAGES:
                        slug = route.replace("/", "-").removesuffix(".html")
                        page.screenshot(
                            path=ARTIFACT_DIR / f"{slug}-{viewport['name']}.png",
                            full_page=False,
                        )

                    results.append(
                        {
                            "route": route,
                            "viewport": viewport,
                            "status": status,
                            "metrics": metrics,
                            "first_focus": first_focus,
                            "browser_errors": browser_errors,
                        }
                    )
                    page.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
        os.chdir(previous_cwd)

    summary = {
        "pages_checked": len(PAGES),
        "viewports_checked": len(VIEWPORTS),
        "render_combinations": len(results),
        "failures": failures,
        "results": results,
    }
    (ARTIFACT_DIR / "browser-check-summary.json").write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    if failures:
        print("Rendered portfolio validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        f"Rendered {len(PAGES)} pages across {len(VIEWPORTS)} viewports "
        f"({len(results)} combinations) without page overflow or landmark/focus failures."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
