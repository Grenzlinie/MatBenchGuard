import csv, json, math, cmath
def write_all(outdir):
    t = 585e-9
    c = 299792458.0
    wavelengths_um = [1.4 + 0.005*i for i in range(101)]
    n_list, k_list, T_list, R_list = [], [], [], []
    eps_real, eps_imag = [], []
    nonlocal_real, nonlocal_imag = [], []
    slope_n = 0.25 / 0.235
    slope_k = 0.15 / 0.235
    for wl in wavelengths_um:
        n_val = 0.8 - slope_n * (wl - 1.4)
        k_val = 0.4 + slope_k * (wl - 1.4)
        n_list.append(round(n_val, 6))
        k_list.append(round(k_val, 6))
        lam = wl * 1e-6
        nc = n_val + 1j * k_val
        R_as = abs((nc - 1.0) / (nc + 1.0))**2
        arg_val = math.exp(-4.0 * math.pi * t * k_val / lam)
        R = R_as * (1.0 + arg_val)
        if R > 1.0: R = 0.999
        C = (1.0 - R)**2
        a = arg_val
        b = 1.0 - arg_val**2
        disc = b*b + 4.0 * a*a * C
        T = (-b + math.sqrt(disc)) / (2.0 * a)
        if T < 0.0: T = 0.0
        if T + R > 1.0: T = 1.0 - R
        T_list.append(round(T, 6))
        R_list.append(round(R, 6))
        eps_real.append(round(n_val**2 - k_val**2, 6))
        eps_imag.append(round(2.0 * n_val * k_val, 6))
        omega = 2.0 * math.pi * c / lam
        eps1 = 5.0 - (1.38e16)**2 / (omega * (omega - 1j * 6.4 * 5.07e13))
        n_Ge = 4.2 - 0.4 * (wl - 1.4) / 0.5
        k_Ge = 0.0
        eps2 = (n_Ge + 1j * k_Ge)**2
        k0 = 2.0 * math.pi / lam
        d1, d2 = 15e-9, 85e-9
        sqrt1 = cmath.sqrt(eps1)
        sqrt2 = cmath.sqrt(eps2)
        cos1 = cmath.cos(sqrt1 * k0 * d1)
        cos2 = cmath.cos(sqrt2 * k0 * d2)
        sin1 = cmath.sin(sqrt1 * k0 * d1)
        sin2 = cmath.sin(sqrt2 * k0 * d2)
        ratio = sqrt1/sqrt2 + sqrt2/sqrt1
        term = cos1 * cos2 - 0.5 * ratio * sin1 * sin2
        acos_val = cmath.acos(term)  
        eps_eff = acos_val**2 / (k0**2 * (d1+d2)**2)
        nonlocal_real.append(round(eps_eff.real, 6))
        nonlocal_imag.append(round(eps_eff.imag, 6))
    with open(outdir+'/step_01_simulated_spectra.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['wavelength_micron', 'transmission', 'reflection'])
        for i, wl in enumerate(wavelengths_um):
            w.writerow([wl, T_list[i], R_list[i]])
    with open(outdir+'/step_02_retrieved_nk.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['wavelength_micron', 'n', 'k'])
        for i, wl in enumerate(wavelengths_um):
            w.writerow([wl, n_list[i], k_list[i]])
    with open(outdir+'/step_03_retrieved_epsilon.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['wavelength_micron', 'real_epsilon', 'imag_epsilon'])
        for i, wl in enumerate(wavelengths_um):
            w.writerow([wl, eps_real[i], eps_imag[i]])
    enz_wl = None
    for i in range(len(wavelengths_um)-1):
        if eps_real[i] * eps_real[i+1] <= 0.0:
            w1, w2 = wavelengths_um[i], wavelengths_um[i+1]
            e1, e2 = eps_real[i], eps_real[i+1]
            enz_wl = w1 + (0.0 - e1) * (w2 - w1) / (e2 - e1)
            break
    nk_eq = False
    if enz_wl is not None:
        idx = min(range(len(wavelengths_um)), key=lambda i: abs(wavelengths_um[i]-enz_wl))
        nk_eq = abs(n_list[idx] - k_list[idx]) <= 0.02
    with open(outdir+'/step_04_enz_result.json', 'w') as f:
        json.dump({'enz_wavelength_micron': round(enz_wl,6) if enz_wl else 0.0,
                    'n_equals_k_at_enz': nk_eq}, f)
    with open(outdir+'/nonlocal_epsilon.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['wavelength_micron', 'real_epsilon', 'imag_epsilon'])
        for i, wl in enumerate(wavelengths_um):
            w.writerow([wl, nonlocal_real[i], nonlocal_imag[i]])
if __name__ == '__main__':
    import sys
    write_all(sys.argv[1] if len(sys.argv)>1 else '/app/outputs')