#!/usr/bin/env python3
"""Validate core documentation structure without external dependencies."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md", "README.md", "PROMPT_VIVO/AGENTS.md",
    "PROMPT_VIVO/README.md", "PROMPT_VIVO/CURRENT_WORK.md",
    "PROMPT_VIVO/ARCHITECTURE_GOVERNANCE.md", "PROMPT_VIVO/BOOTSTRAP.md",
    "operations/README.md", "operations/STATE.md", "PROMPT_VIVO/runs/README.md",
    "PROMPT_VIVO/runs/PV-2026-11-25-TOTALMENTE-GRATUITA/README.md",
    "PROMPT_VIVO/runs/PV-2026-11-25-TOTALMENTE-GRATUITA/RUN_STATE.md",
    "PROMPT_VIVO/runs/PV-2026-11-25-TOTALMENTE-GRATUITA/PHASE_CONTROL.md",
    "PROMPT_VIVO/runs/PV-2026-11-25-TOTALMENTE-GRATUITA/RESUME_PACKET.md",
    "mkdocs.yml", "portfolio_site/docs/index.md",
]

LINE_BUDGETS = {
    "AGENTS.md": 100,
    "PROMPT_VIVO/AGENTS.md": 100,
    "PROMPT_VIVO/BOOTSTRAP.md": 180,
    "PROMPT_VIVO/CURRENT_WORK.md": 100,
    "PROMPT_VIVO/ARCHITECTURE_GOVERNANCE.md": 260,
    "PROMPT_VIVO/runs/PV-2026-11-25-TOTALMENTE-GRATUITA/README.md": 100,
    "PROMPT_VIVO/runs/PV-2026-11-25-TOTALMENTE-GRATUITA/RESUME_PACKET.md": 120,
}

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    errors = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"required file missing: {relative}")

    for relative, maximum in LINE_BUDGETS.items():
        path = ROOT / relative
        if path.is_file():
            count = len(path.read_text(encoding="utf-8").splitlines())
            if count > maximum:
                errors.append(f"{relative}: {count} lines exceeds budget {maximum}")

    current = ROOT / "PROMPT_VIVO/CURRENT_WORK.md"
    state = ROOT / "operations/STATE.md"
    resume = ROOT / "PROMPT_VIVO/runs/PV-2026-11-25-TOTALMENTE-GRATUITA/RESUME_PACKET.md"
    if current.is_file() and "operations/COMPANY_SOLUTIONS/" not in current.read_text(encoding="utf-8"):
        errors.append("CURRENT_WORK must retain the Company Solutions line until superseded")
    if state.is_file() and "PROMPT_VIVO/CURRENT_WORK.md" not in state.read_text(encoding="utf-8"):
        errors.append("operations/STATE must point to CURRENT_WORK")
    if resume.is_file():
        content = resume.read_text(encoding="utf-8")
        for required in ("CURRENT_WORK.md", "RUN_STATE.md", "PHASE_CONTROL.md"):
            if required not in content:
                errors.append(f"RESUME_PACKET must point to {required}")

    link_files = [
        "README.md", "AGENTS.md", "PROMPT_VIVO/README.md",
        "PROMPT_VIVO/AGENTS.md", "PROMPT_VIVO/BOOTSTRAP.md",
        "PROMPT_VIVO/ARCHITECTURE_GOVERNANCE.md", "operations/README.md",
        "PROMPT_VIVO/runs/README.md",
        "PROMPT_VIVO/runs/PV-2026-11-25-TOTALMENTE-GRATUITA/README.md",
        "portfolio_site/docs/index.md",
    ]
    for relative in link_files:
        source = ROOT / relative
        if not source.is_file():
            continue
        for target in LINK_RE.findall(source.read_text(encoding="utf-8")):
            target = target.strip().split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            if not (source.parent / target).resolve().exists():
                errors.append(f"broken local link in {relative}: {target}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Documentation validation passed: {len(REQUIRED_FILES)} required files, "
          f"{len(LINE_BUDGETS)} line budgets, selected local links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
