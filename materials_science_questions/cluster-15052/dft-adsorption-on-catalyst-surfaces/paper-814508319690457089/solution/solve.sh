#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: delta_G_H_table.csv ===
python3 - "$OUTDIR" << 'PYEOF'
import csv, sys
outdir = sys.argv[1] if len(sys.argv) > 1 else '/app/outputs'
path = f"{outdir}/delta_G_H_table.csv"

rows = [
    # System, Coverage, ActiveSite, DeltaE_H, DeltaG_H, ChargeTransfer
    ["V2CO2", "12.5%ML", "T0", -0.82, -0.45, 0.895],
    ["Fe-V2CO2", "12.5%ML", "T0", -0.58, -0.21, 0.912],
    ["Fe-V2CO2", "12.5%ML", "T1", -0.53, -0.16, 0.927],
    ["Fe-V2CO2", "12.5%ML", "T2", -0.28, 0.09, 0.941],
    ["Fe-V2CO2", "16.7%ML", "T0", -0.41, -0.04, 0.918],
    ["Fe-V2CO2", "16.7%ML", "T1", -0.34, 0.03, 0.933],
    ["Fe-V2CO2", "16.7%ML", "T2", -0.22, 0.15, 0.941],
    ["Fe-V2CO2", "25%ML", "T3", -0.06, 0.31, 0.967],
    ["Co-V2CO2", "12.5%ML", "T0", -0.60, -0.23, 0.909],
    ["Co-V2CO2", "12.5%ML", "T1", -0.60, -0.23, 0.924],
    ["Co-V2CO2", "12.5%ML", "T2", -0.40, -0.03, 0.932],
    ["Co-V2CO2", "16.7%ML", "T0", -0.47, -0.10, 0.913],
    ["Co-V2CO2", "16.7%ML", "T1", -0.42, -0.05, 0.929],
    ["Co-V2CO2", "16.7%ML", "T2", -0.30, 0.07, 0.932],
    ["Co-V2CO2", "25%ML", "T3", -0.27, 0.10, 0.952],
    ["Ni-V2CO2", "12.5%ML", "T0", -0.72, -0.35, 0.899],
    ["Ni-V2CO2", "12.5%ML", "T1", -0.66, -0.29, 0.918],
    ["Ni-V2CO2", "12.5%ML", "T2", -0.52, -0.15, 0.923],
    ["Ni-V2CO2", "16.7%ML", "T0", -0.60, -0.23, 0.905],
    ["Ni-V2CO2", "16.7%ML", "T1", -0.53, -0.16, 0.918],
    ["Ni-V2CO2", "16.7%ML", "T2", -0.45, -0.08, 0.927],
    ["Ni-V2CO2", "25%ML", "T3", -0.38, -0.01, 0.946]
]

with open(path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['System','Coverage','ActiveSite','DeltaE_H','DeltaG_H','ChargeTransfer'])
    for r in rows:
        # guarantee numeric types: replace None with 0.0 (should never hit, but safe)
        r[3] = float(r[3]) if r[3] is not None else 0.0
        r[4] = float(r[4]) if r[4] is not None else 0.0
        r[5] = float(r[5]) if r[5] is not None else 0.0
        writer.writerow(r)
PYEOF

# === solve block: strain_dependence.csv ===
python3 << 'EOF'
import csv

# Linear models derived from paper's strain points:
# T0(12.5% Co): at e=-0.025 dG=-0.09; at e=0 dG=-0.23  -> dG = -0.23 - 5.6*e
# T1(12.5% Fe): at e=-0.025 dG=-0.03; at e=0 dG=-0.16  -> dG = -0.16 - 5.2*e
# T2(12.5% Co): at e=-0.005 dG=0.00; at e=0 dG=-0.03  -> dG = -0.03 - 6.0*e
# T3(25% Ni):   at e=-0.0027 dG=0.00; at e=0 dG=-0.01 -> dG = -0.01 - 3.704*e
# T3(25% Co):   at e=0.025 dG=0.03;  at e=0 dG=0.10   -> dG =  0.10 - 2.8*e

def gh_T0_Co(e): return -0.23 - 5.6 * e
def gh_T1_Fe(e): return -0.16 - 5.2 * e
def gh_T2_Co(e): return -0.03 - 6.0 * e
def gh_T3_Ni(e): return -0.01 - 3.704 * e
def gh_T3_Co(e): return  0.10 - 2.8 * e

strains = [-0.025, -0.01, -0.005, -0.0027, 0.0, 0.005, 0.01, 0.025]

rows = []
for e in strains:
    rows.append(["T0(12.5% Co)", e, round(gh_T0_Co(e), 6)])
    rows.append(["T1(12.5% Fe)", e, round(gh_T1_Fe(e), 6)])
    rows.append(["T2(12.5% Co)", e, round(gh_T2_Co(e), 6)])
    rows.append(["T3(25% Ni)",   e, round(gh_T3_Ni(e), 6)])
    rows.append(["T3(25% Co)",   e, round(gh_T3_Co(e), 6)])

with open('/app/outputs/strain_dependence.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['System','Strain','DeltaG_H'])
    writer.writerows(rows)
EOF
