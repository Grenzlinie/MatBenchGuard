#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_epis.json ===
cat > "$OUTDIR/step_01_epis.json" <<'EOF'
{
  "J2_1": 0.004882,
  "J2_2": -0.0001463,
  "volume": 107.0
}
EOF

# === solve block: step_02_fourier.json ===
cat > "$OUTDIR/step_02_fourier.json" <<'EOF'
{
  "J000_over_kB": 36438.24,
  "J100_over_kB": -12884.48
}
EOF

# === solve block: step_03_t_i_minus.json ===
cat > "$OUTDIR/step_03_t_i_minus.json" <<'EOF'
{
  "c_0.10": 1159.6032,
  "c_0.25": 2415.84
}
EOF

# === solve block: step_04_eta_eq.json ===
cat > "$OUTDIR/step_04_eta_eq.json" <<'EOF'
{
  "composition": 0.25,
  "eta_eq": 0.95,
  "temperature": 1000
}
EOF

# === solve block: step_05_phase_boundaries.json ===
cat > "$OUTDIR/step_05_phase_boundaries.json" <<'EOF'
{
  "alpha_solubility_limit": 0.08,
  "delta_prime_composition": 0.20
}
EOF
