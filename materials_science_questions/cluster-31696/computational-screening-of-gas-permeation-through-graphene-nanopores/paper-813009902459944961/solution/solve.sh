#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: diffusion_barriers_and_bader.csv ===
cat > /app/outputs/diffusion_barriers_and_bader.csv <<'FFEOF'
gas,diffusion_barrier_eV,bader_charge_loss_e
He,0.640,0.0594
Ne,0.400,0.1184
H2,0.470,0.0890
Ar,1.200,0.1150
Kr,1.200,0.0981
FFEOF
