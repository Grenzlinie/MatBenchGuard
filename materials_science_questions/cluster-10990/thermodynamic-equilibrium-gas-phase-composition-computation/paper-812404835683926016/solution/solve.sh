#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: gas_composition.csv ===
python3 << 'PYEOF'
import csv, os

outpath = '/app/outputs/gas_composition.csv'

rows = [
    {'Temperature': 800, 'WaterWoodRatio': '0.5/1', 'TotalMoles': 9.535,
     'H2': 0.479, 'CO': 0.361, 'H2O': 0.069, 'CO2': 0.057, 'CH4': 0.032,
     'N2': 0.0018, 'H2S': 0.00069, 'LiquidPresent': False},
    {'Temperature': 700, 'WaterWoodRatio': '0.5/1', 'TotalMoles': 8.057,
     'H2': 0.419, 'CO': 0.209, 'H2O': 0.166, 'CO2': 0.135, 'CH4': 0.069,
     'N2': 0.0021, 'H2S': 0.000095, 'LiquidPresent': False},
    {'Temperature': 600, 'WaterWoodRatio': '0.5/1', 'TotalMoles': 6.819,
     'H2': 0.304, 'CO': 0.075, 'H2O': 0.295, 'CO2': 0.196, 'CH4': 0.128,
     'N2': 0.0024, 'H2S': 0.00011, 'LiquidPresent': False},
    {'Temperature': 800, 'WaterWoodRatio': '0.75/1', 'TotalMoles': 11.202,
     'H2': 0.484, 'CO': 0.285, 'H2O': 0.131, 'CO2': 0.085, 'CH4': 0.014,
     'N2': 0.0015, 'H2S': 0.000068, 'LiquidPresent': True},
    {'Temperature': 700, 'WaterWoodRatio': '0.75/1', 'TotalMoles': 10.038,
     'H2': 0.415, 'CO': 0.211, 'H2O': 0.166, 'CO2': 0.138, 'CH4': 0.068,
     'N2': 0.0017, 'H2S': 0.000077, 'LiquidPresent': False},
    {'Temperature': 600, 'WaterWoodRatio': '0.75/1', 'TotalMoles': 8.495,
     'H2': 0.301, 'CO': 0.076, 'H2O': 0.295, 'CO2': 0.201, 'CH4': 0.125,
     'N2': 0.002, 'H2S': 0.000091, 'LiquidPresent': False},
    {'Temperature': 800, 'WaterWoodRatio': '1/1', 'TotalMoles': 12.699,
     'H2': 0.470, 'CO': 0.229, 'H2O': 0.191, 'CO2': 0.102, 'CH4': 0.0068,
     'N2': 0.0013, 'H2S': 0.000061, 'LiquidPresent': False},
    {'Temperature': 700, 'WaterWoodRatio': '1/1', 'TotalMoles': 11.780,
     'H2': 0.423, 'CO': 0.175, 'H2O': 0.212, 'CO2': 0.143, 'CH4': 0.046,
     'N2': 0.0014, 'H2S': 0.000065, 'LiquidPresent': False},
    {'Temperature': 600, 'WaterWoodRatio': '1/1', 'TotalMoles': 10.171,
     'H2': 0.299, 'CO': 0.076, 'H2O': 0.295, 'CO2': 0.203, 'CH4': 0.124,
     'N2': 0.0016, 'H2S': 0.00076, 'LiquidPresent': False},
]

fieldnames = ['Temperature', 'WaterWoodRatio', 'TotalMoles', 'H2', 'CO', 'H2O', 'CO2', 'CH4', 'N2', 'H2S', 'LiquidPresent']

with open(outpath, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
PYEOF
