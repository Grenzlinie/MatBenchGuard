#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: c60_bk_tables.json ===
cat > /app/outputs/c60_bk_tables.json <<'JSONEOF'
[
  {"mode_id": 1, "frequency_cm1": 1681.0, "B_La": 0.22, "B_Ba": 0.11},
  {"mode_id": 2, "frequency_cm1": 1450.0, "B_La": 0.0,  "B_Ba": 0.10},
  {"mode_id": 3, "frequency_cm1": 1402.0, "B_La": 0.0,  "B_Ba": 0.0 },
  {"mode_id": 4, "frequency_cm1": 1368.0, "B_La": 0.13, "B_Ba": 0.12},
  {"mode_id": 5, "frequency_cm1": 1339.0, "B_La": 0.12, "B_Ba": 0.11},
  {"mode_id": 6, "frequency_cm1": 1309.0, "B_La": 0.0,  "B_Ba": 0.0 },
  {"mode_id": 7, "frequency_cm1": 1288.0, "B_La": 0.23, "B_Ba": 0.31},
  {"mode_id": 8, "frequency_cm1": 1285.0, "B_La": 0.47, "B_Ba": 0.40},
  {"mode_id": 9, "frequency_cm1": 1263.0, "B_La": 0.24, "B_Ba": 0.0 },
  {"mode_id": 10, "frequency_cm1": 1232.0, "B_La": 0.13, "B_Ba": 0.0 },
  {"mode_id": 11, "frequency_cm1": 1188.0, "B_La": 0.10, "B_Ba": 0.0 },
  {"mode_id": 12, "frequency_cm1": 437.0,  "B_La": 0.08, "B_Ba": 0.0 },
  {"mode_id": 13, "frequency_cm1": 342.0,  "B_La": 0.18, "B_Ba": 0.0 },
  {"mode_id": 14, "frequency_cm1": 225.0,  "B_La": 0.16, "B_Ba": 0.22}
]
JSONEOF

# === solve block: c78_bk_tables.json ===
cat > /app/outputs/c78_bk_tables.json <<'JSONEOF'
[
  {"mode_id": 1, "frequency_cm1": 1682.0, "B_La": 0.32, "B_Ba": 0.20},
  {"mode_id": 2, "frequency_cm1": 1388.0, "B_La": 0.13, "B_Ba": 0.0 },
  {"mode_id": 3, "frequency_cm1": 1330.0, "B_La": 0.11, "B_Ba": 0.25},
  {"mode_id": 4, "frequency_cm1": 1316.0, "B_La": 0.0,  "B_Ba": 0.17},
  {"mode_id": 5, "frequency_cm1": 1286.0, "B_La": 0.35, "B_Ba": 0.44},
  {"mode_id": 6, "frequency_cm1": 1272.0, "B_La": 0.29, "B_Ba": 0.0 },
  {"mode_id": 7, "frequency_cm1": 1267.0, "B_La": 0.29, "B_Ba": 0.11},
  {"mode_id": 8, "frequency_cm1": 1236.0, "B_La": 0.22, "B_Ba": 0.0 },
  {"mode_id": 9, "frequency_cm1": 1189.0, "B_La": 0.14, "B_Ba": 0.0 },
  {"mode_id": 10, "frequency_cm1": 379.0,  "B_La": 0.17, "B_Ba": 0.0 },
  {"mode_id": 11, "frequency_cm1": 331.0,  "B_La": 0.22, "B_Ba": 0.0 },
  {"mode_id": 12, "frequency_cm1": 288.0,  "B_La": 0.20, "B_Ba": 0.0 },
  {"mode_id": 13, "frequency_cm1": 180.0,  "B_La": 0.29, "B_Ba": 0.39}
]
JSONEOF

# === solve block: c114_bk_tables.json ===
cat > /app/outputs/c114_bk_tables.json <<'JSONEOF'
[
  {"mode_id": 1, "frequency_cm1": 1682.0, "B_La": 0.31, "B_Ba": 0.25},
  {"mode_id": 2, "frequency_cm1": 1680.0, "B_La": 0.18, "B_Ba": 0.16},
  {"mode_id": 3, "frequency_cm1": 1390.0, "B_La": 0.11, "B_Ba": 0.0 },
  {"mode_id": 4, "frequency_cm1": 1328.0, "B_La": 0.0,  "B_Ba": 0.12},
  {"mode_id": 5, "frequency_cm1": 1320.0, "B_La": 0.10, "B_Ba": 0.30},
  {"mode_id": 6, "frequency_cm1": 1314.0, "B_La": 0.0,  "B_Ba": 0.19},
  {"mode_id": 7, "frequency_cm1": 1288.0, "B_La": 0.10, "B_Ba": 0.26},
  {"mode_id": 8, "frequency_cm1": 1277.0, "B_La": 0.28, "B_Ba": 0.25},
  {"mode_id": 9, "frequency_cm1": 1269.0, "B_La": 0.18, "B_Ba": 0.12},
  {"mode_id": 10, "frequency_cm1": 1259.0, "B_La": 0.33, "B_Ba": 0.0 },
  {"mode_id": 11, "frequency_cm1": 1240.0, "B_La": 0.28, "B_Ba": 0.0 },
  {"mode_id": 12, "frequency_cm1": 376.0,  "B_La": 0.10, "B_Ba": 0.0 },
  {"mode_id": 13, "frequency_cm1": 335.0,  "B_La": 0.27, "B_Ba": 0.10},
  {"mode_id": 14, "frequency_cm1": 302.0,  "B_La": 0.0,  "B_Ba": 0.0 },
  {"mode_id": 15, "frequency_cm1": 292.0,  "B_La": 0.20, "B_Ba": 0.10},
  {"mode_id": 16, "frequency_cm1": 125.0,  "B_La": 0.65, "B_Ba": 0.62}
]
JSONEOF

# === solve block: trend_summary.json ===
echo "trend_summary.json will be written by finalize"

# === solve block: low_freq_modes.json ===
echo "low_freq_modes.json will be written by finalize"

# === solve finalize ===
python3 /solution/compute_derived.py
