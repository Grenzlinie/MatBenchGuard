#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: deflection_results.json ===
python3 -c '
import json, math

h = 0.335e-9
b = 1e-9
l = 10e-9
E = 1e12
G = 4.6e9
P = 1e-9

lam2 = math.sqrt(8*G/(E*h*h))
e2l = math.exp(2*lam2*l)
w_bl = (9*P*(1-e2l))/(16*lam2*(1+e2l)*G*b*h) + (9*P*l)/(16*G*b*h) + (P*l**3)/(2*E*b*h**3)
stiff_bl = P*l/(w_bl*b*h) * 1e-9
w_bl_nm = w_bl * 1e9

lam3 = math.sqrt(9*G/(E*h*h))
e2l3 = math.exp(2*lam3*l)
w_tl = (32*P*(1-e2l3))/(81*lam3*(1+e2l3)*G*b*h) + (4*P*l**3)/(27*E*b*h**3) + (32*P*l)/(81*G*b*h)
stiff_tl = P*l/(w_tl*b*h) * 1e-9
w_tl_nm = w_tl * 1e9

res = {
    "bilayer": {
        "w_l": round(w_bl_nm, 10),
        "Pl_over_wl_bh": round(stiff_bl, 10),
        "parameters": {"E": 1.0, "G": 4.6, "h": 0.335, "b": 1.0, "l": 10.0, "P": 1.0}
    },
    "trilayer": {
        "w_l": round(w_tl_nm, 10),
        "Pl_over_wl_bh": round(stiff_tl, 10),
        "parameters": {"E": 1.0, "G": 4.6, "h": 0.335, "b": 1.0, "l": 10.0, "P": 1.0}
    }
}
with open("/app/outputs/deflection_results.json", "w") as f:
    json.dump(res, f, indent=2)
'
