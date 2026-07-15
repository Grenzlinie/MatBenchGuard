#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_02_work_of_adhesion.csv ===
cat > "$OUTDIR/step_02_work_of_adhesion.csv" <<'FFEOF'
interface,w_ad,area,total_energy_interface,total_energy_slab1,total_energy_slab2
undoped,-2.429,80.0,-150.8912,-100.0,-50.0
sidoped,-2.785,80.0,-151.0224,-100.0,-50.0
FFEOF

# === solve block: step_03_charge_transfer.csv ===
cat > "$OUTDIR/step_03_charge_transfer.csv" <<'FFEOF'
interface,ict
undoped,-0.467
sidoped,-0.346
FFEOF

# === solve block: step_04_bond_lengths.txt ===
cat > "$OUTDIR/step_04_bond_lengths.txt" <<'FFEOF'
Undoped: Ti-O 1.83 Å, Ca-O 2.43 Å (3 bonds: 2.36, 2.43, 2.50 Å). Si-doped: Ti-O 1.90 Å and 2.22 Å, Ca-O 2.34, 2.44, 2.46 Å (3 bonds).
FFEOF

# === solve finalize ===
echo "All reference outputs written."
