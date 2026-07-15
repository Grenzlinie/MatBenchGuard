#!/usr/bin/env python3
import math
import csv
import os
import sys

# Physical constants (SI)
mu0 = 4e-7 * math.pi         # vacuum permeability, H/m
mu_e = 1.0                   # matrix relative permeability
mu_p = 1000.0                # particle relative permeability
M_s  = 1.7e6                 # saturation magnetization, A/m
R    = 1.25e-6               # particle radius, m
Vp   = (4.0/3.0) * math.pi * R**3   # particle volume, m^3
phi  = 0.11                  # particle volume fraction

beta  = (mu_p - mu_e) / (mu_p + 2.0*mu_e)
alpha = 3.0 * mu_e * mu0 * beta * Vp   # coefficient in linear limit
kappa = 3.0 * mu_e * beta / M_s        # saturation coefficient

DELTA_GAMMA = 1e-6           # finite-difference step for γ derivative
LMAX        = 200            # enough for max 2L = 200 (L up to 100)

def range_A1_A2(b):
    """integer (A1,A2) pairs for class A chains"""
    if b % 2 == 1:                      # odd b
        half = (b-1)//2
        return [(i,j) for i in range(-half, half+1) for j in range(-half, half+1)]
    else:                               # even b
        half = b//2 - 1
        return [(i,j) for i in range(-half, half+1) for j in range(-half, half+1)]

def range_B1_B2(b):
    """integer (B1,B2) pairs for class B chains, excludes zero"""
    if b % 2 == 1:
        half = (b-1)//2
        vals = list(range(-half, 0)) + list(range(1, half+1))
    else:
        half = b//2
        vals = list(range(-half, 0)) + list(range(1, half+1))
    return [(i,j) for i in vals for j in vals]

def precompute_contrib(b, gamma, max_A3):
    """Compute per-coordinate contribution of dipole sum g(x,y,z)
    for class A and class B. Returns two dicts keyed by (A1,A2,A3) or (B1,B2,B3)."""
    sin_g = math.sin(gamma)
    cos_g = math.cos(gamma)
    sqrt6   = math.sqrt(6.0)
    sqrt6_h = sqrt6 / 2.0
    contribA = {}
    # Class A
    for A1, A2 in range_A1_A2(b):
        for A3 in range(-max_A3, max_A3+1):
            x = sqrt6 * A1 * R + 2.0 * A3 * R * sin_g
            y = sqrt6 * A2 * R
            z = 2.0 * A3 * R * cos_g
            r2 = x*x + y*y + z*z
            if r2 == 0.0:
                continue
            r5 = r2 * r2 * math.sqrt(r2)
            g = (2.0*z*z - x*x - y*y) / (4.0 * math.pi * mu0 * r5)
            contribA[(A1,A2,A3)] = g
    # Class B
    contribB = {}
    for B1, B2 in range_B1_B2(b):
        for B3 in range(-max_A3, max_A3+1):
            x = sqrt6_h * (2.0*B1 - 1.0) * R + 2.0*(B3-1.0)*R*sin_g
            y = sqrt6_h * (2.0*B2 - 1.0) * R
            z = 2.0*(B3-1.0)*R*cos_g
            r2 = x*x + y*y + z*z
            if r2 == 0.0:
                continue
            r5 = r2 * r2 * math.sqrt(r2)
            g = (2.0*z*z - x*x - y*y) / (4.0 * math.pi * mu0 * r5)
            contribB[(B1,B2,B3)] = g
    return contribA, contribB

def get_A3_range(l):
    """A3 indices for a column of length l."""
    if l % 2 == 1:
        half = (l-1)//2
        return list(range(-half, half+1))
    else:
        half = l//2 - 1
        return list(range(-half, half+1))

def get_B3_range(l):
    """B3 indices for a column of length l, excludes the layer containing the origin."""
    if l % 2 == 1:
        half = (l-1)//2
        return list(range(-half, 0)) + list(range(1, half+1))
    else:
        half = l//2
        return list(range(-half, 0)) + list(range(1, half+1))

def compute_f_fplus(b, gamma):
    """Precompute the total local field factor f(l,b,γ) and f(l,b,γ+Δγ) for l=1..LMAX."""
    contribA_base, contribB_base = precompute_contrib(b, gamma,            LMAX)
    contribA_plus, contribB_plus = precompute_contrib(b, gamma+DELTA_GAMMA, LMAX)
    f_base = [0.0]*(LMAX+1)
    f_plus = [0.0]*(LMAX+1)
    for l in range(1, LMAX+1):
        sum_base = 0.0
        sum_plus = 0.0
        # class A
        a3_range = get_A3_range(l)
        for A1,A2 in range_A1_A2(b):
            for A3 in a3_range:
                key = (A1,A2,A3)
                sum_base += contribA_base.get(key, 0.0)
                sum_plus += contribA_plus.get(key, 0.0)
        # class B
        b3_range = get_B3_range(l)
        for B1,B2 in range_B1_B2(b):
            for B3 in b3_range:
                key = (B1,B2,B3)
                sum_base += contribB_base.get(key, 0.0)
                sum_plus += contribB_plus.get(key, 0.0)
        f_base[l] = sum_base
        f_plus[l] = sum_plus
    return f_base, f_plus

def solve_pz(l, b, f, H0):
    """Self-consistent solution for the z-component of the particle dipole moment."""
    if f == 0.0:
        return alpha * H0 / (1.0 + kappa * H0)
    a = kappa * f
    b_coeff = 1.0 + kappa * H0 - alpha * f
    c = -alpha * H0
    disc = b_coeff*b_coeff - 4.0*a*c
    if disc < 0.0:
        disc = 0.0
    sqrt_disc = math.sqrt(disc)
    p = (-b_coeff + sqrt_disc) / (2.0*a)
    if p < 0.0:
        p = (-b_coeff - sqrt_disc) / (2.0*a)
    return p

def compute_J(L, sigma, b, H0, f_arr):
    """Average polarization J in the field direction."""
    twol = 2*L
    sigma2 = sigma*sigma
    w = [0.0]*(twol+1)
    for l in range(1, twol+1):
        w[l] = math.exp(-(l-L)*(l-L)/(2.0*sigma2))
    S1 = sum(l*w[l] for l in range(1, twol+1))
    factor = phi / (Vp * (b*b + (b-1)*(b-1)))
    total = 0.0
    for l in range(1, twol+1):
        pz = solve_pz(l, b, f_arr[l], H0)
        n_l_l = b*b*l + (b-1)*(b-1)*(l-1)
        pl = n_l_l * pz
        total += pl * w[l]
    J = factor * total / S1
    return J

def compute_Delta_G(L, sigma, b, H0, gamma, f_base, f_plus):
    """Field-induced shear modulus ΔG (in Pa)."""
    J_base = compute_J(L, sigma, b, H0, f_base)
    J_plus = compute_J(L, sigma, b, H0, f_plus)
    dJ_dg = (J_plus - J_base) / DELTA_GAMMA
    chi_eff = J_base / (mu0 * H0)
    dchi_dg = dJ_dg / (mu0 * H0)
    tau = -0.5 * mu0 * (H0 / (1.0 + chi_eff))**2 * dchi_dg
    Delta_G = tau / gamma
    return Delta_G

def main():
    # -- Precompute f arrays for all (b,γ) combos that will be needed --
    b_vals     = [2,3,4,5,6,7]
    gamma_vals = [0.001, 0.003, 0.005]
    cache = {}
    for b in b_vals:
        for gamma in gamma_vals:
            print(f"Precomputing b={b}, gamma={gamma}", file=sys.stderr)
            f_base, f_plus = compute_f_fplus(b, gamma)
            cache[(b,gamma)] = (f_base, f_plus)

    rows = []
    # -----------------------------------
    # Series (a): L variation
    L_vals    = list(range(10,101,10))
    sigma_vals = [3,6,9]
    for L in L_vals:
        for sigma in sigma_vals:
            b = 2
            H0   = 1e6
            gamma = 0.003
            f_base, f_plus = cache[(b,gamma)]
            Delta_G = compute_Delta_G(L, sigma, b, H0, gamma, f_base, f_plus)
            Delta_G_MPa = Delta_G / 1e6
            H0_MA = 1.0
            cond_id = f"a_L{L}_s{sigma}"
            rows.append([cond_id, L, sigma, b, H0_MA, gamma, Delta_G_MPa])

    # -----------------------------------
    # Series (b): column width variation
    # (b) experimental pairs
    exp_pairs = [(10,2), (20,3), (30,4), (40,5)]
    for L,b in exp_pairs:
        sigma = 9
        H0   = 1e6
        gamma = 0.003
        if (b,gamma) not in cache:
            f_base, f_plus = compute_f_fplus(b,gamma)
            cache[(b,gamma)] = (f_base, f_plus)
        f_base, f_plus = cache[(b,gamma)]
        Delta_G = compute_Delta_G(L, sigma, b, H0, gamma, f_base, f_plus)
        Delta_G_MPa = Delta_G / 1e6
        H0_MA = 1.0
        cond_id = f"b_exp_L{L}_b{b}"
        rows.append([cond_id, L, sigma, b, H0_MA, gamma, Delta_G_MPa])
    # (b) continuous curve L=30, b=2..7
    L      = 30
    sigma  = 9
    H0     = 1e6
    gamma  = 0.003
    for b in range(2,8):
        f_base, f_plus = cache[(b,gamma)]
        Delta_G = compute_Delta_G(L, sigma, b, H0, gamma, f_base, f_plus)
        Delta_G_MPa = Delta_G / 1e6
        H0_MA = 1.0
        cond_id = f"b_cont_b{b}"
        rows.append([cond_id, L, sigma, b, H0_MA, gamma, Delta_G_MPa])

    # -----------------------------------
    # Series (c): H0 and γ variation
    H0_vals = [0.1e6,0.2e6,0.3e6,0.4e6,0.5e6,0.6e6,0.7e6,0.8e6,0.9e6,1.0e6]
    gamma_c_vals = [0.001, 0.003, 0.005]
    L     = 30
    sigma = 3
    b     = 2
    for H0 in H0_vals:
        for gamma in gamma_c_vals:
            f_base, f_plus = cache[(b,gamma)]
            Delta_G = compute_Delta_G(L, sigma, b, H0, gamma, f_base, f_plus)
            Delta_G_MPa = Delta_G / 1e6
            H0_MA = H0 / 1e6
            cond_id = f"c_H0_{H0_MA:.1f}_g{gamma}"
            rows.append([cond_id, L, sigma, b, H0_MA, gamma, Delta_G_MPa])

    # -----------------------------------
    # Write results.csv
    out_dir = "/app/outputs"
    os.makedirs(out_dir, exist_ok=True)
    outpath = os.path.join(out_dir, "results.csv")
    with open(outpath, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["condition_id","L","sigma","b","H0","gamma","Delta_G"])
        writer.writerows(rows)
    print(f"Written {len(rows)} rows to {outpath}", file=sys.stderr)

if __name__ == "__main__":
    main()