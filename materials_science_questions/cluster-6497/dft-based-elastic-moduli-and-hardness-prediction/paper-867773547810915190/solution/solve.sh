#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: configurational_energies.csv ===
cat > "$OUTDIR/configurational_energies.csv" <<'FFEOF'
configuration_id,degeneracy,iron_positions,relative_energy_kJ_per_mol,space_group
1,3,"L1,L4,L7,L10",0.0,P4_12_12
2,6,"L1,L3,L7,L9",32.0,C222_1
3,24,"L1,L3,L7,L10",53.0,P1
4,12,"L1,L5,L6,L10",77.0,P2_1
5,12,"L1,L5,L6,L8",87.0,C2
6,12,"L1,L3,L7,L11",106.0,C2
7,24,"L1,L2,L5,L9",116.0,P1
8,24,"L1,L3,L7,L8",136.0,P1
9,24,"L1,L2,L5,L8",149.0,P1
10,6,"L1,L2,L7,L8",167.0,P2_12_12_1
11,12,"L1,L3,L6,L8",182.0,P2_1
12,12,"L1,L2,L5,L10",213.0,P2_1
13,12,"L1,L3,L5,L10",215.0,P1
14,12,"L1,L2,L6,L7",235.0,C2
15,24,"L1,L3,L7,L12",276.0,P1
16,24,"L1,L3,L6,L7",280.0,P1
17,24,"L1,L4,L5,L6",310.0,P1
18,12,"L1,L3,L5,L7",343.0,C2
19,24,"L1,L3,L4,L10",380.0,P1
20,24,"L1,L3,L4,L7",413.0,P1
21,12,"L1,L2,L5,L6",425.0,P2_1
22,12,"L1,L2,L3,L8",470.0,C2
23,24,"L1,L2,L3,L7",501.0,P1
24,24,"L1,L3,L5,L6",560.0,P1
25,24,"L1,L2,L3,L6",608.0,P1
26,12,"L1,L3,L4,L6",640.0,P2_1
27,12,"L1,L2,L4,L5",652.0,P1
28,24,"L1,L2,L3,L5",722.0,P1
29,12,"L1,L2,L3,L4",847.0,P2_1
FFEOF
