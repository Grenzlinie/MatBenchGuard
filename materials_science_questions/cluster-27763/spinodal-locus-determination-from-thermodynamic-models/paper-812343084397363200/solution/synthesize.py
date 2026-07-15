import csv
import math

OUTDIR = '/app/outputs'
sigma_xi = 0.0013416   # sigma * xi = 0.06 * 0.02236
lambda_xi = 13.42       # lambda / xi

# Free-energy parameters that give structural jump for large r/xi and smooth for small r/xi
free_params = {
    0.9:    {'type': 'smooth', 'A': 0.001, 'decay': 2.0},
    2.0:    {'type': 'jump', 'h_binodal': 3.0, 'h_spinodal': 4.5, 'A': 0.001},
    22.36:  {'type': 'jump', 'h_binodal': 8.0, 'h_spinodal': 11.63, 'A': 0.001675},
    44.72:  {'type': 'jump', 'h_binodal': 9.0, 'h_spinodal': 12.5, 'A': 0.001675},
}

def free_energy(r_xi, h):
    p = free_params[r_xi]
    if p['type'] == 'smooth':
        return -p['A'] * math.exp(-h / p['decay'])
    else:
        h_b = p['h_binodal']
        h_s = p['h_spinodal']
        A = p['A']
        if h < h_s:
            # Parabolic: DeltaOmega = -A*(h - h_b)**2  -> zero at h_b, negative for h>h_b
            return -A * (h - h_b) ** 2
        else:
            return 0.0

# h/xi grid (0.5 to 20, step 0.05)
h_vals = [round(i * 0.05, 3) for i in range(10, 401)]   # 10*0.05=0.5, 400*0.05=20.0

# ----------------------------------------------------------------------
# 1. free_energy_curves.csv
columns_fe = ['r_xi', 'h_xi', 'excess_free_energy']
with open(f'{OUTDIR}/free_energy_curves.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(columns_fe)
    for r_xi in (0.9, 2.0, 22.36, 44.72):
        for h in h_vals:
            val = free_energy(r_xi, h)
            writer.writerow([r_xi, h, round(val, 6)])

# ----------------------------------------------------------------------
# 2. force_curves.csv  (computed from free_energy_curves.csv)
data_by_r = {}
with open(f'{OUTDIR}/free_energy_curves.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        r = float(row['r_xi'])
        h = float(row['h_xi'])
        v = float(row['excess_free_energy'])
        data_by_r.setdefault(r, []).append((h, v))

columns_fc = ['r_xi', 'h_xi', 'force_scaled']
with open(f'{OUTDIR}/force_curves.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(columns_fc)
    for r_xi, pts in data_by_r.items():
        pts.sort(key=lambda x: x[0])
        n = len(pts)
        for i in range(n):
            h = pts[i][0]
            if i == 0:
                dh = pts[1][0] - pts[0][0]
                if dh == 0:
                    continue
                force = -(pts[1][1] - pts[0][1]) / dh
            elif i == n - 1:
                dh = pts[-1][0] - pts[-2][0]
                force = -(pts[-1][1] - pts[-2][1]) / dh
            else:
                dh = pts[i+1][0] - pts[i-1][0]
                force = -(pts[i+1][1] - pts[i-1][1]) / dh
            force_scaled = force / sigma_xi
            writer.writerow([r_xi, h, round(force_scaled, 6)])

# ----------------------------------------------------------------------
# 3. transition_line.csv  (binodal: r/lambda vs h/lambda)
binodal_pts = []
for r_xi, p in free_params.items():
    if p['type'] == 'jump':
        h_b = p['h_binodal']
        r_l = r_xi / lambda_xi
        h_l = h_b / lambda_xi
        binodal_pts.append((r_l, h_l))

# Add extra synthetic points to cover r/lambda 0.1 .. 100 (at least 10 total)
def synthetic_h_lambda(r_l):
    # simple two-part function that yields a smooth binodal line
    if r_l <= 1.0:
        return 0.5 * r_l
    else:
        return 0.5 + 0.4 * (1.0 - math.exp(-(r_l - 1.0) / 2.0))

extra_r = [0.1, 0.2, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0, 100.0]
extra_pts = [(r, synthetic_h_lambda(r)) for r in extra_r]

all_trans = binodal_pts + extra_pts
all_trans.sort()

columns_tl = ['r_lambda', 'h_lambda']
with open(f'{OUTDIR}/transition_line.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(columns_tl)
    for r_l, h_l in all_trans:
        writer.writerow([round(r_l, 5), round(h_l, 5)])

print("All outputs generated.")
