"""Internal-only path guards for the legacy scientific engine.

Public Review and Repair routing is exclusively owned by ``run_context``.
These helpers reject arbitrary destinations for internal engine calls while
the engine is invoked from a run-local workspace.
"""

from __future__ import annotations

import re
from pathlib import Path

# Single annotation, never a routing switch.
REVIEW_LANE = "dual"
EXECUTION_CLAIM = "DUAL_LANE_CHECKER_ONLY"

MANAGEMENT_DIR_NAMES = frozenset(
    {
        "review_outputs",
        "review_records",
        "benchmark_audit",
        "benchmark_audit_history",
        ".benchmark_audit_tmp",
        ".benchmark_repair_tmp",
        ".benchmark_repair_history",
        "repair_history",
        "benchmark_repair_history",
    }
)

_CANONICAL_RELATIVE_ROOTS = {
    "review": Path("."),
    "source_audit": Path("benchmark_audit"),
    "repair": Path("repair"),
    "reaudit": Path("repair_reaudit"),
}

_PAPER_DIR_RE = re.compile(r"^paper-(.+)$")


def normalize_paper_id(package_name: str) -> str:
    """Return the paper id segment used under review_outputs/."""
    match = _PAPER_DIR_RE.fullmatch(package_name)
    if match:
        return match.group(1)
    if package_name.startswith("paper-"):
        return package_name[len("paper-") :]
    return package_name


def default_review_output_dir(package_root: Path) -> Path:
    """Return the historical internal-engine destination.

    Do not call this from public CLI or batch coordination code.
    """
    root = package_root.expanduser().resolve()
    topic = root.parent
    return (topic / "review_outputs" / normalize_paper_id(root.name)).resolve()


def require_external_output_dir(
    package_root: Path,
    output_dir: Path | None,
    *,
    label: str = "audit output directory",
    purpose: str = "review",
) -> Path:
    """Require one canonical output workspace below the theme sibling root."""
    root = package_root.expanduser().resolve()
    if output_dir is None:
        raise ValueError(f"{label} is required and must remain outside the Harbor 题包")
    resolved = output_dir.expanduser().resolve()
    if resolved == root or resolved.is_relative_to(root):
        raise ValueError(f"{label} must remain outside the Harbor 题包")
    # A public run owns an explicitly constructed ``.review_records`` root.
    # Internal preparation/finalization code still calls this guard, so accept
    # that one controlled layout without reopening arbitrary output routing.
    if ".review_records" in resolved.parts:
        return resolved
    expected = canonical_management_path(root, purpose)
    if resolved != expected:
        raise ValueError(
            f"{label} must equal the theme-sibling review root: {expected}"
        )
    return resolved


def canonical_management_path(package_root: Path, purpose: str) -> Path:
    """Return a role-specific path under the one canonical management root."""
    try:
        relative = _CANONICAL_RELATIVE_ROOTS[purpose]
    except KeyError as exc:
        raise ValueError(f"unknown review-output purpose: {purpose}") from exc
    return (default_review_output_dir(package_root) / relative).resolve()


def management_purpose(package_root: Path, path: Path) -> str:
    """Identify a canonical workspace path; reject arbitrary descendants."""
    resolved = path.expanduser().resolve()
    if ".review_records" in resolved.parts:
        return "review"
    for purpose in ("review", "reaudit"):
        if resolved == canonical_management_path(package_root, purpose):
            return purpose
    raise ValueError(
        "audit output directory must equal the canonical review or re-audit "
        f"workspace under {default_review_output_dir(package_root)}"
    )


def require_management_path(
    package_root: Path,
    path: Path | None,
    *,
    purpose: str,
    label: str,
) -> Path:
    """Require a role-specific path under the canonical sibling root."""
    if path is not None and ".review_records" in Path(path).expanduser().resolve().parts:
        # The only non-legacy management root is the run record. This branch
        # exists for internal engine composition; public callers cannot supply
        # it because their sole seam is --run-dir.
        return Path(path).expanduser().resolve()
    expected = canonical_management_path(package_root, purpose)
    if path is None or Path(path).expanduser().resolve() != expected:
        raise ValueError(f"{label} must equal {expected}")
    return expected


def is_management_path(path: Path, *, corpus_root: Path | None = None) -> bool:
    """True when a path is under a review/repair management directory name."""
    parts = set(path.parts)
    if parts & MANAGEMENT_DIR_NAMES:
        return True
    if corpus_root is not None:
        try:
            relative = path.resolve().relative_to(corpus_root.resolve())
        except ValueError:
            return False
        return bool(set(relative.parts) & MANAGEMENT_DIR_NAMES)
    return False
