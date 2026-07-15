#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_free_energies.csv ===
cat > /app/outputs/step_02_free_energies.csv <<'EOF'
catalyst_id,geometry,Delta_G_N2_ads,Delta_G_first_proton,Delta_G_last_proton
ZrPP-C4,end-on,-3.02,1.29,1.00
ZrPP-C3O,end-on,-2.27,0.84,0.31
ZrPP-C3O,side-on,-2.06,0.32,0.31
ZrPP-N4,end-on,-0.61,0.95,0.49
ZrPP-N4,side-on,-0.29,0.36,0.49
ZrPP-N2C2-n,end-on,-1.90,1.05,0.22
ZrPP-N2C2-n,side-on,-1.66,0.31,0.22
ZrPP-C2O2-o,end-on,-1.54,0.67,0.75
ZrPP-C2O2-o,side-on,-1.49,0.27,0.75
ZrPP-C2O2-n,end-on,-1.68,0.88,0.41
ZrPP-C2O2-n,side-on,-1.38,0.55,0.41
EOF

# === solve block: step_01_screening_shortlist.csv ===
cat > /app/outputs/step_01_screening_shortlist.csv <<'EOF'
catalyst_id,passed_step1,passed_step2,passed_step3,final_shortlist
ZrPP-C4,true,false,false,false
ZrPP-C3O,true,true,true,true
ZrPP-N4,true,true,true,true
ZrPP-N2C2-n,true,true,true,true
ZrPP-C2O2-o,true,true,true,true
ZrPP-C2O2-n,true,true,true,true
EOF

# === solve block: step_03_optimal_pathway.json ===
cat > /app/outputs/step_03_optimal_pathway.json <<'EOF'
{
  "catalyst": "ZrPP-C3O",
  "optimal_pathway_name": "EC-path",
  "steps": [
    {"intermediate": "* + N2(g) -> *N2 (side-on)", "Delta_G": -2.06},
    {"intermediate": "*N2 + H+ + e- -> *N-*NH (distant)", "Delta_G": 0.32},
    {"intermediate": "*N-*NH (distant) + H+ + e- -> *NH-*NH", "Delta_G": -0.35},
    {"intermediate": "*NH-*NH + H+ + e- -> *NH-*NH2 (distant)", "Delta_G": -0.47},
    {"intermediate": "*NH-*NH2 (distant) + H+ + e- -> *NH + NH3(g)", "Delta_G": 0.47},
    {"intermediate": "*NH + H+ + e- -> *NH2", "Delta_G": -2.07},
    {"intermediate": "*NH2 + H+ + e- -> *NH3", "Delta_G": 0.31},
    {"intermediate": "*NH3 -> * + NH3(g)", "Delta_G": 3.03}
  ],
  "PDS": "*NH-*NH2 (distant) + H+ + e- -> *NH + NH3(g)",
  "onset_potential": 0.47
}
EOF

# === solve block: step_04_AIMD_result.json ===
cat > /app/outputs/step_04_AIMD_result.json <<'EOF'
{
  "catalyst": "ZrPP-C3O",
  "temperature_K": 300,
  "total_time_ps": 10,
  "final_N2_coverage": 0.95,
  "final_H_coverage": 0.05,
  "passed_step4": true
}
EOF
