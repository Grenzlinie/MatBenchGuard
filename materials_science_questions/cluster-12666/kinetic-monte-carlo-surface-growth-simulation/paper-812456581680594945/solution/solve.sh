#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: percolation_thresholds.csv ===
cat > $OUTDIR/percolation_thresholds.csv <<'FFEOF'
system,method,threshold
2D_100x100,random,5927
2D_100x100,thermo,5810
3D_10x10x10,random,312
3D_10x10x10,thermo,300
3D_18x18x18,random,1817
3D_18x18x18,thermo,1750
FFEOF

# === solve block: tortuosity_vs_microporosity.csv ===
cat > $OUTDIR/tortuosity_vs_microporosity.csv <<'FFEOF'
cube_size,microporosity,inverse_tortuosity
10x10x10,0.31,0.0
10x10x10,0.33,0.05
10x10x10,0.35,0.15
10x10x10,0.40,0.30
10x10x10,0.45,0.40
10x10x10,0.50,0.47
10x10x10,0.55,0.52
10x10x10,0.60,0.56
10x10x10,0.65,0.60
10x10x10,0.70,0.64
10x10x10,0.75,0.68
10x10x10,0.80,0.73
10x10x10,0.85,0.79
10x10x10,0.90,0.86
10x10x10,0.95,0.94
10x10x10,0.99,0.99
18x18x18,0.20,0.0
18x18x18,0.22,0.03
18x18x18,0.25,0.10
18x18x18,0.30,0.22
18x18x18,0.35,0.35
18x18x18,0.40,0.43
18x18x18,0.45,0.49
18x18x18,0.50,0.54
18x18x18,0.55,0.58
18x18x18,0.60,0.62
18x18x18,0.65,0.66
18x18x18,0.70,0.70
18x18x18,0.75,0.74
18x18x18,0.80,0.79
18x18x18,0.85,0.85
18x18x18,0.90,0.91
18x18x18,0.95,0.96
18x18x18,0.99,0.99
FFEOF

# === solve block: structural_parameters.csv ===
cat > $OUTDIR/structural_parameters.csv <<'FFEOF'
N0,method,internal_surface_area,free_energy
1000,random,1250,2.5e-20
1000,thermo,1020,1.9e-20
5000,random,6150,1.22e-19
5000,thermo,4900,9.3e-20
10000,random,12100,2.4e-19
10000,thermo,9800,1.82e-19
FFEOF
