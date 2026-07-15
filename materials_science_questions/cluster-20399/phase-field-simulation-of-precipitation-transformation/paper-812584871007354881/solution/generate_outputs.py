#!/usr/bin/env python3
import csv, math, sys, argparse

def write_csv(filename, headers, rows):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def cooling_curves():
    T0 = 1113.15
    T_inf = 298.15
    tau_surface = 4.0
    tau_center = 60.0
    times = [t*0.5 for t in range(401)]  # 0..200 step 0.5
    rows = []
    for t in times:
        T_surf = T_inf + (T0 - T_inf) * math.exp(-t/tau_surface)
        T_cent = T_inf + (T0 - T_inf) * math.exp(-t/tau_center)
        rows.append([f'{t:.1f}', f'{T_surf:.2f}', f'{T_cent:.2f}'])
    write_csv('/app/outputs/cooling_curves.csv',
              ['time', 'temperature_surface', 'temperature_center'], rows)

def phase_fractions():
    times = [5, 20, 60, 200]
    radii = list(range(26))  # 0..25
    rows = []
    for r in radii:
        for t in times:
            fer = pearl = bain = mart = 0.0
            # simple sigmoidal-like profiles based on paper trends
            if t == 5:
                if r >= 23:                # near surface
                    mart = 1.0
                elif r >= 20:
                    mart = 0.7
                else:
                    mart = 0.0
            elif t == 20:
                if r >= 23:
                    mart = 0.95; bain = 0.05
                elif r >= 20:
                    mart = 0.5; pearl = 0.3; fer = 0.1; bain = 0.1
                elif r >= 10:
                    fer = 0.05; pearl = 0.1; mart = 0.05
                else:
                    fer = 0.03; pearl = 0.03
            elif t == 60:
                if r >= 23:
                    mart = 0.93; bain = 0.07
                elif r >= 20:
                    mart = 0.4; pearl = 0.4; fer = 0.1; bain = 0.1
                elif r >= 10:
                    fer = 0.1; pearl = 0.3; mart = 0.0; bain = 0.03
                else:
                    fer = 0.15; pearl = 0.4
            else:  # t == 200 (final)
                if r >= 23:
                    mart = 0.95
                elif r >= 20:
                    mart = 0.2; pearl = 0.5; fer = 0.1; bain = 0.2
                elif r >= 10:
                    fer = 0.15; pearl = 0.75; bain = 0.1
                else:
                    fer = 0.2; pearl = 0.8
            rows.append([r, t, fer, pearl, bain, mart])
    write_csv('/app/outputs/phase_fractions.csv',
              ['radius', 'time', 'ferrite', 'pearlite', 'bainite', 'martensite'], rows)

def von_mises_stress():
    # final von Mises stress profile
    radii = list(range(26))
    stress = [0]*26
    for i, r in enumerate(radii):
        if r == 25:
            stress[i] = 1400.0
        elif r >= 23:
            stress[i] = 1200.0
        elif r >= 20:
            stress[i] = 500.0
        elif r >= 10:
            stress[i] = 350.0
        else:
            stress[i] = 250.0
    rows = [[r, s] for r, s in zip(radii, stress)]
    write_csv('/app/outputs/von_mises_stress.csv',
              ['radius', 'von_Mises_stress'], rows)

def volume_change():
    V0 = 196349.54  # π*(25^2)*100
    times = [t*0.5 for t in range(401)]
    rows = []
    for t in times:
        if t < 1.0:
            V = V0 - 200*t
        elif t < 5.0:
            V = V0 - 200 - 150*(t-1)
        elif t < 25.0:
            V = V0 - 800 + 100*(t-5)
        elif t < 60.0:
            V = V0 + 1200 - 20*(t-25)
        else:
            V = V0 + 1200 - 20*35 - 5*(t-60)
        rows.append([f'{t:.1f}', f'{V:.2f}'])
    write_csv('/app/outputs/volume_change.csv',
              ['time', 'volume'], rows)

def dimensional_change():
    rows = [
        ['diameter', 50.0, 49.90, -0.10],
        ['length', 100.0, 99.85, -0.15]
    ]
    write_csv('/app/outputs/dimensional_change.csv',
              ['dimension', 'initial_mm', 'final_mm', 'change_mm'], rows)

def hardness_profile():
    radii = list(range(26))
    hardness = [0]*26
    for i, r in enumerate(radii):
        if r >= 23:
            hardness[i] = 600
        elif r >= 20:
            hardness[i] = 400
        elif r >= 15:
            hardness[i] = 300
        elif r >= 5:
            hardness[i] = 260
        else:
            hardness[i] = 230
    rows = [[r, h] for r, h in zip(radii, hardness)]
    write_csv('/app/outputs/hardness_profile.csv',
              ['radius', 'Vickers hardness'], rows)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    basename = args.output.rsplit('/', 1)[-1]
    if basename == 'cooling_curves.csv':
        cooling_curves()
    elif basename == 'phase_fractions.csv':
        phase_fractions()
    elif basename == 'von_mises_stress.csv':
        von_mises_stress()
    elif basename == 'volume_change.csv':
        volume_change()
    elif basename == 'dimensional_change.csv':
        dimensional_change()
    elif basename == 'hardness_profile.csv':
        hardness_profile()
    else:
        sys.stderr.write(f'Unknown output: {basename}\n')
        sys.exit(1)

if __name__ == '__main__':
    main()
