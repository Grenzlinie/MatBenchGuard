#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_formation_energies.json ===
cat > "$OUTDIR/step_01_formation_energies.json" <<'FFEOF'
{
  "bulk_formation_energy": 1.1838,
  "layer1": {"site1": 1.1814, "site2": -0.2288, "site3": -0.2288},
  "layer2": {"site1": 1.1829, "site2": 1.1669, "site3": 1.1669},
  "layer3": {"site1": 1.1836, "site2": 1.1834, "site3": 1.1834},
  "layer4": {"site1": 1.1838, "site2": 1.1838, "site3": 1.1838}
}
FFEOF

# === solve block: step_02_activation_energies.json ===
cat > "$OUTDIR/step_02_activation_energies.json" <<'FFEOF'
{
  "intra_1L": {
    "1_to_2": 2.49,
    "1_to_3": 2.49,
    "2_to_3": 2.15,
    "2_to_4": 2.05,
    "3_to_5": 2.05
  },
  "intra_2L": {
    "a_to_b": 2.35,
    "a_to_c": 2.35,
    "b_to_c": 2.30,
    "b_to_d": 2.30,
    "c_to_e": 2.30
  },
  "intra_3L": {
    "1_to_2": 2.37,
    "1_to_3": 2.37,
    "2_to_3": 2.35,
    "2_to_4": 2.35,
    "3_to_5": 2.35
  },
  "intra_4L": {
    "a_to_b": 2.3738,
    "a_to_c": 2.3738,
    "b_to_c": 2.3738,
    "b_to_d": 2.3738,
    "c_to_e": 2.3738
  },
  "inter_1L-1LR": {
    "2_to_cR": 2.25,
    "3_to_bR": 2.25
  },
  "inter_2L-1L": {
    "a_to_2": 2.55,
    "b_to_2": 2.15,
    "c_to_2": 2.15
  },
  "inter_3L-2L": {
    "1_to_a": 2.30,
    "2_to_a": 2.01,
    "3_to_a": 2.01
  },
  "inter_4L-3L": {
    "a_to_1": 2.35,
    "b_to_1": 2.35,
    "c_to_1": 2.35
  },
  "inter_5L-4L": {
    "1_to_a": 2.3738,
    "2_to_a": 2.3738,
    "3_to_a": 2.3738
  }
}
FFEOF
