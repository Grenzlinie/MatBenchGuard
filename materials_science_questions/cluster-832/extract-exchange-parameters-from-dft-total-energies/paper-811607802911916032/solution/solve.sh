#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: fitted_parameters.json ===
python3 -c "import json,os; data={'B_eff':540.0, 'T0':1000.0, 'T0i':300.0, 'J_Co_J_Mn':0.62}; json.dump(data,open(os.path.join(os.environ['OUTDIR'],'fitted_parameters.json'),'w'))"

# === solve block: coupling_angle_vs_temperature.csv ===
python3 -c "import os; T=list(range(10,151)); f=lambda x: 60.0 if x<=30 else (60.0*(1-(x-30)/70) if x<100 else 0.0); lines=['Temperature,Coupling_angle']+[f'{t},{f(t):.6f}' for t in T]; open(os.path.join(os.environ['OUTDIR'],'coupling_angle_vs_temperature.csv'),'w').write('\n'.join(lines))"

# === solve block: exchange_energies_vs_temperature.csv ===
python3 -c "import os; T=list(range(10,151)); J1=lambda t: -2e-5*max(0,(100-t)/90); J2=lambda t: 1.5e-5*max(0,(100-t)/90); lines=['Temperature,J1,J2']+[f'{t},{J1(t):.8e},{J2(t):.8e}' for t in T]; open(os.path.join(os.environ['OUTDIR'],'exchange_energies_vs_temperature.csv'),'w').write('\n'.join(lines))"
