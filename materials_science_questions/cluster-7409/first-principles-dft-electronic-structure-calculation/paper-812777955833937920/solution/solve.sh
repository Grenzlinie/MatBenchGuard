#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "single_ni_magnetic_moment": 2.0,
  "table1": [
    {"config": "Ni_{Sn5cI} and Ni_{Sn5cI}", "ni_ni_distance": 3.13, "delta_E": 145, "m_tot": 3.6, "coupling": "FM"},
    {"config": "Ni_{Sn5cI} and Ni_{Sn5cII}", "ni_ni_distance": 6.78, "delta_E": 32, "m_tot": 3.6, "coupling": "FM"},
    {"config": "Ni_{Sn5cI} and Ni_{Sn5cIII}", "ni_ni_distance": 7.47, "delta_E": -41, "m_tot": 0, "coupling": "AFM"},
    {"config": "Ni_{Sn6cI} and Ni_{Sn6cI}", "ni_ni_distance": 3.13, "delta_E": -64, "m_tot": 0, "coupling": "AFM"},
    {"config": "Ni_{Sn6cI} and Ni_{Sn6cII}", "ni_ni_distance": 6.78, "delta_E": 16, "m_tot": 4, "coupling": "FM"},
    {"config": "Ni_{Sn6cI} and Ni_{Sn6cIII}", "ni_ni_distance": 7.47, "delta_E": 33, "m_tot": 3.6, "coupling": "FM"}
  ],
  "table2": [
    {"case": "Case (1)", "ni_ni_distance": 3.14, "delta_E": 102, "m_tot": 4, "coupling": "FM"},
    {"case": "Case (2)", "ni_ni_distance": 6.79, "delta_E": -30, "m_tot": 0, "coupling": "AFM"},
    {"case": "Case (3)", "ni_ni_distance": 7.49, "delta_E": -33, "m_tot": 0, "coupling": "AFM"},
    {"case": "Case (4)", "ni_ni_distance": 3.14, "delta_E": -91, "m_tot": 0, "coupling": "AFM"},
    {"case": "Case (5)", "ni_ni_distance": 6.79, "delta_E": -13, "m_tot": 0, "coupling": "AFM"},
    {"case": "Case (6)", "ni_ni_distance": 7.56, "delta_E": 30, "m_tot": 4, "coupling": "FM"}
  ]
}
FFEOF
