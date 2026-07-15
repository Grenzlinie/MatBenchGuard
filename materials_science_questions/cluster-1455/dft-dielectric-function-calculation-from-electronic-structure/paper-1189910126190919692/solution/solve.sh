#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_and_dispersion_results.json ===
python3 - <<'ENDOFPYTHON'
import json, math, cmath, os

# Static dielectric constants (from DFT in the paper)
pristine = {"epsilon_x": 6.7, "epsilon_y": 6.5, "epsilon_z": 4.5}
sn_int   = {"epsilon_x": 13.3, "epsilon_y": 13.2, "epsilon_z": 4.8}

# Lorentz oscillator parameters (Ref [38], Adv. Mater. 2020, 1908176)
# [100] – x  (820–972 cm⁻¹)
wx_TO = 822.0
wx_LO = 972.0
gamma_x = 4.0

# [010] – z  (955–1005 cm⁻¹)  - needed for the analytical PhP waveguide model
wz_TO = 955.0
wz_LO = 1005.0
gamma_z = 6.0

# Substrate permittivities: air = 1.0, Si ≈ 11.7 (undoped)
eps_air = 1.0
eps_Si  = 11.7
flake_thickness_um = 0.120   # 120 nm

def eps_x(omega_cm, eps_inf_x):
    """Complex permittivity along [100] (x)"""
    return eps_inf_x * (1.0 + (wx_LO**2 - wx_TO**2) / (wx_TO**2 - omega_cm**2 - 1j*gamma_x*omega_cm))

def eps_z(omega_cm, eps_inf_z):
    """Complex permittivity along [010] (z) – needed for ? in Eq. S1"""
    return eps_inf_z * (1.0 + (wz_LO**2 - wz_TO**2) / (wz_TO**2 - omega_cm**2 - 1j*gamma_z*omega_cm))

def compute_dispersion(eps_inf_x, eps_inf_z, freq_range):
    """PhP dispersion for a 120 nm flake on Si, fundamental mode l=0"""
    data = []
    for w in freq_range:
        ex = eps_x(w, eps_inf_x)
        ez = eps_z(w, eps_inf_z)
        rho = 1j * cmath.sqrt(ez / ex)
        # free-space wavevector in µm⁻¹: k0 = ?/c with ? in cm⁻¹ → 2?? * 1e-4
        k0 = 0.0002 * math.pi * w
        arg1 = eps_air * rho / ez
        arg2 = eps_Si  * rho / ez
        # Eq. S1, l=0
        q = (rho / (k0 * flake_thickness_um)) * (cmath.atan(arg1) + cmath.atan(arg2))
        k_php_real = (q * k0).real   # in-plane wavevector, µm⁻¹
        data.append({"frequency_cm-1": w, "wavevector_um-1": k_php_real})
    return data

freqs = list(range(820, 971, 10))   # 820 … 970 inclusive

pristine_disp = compute_dispersion(pristine["epsilon_x"], pristine["epsilon_z"], freqs)
sn_disp       = compute_dispersion(sn_int["epsilon_x"],   sn_int["epsilon_z"],   freqs)

# Dispersion shift at 860 cm⁻¹
pristine_k860 = compute_dispersion(pristine["epsilon_x"], pristine["epsilon_z"], [860])[0]["wavevector_um-1"]
sn_k860       = compute_dispersion(sn_int["epsilon_x"],   sn_int["epsilon_z"],   [860])[0]["wavevector_um-1"]
delta_k_over_k = (pristine_k860 - sn_k860) / pristine_k860

result = {
    "pristine": pristine,
    "Sn_intercalated": sn_int,
    "dispersion_shift": delta_k_over_k,
    "analytical_dispersion_pristine": pristine_disp,
    "analytical_dispersion_Sn": sn_disp
}

outdir = os.environ.get("OUTDIR", "/app/outputs")
output_path = os.path.join(outdir, "dft_and_dispersion_results.json")
with open(output_path, "w") as f:
    json.dump(result, f, indent=2)

print("dft_and_dispersion_results.json written")
ENDOFPYTHON
