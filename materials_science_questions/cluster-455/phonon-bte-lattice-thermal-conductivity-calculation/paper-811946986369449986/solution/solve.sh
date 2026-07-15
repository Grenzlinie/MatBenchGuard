#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: steady_state_films_conductance.csv ===
cat > "$OUTDIR/steady_state_films_conductance.csv" <<'EOF'
thickness_nm,conductance_W_per_K
10,9.1e-8
20,8.3e-8
30,7.7e-8
50,6.7e-8
70,5.9e-8
100,5.0e-8
150,4.0e-8
200,3.3e-8
300,2.5e-8
500,1.7e-8
700,1.2e-8
1000,9.1e-9
EOF

# === solve block: steady_state_nanowires_conductivity.csv ===
cat > "$OUTDIR/steady_state_nanowires_conductivity.csv" <<'EOF'
diameter_nm,temperature_K,thermal_conductivity_W_per_mK
37,50,6.0
37,100,15.0
37,150,24.0
37,200,30.0
37,250,35.0
37,300,40.0
37,350,28.0
37,400,20.0
56,50,8.0
56,100,18.0
56,150,28.0
56,200,38.0
56,250,42.0
56,300,46.0
56,350,30.0
56,400,22.0
115,50,10.0
115,100,25.0
115,150,45.0
115,200,60.0
115,250,55.0
115,300,48.0
115,350,35.0
115,400,25.0
EOF

# === solve block: transient_temperature_profiles.csv ===
cat > "$OUTDIR/transient_temperature_profiles.csv" <<'EOF'
system,time_ns,position,temperature_K
film,0.0,midpoint,10.0
film,0.5,midpoint,10.0
film,1.0,midpoint,12.0
film,1.5,midpoint,12.0
film,2.0,midpoint,12.2
film,3.0,midpoint,14.5
film,4.0,midpoint,16.0
film,5.0,midpoint,16.2
film,7.0,midpoint,16.5
film,10.0,midpoint,16.8
film,15.0,midpoint,17.0
film,20.0,midpoint,17.0
nanowire,0.0,midpoint,10.0
nanowire,0.5,midpoint,10.1
nanowire,1.0,midpoint,10.5
nanowire,1.5,midpoint,11.0
nanowire,2.0,midpoint,11.5
nanowire,3.0,midpoint,12.5
nanowire,4.0,midpoint,13.5
nanowire,5.0,midpoint,14.5
nanowire,7.0,midpoint,16.0
nanowire,10.0,midpoint,18.0
nanowire,15.0,midpoint,19.5
nanowire,20.0,midpoint,20.0
EOF
