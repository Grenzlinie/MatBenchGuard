#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: n1_energy_diff.txt ===
cat > /app/outputs/n1_energy_diff.txt <<'FFEOF'
4.0
FFEOF

# === solve block: n2_energy_diff.txt ===
cat > /app/outputs/n2_energy_diff.txt <<'FFEOF'
76.0
FFEOF

# === solve block: n3_energy_diff.txt ===
cat > /app/outputs/n3_energy_diff.txt <<'FFEOF'
6.0
FFEOF

# === solve block: n4_band_gap.txt ===
cat > /app/outputs/n4_band_gap.txt <<'FFEOF'
0.6
FFEOF

# === solve block: n5_band_gap.txt ===
cat > /app/outputs/n5_band_gap.txt <<'FFEOF'
0.0
FFEOF

# === solve block: n1_orbital_moment.txt ===
cat > /app/outputs/n1_orbital_moment.txt <<'FFEOF'
0.75
FFEOF
