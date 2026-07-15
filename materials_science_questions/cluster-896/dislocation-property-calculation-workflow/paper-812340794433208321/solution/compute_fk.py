import numpy as np
from scipy.optimize import minimize
import csv

# Parameters (all dimensionless in the paper's units)
U0 = 1.0
a = 1.0
b = 0.887           # b/a
k = 800.0           # k a^2 / U0 = 800 => k = 800 (since a=1, U0=1)
m = 1.0
mu = 3.0            # mu = 3 sqrt(U0/(m a^2)) = 3
Ks = 10.0           # Ks a^2 / U0 = 10 => Ks = 10
vs = 0.01           # v_s = 0.01 sqrt(U0/m)
dt = 0.01
Ns = [7, 8, 9, 10, 11]

def total_energy(x, N):
    """FK total energy (Eq. 1)"""
    sub = U0 * (1.0 - np.cos(2.0 * np.pi * x))
    springs = 0.0
    for i in range(N - 1):
        dx = x[i+1] - x[i] - b
        springs += 0.5 * k * dx * dx
    return np.sum(sub) + springs

def grad_energy(x, N):
    """Gradient of total energy w.r.t. x"""
    grad = 2.0 * np.pi * U0 * np.sin(2.0 * np.pi * x)
    for i in range(N):
        if i > 0:
            dx = x[i] - x[i-1] - b
            grad[i] += k * dx
        if i < N-1:
            dx = x[i+1] - x[i] - b
            grad[i] -= k * dx
    return grad

def energy_minimisation(N):
    """Find unconstrained minimum-energy configuration."""
    x0 = np.arange(N) * b
    x0 -= np.mean(x0)  # center around 0
    res = minimize(total_energy, x0, args=(N,), method='L-BFGS-B',
                   jac=grad_energy, options={'gtol': 1e-12, 'ftol': 1e-14})
    return res.x, res.fun

def activation_energy(N, x_min, e_min):
    """Compute activation energy by constraining each atom at a potential peak."""
    energies = []
    for j in range(N):
        # nearest peak for atom j
        peak = np.round(x_min[j] - 0.5) + 0.5
        # Fix x[j] at peak
        x_fix = x_min.copy()
        x_fix[j] = peak
        # Optimise the other N-1 coordinates
        def opt_others(vars):
            x_full = x_fix.copy()
            idx = 0
            for i in range(N):
                if i != j:
                    x_full[i] = vars[idx]
                    idx += 1
            return total_energy(x_full, N)
        def grad_others(vars):
            x_full = x_fix.copy()
            idx = 0
            for i in range(N):
                if i != j:
                    x_full[i] = vars[idx]
                    idx += 1
            full_grad = grad_energy(x_full, N)
            return np.delete(full_grad, j)
        init = np.delete(x_min, j)
        res = minimize(opt_others, init, method='L-BFGS-B',
                       jac=grad_others, options={'gtol': 1e-12, 'ftol': 1e-14})
        energies.append(res.fun)
    return max(energies) - e_min

def depinning_force(N, x_eq):
    """Binary search for critical depinning force."""
    def simulate_constant_force(F):
        x = x_eq.copy()
        v = np.zeros(N)
        nsteps = 5000
        for step in range(nsteps):
            # Velocity Verlet half-step for v? Simple Euler: a = F_total / m
            grad = grad_energy(x, N)
            a = -grad - mu * v + F  # m=1
            v += a * dt
            x += v * dt
        # drift velocity in last half
        x_start = np.copy(x)
        v_half = np.zeros(N)
        for step in range(2500):
            grad = grad_energy(x, N)
            a = -grad - mu * v + F
            v += a * dt
            x += v * dt
        x_cm_end = np.mean(x)
        x_cm_start = np.mean(x_start)
        v_drift = (x_cm_end - x_cm_start) / (2500 * dt)
        return v_drift

    # bracket the threshold
    lo, hi = 0.0, 1.0
    # find hi that depins
    while simulate_constant_force(hi) < 1e-3:
        hi *= 2.0
        if hi > 10.0:  # safety
            break
    for _ in range(15):
        mid = (lo + hi) / 2.0
        if simulate_constant_force(mid) > 1e-3:
            hi = mid
        else:
            lo = mid
    return hi

def max_spring_force(N, x_eq):
    """Stick-slip spring-driven simulation."""
    x = x_eq.copy()
    v = np.zeros(N)
    t = 0.0
    nsteps = 15000  # total time = 15000*0.01=150, sliding several periods
    forces = []
    for step in range(nsteps):
        cm = np.mean(x)
        F_spring = -Ks * (cm - vs * t)
        grad = grad_energy(x, N)
        a = -grad - mu * v + F_spring
        v += a * dt
        x += v * dt
        t += dt
        if step > 500:  # discard initial transient
            forces.append(abs(F_spring))
    return max(forces)

if __name__ == "__main__":
    act_vals = []
    crit_vals = []
    maxf_vals = []
    for N in Ns:
        x_eq, e_eq = energy_minimisation(N)
        ea = activation_energy(N, x_eq, e_eq)
        act_vals.append((N, ea))
        Fc = depinning_force(N, x_eq)
        crit_vals.append((N, Fc))
        Fm = max_spring_force(N, x_eq)
        maxf_vals.append((N, Fm))
        print(f"N={N}: Ea={ea:.4f}, Fc={Fc:.4f}, Fm={Fm:.4f}")
    # Write CSVs
    with open("/app/outputs/activation_energy_vs_N.csv", "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["N", "activation_energy"])
        for row in act_vals:
            w.writerow(row)
    with open("/app/outputs/critical_force_vs_N.csv", "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["N", "critical_force"])
        for row in crit_vals:
            w.writerow(row)
    with open("/app/outputs/max_spring_force_vs_N.csv", "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["N", "max_spring_force"])
        for row in maxf_vals:
            w.writerow(row)
