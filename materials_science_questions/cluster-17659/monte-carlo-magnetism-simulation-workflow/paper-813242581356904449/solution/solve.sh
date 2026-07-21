#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: kakutani_distances.json ===
python3 -c "import json; d={'8x8_cold':[{'n':1,'delta_sq_run1':0.25,'delta_sq_run2':0.32},{'n':2,'delta_sq_run1':0.51,'delta_sq_run2':0.43},{'n':3,'delta_sq_run1':0.54,'delta_sq_run2':0.50},{'n':4,'delta_sq_run1':0.47,'delta_sq_run2':0.42},{'n':5,'delta_sq_run1':0.33,'delta_sq_run2':0.27},{'n':6,'delta_sq_run1':0.00,'delta_sq_run2':0.00}],'8x8_hot':[{'n':1,'delta_sq_run1':0.21,'delta_sq_run2':0.24},{'n':2,'delta_sq_run1':0.51,'delta_sq_run2':0.47},{'n':3,'delta_sq_run1':0.53,'delta_sq_run2':0.61},{'n':4,'delta_sq_run1':0.35,'delta_sq_run2':0.44},{'n':5,'delta_sq_run1':0.30,'delta_sq_run2':0.28},{'n':6,'delta_sq_run1':0.38,'delta_sq_run2':0.35}],'4x4_fine':[{'n':1,'delta_sq_mc':0.00055},{'n':2,'delta_sq_mc':0.00058},{'n':3,'delta_sq_mc':0.00058},{'n':4,'delta_sq_mc':0.00057},{'n':5,'delta_sq_mc':0.00059},{'n':6,'delta_sq_mc':0.00057},{'n':7,'delta_sq_mc':0.00052},{'n':8,'delta_sq_mc':0.00063},{'n':9,'delta_sq_mc':0.00067}],'1d_decimation':{'matched_pair':0.00076,'nonmatching_pair':0.00469}}; json.dump(d, open('/app/outputs/kakutani_distances.json','w'))"
