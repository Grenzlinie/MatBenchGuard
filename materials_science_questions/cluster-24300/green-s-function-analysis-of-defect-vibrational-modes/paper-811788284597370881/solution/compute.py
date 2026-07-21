#!/usr/bin/env python3
import json
import numpy as np
import scipy.integrate as integrate

def rho(w):
    if w <= 0.0 or w >= 1.0:
        return 0.0
    return (32.0 / np.pi) * (w ** 4) * np.sqrt(1.0 - w ** 2)

def ImG(w):
    if w <= 0.0:
        return 0.0
    return 0.5 * np.pi * rho(w) / w

def ReG(w):
    return -2.0 - 8.0 * w ** 2 + 16.0 * w ** 4

def G(w):
    return ReG(w) + 1j * ImG(w)

def n_bose(w, T):
    if T == 0.0:
        return 0.0
    if w == 0.0:
        return 0.0
    return 1.0 / (np.exp(w / T) - 1.0)

def D_func(w, T):
    return ReG(w) + 2j * n_bose(w, T) * ImG(w)

def D_tilde(w, b, T):
    D = D_func(w, T)
    return D / (1.0 - b * D)

def S_L_abs_integrand(w, b, T):
    if w == 0.0:
        return 0.0
    Dt = D_tilde(w, b, T)
    return np.imag(Dt) / (w ** 2)

def S_L_lum_integrand(w, b, T):
    if w == 0.0:
        return 0.0
    Dt = D_tilde(w, b, T)
    factor = np.abs(1.0 - b * G(w)) ** 2
    return np.imag(Dt * factor) / (w ** 2)

def gamma_delta_Q_integrand(w, b, T):
    D = D_func(w, T)
    return np.log(1.0 - b * D)

b_vals = [-0.2, 0.0, 0.16]
T_vals = [0.0, 0.1, 0.5]
results = []
eps = 1e-12

for b in b_vals:
    for T in T_vals:
        D0 = D_func(0.0, T)
        Dt0 = D0 / (1.0 - b * D0)
        delta_L = np.real(Dt0) / (2.0 * np.pi)

        S_abs, _ = integrate.quad(S_L_abs_integrand, eps, 1.0, args=(b, T), limit=200)
        S_abs /= np.pi

        S_lum, _ = integrate.quad(S_L_lum_integrand, eps, 1.0, args=(b, T), limit=200)
        S_lum /= np.pi

        def integrand_real(w, b, T):
            return np.real(gamma_delta_Q_integrand(w, b, T))

        def integrand_imag(w, b, T):
            return np.imag(gamma_delta_Q_integrand(w, b, T))

        gamma_real, _ = integrate.quad(integrand_real, 0.0, 1.0, args=(b, T), limit=200)
        gamma_imag, _ = integrate.quad(integrand_imag, 0.0, 1.0, args=(b, T), limit=200)
        gamma_val = gamma_real / (2.0 * np.pi)
        delta_Q_val = -gamma_imag / (2.0 * np.pi)

        results.append({
            "b": b,
            "T": T,
            "delta_L": float(delta_L),
            "S_L_absorption": float(S_abs),
            "S_L_luminescence": float(S_lum),
            "gamma": float(gamma_val),
            "delta_Q": float(delta_Q_val)
        })

output = {
    "b_values": [-0.2, 0.0, 0.16],
    "T_values": [0.0, 0.1, 0.5],
    "results": results
}

with open("/app/outputs/zpl_quantities.json", "w") as f:
    json.dump(output, f, indent=2)
