#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: toe_constants.csv ===
cat > "$OUTDIR/toe_constants.csv" <<'EOF'
compound,model,C111,C112,C166,C123,C144,C456
CsCl,NN,-2.1846,-0.8829,-0.9316,-0.7312,-0.7989,-0.8325
CsCl,NNN,-3.0897,-0.7625,-0.9405,-0.6398,-0.8367,-0.9352
CsBr,NN,-1.7930,-0.7396,-0.8293,-0.6148,-0.7224,-0.7763
CsBr,NNN,-2.3430,-0.6665,-0.8401,-0.5591,-0.7507,-0.8464
CsI,NN,-1.4659,-0.6171,-0.6968,-0.5144,-0.6113,-0.6595
CsI,NNN,-2.0387,-0.5413,-0.7109,-0.4556,-0.6423,-0.7357
EOF

# === solve block: pressure_derivatives.csv ===
cat > "$OUTDIR/pressure_derivatives.csv" <<'EOF'
compound,model,dC44'_dp,dS'_dp
CsCl,NN,4.097,0.160
CsCl,NNN,4.208,1.144
CsBr,NN,4.293,0.095
CsBr,NNN,4.407,0.789
CsI,NN,4.438,0.081
CsI,NNN,4.605,0.966
EOF

# === solve block: linear_combinations.csv ===
cat > "$OUTDIR/linear_combinations.csv" <<'EOF'
compound,model,C111+2C112,C123+2C112,C144+2C166
CsCl,NN,-3.9504,-2.4970,-2.6619
CsCl,NNN,-4.6147,-2.1648,-2.7177
CsBr,NN,-3.2732,-2.0940,-2.3812
CsBr,NNN,-3.6759,-1.8921,-2.4309
CsI,NN,-2.7001,-1.7486,-2.0048
CsI,NNN,-3.1213,-1.5382,-2.0641
EOF
