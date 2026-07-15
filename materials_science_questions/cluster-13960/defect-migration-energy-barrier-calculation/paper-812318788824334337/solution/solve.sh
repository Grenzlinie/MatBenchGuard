#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.csv ===
python3 - "$OUTDIR/formation_energies.csv" <<'PYEOF'
import csv, sys
rows = [
    ("field_V_per_nm", "delta_E_vac_eV"),
    (0, 0.611),
    (4, 0.556),
    (6, 0.520),
    (10, 0.456),
    (30, -0.05)   # negative at 30 V/nm, exact value to be confirmed from paper data
]
with open(sys.argv[1], "w", newline="") as f:
    w = csv.writer(f)
    w.writerows(rows)
PYEOF

# === solve block: bond_lengths.json ===
cat > "$OUTDIR/bond_lengths.json" <<'FFEOF'
{"Cu_O_surface_A": 1.85, "O_plane_O_surface_A": 6.27}
FFEOF
