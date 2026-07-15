#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_sc_sdel.json ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

python3 << 'PYEOF'
import math
import json

# ---------- Constants ----------
R = 8.314            # J/mol/K
M_w = 0.018          # kg/mol water
rho_w = 1000.0       # kg/m^3 water
sigma_w = 0.072      # J/m^2 surface tension of water
T = 298.15           # K
M_aa = 0.14614       # kg/mol adipic acid
rho_aa = 1360.0      # kg/m^3 adipic acid density
solubility_gL = 25.0 # g/L (unused but kept for reference)

a_sz = 0.0106        # Szyszkowski-Langmuir parameter a
b_sz = 11.836        # Szyszkowski-Langmuir parameter b

gamma_w_del = 0.990  # water activity for deliquescence
sigma_del_low = 0.060
sigma_del_high = 0.072
sigma_del_mid = 0.066

# ---------- Helper functions ----------

def compute_S_pct(d_d, d_p):
    """Kohler supersaturation percent for given dry diam d_d (m) and wet diam d_p (m)."""
    # mass of dry particle
    V_dry = (math.pi/6.0) * d_d**3
    m_aa = V_dry * rho_aa   # kg
    n_aa = m_aa / M_aa       # mol

    # volume of droplet
    V_drop = (math.pi/6.0) * d_p**3
    # mass of water in droplet (assume solution density = rho_w, i.e. volume additivity approx)
    m_w = V_drop * rho_w - m_aa
    if m_w <= 0:
        return -1.0   # invalid, supersaturation not defined
    n_w = m_w / M_w

    # mole fraction of water
    x_w = n_w / (n_w + n_aa)

    # concentration of dissolved carbon (mol carbon per kg water)
    # adipic acid has 6 carbon atoms
    C = (n_aa * 6.0) / m_w   # m_w in kg

    # surface tension from Szyszkowski-Langmuir
    sigma = sigma_w - a_sz * T * math.log(1.0 + b_sz * C)
    if sigma < 0:
        sigma = 0.0  # safeguard

    # Kohler equation: S_w = gamma_w * x_w * exp(...), gamma_w = 1 for ideal
    kelvin = (4.0 * M_w * sigma) / (R * T * rho_w * d_p)
    S_w = x_w * math.exp(kelvin)
    S_pct = (S_w - 1.0) * 100.0
    return S_pct

def golden_section_max(d_d, a, b, tol=1e-12):
    """Golden-section search for maximum of f(d_p)=S_pct on interval [a,b]."""
    phi = (math.sqrt(5.0) - 1.0) / 2.0
    resphi = 2.0 - phi
    
    # initial points
    c = a + resphi * (b - a)
    d = a + phi * (b - a)
    fc = compute_S_pct(d_d, c)
    fd = compute_S_pct(d_d, d)
    
    while abs(b - a) > tol * (abs(c) + abs(d)):
        if fc > fd:
            b = d
            d = c
            fd = fc
            c = a + resphi * (b - a)
            fc = compute_S_pct(d_d, c)
        else:
            a = c
            c = d
            fc = fd
            d = a + phi * (b - a)
            fd = compute_S_pct(d_d, d)
    x_max = 0.5 * (a + b)
    S_max = compute_S_pct(d_d, x_max)
    # Ensure we got the maximum; sometimes the maximum is at an endpoint if function is not unimodal? 
    # But for Kohler, it's smooth and the maximum lies inside. We'll return the found peak.
    return S_max

def Sdel_pct(d_d, sigma_sat):
    """Deliquescence supersaturation % for given dry diameter d_d (m) and sigma_sat."""
    kelvin = (4.0 * M_w * sigma_sat) / (d_d * rho_w * R * T)
    S_w_del = gamma_w_del * math.exp(kelvin)
    return (S_w_del - 1.0) * 100.0

# ---------- Generate curves ----------
dry_diameters_nm = []
Sc_kohler_pct = []
Sdel_lower_pct = []
Sdel_upper_pct = []

# Use 0.5 nm step from 50 to 300 nm
start_nm = 50.0
end_nm = 300.0
step_nm = 0.5

# Store computed values for crossover detection
Sc_vals = []
Sdel_mid_vals = []

d_nm = start_nm
while d_nm <= end_nm:
    d_d = d_nm * 1e-9   # m
    
    # critical supersaturation via golden-section search
    # search bracket: from just above dry particle to 20 times dry diameter
    a = d_d * 1.001
    b = d_d * 20.0
    Sc = golden_section_max(d_d, a, b)
    
    # deliquescence supersaturations
    S_low = Sdel_pct(d_d, sigma_del_low)
    S_high = Sdel_pct(d_d, sigma_del_high)
    S_mid = Sdel_pct(d_d, sigma_del_mid)
    
    dry_diameters_nm.append(round(d_nm, 1))
    Sc_kohler_pct.append(round(Sc, 8))
    Sdel_lower_pct.append(round(S_low, 8))
    Sdel_upper_pct.append(round(S_high, 8))
    
    Sc_vals.append(Sc)
    Sdel_mid_vals.append(S_mid)
    
    d_nm += step_nm

# ---------- Crossover diameter ----------
crossover_diameter_nm = None
for i in range(len(dry_diameters_nm) - 1):
    diff_i = Sc_vals[i] - Sdel_mid_vals[i]
    diff_next = Sc_vals[i+1] - Sdel_mid_vals[i+1]
    if diff_i * diff_next <= 0.0:
        # linear interpolation
        d_nm1 = dry_diameters_nm[i]
        d_nm2 = dry_diameters_nm[i+1]
        if abs(diff_i) < 1e-12:
            crossover_diameter_nm = d_nm1
        elif abs(diff_next) < 1e-12:
            crossover_diameter_nm = d_nm2
        else:
            # Solve for d where diff=0
            slope = (diff_next - diff_i) / (d_nm2 - d_nm1)
            d_cross = d_nm1 - diff_i / slope
            crossover_diameter_nm = round(d_cross, 3)
        break

if crossover_diameter_nm is None:
    # fallback: use midpoint of first zero crossing? This shouldn't happen
    crossover_diameter_nm = 0.0

# ---------- Build output ----------
output = {
    "dry_diameters_nm": dry_diameters_nm,
    "Sc_kohler_pct": Sc_kohler_pct,
    "Sdel_lower_pct": Sdel_lower_pct,
    "Sdel_upper_pct": Sdel_upper_pct,
    "gamma_w": gamma_w_del,
    "crossover_diameter_nm": crossover_diameter_nm
}

with open("/app/outputs/step_01_sc_sdel.json", "w") as f:
    json.dump(output, f)

print("step_01_sc_sdel.json written successfully.")
print(f"Crossover diameter: {crossover_diameter_nm} nm")
PYEOF
