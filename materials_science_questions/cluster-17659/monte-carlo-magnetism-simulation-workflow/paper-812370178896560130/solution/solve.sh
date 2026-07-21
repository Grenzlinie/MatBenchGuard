#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: T_ms.txt ===
cat > /app/outputs/T_ms.txt <<'FFEOF'
1.63
FFEOF

# === solve block: T_fm.txt ===
cat > /app/outputs/T_fm.txt <<'FFEOF'
1.21
FFEOF

# === solve block: T_c_and_T_K.txt ===
cat > /app/outputs/T_c_and_T_K.txt <<'FFEOF'
T_c 0.745 T_K 0.660
FFEOF

# === solve block: S_conf_at_Tc.txt ===
cat > /app/outputs/S_conf_at_Tc.txt <<'FFEOF'
0.063
FFEOF
