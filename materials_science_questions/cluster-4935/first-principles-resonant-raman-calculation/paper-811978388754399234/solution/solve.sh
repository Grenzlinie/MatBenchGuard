#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: cf_analysis_results.json ===
cat > /app/outputs/cf_analysis_results.json <<'FFEOF'
{
  "YbAG": {
    "Bkq": [-248.0, 372.0, -1668.0, 290.0, 715.0, 743.0, -560.0, 920.0, -303.0],
    "R": 2.21,
    "alpha": 0.00336
  },
  "YbGG": {
    "Bkq": [-88.0, 185.0, -1444.0, 331.0, 688.0, 795.0, -507.0, 1057.0, -271.0],
    "R": null,
    "alpha": 0.00356
  },
  "reassignment_validated": true,
  "reassignment_reasoning": "The 10903 cm-1 line, previously assigned as vibronic, must be an electronic crystal-field level because test fitting omitting 2F7/2 levels and with different initial guesses consistently identifies 10328 and 10903 cm-1 as electronic, while the choice between 10640 and 10680 cm-1 is unresolved; selecting 10680 gives a better fit. Additionally, derivative analysis shows the highest 2F5/2 level is most sensitive to non-cubic parameters B20 and B22, contradicting the earlier vibronic assignment premise."
}
FFEOF
