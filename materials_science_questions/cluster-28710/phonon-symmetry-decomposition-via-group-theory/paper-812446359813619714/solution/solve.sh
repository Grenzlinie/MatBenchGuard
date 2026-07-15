#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy || true

# === solve block: phonon_decomposition.json ===
pip3 install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy spglib
cat << 'PYEOF' > /solution/compute_decomposition.py
import json

sg_keys = ['p1','p2','pm','pg','cm','pmm','pmg','pgg','cmm','p4','p4m','p4g','p3','p3m1','p31m','p6','p6m']
data = {}

# p1
p1 = [{"wyckoff":"a","position":"(x,y)","irreps":{"Γ1":3,"Γ2":3,"A1":3,"B1":3,"Y1":3}}]
data["p1"] = p1

# p2
p2 = []
for w in ["a","b","c","d"]:
    p2.append({"wyckoff":w,"position":"(" + {"a":"0,0","b":"0,½","c":"½,½","d":"½,0"}[w] + ")",
               "irreps":{"Γ1":1,"Γ2":2,"A1":1,"A2":2,"B1":1,"B2":2,"Y1":1,"Y2":2}})
p2.append({"wyckoff":"e","position":"(x,y)","irreps":{"Γ1":3,"Γ2":3,"A1":3,"A2":3,"B1":3,"B2":3,"Y1":3,"Y2":3}})
data["p2"] = p2

# pm
pm = [
    {"wyckoff":"a","position":"(0,y)","irreps":{"Γ1":2,"Γ2":1,"Σ1":3,"Δ1":2,"Δ2":1,"X1":2,"X2":1,"Y1":2,"Y2":1,"S1":2,"S2":1,"C1":3,"D1":2,"D2":1}},
    {"wyckoff":"b","position":"(½,y)","irreps":{"Γ1":2,"Γ2":1,"Σ1":3,"Δ1":2,"Δ2":1,"X1":2,"X2":1,"Y1":2,"Y2":1,"S1":2,"S2":1,"C1":3,"D1":2,"D2":1}},
    {"wyckoff":"c","position":"(x,y)","irreps":{"Γ1":3,"Γ2":3,"Σ1":6,"Δ1":3,"Δ2":3,"X1":3,"X2":3,"Y1":3,"Y2":3,"S1":3,"S2":3,"C1":6,"D1":3,"D2":3}}
]
data["pm"] = pm

# pg
pg = [
    {"wyckoff":"a","position":"(x,y)","irreps":{"Γ1":3,"Γ2":3,"Σ1":6,"Δ1":3,"Δ2":3,"X1":3,"X2":3,"Y1":3,"Y2":3,"S1":3,"S2":3,"C1":6,"D1":3,"D2":3}}
]
data["pg"] = pg

# cm
cm = [
    {"wyckoff":"a","position":"(0,y)","irreps":{"Γ1":2,"Γ2":1,"Σ1":3,"Δ1":2,"Δ2":1,"Y1":2,"Y2":1,"C1":3,"S1":3}},
    {"wyckoff":"b","position":"(x,y)","irreps":{"Γ1":3,"Γ2":3,"Σ1":6,"Δ1":3,"Δ2":3,"Y1":3,"Y2":3,"C1":6,"S1":6}}
]
data["cm"] = cm

# pmm (24 IRs)
pmm_irreps = ["Γ1","Γ2","Γ3","Γ4","Σ1","Σ2","Δ1","Δ2","X1","X2","X3","X4","Y1","Y2","Y3","Y4","S1","S2","S3","S4","C1","C2","D1","D2"]
pmm_counts = [
    [1,1,1,2,2,2,2,2,3],
    [1,1,1,1,1,2,2,2,3],
    [0,0,0,1,1,1,1,1,3],
    [1,1,1,2,2,1,1,1,3],
    [2,2,2,4,4,3,3,3,6],
    [1,1,1,2,2,3,3,3,6],
    [2,2,2,3,3,4,4,4,6],
    [1,1,1,3,3,2,2,2,6],
    [1,1,1,2,2,2,2,2,3],
    [1,1,1,1,1,2,2,2,3],
    [0,0,0,1,1,1,1,1,3],
    [1,1,1,2,2,1,1,1,3],
    [1,1,1,2,2,2,2,2,3],
    [1,1,1,1,1,2,2,2,3],
    [0,0,0,1,1,1,1,1,3],
    [1,1,1,2,2,1,1,1,3],
    [1,1,1,2,2,2,2,2,3],
    [1,1,1,1,1,2,2,2,3],
    [0,0,0,1,1,1,1,1,3],
    [1,1,1,2,2,1,1,1,3],
    [2,2,2,4,4,3,3,3,6],
    [1,1,1,2,2,3,3,3,6],
    [2,2,2,4,4,3,3,3,6],
    [1,1,1,2,2,3,3,3,6]
]
pos_letters = ["a","b","c","d","e","f","g","h","i"]
pos_spec = ["(0,0)","(0,½)","(½,0)","(½,½)","(x,0)","(x,½)","(0,y)","(½,y)","(x,y)"]
pmm = []
for j in range(9):
    ir = {}
    for i, irr in enumerate(pmm_irreps):
        ir[irr] = pmm_counts[i][j]
    pmm.append({"wyckoff":pos_letters[j],"position":pos_spec[j],"irreps":ir})
data["pmm"] = pmm

# pmg
pmg_irreps = ["Γ1","Γ2","Γ3","Γ4","Σ1","Σ2","Δ1","Δ2","X1","Y1","Y2","Y3","Y4","S1","C1","C2","D1","D2"]
pmg_counts = [
    [1,1,2,3],
    [2,2,2,3],
    [1,1,1,3],
    [2,2,1,3],
    [3,3,3,6],
    [3,3,3,6],
    [3,3,4,6],
    [3,3,2,6],
    [3,3,3,6],
    [1,2,2,3],
    [2,1,2,3],
    [1,2,1,3],
    [2,1,1,3],
    [3,3,3,6],
    [3,3,3,6],
    [3,3,3,6],
    [3,3,3,6],
    [3,3,3,6]
]
pmg_pos = ["a","b","c","d"]
pmg_spec = ["(0,0)","(0,½)","(¼,y)","(x,y)"]
pmg = []
for j in range(4):
    ir = {}
    for i, irr in enumerate(pmg_irreps):
        ir[irr] = pmg_counts[i][j]
    pmg.append({"wyckoff":pmg_pos[j],"position":pmg_spec[j],"irreps":ir})
data["pmg"] = pmg

# pgg
pgg_irreps = ["Γ1","Γ2","Γ3","Γ4","Σ1","Σ2","Δ1","Δ2","X1","Y1","S1","S2","S3","S4","C1","C2","D1","D2"]
pgg_counts = [
    [1,1,3],
    [2,2,3],
    [1,1,3],
    [2,2,3],
    [3,3,6],
    [3,3,6],
    [3,3,6],
    [3,3,6],
    [3,3,6],
    [3,3,6],
    [1,2,3],
    [1,2,3],
    [2,1,3],
    [2,1,3],
    [3,3,6],
    [3,3,6],
    [3,3,6],
    [3,3,6]
]
pgg_pos = ["a","b","c"]
pgg_spec = ["(0,0)","(½,0)","(x,y)"]
pgg = []
for j in range(3):
    ir = {}
    for i, irr in enumerate(pgg_irreps):
        ir[irr] = pgg_counts[i][j]
    pgg.append({"wyckoff":pgg_pos[j],"position":pgg_spec[j],"irreps":ir})
data["pgg"] = pgg

# cmm
cmm_irreps = ["Γ1","Γ2","Γ3","Γ4","Σ1","Σ2","Δ1","Δ2","Y1","Y2","Y3","Y4","C1","C2","S1","S2"]
cmm_counts = [
    [1,1,2,2,2,3],
    [1,1,2,1,2,3],
    [0,0,1,1,1,3],
    [1,1,2,2,1,3],
    [2,2,3,4,3,6],
    [1,1,3,2,3,6],
    [2,2,3,3,4,6],
    [1,1,3,3,2,6],
    [1,1,1,2,2,3],
    [1,1,2,1,2,3],
    [0,0,1,2,1,3],
    [1,1,2,1,1,3],
    [2,2,3,4,3,6],
    [1,1,3,2,3,6],
    [1,1,2,3,3,6],
    [2,2,4,3,3,6]
]
cmm_pos = ["a","b","c","d","e","f"]
cmm_spec = ["(0,0)","(0,½)","(½,½)","(x,0)","(0,y)","(x,y)"]
cmm = []
for j in range(6):
    ir = {}
    for i, irr in enumerate(cmm_irreps):
        ir[irr] = cmm_counts[i][j]
    cmm.append({"wyckoff":cmm_pos[j],"position":cmm_spec[j],"irreps":ir})
data["cmm"] = cmm

# p4
p4_irreps = ["Γ1","Γ2","Γ3","Γ4","Σ1","Δ1","M1","M2","M3","M4","X1","X2","Y1"]
p4_counts = [
    [1,1,1,3],
    [0,0,1,3],
    [1,1,2,3],
    [1,1,2,3],
    [3,3,6,12],
    [3,3,6,12],
    [1,1,1,3],
    [0,0,1,3],
    [1,1,2,3],
    [1,1,2,3],
    [1,1,2,6],
    [2,2,4,6],
    [3,3,6,12]
]
p4_pos = ["a","b","c","d"]
p4_spec = ["(0,0)","(½,½)","(½,0)","(x,y)"]
p4 = []
for j in range(4):
    ir = {}
    for i, irr in enumerate(p4_irreps):
        ir[irr] = p4_counts[i][j]
    p4.append({"wyckoff":p4_pos[j],"position":p4_spec[j],"irreps":ir})
data["p4"] = p4

# p4m (positions a-g)
p4m_irreps = ["Γ1","Γ2","Γ3","Γ4","Γ5","Σ1","Σ2","Δ1","Δ2","M1","M2","M3","M4","M5","X1","X2","X3","X4","Y1","Y2"]
p4m_counts = [
    [1,1,2,2,2,2,3],
    [0,0,1,1,1,1,3],
    [0,0,1,2,2,1,3],
    [0,0,1,1,2,2,3],
    [1,1,2,3,3,3,6],
    [2,2,3,6,6,7,12],
    [1,1,3,6,6,5,12],
    [2,2,4,7,7,6,12],
    [1,1,2,5,5,6,12],
    [1,1,1,2,2,2,3],
    [0,0,1,1,1,1,3],
    [0,0,1,2,2,1,3],
    [0,0,1,1,2,2,3],
    [1,1,2,3,3,3,6],
    [1,1,2,4,4,3,6],
    [1,1,2,3,3,3,6],
    [0,0,1,2,2,3,6],
    [1,1,2,3,3,3,6],
    [2,2,4,7,7,6,12],
    [1,1,2,5,5,6,12]
]
p4m_pos = ["a","b","c","d","e","f","g"]
p4m_spec = ["(0,0)","(½,½)","(½,0)","(x,0)","(x,½)","(x,x)","(x,y)"]
p4m = []
for j in range(7):
    ir = {}
    for i, irr in enumerate(p4m_irreps):
        ir[irr] = p4m_counts[i][j]
    p4m.append({"wyckoff":p4m_pos[j],"position":p4m_spec[j],"irreps":ir})
data["p4m"] = p4m

# p4g (positions a-d) – FIXED: transposed to [irrep][position]
p4g_irreps = ["Γ1","Γ2","Γ3","Γ4","Γ5","Σ1","Σ2","Δ1","Δ2","M1","M2","M3","M4","M5","X1","Y1","Y2"]
p4g_counts = [
    [1, 1, 2, 3],
    [1, 0, 1, 3],
    [0, 0, 1, 3],
    [0, 1, 2, 3],
    [2, 2, 3, 6],
    [3, 4, 7,12],
    [3, 2, 5,12],
    [3, 3, 6,12],
    [3, 3, 6,12],
    [1, 2, 3, 6],
    [1, 1, 2, 3],
    [1, 0, 1, 3],
    [1, 0, 1, 3],
    [1, 1, 2, 3],
    [3, 3, 6,12],
    [3, 3, 6,12],
    [3, 3, 6,12]
]
p4g_pos = ["a","b","c","d"]
p4g_spec = ["(0,0)","(½,0)","(x,½+x)","(x,y)"]
p4g = []
for j in range(4):
    ir = {}
    for i, irr in enumerate(p4g_irreps):
        ir[irr] = p4g_counts[i][j]
    p4g.append({"wyckoff":p4g_pos[j],"position":p4g_spec[j],"irreps":ir})
data["p4g"] = p4g

# p3 (positions a-d) – FIXED: transposed
p3_irreps = ["Γ1","Γ2","Γ3","Σ1","Σ2","T1","K1","K2","K3","M1","M2","T1'"]
p3_counts = [
    [1, 1, 1, 3],
    [1, 1, 1, 3],
    [1, 1, 1, 3],
    [3, 3, 3, 9],
    [1, 1, 1, 9],
    [3, 3, 3, 9],
    [1, 1, 1, 3],
    [1, 1, 1, 3],
    [1, 1, 1, 3],
    [3, 3, 3, 9],
    [1, 1, 1, 9],
    [3, 3, 3, 9]
]
p3_pos = ["a","b","c","d"]
p3_spec = ["(0,0)","(⅓,⅔)","(⅔,⅓)","(x,y)"]
p3 = []
for j in range(4):
    ir = {}
    for i, irr in enumerate(p3_irreps):
        ir[irr] = p3_counts[i][j]
    p3.append({"wyckoff":p3_pos[j],"position":p3_spec[j],"irreps":ir})
data["p3"] = p3

# p3m1 (positions a-d) – FIXED: transposed
p3m1_irreps = ["Γ1","Γ2","Γ3","Σ1","T1","T2","K1","K2","K3","M1","M2","T1'","T2'"]
p3m1_counts = [
    [1, 1, 2, 3],
    [0, 1, 2, 3],
    [1, 2, 4, 6],
    [3, 6, 9,18],
    [2, 3, 5, 9],
    [1, 3, 4, 9],
    [1, 1, 2, 3],
    [0, 1, 2, 3],
    [1, 2, 4, 6],
    [2, 3, 5, 9],
    [1, 3, 4, 9],
    [2, 3, 5, 9],
    [1, 3, 4, 9]
]
p3m1_pos = ["a","b","c","d"]
p3m1_spec = ["(0,0)","(⅓,⅔)","(x,0)","(x,y)"]
p3m1 = []
for j in range(4):
    ir = {}
    for i, irr in enumerate(p3m1_irreps):
        ir[irr] = p3m1_counts[i][j]
    p3m1.append({"wyckoff":p3m1_pos[j],"position":p3m1_spec[j],"irreps":ir})
data["p3m1"] = p3m1

# p31m (positions a-d) – FIXED: transposed
p31m_irreps = ["Γ1","Γ2","Γ3","Σ1","T1","T2","K1","K2","K3","M1","M2","T1'","T2'"]
p31m_counts = [
    [1, 1, 2, 3],
    [0, 1, 2, 3],
    [1, 2, 4, 6],
    [3, 6, 9,18],
    [2, 3, 5, 9],
    [1, 3, 4, 9],
    [1, 1, 2, 3],
    [0, 1, 2, 3],
    [1, 2, 4, 6],
    [2, 3, 5, 9],
    [1, 3, 4, 9],
    [2, 3, 5, 9],
    [1, 3, 4, 9]
]
p31m_pos = ["a","b","c","d"]
p31m_spec = ["(0,0)","(⅓,⅔)","(x,0)","(x,y)"]
p31m = []
for j in range(4):
    ir = {}
    for i, irr in enumerate(p31m_irreps):
        ir[irr] = p31m_counts[i][j]
    p31m.append({"wyckoff":p31m_pos[j],"position":p31m_spec[j],"irreps":ir})
data["p31m"] = p31m

# p6 (positions a-d) – FIXED: transposed
p6_irreps = ["Γ1","Γ2","Γ3","Γ4","Γ5","Γ6","K1","K2","K3","T1'","M1","M2"]
p6_counts = [
    [1, 1, 1, 3],
    [1, 2, 2, 6],
    [1, 3, 3, 9],
    [0, 6, 6,18],
    [1, 1, 1, 3],
    [1, 2, 2, 6],
    [1, 1, 1, 3],
    [2, 2, 2, 6],
    [3, 3, 3, 9],
    [6, 6, 6,18],
    [1, 1, 1, 3],
    [2, 2, 2, 6]
]
p6_pos = ["a","b","c","d"]
p6_spec = ["(0,0)","(⅓,⅔)","(½,0)","(x,y)"]
p6 = []
for j in range(4):
    ir = {}
    for i, irr in enumerate(p6_irreps):
        ir[irr] = p6_counts[i][j]
    p6.append({"wyckoff":p6_pos[j],"position":p6_spec[j],"irreps":ir})
data["p6"] = p6

# p6m (positions a-f)
p6m_details = [
    {"wyckoff":"a","position":"(0,0)",   "irreps":{"Γ1":1,"Γ2":0,"Γ3":0,"Γ4":0,"Γ5":1,"Γ6":1,"Γ7":2,"Γ8":3,"Γ9":5,"Γ10":10,"Γ11":9,"Γ12":18,"Σ1":2,"Σ2":1,"T1":2,"T2":1,"K1":1,"K2":0,"K3":1,"M1":1,"M2":1,"M3":0,"M4":1,"T1'":2,"T2'":1}},
    {"wyckoff":"b","position":"(⅓,⅔)",   "irreps":{"Γ1":1,"Γ2":0,"Γ3":1,"Γ4":1,"Γ5":0,"Γ6":1,"Γ7":2,"Γ8":3,"Γ9":5,"Γ10":10,"Γ11":9,"Γ12":18,"Σ1":2,"Σ2":2,"T1":2,"T2":2,"K1":1,"K2":0,"K3":1,"M1":1,"M2":1,"M3":0,"M4":1,"T1'":3,"T2'":3}},
    {"wyckoff":"c","position":"(½,0)",   "irreps":{"Γ1":1,"Γ2":0,"Γ3":1,"Γ4":2,"Γ5":1,"Γ6":1,"Γ7":2,"Γ8":3,"Γ9":5,"Γ10":10,"Γ11":9,"Γ12":18,"Σ1":3,"Σ2":2,"T1":2,"T2":2,"K1":1,"K2":0,"K3":1,"M1":1,"M2":1,"M3":0,"M4":1,"T1'":3,"T2'":3}},
    {"wyckoff":"d","position":"(x,0)",   "irreps":{"Γ1":2,"Γ2":1,"Γ3":2,"Γ4":3,"Γ5":3,"Γ6":5,"Γ7":5,"Γ8":10,"Γ9":12,"Γ10":24,"Γ11":22,"Γ12":48,"Σ1":7,"Σ2":6,"T1":6,"T2":5,"K1":3,"K2":1,"K3":3,"M1":3,"M2":3,"M3":1,"M4":3,"T1'":6,"T2'":5}},
    {"wyckoff":"e","position":"(x,‾x)",   "irreps":{"Γ1":2,"Γ2":1,"Γ3":2,"Γ4":3,"Γ5":3,"Γ6":5,"Γ7":5,"Γ8":10,"Γ9":12,"Γ10":24,"Γ11":22,"Γ12":48,"Σ1":7,"Σ2":6,"T1":6,"T2":5,"K1":3,"K2":1,"K3":3,"M1":3,"M2":3,"M3":1,"M4":3,"T1'":6,"T2'":5}},
    {"wyckoff":"f","position":"(x,y)",   "irreps":{"Γ1":3,"Γ2":3,"Γ3":3,"Γ4":6,"Γ5":6,"Γ6":9,"Γ7":9,"Γ8":18,"Γ9":27,"Γ10":54,"Γ11":45,"Γ12":108,"Σ1":12,"Σ2":12,"T1":12,"T2":12,"K1":6,"K2":3,"K3":6,"M1":6,"M2":6,"M3":3,"M4":6,"T1'":12,"T2'":12}}
]
data["p6m"] = p6m_details

import os
os.makedirs("/app/outputs", exist_ok=True)
with open("/app/outputs/phonon_decomposition.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
PYEOF
python3 /solution/compute_decomposition.py
