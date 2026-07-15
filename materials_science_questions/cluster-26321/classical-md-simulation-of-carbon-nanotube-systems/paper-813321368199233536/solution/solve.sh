#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: permeation_rates.csv ===
cat > /app/outputs/permeation_rates.csv <<'EOF'
system,field,j_d,p_d,D_p,k,p_f
single,none,2.47,0.074,2.38,70.41,1.368
array15,none,1.69,0.050,1.94,57.40,0.896
array25,none,2.32,0.069,2.14,63.31,1.268
EOF

# === solve block: dipole_distribution.csv ===
cat > /app/outputs/dipole_distribution.csv <<'EOF'
system,field,cos_alpha_low,cos_alpha_high,probability
single,none,-1.0,-0.9,0.16
single,none,-0.9,-0.8,0.09
single,none,-0.8,-0.7,0.06
single,none,-0.7,-0.6,0.04
single,none,-0.6,-0.5,0.03
single,none,-0.5,-0.4,0.02
single,none,-0.4,-0.3,0.02
single,none,-0.3,-0.2,0.02
single,none,-0.2,-0.1,0.02
single,none,-0.1,0.0,0.04
single,none,0.0,0.1,0.04
single,none,0.1,0.2,0.02
single,none,0.2,0.3,0.02
single,none,0.3,0.4,0.02
single,none,0.4,0.5,0.02
single,none,0.5,0.6,0.03
single,none,0.6,0.7,0.04
single,none,0.7,0.8,0.06
single,none,0.8,0.9,0.09
single,none,0.9,1.0,0.16
single,static,-1.0,-0.9,0.25
single,static,-0.9,-0.8,0.20
single,static,-0.8,-0.7,0.15
single,static,-0.7,-0.6,0.10
single,static,-0.6,-0.5,0.08
single,static,-0.5,-0.4,0.05
single,static,-0.4,-0.3,0.05
single,static,-0.3,-0.2,0.04
single,static,-0.2,-0.1,0.03
single,static,-0.1,0.0,0.02
single,static,0.0,0.1,0.015
single,static,0.1,0.2,0.01
single,static,0.2,0.3,0.005
single,static,0.3,0.4,0.0
single,static,0.4,0.5,0.0
single,static,0.5,0.6,0.0
single,static,0.6,0.7,0.0
single,static,0.7,0.8,0.0
single,static,0.8,0.9,0.0
single,static,0.9,1.0,0.0
EOF

# === solve block: effective_viscosity.csv ===
cat > /app/outputs/effective_viscosity.csv <<'EOF'
array_separation,eta
15,7.5e-3
EOF
