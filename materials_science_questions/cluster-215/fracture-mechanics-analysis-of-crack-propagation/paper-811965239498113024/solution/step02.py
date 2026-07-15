import sys
sys.path.insert(0,'/solution')
import numpy as np
import eff_utils
import csv

outpath = '/app/outputs/step_02_slowness_surfaces.csv'

C_b = eff_utils.C_b
k = 0.04
h_f = 0.04
C_f = k * C_b
C_eff = eff_utils.generalized_effective_for_normal(C_b, C_f, h_f, axis=0)

def n_x3x1(theta):
    return np.array([np.sin(theta), 0.0, np.cos(theta)])
def n_x3x2(theta):
    return np.array([0.0, np.sin(theta), np.cos(theta)])
def n_x1x2(theta):
    return np.array([np.cos(theta), np.sin(theta), 0.0])

planes = [
    ('x3x1', n_x3x1),
    ('x3x2', n_x3x2),
    ('x1x2', n_x1x2)
]

angles_deg = np.arange(0, 91, 1.0)
rows = []
for plane_name, n_func in planes:
    for angle in angles_deg:
        theta = np.deg2rad(angle)
        n = n_func(theta)
        Gamma = eff_utils.christoffel(C_eff, n)
        evals = np.linalg.eigvalsh(Gamma)
        vp_sq = np.sort(evals)[::-1]
        slowness = 1.0 / np.sqrt(np.maximum(vp_sq, 1e-15))
        for i, wave_label in enumerate(['qP', 'qS1', 'qS2']):
            rows.append([plane_name, wave_label, angle, slowness[i]])

with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['plane', 'wave_type', 'angle_degrees', 'slowness_s_per_km'])
    for row in rows:
        writer.writerow(row)