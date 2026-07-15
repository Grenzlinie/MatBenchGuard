import sys, csv

def single_rows():
    # 30 rows with actual band gaps: first 15 in [0.9, 1.7], next 15 outside
    return [
        ['Al2O3', 1.32, 1.21],
        ['SiO2', 1.48, 1.35],
        ['TiO2', 1.56, 1.62],
        ['ZnO', 1.44, 1.29],
        ['GaN', 1.22, 1.08],
        ['MoS2', 1.28, 1.41],
        ['Cu2O', 1.12, 0.98],
        ['SnO2', 1.67, 1.55],
        ['Fe2O3', 1.39, 1.44],
        ['V2O5', 1.24, 1.11],
        ['WO3', 1.63, 1.70],
        ['BaTiO3', 1.41, 1.33],
        ['LiCoO2', 1.50, 1.47],
        ['Bi2Se3', 1.05, 0.94],
        ['InP', 1.15, 1.05],
        ['NaCl', 4.21, 5.67],
        ['KBr', 3.85, 4.32],
        ['MgO', 5.12, 6.01],
        ['CaF2', 5.77, 6.24],
        ['AlN', 4.66, 5.32],
        ['SiC', 2.34, 2.78],
        ['GaAs', 0.74, 0.68],
        ['CdTe', 0.82, 0.79],
        ['PbS', 0.51, 0.43],
        ['SnTe', 0.61, 0.55],
        ['InSb', 0.23, 0.18],
        ['Ge', 0.35, 0.28],
        ['Si', 0.47, 0.41],
        ['GaSb', 0.39, 0.33],
        ['CdSe', 0.87, 0.81],
    ]

def partitioned_rows():
    # 30 rows: 21 in [0.9,1.7], 9 outside
    return [
        ['Al2O3', 1.33, 1.25],
        ['SiO2', 1.47, 1.38],
        ['TiO2', 1.55, 1.60],
        ['ZnO', 1.43, 1.28],
        ['GaN', 1.24, 1.12],
        ['MoS2', 1.26, 1.36],
        ['Cu2O', 1.14, 1.02],
        ['SnO2', 1.68, 1.57],
        ['Fe2O3', 1.38, 1.46],
        ['V2O5', 1.22, 1.09],
        ['WO3', 1.62, 1.68],
        ['BaTiO3', 1.42, 1.35],
        ['LiCoO2', 1.51, 1.44],
        ['Bi2Se3', 1.07, 0.96],
        ['InP', 1.17, 1.08],
        ['CdS', 1.29, 1.19],
        ['BiI3', 1.62, 1.52],
        ['Sb2S3', 1.48, 1.41],
        ['CuGaSe2', 1.12, 1.03],
        ['CsSnI3', 1.39, 1.30],
        ['FeS2', 0.94, 0.88],
        ['AgBiI4', 1.23, 1.14],
        ['LiF', 8.34, 9.12],
        ['NaF', 7.89, 8.56],
        ['KCl', 6.45, 7.01],
        ['MgO', 5.23, 6.13],
        ['AlN', 4.71, 5.28],
        ['SiC', 2.31, 2.82],
        ['GaP', 1.71, 1.82],
        ['InN', 0.78, 0.72],
        ['CdTe', 0.83, 0.77],
    ]

if __name__ == '__main__':
    kind = sys.argv[1]
    writer = csv.writer(sys.stdout, lineterminator='\n')
    writer.writerow(['composition', 'predicted_band_gap', 'actual_band_gap'])
    rows = single_rows() if kind == 'single' else partitioned_rows()
    for row in rows:
        writer.writerow(row)
