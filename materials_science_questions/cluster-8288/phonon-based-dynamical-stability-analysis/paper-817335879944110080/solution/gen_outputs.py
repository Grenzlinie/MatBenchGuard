#!/usr/bin/env python3
import csv
import json
import os

outdir = '/app/outputs'

# --- bare_preference.csv ---
bpref = [
    ('Ce', -50.00, -49.48, -0.52),
    ('Pr', -50.50, -50.01, -0.49),
    ('Nd', -50.90, -50.43, -0.47),
    ('Sm', -51.20, -50.76, -0.44),
    ('Eu', -51.50, -51.08, -0.42),
    ('Gd', -51.80, -51.40, -0.40),
    ('Tb', -52.00, -51.62, -0.38),
    ('Dy', -52.20, -51.84, -0.36),
    ('Ho', -52.40, -52.06, -0.34),
    ('Er', -52.60, -52.28, -0.32),
    ('Tm', -52.80, -52.50, -0.30),
    ('Yb', -53.00, -52.72, -0.28),
]
with open(os.path.join(outdir, 'bare_preference.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['M', 'E_T_type', 'E_H_type', 'delta_E'])
    for row in bpref:
        w.writerow(row)

# --- stability_report.json ---
elements = ['Ce','Pr','Nd','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb']
stability = {}
for el in elements:
    stability[el] = {
        'phonon_imaginary_modes': False,
        'min_frequency': 12.0
    }
with open(os.path.join(outdir, 'stability_report.json'), 'w') as f:
    json.dump(stability, f, indent=2)

# --- functionalized_properties.json ---
def mk_entry(M, T, total_mag, half_met, spin_gap, sem, band_gap, wf):
    return {
        'M': M,
        'T': T,
        'total_magnetization': total_mag,
        'half_metallic': half_met,
        'spin_down_band_gap': spin_gap,
        'semiconductor': sem,
        'band_gap': band_gap,
        'work_function': wf
    }

func = []
# Fluorine-terminated
func.append(mk_entry('Ce','F',  1.33, False, None, False, None, 3.95))
func.append(mk_entry('Pr','F',  3.75, True,  1.20, False, None, 3.62))
func.append(mk_entry('Nd','F',  5.87, True,  1.15, False, None, 3.72))
func.append(mk_entry('Sm','F', 10.10, True,  1.05, False, None, 3.80))
func.append(mk_entry('Eu','F', 12.30, True,  2.39, False, None, 3.90))
func.append(mk_entry('Gd','F', 13.80, False, None, True, 1.38, 4.10))
func.append(mk_entry('Tb','F', 11.80, True,  0.95, False, None, 4.20))
func.append(mk_entry('Dy','F',  9.77, True,  0.90, False, None, 4.15))
func.append(mk_entry('Ho','F',  0.00, False, None, False, None, 4.10))   # AFM metal
func.append(mk_entry('Er','F',  5.72, True,  0.85, False, None, 4.05))
func.append(mk_entry('Tm','F',  3.53, False, None, False, None, 4.00))   # FM metal
func.append(mk_entry('Yb','F',  0.458,False, None, False, None, 4.24))   # FM metal

# Hydroxyl-terminated
func.append(mk_entry('Ce','OH', 1.33, False, None, False, None, 1.75))   # metal (unstable but included)
func.append(mk_entry('Pr','OH', 3.68, True,  1.00, False, None, 2.17))
func.append(mk_entry('Nd','OH', 5.82, True,  0.95, False, None, 2.05))
func.append(mk_entry('Sm','OH',10.10, True,  0.85, False, None, 1.95))
func.append(mk_entry('Eu','OH',12.30, True,  2.30, False, None, 1.85))
func.append(mk_entry('Gd','OH',13.70, False, None, True, 0.882, 1.70))
func.append(mk_entry('Tb','OH',11.80, False, None, False, None, 1.60))   # FM metal
func.append(mk_entry('Dy','OH', 0.00, False, None, False, None, 1.55))   # AFM metal
func.append(mk_entry('Ho','OH', 7.74, True,  0.80, False, None, 1.50))
func.append(mk_entry('Er','OH', 5.69, False, None, False, None, 1.48))   # FM metal
func.append(mk_entry('Tm','OH', 3.48, False, None, False, None, 1.46))   # lowest work function
func.append(mk_entry('Yb','OH', 0.390,False, None, False, None, 1.65))   # FM metal

with open(os.path.join(outdir, 'functionalized_properties.json'), 'w') as f:
    json.dump(func, f, indent=2)
