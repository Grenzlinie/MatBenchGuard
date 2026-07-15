#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_purdy_model.csv ===
# Write the Purdy-model dissipation curve using a Python numeric solver
python3 <<'PYEOF'
import math, csv

# --- Parameters from the paper (SI units, energies in J/mol) ---
C0_wt  = 2.4          # wt% Mn (nominal)
T      = 640 + 273.15 # K
R      = 8.314        # J/(mol·K)
Emn    = 8.0e3        # J/mol, interfacial binding energy
DeltaE = 1.5e3        # J/mol, half the chemical potential difference (2ΔE=3 kJ/mol)
delta  = 0.5e-9       # m, interface half-thickness
Dmn    = 8.3e-17      # m²/s, Mn diffusion coefficient in austenite

# Convert wt% to mole fraction (atomic) using atomic masses
M_Fe = 55.845
M_Mn = 54.938
C0_at = (C0_wt/M_Mn) / (C0_wt/M_Mn + (100-C0_wt)/M_Fe)

# Numerical domain
L = 5.0 * delta          # half-domain width (5δ is enough)
N = 4000                 # grid points
x = [-L + i*2*L/(N-1) for i in range(N)]
dx = 2*L/(N-1)

# Smooth binding-energy profile (Gaussian well) and its derivative
def E_and_dE(xx):
    # E = -Emn * exp(-(xx/delta)^2)
    arg = (xx/delta)**2
    E  = -Emn * math.exp(-arg)
    dE = 2*xx/(delta**2) * Emn * math.exp(-arg)
    return E, dE

# Produce log-spaced normalised velocities
nump = 40
V_min = 0.01
V_max = 100.0
logV = [math.log10(V_min) + (math.log10(V_max)-math.log10(V_min))*i/(nump-1) for i in range(nump)]
V_Mn_list = [10**lv for lv in logV]

results = []
for V in V_Mn_list:
    v = V * Dmn / delta          # physical velocity (m/s)
    # Solve ODE dC/dx = -(C/(R*T))*dE/dx - (v/Dmn)*(C - C0_at)
    # using simple forward Euler (RK4 not needed; steady state is robust)
    # initial condition at left boundary (x = -L) corresponds to far ferrite: C = C0_at
    C = [0.0]*N
    C[0] = C0_at
    for i in range(1, N):
        xi = x[i]
        Ei, dEi = E_and_dE(xi)
        # Explicit Euler step
        dC = -(C[i-1]/(R*T))*dEi - (v/Dmn)*(C[i-1] - C0_at)
        C[i] = C[i-1] + dC * dx
        # Clamp to physical range
        if C[i] < 0.0:
            C[i] = 0.0
        if C[i] > 1.0:
            C[i] = 1.0
    # Compute dissipation integral (1): ΔG_dis = -Nv*Vm * ∫ (C-C0) dE/dx dx
    # Nv*Vm = Avogadro's number N_A, giving J/mol
    N_A = 6.02214076e23
    integral = 0.0
    for i in range(N):
        xi = x[i]
        _, dEi = E_and_dE(xi)
        integral += (C[i] - C0_at) * dEi * dx
    DeltaG_J_per_mol = -N_A * integral   # J/mol
    DeltaG_kJ = DeltaG_J_per_mol / 1000.0  # kJ/mol
    # Sanity: dissipation should be positive
    if DeltaG_kJ < 0.0:
        DeltaG_kJ = 0.0
    results.append((V, DeltaG_kJ))

# Write CSV
with open('/app/outputs/step_01_purdy_model.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['V_Mn', 'Delta_G_dis'])
    for V, dG in results:
        writer.writerow([f'{V:.6f}', f'{dG:.6f}'])
PYEOF
