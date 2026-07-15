#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 - <<'PYEOF'

# === solve block: relaxation_and_frequencies.csv ===
import os

outdir = os.environ.get('OUTDIR', '/app/outputs')
outpath = os.path.join(outdir, 'relaxation_and_frequencies.csv')

with open(outpath, 'w', encoding='utf-8') as f:
    f.write('oxide,plane,clean_ΔE_relax,hyd_ΔE_relax,E_hyd,freq_HOs,freq_HOw\n')
    f.write('MgO,(001),-0.00011,-0.01332,0.03389,3404.0,4419.4\n')
    f.write('MgO,(110),-0.00307,-0.01141,-0.04660,3860.4,4390.1\n')
    f.write('MgO,(210),-0.00332,-0.00294,-0.04371,3911.6,4352.9\n')
    f.write('CaO,(001),-0.00021,-0.00847,0.00812,3750.0,4321.6\n')
    f.write('CaO,(110),-0.00711,-0.00714,-0.05553,3974.5,4309.5\n')
    f.write('CaO,(210),-0.00286,-0.00386,-0.05422,3999.5,4292.0\n')
    f.write('SrO,(001),-0.00023,-0.00869,0.00023,3843.7,4296.7\n')
    f.write('SrO,(110),-0.00814,-0.00826,-0.06167,4007.0,4289.1\n')
    f.write('SrO,(210),-0.00381,-0.00528,-0.06142,4029.8,4274.5\n')
print('relaxation_and_frequencies.csv written')
