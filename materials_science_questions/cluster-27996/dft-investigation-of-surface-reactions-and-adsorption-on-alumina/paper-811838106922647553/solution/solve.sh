#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: ethanol_adsorption_dehydrated.csv ===
cat > "$OUTDIR/ethanol_adsorption_dehydrated.csv" <<'EOF'
E_ads_kcal_mol
-34.50
EOF

# === solve block: c_c_barrier_dehydrated.csv ===
cat > "$OUTDIR/c_c_barrier_dehydrated.csv" <<'EOF'
barrier_kcal_mol
24.92
EOF

# === solve block: ethanol_adsorption_hydrated.csv ===
cat > "$OUTDIR/ethanol_adsorption_hydrated.csv" <<'EOF'
E_ads_kcal_mol
-21.25
EOF

# === solve block: c_c_barrier_hydrated.csv ===
cat > "$OUTDIR/c_c_barrier_hydrated.csv" <<'EOF'
barrier_kcal_mol
21.55
EOF

# === solve block: ring_stability.csv ===
cat > "$OUTDIR/ring_stability.csv" <<'EOF'
system,ring_stable,intermediate_energy_kcal_mol
dehydrated,true,-57.11
hydrated,false,-21.25
EOF
