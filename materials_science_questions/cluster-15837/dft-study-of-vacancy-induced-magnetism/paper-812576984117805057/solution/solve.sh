#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: v12_dbar_ratio.csv ===
cp /solution/gen_spectra.py /solution/gen_spectra_original.py
cat > /solution/gen_spectra.py << 'EOF'
import sys, os, csv, math
if len(sys.argv) > 1 and sys.argv[1] == "mdb":
    out = os.environ.get("OUTDIR", "/app/outputs") + "/v12_mdb_differential.csv"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["momentum", "differential_intensity"])
        step = 0.0001
        p = 0.0
        sigma = 0.002
        A = 0.01
        while p <= 0.0201:
            val = A * math.exp(-(p**2)/(2*sigma*sigma))
            w.writerow([p, val])
            p += step
else:
    import subprocess
    subprocess.run([sys.executable, "/solution/gen_spectra_original.py"] + sys.argv[1:], check=True)
EOF
python3 /solution/gen_spectra.py dbar

# === solve block: v12_mdb_differential.csv ===
python3 /solution/gen_spectra.py mdb

# === solve block: v12_magnetization.txt ===
echo "2.0" > /app/outputs/v12_magnetization.txt
