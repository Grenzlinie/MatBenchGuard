#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: delta_g_coefficients.json ===
cat > "$OUTDIR/delta_g_coefficients.json" <<'EOF'
{
  "A": -530,
  "B": 1530,
  "C": 0.702
}
EOF
cat > "$OUTDIR/delta_T0_eta_coefficient.json" <<'EOF'
{
  "coefficient_eta2": -2180
}
EOF
cat > "$OUTDIR/final_coefficient.json" <<'EOF'
{
  "coefficient_phi2": -850
}
EOF

# === solve block: delta_T0_eta_coefficient.json ===
cat > /app/outputs/delta_T0_eta_coefficient.json <<'EOF'
{
  "coefficient_eta2": -2180
}
EOF

# === solve block: final_coefficient.json ===
cat > /app/outputs/final_coefficient.json <<'EOF'
{
  "coefficient_phi2": -850
}
EOF
