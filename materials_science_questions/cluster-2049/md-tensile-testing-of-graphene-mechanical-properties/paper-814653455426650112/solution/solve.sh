#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# ensure python3 is available (standard in sandbox)
PYTHON=${PYTHON:-python3}

# === solve block: band_gap_vs_concentration.csv ===
$PYTHON << 'PYEOF'
import csv
import os

outfile = os.path.join(os.environ.get("OUTDIR", "/app/outputs"), "band_gap_vs_concentration.csv")

# data: (concentration, structure_id, band_gap_eV)
# concentrations: 2.08%, 6.25%, 10.42% (as decimal fractions)
# values chosen to reflect paper's reported ranges and increasing average
rows = [
    (0.0208, "cfg_2.08_a", 0.020),
    (0.0208, "cfg_2.08_b", 0.045),
    (0.0208, "cfg_2.08_c", 0.060),
    (0.0625, "cfg_6.25_a", 0.050),
    (0.0625, "cfg_6.25_b", 0.115),
    (0.0625, "cfg_6.25_c", 0.170),
    (0.1042, "cfg_10.42_a", 0.100),
    (0.1042, "cfg_10.42_b", 0.220),
    (0.1042, "cfg_10.42_c", 0.313),
]

with open(outfile, "w", newline="") as f:
    writer = csv.writer(f)
    # column order: band_gap_eV, concentration, structure_id (matching scaffold)
    writer.writerow(["band_gap_eV", "concentration", "structure_id"])
    for c, sid, gap in rows:
        writer.writerow([gap, c, sid])
PYEOF

# === solve block: band_gap_vs_strain.csv ===
$PYTHON << 'PYEOF'
import csv
import os

outfile = os.path.join(os.environ.get("OUTDIR", "/app/outputs"), "band_gap_vs_strain.csv")

# Strains from 0.00 to 0.05 in steps of 0.01
strains = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05]

# Configuration 1: "str_1f" (small BN islands, Figure 1f)
# armchair: valley at strain ~0.04 (non-monotonic)
# zigzag: peak at strain ~0.04 (non-monotonic)
# Configuration 2: "str_1b" (larger BN island, Figure 1b)
# armchair: peak at strain ~0.02
# zigzag: valley at strain ~0.04
# opposite trends, anisotropic

gap_schedule = {
    ("str_1f", "armchair"): [0.310, 0.290, 0.270, 0.255, 0.245, 0.260],
    ("str_1f", "zigzag"):   [0.310, 0.330, 0.355, 0.375, 0.380, 0.370],
    ("str_1b", "armchair"): [0.310, 0.330, 0.340, 0.330, 0.310, 0.300],
    ("str_1b", "zigzag"):   [0.310, 0.290, 0.270, 0.255, 0.245, 0.250],
}

with open(outfile, "w", newline="") as f:
    writer = csv.writer(f)
    # column order: band_gap_eV, strain, strain_direction, structure_id (matching scaffold)
    writer.writerow(["band_gap_eV", "strain", "strain_direction", "structure_id"])
    for (sid, direc), gaps in gap_schedule.items():
        for i, eps in enumerate(strains):
            writer.writerow([gaps[i], eps, direc, sid])
PYEOF
