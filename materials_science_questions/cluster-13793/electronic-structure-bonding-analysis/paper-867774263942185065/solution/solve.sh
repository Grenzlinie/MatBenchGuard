#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results_table.csv ===
cat > /app/outputs/results_table.csv <<'CSVEOF'
configuration_name,band_gap_eV,gap_type,magnetic_moment_muB,classification
AGNR_N12_pristine,0.60,direct,0.00,NM_Semiconductor
AGNR_13s,0.00,metal,0.00,NM_Metal
AGNR_1s,0.00,metal,0.47,FM_Metal
AGNR_6_21s,0.00,metal,0.00,NM_Metal
AGNR_6_21d,0.00,metal,0.00,NM_Metal
AGNR_1_23s,0.00,metal,0.76,FM_Metal
AGNR_1_23d,0.00,metal,0.76,FM_Metal
AGNR_1_6d,0.64,indirect,0.00,NM_Semiconductor
ZGNR_N8_pristine,0.46,direct,0.00,AFM_Semiconductor_no_split
ZGNR_3s,0.00,metal,0.42,FM_Metal
ZGNR_3_30s,0.20,direct,0.00,AFM_Semiconductor_no_split
ZGNR_3_30d,0.46,direct,0.00,NM_Semiconductor
ZGNR_11_14d,0.00,metal,0.37,FM_Metal
ZGNR_3_14d,0.00,metal,0.40,FM_Metal
CSVEOF
