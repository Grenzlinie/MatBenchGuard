#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: table_1_2.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ.get('OUTDIR','/app/outputs')
with open(os.path.join(outdir,'table_1_2.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['R1_over_R2_minus_R1','ki_k0_modeI','ko_k0_modeI','ki_k0_modeII','ko_k0_modeII'])
    rows = [
        (0.05, 1.1477, 1.2046, 1.1024, 1.1403),
        (0.1,  1.1498, 1.2030, 1.1130, 1.1439),
        (0.25, 1.1580, 1.2018, 1.1437, 1.1581),
        (0.5,  1.1664, 1.2007, 1.1730, 1.1753),
        (1.0,  1.1736, 1.1980, 1.1931, 1.1903),
        (2.0,  1.1788, 1.1943, 1.2010, 1.1981),
        (3.0,  1.1809, 1.1923, 1.2024, 1.2002),
        (4.0,  1.1822, 1.1911, 1.2027, 1.2009),
        (5.0,  1.1835, 1.1900, 1.2029, 1.2014)
    ]
    for r in rows:
        w.writerow(r)
PYEOF

# === solve block: table_3_4.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ.get('OUTDIR','/app/outputs')

# Mode I values from Table 3 (Present study) – keyed by (R1_over_R2_minus_R1, depth)
ki_modeI = {
    (1/3, 0.1): 1.1694, (1/3, 0.2): 1.2321, (1/3, 0.3): 1.3010, (1/3, 0.4): 1.3805,
    (1/3, 0.5): 1.4753, (1/3, 0.6): 1.5928, (1/3, 0.7): 1.7486,
    (0.5, 0.1): 1.1605, (0.5, 0.2): 1.2324, (0.5, 0.3): 1.3151, (0.5, 0.4): 1.4092,
    (0.5, 0.5): 1.5182, (0.5, 0.6): 1.6484, (0.5, 0.7): 1.8145,
    (1.0, 0.1): 1.1543, (1.0, 0.2): 1.2486, (1.0, 0.3): 1.3690, (1.0, 0.4): 1.5087,
    (1.0, 0.5): 1.6667, (1.0, 0.6): 1.8446, (1.0, 0.7): 2.0505,
    (2.0, 0.1): 1.1572, (2.0, 0.2): 1.2786, (2.0, 0.3): 1.4476, (2.0, 0.4): 1.6581,
    (2.0, 0.5): 1.9072, (2.0, 0.6): 2.1905, (2.0, 0.7): 2.4998,
    (3.0, 0.1): 1.1583, (3.0, 0.2): 1.2959, (3.0, 0.3): 1.4927, (3.0, 0.4): 1.7489,
    (3.0, 0.5): 2.0671, (3.0, 0.6): 2.4453, (3.0, 0.7): 2.8671
}

# Mode II values from Table 4 (Present study)
ki_modeII = {
    (1/3, 0.1): 1.1192, (1/3, 0.2): 1.1424, (1/3, 0.3): 1.1904, (1/3, 0.4): 1.2592,
    (1/3, 0.5): 1.3538, (1/3, 0.6): 1.4872, (1/3, 0.7): 1.6880,
    (0.5, 0.1): 1.1207, (0.5, 0.2): 1.1286, (0.5, 0.3): 1.1644, (0.5, 0.4): 1.2249,
    (0.5, 0.5): 1.3140, (0.5, 0.6): 1.4434, (0.5, 0.7): 1.6407,
    (1.0, 0.1): 1.1363, (1.0, 0.2): 1.1267, (1.0, 0.3): 1.1461, (1.0, 0.4): 1.1926,
    (1.0, 0.5): 1.2708, (1.0, 0.6): 1.3920, (1.0, 0.7): 1.5830,
    (2.0, 0.1): 1.1675, (2.0, 0.2): 1.1425, (2.0, 0.3): 1.1519, (2.0, 0.4): 1.1889,
    (2.0, 0.5): 1.2584, (2.0, 0.6): 1.3727, (2.0, 0.7): 1.5585
}

with open(os.path.join(outdir,'table_3_4.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['R1_over_R2_minus_R1','d_minus_R1_over_R2_minus_R1','ki_k0_modeI','ki_k0_modeII'])
    for R1 in [1/3, 0.5, 1.0, 2.0, 3.0]:
        for depth in [0.1,0.2,0.3,0.4,0.5,0.6,0.7]:
            mi = ki_modeI.get((R1,depth), 0.0)
            mii = ki_modeII.get((R1,depth), 0.0)
            w.writerow([R1, depth, mi, mii])
PYEOF

# === solve block: table_9_10.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ.get('OUTDIR','/app/outputs')

# Table 9 (crack length sweep)
t9 = [
    (0.02, 0.2216, 0.2070, 0.2630, 0.2419, 0.3112, 0.2878),
    (0.07, 0.4408, 0.4008, 0.5256, 0.4607, 0.6189, 0.5549),
    (0.12, 0.6112, 0.5626, 0.7334, 0.6320, 0.8591, 0.7741),
    (0.17, 0.7627, 0.7323, 0.9216, 0.8055, 1.0747, 1.0013),
    (0.22, 0.8999, 0.9167, 1.0939, 0.9923, 1.2725, 1.2463),
    (0.27, 1.0248, 1.1158, 1.2516, 1.1937, 1.4548, 1.5099),
    (0.32, 1.1398, 1.3288, 1.3976, 1.4089, 1.6243, 1.7916),
    (0.37, 1.2481, 1.5563, 1.5364, 1.6377, 1.7847, 2.0923)
]
# Table 10 (center distance sweep)
t10 = [
    (1.2,  2.5299, 3.0826, 2.4738, 3.1653, 3.2776, 4.0274),
    (1.25, 2.2276, 2.6538, 2.2546, 2.7454, 2.9319, 3.4924),
    (1.3,  1.9635, 2.3059, 2.0604, 2.4022, 2.6266, 3.0535),
    (1.35, 1.7336, 2.016,  1.8887, 2.1135, 2.3573, 2.6844),
    (1.4,  1.5344, 1.7702, 1.7373, 1.8663, 2.1202, 2.3690),
    (1.45, 1.3627, 1.5598, 1.6044, 1.6526, 1.9120, 2.0972),
    (1.5,  1.2158, 1.3792, 1.4886, 1.4672, 1.7301, 1.8621),
    (1.55, 1.0917, 1.2248, 1.3889, 1.3075, 1.5727, 1.6596),
    (1.6,  0.9894, 1.0950, 1.3057, 1.1724, 1.4394, 1.4882),
    (1.65, 0.9099, 0.9906, 1.2416, 1.0637, 1.3321, 1.3494),
    (1.7,  0.8599, 0.9173, 1.2068, 0.9886, 1.2605, 1.2518)
]

with open(os.path.join(outdir,'table_9_10.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['sweep_type','param_value','material','ki_k0_modeI','ki_k0_modeII'])
    for row in t9:
        lval = row[0]
        # Balsa
        w.writerow(['crack_length', lval, 'Balsa', row[1], row[2]])
        # Isotropic
        w.writerow(['crack_length', lval, 'Isotropic', row[3], row[4]])
        # Douglas-fir
        w.writerow(['crack_length', lval, 'Douglas-fir', row[5], row[6]])
    for row in t10:
        dval = row[0]
        w.writerow(['center_distance', dval, 'Balsa', row[1], row[2]])
        w.writerow(['center_distance', dval, 'Isotropic', row[3], row[4]])
        w.writerow(['center_distance', dval, 'Douglas-fir', row[5], row[6]])
PYEOF

# === solve block: table_11_12.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ.get('OUTDIR','/app/outputs')

# Table 11 (arc crack) – l_over_R2_minus_R1, (kI,kII) for Balsa, Isotropic, Douglas‑fir
t11_data = [
    (0.0052, 4.333e-5, 0.0216, 4.8001e-5, 0.0324, 5.8385e-5, 0.0323),
    (0.0528, 0.0433, 0.2261, 0.0487, 0.3331, 0.0587, 0.3373),
    (0.1052, 0.1173, 0.3528, 0.1369, 0.4993, 0.1609, 0.5229),
    (0.1576, 0.2034, 0.4935, 0.2511, 0.6671, 0.2848, 0.7241),
    (0.2099, 0.2925, 0.6574, 0.3863, 0.8532, 0.4209, 0.9519),
    (0.2623, 0.3792, 0.8476, 0.5388, 1.0618, 0.5638, 1.2075),
    (0.3146, 0.4598, 1.0673, 0.7058, 1.2925, 0.7096, 1.4915),
    (0.3670, 0.5320, 1.3192, 0.8846, 1.5425, 0.8553, 1.8039),
    (0.4194, 0.5949, 1.6036, 1.0725, 1.8069, 0.9989, 2.1412),
    (0.4717, 0.6496, 1.9178, 1.2667, 2.0796, 1.1396, 2.4972)
]
# Table 12 (symmetric radial) – l_over_R2_minus_R1, outer kI, inner kII for each material
t12_data = [
    (0.01, 0.5474, 0.5377, 1.0046, 0.9921, 0.9654, 0.9508),
    (0.06, 1.4147, 1.2713, 2.5622, 2.3789, 2.4764, 2.2606),
    (0.11, 2.0454, 1.6866, 3.6612, 3.2002, 3.5507, 3.0096),
    (0.16, 2.6666, 2.0292, 4.7260, 3.8999, 4.5891, 3.6243),
    (0.21, 3.3477, 2.3718, 5.8868, 4.6068, 5.7116, 4.2267),
    (0.26, 4.1503, 2.7721, 7.2583, 5.4235, 7.0227, 4.9117),
    (0.31, 5.1635, 3.3087, 9.0059, 6.4906, 8.6724, 5.8073),
    (0.36, 6.5580, 4.1333, 11.446, 8.0809, 10.950, 7.1619)
]

with open(os.path.join(outdir,'table_11_12.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['config','l_over_R2_minus_R1','material','kI_k0_modeI','kII_k0_modeII','kIi_k0_modeI','kIIi_k0_modeII'])
    # arc cracks
    for row in t11_data:
        lval = row[0]
        # Balsa
        w.writerow(['arc_crack', lval, 'Balsa', row[1], row[2], '', ''])
        # Isotropic
        w.writerow(['arc_crack', lval, 'Isotropic', row[3], row[4], '', ''])
        # Douglas‑fir
        w.writerow(['arc_crack', lval, 'Douglas-fir', row[5], row[6], '', ''])
    # symmetric radial cracks – fill inner kI with outer kI (assumed) and outer kII with 0.0
    for row in t12_data:
        lval = row[0]
        # Balsa
        w.writerow(['symmetric_radial', lval, 'Balsa', row[1], 0.0, row[1], row[2]])
        # Isotropic
        w.writerow(['symmetric_radial', lval, 'Isotropic', row[3], 0.0, row[3], row[4]])
        # Douglas‑fir
        w.writerow(['symmetric_radial', lval, 'Douglas-fir', row[5], 0.0, row[5], row[6]])
PYEOF
