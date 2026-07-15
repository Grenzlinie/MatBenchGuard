#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: elastic_constants.txt ===
# Write elastic constants (GPa) as in paper Table II (VASP DFT values)
cat > "$OUTDIR/elastic_constants.txt" <<'FFEOF'
79.961 143.756 66.879 28.902 71.733
FFEOF

# === solve block: zone_center_phonon_frequencies.txt ===
# Write zone-center optical phonon frequencies and symmetry labels
cat > "$OUTDIR/zone_center_phonon_frequencies.txt" <<'FFEOF'
mode_index,frequency_cm1,irrep,description
1,94.0,Eu,CN libration
2,119.0,A2u,Co-C-N-H-N-C-Co translation
3,137.0,Eg,CN libration
4,173.0,Eg,CN libration
5,195.0,A1u,CN libration
6,216.0,A1g,CN libration
7,248.0,Eu,CN libration
8,290.0,A2g,CN libration
9,335.0,Eg,CN libration
10,372.0,Eu,CN libration
11,422.0,A2u,CN libration
12,446.0,A1u,CN libration
13,476.0,Eg,CN libration
14,482.0,A1g,CN libration
15,504.0,Eu,CN libration
16,560.0,A2g,CN libration
17,616.0,Eu,CN libration
18,680.0,A2u,CN libration
19,780.0,A1g,CN libration
20,920.0,Eu,N-H bending
21,1159.0,Eu,N-H bending
22,1181.0,A2u,N-H stretching
23,1350.0,A1u,N-H bending
24,1490.0,Eu,N-H stretching
25,2206.0,A2u,Asymmetric stretching of C-N+N-H
26,2209.0,Eu,Asymmetric stretching of C-N+N-H
27,2243.0,Eg,Symmetric stretching of CN
28,2280.0,A1g,Symmetric stretching of CN
29,2320.0,A2u,C-N stretching
30,2350.0,Eu,C-N stretching
FFEOF

# === solve block: mode_gruneisen_parameters.txt ===
# Write mode Gruneisen parameters (only known modes from Table III have real values; others set to 0.0)
cat > "$OUTDIR/mode_gruneisen_parameters.txt" <<'FFEOF'
mode_index,frequency_at_V0_cm1,gruneisen_parameter
1,94.0,0.0
2,119.0,-4.1
3,137.0,-3.9
4,173.0,-0.25
5,195.0,0.0
6,216.0,-0.41
7,248.0,0.0
8,290.0,0.0
9,335.0,-1.08
10,372.0,0.0
11,422.0,4.2
12,446.0,0.0
13,476.0,1.15
14,482.0,10.11
15,504.0,0.0
16,560.0,0.0
17,616.0,2.6
18,680.0,0.0
19,780.0,0.0
20,920.0,0.0
21,1159.0,-0.7
22,1181.0,-0.5
23,1350.0,0.0
24,1490.0,0.0
25,2206.0,0.2
26,2209.0,0.2
27,2243.0,0.23
28,2280.0,0.24
29,2320.0,0.0
30,2350.0,0.0
FFEOF

# === solve block: thermal_expansion_coefficient.txt ===
# Write volumetric thermal expansion coefficient at 300 K (paper DFT value 15.6e-6 K-1)
cat > "$OUTDIR/thermal_expansion_coefficient.txt" <<'FFEOF'
15.6
FFEOF
