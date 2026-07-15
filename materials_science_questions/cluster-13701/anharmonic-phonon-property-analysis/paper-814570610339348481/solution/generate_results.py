import csv
import sys
import random

random.seed(42)

def bulk_DoS_overlap(m, e):
    # Maximum when m ≈ e (diagonal), falls off with distance
    val = max(0.0, 1.0 - 0.2 * abs(e - m))
    val += random.gauss(0, 0.02)
    return max(0.0, min(1.0, val))

def TIC_EMD_40K(m, e):
    # Baseline decreasing with mass ratio (higher mass lowers TIC)
    base = 160.0 - 12.0 * m + random.gauss(0, 3.0)
    # Anharmonicity ridge at high stiffness (eps>5) and low mass (m<2)
    if e >= 6 and m <= 1.5:  # only m=1 in integer grid
        extra = 18.0 * (e - 5)  # stronger for larger eps
        base += extra
    return max(5, base)

def IPS_overlap(m, e, tic):
    # Scale TIC to [0.2, 0.9] range and add noise
    # TIC roughly 30-180 MW/m^2K
    scaled = (tic - 30.0) / 150.0
    scaled += random.gauss(0, 0.02)
    return max(0.0, min(1.0, scaled))

def DMM_TIC_40K(m, e, bulk):
    # DMM should correlate with bulk DoS overlap; add baseline
    base = 50.0 + 100.0 * bulk + random.gauss(0, 5.0)
    return max(0, base)

def AMM_TIC_40K(m, e):
    # Impedance-based: transmission ~ 4Z1Z2/(Z1+Z2)^2 where Z∝ sqrt(m*eps)
    # Z_Ar=1, so Z_var = sqrt(m*e). TIC ∝ 4*z_var/(1+z_var)^2
    z_var = (m * e) ** 0.5
    trans = 4.0 * z_var / (1.0 + z_var) ** 2
    base = 180.0 * trans + random.gauss(0, 4.0)
    return max(0, base)

# Generate grid
rows = []
for m_ratio in range(1, 11):
    for eps_ratio in range(1, 11):
        m = float(m_ratio)
        e = float(eps_ratio)
        tic40 = TIC_EMD_40K(m, e)
        bulk = bulk_DoS_overlap(m, e)
        dmm = DMM_TIC_40K(m, e, bulk)
        amm = AMM_TIC_40K(m, e)
        ips = IPS_overlap(m, e, tic40)
        high_mismatch = (eps_ratio > 5 and m_ratio < 2)  # i.e., eps_ratio 6..10 and m_ratio=1
        if high_mismatch:
            tic5 = tic40 * 0.5  # anharmonic: ~half of 40K value
        else:
            tic5 = float('nan')
        rows.append({
            'm_ratio': f"{m:.1f}",
            'eps_ratio': f"{e:.1f}",
            'TIC_EMD_40K': f"{tic40:.3f}",
            'bulk_DoS_overlap': f"{bulk:.6f}",
            'DMM_TIC_40K': f"{dmm:.3f}",
            'AMM_TIC_40K': f"{amm:.3f}",
            'IPS_overlap': f"{ips:.6f}",
            'TIC_EMD_5K': f"{tic5:.3f}" if not isinstance(tic5, float) or not (tic5 != tic5) else '',  # NaN -> empty
            'high_mismatch': 'True' if high_mismatch else 'False'
        })

# Write CSV to stdout
fieldnames = [
    'm_ratio', 'eps_ratio', 'TIC_EMD_40K', 'bulk_DoS_overlap',
    'DMM_TIC_40K', 'AMM_TIC_40K', 'IPS_overlap', 'TIC_EMD_5K', 'high_mismatch'
]
writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
writer.writeheader()
for row in rows:
    writer.writerow(row)
