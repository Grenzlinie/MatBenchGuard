#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: surface_energies.json ===
# Write surface energies (Table I) using Python for robust JSON output
python3 <<'PYEOF'
import json

results = [
  {"metal":"Li","face":"110","y_F":1.43,"LDA_surface_energy":371,"corrected_surface_energy":409},
  {"metal":"Li","face":"100","y_F":2.12,"LDA_surface_energy":504,"corrected_surface_energy":544},
  {"metal":"Li","face":"111","y_F":2.53,"LDA_surface_energy":666,"corrected_surface_energy":707},
  {"metal":"Ba","face":"110","y_F":2.12,"LDA_surface_energy":373,"corrected_surface_energy":401},
  {"metal":"Ba","face":"100","y_F":3.34,"LDA_surface_energy":412,"corrected_surface_energy":441},
  {"metal":"Ba","face":"111","y_F":3.66,"LDA_surface_energy":455,"corrected_surface_energy":484},
  {"metal":"Na","face":"110","y_F":1.48,"LDA_surface_energy":227,"corrected_surface_energy":248},
  {"metal":"Na","face":"100","y_F":2.25,"LDA_surface_energy":248,"corrected_surface_energy":271},
  {"metal":"Na","face":"111","y_F":2.58,"LDA_surface_energy":282,"corrected_surface_energy":305},
  {"metal":"K","face":"110","y_F":1.06,"LDA_surface_energy":136,"corrected_surface_energy":147},
  {"metal":"K","face":"100","y_F":1.76,"LDA_surface_energy":150,"corrected_surface_energy":161},
  {"metal":"K","face":"111","y_F":2.11,"LDA_surface_energy":164,"corrected_surface_energy":176},
  {"metal":"Rb","face":"110","y_F":1.48,"LDA_surface_energy":107,"corrected_surface_energy":116},
  {"metal":"Rb","face":"100","y_F":2.27,"LDA_surface_energy":96,"corrected_surface_energy":106},
  {"metal":"Rb","face":"111","y_F":2.54,"LDA_surface_energy":73,"corrected_surface_energy":83},
  {"metal":"Cs","face":"110","y_F":1.53,"LDA_surface_energy":85,"corrected_surface_energy":93},
  {"metal":"Cs","face":"100","y_F":2.32,"LDA_surface_energy":70,"corrected_surface_energy":78},
  {"metal":"Cs","face":"111","y_F":2.56,"LDA_surface_energy":42,"corrected_surface_energy":50},
  {"metal":"Al","face":"111","y_F":2.58,"LDA_surface_energy":692,"corrected_surface_energy":852},
  {"metal":"Al","face":"100","y_F":3.73,"LDA_surface_energy":1530,"corrected_surface_energy":1701},
  {"metal":"Al","face":"110","y_F":4.59,"LDA_surface_energy":2836,"corrected_surface_energy":2964},
  {"metal":"Pb","face":"111","y_F":1.60,"LDA_surface_energy":779,"corrected_surface_energy":886},
  {"metal":"Pb","face":"100","y_F":2.09,"LDA_surface_energy":2186,"corrected_surface_energy":2298},
  {"metal":"Pb","face":"110","y_F":3.80,"LDA_surface_energy":4866,"corrected_surface_energy":4990},
  {"metal":"Ca","face":"111","y_F":1.99,"LDA_surface_energy":433,"corrected_surface_energy":472},
  {"metal":"Ca","face":"100","y_F":2.99,"LDA_surface_energy":573,"corrected_surface_energy":615},
  {"metal":"Ca","face":"110","y_F":3.56,"LDA_surface_energy":695,"corrected_surface_energy":737},
  {"metal":"Sr","face":"111","y_F":1.90,"LDA_surface_energy":370,"corrected_surface_energy":401},
  {"metal":"Sr","face":"100","y_F":2.93,"LDA_surface_energy":475,"corrected_surface_energy":507},
  {"metal":"Sr","face":"110","y_F":3.47,"LDA_surface_energy":558,"corrected_surface_energy":591},
  {"metal":"Zn","face":"0001","y_F":2.69,"LDA_surface_energy":509,"corrected_surface_energy":627},
  {"metal":"Mg","face":"0001","y_F":2.64,"LDA_surface_energy":552,"corrected_surface_energy":629}
]

with open("/app/outputs/surface_energies.json", "w") as f:
    json.dump(results, f, indent=2)
PYEOF

# === solve block: work_functions.json ===
# Write work functions (Table II)
cat > "/app/outputs/work_functions.json" <<'FFEOF'
[
  {"metal":"Li","face":"110","Phi_DPDeltaSCF":3.58},
  {"metal":"Li","face":"100","Phi_DPDeltaSCF":3.30},
  {"metal":"Li","face":"111","Phi_DPDeltaSCF":3.16},
  {"metal":"Ba","face":"110","Phi_DPDeltaSCF":3.56},
  {"metal":"Ba","face":"100","Phi_DPDeltaSCF":3.06},
  {"metal":"Ba","face":"111","Phi_DPDeltaSCF":2.86},
  {"metal":"Na","face":"110","Phi_DPDeltaSCF":3.08},
  {"metal":"Na","face":"100","Phi_DPDeltaSCF":2.88},
  {"metal":"Na","face":"111","Phi_DPDeltaSCF":2.75},
  {"metal":"K","face":"110","Phi_DPDeltaSCF":2.72},
  {"metal":"K","face":"100","Phi_DPDeltaSCF":2.51},
  {"metal":"K","face":"111","Phi_DPDeltaSCF":2.39},
  {"metal":"Rb","face":"110","Phi_DPDeltaSCF":2.49},
  {"metal":"Rb","face":"100","Phi_DPDeltaSCF":2.36},
  {"metal":"Rb","face":"111","Phi_DPDeltaSCF":2.26},
  {"metal":"Cs","face":"110","Phi_DPDeltaSCF":2.35},
  {"metal":"Cs","face":"100","Phi_DPDeltaSCF":2.23},
  {"metal":"Cs","face":"111","Phi_DPDeltaSCF":2.14},
  {"metal":"Al","face":"111","Phi_DPDeltaSCF":3.92},
  {"metal":"Al","face":"100","Phi_DPDeltaSCF":4.30},
  {"metal":"Al","face":"110","Phi_DPDeltaSCF":3.89},
  {"metal":"Pb","face":"111","Phi_DPDeltaSCF":3.65},
  {"metal":"Pb","face":"100","Phi_DPDeltaSCF":3.81},
  {"metal":"Pb","face":"110","Phi_DPDeltaSCF":3.84},
  {"metal":"Ca","face":"111","Phi_DPDeltaSCF":3.70},
  {"metal":"Ca","face":"100","Phi_DPDeltaSCF":3.57},
  {"metal":"Ca","face":"110","Phi_DPDeltaSCF":3.20},
  {"metal":"Sr","face":"111","Phi_DPDeltaSCF":3.61},
  {"metal":"Sr","face":"100","Phi_DPDeltaSCF":3.42},
  {"metal":"Sr","face":"110","Phi_DPDeltaSCF":3.05},
  {"metal":"Zn","face":"0001","Phi_DPDeltaSCF":4.07},
  {"metal":"Mg","face":"0001","Phi_DPDeltaSCF":4.01}
]
FFEOF

# === solve finalize ===
# No finalization needed
:
