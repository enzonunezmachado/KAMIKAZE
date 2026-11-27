"""Fail the Pages build when the custom portfolio shell or layout contract regresses."""
from pathlib import Path
import re
import sys

ROOT = Path("portfolio_site/site")
INDEX = ROOT / "index.html"
ASSETS = {
    "base CSS": ROOT / "assets" / "kamikaze-base.css",
    "portfolio CSS": ROOT / "assets" / "portfolio.css",
    "progressive JS": ROOT / "assets" / "kamikaze.js",
}
REQUIRED_MARKERS = (
    'data-km-custom-shell',
    'class="km-header"',
    'class="km-nav"',
    'class="km-footer"',
    "Menos atrito.",
    "Conhecer soluções",
)
LEGACY_NAV_MARKERS = ("wy-nav-side", "wy-nav-top")
PUBLIC_PAGES = ("solucoes/index.html", "projetos/index.html", "processo/index.html")


def fail(message: str) -> None:
    print(f"PORTFOLIO VALIDATION FAILED: {message}", file=sys.stderr)
    raise SystemExit(1)


if not INDEX.is_file():
    fail("MkDocs did not generate portfolio_site/site/index.html")

for label, path in ASSETS.items():
    if not path.is_file():
        fail(f"{label} is missing from the generated site")

html = INDEX.read_text(encoding="utf-8")
css = ASSETS["portfolio CSS"].read_text(encoding="utf-8")
base_css = ASSETS["base CSS"].read_text(encoding="utf-8")
js = ASSETS["progressive JS"].read_text(encoding="utf-8")
flat_css = re.sub(r"\s+", " ", css)

for marker in REQUIRED_MARKERS:
    if marker not in html:
        fail(f"custom layout marker missing from index.html: {marker}")

for marker in LEGACY_NAV_MARKERS:
    if marker not in css or "display: none !important" not in css:
        fail(f"legacy ReadTheDocs navigation is not explicitly hidden: {marker}")

# Full-width shell; only the inner header/content/footer containers share the max-width.
layout_contract = (
    ".km-header { width: 100%;",
    ".km-footer { width: 100%;",
    ".km-main { width: 100%; max-width: none; margin: 0; padding: 0; }",
    ".km-header-inner { max-width: var(--km-width);",
    ".rst-content { max-width: var(--km-width); margin: 0 auto; padding:",
    ".km-footer-inner { max-width: var(--km-width);",
)
for rule in layout_contract:
    if rule not in flat_css:
        fail(f"full-width/alignment contract missing: {rule}")

if "@media (max-width: 620px)" not in css:
    fail("mobile layout breakpoint is missing")
if "prefers-reduced-motion" not in base_css or "prefers-reduced-motion" not in css:
    fail("reduced-motion support is missing")
if "data-menu-toggle" not in js or "data-menu" not in js:
    fail("progressive navigation behavior is missing")

for page in PUBLIC_PAGES:
    page_path = ROOT / page
    if not page_path.is_file():
        fail(f"expected public page missing: {page}")
    page_html = page_path.read_text(encoding="utf-8")
    for marker in ('data-km-custom-shell', 'class="km-header"', 'class="km-footer"'):
        if marker not in page_html:
            fail(f"custom site shell missing from {page}: {marker}")

print("Portfolio validation passed: assets, custom shell, full-width layout contract, responsive/reduced-motion rules and public pages.")
