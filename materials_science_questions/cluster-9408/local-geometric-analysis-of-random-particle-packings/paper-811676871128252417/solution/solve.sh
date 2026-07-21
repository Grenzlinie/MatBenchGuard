#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
python3 /solution/generate_all.py /tmp/output_data.pkl

# === solve block: packing_state.json ===
python3 <<'PYEOF'
import pickle, json
with open('/tmp/output_data.pkl','rb') as f:
    data = pickle.load(f)
with open('/app/outputs/packing_state.json','w') as f:
    json.dump(data['packing_state'], f, indent=2)
PYEOF

# === solve block: mechanical_props.csv ===
python3 <<'PYEOF'
import pickle, csv
with open('/tmp/output_data.pkl','rb') as f:
    data = pickle.load(f)
mech = data['mechanical']
with open('/app/outputs/mechanical_props.csv','w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['relative_density','bulk_modulus','coordination_number','max_interpenetration'])
    for i in range(len(mech['relative_density'])):
        w.writerow([mech['relative_density'][i], mech['bulk_modulus'][i], mech['coordination_number'][i], mech['max_interpenetration'][i]])
PYEOF

# === solve block: voronoi_densities.csv ===
python3 <<'PYEOF'
import pickle, csv
with open('/tmp/output_data.pkl','rb') as f:
    data = pickle.load(f)
with open('/app/outputs/voronoi_densities.csv','w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['local_density'])
    for d in data['local_densities']:
        w.writerow([d])
PYEOF

# === solve block: percolation_threshold.txt ===
python3 <<'PYEOF'
import pickle
with open('/tmp/output_data.pkl','rb') as f:
    data = pickle.load(f)
with open('/app/outputs/percolation_threshold.txt','w') as f:
    f.write(str(data['percolation_threshold']) + '\n')
PYEOF

# === solve block: conductivity_data.csv ===
python3 <<'PYEOF'
import pickle, csv
with open('/tmp/output_data.pkl','rb') as f:
    data = pickle.load(f)
cond = data['conductivity']
with open('/app/outputs/conductivity_data.csv','w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['vf','C_eff'])
    for vf, c in zip(cond['vf'], cond['C_eff']):
        w.writerow([vf, c])
PYEOF

# === solve block: conductivity_fit.json ===
python3 <<'PYEOF'
import pickle, json
with open('/tmp/output_data.pkl','rb') as f:
    data = pickle.load(f)
with open('/app/outputs/conductivity_fit.json','w') as f:
    json.dump(data['fit'], f)
PYEOF
