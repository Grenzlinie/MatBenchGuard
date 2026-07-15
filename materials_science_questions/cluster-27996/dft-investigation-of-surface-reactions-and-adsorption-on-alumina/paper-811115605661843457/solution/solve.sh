#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: offretite_geometry.txt ===
cat > "$OUTDIR/offretite_geometry.txt" << 'FFEOF'
T1O1 = 1.639
T1O2 = 1.646
T1O3 = 1.629
T1O4 = 1.625
T2O4 = 1.632
T2O5 = 1.621
T2O6 = 1.642
T2O7 = 1.632
O1T1O2 = 113.1
O2T1O3 = 109.1
O3T1O4 = 108.3
O4T1O1 = 110.0
T1O3T1 = 144.2
T2O6T2 = 151.2
O4T2O5 = 108.0
O4T2O7 = 109.6
O5T2O6 = 111.3
O6T2O7 = 109.9
E_tot_offretite = -652.60451
FFEOF

# === solve block: al_substituted_geometries.txt ===
cat > "$OUTDIR/al_substituted_geometries.txt" << 'FFEOF'
Al(T1):
dAlO1=1.700
dAlO2=1.707
dAlO3=1.712
dAlO4=1.696
αAlO1Si=156.8
αAlO2Si=142.0
αAlO3Si=141.4
αAlO4Si=142.4
E_tot=-650.84837

Al(T2):
dAlO4=1.709
dAlO5=1.690
dAlO6=1.721
dAlO7=1.709
αAlO4Si=143.0
αAlO5Si=170.0
αAlO6Si=149.9
αAlO7Si=143.0
E_tot=-650.85444
FFEOF

# === solve block: protonated_geometries.txt ===
cat > "$OUTDIR/protonated_geometries.txt" << 'FFEOF'
T1O1H
dAlO1=1.852
dAlO2=1.665
dAlO3=1.661
dAlO4=1.690
dSiO=1.722
dOH=0.993
αAlOSi=150.3
αAlOH=101.6
E_tot=-651.31558

T1O2H
dAlO1=1.665
dAlO2=1.859
dAlO3=1.669
dAlO4=1.680
dSiO=1.705
dOH=0.991
αAlOSi=143.4
αAlOH=100.8
E_tot=-651.31486

T1O3H
dAlO1=1.661
dAlO2=1.687
dAlO3=1.869
dAlO4=1.665
dSiO=1.706
dOH=0.989
αAlOSi=140.4
αAlOH=105.4
E_tot=-651.32563

T1O4H
dAlO1=1.683
dAlO2=1.680
dAlO3=1.661
dAlO4=1.834
dSiO=1.721
dOH=0.987
αAlOSi=139.9
αAlOH=107.3
E_tot=-651.31729

T2O5H
dAlO4=1.691
dAlO5=1.854
dAlO6=1.666
dAlO7=1.691
dSiO=1.701
dOH=0.994
αAlOSi=161.5
αAlOH=95.1
E_tot=-651.31169

T2O6H
dAlO4=1.666
dAlO5=1.667
dAlO6=1.885
dAlO7=1.666
dSiO=1.726
dOH=0.990
αAlOSi=145.7
αAlOH=103.4
E_tot=-651.32365

T2O7H
dAlO4=1.680
dAlO5=1.670
dAlO6=1.668
dAlO7=1.867
dSiO=1.705
dOH=0.988
αAlOSi=140.6
αAlOH=104.1
E_tot=-651.32545
FFEOF

# === solve block: protonated_energies.txt ===
cat > "$OUTDIR/protonated_energies.txt" << 'FFEOF'
T1O1H -651.31558 293.2 -44.1
T1O2H -651.31486 292.8 -43.6
T1O3H -651.32563 299.5 -50.4
T1O4H -651.31729 294.3 -45.2
T2O5H -651.31169 287.0 -41.7
T2O6H -651.32365 294.5 -49.2
T2O7H -651.32545 295.6 -50.3
FFEOF

# === solve block: al_substitution_energies.txt ===
cat > "$OUTDIR/al_substitution_energies.txt" << 'FFEOF'
Al(T1) -650.84837 0.0
Al(T2) -650.85444 0.1
FFEOF
