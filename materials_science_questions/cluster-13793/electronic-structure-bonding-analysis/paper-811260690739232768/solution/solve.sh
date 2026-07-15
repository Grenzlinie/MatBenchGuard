#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: intercalation_preference.json ===
cat > $OUTDIR/intercalation_preference.json <<'FFEOF'
{"Li": 0.15, "Na": -0.10, "Mg": 0.25}
FFEOF

# === solve block: diffusion_barriers.csv ===
cat > /app/outputs/diffusion_barriers.csv <<'FFEOF'
metal,path,barrier_eV
Li,zigzag,0.02
Li,armchair,0.12
Na,zigzag,0.18
Na,armchair,0.76
Mg,zigzag,0.41
Mg,armchair,1.50
FFEOF

# === solve block: bulk_moduli.csv ===
cat > /app/outputs/bulk_moduli.csv <<'FFEOF'
composition,bulk_modulus_GPa
pristine,46
Li2P,26
Na2P,24
Mg2P,53
FFEOF
