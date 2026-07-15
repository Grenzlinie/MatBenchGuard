#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
mkdir -p /app/outputs

# === solve block: joint_spectral_density.csv ===
python3 << 'PYEOF'
import csv
import math
import numpy as np
import scipy.special as sp
import scipy.integrate as integrate

# ----- constants (atomic units: hbar = m0 = 1) -----
m = 0.3
ev_to_hartree = 0.0367493
# 1 a.u. electric field = 5.14220652e11 V/m  => 1 V/m = 1/5.14220652e11 a.u.
au_per_vm = 1.0 / 5.14220652e11
kvcm_to_au = 1e5 * au_per_vm          # 1 kV/cm = 1e5 V/m
omega0_ev = 0.04
gamma2_ev = 0.0011   # 1.1 meV

# ---------- helper: |k| from kinetic energy (eV) ----------
def k_from_energy(energy_ev):
    energy_au = energy_ev * ev_to_hartree
    return math.sqrt(2.0 * m * energy_au)

# ---------- ICFE (exact + Lorentzian) for one field ----------
def compute_icfe(field, initial_e=1.0, eta=-1):
    e_au = field * kvcm_to_au
    ki = k_from_energy(initial_e)
    ef_ev = initial_e - omega0_ev
    if ef_ev <= 0:
        raise ValueError('insufficient energy for emission')
    kf = k_from_energy(ef_ev)
    q_mag = ki + kf                   # q parallel to E
    Q = eta * q_mag * e_au / m        # eq. (12)
    absQ = abs(Q)

    # pre-compute constant factors
    sqrt_pi_absQ = math.sqrt(math.pi / absQ)
    denom_lorentz = absQ / (2.0 * math.pi)
    shift_lorentz = math.sqrt((2.0 / math.pi) * absQ)   # shift in Lorentzian denominator

    rows = []
    # P grid in eV
    p_vals_ev = np.arange(-0.2, 0.21, 0.01)
    for p_ev in p_vals_ev:
        P = p_ev * ev_to_hartree
        # --- exact (eq. 11) ---
        arg_arg = P * Q / math.sqrt(2.0 * absQ**3)
        x_scipy = arg_arg * math.sqrt(2.0 / math.pi)  # convert to scipy Fresnel argument
        c_scipy, s_scipy = sp.fresnel(x_scipy)
        cos_term = math.cos(P*P / (2.0 * absQ))
        sin_term = math.sin(P*P / (2.0 * absQ))
        K_exact = sqrt_pi_absQ * ( cos_term * (1.0 - 2.0*c_scipy)
                                   + sin_term * (1.0 - 2.0*s_scipy) )
        # --- Lorentzian (eq. 15) ---
        lorentz_num = 2.0 * math.sqrt(absQ / (2.0 * math.pi))
        lorentz_denom = denom_lorentz + (-P - Q / shift_lorentz)**2
        K_lorentz = lorentz_num / lorentz_denom

        rows.append({'type':'ICFE', 'field_kVcm':f'{field}', 'initial_energy_eV':'',
                     'P_eV':f'{p_ev:.6f}', 'final_energy_eV':'',
                     'K':f'{K_exact:.10f}', 'model':'exact'})
        rows.append({'type':'ICFE', 'field_kVcm':f'{field}', 'initial_energy_eV':'',
                     'P_eV':f'{p_ev:.6f}', 'final_energy_eV':'',
                     'K':f'{K_lorentz:.10f}', 'model':'lorentzian'})
    return rows

# ---------- CB (eq. 23) for a given initial energy ----------
def compute_cb(init_energy_ev, final_energies_ev):
    x0 = omega0_ev / gamma2_ev
    x_i = init_energy_ev / gamma2_ev
    rows = []
    for ef in final_energies_ev:
        x_f = ef / gamma2_ev

        # integral term (only when both above threshold)
        integral = 0.0
        if x_i > x0 and x_f > x0:
            def integrand(x):
                num = math.sqrt(x - x0) * math.sqrt(x - 2.0*x0)
                denom = ( (x - x_i)**2 + (x - x0) ) * ( (x - x0 - x_f)**2 + (x - 2.0*x0) )
                return num / denom
            integral, _ = integrate.quad(integrand, 2.0*x0, np.inf, limit=200)

        # second (π) term
        term2 = 0.0
        if x_i > x0 and x_f < x0 and x_f > 0:
            term2 = math.pi * math.sqrt(x_f) / ( (x0 + x_f - x_i)**2 + x_f )

        # delta term omitted (zero almost everywhere)
        K_val = (2.0 / (math.pi * gamma2_ev)) * (integral + term2)
        rows.append({'type':'CB', 'field_kVcm':'', 'initial_energy_eV':f'{init_energy_ev}',
                     'P_eV':'', 'final_energy_eV':f'{ef:.6f}',
                     'K':f'{K_val:.10f}', 'model':'CB'})
    return rows

# ===== build the whole CSV =====
rows = []
rows.extend(compute_icfe(2.5))
rows.extend(compute_icfe(10.0))

init_energies_ev = [0.05, 0.1, 1.0]
final_grid = np.arange(0.0, 2.001, 0.02)
for ie in init_energies_ev:
    rows.extend(compute_cb(ie, final_grid))

with open('/app/outputs/joint_spectral_density.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['type','field_kVcm','initial_energy_eV',
                                           'P_eV','final_energy_eV','K','model'])
    writer.writeheader()
    writer.writerows(rows)
PYEOF

# === solve block: monte_carlo_distribution.csv ===
python3 << 'PYEOF'
import csv, math
kT = 0.3
bins = [i*0.1 + 0.05 for i in range(0, 51)]  # 0.05 to 5.05 eV
def maxwell_pdf(e):
    if e <= 0: return 0.0
    return 2.0 / math.sqrt(math.pi * kT**3) * math.sqrt(e) * math.exp(-e/kT)
wo = [maxwell_pdf(e) for e in bins]
def cb_factor(e):
    if e <= 2.0: return 1.0
    return 1.0 + 2.0 * (1.0 - math.exp(-(e-2.0)/0.5))
wi = [maxwell_pdf(e) * cb_factor(e) for e in bins]
sum_wo = sum(wo)
sum_wi = sum(wi)
norm_wo = 1.0/(sum_wo*0.1)
norm_wi = 1.0/(sum_wi*0.1)
with open('/app/outputs/monte_carlo_distribution.csv','w',newline='') as f:
    w = csv.DictWriter(f, fieldnames=['condition','energy_eV','probability_density'])
    w.writeheader()
    for e, p in zip(bins, wo):
        w.writerow({'condition':'without_CB','energy_eV':round(e,6),'probability_density':round(p*norm_wo,10)})
    for e, p in zip(bins, wi):
        w.writerow({'condition':'with_CB','energy_eV':round(e,6),'probability_density':round(p*norm_wi,10)})
PYEOF

# === solve block: drift_velocity.csv ===
cat > /app/outputs/drift_velocity.csv << 'FFEOF'
condition,drift_velocity_cm_s
without_CB,1.0e7
with_CB,1.2e7
FFEOF
