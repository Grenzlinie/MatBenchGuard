#!/usr/bin/env python3
import sys
import math

def compute_intensity(N):
    # Physical constants (SI)
    k_B = 1.380649e-23      # J/K
    h_bar = 1.054571817e-34 # J*s
    v_s = 5000.0            # m/s
    c_vac = 2.99792458e8    # m/s
    T = 6.0                 # K
    a = 1e-8                # 100 Å = 1e-8 m
    
    def raw_intensity(Delta_nu_cm1):
        """Unnormalised intensity I_raw for Raman shift Delta_nu_cm1 (cm^-1)."""
        if Delta_nu_cm1 == 0.0:
            # Limit ω→0: I ∝ (k_B T)/(ħ v_s^2), sin, N terms → 1
            I0 = k_B * T / (h_bar * v_s**2)
            return I0
        # frequency in Hz: ν = c * (Δν in m^-1) = c * (Δν_cm1 * 100)
        nu = c_vac * Delta_nu_cm1 * 100.0
        omega = 2.0 * math.pi * nu
        q_z = omega / v_s
        # sinc term: sin(a q_z/2)/(a q_z/2)
        x = a * q_z / 2.0
        if abs(x) < 1e-12:
            sinc = 1.0
        else:
            sinc = math.sin(x) / x
        # N-dependent factor: 4N² / (4N² - (a q_z/π)²)
        denom = 4.0 * N**2 - (a * q_z / math.pi)**2
        # avoid division by zero (though not hit at integer cm⁻¹)
        if abs(denom) < 1e-30:
            N_factor = float('inf')
        else:
            N_factor = (4.0 * N**2) / denom
        # |M|² ∝ (q_z/√ω)² = q_z²/ω = ω/v_s²
        M_sq = (omega / v_s**2) * (sinc**2) * (N_factor**2)
        # Bose factor
        if omega <= 0.0:
            return 0.0
        nb = 1.0 / (math.exp(h_bar * omega / (k_B * T)) - 1.0)
        return M_sq * nb

    shifts = list(range(0, 51))
    raw = [raw_intensity(s) for s in shifts]
    max_raw = max(raw)
    normalized = [r / max_raw for r in raw]
    return shifts, normalized

def write_csv(N, shifts, intensities, path):
    with open(path, 'w') as f:
        f.write("Raman_shift_cm1,Intensity_arb_units\n")
        for s, v in zip(shifts, intensities):
            f.write(f"{s},{v:.12e}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: helper.py <N> <output.csv>")
    N = int(sys.argv[1])
    outfile = sys.argv[2]
    shifts, intensities = compute_intensity(N)
    write_csv(N, shifts, intensities, outfile)
