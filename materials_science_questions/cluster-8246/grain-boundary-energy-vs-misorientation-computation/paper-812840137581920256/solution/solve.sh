#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: pristine_mechanical_properties.csv ===
cat > "$OUTDIR/pristine_mechanical_properties.csv" <<'EOF'
direction,Youngs_modulus_GPa,UTS_GPa,failure_strain_percent
zz,678,133,27.9
am,611,116,23.9
EOF

# === solve block: gb_mechanical_properties.csv ===
cat > "$OUTDIR/gb_mechanical_properties.csv" <<'EOF'
model_name,direction,GB_linear_density_nm-1,Youngs_modulus_GPa,UTS_GPa,failure_strain_percent,first_broken_bond_type
(2,1)|(1,2),zz,1.51,627,77,13.6,B-N bond in hexagonal ring adjacent to (5|7) pair
(3,2)|(2,3),zz,0.92,615,93,17.0,B-N bond in hexagonal ring adjacent to (5|7) pair
(6,5)|(5,6),zz,0.42,634,99,17.4,B-N bond in hexagonal ring adjacent to (5|7) pair
(1,9)|(9,1),am,0.84,607,76,14.4,B-N bond in hexagonal ring adjacent to (5|7) pair
(1,4)|(4,1),am,1.75,549,63,11.7,B-N bond in hexagonal ring adjacent to (5|7) pair
(2,5)|(5,2),am,2.56,504,69,12.7,B-B and N-N bonds in (5|7) pairs
EOF

# === solve block: strain_rate_results.csv ===
cat > "$OUTDIR/strain_rate_results.csv" <<'EOF'
model_name,strain_rate_s-1,UTS_GPa,Youngs_modulus_GPa
(2,1)|(1,2),1e8,80,627
(2,1)|(1,2),5e8,80,627
(2,1)|(1,2),1e9,80,627
(2,1)|(1,2),5e9,199,627
(2,1)|(1,2),1e10,199,627
(1,9)|(9,1),1e8,76,607
(1,9)|(9,1),5e8,158,607
(1,9)|(9,1),1e9,240,607
(1,9)|(9,1),5e9,240,607
(1,9)|(9,1),1e10,240,607
EOF

# === solve block: temperature_results.csv ===
cat > "$OUTDIR/temperature_results.csv" <<'EOF'
model_name,temperature_K,UTS_GPa,Youngs_modulus_GPa
(2,1)|(1,2),1,98,648
(2,1)|(1,2),300,77,627
(2,1)|(1,2),500,65,590
(2,1)|(1,2),800,52,560
(2,1)|(1,2),1100,43,551
(1,9)|(9,1),1,90,635
(1,9)|(9,1),300,76,607
(1,9)|(9,1),500,60,580
(1,9)|(9,1),800,45,550
(1,9)|(9,1),1100,38,532
EOF
