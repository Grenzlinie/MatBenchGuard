import numpy as np
from scipy.optimize import fsolve
from scipy.ndimage import minimum_filter
import math, cmath

def k0(omega, c):
    if omega.imag == 0:
        if abs(omega.real) <= c:
            return 1j * math.sqrt(c**2 - omega.real**2)
        else:
            return math.sqrt(omega.real**2 - c**2) if omega.real > c else -math.sqrt(omega.real**2 - c**2)
    else:
        val = cmath.sqrt(omega**2 - c**2)
        if omega.imag < 0 and (omega.real > c or omega.real < -c):
            return -val
        else:
            return val

def build_A(omega, N, a, c, alpha, epsilon):
    d = c**2 * epsilon - omega**2 * alpha
    x = (np.arange(N) + 0.5) * a
    B = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(N):
            B[i,j] = d * np.exp(1j * k0(omega, c) * abs(x[i] - x[j]))
    A = 2j * k0(omega, c) * np.eye(N) - B
    g_vec = np.exp(1j * k0(omega, c) * abs(x))
    return A, g_vec, d, x

def det_val(omega, N, a, c, alpha, epsilon):
    A, _, _, _ = build_A(omega, N, a, c, alpha, epsilon)
    return np.linalg.det(A)

def find_poles(N, a, c, alpha, epsilon):
    poles = []
    if N == 1:
        def f(om):
            return [det_val(om[0]+1j*om[1], N, a, c, alpha, epsilon).real,
                    det_val(om[0]+1j*om[1], N, a, c, alpha, epsilon).imag]
        # initial guess from approximate formula if available
        if abs(alpha) < 1e-12:
            # alpha=0 case
            if abs(epsilon*c) < 2:
                omega_real = c*math.sqrt(1 - (epsilon*c)**2/4)
                guess = omega_real + 0.1j
            else:
                guess = c + 0.1j
        else:
            # guess near continuous edge
            guess = c + 0.1j
        try:
            sol = fsolve(f, [guess.real, guess.imag], maxfev=200, xtol=1e-8)
            root = sol[0] + 1j*sol[1]
            if abs(det_val(root, N, a, c, alpha, epsilon)) < 1e-4:
                poles.append(root)
        except:
            pass
        return poles

    # For N >= 2: scan near asymptotic centers
    centers = []
    n = 1
    while True:
        center_real = math.sqrt(c**2 + (n*math.pi/a)**2)
        if center_real > 20:
            break
        centers.append(center_real)
        n += 1

    for cr in centers:
        real_vals = np.linspace(cr-0.8, cr+0.8, 120)
        imag_vals = np.linspace(-0.4, 0.0, 80)
        grid_values = np.zeros((len(real_vals), len(imag_vals)))
        for i, r in enumerate(real_vals):
            for j, im in enumerate(imag_vals):
                omega = r + 1j*im
                d = abs(np.linalg.det(build_A(omega, N, a, c, alpha, epsilon)[0]))
                grid_values[i,j] = np.log10(max(d, 1e-300))
        local_min = minimum_filter(grid_values, size=5) == grid_values
        candidates = []
        for i in range(len(real_vals)):
            for j in range(len(imag_vals)):
                if local_min[i,j] and grid_values[i,j] < -1:
                    candidates.append((real_vals[i], imag_vals[j]))
        for r0, im0 in candidates:
            def f(om):
                return [det_val(om[0]+1j*om[1], N, a, c, alpha, epsilon).real,
                        det_val(om[0]+1j*om[1], N, a, c, alpha, epsilon).imag]
            try:
                sol = fsolve(f, [r0, im0], maxfev=100, xtol=1e-6)
                root = sol[0] + 1j*sol[1]
                if abs(det_val(root, N, a, c, alpha, epsilon)) < 1e-4:
                    poles.append(root)
            except:
                pass
    # deduplicate and filter
    unique = []
    for p in poles:
        if not any(abs(p - q) < 1e-5 for q in unique):
            unique.append(p)
    unique = [p for p in unique if p.imag < 0 and c < p.real < 20]
    return unique

def compute_transmission(N, a, c, alpha, epsilon):
    if N == 0:
        return [], []
    omega_arr = np.arange(c+0.01, 20.0, 0.01)
    kappa_arr = []
    for omega in omega_arr:
        A, g_vec, d, x = build_A(omega, N, a, c, alpha, epsilon)
        w = np.linalg.solve(A, g_vec)
        x_plus = x[-1] + 1.0
        g_plus = np.exp(1j * k0(omega, c) * x_plus) / (2j * k0(omega, c))
        w_plus = g_plus + np.sum(w * d * np.exp(1j * k0(omega, c) * abs(x_plus - x)) / (2j * k0(omega, c)))
        kappa = abs(w_plus / g_plus)**2
        kappa_arr.append(kappa)
    return omega_arr, np.array(kappa_arr)

def find_bands_from_transmission(omega_arr, kappa_arr, threshold=0.5):
    bands = []
    in_band = False
    start = None
    for i, k in enumerate(kappa_arr):
        if k > threshold and not in_band:
            start = omega_arr[i]
            in_band = True
        elif k <= threshold and in_band:
            bands.append((start, omega_arr[i]))
            in_band = False
    if in_band:
        bands.append((start, omega_arr[-1]))
    return bands

def compute_bloch_bands(a, c, alpha, epsilon, max_omega=20.0):
    omega_arr = np.arange(c+0.01, max_omega, 0.01)
    bands = []
    in_band = False
    start = None
    for omega in omega_arr:
        k0_val = math.sqrt(omega**2 - c**2)
        d = c**2 * epsilon - omega**2 * alpha
        L = abs( np.cos(a * k0_val) + (d * a / k0_val) * np.sin(a * k0_val) )
        if L < 1:
            if not in_band:
                start = omega
                in_band = True
        else:
            if in_band:
                bands.append((start, omega))
                in_band = False
    if in_band:
        bands.append((start, max_omega))
    return bands

def main():
    params = [(0.5, 0.5, 1.0, 4.0), (0.0, 1.0, 1.0, 4.0)]
    Ns = [1, 2, 5, 10, 20, 50]

    with open('/app/outputs/poles_all_N.csv', 'w') as f:
        f.write('N,real_part,imag_part,alpha,epsilon,a,c\n')
        for alpha, epsilon, a, c_val in params:
            for N in Ns:
                poles = find_poles(N, a, c_val, alpha, epsilon)
                for p in poles:
                    f.write(f'{N},{p.real:.8f},{p.imag:.8f},{alpha},{epsilon},{a},{c_val}\n')

    with open('/app/outputs/transmission_coefficient_N.csv', 'w') as f:
        f.write('N,kappa_plus,omega\n')
        for alpha, epsilon, a, c_val in params:
            for N in Ns:
                omega_arr, kappa_arr = compute_transmission(N, a, c_val, alpha, epsilon)
                for om, kap in zip(omega_arr, kappa_arr):
                    f.write(f'{N},{kap:.8f},{om:.8f}\n')

    with open('/app/outputs/band_edges_comparison.csv', 'w') as f:
        f.write('band_type,lower_edge,upper_edge,method\n')
        for alpha, epsilon, a, c_val in params:
            omega_arr, kappa_arr = compute_transmission(50, a, c_val, alpha, epsilon)
            bands_trans = find_bands_from_transmission(omega_arr, kappa_arr)
            for low, high in bands_trans:
                f.write(f'transmission,{low:.8f},{high:.8f},kappa_plus\n')
            bands_bloch = compute_bloch_bands(a, c_val, alpha, epsilon)
            for low, high in bands_bloch:
                f.write(f'Bloch-Floquet,{low:.8f},{high:.8f},inequality\n')

if __name__ == '__main__':
    main()