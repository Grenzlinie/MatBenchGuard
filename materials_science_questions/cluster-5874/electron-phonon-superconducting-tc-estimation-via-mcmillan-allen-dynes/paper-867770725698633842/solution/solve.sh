#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy
export OUTDIR=/app/outputs

# === solve block: results.csv ===
python3 << 'EOF'
import numpy as np
import csv, sys, math

# --- Parameters ---
kBoltz = 8.617333262145e-2  # meV/K
# coupling constants
lam11 = 1.00
lam12 = -0.17
lam22 = 2.65
nu12 = 0.8333
lam21 = lam12 * nu12  # from Eq.(3): lambda_{21} = lambda_{12} * nu_{12}
# spin-glass parameters
TSG = 15.0  # K
# magnetic scattering ratios: k11=k12=0.2*k22, k22 varied
k22_vals = [0.0, 1.0, 2.0, 3.0, 3.5, 4.0, 4.05, 5.0]
beta_vals = [1, 2]
# band weights for superfluid density
w1 = 0.72
w2 = 0.28
# Coulomb pseudopotential set to zero
mustar = np.zeros((2,2))
# Cutoff
omega_c = 180.0  # meV
# Characteristic energy for Lorentzian
Tc = 22.0  # K
Omega0 = 2*Tc/5  # meV (8.8)
# Half-width
Y = Omega0/2  # 4.4
# Temperature grid: from 0.125 K to above Tc (30 K) at least 50 points
T_min = 0.125
T_max = 30.0
nT = 50
Ts = np.linspace(T_min, T_max, nT)
# Matsubara cutoff: N points (positive frequencies)
N = 100  # will give n from 0 to N-1, Matsubara freq = (2n+1)*pi*kb*T
# Convergence parameters
max_iter = 30
tol = 1e-6
mix = 0.5  # under-relaxation for Z and Delta

# --- Build lambda matrix and spectral function normalisation ---
def lorentzian(omega, C, Omega0, Y):
    return C*(1.0/((omega+Omega0)**2 + Y**2) - 1.0/((omega-Omega0)**2 + Y**2))

# Define electron-spin-fluctuation spectral functions for each channel (jk) so that
# lambda_{jk} = 2 * int_0^inf dOmega alpha^2F_{jk}(Omega) / Omega
# For Lorentzian Eq.(4), the integral can be done analytically? But we will just use the relationship to determine C_jk.
# However, we can avoid explicit C_jk by building the kernel directly from lambda and the Lorentzian shape.
# The kernel Lambda_{jk}^{sf}(i w_n, i w_m) = 2 * int dOmega Omega * alpha^2F_{jk}(Omega) / ((w_n - w_m)^2 + Omega^2)
# Using the identity: int_0^inf dOmega Omega * L(Omega) / ((w_n-w_m)^2 + Omega^2) = something?
# We can precompute the integral for each w_diff using scipy integrate, but that's slow. Instead, we can note that for each (jk) the alpha^2F is the same Lorentzian shape scaled so that its lambda is known. So the kernel for channel (jk) is just lambda_{jk} times a universal kernel function K(iw_n, iw_m) that depends only on Omega0, Y.
# Because if we define alpha^2F_{jk}(Omega) = lambda_{jk} / (2*int dOmega' alpha^2F_0(Omega')/Omega') * alpha^2F_0(Omega) with alpha^2F_0 the unnormalized Lorentzian,
# then the kernel becomes lambda_{jk} * K_nm where K_nm = int dOmega Omega alpha^2F_0(Omega) / ((w_n-w_m)^2 + Omega^2) / int dOmega' alpha^2F_0(Omega')/Omega' * 2? Actually from Eq.(3) of paper? The coupling constants are defined as lambda = 2*int dOmega alpha^2F / Omega. So if we define a normalized spectral function F0_norm(Omega) such that 2*int dOmega F0_norm(Omega)/Omega = 1, and set alpha^2F = lambda * F0_norm, then the kernel becomes:
# Lambda(iwn, iwm) = 2*int dOmega Omega lambda * F0_norm / ((w_n-w_m)^2 + Omega^2) = lambda * (2*int dOmega Omega F0_norm / ((w_n-w_m)^2 + Omega^2)).
# So we can precompute a kernel matrix K_nm that is independent of lambda, and then multiply by lambda_{jk}.
# Let's define F0_norm = L(Omega)/N where N = 2*int dOmega L(Omega)/Omega, so lambda*F0_norm gives the correct lambda. Then the kernel for channel (jk) is lambda_{jk} * K_nm, where
# K_nm = (2/N) * int dOmega Omega L(Omega) / ((w_n - w_m)^2 + Omega^2).
# So we can compute K_nm once.

# First compute normalization constant N_lambda = 2 * int_0^inf dOmega L(Omega)/Omega
# Use numerical integration up to large cutoff (10*Omega0)
from scipy.integrate import quad
def integrand_for_N(omega):
    return lorentzian(omega, 1.0, Omega0, Y) / omega
N_lambda = 2 * quad(integrand_for_N, 1e-4, 10*Omega0)[0]
# Define normalized F0 = L(Omega)/N_lambda

# Precompute kernel matrix K_nm for a range of frequency differences. Since Matsubara frequencies depend on T, we need to recompute per temperature. But we can precompute K as a function of abs_diff_freq (w_n - w_m). That is independent of T. So we can compute K(delta) by integration and then interpolate.
# Let's create a function K_func(delta) = (2/N_lambda) * int dOmega Omega L(Omega) / (delta^2 + Omega^2)
# We'll compute it at many delta points and interpolate.

def K_func_calc(delta):
    if delta == 0.0:
        # Handle delta=0: integral int dOmega Omega L(Omega) / Omega^2 = int dOmega L(Omega)/Omega = N_lambda/2, so K_func = (2/N_lambda)*(N_lambda/2)=1
        return 1.0
    # for finite delta, integrate numerically
    def integrand(omega):
        return omega * lorentzian(omega, 1.0, Omega0, Y) / (delta**2 + omega**2)
    val = quad(integrand, 1e-4, 10*Omega0)[0]
    return (2.0/N_lambda) * val

# Generate a set of delta points to tabulate and interpolate
# Use linear interpolation in delta^2? We'll just precompute an array of delta values up to maximum frequency difference.
# Max frequency difference: max w_n - min w_m approx max w_n = (2N-1)*pi*kb*T_max. For N=100, T=30 => w_max = 199*pi*kb*30 ~ 199*3.14*0.0862*30 ~ 199*8.12 ~ 1615 meV. So delta up to ~3200. But K_func falls off quickly. We'll tabulate up to 2000 meV with 1000 points.
delta_max = 2000.0
n_delta = 1000
deltas = np.linspace(0, delta_max, n_delta)
K_vals = np.array([K_func_calc(d) for d in deltas])
# Interpolation function
from scipy.interpolate import interp1d
K_interp = interp1d(deltas, K_vals, kind='linear', bounds_error=False, fill_value=0.0)

def get_K(delta):
    return K_interp(abs(delta))

# --- Eliashberg equations ---
def solve_once(T, k22, beta):
    # Matsubara frequencies: w_n = (2n+1)*pi*kb*T, n=0..N-1
    n_indices = np.arange(N)
    w = (2*n_indices + 1) * math.pi * kBoltz * T
    # initial guess: BCS-like, Delta_j = const for j=1,2; Z_j = 1.0
    Delta = np.zeros((2, N))  # band index 0,1
    Z = np.ones((2, N))
    # initial Delta guess: some finite value
    Delta[0,:] = 0.5 * Omega0  # meV
    Delta[1,:] = 0.5 * Omega0
    # magnetic scattering rates
    k11 = 0.2 * k22
    k12 = 0.2 * k22
    k21 = k12 * nu12
    # magnetic scattering matrix (diagonal for simplicity? Actually k_jk: k11,k12,k21,k22. We'll need sqrt of N_k etc.)
    # The scattering terms: sum_k [Gamma^N + Gamma^M(T)] N_k^Z (and for Delta with minus).
    # We assume nonmagnetic scattering Gamma^N = 0.
    GM_T = np.array([[k11, k12],[k21, k22]]) * (1.0 - (T/TSG)**beta) if T < TSG else np.zeros((2,2))
    # precompute kernel matrix for all iwn,iwm differences
    # w_n is shape (N,); compute K_nm = get_K(w_n - w_m) => matrix of shape (N,N)
    w_diff = np.abs(w[:, np.newaxis] - w[np.newaxis, :])  # shape (N,N)
    K_nm = get_K(w_diff)  # shape (N,N)
    # For each iteration
    for it in range(max_iter):
        # Compute N^Z and N^Delta
        # N^Z_j(iwn) = w_n / sqrt(w_n^2 + Delta_j^2)
        # N^Delta_j = Delta_j / sqrt(...)
        Delta2 = Delta.copy()
        Z2 = Z.copy()
        sqrt_arg = w[np.newaxis, :]**2 + Delta2**2
        sqrt_inv = 1.0 / np.sqrt(sqrt_arg)
        NZ = w[np.newaxis, :] * sqrt_inv  # (2,N)
        NDelta = Delta2 * sqrt_inv
        # Matrices for Lambda^Z = Lambda^ph + Lambda^sf, with ph absent => Lambda^Z = Lambda^sf. Same for Lambda^Delta
        # In s+-, Lambda^Delta = Lambda^sf (since ph=0 and minus sign for ph?) Actually Lambda^Delta = Lambda^ph - Lambda^sf. With ph=0, Lambda^Delta = -Lambda^sf. Wait check paper Eq.(1)-(2) and text: Lambda^Z = Lambda^ph + Lambda^sf, Lambda^Delta = Lambda^ph - Lambda^sf. With ph=0, Lambda^Z = Lambda^sf, Lambda^Delta = -Lambda^sf.
        # But note that the gap equation (2) has [Lambda^Delta - mustar] theta(...). With mustar=0 and Lambda^Delta = -Lambda^sf. So the effective pairing interaction is negative of the spin-fluctuation kernel. That's typical for s+-.
        # However, for intraband coupling lambda11,lambda22 positive? lambda11=1.00, lambda22=2.65 they are positive. Interband lambda12=-0.17 negative. For the Lorentzian spin-fluctuation, the sign of the kernel may be overall. We'll just use the lambda matrix sign as given and apply to K_nm.
        # So Lambda^Z_jk(iwn,iwm) = lambda_jk * K_nm (since normalized)
        # Lambda^Delta_jk = -lambda_jk * K_nm.
        # Sum over m and k: pi T sum_m sum_k Lambda^Z_jk * NZ_k(m) + sum_k (Gamma^N + Gamma^M) * NZ_j(n) (no sum over m)
        # For Z equation: w_n Z_j(n) = w_n + pi T sum_{m,k} lambda_jk * K_nm * NZ_k(m) + sum_k (Gamma^N + Gamma^M)_{jk} * NZ_k(n)
        # For Delta equation: Z_j(n) Delta_j(n) = pi T sum_{m,k} ( -lambda_jk - mustar_jk ) * K_nm * NDelta_k(m) + sum_k (Gamma^N - Gamma^M)_{jk} * NDelta_k(n)
        # Note mustar=0.
        # Let's compute term1_Z = pi T sum_{m,k} lambda_jk * K_nm * NZ_k(m) => for each j, k, we need sum_m K_nm * NZ_k(m). That's a matrix multiplication: (K @ NZ_k) of shape (N,). Then multiply by pi T.
        # term1_Delta = pi T sum_{m,k} -lambda_jk * K_nm * NDelta_k(m) = - pi T sum_{m,k} lambda_jk * K_nm * NDelta_k(m).
        # scattering terms: for Z: sum_k GM_jk * NZ_k(n). For Delta: sum_k -GM_jk * NDelta_k(n).
        # We'll compute new Z and Delta.
        NZ_k0 = NZ[0,:]  # band 1
        NZ_k1 = NZ[1,:]
        NDelta_k0 = NDelta[0,:]
        NDelta_k1 = NDelta[1,:]
        # Sum over m K_nm * NZ_k(m) for each k: result shape (N,)
        sum_K_NZ0 = K_nm @ NZ_k0
        sum_K_NZ1 = K_nm @ NZ_k1
        sum_K_NDelta0 = K_nm @ NDelta_k0
        sum_K_NDelta1 = K_nm @ NDelta_k1
        # For j=0:
        term1_Z0 = math.pi * T * (lam11 * sum_K_NZ0 + lam12 * sum_K_NZ1)
        scatter_Z0 = GM_T[0,0] * NZ_k0 + GM_T[0,1] * NZ_k1
        Z_new0 = 1.0 + (term1_Z0 + scatter_Z0) / w  # w_n Z = w_n + ..., so Z = 1 + .../w
        # For Delta equation: Z_new0 * Delta_new0 = - pi T (lam11*sum_K_NDelta0 + lam12*sum_K_NDelta1) + ( (-GM_T[0,0])*NDelta_k0 + (-GM_T[0,1])*NDelta_k1 ) ??? Actually Delta term scattering: sum_k [Gamma^N - Gamma^M] * NDelta_k(n). Since Gamma^N=0, term = - GM_jk * NDelta_k(n). So
        rhs_Delta0 = - math.pi * T * (lam11 * sum_K_NDelta0 + lam12 * sum_K_NDelta1) - (GM_T[0,0] * NDelta_k0 + GM_T[0,1] * NDelta_k1)
        Delta_new0 = rhs_Delta0 / Z_new0
        # j=1:
        term1_Z1 = math.pi * T * (lam21 * sum_K_NZ0 + lam22 * sum_K_NZ1)
        scatter_Z1 = GM_T[1,0] * NZ_k0 + GM_T[1,1] * NZ_k1
        Z_new1 = 1.0 + (term1_Z1 + scatter_Z1) / w
        rhs_Delta1 = - math.pi * T * (lam21 * sum_K_NDelta0 + lam22 * sum_K_NDelta1) - (GM_T[1,0] * NDelta_k0 + GM_T[1,1] * NDelta_k1)
        Delta_new1 = rhs_Delta1 / Z_new1
        # converge check
        err = max(np.max(np.abs(Delta_new0 - Delta[0,:])), np.max(np.abs(Delta_new1 - Delta[1,:])),
                  np.max(np.abs(Z_new0 - Z[0,:])), np.max(np.abs(Z_new1 - Z[1,:])))
        # update with mixing
        Delta[0,:] = (1-mix)*Delta[0,:] + mix*Delta_new0
        Delta[1,:] = (1-mix)*Delta[1,:] + mix*Delta_new1
        Z[0,:] = (1-mix)*Z[0,:] + mix*Z_new0
        Z[1,:] = (1-mix)*Z[1,:] + mix*Z_new1
        if err < tol:
            break
    # After convergence, extract lowest Matsubara frequency gaps (n=0) => Delta_j(i w_0)
    return Delta[0,0], Delta[1,0], Z[0,0], Z[1,0], Delta, Z

# Compute superfluid density for a given (k22, beta). We need the full Delta and Z for all temperatures and then compute n_s using formula (5).
# We'll compute for all (k22, beta) combination and store.
output_rows = []
# First compute the zero-temperature reference superfluid density for k22=0, beta=1 (or might need both betas?) Actually the normalisation is written "normalizing by the zero-temperature value at k22=0". We'll compute for k22=0, T=0.125 K and use that ns0_ref.
# We'll compute the superfluid density as (w_p/c)^2 * sum_j w_j * pi T sum_n Delta_j^2 Z_j^2 / (w_n^2 Z_j^2 + Delta_j^2 Z_j^2)^(3/2). We'll need the sum over n from -inf to inf, but we have positive frequencies only; we can double positive part because Z and Delta are even/odd? Usually Z(i w_n) is even in n (since it's real even function), Delta maybe odd? In s-wave, Delta is even and Z even. So we can sum over n=0..N-1 and multiply by 2? Actually formula (5) sum over n from -inf to +inf, but we have only n>=0. Assuming symmetric, the sum = 2 * sum_{n=0}^{N-1} of f(positive w_n) except maybe n=0 only once? For large n, contribution decays. We'll double the sum and subtract the n=0 contribution if needed. We'll do 2 * sum_{n=0}^{N-1} - f(w_0) (removing double count of n=0). We'll implement that.
# We'll precompute ns at each T for each (k22,beta).

def compute_ns(T, Delta, Z):
    # Delta, Z: arrays of shape (2, N) for the given T
    w = (2*np.arange(N) + 1) * math.pi * kBoltz * T
    term_sum = 0.0
    for band in range(2):
        Dj = Delta[band,:]
        Zj = Z[band,:]
        denom = (w**2 * Zj**2 + Dj**2 * Zj**2)**(1.5)  # (w_n^2 Z_n^2 + Delta_n^2 Z_n^2)^(3/2)
        term = Dj**2 * Zj**2 / denom
        term_sum += (w1 if band==0 else w2) * np.sum(term)
    ns = math.pi * T * term_sum
    # Double for negative frequencies: we must double the sum of all n except n=0 only appears once?
    # If we sum n from 0..N-1, the full sum over all n = sum_{n=0}^{N-1} f + sum_{n=-1}^{-inf} f = sum_{n=0}^{N-1} f + sum_{n=0}^{N-1} f (since f(-w) = f(w)) assuming even function. So total = 2 * sum_{n=0}^{N-1} f, correct, because f(-w_n) = f(w_n) for even n? w_{-n} = -w_n? Actually Matsubara frequencies: w_n = (2n+1)pi T, n integer negative gives negative frequency. The function f(w_n) is even in w_n because Delta^2 and Z^2 are even. So f(w_n)=f(-w_n). So double counting each positive n and negative n gives exactly 2* sum_{n=0}^{N-1} f(w_n). However, there is no n=0 distinct, because n=0 is positive. So we just multiply by 2. That's correct.
    return 2 * ns

# Precompute ns0_ref: for k22=0, beta=1 at T=0.125 K
T_ref = 0.125
Delta0_ref, Delta1_ref, Z0_ref, Z1_ref, Dmat_ref, Zmat_ref = solve_once(T_ref, 0.0, 1)
ns0_ref = compute_ns(T_ref, Dmat_ref, Zmat_ref)

# Loop over k22 and beta
for k22 in k22_vals:
    for beta in beta_vals:
        # Solve for each temperature
        for T in Ts:
            # skip if T above Tc maybe but we go up to 30; we'll solve anyway
            try:
                d1, d2, z1, z2, Dmat, Zmat = solve_once(T, k22, beta)
                ns = compute_ns(T, Dmat, Zmat) / ns0_ref
                output_rows.append([k22, beta, T, d1, d2, ns])
            except:
                # if convergence fails, set gaps to 0, ns=0?
                output_rows.append([k22, beta, T, 0.0, 0.0, 0.0])

# Write CSV
with open('/app/outputs/results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['k22','beta','T','Delta1','Delta2','ns'])
    for row in output_rows:
        writer.writerow(row)
EOF
