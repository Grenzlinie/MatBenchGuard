#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: slope_case1.txt ===
python3 -c "import math; m_A=2; m_B=3; Tg0=318; Tg1=452; ratio=m_B/m_A; exponent=(Tg0-Tg1)/Tg0; numerator=1-ratio**exponent; denom=math.log(ratio); slope=Tg0*numerator/denom; print(slope)" > "$OUTDIR/slope_case1.txt"

# === solve block: slope_case2.txt ===
python3 -c "print(240-318)" > "$OUTDIR/slope_case2.txt"
