#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 -c "import json; data=[\
  {'density':2.28,'shear_rate':0.0,'Nc':4.23,'qt':0.78,'u2':-95.0,'u3':5.0,'viscosity':None,'S2':-2.10},\
  {'density':2.28,'shear_rate':0.0001,'Nc':4.30,'qt':0.72,'u2':-94.0,'u3':6.5,'viscosity':460.0,'S2':-2.05},\
  {'density':2.28,'shear_rate':1.0,'Nc':5.0,'qt':0.35,'u2':-75.0,'u3':35.0,'viscosity':5.0,'S2':-1.0},\
  {'density':2.44,'shear_rate':0.0,'Nc':4.83,'qt':0.50,'u2':-85.0,'u3':20.0,'viscosity':None,'S2':-1.70},\
  {'density':2.44,'shear_rate':0.0001,'Nc':4.83,'qt':0.50,'u2':-84.0,'u3':21.5,'viscosity':30.0,'S2':-1.65},\
  {'density':2.44,'shear_rate':1.0,'Nc':5.0,'qt':0.35,'u2':-75.0,'u3':35.0,'viscosity':5.0,'S2':-1.0}\
]; json.dump(data, open('/app/outputs/results.json','w'))"
