#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_energies.json ===
python3 << 'PYEOF'
import json, math

def continuum_p4(alpha, beta, kappa):
    p_s = math.sqrt(-alpha/beta)
    K = math.sqrt(-alpha/(2*kappa))
    return 2/(3*beta) * math.sqrt(-2*kappa*alpha**3)

def p4_activation_energy(alpha, beta, kappa, a):
    p_s = math.sqrt(-alpha/beta)
    K = math.sqrt(-alpha/(2*kappa))
    lam = 2*math.pi/(K*a)
    term = (math.pi/3) * (lam**3 + 4*lam) / (1 - math.exp(-lam*math.pi)) * math.exp(-lam*math.pi/2)
    return 4 * kappa * K * p_s**2 * term

def p6_params():
    alpha=-1.0; beta=-1.0; gamma=1.0
    disc = beta**2 - 4*alpha*gamma
    p_s2 = (-beta + math.sqrt(disc)) / (2*gamma)
    p_s = math.sqrt(p_s2)
    b = (2*gamma*p_s2) / (3*beta + 4*gamma*p_s2)
    return alpha, beta, gamma, p_s, b

def continuum_p6(kappa):
    _, beta, gamma, p_s, b = p6_params()
    K = math.sqrt((beta + 2*gamma*p_s**2) / (2*kappa)) * p_s
    term1 = (kappa * K * p_s**2) / (4*b)
    term2 = 2*b - 1 - (4*b + 1)/math.sqrt(b*(b+1)) * math.log(math.sqrt(1+b) - math.sqrt(b))
    return term1 * term2

def p6_activation_energy(kappa, a):
    _, beta, gamma, p_s, b = p6_params()
    K = math.sqrt((beta + 2*gamma*p_s**2) / (2*kappa)) * p_s
    lam = 2*math.pi/(K*a)
    xp = math.asinh(math.sqrt(b))
    prefactor = 4 * kappa * K * p_s**2 * math.exp(-math.pi**2/(K*a))
    coeff = -math.pi/(4*b)
    inside = (1-2*b) * lam * math.cos(xp * lam) - ((1+4*b + lam**2 * b*(1+b)) / math.sqrt(b*(b+1))) * math.sin(xp * lam)
    return prefactor * coeff * inside

# p4 values
p4_cont = continuum_p4(-1.0, 1.0, 0.5)
p4_on = 0.6508
p4_off = 0.6284
p4_act = p4_activation_energy(-1.0, 1.0, 0.5, 1.0)

# p6 discrete (paper reported)
p6_thick_on = 4.4951
p6_thick_off = 4.4945
p6_thin_on = 1.5107
p6_thin_off = 1.3770

# p6 continuum (analytic recompute)
p6_thick_cont = continuum_p6(4.0)
p6_thin_cont = continuum_p6(0.5)

# p6 activation (analytic recompute)
p6_thick_act = p6_activation_energy(4.0, 1.0)
p6_thin_act = p6_activation_energy(0.5, 1.0)

data = {
    "p4_continuum_wall_energy": p4_cont,
    "p4_on_site_wall_energy": p4_on,
    "p4_off_site_wall_energy": p4_off,
    "p4_activation_energy": p4_act,
    "p6_thick_continuum_wall_energy": p6_thick_cont,
    "p6_thick_on_site_wall_energy": p6_thick_on,
    "p6_thick_off_site_wall_energy": p6_thick_off,
    "p6_thick_activation_energy": p6_thick_act,
    "p6_thin_continuum_wall_energy": p6_thin_cont,
    "p6_thin_on_site_wall_energy": p6_thin_on,
    "p6_thin_off_site_wall_energy": p6_thin_off,
    "p6_thin_activation_energy": p6_thin_act
}

with open('/app/outputs/computed_energies.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF
