"""Fail the Pages build if the custom portfolio layout or its dark theme regresses."""
from pathlib import Path
import sys

ROOT = Path("portfolio_site/site")
INDEX = ROOT / "index.html"
CSS = ROOT / "assets" / "portfolio.css"
REQUIRED_MARKERS = (
    'data-km-custom-shell',
    'class="km-header"',
    'class="km-nav"',
    'class="km-footer"',
    "Menos atrito.",
    "Conhecer soluções",
)
FORBIDDEN_MARKERS = (
    "wy-nav-side",
    "wy-nav-top",
)

def fail(message: str) -> None:
    print(f"PORTFOLIO VALIDATION FAILED: {message}", file=sys.stderr)
    raise SystemExit(1)

if not INDEX.is_file():
    fail("MkDocs did not generate portfolio_site/site/index.html")
if not CSS.is_file():
    fail("portfolio.css is missing from the generated site")

html = INDEX.read_text(encoding="utf-8")
css = CSS.read_text(encoding="utf-8")

for marker in REQUIRED_MARKERS:
    if marker not in html:
        fail(f"custom layout marker missing from index.html: {marker}")

# The old ReadTheDocs sidebar must not be visible in the shipped stylesheet.
if ".wy-nav-side, .wy-nav-top" not in css or "display: none !important" not in css:
    fail("legacy ReadTheDocs navigation is not explicitly hidden")

for page in ("solucoes/index.html", "projetos/index.html", "processo/index.html"):
    if not (ROOT / page).is_file():
        fail(f"expected public page missing: {page}")
    page_html = (ROOT / page).read_text(encoding="utf-8")
    if 'data-km-custom-shell' not in page_html or 'class="km-header"' not in page_html:
        fail(f"custom site shell missing from {page}")

print("Portfolio validation passed: custom shell, navigation, footer, dark theme and all public pages are present.")
