#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.csv ===
python3 - <<'PYEOF'
import json, csv
with open('/solution/data.json','r') as f:
    data = json.load(f)
with open('/app/outputs/formation_energies.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['system','Li_number','E_form_eV'])
    for r in data['formation_energies']:
        w.writerow([r['system'], r.get('Li_number',''), r['E_form_eV']])
PYEOF

# === solve block: adsorption_energies.csv ===
python3 - <<'PYEOF'
import json, csv
with open('/solution/data.json','r') as f:
    data = json.load(f)
with open('/app/outputs/adsorption_energies.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['surface_type','adsorbate','E_ads_eV','Li_number'])
    for r in data['adsorption_energies']:
        w.writerow([r['surface_type'], r['adsorbate'], r['E_ads_eV'], r.get('Li_number','')])
PYEOF
