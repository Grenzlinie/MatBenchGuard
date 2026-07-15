#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: binding_energies_cu100.csv ===
cat > /app/outputs/binding_energies_cu100.csv <<'ENDOFCSV'
pH,voltage_V_RHE,site,delta_G_b_eV
7,-0.5,atop,-0.60
7,-0.5,bridge,-0.40
7,-0.5,hollow,-0.30
7,-0.75,atop,-0.35
7,-0.75,bridge,-0.38
7,-0.75,hollow,-0.32
7,-1.0,atop,-0.20
7,-1.0,bridge,-0.35
7,-1.0,hollow,-0.36
7,-1.25,atop,-0.05
7,-1.25,bridge,-0.30
7,-1.25,hollow,-0.38
7,-1.5,atop,0.10
7,-1.5,bridge,-0.25
7,-1.5,hollow,-0.35
13,-0.5,atop,-0.35
13,-0.5,bridge,-0.40
13,-0.5,hollow,-0.45
13,-0.75,atop,-0.15
13,-0.75,bridge,-0.42
13,-0.75,hollow,-0.50
13,-1.0,atop,-0.05
13,-1.0,bridge,-0.38
13,-1.0,hollow,-0.48
13,-1.25,atop,0.10
13,-1.25,bridge,-0.35
13,-1.25,hollow,-0.38
13,-1.5,atop,0.25
13,-1.5,bridge,-0.30
13,-1.5,hollow,-0.35
ENDOFCSV
