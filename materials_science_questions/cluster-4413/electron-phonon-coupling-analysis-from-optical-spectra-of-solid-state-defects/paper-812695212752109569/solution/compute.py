#!/usr/bin/env python3
"""Reference computation of g(q) and line shapes for ξ=4 nm."""
import csv, math, itertools, os
from scipy.special import iv

# ---------- physical constants (SI) ----------
hbar = 1.054571817e-34
eV_J = 1.602176634e-19
meV_J = 1.602176634e-22
kB_J = 1.380649e-23
m0 = 9.10938356e-31

# ---------- material / model parameters ----------
rho = 5.51e3               # kg/m³
us = 4.0e3                 # m/s
Dc = -5.0  * eV_J
Dv =  1.0  * eV_J
xi = 4.0e-9                # m
lam0 = 42.0e-10            # m (42 Å)

# effective masses (CdTe)
me = 0.096 * m0
mh = 0.57  * m0
M  = me + mh
alpha = mh / M   # weight for electron
beta  = me / M   # weight for hole

# ---------- form factor helpers ----------
def f_com(q):
    """Gaussian centre-of-mass form factor."""
    return math.exp(-xi**2 * q**2 / 4.0)

def f_rel(k):
    """Exponential correlation form factor (2D)."""
    return (1.0 + (lam0 * k)**2 / 4.0)**(-1.5)

# ---------- g(q) per unit q (m) ----------
def g_per_q_m(q):
    Fe = f_com(q) * f_rel(alpha * q)
    Fh = f_com(q) * f_rel(beta  * q)
    dF = Dc * Fe - Dv * Fh   # negative Dc plus positive Dv gives addition
    num = q * dF**2
    den = 4.0 * math.pi**2 * rho * us**3 * hbar
    return num / den   # metres

# ---------- generate g(q) vs phonon energy (0 .. 4 meV) ----------
energies_meV = []
g_nm_vals = []
E_step = 0.1
for i in range(41):          # 0, 0.1, ..., 4.0
    E_meV = i * E_step
    E_J = E_meV * meV_J
    q = E_J / (hbar * us)
    g_m = g_per_q_m(q)
    g_nm = g_m * 1e9          # convert to nm for output (matches plot scale ~0.18)
    energies_meV.append(E_meV)
    g_nm_vals.append(g_nm)

# Write /tmp/gq_vs_energy.csv
with open('/tmp/gq_vs_energy.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['phonon_energy_meV', 'g'])
    for e, g in zip(energies_meV, g_nm_vals):
        w.writerow([f'{e:.1f}', f'{g:.15g}'])

# ---------- discretise into N=12 effective phonon modes ----------
Nmodes = 12
Emin = 0.0
Emax = 4.0   # meV
phi_E_meV_bins = []
for i in range(Nmodes):
    e1 = Emin + i*(Emax-Emin)/Nmodes
    e2 = e1 + (Emax-Emin)/Nmodes
    ec = (e1 + e2) / 2.0
    phi_E_meV_bins.append((e1, e2, ec))

# Fine grid for g_per_E (1/J) to integrate later
fine_estep = 0.002   # meV
fine_Es = []
fine_gE = []  # g per energy in 1/meV? We'll compute g_per_E_J (1/J) then convert to 1/meV when needed.
# Actually g_per_E_J = g_per_q_m(q) / (hbar * us)
# We'll integrate over E in J to get g_qi dimensionless.
# We'll store (E_J, g_per_E_J)
n_fine = int(Emax / fine_estep) + 40
for i in range(n_fine):
    E_meV = i * fine_estep
    if E_meV > Emax + 0.01:
        break
    E_J = E_meV * meV_J
    q = E_J / (hbar * us)
    gpm = g_per_q_m(q)
    gpE_J = gpm / (hbar * us)   # 1/J
    fine_Es.append(E_J)
    fine_gE.append(gpE_J)

# integrate to get g_qi per bin via trapezoidal rule
modes = []  # (E_meV_center, g_qi, E_J_center)
for e1_mev, e2_mev, ec_mev in phi_E_meV_bins:
    e1_J = e1_mev * meV_J
    e2_J = e2_mev * meV_J
    # integration
    integral = 0.0
    for k in range(len(fine_Es)-1):
        a = fine_Es[k]
        b = fine_Es[k+1]
        if b < e1_J or a > e2_J:
            continue
        # clip
        fa = fine_gE[k]
        fb = fine_gE[k+1]
        # linear interpolation between a,b
        # if interval straddles boundary, approximate by sub-interval
        if a < e1_J:
            # start at e1_J
            afrac = (b - e1_J) / (b - a)
            val_a = fa + (fb - fa) * (1.0 - afrac)
            integral += 0.5 * (val_a + fb) * (b - e1_J)
        elif b > e2_J:
            bfrac = (e2_J - a) / (b - a)
            val_b = fa + (fb - fa) * bfrac
            integral += 0.5 * (fa + val_b) * (e2_J - a)
        else:
            integral += 0.5 * (fa + fb) * (b - a)
    g_qi = integral   # dimensionless
    modes.append((ec_mev, g_qi, ec_mev * meV_J))  # E_J_center not used direclty

# ---------- line shape for T = 5, 30, 50 K ----------
temps = [5, 30, 50]

# helper for P(p; n,g)
def phonon_probabilities(g, n, T=None):
    """Return dict p->probability for |p|<=2.
       For n=0 use Poisson; otherwise Mahan formula."""
    probs = {}
    if n < 1e-12:
        # zero temperature limit
        eP = [1.0, g, 0.5*g**2]  # Poisson for p=0,1,2
        norm = math.exp(-g)
        probs[0] = norm * eP[0]
        probs[1] = norm * eP[1]
        probs[2] = norm * eP[2]
        # absorption impossible
        probs[-1] = 0.0
        probs[-2] = 0.0
        return probs
    
    # finite T
    expfactor = math.exp(-g * (2.0*n + 1.0))
    arg = 2.0 * g * math.sqrt(n * (n + 1.0))
    for p in range(-2, 3):
        if p == 0:
            pref = 1.0
        elif p > 0:
            pref = ((n + 1.0) / n) ** (p / 2.0)
        else:
            pref = (n / (n + 1.0)) ** (abs(p) / 2.0)
        probs[p] = expfactor * pref * iv(abs(p), arg)
    return probs

# Compute line shapes
line_records = []
for T in temps:
    # ZPL Lorentzian width (meV)
    fwhm_ueV = 180.0 + 1.5 * T   # µeV
    gamma_meV = fwhm_ueV / 1000.0  # meV
    
    # Boltzmann occupations and phonon probabilities per mode
    mode_data = []
    for idx, (ec, g_qi, E_J) in enumerate(modes):
        n_i = 0.0
        if T > 0:
            if E_J < 1e-15:
                n_i = 0.0
            else:
                n_i = 1.0 / (math.exp(E_J/(kB_J * T)) - 1.0)
        probs = phonon_probabilities(g_qi, n_i)
        mode_data.append({'ec': ec, 'g_qi': g_qi, 'n_i': n_i, 'probs': probs})
    
    # product of P_i(0)
    P0_all = 1.0
    for m in mode_data:
        P0_all *= m['probs'][0]
    if P0_all == 0.0:
        P0_all = 1e-300
    
    # collect contributions (offset_meV -> weight)
    contrib = {}
    
    # zero-phonon
    contrib[0.0] = P0_all
    
    # single phonon |p|=1 or 2
    for i, m in enumerate(mode_data):
        w0 = P0_all / m['probs'][0]
        for p in [-2, -1, 1, 2]:
            w = w0 * m['probs'][p]
            if w == 0.0:
                continue
            offset = -p * m['ec']
            contrib[offset] = contrib.get(offset, 0.0) + w
    
    # two different modes |p_i|=|p_j|=1
    for i, j in itertools.combinations(range(Nmodes), 2):
        mi = mode_data[i]
        mj = mode_data[j]
        w0 = P0_all / (mi['probs'][0] * mj['probs'][0])
        for pi in [-1, 1]:
            wi = mi['probs'][pi]
            if wi == 0.0:
                continue
            for pj in [-1, 1]:
                wj = mj['probs'][pj]
                if wj == 0.0:
                    continue
                w = w0 * wi * wj
                offset = -pi * mi['ec'] - pj * mj['ec']
                contrib[offset] = contrib.get(offset, 0.0) + w
    
    # Build intensity array on offset grid -3 .. 3 meV step 0.1
    offsets = []
    intensities = []
    gamma_half = gamma_meV / 2.0
    inv_norm = gamma_half / math.pi   # area of Lorentzian = 1
    for k in range(61):
        eoff = -3.0 + k * 0.1
        I = 0.0
        for off, w in contrib.items():
            dx = eoff - off
            # Lorentzian: L(x) = (gamma/2π) / (x^2 + (gamma/2)^2)
            I += w * inv_norm / (dx**2 + gamma_half**2)
        offsets.append(eoff)
        intensities.append(I)
    
    # normalize to peak
    peak = max(intensities)
    if peak > 0:
        intensities = [v/peak for v in intensities]
    else:
        intensities = [0.0]*len(offsets)
    
    for eoff, inten in zip(offsets, intensities):
        line_records.append((T, f'{eoff:.1f}', f'{inten:.15g}'))

# Write /tmp/line_shapes.csv
with open('/tmp/line_shapes.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['temperature_K', 'energy_offset_meV', 'intensity'])
    for rec in line_records:
        w.writerow(rec)

print('Oracle artifacts written to /tmp')
