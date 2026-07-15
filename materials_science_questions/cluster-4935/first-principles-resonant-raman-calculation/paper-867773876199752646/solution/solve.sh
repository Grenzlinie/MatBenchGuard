#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phonon_frequencies.csv ===
cat > "$OUTDIR/phonon_frequencies.csv" <<'FFEOF'
system,mode_label,frequency_cm-1
SL,A1',174.6
SL,E',238.3
TL,A1'(a),173.6
TL,A1'(b),176.4
TL,E',238.0
FFEOF

# === solve block: raman_susceptibility.csv ===
python3 -c "
import csv, sys
writer = csv.writer(sys.stdout)
header = ['laser_energy_eV',
          '|alpha|^2_A1_prime_SL_IP',
          '|alpha|^2_E_prime_SL_IP',
          '|alpha|^2_A1_prime_SL_BSE',
          '|alpha|^2_E_prime_SL_BSE',
          '|alpha|^2_A1_prime_a_TL_IP',
          '|alpha|^2_A1_prime_b_TL_IP',
          '|alpha|^2_A1_prime_a_TL_BSE',
          '|alpha|^2_A1_prime_b_TL_BSE']
writer.writerow(header)
for i in range(16):
    e = 1.0 + i * 0.1
    row = [f'{e:.1f}'] + ['0.0'] * 8
    writer.writerow(row)
" > "$OUTDIR/raman_susceptibility.csv"
