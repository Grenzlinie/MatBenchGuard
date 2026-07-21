import numpy as np
from scipy.optimize import minimize

# Bain strain parameters
alpha = 1.0619
beta  = 0.9178
gamma = 1.0231

# Right stretch tensors
U1 = np.array([[(alpha+gamma)/2, (alpha-gamma)/2, 0],
               [(alpha-gamma)/2, (alpha+gamma)/2, 0],
               [0, 0, beta]])
U2 = np.array([[(alpha+gamma)/2, (gamma-alpha)/2, 0],
               [(gamma-alpha)/2, (alpha+gamma)/2, 0],
               [0, 0, beta]])

# Rotation Q
Q = np.array([[2*alpha*gamma/(alpha**2+gamma**2), -(alpha**2-gamma**2)/(alpha**2+gamma**2), 0],
              [(alpha**2-gamma**2)/(alpha**2+gamma**2), 2*alpha*gamma/(alpha**2+gamma**2), 0],
              [0, 0, 1.0]])

F1B = Q @ U1   # Bain deformation gradient phase 1
F2B = U2       # Bain deformation gradient phase 2

p = 0.5

# Neo-Hookean material parameters (compressible, arbitrary positive values)
mu = 1.0
lam = 1.0

def neoHook(Fe):
    C = Fe.T @ Fe
    J = np.linalg.det(Fe)
    I1 = np.trace(C)
    return 0.5 * mu * (I1 - 3) - mu * np.log(J) + 0.5 * lam * (np.log(J))**2

def energy_Voigt(F_flat):
    F = F_flat.reshape((3,3))
    Fe1 = F @ np.linalg.inv(F1B)
    Fe2 = F @ np.linalg.inv(F2B)
    e1 = neoHook(Fe1)
    e2 = neoHook(Fe2)
    return (1-p)*e1 + p*e2

def energy_Reuss(x):
    F = x[:9].reshape((3,3))
    DF = x[9:].reshape((3,3))
    F1 = F - p * DF
    F2 = F + (1-p) * DF
    Fe1 = F1 @ np.linalg.inv(F1B)
    Fe2 = F2 @ np.linalg.inv(F2B)
    e1 = neoHook(Fe1)
    e2 = neoHook(Fe2)
    return (1-p)*e1 + p*e2

def energy_PR(x, N):
    F = x[:9].reshape((3,3))
    a = x[9:]
    aN = np.outer(a, N)
    F1 = F - p * aN
    F2 = F + (1-p) * aN
    Fe1 = F1 @ np.linalg.inv(F1B)
    Fe2 = F2 @ np.linalg.inv(F2B)
    e1 = neoHook(Fe1)
    e2 = neoHook(Fe2)
    return (1-p)*e1 + p*e2

# Minimize Voigt/Taylor energy (independent of N)
n_restarts = 5
best_EV = np.inf
for _ in range(n_restarts):
    x0 = np.eye(3).flatten() + 0.1*np.random.randn(9)
    res = minimize(energy_Voigt, x0, method='L-BFGS-B')
    if res.fun < best_EV:
        best_EV = res.fun

# Minimize Reuss/Sachs energy (independent of N)
best_ER = np.inf
for _ in range(n_restarts):
    x0 = np.random.randn(18)*0.1
    res = minimize(energy_Reuss, x0, method='L-BFGS-B')
    if res.fun < best_ER:
        best_ER = res.fun

print("Voigt/Taylor energy:", best_EV)
print("Reuss/Sachs energy:", best_ER)

# Grid of orientations covering the coherent directions N = (1,0,0), (0,1,0), etc.
theta_vals = [0, np.pi/4, np.pi/2, np.pi/2, np.pi/2, np.pi/2, np.pi/2, 3*np.pi/4, np.pi]
phi_vals   = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4]

# Ensure exact coherent orientations are included
coherent = [(np.pi/2, 0), (np.pi/2, np.pi/2), (np.pi/2, np.pi), (np.pi/2, 3*np.pi/2)]

rows = []
for th in theta_vals:
    for ph in phi_vals:
        rows.append((th, ph))
# Add any missing coherent ones
for (th, ph) in coherent:
    if (th, ph) not in rows:
        rows.append((th, ph))

energies = []
for th, ph in rows:
    N = np.array([np.sin(th)*np.cos(ph), np.sin(th)*np.sin(ph), np.cos(th)])
    # partial rank-one minimization
    best_EPR = np.inf
    for _ in range(n_restarts):
        x0 = np.zeros(12)
        x0[:9] = np.eye(3).flatten() + 0.1*np.random.randn(9)
        x0[9:] = np.random.randn(3)*0.1
        res = minimize(lambda x: energy_PR(x, N), x0, method='L-BFGS-B')
        if res.fun < best_EPR:
            best_EPR = res.fun
    energies.append((th, ph, best_EV, best_ER, best_EPR))

# Write CSV (columns: theta, phi, energy_VoigtTaylor, energy_ReussSachs, energy_PartialRankOne)
import csv
with open('/app/outputs/orientation_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['theta', 'phi', 'energy_VoigtTaylor', 'energy_ReussSachs', 'energy_PartialRankOne'])
    for th, ph, EV, ER, EPR in energies:
        writer.writerow([th, ph, EV, ER, EPR])

print("orientation_energies.csv written.")
