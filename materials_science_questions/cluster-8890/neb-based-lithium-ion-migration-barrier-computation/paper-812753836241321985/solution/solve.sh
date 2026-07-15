#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lattice_constant.json ===
cat >/app/outputs/lattice_constant.json <<'FFEOF'
{
  "lattice_constant": 3.153
}
FFEOF

# === solve block: single_li_adsorption.csv ===
cat >/app/outputs/single_li_adsorption.csv <<'FFEOF'
site,energy_eV
S1,3.75
S2,3.44
S4,3.50
S5,3.52
S6,3.64
Mo4',2.87
Mo5',2.05
Mo6',2.14
Mo7',3.11
middle_a,2.73
middle_b,2.76
middle_c,2.99
middle_d,3.04
Mo-top,1.70
S-top,1.01
valley-top,1.54
FFEOF

# === solve block: two_li_adsorption.csv ===
cat >/app/outputs/two_li_adsorption.csv <<'FFEOF'
configuration,energy_eV
S_terminal_1-1N,6.71
S_terminal_1-d,6.29
S_terminal_1-1s,6.98
Mo_terminal_7'-7N',5.23
Mo_terminal_7'-a,5.13
Mo_terminal_7'-1',4.93
Mo_terminal_7'-7s',5.57
FFEOF

# === solve block: diffusion_barriers.csv ===
cat >/app/outputs/diffusion_barriers.csv <<'FFEOF'
path,barrier_eV
S_edge_T1_T2,0.31
Mo_edge_T1_T2,0.47
middle_to_S_edge,0.18
middle_to_Mo_edge,0.22
2D_monolayer,0.23
FFEOF
