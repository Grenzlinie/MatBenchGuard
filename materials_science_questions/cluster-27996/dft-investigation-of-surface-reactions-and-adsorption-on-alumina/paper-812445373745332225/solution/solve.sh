#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail

# === solve block: table1_chemisorption_energies.csv ===
python3 << 'PYEOF'
import csv, os
outfile = os.path.join(os.environ.get('OUTDIR', '/app/outputs'), 'table1_chemisorption_energies.csv')
rows = [
    ("H",    "–", 0.0, 52.0, 52.0),
    ("O",    "–", 0.0, 80.0, 80.0),
    ("C",    "–", 0.0, 133.0, 133.0),
    ("Cl",   "–", 0.0, 50.0, 50.0),
    ("Cl",   "–", 0.0, 55.0, 55.0),
    ("Cl",   "–", 0.0, 60.0, 60.0),
    ("OH",   "η¹ (O)", 102.0, 55.0, 157.0),
    ("H2O",  "η¹ (O)", 220.0, 9.0, 229.0),
    ("CH2CH2", "η² (C, C)", 538.0, 9.0, 547.0),
    ("CH2CHCH3", "η² (C=C, H)", 822.0, 10.0, 832.0),
    ("pi-CH2~CH~CH2", "η² (C, C)", 736.0, 25.0, 761.0),
    ("sigma-CH2=CH-CH2", "η¹(C)", 722.0, 31.0, 753.0),
    ("sigma-CH2=CH-CH2", "η² (C=C, C)", 722.0, 33.0, 755.0),
    ("CH2CHCH2Cl", "η² (C=C, Cl)", 803.0, 13.0, 816.0),
    ("CH2CHCH2Cl", "η² (C=C, Cl)", 803.0, 14.0, 817.0),
    ("CH2CHCH2Cl", "η² (C=C, Cl)", 803.0, 15.0, 818.0),
    ("CH2CHCH2OH", "η² (C=C, O)", 918.0, 14.0, 932.0),
    ("CH2CHCH2O", "η² (C=C, O)", 816.0, 59.0, 875.0),
    ("CH2CHCHO", "η² (C=C, O)", 802.0, 14.0, 816.0),
    ("C6H10 (diallyl)", "η² (C=C, C=C)", 1529.0, 19.0, 1548.0),
]
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["species", "coordination_mode", "D_kcal_mol", "Q_kcal_mol", "D_plus_Q_kcal_mol"])
    w.writerows(rows)
PYEOF

# === solve block: tables_3_4_activation_barriers.csv ===
python3 << 'PYEOF'
import csv, os
outfile = os.path.join(os.environ.get('OUTDIR', '/app/outputs'), 'tables_3_4_activation_barriers.csv')
rows = [
    ("Table3", "CH2CHCH3,s <=> CH2CHCH3,g", "", 10.0, 0.0),
    ("Table3", "CH2CHCH3,s <=> pi-CH2CHCH2,s + H_s", "", 18.0, 0.0),
    ("Table3", "CH2CHCH3,s + O_s <=> pi-CH2CHCH2,s + OH_s", "", 2.0, 8.0),
    ("Table3", "CH2CHCH3,s + OH_s <=> pi-CH2CHCH2,s + H2O_s", "", 3.0, 5.0),
    ("Table3", "pi-CH2CHCH2,s + O_s <=> CH2CHCH2O_s", "", 0.0, 34.0),
    ("Table3", "CH2CHCH2O_s <=> CH2CHCHO_s + H_s", "", 9.0, 2.0),
    ("Table3", "CH2CHCH2O_s + O_s <=> CH2CHCHO_s + OH_s", "", 8.0, 26.0),
    ("Table3", "pi-CH2CHCH2,s + O_s <=> CH2CHCHO_s + H_s", "", 0.0, 27.0),
    ("Table4", "CH2CHCH2OH_s <=> CH2CHCH2OH_g", "", 14.0, 0.0),
    ("Table4", "CH2CHCH2OH_s <=> CH2CHCH2O_s + H_s", "", 16.0, 11.0),
    ("Table4", "CH2CHCH2OH_s <=> pi-CH2CHCH2,s + OH_s", "", 16.0, 2.0),
    ("Table4", "CH2CHCH2OH_s + O_s <=> CH2CHCH2O_s + OH_s", "", 4.0, 24.0),
    ("Table4", "CH2CHCH2OH_s + OH_s <=> CH2CHCH2O_s + H2O_s", "", 0.0, 16.0),
    ("Table4", "CH2CHCH2OH_s + pi-CH2CHCH2,s <=> CH2CHCH2O_s + CH2CHCH3,s", "", 0.0, 14.0),
    ("Table4", "CH2CHCH2O_s <=> CH2CHCHO_s + H_s", "", 9.0, 2.0),
    ("Table4", "CH2CHCH2O_s + O_s <=> CH2CHCHO_s + OH_s", "", 8.0, 26.0),
    ("Table4", "CH2CHCH2O_s + OH_s <=> CH2CHCHO_s + H2O_s", "", 7.0, 21.0),
    ("Table4", "CH2CHCH2O_s + pi-CH2CHCH2,s <=> CH2CHCHO_s + CH2CHCH3,s", "", 3.0, 15.0),
    ("Table4", "CH2CHCH2Cl_s <=> CH2CHCH2Cl_g", 50, 13.0, 0.0),
    ("Table4", "CH2CHCH2Cl_s <=> CH2CHCH2Cl_g", 55, 14.0, 0.0),
    ("Table4", "CH2CHCH2Cl_s <=> CH2CHCH2Cl_g", 60, 15.0, 0.0),
    ("Table4", "CH2CHCH2Cl_s <=> pi-CH2CHCH2,s + Cl_s", 50, 11.0, 6.0),
    ("Table4", "CH2CHCH2Cl_s <=> pi-CH2CHCH2,s + Cl_s", 55, 9.0, 8.0),
    ("Table4", "CH2CHCH2Cl_s <=> pi-CH2CHCH2,s + Cl_s", 60, 8.0, 11.0),
    ("Table4", "H2O_s <=> OH_s + H_s", "", 24.0, 3.0),
    ("Table4", "H2O_s + O_s <=> 2 OH_s", "", 12.0, 16.0),
    ("Table4", "OH_s <=> O_s + H_s", "", 28.0, 3.0),
]
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["table_id", "reaction_equation", "Q_Cl_value_if_applicable", "DeltaE_f_kcal_mol", "DeltaE_r_kcal_mol"])
    w.writerows(rows)
PYEOF
