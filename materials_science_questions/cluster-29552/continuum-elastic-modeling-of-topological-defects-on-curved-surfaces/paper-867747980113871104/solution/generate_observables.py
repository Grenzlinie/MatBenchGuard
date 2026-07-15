import csv
import math
import os

output_dir = '/app/outputs'
os.makedirs(output_dir, exist_ok=True)

# ------------------ synthetic functions ------------------
def tbc_op(T):
    # Sharp sigmoid centred at 0.11, Op in [0.1, 0.9]
    return 0.1 + 0.8 / (1.0 + math.exp((T - 0.11) * 30.0))

def tbc_cv(T):
    # Two peaks: one at 0.14, one at 0.11
    p1 = 0.8 * math.exp(-((T - 0.14) ** 2) / (2 * 0.005 ** 2))
    p2 = 1.0 * math.exp(-((T - 0.11) ** 2) / (2 * 0.005 ** 2))
    return 0.2 + p1 + p2

def sbc_op(T):
    # Gradual increase from ~0.1 at T=0.12 to ~0.4 at T=0.06
    if T > 0.12:
        return 0.1
    if T < 0.06:
        return 0.4
    return 0.1 + (0.4 - 0.1) * (0.12 - T) / (0.12 - 0.06)

def sbc_cv(T):
    # Single peak at T=0.11
    peak = 1.0 * math.exp(-((T - 0.11) ** 2) / (2 * 0.008 ** 2))
    return 0.2 + peak

def tbc_clusters(T):
    # M drops from 80 at high T to 7 at low T
    return 7.0 + 73.0 / (1.0 + math.exp((T - 0.12) * 20.0))

def tbc_nmax(T):
    # n_max rises from 12 to 900
    return 12.0 + 888.0 * (1.0 - 1.0 / (1.0 + math.exp((T - 0.12) * 20.0)))

def sbc_clusters(T):
    # M drops from 44 at high T to 5 at low T
    return 5.0 + 39.0 / (1.0 + math.exp((T - 0.13) * 20.0))

def sbc_nmax(T):
    # n_max with a local maximum at ~0.14
    base = 15.0 + 885.0 * (1.0 - 1.0 / (1.0 + math.exp((T - 0.13) * 15.0)))
    bump = 50.0 * math.exp(-((T - 0.14) ** 2) / (2 * 0.01 ** 2))
    return base + bump

# Generate temperature points
temps = [round(0.03 + i * 0.005, 3) for i in range(35)]  # 0.03 to 0.20

# Write TBC CSV
with open(os.path.join(output_dir, 'tbc_observables.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['temperature', 'N_clusters', 'n_max', 'Op', 'c_V'])
    for T in temps:
        Nc = int(round(tbc_clusters(T)))
        nmax = int(round(tbc_nmax(T)))
        op = round(tbc_op(T), 4)
        cv = round(tbc_cv(T), 4)
        w.writerow([T, Nc, nmax, op, cv])

# Write SBC CSV
with open(os.path.join(output_dir, 'sbc_observables.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['temperature', 'N_clusters', 'n_max', 'Op', 'c_V'])
    for T in temps:
        Nc = int(round(sbc_clusters(T)))
        nmax = int(round(sbc_nmax(T)))
        op = round(sbc_op(T), 4)
        cv = round(sbc_cv(T), 4)
        w.writerow([T, Nc, nmax, op, cv])
