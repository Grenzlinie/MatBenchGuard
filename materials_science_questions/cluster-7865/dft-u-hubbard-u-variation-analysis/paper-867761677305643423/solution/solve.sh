#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: total_moments.csv ===
cat > /app/outputs/total_moments.csv <<'EOF'
n,total_moment_per_atom
9,1.45
10,1.50
11,1.45
12,1.35
13,0.75
14,1.15
15,1.20
16,1.25
17,1.30
18,1.25
19,1.15
20,1.20
22,1.05
23,0.95
24,0.90
25,0.85
26,0.80
27,0.85
28,0.70
30,0.80
31,0.85
32,0.90
34,0.65
35,0.80
36,0.85
38,0.85
39,0.90
41,0.85
42,0.80
43,0.75
44,0.80
45,0.85
46,0.90
47,0.85
48,0.80
49,0.75
50,0.70
51,0.75
52,0.80
53,0.85
54,0.90
55,0.85
56,0.75
57,0.80
58,0.85
60,0.90
EOF
