#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: band_gaps.csv ===
cat > "$OUTDIR/band_gaps.csv" <<'FFEOF'
compound,band_gap_ev
α-NaMnFe(MoO₄)₃,1.15
α-NaFe₂(MoO₄)₃,1.22
α-NaCoFe(MoO₄)₃,2.33
α-NaNiFe(MoO₄)₃,2.51
α-NaZnFe(MoO₄)₃,2.58
β-NaMnFe(MoO₄)₃,1.56
β-NaFe₂(MoO₄)₃,1.06
β-NaCoFe(MoO₄)₃,2.18
β-NaNiFe(MoO₄)₃,2.39
β-NaZnFe(MoO₄)₃,2.54
FFEOF

# === solve block: extraction_potentials.csv ===
cat > "$OUTDIR/extraction_potentials.csv" <<'FFEOF'
compound,V1_ev,V2_ev
α-NaMnFe(MoO₄)₃,3.22,3.74
α-NaFe₂(MoO₄)₃,3.36,3.58
α-NaCoFe(MoO₄)₃,4.30,4.23
α-NaNiFe(MoO₄)₃,4.99,4.99
α-NaZnFe(MoO₄)₃,5.08,5.08
β-NaMnFe(MoO₄)₃,4.00,3.99
β-NaFe₂(MoO₄)₃,3.50,3.64
β-NaCoFe(MoO₄)₃,4.43,4.62
β-NaNiFe(MoO₄)₃,4.97,5.22
β-NaZnFe(MoO₄)₃,5.08,5.29
FFEOF
