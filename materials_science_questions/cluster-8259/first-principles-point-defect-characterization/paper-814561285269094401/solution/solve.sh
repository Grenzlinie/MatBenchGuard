#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: perfect_lonsdaleite.json ===
python3 -c "import json; d={'pbe_bg':3.65,'hse06_bg':4.60}; json.dump(d,open('/app/outputs/perfect_lonsdaleite.json','w'))"

# === solve block: fe_doped.json ===
python3 -c "import json; d={'pbe_occ_unocc_gap':2.20,'pbe_occ_above_vbm':0.30,'ggau1_occ_unocc_gap':2.40,'ggau1_occ_above_vbm':0.10}; json.dump(d,open('/app/outputs/fe_doped.json','w'))"

# === solve block: additional_dopants.json ===
python3 -c "
import json
d = {
  'K_lonsdaleite': {'occ_level_above_vbm_pbe':0.50, 'occ_unocc_gap_pbe': None},
  'Ca_lonsdaleite': {'occ_level_above_vbm_pbe':0.00, 'occ_unocc_gap_pbe': None},
  'Zn_lonsdaleite': {'occ_level_above_vbm_pbe':0.10, 'occ_unocc_gap_pbe': None},
  'C_vacancy_lonsdaleite': {'occ_level_above_vbm_pbe':0.30, 'occ_unocc_gap_pbe': None},
  'Cr_lonsdaleite': {'occ_level_above_vbm_pbe':0.10, 'occ_unocc_gap_pbe': None},
  'Mn_lonsdaleite': {'occ_level_above_vbm_pbe':0.10, 'occ_unocc_gap_pbe': None},
  'Fe_cubic_diamond': {'occ_level_above_vbm_pbe':0.65, 'occ_unocc_gap_pbe': None}
}
json.dump(d, open('/app/outputs/additional_dopants.json','w'))
"
