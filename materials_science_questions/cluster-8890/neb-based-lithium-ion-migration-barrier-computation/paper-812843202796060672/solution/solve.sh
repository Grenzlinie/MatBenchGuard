#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dipole_evidence.json ===
cat > /app/outputs/dipole_evidence.json <<'FFEOF'
{
  "dipole_moments": {
    "SLM": {
      "x=0": -1.61,
      "x=1": 0.78,
      "x=2": -0.03
    },
    "DLM": {
      "x=0": -2.99,
      "x=1": -1.88,
      "x=2": 0.53
    }
  }
}
FFEOF

# === solve block: migration_barriers.json ===
cat > /app/outputs/migration_barriers.json <<'FFEOF'
{
  "barriers": {
    "slm_Li_ion_S_layer": 0.29,
    "slm_Li_ion_Se_layer": 0.24,
    "slm_Li_vacancy_S_layer": 0.44,
    "slm_Li_vacancy_Se_layer": 0.34,
    "dlm_Li_ion_S_layer": 0.28,
    "dlm_Li_ion_middle_layer": 0.43,
    "dlm_Li_ion_Se_layer": 0.23,
    "dlm_Li_vacancy_S_layer": 0.42,
    "dlm_Li_vacancy_middle_layer": 0.36,
    "dlm_Li_vacancy_Se_layer": 0.31
  }
}
FFEOF
