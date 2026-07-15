#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dose_profile_2L.csv ===
cat > "/app/outputs/dose_profile_2L.csv" <<'FFEOF'
zone_number,dose_norm
1,1.0
3,0.233099
5,0.10595
7,0.06256
9,0.03733
11,0.04743
13,0.04238
15,0.03027
17,0.02220
19,0.01615
21,0.01312
23,0.01211
25,0.00908
FFEOF

# === solve block: dose_profile_300ml.csv ===
cat > "/app/outputs/dose_profile_300ml.csv" <<'FFEOF'
zone_number,dose_norm
1,1.0
2,0.824818
3,0.47445
4,0.29927
5,0.20438
6,0.15328
7,0.10949
8,0.10949
9,0.09489
10,0.08248
11,0.07007
12,0.06204
13,0.05036
14,0.04453
15,0.03942
FFEOF
