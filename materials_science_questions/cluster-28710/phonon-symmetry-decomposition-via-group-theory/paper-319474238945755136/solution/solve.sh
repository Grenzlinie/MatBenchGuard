#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: selection_rules.json ===
python3 << 'PYEOF' > /app/outputs/selection_rules.json
import json

# star product decompositions (unordered pairs)
star_products = [
    {"star1":"k0","star2":"k0","decomposition":[{"star":"k0","multiplicity":1}]},
    {"star1":"k0","star2":"k3","decomposition":[{"star":"k3","multiplicity":1}]},
    {"star1":"k0","star2":"k4","decomposition":[{"star":"k4","multiplicity":1}]},
    {"star1":"k0","star2":"k9","decomposition":[{"star":"k9","multiplicity":1}]},
    {"star1":"k0","star2":"k10","decomposition":[{"star":"k10","multiplicity":1}]},
    {"star1":"k0","star2":"k11","decomposition":[{"star":"k11","multiplicity":1}]},
    {"star1":"k3","star2":"k3","decomposition":[{"star":"k3","multiplicity":2},{"star":"k0","multiplicity":2}]},
    {"star1":"k3","star2":"k4","decomposition":[{"star":"k0","multiplicity":3}]},
    {"star1":"k3","star2":"k9","decomposition":[{"star":"k3","multiplicity":1},{"star":"k0","multiplicity":1}]},
    {"star1":"k3","star2":"k10","decomposition":[{"star":"k0","multiplicity":1}]},
    {"star1":"k3","star2":"k11","decomposition":[{"star":"k3","multiplicity":1}]},
    {"star1":"k4","star2":"k4","decomposition":[{"star":"k4","multiplicity":2},{"star":"k0","multiplicity":2}]},
    {"star1":"k4","star2":"k9","decomposition":[{"star":"k4","multiplicity":1},{"star":"k0","multiplicity":1}]},
    {"star1":"k4","star2":"k10","decomposition":[{"star":"k4","multiplicity":2}]},
    {"star1":"k4","star2":"k11","decomposition":[{"star":"k4","multiplicity":1}]},
    {"star1":"k9","star2":"k9","decomposition":[{"star":"k9","multiplicity":2},{"star":"k11","multiplicity":3}]},
    {"star1":"k9","star2":"k10","decomposition":[{"star":"k4","multiplicity":1}]},
    {"star1":"k9","star2":"k11","decomposition":[{"star":"k9","multiplicity":1}]},
    {"star1":"k10","star2":"k10","decomposition":[{"star":"k10","multiplicity":1},{"star":"k11","multiplicity":2}]},
    {"star1":"k10","star2":"k11","decomposition":[{"star":"k10","multiplicity":1}]},
    {"star1":"k11","star2":"k11","decomposition":[{"star":"k11","multiplicity":1}]}
]

# ir product decompositions -- all given in the paper, plus trivial ones involving A1
ir_decomps = {}

# helper to add

def add(ir1,ir2,entries):
    ir_decomps[(ir1,ir2)] = entries

# products involving A1
for ir in ["F1","F2","B1","B2","U1","U2","U3","U4","P1","P2","P3","Δ1","Δ2","Δ3","Δ4","Δ5","Δ6"]:
    add("A1",ir,[(ir,1)])
    add(ir,"A1",[(ir,1)])
add("A1","A1",[("A1",1)])

# k3×k3
add("F1","F1",[("F1",2),("A1",2)])
add("F1","F2",[("F2",2),("A1",2)])
add("F2","F1",[("F2",2),("A1",2)])
add("F2","F2",[("F1",2),("A1",2)])

# k3×k4
add("F1","B1",[("A1",3)])
add("F1","B2",[("A1",3)])
add("F2","B1",[("A1",3)])
add("F2","B2",[("A1",3)])
add("B1","F1",[("A1",3)])
add("B1","F2",[("A1",3)])
add("B2","F1",[("A1",3)])
add("B2","F2",[("A1",3)])

# k3×k9
add("F1","U1",[("F1",1),("A1",1)])
add("F1","U2",[("F2",1),("A1",1)])
add("F1","U3",[("F1",1),("A1",1)])
add("F1","U4",[("F2",1),("A1",1)])
add("F2","U1",[("F2",1),("A1",1)])
add("F2","U2",[("F1",1),("A1",1)])
add("F2","U3",[("F2",1),("A1",1)])
add("F2","U4",[("F1",1),("A1",1)])
add("U1","F1",[("F1",1),("A1",1)])
add("U1","F2",[("F2",1),("A1",1)])
add("U2","F1",[("F2",1),("A1",1)])
add("U2","F2",[("F1",1),("A1",1)])
add("U3","F1",[("F1",1),("A1",1)])
add("U3","F2",[("F2",1),("A1",1)])
add("U4","F1",[("F2",1),("A1",1)])
add("U4","F2",[("F1",1),("A1",1)])

# k3×k10
add("F1","P1",[("A1",1)])
add("F1","P2",[("A1",1)])
add("F1","P3",[("A1",2)])
add("F2","P1",[("A1",1)])
add("F2","P2",[("A1",1)])
add("F2","P3",[("A1",2)])
add("P1","F1",[("A1",1)])
add("P1","F2",[("A1",1)])
add("P2","F1",[("A1",1)])
add("P2","F2",[("A1",1)])
add("P3","F1",[("A1",2)])
add("P3","F2",[("A1",2)])

# k3×k11
add("F1","Δ1",[("F1",1)])
add("F1","Δ2",[("F2",1)])
add("F1","Δ3",[("F1",1)])
add("F1","Δ4",[("F2",1)])
add("F1","Δ5",[("F1",1),("F2",1)])
add("F1","Δ6",[("F1",1),("F2",1)])
add("F2","Δ1",[("F2",1)])
add("F2","Δ2",[("F1",1)])
add("F2","Δ3",[("F2",1)])
add("F2","Δ4",[("F1",1)])
add("F2","Δ5",[("F1",1),("F2",1)])
add("F2","Δ6",[("F1",1),("F2",1)])
add("Δ1","F1",[("F1",1)])
add("Δ1","F2",[("F2",1)])
add("Δ2","F1",[("F2",1)])
add("Δ2","F2",[("F1",1)])
add("Δ3","F1",[("F1",1)])
add("Δ3","F2",[("F2",1)])
add("Δ4","F1",[("F2",1)])
add("Δ4","F2",[("F1",1)])
add("Δ5","F1",[("F1",1),("F2",1)])
add("Δ5","F2",[("F1",1),("F2",1)])
add("Δ6","F1",[("F1",1),("F2",1)])
add("Δ6","F2",[("F1",1),("F2",1)])

# k4×k4
add("B1","B1",[("B1",2),("A1",2)])
add("B1","B2",[("B2",2),("A1",2)])
add("B2","B1",[("B2",2),("A1",2)])
add("B2","B2",[("B1",2),("A1",2)])

# k4×k9
add("B1","U1",[("B1",1),("A1",1)])
add("B1","U2",[("B1",1),("A1",1)])
add("B1","U3",[("B2",1),("A1",1)])
add("B1","U4",[("B2",1),("A1",1)])
add("B2","U1",[("B2",1),("A1",1)])
add("B2","U2",[("B2",1),("A1",1)])
add("B2","U3",[("B1",1),("A1",1)])
add("B2","U4",[("B1",1),("A1",1)])
add("U1","B1",[("B1",1),("A1",1)])
add("U1","B2",[("B2",1),("A1",1)])
add("U2","B1",[("B1",1),("A1",1)])
add("U2","B2",[("B2",1),("A1",1)])
add("U3","B1",[("B2",1),("A1",1)])
add("U3","B2",[("B1",1),("A1",1)])
add("U4","B1",[("B2",1),("A1",1)])
add("U4","B2",[("B1",1),("A1",1)])

# k4×k10
add("B1","P1",[("B1",2)])
add("B1","P2",[("B2",2)])
add("B1","P3",[("B1",2),("B2",2)])
add("B2","P1",[("B2",2)])
add("B2","P2",[("B1",2)])
add("B2","P3",[("B1",2),("B2",2)])
add("P1","B1",[("B1",2)])
add("P1","B2",[("B2",2)])
add("P2","B1",[("B2",2)])
add("P2","B2",[("B1",2)])
add("P3","B1",[("B1",2),("B2",2)])
add("P3","B2",[("B1",2),("B2",2)])

# k4×k11
add("B1","Δ1",[("B1",1)])
add("B1","Δ2",[("B2",1)])
add("B1","Δ3",[("B2",1)])
add("B1","Δ4",[("B1",1)])
add("B1","Δ5",[("B1",1),("B2",1)])
add("B1","Δ6",[("B1",1),("B2",1)])
add("B2","Δ1",[("B2",1)])
add("B2","Δ2",[("B1",1)])
add("B2","Δ3",[("B1",1)])
add("B2","Δ4",[("B2",1)])
add("B2","Δ5",[("B1",1),("B2",1)])
add("B2","Δ6",[("B1",1),("B2",1)])
add("Δ1","B1",[("B1",1)])
add("Δ1","B2",[("B2",1)])
add("Δ2","B1",[("B2",1)])
add("Δ2","B2",[("B1",1)])
add("Δ3","B1",[("B2",1)])
add("Δ3","B2",[("B1",1)])
add("Δ4","B1",[("B1",1)])
add("Δ4","B2",[("B2",1)])
add("Δ5","B1",[("B1",1),("B2",1)])
add("Δ5","B2",[("B1",1),("B2",1)])
add("Δ6","B1",[("B1",1),("B2",1)])
add("Δ6","B2",[("B1",1),("B2",1)])

# k9×k9
add("U1","U1",[("U1",1),("U4",1),("Δ1",1),("Δ5",1)])
add("U1","U2",[("U2",1),("U3",1),("Δ4",1),("Δ6",1)])
add("U1","U3",[("U2",1),("U3",1),("Δ3",1),("Δ6",1)])
add("U1","U4",[("U1",1),("U4",1),("Δ2",1),("Δ5",1)])
add("U2","U1",[("U2",1),("U3",1),("Δ4",1),("Δ6",1)])
add("U2","U2",[("U1",1),("U4",1),("Δ1",1),("Δ5",1)])
add("U2","U3",[("U1",1),("U4",1),("Δ2",1),("Δ5",1)])
add("U2","U4",[("U2",1),("U3",1),("Δ3",1),("Δ6",1)])
add("U3","U1",[("U2",1),("U3",1),("Δ3",1),("Δ6",1)])
add("U3","U2",[("U1",1),("U4",1),("Δ2",1),("Δ5",1)])
add("U3","U3",[("U1",1),("U4",1),("Δ1",1),("Δ5",1)])
add("U3","U4",[("U2",1),("U3",1),("Δ4",1),("Δ6",1)])
add("U4","U1",[("U1",1),("U4",1),("Δ2",1),("Δ5",1)])
add("U4","U2",[("U2",1),("U3",1),("Δ3",1),("Δ6",1)])
add("U4","U3",[("U2",1),("U3",1),("Δ4",1),("Δ6",1)])
add("U4","U4",[("U1",1),("U4",1),("Δ1",1),("Δ5",1)])

# k9×k10 (note k9×k10 = k4, so only ir products that land on k4 irs: B1,B2, and no extra star multiplicity)
add("U1","P1",[("B1",1)])
add("U1","P2",[("B2",1)])
add("U1","P3",[("B1",1),("B2",1)])
add("U2","P1",[("B1",1)])
add("U2","P2",[("B2",1)])
add("U2","P3",[("B1",1),("B2",1)])
add("U3","P1",[("B2",1)])
add("U3","P2",[("B1",1)])
add("U3","P3",[("B1",1),("B2",1)])
add("U4","P1",[("B2",1)])
add("U4","P2",[("B1",1)])
add("U4","P3",[("B1",1),("B2",1)])
add("P1","U1",[("B1",1)])
add("P1","U2",[("B1",1)])
add("P1","U3",[("B2",1)])
add("P1","U4",[("B2",1)])
add("P2","U1",[("B2",1)])
add("P2","U2",[("B2",1)])
add("P2","U3",[("B1",1)])
add("P2","U4",[("B1",1)])
add("P3","U1",[("B1",1),("B2",1)])
add("P3","U2",[("B1",1),("B2",1)])
add("P3","U3",[("B1",1),("B2",1)])
add("P3","U4",[("B1",1),("B2",1)])

# k9×k11
add("U1","Δ1",[("U1",1)])
add("U1","Δ2",[("U4",1)])
add("U1","Δ3",[("U3",1)])
add("U1","Δ4",[("U2",1)])
add("U1","Δ5",[("U1",1),("U4",1)])
add("U1","Δ6",[("U2",1),("U3",1)])
add("U2","Δ1",[("U2",1)])
add("U2","Δ2",[("U3",1)])
add("U2","Δ3",[("U4",1)])
add("U2","Δ4",[("U1",1)])
add("U2","Δ5",[("U2",1),("U3",1)])
add("U2","Δ6",[("U1",1),("U4",1)])
add("U3","Δ1",[("U3",1)])
add("U3","Δ2",[("U2",1)])
add("U3","Δ3",[("U1",1)])
add("U3","Δ4",[("U4",1)])
add("U3","Δ5",[("U2",1),("U3",1)])
add("U3","Δ6",[("U1",1),("U4",1)])
add("U4","Δ1",[("U4",1)])
add("U4","Δ2",[("U1",1)])
add("U4","Δ3",[("U2",1)])
add("U4","Δ4",[("U3",1)])
add("U4","Δ5",[("U1",1),("U4",1)])
add("U4","Δ6",[("U2",1),("U3",1)])
add("Δ1","U1",[("U1",1)])
add("Δ1","U2",[("U2",1)])
add("Δ1","U3",[("U3",1)])
add("Δ1","U4",[("U4",1)])
add("Δ2","U1",[("U4",1)])
add("Δ2","U2",[("U3",1)])
add("Δ2","U3",[("U2",1)])
add("Δ2","U4",[("U1",1)])
add("Δ3","U1",[("U3",1)])
add("Δ3","U2",[("U4",1)])
add("Δ3","U3",[("U1",1)])
add("Δ3","U4",[("U2",1)])
add("Δ4","U1",[("U2",1)])
add("Δ4","U2",[("U1",1)])
add("Δ4","U3",[("U4",1)])
add("Δ4","U4",[("U3",1)])
add("Δ5","U1",[("U1",1),("U4",1)])
add("Δ5","U2",[("U2",1),("U3",1)])
add("Δ5","U3",[("U2",1),("U3",1)])
add("Δ5","U4",[("U1",1),("U4",1)])
add("Δ6","U1",[("U2",1),("U3",1)])
add("Δ6","U2",[("U1",1),("U4",1)])
add("Δ6","U3",[("U1",1),("U4",1)])
add("Δ6","U4",[("U2",1),("U3",1)])

# k10×k10
add("P1","P1",[("P1",1),("Δ1",1),("Δ4",1)])
add("P1","P2",[("P2",1),("Δ2",1),("Δ3",1)])
add("P1","P3",[("P3",1),("Δ5",1),("Δ6",1)])
add("P2","P1",[("P2",1),("Δ2",1),("Δ3",1)])
add("P2","P2",[("P1",1),("Δ1",1),("Δ4",1)])
add("P2","P3",[("P3",1),("Δ5",1),("Δ6",1)])
add("P3","P1",[("P3",1),("Δ5",1),("Δ6",1)])
add("P3","P2",[("P3",1),("Δ5",1),("Δ6",1)])
add("P3","P3",[("P1",1),("P2",1),("P3",1),("Δ1",1),("Δ2",1),("Δ3",1),("Δ4",1),("Δ5",1),("Δ6",1)])

# k10×k11
add("P1","Δ1",[("P1",1)])
add("P1","Δ2",[("P2",1)])
add("P1","Δ3",[("P2",1)])
add("P1","Δ4",[("P1",1)])
add("P1","Δ5",[("P3",1)])
add("P1","Δ6",[("P3",1)])
add("P2","Δ1",[("P2",1)])
add("P2","Δ2",[("P1",1)])
add("P2","Δ3",[("P1",1)])
add("P2","Δ4",[("P2",1)])
add("P2","Δ5",[("P3",1)])
add("P2","Δ6",[("P3",1)])
add("P3","Δ1",[("P3",1)])
add("P3","Δ2",[("P3",1)])
add("P3","Δ3",[("P3",1)])
add("P3","Δ4",[("P3",1)])
add("P3","Δ5",[("P1",1),("P2",1),("P3",1)])
add("P3","Δ6",[("P1",1),("P2",1),("P3",1)])
add("Δ1","P1",[("P1",1)])
add("Δ1","P2",[("P2",1)])
add("Δ1","P3",[("P3",1)])
add("Δ2","P1",[("P2",1)])
add("Δ2","P2",[("P1",1)])
add("Δ2","P3",[("P3",1)])
add("Δ3","P1",[("P2",1)])
add("Δ3","P2",[("P1",1)])
add("Δ3","P3",[("P3",1)])
add("Δ4","P1",[("P1",1)])
add("Δ4","P2",[("P2",1)])
add("Δ4","P3",[("P3",1)])
add("Δ5","P1",[("P3",1)])
add("Δ5","P2",[("P3",1)])
add("Δ5","P3",[("P1",1),("P2",1),("P3",1)])
add("Δ6","P1",[("P3",1)])
add("Δ6","P2",[("P3",1)])
add("Δ6","P3",[("P1",1),("P2",1),("P3",1)])

# k11×k11
add("Δ1","Δ1",[("Δ1",1)])
add("Δ1","Δ2",[("Δ2",1)])
add("Δ1","Δ3",[("Δ3",1)])
add("Δ1","Δ4",[("Δ4",1)])
add("Δ1","Δ5",[("Δ5",1)])
add("Δ1","Δ6",[("Δ6",1)])
add("Δ2","Δ1",[("Δ2",1)])
add("Δ2","Δ2",[("Δ1",1)])
add("Δ2","Δ3",[("Δ4",1)])
add("Δ2","Δ4",[("Δ3",1)])
add("Δ2","Δ5",[("Δ5",1)])
add("Δ2","Δ6",[("Δ6",1)])
add("Δ3","Δ1",[("Δ3",1)])
add("Δ3","Δ2",[("Δ4",1)])
add("Δ3","Δ3",[("Δ1",1)])
add("Δ3","Δ4",[("Δ2",1)])
add("Δ3","Δ5",[("Δ6",1)])
add("Δ3","Δ6",[("Δ5",1)])
add("Δ4","Δ1",[("Δ4",1)])
add("Δ4","Δ2",[("Δ3",1)])
add("Δ4","Δ3",[("Δ2",1)])
add("Δ4","Δ4",[("Δ1",1)])
add("Δ4","Δ5",[("Δ6",1)])
add("Δ4","Δ6",[("Δ5",1)])
add("Δ5","Δ1",[("Δ5",1)])
add("Δ5","Δ2",[("Δ5",1)])
add("Δ5","Δ3",[("Δ6",1)])
add("Δ5","Δ4",[("Δ6",1)])
add("Δ5","Δ5",[("Δ1",1),("Δ2",1),("Δ5",1)])
add("Δ5","Δ6",[("Δ3",1),("Δ4",1),("Δ6",1)])
add("Δ6","Δ1",[("Δ6",1)])
add("Δ6","Δ2",[("Δ6",1)])
add("Δ6","Δ3",[("Δ5",1)])
add("Δ6","Δ4",[("Δ5",1)])
add("Δ6","Δ5",[("Δ3",1),("Δ4",1),("Δ6",1)])
add("Δ6","Δ6",[("Δ1",1),("Δ2",1),("Δ5",1)])

# assemble ir_products list
ir_products = []
for (ir1,ir2),decomp in ir_decomps.items():
    ir_products.append({
        "ir1": ir1,
        "ir2": ir2,
        "decomposition": [{"ir": ir, "multiplicity": mult} for ir,mult in decomp]
    })

result = {
    "star_products": star_products,
    "ir_products": ir_products
}

print(json.dumps(result, ensure_ascii=False, indent=2))
PYEOF

# === solve block: cgc_table.json ===
python3 << 'PYEOF' > $OUTDIR/cgc_table.json
import json
import sys

rows = [
    {"i":"k1","j":"k1",
     "U1_k1":"1/sqrt(2)","U1_k2":"eta/sqrt(2)","U1_k3":"phi/sqrt(2)",
     "U4_k1":"1/sqrt(2)","U4_k2":"-eta/sqrt(2)","U4_k3":"phi/sqrt(2)",
     "Delta1_k1pp":"1/sqrt(3)","Delta5_k1pp_1":"1/sqrt(3)","Delta5_k1pp_2":"1/sqrt(3)"},

    {"i":"k1","j":"k2",
     "U1_k1":"1/sqrt(2)","U1_k2":"eta/sqrt(2)","U1_k3":"phi/sqrt(2)",
     "U4_k1":"1/sqrt(2)","U4_k2":"-eta/sqrt(2)","U4_k3":"phi/sqrt(2)",
     "Delta1_k1pp":"phi/sqrt(3)","Delta5_k1pp_1":"-omega*phi/sqrt(3)","Delta5_k1pp_2":"omega*^2 phi/sqrt(3)"},

    {"i":"k1","j":"k3",
     "U1_k1":"1/sqrt(2)","U1_k2":"eta/sqrt(2)","U1_k3":"-1/sqrt(2)",
     "U4_k1":"1/sqrt(2)","U4_k2":"-eta/sqrt(2)","U4_k3":"0",
     "Delta1_k1pp":"phi/sqrt(3)","Delta5_k1pp_1":"-omega*phi/sqrt(3)","Delta5_k1pp_2":"omega*^2 phi/sqrt(3)"},

    {"i":"k2","j":"k1",
     "U1_k1":"1/sqrt(2)","U1_k2":"eta/sqrt(2)","U1_k3":"1/sqrt(2)",
     "U4_k1":"1/sqrt(2)","U4_k2":"0","U4_k3":"0",
     "Delta1_k1pp":"phi/sqrt(3)","Delta5_k1pp_1":"-omega*phi/sqrt(3)","Delta5_k1pp_2":"omega*^2 phi/sqrt(3)"},

    {"i":"k2","j":"k2",
     "U1_k1":"1/sqrt(2)","U1_k2":"0","U1_k3":"0",
     "U4_k1":"eta/sqrt(2)","U4_k2":"0","U4_k3":"eta/sqrt(2)",
     "Delta1_k1pp":"phi/sqrt(3)","Delta5_k1pp_1":"-omega*phi/sqrt(3)","Delta5_k1pp_2":"omega*^2 phi/sqrt(3)"},

    {"i":"k2","j":"k3",
     "U1_k1":"1/sqrt(2)","U1_k2":"0","U1_k3":"0",
     "U4_k1":"eta/sqrt(2)","U4_k2":"0","U4_k3":"eta/sqrt(2)",
     "Delta1_k1pp":"phi/sqrt(3)","Delta5_k1pp_1":"-omega*phi/sqrt(3)","Delta5_k1pp_2":"omega*^2 phi/sqrt(3)"},

    {"i":"k3","j":"k1",
     "U1_k1":"phi/sqrt(2)","U1_k2":"0","U1_k3":"0",
     "U4_k1":"-phi/sqrt(2)","U4_k2":"0","U4_k3":"0",
     "Delta1_k1pp":"1/sqrt(3)","Delta5_k1pp_1":"omega*^2/sqrt(3)","Delta5_k1pp_2":"-omega*/sqrt(3)"},

    {"i":"k3","j":"k2",
     "U1_k1":"phi/sqrt(2)","U1_k2":"0","U1_k3":"0",
     "U4_k1":"-phi/sqrt(2)","U4_k2":"0","U4_k3":"0",
     "Delta1_k1pp":"1/sqrt(3)","Delta5_k1pp_1":"omega*^2/sqrt(3)","Delta5_k1pp_2":"-omega*/sqrt(3)"},

    {"i":"k3","j":"k3",
     "U1_k1":"phi/sqrt(2)","U1_k2":"0","U1_k3":"0",
     "U4_k1":"-phi/sqrt(2)","U4_k2":"0","U4_k3":"0",
     "Delta1_k1pp":"1/sqrt(3)","Delta5_k1pp_1":"omega*^2/sqrt(3)","Delta5_k1pp_2":"-omega*/sqrt(3)"}
]

json.dump(rows, sys.stdout, ensure_ascii=False, indent=2)
PYEOF
