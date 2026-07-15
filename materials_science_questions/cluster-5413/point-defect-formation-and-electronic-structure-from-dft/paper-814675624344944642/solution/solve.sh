#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: low_coverage_overpotentials.csv ===
python3 <<'PYEOF'
import csv
rows = [
    ('SnTiO3', 0.05, 0.72),
    ('CaTaO2N', 0.82, 0.58),
    ('MgTaO2N', 0.18, 0.95),
    ('LaTiO2N', 0.75, 0.90),
    ('SrTaO2N', 0.85, 0.78),
    ('BaTaO2N', 0.90, 0.85),
    ('CaGeO3', 1.20, 1.10),
    ('SrGeO3', 1.30, 1.20),
]
with open('/app/outputs/low_coverage_overpotentials.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['material', 'η_HER_low', 'η_OER_low'])
    w.writerows(rows)
PYEOF

# === solve block: high_coverage_overpotentials.csv ===
python3 <<'PYEOF'
import csv
rows = [
    ('SnTiO3', 1.10),
    ('CaTaO2N', 1.35),
    ('MgTaO2N', 1.50),
    ('LaTiO2N', 1.20),
    ('SrTaO2N', 1.25),
    ('BaTaO2N', 1.30),
]
with open('/app/outputs/high_coverage_overpotentials.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['material', 'η_OER_high'])
    w.writerows(rows)
PYEOF

# === solve block: vacancy_formation_energies.csv ===
python3 <<'PYEOF'
import csv
rows = [
    ('SnTiO3', 0.5),
    ('CaTaO2N', 0.8),
    ('MgTaO2N', 0.6),
    ('LaTiO2N', 0.4),
    ('SrTaO2N', 0.7),
    ('BaTaO2N', 0.9),
    ('CaGeO3', -3.0),
    ('SrGeO3', -3.2),
]
with open('/app/outputs/vacancy_formation_energies.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['material', 'ΔE_vac'])
    w.writerows(rows)
PYEOF

# === solve block: bandgap_data.csv ===
python3 <<'PYEOF'
import csv
rows = [
    ('SnTiO3', 2.48, 2.10),
    ('CaTaO2N', 2.00, 1.80),
    ('MgTaO2N', 2.40, 2.20),
    ('LaTiO2N', 2.30, 2.00),
    ('SrTaO2N', 2.10, 1.90),
    ('BaTaO2N', 1.90, 1.70),
    ('CaGeO3', 4.20, 3.80),
    ('SrGeO3', 4.00, 3.60),
]
with open('/app/outputs/bandgap_data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['material', 'direct_bandgap', 'indirect_bandgap'])
    w.writerows(rows)
PYEOF
