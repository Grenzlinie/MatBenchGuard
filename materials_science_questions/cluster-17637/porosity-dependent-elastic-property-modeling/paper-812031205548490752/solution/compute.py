import csv
import math
import os

kL = 2.4
kT = 3.8
B0 = 36.9
G0 = 31.0

samples = [
    {"sample": "1A", "D_nm": 1050, "porosity_pct": 57, "rho_gcm3": 1.05, "f0_GHz": 3.53, "kind": "filled"},
    {"sample": "1B", "D_nm": 1050, "porosity_pct": 57, "rho_gcm3": 1.25, "f0_GHz": 3.35, "kind": "filled"},
    {"sample": "1C", "D_nm": 1050, "porosity_pct": 57, "rho_gcm3": 2.15, "f0_GHz": 3.28, "kind": "filled"},
    {"sample": "Bare 1050 nm", "D_nm": 1050, "porosity_pct": 57, "rho_gcm3": 0.90, "f0_GHz": 3.68, "kind": "bare"},
    {"sample": "2A", "D_nm": 620, "porosity_pct": 54, "rho_gcm3": 1.10, "f0_GHz": 6.24, "kind": "filled"},
    {"sample": "2B", "D_nm": 620, "porosity_pct": 54, "rho_gcm3": 1.41, "f0_GHz": 6.01, "kind": "filled"},
    {"sample": "Bare 620 nm", "D_nm": 620, "porosity_pct": 54, "rho_gcm3": 0.95, "f0_GHz": 6.35, "kind": "bare"},
]

rows = []
for s in samples:
    if s["kind"] == "filled":
        sL = (math.pi * s["f0_GHz"] * s["D_nm"]) / (kL * 1000)
        sT = (math.pi * s["f0_GHz"] * s["D_nm"]) / (kT * 1000)
        G = s["rho_gcm3"] * sT ** 2
        B = s["rho_gcm3"] * sL ** 2 - (4 / 3) * G
        rows.append({
            "sample": s["sample"],
            "D_nm": s["D_nm"],
            "rho_gcm3": s["rho_gcm3"],
            "f0_GHz": s["f0_GHz"],
            "sL_kms": round(sL, 2),
            "sT_kms": round(sT, 2),
            "B_GPa": round(B, 1),
            "G_GPa": round(G, 2),
            "theoretical_Bp_GPa": ""
        })
    else:
        p_frac = s["porosity_pct"] / 100.0
        Bp = (1 - p_frac) * B0 / (1 + p_frac * (3 * B0 / (4 * G0)))
        rows.append({
            "sample": s["sample"],
            "D_nm": s["D_nm"],
            "rho_gcm3": s["rho_gcm3"],
            "f0_GHz": s["f0_GHz"],
            "sL_kms": "",
            "sT_kms": "",
            "B_GPa": "",
            "G_GPa": "",
            "theoretical_Bp_GPa": round(Bp, 1)
        })

outdir = "/app/outputs"
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "elastic_moduli.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["sample", "D_nm", "rho_gcm3", "f0_GHz", "sL_kms", "sT_kms", "B_GPa", "G_GPa", "theoretical_Bp_GPa"])
    writer.writeheader()
    writer.writerows(rows)
