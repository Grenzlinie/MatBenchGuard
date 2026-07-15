#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: corrected_frequencies.csv ===
cat > "$OUTDIR/corrected_frequencies.csv" <<'CSVEOF'
mode_index,corrected_frequency
1,3444
2,3347
3,3015
4,2999
5,2987
6,2977
7,2946
8,2922
9,2870
10,1624
11,1598
12,1579
13,1495
14,1485
15,1474
16,1446
17,1390
18,1314
19,1297
20,1279
21,1166
22,1163
23,1104
24,1062
25,1039
26,995
27,1002
28,949
29,935
30,863
31,849
32,779
33,741
34,700
35,588
36,555
37,534
38,523
39,445
40,423
41,288
42,274
43,223
44,202
45,44
CSVEOF
