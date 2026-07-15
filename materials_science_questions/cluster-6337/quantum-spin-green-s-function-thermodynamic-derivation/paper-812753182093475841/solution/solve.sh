#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: derived_expressions.py ===
cat > "$OUTDIR/derived_expressions.py" <<'FFEOF'
import math


def omega(k: float, I: float, h: float, S: float, T: float) -> float:
    """Low-temperature spin-wave frequency spectrum (Equation 17)."""
    # Precompute common terms
    four_I_S = 4.0 * I * S
    term = 1.0 - 0.5 * T / (I * S * S) * (1.0 - h / (h + four_I_S))
    # Ensure term positive; for physical parameters it is positive.
    if term < 0.0:
        term = 0.0
    return h + four_I_S * (math.sin(k / 2.0) ** 2) * math.sqrt(term)


def Gamma(k: float, I: float, h: float, S: float, T: float) -> float:
    """Low-temperature damping factor (Equation 17)."""
    return (8.0 * I * I / (h * (h + 4.0 * I * S))) * T * T * ((1.0 - math.cos(k)) ** 2)


def magnetization(I: float, h: float, S: float, T: float) -> float:
    """Low-temperature magnetization (Equation 17)."""
    return S - T / math.sqrt(h * (h + 4.0 * I * S))


def correlation(k: float, I: float, h: float, S: float, T: float) -> float:
    """Normalized spin correlation function <S_k^+ S_{-k}^->/(N S^2) (Equation 19)."""
    return (2.0 / S) * T / (h + 2.0 * I * S * (1.0 - math.cos(k)))
FFEOF
