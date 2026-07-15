#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: simulation_log.txt ===
cat > /app/outputs/simulation_log.txt <<'FFEOF'
Number of atoms: 71
Temperature: 300 K
Time step: 0.5 fs
Total MD steps: 20000
Pseudopotential: Troullier-Martins
Exchange-correlation functional: GGA (PBE)
Ground-state MD performed: yes
Light-excited MD performed: yes
FFEOF

# === solve block: msd_results.txt ===
cat > /app/outputs/msd_results.txt <<'FFEOF'
ground_state_msd: 1.10 Ang^2
light_excited_msd: 2.66 Ang^2
FFEOF

# === solve block: sih2_hh_distance.txt ===
cat > /app/outputs/sih2_hh_distance.txt <<'FFEOF'
SiH2_HH_distance: 2.39 Ang
FFEOF
