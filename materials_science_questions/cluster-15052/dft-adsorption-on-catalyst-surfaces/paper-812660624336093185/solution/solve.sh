#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: repairing_process_results.csv ===
cat > /app/outputs/repairing_process_results.csv <<'CSVEOF'
state,E_ad,barrier,Hirshfeld_charge_NO,Hirshfeld_charge_N1,Hirshfeld_charge_O1
IS1,-0.06,,,-0.17,-0.08,-0.09
TS1,,0.51,,,-0.34,-0.18,-0.16
FS1,-7.01,,,-0.20,-0.05,-0.15
CSVEOF

# === solve block: removing_process_results.csv ===
cat > /app/outputs/removing_process_results.csv <<'CSVEOF'
state,E_ad,barrier,Hirshfeld_charge_NO2_total,Hirshfeld_charge_N1,Hirshfeld_charge_O1,Hirshfeld_charge_N2,Hirshfeld_charge_O2
IS2,-0.15,,0.01,-0.05,-0.15,0.02,-0.01
TS2,,0.22,0.08,-0.12,-0.22,0.12,-0.04
FS2,-0.28,,-0.06,-0.20,-0.10,0.14,-0.10
CSVEOF
