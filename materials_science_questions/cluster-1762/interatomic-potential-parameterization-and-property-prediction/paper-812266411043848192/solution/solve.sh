#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: elastic_constants.csv ===
cat > /app/outputs/elastic_constants.csv <<'FFEOF'
stoichiometry,prototype,C11,C12,C13,C33,C44,C_prime
Ag3Ru,D03,111.26,132.88,NA,NA,79.45,-10.81
Ag3Ru,L12,160.14,115.28,NA,NA,65.15,22.43
Ag3Ru,D019,191.57,109.15,85.74,225.22,37.26,33.06
AgRu3,D03,167.75,251.31,NA,NA,62.81,-41.78
AgRu3,L12,323.93,192.12,NA,NA,117.60,65.91
AgRu3,D019,275.46,244.52,157.93,387.75,16.66,15.47
FFEOF

# === solve block: phonon_stability.json ===
cat > /app/outputs/phonon_stability.json <<'FFEOF'
[
  {"stoichiometry":"Ag3Ru","prototype":"D03","has_imaginary_frequencies":true},
  {"stoichiometry":"Ag3Ru","prototype":"L12","has_imaginary_frequencies":true},
  {"stoichiometry":"Ag3Ru","prototype":"D019","has_imaginary_frequencies":true},
  {"stoichiometry":"AgRu3","prototype":"D03","has_imaginary_frequencies":true},
  {"stoichiometry":"AgRu3","prototype":"L12","has_imaginary_frequencies":false},
  {"stoichiometry":"AgRu3","prototype":"D019","has_imaginary_frequencies":false}
]
FFEOF
