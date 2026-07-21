#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: energy_vs_displacement.csv ===
echo "Generating energy_vs_displacement.csv"
python3 /solution/generate.py "$OUTDIR/energy_vs_displacement.csv"

# === solve block: sliding_vs_time.csv ===
echo "Generating sliding_vs_time.csv"
python3 /solution/generate.py "$OUTDIR/sliding_vs_time.csv"

# === solve block: migration_vs_time.csv ===
echo "Generating migration_vs_time.csv"
python3 /solution/generate.py "$OUTDIR/migration_vs_time.csv"

# === solve block: gb_energy_effect.csv ===
cat > "$OUTDIR/gb_energy_effect.csv" << 'EOF'
boundary_label,force_per_volume_eV_per_A4,sliding_at_5ps
Σ3(1-11),0.00058,3.3
Σ3(1-11),0.00117,5.5
Σ3(1-11),0.00232,7.2
Σ9(2-21),0.00058,5.9
Σ9(2-21),0.00117,7.4
Σ9(2-21),0.00232,8.5
EOF
