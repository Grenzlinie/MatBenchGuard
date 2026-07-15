#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: equilibrium_compositions.csv ===
cat > /app/outputs/equilibrium_compositions.csv <<'FFEOF'
reaction_label,T_K,WO3_wt,product_wt
sulfidization_with_H2,823,0.0,0.0977
sulfidization_with_H2,923,0.0,0.0973
sulfidization_with_H2,1023,0.0,0.0972
sulfidization_with_H2,1123,0.0,0.0971
sulfidization_with_H2,1223,0.0,0.0970
sulfidization_without_H2,823,0.0,0.620
sulfidization_without_H2,923,0.0,0.614
sulfidization_without_H2,1023,0.0,0.612
sulfidization_without_H2,1123,0.0,0.612
sulfidization_without_H2,1223,0.0,0.611
selenization_with_H2,823,0.0,0.0977
selenization_with_H2,923,0.0,0.0973
selenization_with_H2,1023,0.0,0.0971
selenization_with_H2,1123,0.0,0.0971
selenization_with_H2,1223,0.0,0.0970
selenization_without_H2,823,5.0,0.0
selenization_without_H2,923,5.0,0.0
selenization_without_H2,1023,5.0,0.0
selenization_without_H2,1123,5.0,0.0
selenization_without_H2,1223,5.0,0.0
FFEOF
