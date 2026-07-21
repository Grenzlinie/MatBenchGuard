#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: phonon_dispersion.csv ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple 'numpy<2'
python3 /solution/compute.py --mode dispersion

# === solve block: phonon_dos.csv ===
python3 /solution/compute.py --mode dos

# === solve block: specific_heat.csv ===
python3 /solution/compute.py --mode cv

# === solve block: debye_temperature.csv ===
python3 /solution/compute.py --mode thetad
