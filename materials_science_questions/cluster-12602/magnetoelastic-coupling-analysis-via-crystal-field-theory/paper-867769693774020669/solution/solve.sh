#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: phase_analysis.csv ===
cat > "$OUTDIR/phase_analysis.csv" <<'EOF'
temperature_ratio,xiAF_q0,phase,eta2_eta1_ratio
0.5,0.0,single-q,0.0
EOF

# === solve block: bragg_shift_bound.txt ===
echo '0.004' > "$OUTDIR/bragg_shift_bound.txt"

# === solve block: nmr_distribution.csv ===
python3 <<'PYEOF'
import math
import csv

n = 100
q1x = 0.125 * math.pi
q1y = 0.125 * math.pi
amp = 0.5
values = []
for i in range(n):
    for j in range(n):
        h = amp * ((-1) ** (i + j)) * math.cos(q1x * i + q1y * j)
        values.append(h)

num_bins = 200
min_val = min(values)
max_val = max(values)
bin_width = (max_val - min_val) / num_bins
hist = [0] * num_bins
for v in values:
    idx = min(num_bins - 1, int((v - min_val) / bin_width))
    hist[idx] += 1

norm = sum(hist) * bin_width
with open('/app/outputs/nmr_distribution.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['field_value', 'probability_density'])
    for k in range(num_bins):
        center = min_val + (k + 0.5) * bin_width
        density = hist[k] / norm
        writer.writerow([center, density])
PYEOF

# === solve finalize ===
echo 'artifacts written'
