#!/usr/bin/env python3
"""Validate core documentation structure, size budgets and synchronized state."""

from pathlib import Path
import re
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
RUN = "PROMPT_VIVO/runs/PV-2026-11-25-TOTALMENTE-GRATUITA"

REQUIRED_FILES = [
    "AGENTS.md", "README.md", "PROMPT_VIVO/AGENTS.md",
    "PROMPT_VIVO/README.md", "PROMPT_VIVO/CURRENT_WORK.md",
    "PROMPT_VIVO/ARCHITECTURE_GOVERNANCE.md", "PROMPT_VIVO/BOOTSTRAP.md",
    "operations/README.md", "operations/state.toml", "operations/STATE.md",
    "operations/STATE_HISTORY.md", "operations/COMPANY_SOLUTIONS/README.md",
    "PROMPT_VIVO/runs/README.md", f"{RUN}/README.md",
    f"{RUN}/RUN_STATE.md", f"{RUN}/RUN_HISTORY.md",
    f"{RUN}/PHASE_CONTROL.md", f"{RUN}/RESUME_PACKET.md",
    "PROMPT_VIVO/knowledge/README.md", "mkdocs.yml",
    "requirements-docs.txt", "portfolio_site/README.md",
    "portfolio_site/docs/index.md", "scripts/validate_docs.py",
    ".github/workflows/docs-quality.yml",
]

LINE_BUDGETS = {
    "AGENTS.md": 100,
    "PROMPT_VIVO/AGENTS.md": 100,
    "PROMPT_VIVO/BOOTSTRAP.md": 180,
    "PROMPT_VIVO/CURRENT_WORK.md": 100,
    "PROMPT_VIVO/ARCHITECTURE_GOVERNANCE.md": 260,
    "operations/STATE.md": 100,
    f"{RUN}/README.md": 100,
    f"{RUN}/RUN_STATE.md": 100,
    f"{RUN}/RESUME_PACKET.md": 120,
}

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
NAV_FILES = [
    "README.md", "AGENTS.md", "PROMPT_VIVO/README.md",
    "PROMPT_VIVO/AGENTS.md", "PROMPT_VIVO/BOOTSTRAP.md",
    "PROMPT_VIVO/ARCHITECTURE_GOVERNANCE.md", "operations/README.md",
    "operations/STATE.md", "PROMPT_VIVO/runs/README.md",
    f"{RUN}/README.md", f"{RUN}/RUN_STATE.md",
    f"{RUN}/RESUME_PACKET.md", "portfolio_site/README.md",
    "portfolio_site/docs/index.md",
]


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

    state_path = ROOT / "operations/state.toml"
    state = None
    if state_path.is_file():
        try:
            with state_path.open("rb") as stream:
                state = tomllib.load(stream)
        except (tomllib.TOMLDecodeError, OSError) as exc:
            errors.append(f"operations/state.toml is invalid: {exc}")

    if state:
        project = state.get("project", {})
        execution = state.get("execution", {})
        phases = state.get("phases", {})
        active_run = project.get("active_run", "")
        active_phase = execution.get("active_phase", "")
        active_gate = execution.get("active_gate", "")
        last_work = project.get("last_substantive_work", "")

        checks = {
            "operations/STATE.md": [active_run, active_phase],
            f"{RUN}/RUN_STATE.md": [active_run, active_phase, active_gate],
            f"{RUN}/PHASE_CONTROL.md": [active_phase, active_gate],
            f"{RUN}/RESUME_PACKET.md": [active_run, active_phase],
            "PROMPT_VIVO/CURRENT_WORK.md": [last_work],
        }
        for relative, needles in checks.items():
            path = ROOT / relative
            if path.is_file():
                content = path.read_text(encoding="utf-8")
                for needle in needles:
                    if needle and needle not in content:
                        errors.append(f"{relative} is out of sync with operations/state.toml: missing {needle}")

        for key, expected in phases.items():
            if expected not in (ROOT / f"{RUN}/RUN_STATE.md").read_text(encoding="utf-8"):
                errors.append(f"RUN_STATE.md is out of sync with state.toml phase {key}: {expected}")

    for relative in NAV_FILES:
        source = ROOT / relative
        if not source.is_file():
            continue
        for target in LINK_RE.findall(source.read_text(encoding="utf-8")):
            target = target.strip().split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            resolved = (source.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"broken local link in {relative}: {target}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        f"Documentation validation passed: {len(REQUIRED_FILES)} required files, "
        f"{len(LINE_BUDGETS)} line budgets, TOML/Markdown state synchronization, "
        f"{len(NAV_FILES)} navigation files."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
