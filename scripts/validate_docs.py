#!/usr/bin/env python3
"""Validate core documentation, the active run and synchronized project state."""

from pathlib import Path
import re
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
RUN_ID_RE = re.compile(r"PV-\d{4}-\d{2}-\d{2}-[A-Z0-9-]+")

BASE_REQUIRED_FILES = [
    "AGENTS.md", "README.md",
    "PROMPT_VIVO/AGENTS.md", "PROMPT_VIVO/README.md",
    "PROMPT_VIVO/CURRENT_WORK.md", "PROMPT_VIVO/ARCHITECTURE_GOVERNANCE.md",
    "PROMPT_VIVO/BOOTSTRAP.md", "PROMPT_VIVO/QUALITY_GATE.md",
    "operations/README.md", "operations/state.toml", "operations/STATE.md",
    "operations/STATE_HISTORY.md", "operations/COMPANY_SOLUTIONS/README.md",
    "operations/FIRST_SALE/README.md", "operations/FIRST_SALE/OFFER_V1.md",
    "operations/FIRST_SALE/PROSPECT_CANDIDATES_001.md",
    "PROMPT_VIVO/runs/README.md",
    "PROMPT_VIVO/knowledge/README.md", "PROMPT_VIVO/PHASES/README.md",
    "PROMPT_VIVO/templates/README.md", "scripts/README.md",
    ".github/README.md", ".github/workflows/README.md",
    ".github/workflows/docs-quality.yml", "scripts/validate_docs.py",
    "scripts/validate_portfolio_build.py",
    "mkdocs.yml", "requirements-docs.txt",
    "portfolio_site/README.md", "portfolio_site/docs/README.md",
    "portfolio_site/docs/index.md", "portfolio_site/docs/solucoes.md",
    "portfolio_site/docs/projetos.md", "portfolio_site/docs/processo.md",
    "web/README.md", "web/AI_WEB_DEVELOPMENT_GUIDE.md",
    "web/AI_PROMPT_SCRIPTS.md", "web/templates/starter.html",
]

BASE_LINE_BUDGETS = {
    "AGENTS.md": 100,
    "PROMPT_VIVO/AGENTS.md": 100,
    "PROMPT_VIVO/BOOTSTRAP.md": 180,
    "PROMPT_VIVO/CURRENT_WORK.md": 100,
    "PROMPT_VIVO/ARCHITECTURE_GOVERNANCE.md": 260,
    "PROMPT_VIVO/QUALITY_GATE.md": 180,
    "operations/STATE.md": 100,
    "PROMPT_VIVO/runs/README.md": 100,
}

BASE_NAV_FILES = [
    "README.md", "AGENTS.md", "PROMPT_VIVO/README.md",
    "PROMPT_VIVO/AGENTS.md", "PROMPT_VIVO/BOOTSTRAP.md",
    "PROMPT_VIVO/ARCHITECTURE_GOVERNANCE.md", "operations/README.md",
    "operations/STATE.md", "operations/FIRST_SALE/README.md",
    "operations/FIRST_SALE/OFFER_V1.md",
    "operations/COMPANY_SOLUTIONS/README.md",
    "operations/COMPANY_SOLUTIONS/CONTROL_TOWER.md",
    "PROMPT_VIVO/runs/README.md", "PROMPT_VIVO/PHASES/README.md",
    "PROMPT_VIVO/templates/README.md", "scripts/README.md",
    ".github/README.md", ".github/workflows/README.md",
    "portfolio_site/README.md", "portfolio_site/docs/README.md",
    "portfolio_site/docs/index.md", "web/README.md",
    "web/AI_PROMPT_SCRIPTS.md",
]


def load_state(errors):
    state_path = ROOT / "operations/state.toml"
    if not state_path.is_file():
        errors.append("required file missing: operations/state.toml")
        return None
    try:
        with state_path.open("rb") as stream:
            return tomllib.load(stream)
    except (tomllib.TOMLDecodeError, OSError) as exc:
        errors.append(f"operations/state.toml is invalid: {exc}")
        return None


def main() -> int:
    errors = []
    state = load_state(errors)
    project = state.get("project", {}) if state else {}
    execution = state.get("execution", {}) if state else {}
    phases = state.get("phases", {}) if state else {}

    active_run = project.get("active_run", "")
    if not active_run or not RUN_ID_RE.fullmatch(active_run):
        errors.append(f"invalid or missing project.active_run in state.toml: {active_run!r}")
        run_path = None
    else:
        run_path = f"PROMPT_VIVO/runs/{active_run}"

    required_files = list(BASE_REQUIRED_FILES)
    line_budgets = dict(BASE_LINE_BUDGETS)
    nav_files = list(BASE_NAV_FILES)

    if run_path:
        required_files.extend([
            f"{run_path}/README.md", f"{run_path}/RUN_STATE.md",
            f"{run_path}/RUN_HISTORY.md", f"{run_path}/PHASE_CONTROL.md",
            f"{run_path}/RESUME_PACKET.md",
        ])
        line_budgets.update({
            f"{run_path}/README.md": 100,
            f"{run_path}/RUN_STATE.md": 100,
            f"{run_path}/RESUME_PACKET.md": 120,
        })
        nav_files.extend([
            f"{run_path}/README.md", f"{run_path}/RUN_STATE.md",
            f"{run_path}/RESUME_PACKET.md",
        ])

    for relative in required_files:
        if not (ROOT / relative).is_file():
            errors.append(f"required file missing: {relative}")

    for relative, maximum in line_budgets.items():
        path = ROOT / relative
        if path.is_file():
            count = len(path.read_text(encoding="utf-8").splitlines())
            if count > maximum:
                errors.append(f"{relative}: {count} lines exceeds budget {maximum}")

    if state and run_path:
        active_phase = execution.get("active_phase", "")
        active_gate = execution.get("active_gate", "")
        last_work = project.get("last_substantive_work", "")

        checks = {
            "operations/STATE.md": [active_run, active_phase],
            f"{run_path}/RUN_STATE.md": [active_run, active_phase, active_gate],
            f"{run_path}/PHASE_CONTROL.md": [active_phase, active_gate],
            f"{run_path}/RESUME_PACKET.md": [active_run, active_phase],
            "PROMPT_VIVO/CURRENT_WORK.md": [last_work],
        }
        for relative, needles in checks.items():
            path = ROOT / relative
            if path.is_file():
                content = path.read_text(encoding="utf-8")
                for needle in needles:
                    if needle and needle not in content:
                        errors.append(
                            f"{relative} is out of sync with operations/state.toml: missing {needle}"
                        )

        run_state_path = ROOT / f"{run_path}/RUN_STATE.md"
        if run_state_path.is_file():
            run_state = run_state_path.read_text(encoding="utf-8")
            for key, expected in phases.items():
                if expected not in run_state:
                    errors.append(
                        f"RUN_STATE.md is out of sync with state.toml phase {key}: {expected}"
                    )

    for relative in nav_files:
        source = ROOT / relative
        if not source.is_file():
            continue
        content = re.sub(r"\`\`\`[\s\S]*?\`\`\`", "", source.read_text(encoding="utf-8"))
        for match in LINK_RE.findall(content):
            target = match.strip().split(maxsplit=1)[0].strip("<>")
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:")):
                continue
            resolved = (ROOT / target.lstrip("/")).resolve() if target.startswith("/") else (source.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"broken local link in {relative}: {target}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        f"Documentation validation passed: {len(required_files)} required files, "
        f"{len(line_budgets)} line budgets, active run {active_run}, "
        f"TOML/Markdown state synchronization and {len(nav_files)} navigation files."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
