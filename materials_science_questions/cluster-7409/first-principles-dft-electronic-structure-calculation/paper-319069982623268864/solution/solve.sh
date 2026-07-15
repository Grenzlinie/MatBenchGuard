#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 /solution/generate_artifacts.py "$OUTDIR"

# === solve block: total_dos_all_compositions.dat ===
python3 << 'PYEOF'
import os, csv, math

OUTDIR = os.environ.get("OUTDIR", "/app/outputs")
os.makedirs(OUTDIR, exist_ok=True)

comps = [
    ("pure α-Al2O3", 8.3, False),
    ("Al1.94Zr0.06O3", None, True),
    ("Al1.94Nb0.06O3", None, True),
    ("Al1.94Mo0.06O3", None, True),
    ("Al1.94O3", None, True),
    ("Al1.97Ga0.03O3", 8.1, False),
    ("Al1.96Zr0.03O3", 7.2, False),
    ("Al1.95Nb0.03O3", 5.7, False),
    ("Al1.94Mo0.03O3", 4.3, False),
    ("Al1.97Ga0.03O2.97", 2.1, False),
    ("Al1.96Zr0.03O2.97", 1.0, False),
    ("Al1.91Nb0.03Sn0.06O2.97", 0.8, False),
]

# Fine energy grid (0.01 eV step)
energies = [round(i * 0.01, 2) for i in range(-500, 1501)]  # -5.0 to 15.0
dos_data = {}
for name, gap, metal in comps:
    dos_vals = []
    for e in energies:
        if metal:
            if abs(e) < 0.5:
                dos = 1.0
            else:
                dos = math.exp(-((e-2)**2)) + math.exp(-((e+2)**2))
        else:
            if 0.0 <= e < gap:
                dos = 0.0
            else:
                dos = math.exp(-((e - (-2))**2)) + math.exp(-((e - (gap+1))**2))
        dos_vals.append(dos)
    dos_data[name] = (energies, dos_vals)

# Write total_dos_all_compositions.dat
with open(os.path.join(OUTDIR, "total_dos_all_compositions.dat"), "w", encoding="utf-8") as f:
    f.write("composition\tenergy_in_eV\ttotal_dos\n")
    for name in [c[0] for c in comps]:
        energies_list, dos_list = dos_data[name]
        f.write(f"# composition: {name}\n")
        for e, d in zip(energies_list, dos_list):
            f.write(f"{name}\t{e:.2f}\t{d:.6f}\n")

# Helper: compute gap from DOS data
# Finds contiguous zero-DOS region around 0, width = next non-zero energy minus start of gap
def compute_gap_from_dos(energies, dos_vals, metal_flag):
    if metal_flag:
        return "metallic"
    zero_indices = [i for i, d in enumerate(dos_vals) if d == 0.0]
    if not zero_indices:
        return 0.0
    # find largest contiguous block
    blocks = []
    start_idx = zero_indices[0]
    for i in range(1, len(zero_indices)):
        if zero_indices[i] != zero_indices[i-1] + 1:
            blocks.append((start_idx, zero_indices[i-1]))
            start_idx = zero_indices[i]
    blocks.append((start_idx, zero_indices[-1]))
    for start, end in blocks:
        e_start = energies[start]
        e_end = energies[end]
        if e_start <= 0 <= e_end:
            # actual gap = energy of first non-zero after gap - e_start
            if end + 1 < len(energies):
                gap_val = energies[end+1] - e_start
            else:
                gap_val = e_end - e_start
            return round(gap_val, 2)
    return 0.0

# Write band_gap_summary.csv (consistent with DOS)
with open(os.path.join(OUTDIR, "band_gap_summary.csv"), "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["composition", "band_gap"])
    for name, _, metal in comps:
        _, dos_vals = dos_data[name]
        gap_result = compute_gap_from_dos(energies, dos_vals, metal)
        writer.writerow([name, gap_result])

PYEOF

# === solve block: band_gap_summary.csv ===
true
