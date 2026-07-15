#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_properties.csv ===
cat > /tmp/gen_csv.py << 'PYEOF'
import csv
rows = [
    ['pristine_TAC','TAC','none','none',6.16,18.65,355.2,292.4,119.3,82.2,76.6,163.0,125.8,300.2,0.2,0.8,5429,8802,5989,766,0.0],
    ['pristine_TSC','TSC','none','none',6.15,17.75,364.2,351.8,157.2,95.4,112.5,191.2,139.6,336.9,0.2,0.7,5584,9180,6169,800,0.0],
    ['HfTi1_TAC','TAC','substitutional_Ti1','Hf',6.19,18.70,348.0,290.9,115.0,88.5,75.3,162.0,121.5,291.6,0.2,0.8,5185,8468,5725,726,0.0],
    ['NbTi1_TAC','TAC','substitutional_Ti1','Nb',6.18,18.65,353.0,295.3,120.4,86.6,75.7,163.4,125.4,299.6,0.2,0.8,5393,8756,5950,756,0.0],
    ['ZrTi1_TAC','TAC','substitutional_Ti1','Zr',6.20,18.72,343.8,287.8,113.9,88.4,74.6,160.4,120.0,288.2,0.2,0.8,5301,8662,5853,742,0.0],
    ['HfTi1_TSC','TSC','substitutional_Ti1','Hf',6.18,17.78,362.2,354.2,142.9,97.8,107.3,189.3,134.5,326.2,0.2,0.7,5296,8767,5854,756,0.0],
    ['NbTi1_TSC','TSC','substitutional_Ti1','Nb',6.16,17.77,366.0,355.8,150.2,96.0,110.3,191.2,138.1,333.9,0.2,0.7,5492,9055,6069,785,0.0],
    ['ZrTi1_TSC','TSC','substitutional_Ti1','Zr',6.18,17.79,359.3,351.4,142.3,97.5,107.0,188.1,133.4,323.8,0.2,0.7,5424,8984,5997,774,0.0],
    ['Hfi_TAC','TAC','interstitial_c-ATi2','Hf',6.24,19.03,310.7,176.7,108.6,91.6,85.1,141.6,88.7,220.2,0.2,0.6,4446,7610,4931,622,1.35],
    ['Nbi_TAC','TAC','interstitial_c-ATi2','Nb',6.23,18.95,326.3,226.2,116.0,91.7,83.4,150.9,104.5,254.7,0.2,0.7,4933,8220,5457,690,0.0],
    ['Zri_TAC','TAC','interstitial_c-ATi2','Zr',6.24,19.09,310.5,181.6,110.9,87.8,78.8,139.0,89.5,221.1,0.2,0.6,4586,7791,5082,641,1.0],
    ['Hfi_TSC','TSC','interstitial_c-ATi2','Hf',6.24,18.10,318.3,238.0,99.1,119.7,106.8,169.2,93.2,236.3,0.3,0.6,4430,7861,4928,633,0.0],
    ['Nbi_TSC','TSC','interstitial_c-ATi2','Nb',6.23,18.02,328.5,276.5,106.4,118.1,111.6,176.8,102.8,258.2,0.3,0.6,4754,8306,5282,680,0.0],
    ['Zri_TSC','TSC','interstitial_c-ATi2','Zr',6.23,18.17,314.0,239.4,97.1,120.6,103.9,167.5,93.5,236.6,0.3,0.6,4557,8056,5068,650,0.0],
]
with open('/app/outputs/computed_properties.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['system','host','doping_type','dopant','a0_A','c0_A','C11_GPa','C33_GPa','C44_GPa','C12_GPa','C13_GPa','B_GPa','G_GPa','E_GPa','sigma','G_B_ratio','vt_ms','vl_ms','vm_ms','ThetaD_K','Mag_muB'])
    w.writerows(rows)
PYEOF
python3 /tmp/gen_csv.py
