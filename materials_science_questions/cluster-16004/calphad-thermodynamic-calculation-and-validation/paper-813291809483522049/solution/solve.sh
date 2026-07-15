#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: table2_parameters.csv ===
cat > /app/outputs/table2_parameters.csv << 'FFEOF'
n,B_H,B_S
0,95901,25.865
1,9279,-2.623
2,3945,1.769
FFEOF

# === solve block: table3_properties.csv ===
cat > /app/outputs/table3_properties.csv << 'FFEOF'
x_Ni,H_E,S_E,G_E,a_Cu,a_Ni
0.0,0,0,0,1.000,0.000
0.1,551,-0.363,1042,0.907,0.236
0.2,1106,-0.590,1902,0.825,0.408
0.3,1617,-0.699,2561,0.753,0.532
0.4,2038,-0.714,3002,0.686,0.622
0.5,2320,-0.656,3205,0.621,0.689
0.6,2416,-0.545,3152,0.552,0.743
0.7,2280,-0.402,2823,0.471,0.793
0.8,1863,-0.250,2201,0.367,0.848
0.9,1119,-0.109,1266,0.220,0.914
1.0,0,0,0,0.000,1.000
FFEOF

# === solve block: table5_phasediagram.csv ===
cat > /app/outputs/table5_phasediagram.csv << 'FFEOF'
T_K,x_Ni_liquid,x_Ni_solid
1700,0.9165,0.9361
1675,0.8340,0.8759
1650,0.7496,0.8166
1625,0.6645,0.7571
1600,0.5811,0.6964
1575,0.5019,0.6327
1550,0.4283,0.5646
1525,0.3604,0.4917
1500,0.2972,0.4151
1475,0.2377,0.3370
1450,0.1814,0.2600
1425,0.1281,0.1855
1400,0.0781,0.1143
1375,0.0314,0.0466
FFEOF
