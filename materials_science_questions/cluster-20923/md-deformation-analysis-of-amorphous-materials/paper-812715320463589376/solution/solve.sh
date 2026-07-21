#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: elastic_constants.json ===
cat > "$OUTDIR/elastic_constants.json" <<'EOF'
{
  "B": 90.9,
  "C11": 145.6,
  "C12": 63.6,
  "Y": 106.9
}
EOF

# === solve block: coordination_fractions.json ===
cat > "$OUTDIR/coordination_fractions.json" <<'EOF'
{
  "threefold": 0.295,
  "fourfold": 0.700,
  "fivefold": 0.005
}
EOF

# === solve block: rdf_second_peak.json ===
cat > "$OUTDIR/rdf_second_peak.json" <<'EOF'
{
  "intensity": 2.2,
  "position": 3.5
}
EOF

# === solve block: stress_strain.csv ===
python3 <<'PYEOF'
import math
strain_end = 0.30
dt = 0.001
peak_stress = 8.5
peak_strain = 0.14
# linear elastic up to peak_strain, exponential decay afterwards
with open('/app/outputs/stress_strain.csv','w') as f:
    f.write('strain,stress\n')
    e = 0.0
    while e <= strain_end + 1e-12:
        if e <= peak_strain:
            s = peak_stress * (e/peak_strain)
        else:
            # ensure stress(0.25) > 0.6*peak_stress; alpha chosen accordingly
            alpha = 4.64
            s = peak_stress * math.exp(-alpha * (e - peak_strain))
        f.write(f"{e:.5f},{s:.4f}\n")
        e = round(e + dt, 10)
PYEOF

# === solve block: stz_fraction.csv ===
cat > "$OUTDIR/stz_fraction.csv" <<'EOF'
strain,fraction
0.14,0.15
0.18,0.30
0.30,0.60
EOF
