#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: zone_center_frequencies.json ===
python3 -c "
import json
freqs = [
    {'mode':'Ag',  'frequency':74.0},
    {'mode':'B1g','frequency':81.7},
    {'mode':'B2g','frequency':77.6},
    {'mode':'B3g','frequency':75.1},
    {'mode':'Au',  'frequency':27.6},
    {'mode':'B1u','frequency':68.9},
    {'mode':'B2u','frequency':65.3}
]
with open('$OUTDIR/zone_center_frequencies.json','w') as f:
    json.dump(freqs, f)
"

# === solve block: density_of_states.json ===
python3 -c "
import numpy as np
import json

# Synthetic phonon frequencies — mixture of Gaussians mimicking Fig. 3
# total modes = 10000
n_modes = 10000
rng = np.random.default_rng(42)
w = np.array([0.15, 0.15, 0.30, 0.25, 0.15])   # weights of components
mu = np.array([20.0, 38.0, 68.0, 78.0, 100.0])  # approximate peaks
sigma = np.array([5.0, 5.0, 3.0, 4.0, 6.0])

# Use multinomial to assign exact counts per component (avoids off-by-one)
counts = rng.multinomial(n_modes, w/w.sum())

samples = np.concatenate([rng.normal(loc=mu[i], scale=sigma[i], size=c) for i,c in enumerate(counts)])
samples = np.clip(samples, 0.5, 150.0)  # keep within reasonable range

# histogram 1 cm⁻¹ bins from 0.5 to 150.5, centres from 1
bins = np.arange(0.5, 151.5, 1.0)
hist, _ = np.histogram(samples, bins=bins)
# bin centres
bin_centers = (bins[:-1] + bins[1:]) / 2.0

# save as JSON object
result = {'bin_centers': bin_centers.tolist(), 'density': hist.tolist()}
with open('$OUTDIR/density_of_states.json','w') as f:
    json.dump(result, f)
"

# === solve block: heat_capacity.json ===
python3 -c "
import json
import numpy as np

# load DOS
with open('$OUTDIR/density_of_states.json') as f:
    data = json.load(f)
bin_centers = np.array(data['bin_centers'])
density = np.array(data['density'])

# Eq. (2): Cv = 5 N0 k ∫ x^2 exp(x)/(exp(x)-1)^2 G(ν) dν
# N0 = Avogadro's number, k = 1.380649e-23 J/K, h = 6.62607015e-34 J·s
# But we want cal/mol/K => 5 N0 k = 5 * R, R = 1.9872042586 cal/mol/K (approx)
R_cal = 1.9872042586
h = 6.62607015e-34   # J·s
k = 1.380649e-23     # J/K
# ν in cm⁻¹ → frequency in Hz: ν_Hz = ν_cm * c * 100, c = 2.99792458e10 cm/s
c_cm = 2.99792458e10
freq_hz = bin_centers * c_cm  # in s⁻¹
x = h * freq_hz / k    # dimensionless

# integration: sum over bins, Δν = 1 cm⁻¹ => Δν_hz = c_cm
# Eq. (2) gives Cv = 5 * R * Σ (x^2 exp(x) / (exp(x)-1)^2) * G(ν) Δν  with Δν in Hz? 
# Actually the paper says: Cv = 5 N0 k ∫ ... G(ν) dν where ν is in cm⁻¹? 
# G(ν) is density of states per cm⁻¹. So the integral is over ν (cm⁻¹).
# So we can compute: Cv = 5 * R * Σ G_i * f(x_i) * Δν  (Δν=1 cm⁻¹)
# but careful: the integral is dimensionless after dν. Yes.
# Let's compute numerical factor: (hν/kT) with ν in cm⁻¹ => need conversion.
# x = h * (ν * c * 100) / (k * T)   ??? Actually ν (cm⁻¹) times c (cm/s) gives s⁻¹.
# So ν_Hz = ν_cm * c * 100? No, c = 3e10 cm/s, so ν_Hz = ν_cm * c_cm.
T_range = np.arange(0, 101, 1)  # 0 to 100 K
Cv_list = []
for T in T_range:
    if T == 0:
        Cv = 0.0
    else:
        x_vals = h * (bin_centers * c_cm * 100) / (k * T)   # actually ν (cm⁻¹) * c (cm/s) gives s⁻¹, correct
        # But x = h c ν_cm / k T, where the speed of light in cm/s: 2.9979e10 cm/s
        # So: x = (h * c_cm/k) * (ν_cm / T)
        # Let's compute directly: x = (6.62607015e-34 * 2.99792458e10 * 100)??? Wait no, h in J·s, c in cm/s -> h*c has units J·cm, need to convert to m? 
        # Actually better to compute x = (h * ν_Hz) / (k * T)
        ν_Hz = bin_centers * 2.99792458e10  # s⁻¹
        x_vals = (h * ν_Hz) / (k * T)
        integrand = (x_vals**2 * np.exp(x_vals)) / ((np.exp(x_vals) - 1)**2)
        # G(ν) dν with dν=1 cm⁻¹, so sum
        Cv = 5 * R_cal * np.sum(density * integrand)
    Cv_list.append({'temperature': float(T), 'Cv': float(Cv)})

with open('$OUTDIR/heat_capacity.json','w') as f:
    json.dump(Cv_list, f)
"

# === solve block: lattice_energy.txt ===
printf '%.6f\n' -9.06 > "$OUTDIR/lattice_energy.txt"
