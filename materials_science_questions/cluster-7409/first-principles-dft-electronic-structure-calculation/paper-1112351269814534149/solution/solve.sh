#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_structure.json ===
python3 << 'PYEOF'
import json, math

# lattice constant of the p(2x2) lateral cell (2 * 5.43 Å)
a = 10.86  # Å

# distances to high‑symmetry points (1/Å)
k_M = math.pi * math.sqrt(2) / a   # Gamma-M distance
k_X = math.pi / a                 # Gamma-X distance

# effective masses in units of m_e
m_GM = 0.64
m_GX = 0.68

# constant C = (hbar^2/(2*m_e))  in eV·Å^2
hbar = 1.054571817e-34   # J·s
m_e  = 9.1093837015e-31  # kg
eV_J = 1.602176634e-19   # J/eV
C = (hbar**2 / (2*m_e)) / eV_J * 1e20   # eV·Å^2

A_GM = C / m_GM
A_GX = C / m_GX

# evenly spaced k-points along each direction
npts = 100
k_GM = [i/(npts-1)*k_M for i in range(npts)]
E_GM = [A_GM * k**2 for k in k_GM]
k_GX = [i/(npts-1)*k_X for i in range(npts)]
E_GX = [A_GX * k**2 for k in k_GX]

data = {
  "Gamma_M": {
    "kpoints": k_GM,
    "energies_ev": E_GM
  },
  "Gamma_X": {
    "kpoints": k_GX,
    "energies_ev": E_GX
  }
}

with open("/app/outputs/band_structure.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
