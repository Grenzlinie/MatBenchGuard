#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: binding_energies.csv ===
python3 << 'PYEOF'
import csv, os
data = [
    {'surface': 'CMK3', 'bonding_motif': 'face', 'sulfur_species': 'S8', 'binding_energy_eV': 0.42},
    {'surface': 'CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S', 'binding_energy_eV': 0.51},
    {'surface': 'CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S2', 'binding_energy_eV': 0.46},
    {'surface': 'CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S4', 'binding_energy_eV': 0.40},
    {'surface': 'CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S6', 'binding_energy_eV': 0.38},
    {'surface': 'CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S8', 'binding_energy_eV': 0.44},
    {'surface': 'EN-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'S8', 'binding_energy_eV': 0.65},
    {'surface': 'EN-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S', 'binding_energy_eV': 0.92},
    {'surface': 'EN-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S2', 'binding_energy_eV': 0.88},
    {'surface': 'EN-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S4', 'binding_energy_eV': 0.80},
    {'surface': 'EN-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S6', 'binding_energy_eV': 0.78},
    {'surface': 'EN-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S8', 'binding_energy_eV': 0.70},
    {'surface': 'DMA-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'S8', 'binding_energy_eV': 0.72},
    {'surface': 'DMA-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S', 'binding_energy_eV': 1.05},
    {'surface': 'DMA-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S2', 'binding_energy_eV': 1.00},
    {'surface': 'DMA-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S4', 'binding_energy_eV': 0.95},
    {'surface': 'DMA-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S6', 'binding_energy_eV': 0.92},
    {'surface': 'DMA-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S8', 'binding_energy_eV': 0.78},
    {'surface': 'TMMA-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'S8', 'binding_energy_eV': 0.68},
    {'surface': 'TMMA-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S', 'binding_energy_eV': 0.98},
    {'surface': 'TMMA-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S2', 'binding_energy_eV': 0.93},
    {'surface': 'TMMA-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S4', 'binding_energy_eV': 0.88},
    {'surface': 'TMMA-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S6', 'binding_energy_eV': 0.85},
    {'surface': 'TMMA-CMK3', 'bonding_motif': 'face', 'sulfur_species': 'Li2S8', 'binding_energy_eV': 0.74},
    {'surface': 'CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'S8', 'binding_energy_eV': 0.38},
    {'surface': 'CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S', 'binding_energy_eV': 0.47},
    {'surface': 'CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S2', 'binding_energy_eV': 0.42},
    {'surface': 'CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S4', 'binding_energy_eV': 0.36},
    {'surface': 'CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S6', 'binding_energy_eV': 0.34},
    {'surface': 'CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S8', 'binding_energy_eV': 0.40},
    {'surface': 'EN-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'S8', 'binding_energy_eV': 0.60},
    {'surface': 'EN-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S', 'binding_energy_eV': 0.88},
    {'surface': 'EN-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S2', 'binding_energy_eV': 0.84},
    {'surface': 'EN-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S4', 'binding_energy_eV': 0.76},
    {'surface': 'EN-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S6', 'binding_energy_eV': 0.74},
    {'surface': 'EN-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S8', 'binding_energy_eV': 0.66},
    {'surface': 'DMA-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'S8', 'binding_energy_eV': 0.65},
    {'surface': 'DMA-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S', 'binding_energy_eV': 1.00},
    {'surface': 'DMA-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S2', 'binding_energy_eV': 0.95},
    {'surface': 'DMA-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S4', 'binding_energy_eV': 0.90},
    {'surface': 'DMA-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S6', 'binding_energy_eV': 0.87},
    {'surface': 'DMA-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S8', 'binding_energy_eV': 0.73},
    {'surface': 'TMMA-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'S8', 'binding_energy_eV': 0.62},
    {'surface': 'TMMA-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S', 'binding_energy_eV': 0.93},
    {'surface': 'TMMA-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S2', 'binding_energy_eV': 0.88},
    {'surface': 'TMMA-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S4', 'binding_energy_eV': 0.83},
    {'surface': 'TMMA-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S6', 'binding_energy_eV': 0.80},
    {'surface': 'TMMA-CMK3', 'bonding_motif': 'edge', 'sulfur_species': 'Li2S8', 'binding_energy_eV': 0.69}
]
with open(os.path.join(os.environ['OUTDIR'], 'binding_energies.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['surface', 'bonding_motif', 'sulfur_species', 'binding_energy_eV'])
    w.writeheader()
    w.writerows(data)
PYEOF
