#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: table_1nn_orbital_states.csv ===
cat > "$OUTDIR/table_1nn_orbital_states.csv" <<'EOF'
configuration,c3v_reduction,d3h_representation,allowed_spin
"(⁴A₂g,⁴A₂g)⁰","(A₂,A₂)⁰","A₁′","0,1,2,3"
"(⁴A₂g,²E_g)","(A₂,E)","E′+E″","1,2"
"(⁴A₂g,²T₁g)","{(A₂,(A₂+E)}=(A₂,A₂)+(A₂,E)","A₁′+A₂″+E′+E″","1,2"
"(²E_g,²E_g)⁰","(E,E)⁰","A₁′+A₁″+E′","0,1"
"(²E_g,²T₁g)","{E,(A₂+E)}=(E,A₂)+(E,E)","E′+E″+A₁′+A₂′+E′+A₁″+A₂″+E″","0,1"
"(²T₁g,²T₁g)⁰","{(A₂+E),(A₂+E)}⁰=(A₂,A₂)⁰+(E,E)⁰+(A₂,E)","A₁′+A₁′+A₁″+E′+E′+E″","0,1"
"(²E_g,²T₂g)","{E,(A₁+E)}=(E,A₁)+(E,E)","E′+E″+A₁′+A₂′+E′+A₁″+A₂″+E″","0,1"
EOF

# === solve block: table_1nn_selection_rules.csv ===
cat > "$OUTDIR/table_1nn_selection_rules.csv" <<'EOF'
initial_repr,final_repr,polarization,allowed
"A₁′","A₁′","",false
"A₁′","A₂′","",false
"A₁′","E′","(x,y)",true
"A₁′","A₁″","",false
"A₁′","A₂″","z",true
"A₁′","E″","",false
"A₂′","A₁′","",false
"A₂′","A₂′","",false
"A₂′","E′","(x,y)",true
"A₂′","A₁″","z",true
"A₂′","A₂″","",false
"A₂′","E″","",false
"E′","A₁′","(x,y)",true
"E′","A₂′","(x,y)",true
"E′","E′","(x,y)",true
"E′","A₁″","",false
"E′","A₂″","",false
"E′","E″","z",true
"A₁″","A₁′","",false
"A₁″","A₂′","z",true
"A₁″","E′","",false
"A₁″","A₁″","",false
"A₁″","A₂″","",false
"A₁″","E″","(x,y)",true
"A₂″","A₁′","z",true
"A₂″","A₂′","",false
"A₂″","E′","",false
"A₂″","A₁″","",false
"A₂″","A₂″","",false
"A₂″","E″","(x,y)",true
"E″","A₁′","",false
"E″","A₂′","",false
"E″","E′","z",true
"E″","A₁″","(x,y)",true
"E″","A₂″","(x,y)",true
"E″","E″","(x,y)",true
EOF

# === solve block: table_2nn_orbital_states.csv ===
cat > "$OUTDIR/table_2nn_orbital_states.csv" <<'EOF'
configuration,c2v_reduction,d2h_representation,allowed_spin
"(⁴A₂g,⁴A₂g)⁰","(B₁,B₁)⁰","A_g","0,1,2,3"
"(⁴A₂g,²E_g)","{B₁,(A₁+B₁)}=(A₁,B₁)+(B₁,B₁)","B_2g+B_3u+A_g+B_1u","1,2"
"(⁴A₂g,²T₁g)","{B₁,(A₂+B₁+B₂)}=(A₂,B₁)+(B₁,B₁)+(B₁,B₂)","B_3g+B_2u+A_g+B_1u+B_1g+A_u","1,2"
"(²E_g,²E_g)⁰","{(A₁+B₁),(A₁+B₁)}⁰=(A₁,A₁)⁰+(B₁,B₁)⁰+(A₁,B₁)","A_g+A_g+B_2g+B_3u","0,1"
"(²E_g,²T₁g)","{(A₁+B₁),(A₂+B₁+B₂)}=(A₁,A₂)+(A₁,B₁)+(A₁,B₂)+(A₂,B₁)+(B₁,B₁)+(B₁,B₂)","B_1g+A_u+B_2g+B_3u+B_3g+B_2u+B_3g+B_2u+A_g+B_1u+B_1g+A_u","0,1"
"(²T₁g,²T₁g)⁰","{(A₂+B₁+B₂),(A₂+B₁+B₂)}⁰=(A₂,A₂)⁰+(B₁,B₁)⁰+(B₂,B₂)⁰+(A₂,B₁)+(A₂,B₂)+(B₁,B₂)","A_g+A_g+A_g+B_3g+B_2u+B_2g+B_3u+B_1g+A_u","0,1"
"(²E_g,²T₂g)","{(A₁+B₁),(A₁+A₂+B₂)}=(A₁,A₁)+(A₁,A₂)+(A₁,B₂)+(A₁,B₁)+(A₂,B₁)+(B₁,B₂)","A_g+B_1u+B_1g+A_u+B_3g+B_2u+B_2g+B_3u+B_3g+B_2u+B_1g+A_u","0,1"
EOF

# === solve block: table_2nn_selection_rules.csv ===
cat > "$OUTDIR/table_2nn_selection_rules.csv" <<'EOF'
initial_repr,final_repr,polarization,allowed
"A_g","A_g","",false
"A_g","B_1g","",false
"A_g","B_2g","",false
"A_g","B_3g","",false
"A_g","A_u","",false
"A_g","B_1u","z",true
"A_g","B_2u","y",true
"A_g","B_3u","x",true
"B_1g","A_g","",false
"B_1g","B_1g","",false
"B_1g","B_2g","",false
"B_1g","B_3g","",false
"B_1g","A_u","z",true
"B_1g","B_1u","",false
"B_1g","B_2u","x",true
"B_1g","B_3u","y",true
"B_2g","A_g","",false
"B_2g","B_1g","",false
"B_2g","B_2g","",false
"B_2g","B_3g","",false
"B_2g","A_u","y",true
"B_2g","B_1u","x",true
"B_2g","B_2u","",false
"B_2g","B_3u","z",true
"B_3g","A_g","",false
"B_3g","B_1g","",false
"B_3g","B_2g","",false
"B_3g","B_3g","",false
"B_3g","A_u","x",true
"B_3g","B_1u","y",true
"B_3g","B_2u","z",true
"B_3g","B_3u","",false
"A_u","A_g","",false
"A_u","B_1g","z",true
"A_u","B_2g","y",true
"A_u","B_3g","x",true
"A_u","A_u","",false
"A_u","B_1u","",false
"A_u","B_2u","",false
"A_u","B_3u","",false
"B_1u","A_g","z",true
"B_1u","B_1g","",false
"B_1u","B_2g","x",true
"B_1u","B_3g","y",true
"B_1u","A_u","",false
"B_1u","B_1u","",false
"B_1u","B_2u","",false
"B_1u","B_3u","",false
"B_2u","A_g","y",true
"B_2u","B_1g","x",true
"B_2u","B_2g","",false
"B_2u","B_3g","z",true
"B_2u","A_u","",false
"B_2u","B_1u","",false
"B_2u","B_2u","",false
"B_2u","B_3u","",false
"B_3u","A_g","x",true
"B_3u","B_1g","y",true
"B_3u","B_2g","z",true
"B_3u","B_3g","",false
"B_3u","A_u","",false
"B_3u","B_1u","",false
"B_3u","B_2u","",false
"B_3u","B_3u","",false
EOF
