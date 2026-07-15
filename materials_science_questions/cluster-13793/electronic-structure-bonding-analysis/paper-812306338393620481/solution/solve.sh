#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: li2ga_electronic_properties.json ===
cat > /app/outputs/li2ga_electronic_properties.json <<'HEREDOC'
{
  "Mulliken_charges": {"Ga": 0.241, "Li1": -0.054, "Li2": -0.187},
  "Overlap_populations": {
    "Ga_Ga": 0.188,
    "Ga_Li1_2.70A": 0.127,
    "Ga_Li1_2.86A": 0.086,
    "Ga_Li1_3.05A": 0.048,
    "Ga_Li2_2.77A": 0.097,
    "Ga_Li2_3.16A": 0.043,
    "Ga_Li2_3.20A": 0.038,
    "Li_Li_intra_2.75A": 0.045,
    "Li_Li_intra_2.71A": 0.037,
    "Li_Li_inter_2.72A": 0.039,
    "Li_Li_inter_3.16A": 0.034
  },
  "Li_DOS_percent_at_Fermi": 40.0
}
HEREDOC
