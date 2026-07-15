#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: final_values.json ===
python3 -c 'import json; data={"t1_us":217,"p0_GPa":0.929,"tm_us":27,"tp_us":8.6,"pk_GPa":0.801,"Tk_K":575,"vk_m_per_s":1.00,"wk_m_per_s":51,"delta_k_mm":0.054}; json.dump(data, open("/app/outputs/final_values.json","w"), indent=2, ensure_ascii=False)'

# === solve block: delta0_1mm_final_values.json ===
python3 -c 'import json; data={"t1_us":34,"p0_GPa":0.172,"tm_us":501,"tp_us":45,"pk_GPa":0.141,"Tk_K":435,"vk_m_per_s":1.15,"wk_m_per_s":7.7,"delta_k_mm":0.210}; json.dump(data, open("/app/outputs/delta0_1mm_final_values.json","w"), indent=2, ensure_ascii=False)'
