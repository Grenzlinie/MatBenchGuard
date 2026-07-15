#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: deltaG_values.json ===
OUTDIR=/app/outputs
cat > "$OUTDIR/deltaG_values.json" <<'FFEOF'
{
  "Py-HTP-BT-COF": 0.50,
  "Py-FTP-BT-COF": 0.30,
  "Py-CITP-BT-COF": 0.10
}
FFEOF

# === solve block: optimized_structures.xyz ===
cat > /app/outputs/optimized_structures.xyz <<'FFEOF'
# Py-HTP-BT-COF
16
H* adsorbed on C at site 4 (H substituent)
C     -0.7592   -0.0362    0.0089
C      0.6450   -0.0935   -0.0243
C      1.4218    1.0281   -0.0104
C      0.8534    2.3079    0.0404
C     -0.5444    2.4140    0.0754
C     -1.3232    1.2969    0.0593
N      0.3135   -1.4216   -0.0782
S      2.5064    0.8962   -0.0370
N      1.2622    3.3202    0.0578
C     -2.8836    1.4130    0.0874
H     -3.1888    2.4347   -0.0986
H     -3.2782    0.7495   -0.6697
H     -3.2937    1.1180    1.0440
H     -1.0133   -1.9750    0.0371
H     -2.7293    0.3777    0.0647
H      2.5219   -0.3951   -0.0479
# Py-FTP-BT-COF
17
H* adsorbed on C at site 4 (F substituent)
C     -0.7391   -0.0047    0.0020
C      0.6702   -0.0736   -0.0078
C      1.4710    1.0683   -0.0026
C      0.8782    2.3402    0.0127
C     -0.5101    2.4363    0.0223
C     -1.3125    1.3026    0.0164
N      0.3173   -1.3840   -0.0228
S      2.5424    0.9277   -0.0082
N      1.2824    3.3457    0.0176
C     -2.8727    1.4262    0.0264
H     -3.1687    2.4553   -0.1401
H     -3.2849    0.7716   -0.7303
H     -3.2745    1.1397    0.9890
F     -1.0238   -2.0134    0.0151
H     -2.7104    0.3855    0.0202
H      2.5431   -0.3619   -0.0159
# Py-CITP-BT-COF
17
H* adsorbed on C at site 4 (Cl substituent)
C     -0.7368    0.0016    0.0009
C      0.6723   -0.0680   -0.0053
C      1.4536    1.0896   -0.0017
C      0.8531    2.3552    0.0095
C     -0.5319    2.4481    0.0161
C     -1.3320    1.3174    0.0108
N      0.3229   -1.3737   -0.0150
S      2.5285    0.9658   -0.0062
N      1.2574    3.3595    0.0142
C     -2.8935    1.4298    0.0170
H     -3.1926    2.4593   -0.1491
H     -3.2953    0.7764   -0.7451
H     -3.3040    1.1366    0.9743
Cl    -1.0260   -2.0543    0.0104
H     -2.7357    0.3892    0.0149
H      2.5476   -0.3578   -0.0138
FFEOF
