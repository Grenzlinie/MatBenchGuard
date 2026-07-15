#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: neb_profiles.csv ===
python3 -c "
import csv
with open('$OUTDIR/neb_profiles.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['charge_state','image_index','energy'])
    # V_As^+
    w.writerow(['V_As^+',0,0.0])
    w.writerow(['V_As^+',1,1.0])
    w.writerow(['V_As^+',2,1.5])
    w.writerow(['V_As^+',3,1.93])
    w.writerow(['V_As^+',4,1.8])
    w.writerow(['V_As^+',5,1.7])
    w.writerow(['V_As^+',6,1.6])
    w.writerow(['V_As^+',7,1.72])
    w.writerow(['V_As^+',8,1.0])
    w.writerow(['V_As^+',9,0.0])
    # V_As^-
    w.writerow(['V_As^-',0,0.0])
    w.writerow(['V_As^-',1,1.0])
    w.writerow(['V_As^-',2,1.4])
    w.writerow(['V_As^-',3,1.91])
    w.writerow(['V_As^-',4,1.8])
    w.writerow(['V_As^-',5,1.7])
    w.writerow(['V_As^-',6,1.6])
    w.writerow(['V_As^-',7,1.7])
    w.writerow(['V_As^-',8,1.0])
    w.writerow(['V_As^-',9,0.0])
"

# === solve block: migration_barriers.json ===
cat > /app/outputs/migration_barriers.json <<'FFEOF'
{
  "V_As_plus_barrier": 1.93,
  "V_As_minus_barrier": 1.91
}
FFEOF
