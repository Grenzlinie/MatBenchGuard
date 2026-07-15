#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: total_energies.csv ===
cat > "$OUTDIR/total_energies.csv" <<'CSVEOF'
composition_label,structure,total_energy_per_fu_eV
x0.00_3to1,A15,-55.00
x0.25_3to1,A15,-54.90
x0.50_3to1,A15,-54.80
x0.75_3to1,A15,-54.70
x1.00_3to1,A15,-54.60
x0.00_3to1,Ni2In,-54.00
x0.25_3to1,Ni2In,-53.90
x0.50_3to1,Ni2In,-53.80
x0.75_3to1,Ni2In,-53.70
x1.00_3to1,Ni2In,-53.60
x0.00_2to1,A15,-44.00
x0.25_2to1,A15,-43.85
x0.50_2to1,A15,-43.70
x0.75_2to1,A15,-43.55
x1.00_2to1,A15,-43.40
x0.00_2to1,Ni2In,-44.50
x0.25_2to1,Ni2In,-44.35
x0.50_2to1,Ni2In,-44.20
x0.75_2to1,Ni2In,-44.05
x1.00_2to1,Ni2In,-43.90
x0.00_2to1,Heusler,-45.00
x0.25_2to1,Heusler,-44.20
x0.50_2to1,Heusler,-44.00
x0.75_2to1,Heusler,-43.80
x1.00_2to1,Heusler,-43.70
CSVEOF

# === solve block: magnetic_moments.csv ===
cat > "$OUTDIR/magnetic_moments.csv" <<'CSVEOF'
composition_label,magnetic_moment_muB,site_index
x0.25_3to1_hex,2.22,1
x0.25_3to1_hex,2.58,2
x0.50_3to1_hex,2.20,1
x0.50_3to1_hex,2.62,2
x0.75_3to1_hex,2.25,1
x0.75_3to1_hex,2.55,2
x1.00_3to1_hex,2.21,1
x1.00_3to1_hex,2.60,2
x0.25_2to1_hex,2.18,1
x0.25_2to1_hex,2.57,2
x0.50_2to1_hex,2.23,1
x0.50_2to1_hex,2.61,2
x0.75_2to1_hex,2.20,1
x0.75_2to1_hex,2.59,2
x1.00_2to1_hex,2.24,1
x1.00_2to1_hex,2.63,2
CSVEOF

# === solve finalize ===
echo "All reference artifacts generated."
