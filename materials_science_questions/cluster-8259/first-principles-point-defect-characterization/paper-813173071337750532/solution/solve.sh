#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_stability.csv ===
python3 /solution/write_outputs.py --outfile /app/outputs/step_01_stability.csv --mode stability

# === solve block: step_02_defect_formation.csv ===
cat > $OUTDIR/step_02_defect_formation.csv << 'CSVEOF'
compound,charge_state,formation_energy_eV
Cu4SnS4,-1,1.8
Cu4SnS4,0,1.2
Cu4SnS4,1,2.5
Cu2SnS3,-1,2.2
Cu2SnS3,0,1.5
Cu2SnS3,1,3.0
Cu4Sn7S16,-1,1.5
Cu4Sn7S16,0,0.8
Cu4Sn7S16,1,2.0
E_F_pin_range,0,0.5
E_F_pin_range,1,1.35
E_F_pin_range,2,0.15
CSVEOF

# === solve block: step_03_band_gaps.csv ===
python3 /solution/write_outputs.py --outfile /app/outputs/step_03_band_gaps.csv --mode bandgaps

# === solve block: step_04_absorption_spectra.csv ===
python3 /solution/write_outputs.py --outfile /app/outputs/step_04_absorption_spectra.csv --mode absorption
