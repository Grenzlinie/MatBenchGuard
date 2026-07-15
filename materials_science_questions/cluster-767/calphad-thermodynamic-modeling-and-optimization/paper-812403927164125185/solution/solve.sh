#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: calculated_invariant_reactions.csv ===
cat > /app/outputs/calculated_invariant_reactions.csv <<'FFEOF'
reaction_type,temperature_K,phase_compositions
eutectic,1693,"L:29.93, b.c.c.:25.41, GaTi2:33.3"
congruent,1705,"GaTi2:33.3"
peritectoid,1303,"b.c.c.:19.57, GaTi2:33.3, GaTi3:24.43"
peritectoid,1213,"b.c.c.:16.44, GaTi3:22.81, h.c.p.:16.65"
eutectic,1702,"L:35.0, Ga3Ti5:37.5, GaTi2:33.3"
congruent,1709,"Ga3Ti5:37.5"
eutectic,1704,"L:39.56, Ga3Ti5:37.5, Ga4Ti5:41.81"
congruent,1714,"Ga4Ti5:42.96"
peritectic,1524,"L:57.79, Ga4Ti5:45.95, GaTi:51.66"
eutectic,1439,"L:65.76, GaTi:57.9, Ga2Ti:66.67"
peritectoid,1348,"GaTi:57.11, Ga2Ti:66.67, Ga3Ti2:60.0"
congruent,1440,"Ga2Ti:66.67"
peritectic,1203,"L:97.24, Ga2Ti:66.7, Ga3Ti:75.0"
FFEOF

# === solve block: calculated_formation_enthalpies_298K.csv ===
cat > /app/outputs/calculated_formation_enthalpies_298K.csv <<'FFEOF'
compound,enthalpy_kJ_per_mol_atom
GaTi3,-44.0
GaTi2,-58.0
Ga3Ti5,-45.0
Ga4Ti5,-46.0
GaTi,-48.0
Ga3Ti2,-42.0
Ga2Ti,-38.0
Ga3Ti,-40.2
FFEOF
