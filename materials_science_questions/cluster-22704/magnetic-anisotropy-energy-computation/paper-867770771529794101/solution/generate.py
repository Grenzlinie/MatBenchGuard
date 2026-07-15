import os, sys, math, csv

OUTDIR = os.environ['OUTDIR']
output_path = os.path.join(OUTDIR, 'mae_vs_peak.csv')

# Parameters
start_e = -8.0
end_e   = -2.0
n_steps = 101
step = (end_e - start_e) / (n_steps - 1)

# Model functions
def occupancy_Nd(eps):
    # Linear occupancy: N_d = 2.0 - 0.25*(eps+4)
    # At eps=-8 -> 3.0, -6 -> 2.5, -4 -> 2.0, -2 -> 1.5
    return 2.0 - 0.25 * (eps + 4.0)

def peak_position(eps):
    if eps <= -6.0:
        return 0.0
    elif eps <= -4.0:
        # parabolic rise from 0 at -6 to max (150 meV) at -4
        t = (eps + 6.0) / 2.0  # [0,1]
        return 150.0 * t * t
    else:
        # linear increase for eps > -4
        return 150.0 + 75.0 * (eps + 4.0)  # 75 meV per eV

def MAE(eps, peak):
    if peak < 100.0:
        # linear regime
        return 0.5 + 0.05 * peak
    elif peak <= 150.0:
        # linear transition to asymptotic value at peak=150
        return 5.5 + (6.9 - 5.5) * (peak - 100.0) / (150.0 - 100.0)
    else:
        # beyond half-filling, keep near the renormalized value
        return 6.9

with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['epsilon_d', 'occupancy_Nd', 'peak_position', 'MAE'])
    for i in range(n_steps):
        eps = start_e + i * step
        nd = occupancy_Nd(eps)
        peak = peak_position(eps)
        mae = MAE(eps, peak)
        writer.writerow([f'{eps:.6f}', f'{nd:.6f}', f'{peak:.6f}', f'{mae:.6f}'])
