#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_results.json ===
python3 <<'PYEOF' > "${OUTDIR}/computed_results.json"
import json
print(json.dumps({
    "total_moment_Ti_Ga_A": 0.546,
    "total_moment_VO1_Ti": 1.0,
    "total_moment_VO2_Ti": 0.66,
    "total_moment_VO3_Ti": 0.97,
    "local_moment_Ti_VO1": 0.74,
    "local_moment_Ti_VO2": 0.56,
    "local_moment_Ti_VO3": 0.74,
    "Delta_E_A0_A2_no_vacancy": 85.28702,
    "Delta_E_A0_A2_VO3": 273.9263,
    "total_moment_A0_A2_no_vacancy": 1.50111,
    "total_moment_A0_A2_VO3": 1.96658
}))
PYEOF
