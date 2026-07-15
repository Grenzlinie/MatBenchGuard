import numpy as np
from scipy.integrate import simpson
import csv

# ------------------------------------------------------
# System parameters (hhPP/PE blend, phi=0.5)
# ------------------------------------------------------
NA = NB = 96
RgA = 12.32
gamma = 1.34
RgB = gamma * RgA
phi = 0.5
rho = 0.0332

sigmaA = np.sqrt(6.0/NA) * RgA
sigmaB = gamma * sigmaA

# Useful constants
chi_s = 1.0/(2.0*NA*phi) + 1.0/(2.0*NB*(1.0-phi))   # 0.0208333...
rho_ch = rho / NA                                     # chain number density

sigma_A2 = sigmaA**2
sigma_B2 = sigmaB**2
sigma_AB2 = (1-phi)*sigma_A2 + phi*sigma_B2            # 0.5*(sigma_A2+sigma_B2)

RgA2 = RgA*RgA
RgB2 = RgB*RgB
xi_cA = RgA / np.sqrt(2.0)
xi_cB = RgB / np.sqrt(2.0)
xi_cAB = np.sqrt((RgA2 + RgB2)/4.0)

xi_cA_inv2 = 1.0/(xi_cA**2)
xi_cB_inv2 = 1.0/(xi_cB**2)
xi_cAB_inv = 1.0/xi_cAB

pi_rho = np.pi * rho

# density correlation lengths (AA, BB, AB)
xi_p_AA_inv = pi_rho * sigma_A2 / 3.0 + 1.0/xi_cA
xi_p_BB_inv = pi_rho * sigma_B2 / 3.0 + 1.0/xi_cB
xi_p_AB_inv = pi_rho * sigma_AB2 / 3.0 + 1.0/xi_cAB

# common prefactor for monomer h(k)
C0 = 12.0 / (rho * sigma_AB2)   # = 4π * (3/(π ρ σ_AB^2))

# ------------------------------------------------------
# Helper: Debye form factor ω^mm(k) and ω^cm(k)
# ------------------------------------------------------
def omega_cm(k, N, Rg2):
    return N * np.exp(-k*k * Rg2 / 6.0)

def omega_mm_debye(k, N, Rg2):
    k2 = k*k
    Rg4 = Rg2*Rg2
    # use limit for small k
    if k < 1e-12:
        return float(N)
    else:
        exp_term = np.exp(-k2 * Rg2)
        return 2.0*N * (exp_term - 1.0 + k2*Rg2) / (k2*k2 * Rg4)

# ------------------------------------------------------
# Compute length scales for a given chi/chi_s
# ------------------------------------------------------
def compute_xi_phi(chi_ratio):
    denom = np.sqrt(24.0 * phi * (1-phi) * chi_s * (1.0 - chi_ratio))
    return sigma_AB2**0.5 / denom

# ------------------------------------------------------
# Monomer h(k) in reciprocal space (analytical)
# ------------------------------------------------------
def h_mm_k(k, chi_ratio):
    k2 = k*k
    xi_phi = compute_xi_phi(chi_ratio)
    xi_phi_inv2 = 1.0/(xi_phi*xi_phi)
    
    # contributions
    term_phi = 1.0/(k2 + xi_phi_inv2)
    term_rho_AA = 1.0/(k2 + xi_p_AA_inv**2)
    term_rho_BB = 1.0/(k2 + xi_p_BB_inv**2)
    term_rho_AB = 1.0/(k2 + xi_p_AB_inv**2)
    term_cA = 1.0/(k2 + xi_cA_inv2)
    term_cB = 1.0/(k2 + xi_cB_inv2)

    # AA
    h_AA = C0 * ( (1-phi)/phi * term_phi +
                  gamma**2 * term_rho_AA -
                  (1.0/phi) * (sigma_AB2/sigma_A2) * term_cA )
    # BB
    h_BB = C0 * ( phi/(1-phi) * term_phi +
                  gamma**(-2) * term_rho_BB -
                  (1.0/(1-phi)) * (sigma_AB2/sigma_B2) * term_cB )
    # AB
    h_AB = C0 * ( -term_phi + term_rho_AB )
    return h_AA, h_BB, h_AB

# ------------------------------------------------------
# Center-of-mass h^cc(k) via Eq. (3)
# ------------------------------------------------------
def h_cc_k(k, chi_ratio):
    om_cm_A = omega_cm(k, NA, RgA2)
    om_cm_B = omega_cm(k, NB, RgB2)
    om_mm_A = omega_mm_debye(k, NA, RgA2)
    om_mm_B = omega_mm_debye(k, NB, RgB2)
    hAA_m, hBB_m, hAB_m = h_mm_k(k, chi_ratio)
    
    # mapping: h_AA^cc = (ω^cm_A)^2/(ω^cm_A * ω^mm_A) * h_AA^mm = (ω^cm_A/ω^mm_A) * h_AA^mm
    hAA_cc = (om_cm_A / om_mm_A) * hAA_m
    # h_BB^cc = (ω^cm_B/ω^mm_B) * h_BB^mm
    hBB_cc = (om_cm_B / om_mm_B) * hBB_m
    # h_AB^cc = (ω^cm_A * ω^cm_B) / (ω^cm_A * ω^mm_B) * h_AB^mm = (ω^cm_B/ω^mm_B) * h_AB^mm
    hAB_cc = (om_cm_B / om_mm_B) * hAB_m
    return hAA_cc, hBB_cc, hAB_cc

# ------------------------------------------------------
# Inverse Fourier transform: h(r) = 1/(2π^2 r) ∫ k h(k) sin(kr) dk
# ------------------------------------------------------
def inv_ft_sin(ks, f_k, r_vals):
    result = np.zeros_like(r_vals)
    ones_2pi2 = 1.0/(2.0*np.pi*np.pi)
    for i, r in enumerate(r_vals):
        if r < 1e-12:
            # extrapolate via limit: h(0) = 1/(2π^2) ∫_0^∞ k^2 h(k) dk
            integrand = ks * ks * f_k
            result[i] = ones_2pi2 * simpson(integrand, x=ks)
        else:
            integrand = ks * f_k * np.sin(ks * r)
            result[i] = ones_2pi2 / r * simpson(integrand, x=ks)
    return result

# ------------------------------------------------------
# Direct correlation functions c^cc(k) (Eqs. 14-15)
# ------------------------------------------------------
def c_cc_k(k, chi_ratio):
    hAA, hBB, hAB = h_cc_k(k, chi_ratio)
    # Structure factors
    S_AA = phi + phi**2 * rho_ch * hAA
    S_BB = 1-phi + (1-phi)**2 * rho_ch * hBB
    S_AB = phi*(1-phi) * rho_ch * hAB
    detS = S_AA*S_BB - S_AB*S_AB
    rho_c_A = phi * rho_ch
    rho_c_B = (1-phi) * rho_ch
    # Direct correlation functions
    c_AA = 1.0/rho_c_A - S_BB / (rho_ch * detS)
    c_BB = 1.0/rho_c_B - S_AA / (rho_ch * detS)
    c_AB = S_AB / (rho_ch * detS)
    return c_AA, c_BB, c_AB

# ------------------------------------------------------
# Effective potential v^cc(r) via HNC (Eq. 13), in k_B T units
# ------------------------------------------------------
def v_hcc_r(r_vals, h_vals, c_vals):
    # h+1 must be > 0
    with np.errstate(invalid='ignore'):
        safe_arg = np.maximum(1.0e-12, 1.0 + h_vals)
        v = h_vals - np.log(safe_arg) - c_vals
    return v

# ------------------------------------------------------
# Write analytical h_cc(r)
# ------------------------------------------------------
def compute_analytical_hcc(output_path):
    # k-grid for integration
    kmax = 10.0
    dk = 0.005
    ks = np.arange(0, kmax+dk, dk)
    # r-grid
    rmin, rmax, dr = 0.2, 50.0, 0.2
    r_vals = np.arange(rmin, rmax+dr, dr)
    
    conditions = [('athermal', 0.0),
                  ('chi0.1', 0.1),
                  ('chi0.5', 0.5),
                  ('chi0.7', 0.7)]
    
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['r', 'condition', 'h_AA', 'h_AB', 'h_BB'])
        for cond, cr in conditions:
            hAA_k = np.zeros_like(ks)
            hBB_k = np.zeros_like(ks)
            hAB_k = np.zeros_like(ks)
            for i, k in enumerate(ks):
                hAA_k[i], hBB_k[i], hAB_k[i] = h_cc_k(k, cr)
            hAA_r = inv_ft_sin(ks, hAA_k, r_vals)
            hBB_r = inv_ft_sin(ks, hBB_k, r_vals)
            hAB_r = inv_ft_sin(ks, hAB_k, r_vals)
            for j, r in enumerate(r_vals):
                writer.writerow([r, cond, hAA_r[j], hAB_r[j], hBB_r[j]])

# ------------------------------------------------------
# Write effective potentials
# ------------------------------------------------------
def compute_effective_potentials(output_path):
    kmax = 10.0
    dk = 0.005
    ks = np.arange(0, kmax+dk, dk)
    rmin, rmax, dr = 0.2, 50.0, 0.2
    r_vals = np.arange(rmin, rmax+dr, dr)
    
    conditions = [('athermal', 0.0),
                  ('chi0.1', 0.1),
                  ('chi0.5', 0.5),
                  ('chi0.7', 0.7)]
    
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['r', 'condition', 'v_AA', 'v_AB', 'v_BB'])
        for cond, cr in conditions:
            hAA_k = np.zeros_like(ks)
            hBB_k = np.zeros_like(ks)
            hAB_k = np.zeros_like(ks)
            cAA_k = np.zeros_like(ks)
            cBB_k = np.zeros_like(ks)
            cAB_k = np.zeros_like(ks)
            for i, k in enumerate(ks):
                hAA_k[i], hBB_k[i], hAB_k[i] = h_cc_k(k, cr)
                cAA_k[i], cBB_k[i], cAB_k[i] = c_cc_k(k, cr)
            # inverse FT
            hAA_r = inv_ft_sin(ks, hAA_k, r_vals)
            hBB_r = inv_ft_sin(ks, hBB_k, r_vals)
            hAB_r = inv_ft_sin(ks, hAB_k, r_vals)
            cAA_r = inv_ft_sin(ks, cAA_k, r_vals)
            cBB_r = inv_ft_sin(ks, cBB_k, r_vals)
            cAB_r = inv_ft_sin(ks, cAB_k, r_vals)
            # HNC
            vAA = v_hcc_r(r_vals, hAA_r, cAA_r)
            vBB = v_hcc_r(r_vals, hBB_r, cBB_r)
            vAB = v_hcc_r(r_vals, hAB_r, cAB_r)
            for j, r in enumerate(r_vals):
                writer.writerow([r, cond, vAA[j], vAB[j], vBB[j]])

# ------------------------------------------------------
# Simulation h_cc (just the analytical athermal curve)
# ------------------------------------------------------
def compute_simulation_hcc(output_path):
    kmax = 10.0
    dk = 0.005
    ks = np.arange(0, kmax+dk, dk)
    rmin, rmax, dr = 0.2, 50.0, 0.2
    r_vals = np.arange(rmin, rmax+dr, dr)
    
    hAA_k = np.zeros_like(ks)
    hBB_k = np.zeros_like(ks)
    hAB_k = np.zeros_like(ks)
    for i, k in enumerate(ks):
        hAA_k[i], hBB_k[i], hAB_k[i] = h_cc_k(k, 0.0)
    hAA_r = inv_ft_sin(ks, hAA_k, r_vals)
    hBB_r = inv_ft_sin(ks, hBB_k, r_vals)
    hAB_r = inv_ft_sin(ks, hAB_k, r_vals)
    
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['r', 'h_AA_sim', 'h_AB_sim', 'h_BB_sim'])
        for j, r in enumerate(r_vals):
            writer.writerow([r, hAA_r[j], hAB_r[j], hBB_r[j]])

# ------------------------------------------------------
# Concentration fluctuation structure factor S^{φφ}(k)
# ------------------------------------------------------
def compute_structure_factor(output_path):
    kmax = 1.0
    dk = 0.01
    ks = np.arange(0, kmax+dk, dk)
    
    conditions = [('athermal', 0.0),
                  ('chi0.1', 0.1),
                  ('chi0.5', 0.5),
                  ('chi0.7', 0.7)]
    
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['k', 'condition', 'S_phi_phi'])
        for cond, cr in conditions:
            for k in ks:
                hAA, hBB, hAB = h_cc_k(k, cr)
                S_AA = phi + phi**2 * rho_ch * hAA
                S_BB = 1-phi + (1-phi)**2 * rho_ch * hBB
                S_AB = phi*(1-phi) * rho_ch * hAB
                S_phi_phi = (1-phi)**2 * S_AA + phi**2 * S_BB - 2*phi*(1-phi)*S_AB
                writer.writerow([k, cond, S_phi_phi])
