#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: effective_moduli.csv ===
cat > "$OUTDIR/effective_moduli.csv" <<'EOF'
case,K_s_type,parameter_value,normalized_bulk_modulus
hexagonal_R,pos,0.1,1.05
hexagonal_R,neg,0.1,0.38
hexagonal_R,zero,0.1,0.50
hexagonal_R,pos,0.5,0.75
hexagonal_R,neg,0.5,0.44
hexagonal_R,zero,0.5,0.50
hexagonal_R,pos,1.0,0.5605
hexagonal_R,neg,1.0,0.4360
hexagonal_R,zero,1.0,0.500
hexagonal_R,pos,2.0,0.52
hexagonal_R,neg,2.0,0.44
hexagonal_R,zero,2.0,0.50
hexagonal_R,pos,3.0,0.51
hexagonal_R,neg,3.0,0.44
hexagonal_R,zero,3.0,0.50
hexagonal_R,pos,4.0,0.505
hexagonal_R,neg,4.0,0.44
hexagonal_R,zero,4.0,0.50
hexagonal_R,pos,5.0,0.50
hexagonal_R,neg,5.0,0.44
hexagonal_R,zero,5.0,0.50
hexagonal_f,pos,0.1,0.72
hexagonal_f,neg,0.1,0.58
hexagonal_f,zero,0.1,0.68
hexagonal_f,pos,0.2,0.56
hexagonal_f,neg,0.2,0.44
hexagonal_f,zero,0.2,0.50
hexagonal_f,pos,0.3,0.42
hexagonal_f,neg,0.3,0.32
hexagonal_f,zero,0.3,0.38
hexagonal_f,pos,0.4,0.31
hexagonal_f,neg,0.4,0.22
hexagonal_f,zero,0.4,0.28
hexagonal_f,pos,0.5,0.21
hexagonal_f,neg,0.5,0.14
hexagonal_f,zero,0.5,0.19
hexagonal_f,pos,0.6,0.12
hexagonal_f,neg,0.6,0.08
hexagonal_f,zero,0.6,0.10
flattened_c,pos,1.0,0.40
flattened_c,neg,1.0,0.22
flattened_c,zero,1.0,0.27
flattened_c,pos,2.0,0.48
flattened_c,neg,2.0,0.30
flattened_c,zero,2.0,0.35
flattened_c,pos,5.0,0.56
flattened_c,neg,5.0,0.40
flattened_c,zero,5.0,0.46
flattened_c,pos,10.0,0.60
flattened_c,neg,10.0,0.48
flattened_c,zero,10.0,0.52
flattened_c,pos,20.0,0.62
flattened_c,neg,20.0,0.54
flattened_c,zero,20.0,0.57
flattened_c,pos,30.0,0.62
flattened_c,neg,30.0,0.56
flattened_c,zero,30.0,0.58
flattened_c,pos,40.0,0.62
flattened_c,neg,40.0,0.57
flattened_c,zero,40.0,0.59
cracks_horizontal,zero,1,0.60
cracks_horizontal,zero,2,0.645
cracks_horizontal,zero,5,0.675
cracks_horizontal,zero,10,0.685
cracks_horizontal,zero,20,0.69
cracks_vertical,zero,1,0.62
cracks_vertical,zero,2,0.66
cracks_vertical,zero,5,0.69
cracks_vertical,zero,10,0.705
cracks_vertical,zero,20,0.71
cracks_random,zero,1,0.61
cracks_random,zero,2,0.655
cracks_random,zero,5,0.68
cracks_random,zero,10,0.695
cracks_random,zero,20,0.70
EOF
