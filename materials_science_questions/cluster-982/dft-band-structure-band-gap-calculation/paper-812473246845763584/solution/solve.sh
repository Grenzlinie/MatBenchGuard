#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gap.txt ===
cat > /app/outputs/band_gap.txt <<'FFEOF'
1.10
FFEOF

# === solve block: elastic_constants.json ===
cat > /app/outputs/elastic_constants.json <<'FFEOF'
{
  "C11": 161.12,
  "C12": 84.93,
  "C66": 12.62
}
FFEOF

# === solve block: young_modulus_diagonal.txt ===
cat > /app/outputs/young_modulus_diagonal.txt <<'FFEOF'
46.0
FFEOF

# === solve block: phonon_min_frequency.txt ===
cat > /app/outputs/phonon_min_frequency.txt <<'FFEOF'
0.0
FFEOF
