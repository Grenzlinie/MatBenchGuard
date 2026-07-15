#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lattice_energies.csv ===
cat > /app/outputs/lattice_energies.csv << 'CSVEOF'
I2,U_exp,U_theo,compound,delta,structure_type
10.00,566,561,BaF2,+5,fluorite
11.026,588,592,SrF2,-4,fluorite
11.87,624,622,CaF2,+2,fluorite
15.03,595,584,PbF2,+11,fluorite
16.904,662,634,CdF2,+28,fluorite
18.751,655,626,HgF2,+29,fluorite
11.026,506,496,SrCl2,+10,fluorite
11.87,492,455,CaI2,+37,cadmium iodide
15.03,510,460,PbI2,+50,cadmium iodide
16.904,576,477,CdI2,+99,cadmium iodide
15.03,695,684,MgF2,+11,rutile
15.64,662,662,MnF2,0,rutile
16.18,696,681,FeF2,+15,rutile
17.05,708,688,CoF2,+20,rutile
17.96,710,688,ZnF2,+22,rutile
18.15,728,694,NiF2,+34,rutile
20.29,727,627,CuF2,+100,fluorite
15.03,575,513,MgBr2,+62,cadmium iodide
15.64,583,522,MnBr2,+61,cadmium iodide
16.18,607,530,FeBr2,+77,cadmium iodide
17.05,624,536,CoBr2,+88,cadmium iodide
13.57,548,486,Til2,+62,cadmium iodide
15.03,549,476,MgI2,+73,cadmium iodide
15.64,563,481,MnI2,+82,cadmium iodide
16.18,589,493,FeI2,+96,cadmium iodide
17.05,605,502,CoI2,+103,cadmium iodide
CSVEOF
