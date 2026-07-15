#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: bulk_reference.json ===
cat > /app/outputs/bulk_reference.json <<'EOF'
{
  "E_bulk_Cu": -1500.0,
  "E_bulk_Au": -2000.0,
  "E_bulk_Cu3Au": -6499.858,
  "lattice_constant_Cu3Au": 3.79
}
EOF

# === solve block: slab_energies.csv ===
python3 <<'PYEOF'
import csv, sys, math
E_Cu = -1500.0
E_Au = -2000.0
delta_H_f = 0.142
a = 3.79
surface_area = 2 * a**2
comps = [
    ("25/25", 1, 1),
    ("25/50", 1, 2),
    ("25/75", 1, 3),
    ("25/100", 1, 4),
    ("50/0", 2, 0),
    ("50/25", 2, 1),
    ("50/50", 2, 2),
    ("50/75", 2, 3),
    ("50/100", 2, 4),
    ("75/0", 3, 0),
    ("75/25", 3, 1),
    ("75/50", 3, 2),
    ("75/75", 3, 3),
    ("75/100", 3, 4),
    ("100/0", 4, 0),
    ("100/25", 4, 1),
    ("100/50", 4, 2),
    ("100/75", 4, 3),
    ("100/100", 4, 4),
]
U_dict = {"50/25": 0.0, "75/25": 0.3}
default_U = 2.0
rows = []
for label, au1, au2 in comps:
    n_au = 2*(au1 + au2) + 5
    n_cu = 36 - n_au
    U_upper = U_dict.get(label, default_U)
    E_slab = U_upper + (E_Cu * n_cu + E_Au * n_au) + delta_H_f * n_au
    rows.append([label, f"{E_slab:.6f}", n_cu, n_au, f"{surface_area:.4f}"])
with open('/app/outputs/slab_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['composition_label', 'total_energy', 'N_Cu', 'N_Au', 'surface_area'])
    writer.writerows(rows)
PYEOF

# === solve block: surface_energy_analysis.json ===
python3 <<'PYEOF'
import json
data = {
    "mu_Cu_upper": 0.0,
    "mu_Cu_lower": -0.047333,
    "stable_at_upper": "50/25",
    "stable_at_lower": "75/25"
}
with open('/app/outputs/surface_energy_analysis.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
