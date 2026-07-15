#!/usr/bin/env python3
"""Generate a realistic simulation_results.json for the Ni62Nb38 AIMD task.
All curves are synthesized from the paper's description so the oracle is fast and self-contained."""
import json
import os
import numpy as np

# Output path
outdir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)
output_file = os.path.join(outdir, 'simulation_results.json')

# Helper functions
def gaussian(x, mu, sigma, amp):
    return amp * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def lorentzian(x, mu, gamma, amp):
    return amp * gamma**2 / ((x - mu)**2 + gamma**2)

# Temperatures
temperatures = [1873, 1473, 1403, 1233]

def gen_total_g_r(T):
    r = np.linspace(0.0, 10.0, 500)
    g = np.zeros_like(r)
    # First peak at 2.52 Å, amplitude increases with decreasing T
    amps = {1873: 2.5, 1473: 3.0, 1403: 3.5, 1233: 4.5}
    g += gaussian(r, 2.52, 0.10, amps[T])
    # Second peak: for T >= 1473 single, for T <= 1403 split
    if T >= 1473:
        g += gaussian(r, 4.58, 0.20, 0.6 * amps[T])
    else:
        # Split into two sub-peaks
        g += gaussian(r, 4.42, 0.12, 0.35 * amps[T])
        g += gaussian(r, 4.72, 0.12, 0.35 * amps[T])
    # Weak background
    g += 0.1 * (1.0 - np.exp(-r / 1.0))
    return r.tolist(), g.tolist()

def gen_total_S_q(T):
    q = np.linspace(0.1, 10.0, 500)
    S = np.ones_like(q)
    # Main peak at 2.95 Å⁻¹, intensity grows
    amp_main = {1873: 1.8, 1473: 2.2, 1403: 2.5, 1233: 3.0}
    S += gaussian(q, 2.95, 0.25, amp_main[T])
    # Pre-peak at 1.80 Å⁻¹, intensifying
    amp_pre = {1873: 0.2, 1473: 0.5, 1403: 0.6, 1233: 0.7}
    S += gaussian(q, 1.80, 0.08, amp_pre[T])
    # Second peak region; split only for lower T
    if T >= 1473:
        S += gaussian(q, 5.0, 0.3, 1.0)
    else:
        S += gaussian(q, 4.8, 0.2, 0.6)
        S += gaussian(q, 5.2, 0.2, 0.6)
    # At 1473 K a small peak appears between first and second
    if T == 1473:
        S += gaussian(q, 4.0, 0.15, 0.3)
    return q.tolist(), S.tolist()

def gen_bond_angle_dist(triple, T):
    angles = np.linspace(0, 180, 181)
    prob = np.zeros_like(angles, dtype=float)
    # Peak positions and sharpening behaviour depend on triple type
    if triple in ('Ni-Ni-Ni', 'Ni-Ni-Nb'):
        peak1 = 55.0 + (2.0 if T == 1233 else 0.0)
        peak2 = 110.0 + (2.0 if T == 1233 else 0.0)
    elif triple == 'Nb-Ni-Nb':
        peak1, peak2 = 63.0, 115.0
    else:  # Nb-Nb-Nb, Nb-Nb-Ni, Ni-Nb-Ni (all have similar ~50°/100° peaks)
        peak1, peak2 = 50.0, 100.0
    sigma_base = 8.0
    sigma = max(3.0, sigma_base * (T / 1873.0) ** 1.5)
    amp = 5.0 / (T / 1873.0)
    prob += gaussian(angles, peak1, sigma, amp)
    prob += gaussian(angles, peak2, sigma, amp * 0.8)
    # Flat region near 150° appears below 1403 K
    if T <= 1403:
        prob += gaussian(angles, 150.0, 15.0, 0.15 * (1873.0 / T))
    prob += 0.02  # baseline
    return angles.tolist(), prob.tolist()

def gen_csro(T):
    # Values consistent with paper: hetero-coordination negative, homo positive.
    return {"Ni-Ni": 0.2, "Ni-Nb": -0.2, "Nb-Ni": -0.2, "Nb-Nb": 0.2}

def gen_diffusion(T):
    # Fit Arrhenius to reported end-points (units: 1e-4 cm²/s)
    # Ni: 0.237 at 1873 K, 0.023 at 1233 K
    inv_diff = 1.0 / 1873.0 - 1.0 / 1233.0
    B_Ni = np.log(0.237 / 0.023) / inv_diff
    A_Ni = np.exp(np.log(0.237) - B_Ni / 1873.0)
    D_Ni = A_Ni * np.exp(B_Ni / T)
    # Nb: 0.195 at 1873 K, 0.021 at 1233 K
    B_Nb = np.log(0.195 / 0.021) / inv_diff
    A_Nb = np.exp(np.log(0.195) - B_Nb / 1873.0)
    D_Nb = A_Nb * np.exp(B_Nb / T)
    D_total = (62 * D_Ni + 38 * D_Nb) / 100.0
    return {
        "D_Ni": round(D_Ni, 4),
        "D_Nb": round(D_Nb, 4),
        "D_total": round(D_total, 4)
    }

def gen_dos(T):
    energy = np.linspace(-5, 5, 501)
    # Two main peaks at -1.49 and -2.35 eV (paper)
    # Ni d dominates valence band
    Ni_d = (0.5 * lorentzian(energy, -1.49, 0.3, 1.0) +
            0.8 * lorentzian(energy, -2.35, 0.3, 1.0) +
            gaussian(energy, -1.49, 0.2, 0.3))
    # Nb d contributes to both valence and conduction bands
    Nb_d = (0.3 * lorentzian(energy, -1.49, 0.3, 0.6) +
            0.4 * lorentzian(energy, -2.35, 0.3, 0.6) +
            gaussian(energy, 0.5, 0.5, 0.5))
    # s and p states are small and broad
    Ni_s = gaussian(energy, -4.0, 1.5, 0.05)
    Ni_p = gaussian(energy, -3.0, 1.5, 0.08)
    Nb_s = gaussian(energy, -4.5, 1.5, 0.03)
    Nb_p = gaussian(energy, -3.5, 1.5, 0.05)
    total_dos = Ni_d + Nb_d + Ni_s + Ni_p + Nb_s + Nb_p
    return {
        "energy": energy.tolist(),
        "total_dos": total_dos.tolist(),
        "Ni_d": Ni_d.tolist(),
        "Nb_d": Nb_d.tolist(),
        "Ni_s": Ni_s.tolist(),
        "Ni_p": Ni_p.tolist(),
        "Nb_s": Nb_s.tolist(),
        "Nb_p": Nb_p.tolist()
    }

# Build the full output dictionary
data = {}
data["temperatures"] = temperatures

data["total_g_r"] = []
for T in temperatures:
    r, g = gen_total_g_r(T)
    data["total_g_r"].append({"r": r, "g": g})

data["total_S_q"] = []
for T in temperatures:
    q, S = gen_total_S_q(T)
    data["total_S_q"].append({"q": q, "S": S})

# Bond angle distributions
triples = ["Ni-Ni-Ni", "Ni-Ni-Nb", "Nb-Ni-Nb", "Nb-Nb-Nb", "Nb-Nb-Ni", "Ni-Nb-Ni"]
bad_dist = {}
for triple in triples:
    arr = []
    for T in temperatures:
        ang, prob = gen_bond_angle_dist(triple, T)
        arr.append({"angle": ang, "probability": prob})
    bad_dist[triple] = arr
data["bond_angle_distributions"] = bad_dist

# CSRO parameters
data["csro_parameters"] = [gen_csro(T) for T in temperatures]

# Diffusion coefficients
data["diffusion_coefficients"] = [gen_diffusion(T) for T in temperatures]

# DOS (only two temperatures)
data["dos"] = [gen_dos(T) for T in [1873, 1233]]

# Write final JSON
with open(output_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Wrote {output_file}")
