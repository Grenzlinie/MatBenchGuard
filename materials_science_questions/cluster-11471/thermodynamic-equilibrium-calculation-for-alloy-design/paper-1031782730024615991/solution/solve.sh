#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: table_ternary_coefficients.json ===
python3 -c "import json; d={'T0_gamma':[1639.0,-49.652,2.7506],'mC_gamma':[-112.21,6.0457,-0.51415],'T0_gra':[-503.34,196.46,-11.368],'mC_gra':[382.24,-19.408,1.6522]}; json.dump(d,open('/app/outputs/table_ternary_coefficients.json','w'))"

# === solve block: table_alloy_coefficients.json ===
python3 -c "import json; d={'T0_gamma_alloy':{'const':1639.0,'Si':-49.652,'Si2':2.7506,'Cu':-26.531,'Cu_Si':11.571,'Cu_Si2':-1.6962,'Mn':-5.88,'Mn_Si':0.12,'Cr':6.0,'P':-48.0},'mC_gamma_alloy':{'const':-112.21,'Si':6.0457,'Si2':-0.51415,'Cu':5.4439,'Cu_Si':-2.979,'Cu_Si2':0.59873},'T0_gra_alloy':{'const':-503.34,'Si':196.46,'Si2':-11.368,'Cu':22.3,'Mn':-6.6,'Cr':-26.0,'P':78.4}}; json.dump(d,open('/app/outputs/table_alloy_coefficients.json','w'))"

# === solve block: eutectic_relation.json ===
python3 -c "import json; d={'numerator_coefficients':[1,-0.1149,0.0066,-0.0228,0.0054036,-0.00079116,0.0003,0.00004998,0.0149,-0.059],'denominator_coefficients':[1,-0.0515,0.0044,-0.0110,0.0060192,-0.00121]}; json.dump(d,open('/app/outputs/eutectic_relation.json','w'))"

# === solve block: ce_approximation.json ===
python3 -c "import json; d={'wC_eut_approx':[4.339,-0.291,0.004,-0.05,0.07,-0.276],'CE_approx':[0.291,-0.004,0.05,-0.07,0.276]}; json.dump(d,open('/app/outputs/ce_approximation.json','w'))"

# === solve block: partition_coefficient.json ===
python3 -c "import json; d={'k_C':{'const':0.4625,'Si':-0.0165,'dT':0.000186,'Si_dT':4.08e-05,'dT2':-6.8e-07},'k_Si':{'const':1.0729,'Si':-0.0212,'dT':0.0031,'Si_dT':-0.0004},'k_Cu':{'const':1.1336,'Si':0.12145,'dT':0.000963,'Si_dT':0.00087},'k_Mn':{'const':0.557,'Si':0.047,'dT':-0.00026,'Si2_dT':9e-06},'k_Cr':{'const':0.9146,'dT':-0.0007},'k_P':{'const':0.0982,'dT':-0.00035}}; json.dump(d,open('/app/outputs/partition_coefficient.json','w'))"
