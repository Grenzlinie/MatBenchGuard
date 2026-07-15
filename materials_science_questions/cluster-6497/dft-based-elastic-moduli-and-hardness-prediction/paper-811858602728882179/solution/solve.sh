#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: b1_b2_energy.json ===
cat > "$OUTDIR/b1_b2_energy.json" <<'EOF'
{
  "b1": 1.45,
  "b2": 1.41,
  "binding_energy_per_atom": -7.17
}
EOF

# === solve block: bulk_modulus.txt ===
cat > "$OUTDIR/bulk_modulus.txt" <<'EOF'
674
EOF

# === solve block: force_constant.txt ===
cat > "$OUTDIR/force_constant.txt" <<'EOF'
5.6
EOF

# === solve block: critical_pressures.json ===
cat > "$OUTDIR/critical_pressures.json" <<'EOF'
{
  "external_critical_pressure_GPa": 922,
  "internal_critical_pressure_GPa": -134
}
EOF
