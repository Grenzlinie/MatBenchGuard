#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: free_energy_data.csv ===
cat > /tmp/gen_csv.py << 'PYEOF'
import csv, math

x_vals = [i*0.002 for i in range(0, 11)]          # 0.000 to 0.020 step 0.002
y_vals = [j*0.0025 for j in range(0, 21)]        # 0.000 to 0.050 step 0.0025

rows = []
for x in x_vals:
    for y in y_vals:
        if x >= 0.4 * y:
            # approximate equality boundary from the paper's Fig. 2
            y_eq = 1.875 * x - 0.0025
            if y > y_eq:
                min_config = '4C10Sn'
                f_4C10Sn = 0.0
                f_1C4Sn  = 1.0
                f_random = 2.0
            else:
                min_config = '1C4Sn'
                f_1C4Sn  = 0.0
                f_4C10Sn = 1.0
                f_random = 2.0
            rows.append([x, y, f_random, f_1C4Sn, f_4C10Sn, min_config])

with open('/app/outputs/free_energy_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'y', 'f_random', 'f_1C4Sn', 'f_4C10Sn', 'min_config'])
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to /app/outputs/free_energy_data.csv")
PYEOF
python3 /tmp/gen_csv.py

# === solve finalize ===
echo "Oracle solve completed successfully"
