#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: cohesive_energies.csv ===
cat > /app/outputs/cohesive_energies.csv <<'FFEOF'
buckling_height_delta_A,cohesive_energy_eV_per_atom,element,lattice_constant_a_A,structure
0.0,1.311,Li,3.091,HX
1.159,1.561,Li,3.102,bHC
1.085,1.538,Li,2.960,bSQ
0.0,2.997,Be,2.126,HX
0.959,3.354,Be,2.157,bHC
0.799,3.181,Be,2.090,bSQ
0.0,2.706,Sc,3.149,HX
1.199,3.619,Sc,3.283,bHC
1.038,3.553,Sc,3.218,bSQ
0.0,4.450,Ti,2.674,HX
1.030,5.469,Ti,2.933,bHC
0.930,5.536,Ti,2.795,bSQ
0.0,5.845,V,2.445,HX
0.806,6.654,V,2.885,bHC
1.067,6.874,V,2.401,bSQ
0.702,6.947,V,2.886,3SQ
0.0,6.735,Cr,2.690,HX
0.716,7.388,Cr,2.788,bHC
1.053,7.411,Cr,2.280,bSQ
0.0,6.871,Mn,2.573,HX
0.921,7.437,Mn,2.447,bHC
0.604,7.119,Mn,2.618,bSQ
0.0,6.314,Fe,2.405,HX
0.927,6.903,Fe,2.400,bHC
0.969,6.893,Fe,2.391,bSQ
0.0,5.463,Co,2.355,HX
0.974,6.178,Co,2.441,bHC
0.874,5.901,Co,2.397,bSQ
0.0,4.253,Ni,2.355,HX
1.010,4.827,Ni,2.425,bHC
0.867,4.614,Ni,2.397,bSQ
0.0,3.154,Cu,2.428,HX
1.063,3.407,Cu,2.496,bHC
0.912,3.280,Cu,2.468,bSQ
0.0,0.862,Zn,2.538,HX
1.308,1.039,Zn,2.569,bHC
1.194,0.817,Zn,2.537,bSQ
0.0,2.842,Al,2.682,HX
1.227,3.217,Al,2.748,bHC
1.088,3.085,Al,2.713,bSQ
0.0,3.010,Sn,3.137,HX
1.300,3.353,Sn,3.315,bHC
1.195,3.339,Sn,3.196,bSQ
0.0,1.912,In,3.162,HX
1.459,2.165,In,3.226,bHC
1.382,2.136,In,3.069,bSQ
1.384,2.223,In,3.315,3HX
FFEOF

# === solve block: stability_classification.csv ===
cat > /app/outputs/stability_classification.csv <<'FFEOF'
element,stable,structure
Li,False,HX
Li,True,bHC
Li,False,bSQ
Be,True,HX
Be,True,bHC
Be,False,bSQ
Sc,False,HX
Sc,True,bHC
Sc,True,bSQ
Ti,False,HX
Ti,False,bHC
Ti,True,bSQ
V,False,HX
V,False,bHC
V,False,bSQ
V,True,3SQ
Cr,False,HX
Cr,True,bHC
Cr,False,bSQ
Mn,False,HX
Mn,True,bHC
Mn,True,bSQ
Fe,False,HX
Fe,True,bHC
Fe,False,bSQ
Co,False,HX
Co,True,bHC
Co,False,bSQ
Ni,False,HX
Ni,True,bHC
Ni,True,bSQ
Cu,True,HX
Cu,True,bHC
Cu,True,bSQ
Zn,True,HX
Zn,True,bHC
Zn,False,bSQ
Al,False,HX
Al,True,bHC
Al,True,bSQ
Sn,False,HX
Sn,True,bHC
Sn,False,bSQ
In,False,HX
In,False,bHC
In,False,bSQ
In,True,3HX
FFEOF
