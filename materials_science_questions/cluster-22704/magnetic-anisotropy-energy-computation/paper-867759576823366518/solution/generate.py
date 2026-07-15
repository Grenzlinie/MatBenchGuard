#!/usr/bin/env python3
"""Oracle artifact generator for Co dimer magnetic anisotropy reproduction."""
import sys
import csv
import io
import math

def write_csv(rows, fieldnames):
    """Write rows to stdout as CSV with given fieldnames."""
    writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames, lineterminator='\n')
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

def generate_exchange():
    """step_00_exchange_energies.csv: E_ex(d) for Cu and Pt, with non-monotonous RKKY sign changes."""
    # E_ex = E_FM - E_AFM; FM stable => negative.
    fieldnames = ['separation_angstrom', 'substrate', 'ordering', 'E_ex_meV']
    rows = []

    # Cu data: roughly modelled oscillatory function
    cu_vals = [
        (3.0, -20.5),
        (3.41, -15.2),
        (3.6, -10.8),
        (4.0, -4.6),
        (4.5, -1.3),
        (5.0, 2.1),
        (5.17, 0.7),
        (5.5, -2.9),
        (6.0, -4.8),
        (6.5, -1.2),
        (7.0, -0.3),
        (7.5, -2.4),
        (8.0, -5.1),
        (8.11, -7.8),
        (8.5, -3.2),
        (9.0, -1.0),
        (9.5, 0.4),
        (10.0, -0.9),
        (10.5, -0.2),
        (11.0, -1.1),
        (11.5, 0.1),
        (12.0, -0.4),
    ]
    # Pt data: weaker, similar oscillation
    pt_vals = [
        (3.0, -6.2),
        (3.5, -4.1),
        (4.0, 1.5),
        (4.5, -0.8),
        (5.0, -2.3),
        (5.63, 0.3),
        (6.0, -1.9),
        (6.5, -3.0),
        (7.0, 0.8),
        (7.5, -2.1),
        (8.0, -4.0),
        (8.5, -0.6),
        (9.0, -1.3),
        (9.5, 0.1),
        (10.0, -1.7),
        (10.5, 0.5),
        (11.0, -0.9),
        (11.5, -0.2),
        (12.0, 0.2),
    ]

    for sep, ex in cu_vals:
        rows.append({'separation_angstrom': sep, 'substrate': 'Cu', 'ordering': 'FM', 'E_ex_meV': ex})
        rows.append({'separation_angstrom': sep, 'substrate': 'Cu', 'ordering': 'AFM', 'E_ex_meV': ex})

    for sep, ex in pt_vals:
        rows.append({'separation_angstrom': sep, 'substrate': 'Pt', 'ordering': 'FM', 'E_ex_meV': ex})
        rows.append({'separation_angstrom': sep, 'substrate': 'Pt', 'ordering': 'AFM', 'E_ex_meV': ex})

    write_csv(rows, fieldnames)

def generate_anisotropy():
    """step_01_anisotropy_energies.csv: per-atom E_MA for Cu and Pt, FM and AFM."""
    fieldnames = ['separation_angstrom', 'substrate', 'ordering', 'E_MA_meV']
    rows = []

    # Cu FM: compact dimer 1.94 meV, others in 0.1–0.6 meV with non-monotonous variation
    cu_fm = [
        (3.0, 2.1),
        (3.41, 1.94),
        (3.6, 0.45),
        (4.0, 0.35),
        (4.5, 0.60),
        (5.0, 0.42),
        (5.17, 0.38),
        (5.5, 0.55),
        (6.0, 0.44),
        (6.5, 0.31),
        (7.0, 0.53),
        (7.5, 0.36),
        (8.0, 0.48),
        (8.11, 0.56),
        (8.5, 0.41),
        (9.0, 0.34),
        (9.5, 0.50),
        (10.0, 0.43),
        (10.5, 0.29),
        (11.0, 0.37),
        (11.5, 0.44),
        (12.0, 0.31),
    ]
    # Cu AFM: similar trends but less variation; average ~0.45 meV
    cu_afm = [
        (3.0, 0.52),
        (3.41, 0.51),
        (3.6, 0.49),
        (4.0, 0.46),
        (4.5, 0.45),
        (5.0, 0.44),
        (5.17, 0.43),
        (5.5, 0.47),
        (6.0, 0.45),
        (6.5, 0.43),
        (7.0, 0.46),
        (7.5, 0.44),
        (8.0, 0.47),
        (8.11, 0.48),
        (8.5, 0.45),
        (9.0, 0.43),
        (9.5, 0.46),
        (10.0, 0.44),
        (10.5, 0.42),
        (11.0, 0.45),
        (11.5, 0.43),
        (12.0, 0.44),
    ]

    # Pt FM: strong oscillation in sign and magnitude, up to several meV
    pt_fm = [
        (3.0, -2.5),
        (3.5, 3.2),
        (4.0, -1.1),
        (4.5, 2.8),
        (5.0, -0.3),
        (5.63, 0.6),
        (6.0, 4.5),
        (6.5, -3.0),
        (7.0, 5.8),
        (7.5, -4.2),
        (8.0, 1.5),
        (8.5, -0.8),
        (9.0, 3.1),
        (9.5, -1.9),
        (10.0, 2.2),
        (10.5, -0.7),
        (11.0, 1.8),
        (11.5, -0.3),
        (12.0, 1.0),
    ]
    # Pt AFM: similar oscillations but shifted
    pt_afm = [
        (3.0, -1.0),
        (3.5, 2.1),
        (4.0, -0.5),
        (4.5, 2.0),
        (5.0, -0.1),
        (5.63, 0.2),
        (6.0, 3.8),
        (6.5, -2.2),
        (7.0, 5.0),
        (7.5, -3.5),
        (8.0, 1.1),
        (8.5, -0.4),
        (9.0, 2.6),
        (9.5, -1.3),
        (10.0, 1.5),
        (10.5, -0.3),
        (11.0, 1.2),
        (11.5, -0.1),
        (12.0, 0.8),
    ]

    for sep, ema in cu_fm:
        rows.append({'separation_angstrom': sep, 'substrate': 'Cu', 'ordering': 'FM', 'E_MA_meV': ema})
    for sep, ema in cu_afm:
        rows.append({'separation_angstrom': sep, 'substrate': 'Cu', 'ordering': 'AFM', 'E_MA_meV': ema})
    for sep, ema in pt_fm:
        rows.append({'separation_angstrom': sep, 'substrate': 'Pt', 'ordering': 'FM', 'E_MA_meV': ema})
    for sep, ema in pt_afm:
        rows.append({'separation_angstrom': sep, 'substrate': 'Pt', 'ordering': 'AFM', 'E_MA_meV': ema})

    write_csv(rows, fieldnames)

def generate_magnetization():
    """step_02_magnetization_curves.csv: field sweep for representative dimers."""
    fieldnames = ['substrate', 'separation_angstrom', 'field_T', 'magnetization_norm']
    rows = []

    def add_curve(substrate, d, B0, Bc, Mr, step=0.001):
        """Generate a hysteresis loop with coercive field Bc (T), remanence Mr (norm).
        Forward sweep from -B0 to +B0; backward sweep from +B0 to -B0.
        For paramagnetic case Bc=0, Mr=0, we use a sigmoidal curve with no hysteresis."""
        if Bc == 0 and Mr == 0:
            # paramagnetic: no hysteresis; use tanh function
            fwd = [round(-B0 + i*step, 6) for i in range(int(2*B0/step)+1)]
            bwd = [round(B0 - i*step, 6) for i in range(int(2*B0/step)+1)]
            w = 0.5  # width controls slope
            mf = [math.tanh(f / w) for f in fwd]
            mb = [math.tanh(f / w) for f in bwd]
            for f, m in zip(fwd, mf):
                rows.append({'substrate': substrate, 'separation_angstrom': d,
                             'field_T': f, 'magnetization_norm': m})
            for f, m in zip(bwd, mb):
                rows.append({'substrate': substrate, 'separation_angstrom': d,
                             'field_T': f, 'magnetization_norm': m})
        else:
            # piecewise linear loop with targeted Bc and Mr
            # Forward: -B0 -> -Bc stays -1; -Bc -> 0 linear from -1 to Mr; 0 -> Bc linear from Mr to 0; Bc -> B0 linear from 0 to 1.
            pts_fwd = [
                (-B0, -1.0),
                (-Bc, -1.0),
                (0.0, Mr),
                (Bc, 0.0),
                (B0, 1.0)
            ]
            # Backward: B0 -> Bc stays 1; Bc -> 0 linear from 1 to -Mr; 0 -> -Bc linear from -Mr to 0; -Bc -> -B0 linear from 0 to -1.
            pts_bwd = [
                (B0, 1.0),
                (Bc, 1.0),
                (0.0, -Mr),
                (-Bc, 0.0),
                (-B0, -1.0)
            ]

            def linear_series(pts, start, end, num):
                """Interpolate linearly between pts over start..end with num points."""
                xs = []
                ys = []
                xs_all = [p[0] for p in pts]
                ys_all = [p[1] for p in pts]
                for i in range(num):
                    x = start + i * (end - start) / (num - 1)
                    # find segment
                    for j in range(len(pts)-1):
                        if xs_all[j] <= x <= xs_all[j+1] + 1e-9:
                            x0, x1 = xs_all[j], xs_all[j+1]
                            y0, y1 = ys_all[j], ys_all[j+1]
                            y = y0 + (x - x0) * (y1 - y0) / (x1 - x0 + 1e-12)
                            xs.append(x)
                            ys.append(y)
                            break
                return xs, ys

            n_fwd = int((2*B0)/step) + 1
            n_bwd = int((2*B0)/step) + 1
            fwd_x, fwd_y = linear_series(pts_fwd, -B0, B0, n_fwd)
            bwd_x, bwd_y = linear_series(pts_bwd, B0, -B0, n_bwd)

            for fx, fy in zip(fwd_x, fwd_y):
                rows.append({'substrate': substrate, 'separation_angstrom': d,
                             'field_T': fx, 'magnetization_norm': fy})
            for bx, by in zip(bwd_x, bwd_y):
                rows.append({'substrate': substrate, 'separation_angstrom': d,
                             'field_T': bx, 'magnetization_norm': by})

    # Cu cases
    # d=3.41 A: Bc=0.087 T, Mr=0.67
    add_curve('Cu', 3.41, 2.0, 0.087, 0.67)
    # d=5.17 A: paramagnetic (no hysteresis)
    add_curve('Cu', 5.17, 2.0, 0.0, 0.0)
    # d=8.11 A: Bc=0.120 T, Mr=0.67
    add_curve('Cu', 8.11, 2.0, 0.120, 0.67)

    # Pt cases
    # d=5.63 A: paramagnetic (no hysteresis)
    add_curve('Pt', 5.63, 10.0, 0.0, 0.0)
    # larger-anisotropy separation (d=7.0 A): Bc=4.4 T, Mr=0.8
    add_curve('Pt', 7.0, 10.0, 4.4, 0.8)

    write_csv(rows, fieldnames)

def generate_hysteresis():
    """step_03_hysteresis_summary.csv: coercive field and remanence for representative dimers."""
    fieldnames = ['substrate', 'separation_angstrom', 'coercive_field_T', 'remanence_norm']
    rows = [
        {'substrate': 'Cu', 'separation_angstrom': 3.41, 'coercive_field_T': 0.087, 'remanence_norm': 0.67},
        {'substrate': 'Cu', 'separation_angstrom': 5.17, 'coercive_field_T': 0.0, 'remanence_norm': 0.0},
        {'substrate': 'Cu', 'separation_angstrom': 8.11, 'coercive_field_T': 0.120, 'remanence_norm': 0.67},
        {'substrate': 'Pt', 'separation_angstrom': 5.63, 'coercive_field_T': 0.0, 'remanence_norm': 0.0},
        {'substrate': 'Pt', 'separation_angstrom': 7.0, 'coercive_field_T': 4.4, 'remanence_norm': 0.8},
    ]
    write_csv(rows, fieldnames)

def main():
    if len(sys.argv) < 2:
        print("Usage: generate.py <exchange|anisotropy|magnetization|hysteresis>", file=sys.stderr)
        sys.exit(1)
    mode = sys.argv[1]
    if mode == 'exchange':
        generate_exchange()
    elif mode == 'anisotropy':
        generate_anisotropy()
    elif mode == 'magnetization':
        generate_magnetization()
    elif mode == 'hysteresis':
        generate_hysteresis()
    else:
        print("Unknown mode", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
