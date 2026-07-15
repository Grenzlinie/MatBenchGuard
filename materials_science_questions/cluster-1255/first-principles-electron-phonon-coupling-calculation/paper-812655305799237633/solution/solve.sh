#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: renormalized_frequency.txt ===
cat > "$OUTDIR/renormalized_frequency.txt" <<'EOF'
omega_F^2 = omega0^2 * g / (2*f + g)
EOF

# === solve block: g_T_approximation.txt ===
cat > "$OUTDIR/g_T_approximation.txt" <<'EOF'
g_T = (1/2)*G*coth(hbar*omega_F_T1/(2*k*T))
EOF

# === solve block: barrett_constants.txt ===
cat > "$OUTDIR/barrett_constants.txt" <<'EOF'
A = 1/omega0**2
B = (2*hbar*f*omega_F_T1)/(k*G*omega0**2)
T1 = hbar*omega_F_T1/k
T0 = hbar*Abs(g2)*omega_F_T1/(k*G)
EOF
