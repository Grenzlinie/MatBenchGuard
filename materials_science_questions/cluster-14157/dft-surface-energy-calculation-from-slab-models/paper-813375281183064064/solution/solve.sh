#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: simulation_results.json ===
cat > "$OUTDIR/simulation_results.json" <<'FFEOF'
{
  "AuPd_monomer_fraction_theta015_T300": 0.75,
  "AuPd_dimer_fraction_theta015_T300": 0.10,
  "AuPt_monomer_fraction_theta015_T300": 0.10,
  "AuPt_dimer_fraction_theta015_T300": 0.10,
  "AuPd_short_range_order_1NN_theta01_T300": -0.5,
  "AuPd_short_range_order_2NN_theta01_T300": 0.3,
  "AuPd_short_range_order_3NN_theta01_T300": 0.01,
  "AuPd_c2x2_alpha_1NN_theta05_T100": -0.95,
  "random_monomer_fraction_theta015": 0.52200625,
  "random_dimer_fraction_theta015": 0.226289709375
}
FFEOF

# === solve finalize ===
echo "Reference oracle artifacts written."
