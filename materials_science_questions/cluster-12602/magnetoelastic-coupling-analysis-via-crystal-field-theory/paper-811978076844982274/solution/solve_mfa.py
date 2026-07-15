import numpy as np
from scipy.optimize import fsolve

k = -1.1
c = 1.0
l = 1.0
m = 2.0

# zero-T values
sigma0 = 1.0
eps0_A = (2*l - k) / (2*c)
eps0_F = (2*l + k) / (2*c)
f0_A = 1.0 - m - (2*l - k)**2 / (4*c)
f0_F = -1.0 - m - (2*l + k)**2 / (4*c)

def A_residuals(vars, t, k, l, c, m):
    sigma, eps = vars[0], vars[1]
    b = sigma * (m - (1.0 + k*eps)) / t
    a = l * eps / t
    x = a + np.logaddexp(b, -b)
    sigmoid = 1.0 / (1.0 + np.exp(-x))
    tanh_b = np.tanh(b)
    eq1 = sigma - tanh_b * sigmoid
    eq2 = eps - (2*l * sigmoid - sigma**2 * k) / (2*c)
    return [eq1, eq2]

def F_residuals(vars, t, k, l, c, m):
    sigma, eps = vars[0], vars[1]
    b = sigma * (m + 1.0 + k*eps) / t
    a = l * eps / t
    x = a + np.logaddexp(b, -b)
    sigmoid = 1.0 / (1.0 + np.exp(-x))
    tanh_b = np.tanh(b)
    eq1 = sigma - tanh_b * sigmoid
    eq2 = eps - (2*l * sigmoid + sigma**2 * k) / (2*c)
    return [eq1, eq2]

def free_energy(t, sigma, eps, phase):
    if t == 0:
        if phase == 'A':
            return 1.0 - m - (2*l - k)**2 / (4*c)
        else:
            return -1.0 - m - (2*l + k)**2 / (4*c)
    else:
        if phase == 'A':
            y1 = sigma * (m - (1.0 + k*eps))
        else:
            y1 = sigma * (m + 1.0 + k*eps)
        b = y1 / t
        a = l * eps / t
        x = a + np.logaddexp(b, -b)
        ln_denom = np.logaddexp(x, 0)
        if phase == 'A':
            f = -2 * t * ln_denom + sigma**2 * (-1.0 + m - k*eps) + c * eps**2
        else:
            f = -2 * t * ln_denom + sigma**2 * (1.0 + m + k*eps) + c * eps**2
        return f

# grid
t_fine = np.arange(0.01, 2.01, 0.01)  # 200 points
t_list = np.concatenate([[0.0], t_fine])

sigma_A = np.full_like(t_list, 0.0)
eps_A = np.full_like(t_list, 0.0)
f_A = np.full_like(t_list, 0.0)
sigma_F = np.full_like(t_list, 0.0)
eps_F = np.full_like(t_list, 0.0)
f_F = np.full_like(t_list, 0.0)

# zero
sigma_A[0] = sigma0
eps_A[0] = eps0_A
f_A[0] = f0_A
sigma_F[0] = sigma0
eps_F[0] = eps0_F
f_F[0] = f0_F

# initial guesses for t>0
init_A = [sigma0, eps0_A]
init_F = [sigma0, eps0_F]

for i in range(1, len(t_list)):
    t = t_list[i]
    # A phase
    sol_A, infodict, ier, msg = fsolve(A_residuals, init_A, args=(t, k, l, c, m), full_output=True)
    if ier == 1:
        sA, eA = sol_A[0], sol_A[1]
    else:
        # fallback: try different initial guess
        sol_A, infodict, ier, msg = fsolve(A_residuals, [0.5, 0.5], args=(t, k, l, c, m), full_output=True)
        if ier == 1:
            sA, eA = sol_A[0], sol_A[1]
        else:
            # use previous solution as best guess
            sA, eA = init_A
    init_A = [sA, eA]
    sigma_A[i] = sA
    eps_A[i] = eA
    f_A[i] = free_energy(t, sA, eA, 'A')

    # F phase
    sol_F, infodict, ier, msg = fsolve(F_residuals, init_F, args=(t, k, l, c, m), full_output=True)
    if ier == 1:
        sF, eF = sol_F[0], sol_F[1]
    else:
        sol_F, infodict, ier, msg = fsolve(F_residuals, [0.5, 0.5], args=(t, k, l, c, m), full_output=True)
        if ier == 1:
            sF, eF = sol_F[0], sol_F[1]
        else:
            sF, eF = init_F
    init_F = [sF, eF]
    sigma_F[i] = sF
    eps_F[i] = eF
    f_F[i] = free_energy(t, sF, eF, 'F')

# write CSV
output_path = '/app/outputs/magnetoelastic_results.csv'
with open(output_path, 'w') as f:
    f.write('t,sigma_A,sigma_F,epsilon_A,epsilon_F,f_A,f_F\n')
    for i in range(len(t_list)):
        f.write(f'{t_list[i]:.10f},{sigma_A[i]:.10f},{sigma_F[i]:.10f},{eps_A[i]:.10f},{eps_F[i]:.10f},{f_A[i]:.10f},{f_F[i]:.10f}\n')
