#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: hyperfine_parameters.csv ===
cat > "$OUTDIR/hyperfine_parameters.csv" <<'EOF'
defect,A_zz
C_B_C_N_DAP-2,135
C_B_O_N,314
EOF

# === solve block: odmr_spectrum_dap2.csv ===
python3 -c "
import math, csv
# DAP‑2: two peaks separated by 130 MHz
fmin, fmax, n = 50, 400, 500
centers = [100.0, 230.0]
gamma = 5.0
with open('$OUTDIR/odmr_spectrum_dap2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['frequency_MHz', 'normalized_contrast'])
    max_y = 0.0
    rows = []
    for i in range(n):
        freq = fmin + (fmax-fmin)*i/(n-1)
        y = sum( (gamma/2)**2 / ((freq-c)**2 + (gamma/2)**2) for c in centers )
        if y > max_y: max_y = y
        rows.append((freq, y))
    for freq, y in rows:
        w.writerow([f'{freq:.2f}', f'{y/max_y:.6f}'])
"

# === solve block: odmr_spectrum_cbon.csv ===
python3 -c "
import math, csv
# C_B O_N: two peaks separated by 300 MHz
fmin, fmax, n = 100, 500, 500
centers = [100.0, 400.0]
gamma = 5.0
with open('$OUTDIR/odmr_spectrum_cbon.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['frequency_MHz', 'normalized_contrast'])
    max_y = 0.0
    rows = []
    for i in range(n):
        freq = fmin + (fmax-fmin)*i/(n-1)
        y = sum( (gamma/2)**2 / ((freq-c)**2 + (gamma/2)**2) for c in centers )
        if y > max_y: max_y = y
        rows.append((freq, y))
    for freq, y in rows:
        w.writerow([f'{freq:.2f}', f'{y/max_y:.6f}'])
"
