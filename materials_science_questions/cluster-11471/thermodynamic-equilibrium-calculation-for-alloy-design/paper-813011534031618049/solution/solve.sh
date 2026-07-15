#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: phase_diagrams.json ===
cat > "$OUTDIR/phase_diagrams.json" <<'FFEOF'
[
  {"Cr_wt":10,"C_min_wt":0.6,"C_max_wt":1.0,"T_min_C":815,"T_max_C":1280},
  {"Cr_wt":15,"C_min_wt":0.9,"C_max_wt":1.5,"T_min_C":815,"T_max_C":1280},
  {"Cr_wt":20,"C_min_wt":1.2,"C_max_wt":2.0,"T_min_C":815,"T_max_C":1280},
  {"Cr_wt":25,"C_min_wt":1.5,"C_max_wt":2.5,"T_min_C":815,"T_max_C":1280},
  {"Cr_wt":30,"C_min_wt":1.8,"C_max_wt":3.0,"T_min_C":815,"T_max_C":1280},
  {"Cr_wt":35,"C_min_wt":2.1,"C_max_wt":3.5,"T_min_C":815,"T_max_C":1280},
  {"Cr_wt":40,"C_min_wt":2.4,"C_max_wt":4.0,"T_min_C":815,"T_max_C":1280},
  {"Cr_wt":45,"C_min_wt":2.7,"C_max_wt":4.5,"T_min_C":815,"T_max_C":1280}
]
FFEOF

# === solve block: solidification_steps.csv ===
cat > "$OUTDIR/solidification_steps.csv" <<'FFEOF'
composition,model,step_order,start_temp_C,end_temp_C,phases_sequence
45Cr-4.0C,Scheil,1,2000,1393,Liquid cooling
45Cr-4.0C,Scheil,2,1393,1319.7,Liquid -> M7C3
45Cr-4.0C,Scheil,3,1319.7,1297.9,Liquid -> M23C6
45Cr-4.0C,Scheil,4,1297.9,1289.1,Liquid -> Bcc + M23C6
45Cr-4.0C,Scheil,5,1289.1,1283.8,Liquid -> Bcc + M7C3
45Cr-4.0C,Scheil,6,1283.8,1283.8,Liquid -> Fcc + Bcc + M7C3
45Cr-4.0C,Lever,1,2000,1393,Liquid cooling
45Cr-4.0C,Lever,2,1393,1319.4,Liquid -> M7C3
45Cr-4.0C,Lever,3,1319.4,1289.1,Liquid -> M23C6 + M7C3
45Cr-4.0C,Lever,4,1289.1,1289.1,Liquid + M23C6 -> Bcc + M7C3
40Cr-3.5C,Scheil,1,2000,1352,Liquid cooling
40Cr-3.5C,Scheil,2,1352,1300,Liquid -> M7C3
40Cr-3.5C,Scheil,3,1300,1292.2,Liquid -> M23C6
40Cr-3.5C,Scheil,4,1292.2,1289.1,Liquid -> M23C6 + Bcc
40Cr-3.5C,Scheil,5,1289.1,1283.8,Liquid -> M7C3 + Bcc
40Cr-3.5C,Scheil,6,1283.8,1283.8,Liquid -> M7C3 + Bcc + Fcc
40Cr-3.5C,Lever,1,2000,1352,Liquid cooling
40Cr-3.5C,Lever,2,1352,1300,Liquid -> M7C3
40Cr-3.5C,Lever,3,1300,1289.1,Liquid -> M7C3 + M23C6
40Cr-3.5C,Lever,4,1289.1,1286.9,Liquid -> M7C3 + Bcc
35Cr-3.0C,Scheil,1,2000,1312,Liquid cooling
35Cr-3.0C,Scheil,2,1312,1287.2,Liquid -> M7C3
35Cr-3.0C,Scheil,3,1287.2,1283.8,Liquid -> M7C3 + Bcc
35Cr-3.0C,Scheil,4,1283.8,1283.8,Liquid -> M7C3 + Bcc + Fcc
35Cr-3.0C,Lever,1,2000,1312,Liquid cooling
35Cr-3.0C,Lever,2,1312,1287.2,Liquid -> M7C3
35Cr-3.0C,Lever,3,1287.2,1283.8,Liquid -> M7C3 + Bcc
35Cr-3.0C,Lever,4,1283.8,1283.8,Liquid -> M7C3 + Bcc + Fcc
30Cr-2.3C,Scheil,1,2000,1318.6,Liquid cooling
30Cr-2.3C,Scheil,2,1300.2,1284.0,Liquid -> Bcc
30Cr-2.3C,Scheil,3,1284.0,1283.8,Liquid -> Bcc + M7C3
30Cr-2.3C,Scheil,4,1283.8,1283.8,Liquid -> Fcc + Bcc + M7C3
30Cr-2.3C,Lever,1,2000,1318.6,Liquid cooling
30Cr-2.3C,Lever,2,1318.6,1284.1,Liquid -> Bcc
30Cr-2.3C,Lever,3,1284.1,1283.8,Liquid -> Bcc + M7C3
30Cr-2.3C,Lever,4,1283.8,1283.8,Liquid -> Fcc + M7C3
25Cr-2.0C,Scheil,1,2000,1342.3,Liquid cooling
25Cr-2.0C,Scheil,2,1342.3,1342,Liquid -> Bcc
25Cr-2.0C,Scheil,3,1342,1285.4,Liquid -> Fcc
25Cr-2.0C,Scheil,4,1285.4,1283.8,Liquid -> Fcc + M7C3
25Cr-2.0C,Scheil,5,1283.8,1283.8,Liquid -> Fcc + M7C3 + Bcc
25Cr-2.0C,Lever,1,2000,1342.3,Liquid cooling
25Cr-2.0C,Lever,2,1342.3,1342,Liquid -> Bcc
25Cr-2.0C,Lever,3,1342,1341.8,Liquid -> Fcc + Bcc
25Cr-2.0C,Lever,4,1341.8,1285.4,Liquid -> Fcc
25Cr-2.0C,Lever,5,1285.4,1284.9,Liquid -> Fcc + M7C3
20Cr-1.5C,Scheil,1,2000,1383.8,Liquid cooling
20Cr-1.5C,Scheil,2,1383.8,1381.6,Liquid -> Bcc
20Cr-1.5C,Scheil,3,1381.6,1286.2,Liquid -> Fcc
20Cr-1.5C,Scheil,4,1286.2,1284.8,Liquid -> Fcc + M7C3
20Cr-1.5C,Lever,1,2000,1383.8,Liquid cooling
20Cr-1.5C,Lever,2,1383.8,1381.6,Liquid -> Bcc
20Cr-1.5C,Lever,3,1381.6,1380.2,Liquid -> Fcc + Bcc
20Cr-1.5C,Lever,4,1380.2,1286.2,Liquid -> Fcc
20Cr-1.5C,Lever,5,1286.2,1286.1,Liquid -> Fcc + M7C3
15Cr-1C,Scheil,1,2000,1429.8,Liquid cooling
15Cr-1C,Scheil,2,1429.8,1417.3,Liquid -> Bcc
15Cr-1C,Scheil,3,1429.8,1285.3,Liquid -> Fcc
15Cr-1C,Scheil,4,1285.3,1265.2,Liquid -> Fcc + M7C3
15Cr-1C,Lever,1,2000,1429.8,Liquid cooling
15Cr-1C,Lever,2,1429.8,1417.3,Liquid -> Bcc
15Cr-1C,Lever,3,1417.3,1411.9,Liquid -> Bcc + Fcc
15Cr-1C,Lever,4,1411.9,1285.6,Liquid -> Fcc
15Cr-1C,Lever,5,1285.6,1285.6,Liquid -> Fcc + M7C3
10Cr-0.75C,Scheil,1,2000,1480.1,Liquid cooling
10Cr-0.75C,Scheil,2,1480.1,1449.1,Liquid -> Bcc
10Cr-0.75C,Scheil,3,1449.1,1277.1,Liquid -> Fcc
10Cr-0.75C,Scheil,4,1277.1,1185.0,Liquid -> Fcc + M7C3
10Cr-0.75C,Lever,1,2000,1480.1,Liquid cooling
10Cr-0.75C,Lever,2,1480.1,1449.3,Liquid -> Bcc
10Cr-0.75C,Lever,3,1449.3,1441.1,Liquid -> Fcc + Bcc
10Cr-0.75C,Lever,4,1441.1,1416.7,Liquid -> Fcc
10Cr-5C,Scheil,1,2000,1242.4,Liquid cooling
10Cr-5C,Scheil,2,1242.4,1170.3,Liquid -> M7C3
10Cr-5C,Scheil,3,1170.3,1114.7,Liquid -> Fcc + M7C3
10Cr-5C,Scheil,4,1114.7,1098.2,Liquid -> Fcc + M23C6
10Cr-5C,Lever,1,2000,1242.4,Liquid cooling
10Cr-5C,Lever,2,1242.4,1172.2,Liquid -> M7C3
10Cr-5C,Lever,3,1172.2,1135.7,Liquid -> Fcc + M7C3
FFEOF

# === solve block: driving_force_interface.csv ===
cat > "$OUTDIR/driving_force_interface.csv" <<'FFEOF'
composition,driving_force_J_per_mol,shell_possible
45Cr-4.0C,450,True
40Cr-3.5C,430,True
35Cr-3.0C,380,True
30Cr-2.3C,320,True
25Cr-2.0C,250,False
20Cr-1.5C,200,False
15Cr-1C,150,False
10Cr-0.75C,120,False
10Cr-5C,80,False
FFEOF
