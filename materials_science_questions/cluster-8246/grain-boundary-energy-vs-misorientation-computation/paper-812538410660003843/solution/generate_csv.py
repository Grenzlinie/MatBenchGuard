import sys, csv
from pathlib import Path

# Output file path
out_path = sys.argv[1]

# Data extracted from Tables I, II, III
# Each entry: condition, n_O, config_type (LE/HE), seg_energy_eV
rows = []

# --- Pristine (Table I) ---
# HE:      n=1:0.049, 2:0.499, 3:0.947, 4:0.325
# LE:      n=1:-0.030, 2:-0.039, 3:-0.078, 4:-0.085
pristine_he = [0.049, 0.499, 0.947, 0.325]
pristine_le = [-0.030, -0.039, -0.078, -0.085]
for n, val in enumerate(pristine_le, start=1):
    rows.append(('pristine', n, 'LE', val))
for n, val in enumerate(pristine_he, start=1):
    rows.append(('pristine', n, 'HE', val))

# --- Local strain LS_+3.7% (Table II, single configuration per n) ---
ls37 = {1:-1.589, 2:-2.602, 3:-3.334, 4:-3.984}
for n, val in ls37.items():
    rows.append(('LS_+3.7%', n, 'LE', val))
    rows.append(('LS_+3.7%', n, 'HE', val))

# --- Local strain LS_+5.7% ---
ls57 = {1:-1.607, 2:-2.482, 3:-3.353, 4:-3.999}
for n, val in ls57.items():
    rows.append(('LS_+5.7%', n, 'LE', val))
    rows.append(('LS_+5.7%', n, 'HE', val))

# --- Global strain GS_+3.0% ---
gs30 = {1:-0.426, 2:-0.626, 3:-0.781, 4:-0.768}
for n, val in gs30.items():
    rows.append(('GS_+3.0%', n, 'LE', val))
    rows.append(('GS_+3.0%', n, 'HE', val))

# --- Global strain GS_+0.5% ---
gs05 = {1:-0.080, 2:-0.120, 3:-0.153, 4:-0.150}
for n, val in gs05.items():
    rows.append(('GS_+0.5%', n, 'LE', val))
    rows.append(('GS_+0.5%', n, 'HE', val))

# --- Global strain GS_-0.5% ---
gsm05 = {1:0.086, 2:0.129, 3:0.166, 4:0.163}
for n, val in gsm05.items():
    rows.append(('GS_-0.5%', n, 'LE', val))
    rows.append(('GS_-0.5%', n, 'HE', val))

# --- Global strain GS_-3.0% ---
gsm30 = {1:0.579, 2:0.884, 3:1.154, 4:1.135}
for n, val in gsm30.items():
    rows.append(('GS_-3.0%', n, 'LE', val))
    rows.append(('GS_-3.0%', n, 'HE', val))

# --- Vacancy V1 (Table III) ---
# LE: n=1:-1.933, 2:-2.671, 3:-2.839, 4:-3.073
# HE: n=1:0.075, 2:-0.091, 3:0.766, 4:-0.985
v1_le = {1:-1.933, 2:-2.671, 3:-2.839, 4:-3.073}
v1_he = {1:0.075, 2:-0.091, 3:0.766, 4:-0.985}
for n, val in v1_le.items():
    rows.append(('V1', n, 'LE', val))
for n, val in v1_he.items():
    rows.append(('V1', n, 'HE', val))

# --- Vacancy V2 ---
# LE: n=1:-1.908, 2:-2.634, 3:-2.824, 4:-3.408
# HE: n=1:0.080, 2:-0.179, 3:-0.865, 4:-1.076
v2_le = {1:-1.908, 2:-2.634, 3:-2.824, 4:-3.408}
v2_he = {1:0.080, 2:-0.179, 3:-0.865, 4:-1.076}
for n, val in v2_le.items():
    rows.append(('V2', n, 'LE', val))
for n, val in v2_he.items():
    rows.append(('V2', n, 'HE', val))

# Write CSV
with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['condition', 'config_type', 'n_O', 'seg_energy_eV'])
    writer.writerows(rows)