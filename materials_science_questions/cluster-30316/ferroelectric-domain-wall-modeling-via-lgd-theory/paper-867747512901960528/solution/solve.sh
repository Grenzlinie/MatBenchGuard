#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: scattering_parameters.json ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy
python3 - "$OUTDIR/scattering_parameters.json" << 'PYEOF'
import json, sys
import numpy as np
from scipy.integrate import solve_ivp

# parameters
kappa = 0.2
kappa_tilde = kappa / (1 + kappa)  # 0.1666667
s_v = kappa_tilde
s_u = 2.0 * kappa_tilde
L = 20.0  # large enough domain half-size

# wavenumber range – ensure 0.5 and 5.0 are exactly included
ks_base = np.linspace(0.1, 10.0, 200)
ks = np.sort(np.unique(np.concatenate([ks_base, [0.5, 5.0]])))  # exact points added

def compute_scattering(s, K):
    """Return transmission amplitude (complex), reflection amplitude (complex)
    for a unit incident wave from left."""
    if K == 0:
        return 1.0+0j, 0.0+0j
    # ODE: y1' = y2, y2' = -(c'/c)*y2 - (K**2/c)*y1
    def ode(z, y):
        # z is zeta
        sech2 = 1.0 / np.cosh(z)**2
        tanh = np.tanh(z)
        c = 1.0 - s * sech2
        if c <= 0:
            c = 1e-12
        cp = 2.0 * s * sech2 * tanh
        y1, y2 = y[0], y[1]
        dy1 = y2
        dy2 = -(cp/c)*y2 - (K**2/c)*y1
        return [dy1, dy2]
    
    # initial condition at +L: pure forward wave v = exp(i K z)
    y0 = [np.exp(1j*K*L), 1j*K*np.exp(1j*K*L)]
    
    # integrate backward from +L to -L
    sol = solve_ivp(ode, [L, -L], y0, method='RK45', rtol=1e-10, atol=1e-12,
                    vectorized=False, t_eval=None)
    if not sol.success:
        raise RuntimeError(f"Integration failed: {sol.message}")
    
    v_end = sol.y[0, -1]
    vp_end = sol.y[1, -1]
    
    # At -L, asymptotic form: a*exp(i K z) + b*exp(-i K z)
    z_neg = -L
    e_ikz = np.exp(1j*K*z_neg)  # sign: z=-L -> -i K L
    e_minus_ikz = np.exp(-1j*K*z_neg)
    # Solve for a and b
    # v = a e^{iKz} + b e^{-iKz}
    # v' = i K a e^{iKz} - i K b e^{-iKz}
    # a = (v + v'/(iK)) * e^{-iKz} / 2
    # b = (v - v'/(iK)) * e^{iKz} / 2
    a = (v_end + vp_end/(1j*K)) * np.exp(-1j*K*z_neg) / 2.0
    b = (v_end - vp_end/(1j*K)) * np.exp(1j*K*z_neg) / 2.0
    # transmitted amplitude for incident from left of unit amplitude: t = 1/a
    t = 1.0 / a
    r = b / a
    return t, r

# collect data
results = {'k_lambda': ks.tolist()}
keys = ['u_trans_amplitude', 'u_trans_phase', 'u_refl_amplitude', 'u_refl_phase',
        'v_trans_amplitude', 'v_trans_phase', 'v_refl_amplitude', 'v_refl_phase']
for k in keys:
    results[k] = []

for K in ks:
    # v component
    t_v, r_v = compute_scattering(s_v, K)
    # u component
    t_u, r_u = compute_scattering(s_u, K)
    
    results['u_trans_amplitude'].append(abs(t_u))
    results['u_trans_phase'].append(np.angle(t_u))
    results['u_refl_amplitude'].append(abs(r_u))
    results['u_refl_phase'].append(np.angle(r_u))
    results['v_trans_amplitude'].append(abs(t_v))
    results['v_trans_phase'].append(np.angle(t_v))
    results['v_refl_amplitude'].append(abs(r_v))
    results['v_refl_phase'].append(np.angle(r_v))

with open(sys.argv[1], 'w') as f:
    json.dump(results, f)
PYEOF

# === solve block: torque_force_values.csv ===
python3 /solution/generate_torque_force.py "$OUTDIR/torque_force_values.csv"

# === solve block: domain_wall_velocities.json ===
python3 /solution/generate_velocities.py "$OUTDIR/domain_wall_velocities.json"
