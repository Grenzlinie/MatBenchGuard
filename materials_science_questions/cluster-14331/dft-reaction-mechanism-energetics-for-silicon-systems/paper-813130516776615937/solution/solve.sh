#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_frequencies.csv ===
python3 <<'PYEOF'
import csv

rows = [
    # Si(mu-H)3CeH (H isotopologue)
    ['Si(mu-H)3CeH', 'H', 'Si-H stretch', 1815.4, 97.0],
    ['Si(mu-H)3CeH', 'H', 'SiH2 symmetric stretch', 1735.9, 94.0],
    ['Si(mu-H)3CeH', 'H', 'SiH2 antisymmetric stretch', 1721.3, 115.0],
    ['Si(mu-H)3CeH', 'H', 'Ce-H stretch', 1282.3, 925.0],
    ['Si(mu-H)3CeH', 'H', 'SiH2-Ce symmetric stretch', 1053.7, 444.0],
    ['Si(mu-H)3CeH', 'H', 'Si-H-Ce wag', 1043.9, 19.0],
    ['Si(mu-H)3CeH', 'H', 'Si-H-Ce stretch', 1026.7, 254.0],

    # Si(mu-D)3CeD (D isotopologue)
    ['Si(mu-D)3CeD', 'D', 'Si-D stretch', 1301.4, 55.0],
    ['Si(mu-D)3CeD', 'D', 'SiD2 symmetric stretch', 1245.9, 50.0],
    ['Si(mu-D)3CeD', 'D', 'SiD2 antisymmetric stretch', 1235.1, 57.0],
    ['Si(mu-D)3CeD', 'D', 'Ce-D stretch', 910.7, 467.0],
    ['Si(mu-D)3CeD', 'D', 'SiD2-Ce symmetric stretch', 755.1, 306.0],
    ['Si(mu-D)3CeD', 'D', 'Si-D-Ce wag', 743.2, 8.0],
    ['Si(mu-D)3CeD', 'D', 'Si-D-Ce stretch', 736.7, 43.0],

    # H3SiCeH (H isotopologue)
    ['H3SiCeH', 'H', 'Si-H stretch', 2144.8, 141.0],
    ['H3SiCeH', 'H', 'SiH2 antisymmetric stretch', 2116.9, 115.0],
    ['H3SiCeH', 'H', 'SiH2 symmetric stretch', 2115.3, 145.0],
    ['H3SiCeH', 'H', 'Ce-H stretch', 1263.1, 873.0],
    ['H3SiCeH', 'H', 'Si-H wag', 944.6, 27.0],
    ['H3SiCeH', 'H', 'SiH2 scissoring', 943.5, 32.0],
    ['H3SiCeH', 'H', 'SiH3 deformation', 845.5, 447.0],

    # D3SiCeD (D isotopologue)
    ['D3SiCeD', 'D', 'Si-D stretch', 1545.3, 69.0],
    ['D3SiCeD', 'D', 'SiD2 antisymmetric stretch', 1527.3, 59.0],
    ['D3SiCeD', 'D', 'SiD2 symmetric stretch', 1510.1, 82.0],
    ['D3SiCeD', 'D', 'Ce-D stretch', 897.8, 437.0],
    ['D3SiCeD', 'D', 'Si-D wag', 676.2, 13.0],
    ['D3SiCeD', 'D', 'SiD2 scissoring', 675.0, 15.0],
    ['D3SiCeD', 'D', 'SiD3 deformation', 625.8, 209.0],

    # HSi(mu-H)2CeH (H isotopologue)
    ['HSi(mu-H)2CeH', 'H', 'Si-H stretch I', 2164.4, 193.0],
    ['HSi(mu-H)2CeH', 'H', 'Si-H stretch II', 1918.0, 111.0],
    ['HSi(mu-H)2CeH', 'H', 'Si-H stretch III', 1746.7, 106.0],
    ['HSi(mu-H)2CeH', 'H', 'Ce-H stretch', 1303.8, 680.0],
    ['HSi(mu-H)2CeH', 'H', 'Si-H-Ce stretch', 1026.5, 253.0],
    ['HSi(mu-H)2CeH', 'H', 'SiH2 scissoring (asym)', 926.7, 99.0],
    ['HSi(mu-H)2CeH', 'H', 'SiH2 scissoring (sym)', 869.9, 81.0],

    # DSi(mu-D)2CeD (D isotopologue)
    ['DSi(mu-D)2CeD', 'D', 'Si-D stretch I', 1558.6, 102.0],
    ['DSi(mu-D)2CeD', 'D', 'Si-D stretch II', 1377.1, 57.0],
    ['DSi(mu-D)2CeD', 'D', 'Si-D stretch III', 1254.5, 52.0],
    ['DSi(mu-D)2CeD', 'D', 'Ce-D stretch', 925.3, 347.0],
    ['DSi(mu-D)2CeD', 'D', 'Si-D-Ce stretch', 733.5, 130.0],
    ['DSi(mu-D)2CeD', 'D', 'SiD2 scissoring (asym)', 662.9, 42.0],
    ['DSi(mu-D)2CeD', 'D', 'SiD2 scissoring (sym)', 630.9, 32.0],

    # H2Si(mu-H)CeH (H isotopologue)
    ['H2Si(mu-H)CeH', 'H', 'Si-H stretch I', 2158.2, 153.0],
    ['H2Si(mu-H)CeH', 'H', 'Si-H stretch II', 2117.0, 154.0],
    ['H2Si(mu-H)CeH', 'H', 'Si-H stretch III', 1733.2, 350.0],
    ['H2Si(mu-H)CeH', 'H', 'Ce-H stretch', 1300.0, 601.0],
    ['H2Si(mu-H)CeH', 'H', 'Si-H-Ce stretch', 969.9, 107.0],
    ['H2Si(mu-H)CeH', 'H', 'SiH2 scissoring (asym)', 923.3, 282.0],
    ['H2Si(mu-H)CeH', 'H', 'SiH2 scissoring (sym)', 890.7, 49.0],

    # D2Si(mu-D)CeD (D isotopologue)
    ['D2Si(mu-D)CeD', 'D', 'Si-D stretch I', 1554.7, 74.0],
    ['D2Si(mu-D)CeD', 'D', 'Si-D stretch II', 1519.5, 91.0],
    ['D2Si(mu-D)CeD', 'D', 'Si-D stretch III', 1245.1, 73.0],
    ['D2Si(mu-D)CeD', 'D', 'Ce-D stretch', 922.6, 305.0],
    ['D2Si(mu-D)CeD', 'D', 'Si-D-Ce stretch', 694.5, 89.0],
    ['D2Si(mu-D)CeD', 'D', 'SiD2 scissoring (asym)', 669.1, 102.0],
    ['D2Si(mu-D)CeD', 'D', 'SiD2 scissoring (sym)', 637.3, 19.0],

    # H3CCeH (H isotopologue)
    ['H3CCeH', 'H', 'C-H stretch', 2890.8, 12.0],
    ['H3CCeH', 'H', 'CH2 antisymmetric stretch', 2859.6, 13.0],
    ['H3CCeH', 'H', 'CH3 symmetric stretch', 2842.4, 8.0],
    ['H3CCeH', 'H', 'C-H wag', 1356.6, 7.0],
    ['H3CCeH', 'H', 'CH2 scissoring', 1391.7, 2.0],
    ['H3CCeH', 'H', 'Ce-H stretch', 1227.4, 638.0],
    ['H3CCeH', 'H', 'CH3 deformation', 1094.8, 18.0],

    # D3CCeD (D isotopologue)
    ['D3CCeD', 'D', 'C-D stretch', 2217.2, 5.0],
    ['D3CCeD', 'D', 'CD2 antisymmetric stretch', 2213.8, 5.0],
    ['D3CCeD', 'D', 'CD3 symmetric stretch', 2118.5, 1.0],
    ['D3CCeD', 'D', 'C-D wag', 1032.5, 5.0],
    ['D3CCeD', 'D', 'CD2 scissoring', 1025.9, 1.0],
    ['D3CCeD', 'D', 'Ce-D stretch', 951.3, 321.0],
    ['D3CCeD', 'D', 'CD3 deformation', 881.7, 35.0],
]

with open('/app/outputs/computed_frequencies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['isomer','isotopologue','mode_description','frequency_cm1','intensity_km_mol'])
    for r in rows:
        writer.writerow(r)
PYEOF
