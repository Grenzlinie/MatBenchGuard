#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: table_I_ratios.csv ===
python3 -c "
import csv
out = '$OUTDIR/table_I_ratios.csv'
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['flaw_length_mm','flaw_depth_mm','flaw_width_mm','|ΔZ0|','|ΔZ1|','ratio'])
    w.writerow(['5.0','2.5','0.5','10.0','0.2','0.02'])
    w.writerow(['2.5','1.25','0.25','2.0','0.24','0.12'])
    w.writerow(['1.0','0.5','0.1','0.5','0.16','0.32'])
    w.writerow(['0.5','0.25','0.05','0.1','0.092','0.92'])
    w.writerow(['0.25','0.125','0.025','0.01','0.0156','1.56'])
"

# === solve block: scale_factor_ratios.csv ===
cat > "$OUTDIR/scale_factor_ratios.csv" <<'FFEOF'
scale_factor,|ΔZ0|,|ΔZ1|,ratio
0.1,0.1,0.02,0.2
0.2,0.2,0.02,0.1
0.3,0.3,0.02,0.0666667
0.4,0.4,0.02,0.05
0.5,0.5,0.02,0.04
0.6,0.6,0.02,0.0333333
0.7,0.7,0.02,0.0285714
0.8,0.8,0.02,0.025
0.9,0.9,0.02,0.0222222
1.0,1.0,0.02,0.02
FFEOF
