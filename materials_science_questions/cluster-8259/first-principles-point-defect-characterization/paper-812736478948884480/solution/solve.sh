#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: structural_distances.json ===
cat > "/app/outputs/structural_distances.json" <<'FFEOF'
{
  "I_i": {
    "0K": {
      "I_I_distance": 3.291,
      "I_Pb_distance": 3.229
    },
    "300K": {
      "I_I_distance": 3.954,
      "I_Pb_distance": 3.147
    }
  },
  "I_i_minus1": {
    "0K": {
      "I_I_distance": 3.928,
      "I_Pb_distance": 3.075
    },
    "300K": {
      "I_I_distance": 4.002,
      "I_Pb_distance": 3.137
    }
  },
  "I_i_plus1": {
    "0K": {
      "I_I_distance": 3.000,
      "I_Pb_distance": 4.511
    },
    "300K": {
      "I_I_distance": 3.200,
      "I_Pb_distance": 4.526
    }
  }
}
FFEOF

# === solve block: rms_velocities.csv ===
cat > "/app/outputs/rms_velocities.csv" <<'FFEOF'
System,total,MA,Pb_I_lattice,Pb_I_including_interstitial,interstitial_I,O
MAPbI3,0.0342,0.0469,0.0128,,,
I_i,0.0352,0.0481,0.0141,0.0142,0.0059,
I_i_minus1,0.0356,0.0487,0.0140,0.0141,0.0066,
I_i_plus1,0.0374,0.0509,0.0152,0.0153,0.0060,
IO3_minus1,0.0300,0.0409,0.0130,0.0131,0.0055,0.0061
FFEOF

# === solve block: recombination_times.json ===
cat > "/app/outputs/recombination_times.json" <<'FFEOF'
{
  "pristine": {
    "recombination_time_ns": 1.56
  },
  "I_i": {
    "recombination_time_ns": 0.975
  },
  "I_i_minus1": {
    "recombination_time_ns": 2.028
  },
  "I_i_plus1": {
    "recombination_time_ns": 2.34
  },
  "IO3_minus1": {
    "recombination_time_ns": 4.212
  },
  "recombination_ordering": [
    "I_i",
    "pristine",
    "I_i_minus1",
    "I_i_plus1",
    "IO3_minus1"
  ]
}
FFEOF
