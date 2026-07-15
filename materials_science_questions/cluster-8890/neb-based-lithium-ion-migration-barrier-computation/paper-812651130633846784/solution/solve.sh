#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: results.json ===
cat > $OUTDIR/results.json <<'FFEOF'
{
  "adsorption_energies": [
    {"species": "Li2S", "condition": "vacuum", "with_vdw": true, "energy_eV": -4.43},
    {"species": "Li2S", "condition": "vacuum", "with_vdw": false, "energy_eV": -3.77},
    {"species": "Li2S", "condition": "solvent", "with_vdw": true, "energy_eV": -3.21},
    {"species": "Li2S", "condition": "solvent", "with_vdw": false, "energy_eV": -2.59},
    {"species": "Li2S2", "condition": "vacuum", "with_vdw": true, "energy_eV": -3.48},
    {"species": "Li2S2", "condition": "vacuum", "with_vdw": false, "energy_eV": -2.74},
    {"species": "Li2S2", "condition": "solvent", "with_vdw": true, "energy_eV": -2.54},
    {"species": "Li2S2", "condition": "solvent", "with_vdw": false, "energy_eV": -1.86},
    {"species": "Li2S4", "condition": "vacuum", "with_vdw": true, "energy_eV": -2.62},
    {"species": "Li2S4", "condition": "vacuum", "with_vdw": false, "energy_eV": -1.90},
    {"species": "Li2S4", "condition": "solvent", "with_vdw": true, "energy_eV": -2.11},
    {"species": "Li2S4", "condition": "solvent", "with_vdw": false, "energy_eV": -1.44},
    {"species": "Li2S6", "condition": "vacuum", "with_vdw": true, "energy_eV": -2.54},
    {"species": "Li2S6", "condition": "vacuum", "with_vdw": false, "energy_eV": -1.61},
    {"species": "Li2S6", "condition": "solvent", "with_vdw": true, "energy_eV": -1.93},
    {"species": "Li2S6", "condition": "solvent", "with_vdw": false, "energy_eV": -0.98},
    {"species": "Li2S8", "condition": "vacuum", "with_vdw": true, "energy_eV": -2.99},
    {"species": "Li2S8", "condition": "vacuum", "with_vdw": false, "energy_eV": -1.82},
    {"species": "Li2S8", "condition": "solvent", "with_vdw": true, "energy_eV": -2.37},
    {"species": "Li2S8", "condition": "solvent", "with_vdw": false, "energy_eV": -1.22},
    {"species": "S8", "condition": "vacuum", "with_vdw": true, "energy_eV": -1.08},
    {"species": "S8", "condition": "vacuum", "with_vdw": false, "energy_eV": -0.35},
    {"species": "S8", "condition": "solvent", "with_vdw": true, "energy_eV": -0.94},
    {"species": "S8", "condition": "solvent", "with_vdw": false, "energy_eV": -0.21}
  ],
  "diffusion_barrier": {
    "species": "Li2S",
    "barrier_eV": 1.52
  }
}
FFEOF
