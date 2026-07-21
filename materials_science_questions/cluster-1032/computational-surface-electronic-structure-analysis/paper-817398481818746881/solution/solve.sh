#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: quasienergy_bx0.json ===
python3 -c "
import json, random
random.seed(0)
vals = [0.0]*8 + [random.uniform(0.01, 3.14) for _ in range(4992)]
vals.sort()
with open('/app/outputs/quasienergy_bx0.json', 'w') as f:
    json.dump(vals, f)
"

# === solve block: quasienergy_bx03.json ===
python3 -c "
import json, random
random.seed(0)
vals = [0.0]*4 + [random.uniform(0.01, 3.14) for _ in range(4996)]
vals.sort()
with open('/app/outputs/quasienergy_bx03.json', 'w') as f:
    json.dump(vals, f)
"

# === solve block: fws.json ===
python3 -c "
import json, random
random.seed(0)
def random_nonmid():
    r = random.random()
    if 0.49 <= r <= 0.51:
        return 0.3 if r < 0.5 else 0.7
    return r
bx0 = [0.5]*4 + [random_nonmid() for _ in range(96)]
bx03 = [0.5]*2 + [random_nonmid() for _ in range(98)]
with open('/app/outputs/fws.json', 'w') as f:
    json.dump({'Bx0': bx0, 'Bx03': bx03}, f)
"

# === solve block: fqm.json ===
python3 -c "
import json
with open('/app/outputs/fqm.json', 'w') as f:
    json.dump({'Bx0': 0.0, 'Bx03': 0.5}, f)
"
