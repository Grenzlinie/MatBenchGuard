#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: planar_energies.csv ===
cat > /app/outputs/planar_energies.csv <<'CSVEOF'
phase,layer_index,layer_label,energy
Al(001),0,Al,-3.7800
Al(001),1,As,-3.7800
Al(001),2,Al,-3.7800
Al(001),3,As,-3.7780
Al(001),4,Al,-3.2706
Al(001),5,Al,-3.3031
Al(001),6,Al,-3.3892
Al(001),7,Al,-3.3893
Al(001),8,Al,-3.3893
Al(001),9,Al,-3.3893
Al(001)L,0,Al,-3.7799
Al(001)L,1,As,-3.7799
Al(001)L,2,Al,-3.7788
Al(001)L,3,As,-3.7649
Al(001)L,4,Al,-3.1479
Al(001)L,5,Al,-3.2370
Al(001)L,6,Al,-3.3620
Al(001)L,7,Al,-3.3860
Al(001)L,8,Al,-3.3888
Al(001)L,9,Al,-3.3882
Al(110),0,Al,-3.7800
Al(110),1,As,-3.7799
Al(110),2,Al,-3.7782
Al(110),3,As,-3.7546
Al(110),4,Al,-3.2442
Al(110),5,Al,-3.2113
Al(110),6,Al,-3.3149
Al(110),7,Al,-3.3417
Al(110),8,Al,-3.3429
Al(110),9,Al,-3.3427
Al(110)R,0,Al,-3.7800
Al(110)R,1,As,-3.7800
Al(110)R,2,Al,-3.7796
Al(110)R,3,As,-3.7767
Al(110)R,4,Al,-3.3075
Al(110)R,5,Al,-3.0019
Al(110)R,6,Al,-3.2082
Al(110)R,7,Al,-3.3136
Al(110)R,8,Al,-3.3395
Al(110)R,9,Al,-3.3426
Al(001)/In,0,Al,-3.7800
Al(001)/In,1,As,-3.7800
Al(001)/In,2,Al,-3.7799
Al(001)/In,3,As,-3.3431
Al(001)/In,4,In,-2.7105
Al(001)/In,5,Al,-3.1835
Al(001)/In,6,Al,-3.3893
Al(001)/In,7,Al,-3.3892
Al(001)/In,8,Al,-3.3892
Al(001)/In,9,Al,-3.3892
Al(110)/In,0,Al,-3.7800
Al(110)/In,1,As,-3.7793
Al(110)/In,2,Al,-3.7636
Al(110)/In,3,As,-3.3419
Al(110)/In,4,In,-2.4691
Al(110)/In,5,Al,-3.0182
Al(110)/In,6,Al,-3.2804
Al(110)/In,7,Al,-3.3378
Al(110)/In,8,Al,-3.3421
Al(110)/In,9,Al,-3.3413
CSVEOF
