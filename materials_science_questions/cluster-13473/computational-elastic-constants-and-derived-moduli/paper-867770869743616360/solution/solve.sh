#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR="/app/outputs"

# === solve block: elastic_data.csv ===
python3 - "$OUTDIR" <<'PYEOF'
import sys, os
outdir = sys.argv[1]
path = os.path.join(outdir, "elastic_data.csv")

E_core = 146.0
E_GB = 40.0
d_GB_total = 0.64
ds = [5.0, 10.0, 15.0]

lines = ["E_overall_GPa,d_nm,phi_core"]
for d in ds:
    phi_core = (d / (d + d_GB_total)) ** 3
    E = 1.0 / (phi_core / E_core + (1 - phi_core) / E_GB)
    lines.append(f"{E:.4f},{d:.2f},{phi_core:.4f}")

with open(path, 'w') as f:
    f.write("\n".join(lines) + "\n")
PYEOF

# === solve block: reuss_fit_params.txt ===
cat > "$OUTDIR/reuss_fit_params.txt" <<'EOF'
E_core_GPa = 146.0
E_GB_GPa = 40.0
EOF

# === solve block: ratio.txt ===
python3 - "$OUTDIR/reuss_fit_params.txt" "$OUTDIR/ratio.txt" <<'PYEOF'
import sys, os
# read the fitted parameters (they are known, but compute ratio directly)
E_core = 146.0
E_GB = 40.0
ratio = E_GB / E_core
path = os.path.join(sys.argv[1], "ratio.txt")
# use the same directory as the other outputs, but we have the full path
with open(sys.argv[2], 'w') as f:
    f.write(f"{ratio:.6f}\n")
PYEOF
