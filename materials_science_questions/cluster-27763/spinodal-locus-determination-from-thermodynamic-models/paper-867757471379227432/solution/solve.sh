#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: zero_sound_velocity.json ===
cat > "$OUTDIR/zero_sound_velocity.json" <<'JSONEOF'
{
  "c0_spinodal_mps": 80.0,
  "c1_spinodal_mps": 0.0,
  "Fermi_velocity_mps": 80.0
}
JSONEOF

# === solve block: critical_radius_scaling.csv ===
python3 <<'PYEOF'
import csv, math

# Known: Rc = 10 nm at deltap = 0.02 mbar, power law exponent -0.25
# So Rc(deltap) = A * deltap**(-0.25)
# A = 10 * 0.02**0.25
A = 10.0 * (0.02 ** 0.25)

# Generate points: deltap in mbar, Rc in nm
delta_ps = [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.5, 1.0]
rows = []
for dp in delta_ps:
    rc = A * (dp ** (-0.25))
    rows.append((dp, round(rc, 3)))

# Write CSV
with open('/app/outputs/critical_radius_scaling.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['pressure_offset_mbar', 'critical_radius_nm'])
    for dp, rc in rows:
        writer.writerow([dp, rc])
PYEOF
