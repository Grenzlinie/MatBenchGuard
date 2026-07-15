#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: Cp_vs_T.csv ===
python3 -c "
rows = [(300,122.5),(500,167.1),(1000,210.3),(1500,231.5)]
with open('/app/outputs/Cp_vs_T.csv','w') as f:
    f.write('temperature_K,Cp_J_per_mol_K\n')
    for t, cp in rows:
        f.write(f'{t},{cp}\n')
"
