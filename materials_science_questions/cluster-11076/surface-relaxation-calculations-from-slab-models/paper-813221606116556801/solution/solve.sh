#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: bulk_lattice_constant.txt ===
echo "3.87" > "$OUTDIR/bulk_lattice_constant.txt"

# === solve block: surface_energies.json ===
python3 << 'PYEOF'
import json, os
out = {"SrO_terminated": 1.20, "TiO2_terminated": 1.09}
with open(os.path.join(os.environ["OUTDIR"], "surface_energies.json"), "w") as f:
  json.dump(out, f)
PYEOF

# === solve block: atomic_displacements.csv ===
python3 << 'PYEOF'
import csv, os
rows = [
  ("SrO", "Sr(9)", -0.32),
  ("SrO", "O(10)", -0.02),
  ("SrO", "Ti(5)", 0.02),
  ("SrO", "O(7)", 0.05),
  ("SrO", "Sr(6)", -0.10),
  ("TiO2", "Ti(1)", -0.13),
  ("TiO2", "O(3)", 0.00),
  ("TiO2", "Sr(2)", 0.10),
  ("TiO2", "O(4)", -0.03),
]
path = os.path.join(os.environ["OUTDIR"], "atomic_displacements.csv")
with open(path, "w", newline="") as f:
  w = csv.writer(f)
  w.writerow(["termination", "atom_label", "displacement_A"])
  for row in rows:
    w.writerow(row)
PYEOF

# === solve block: charge_transfers.csv ===
python3 << 'PYEOF'
import csv, os
rows = [
  ("SrO", "Sr(9)", 0.05),
  ("SrO", "O(10)", 0.0),
  ("SrO", "Ti(5)", -0.04),
  ("SrO", "O(7)", -0.03),
  ("TiO2", "Ti(1)", -0.18),
  ("TiO2", "O(3)", 0.14),
  ("TiO2", "Sr(2)", -0.03),
  ("TiO2", "O(4)", -0.03),
]
path = os.path.join(os.environ["OUTDIR"], "charge_transfers.csv")
with open(path, "w", newline="") as f:
  w = csv.writer(f)
  w.writerow(["termination", "atom_label", "charge_transfer"])
  for row in rows:
    w.writerow(row)
PYEOF
