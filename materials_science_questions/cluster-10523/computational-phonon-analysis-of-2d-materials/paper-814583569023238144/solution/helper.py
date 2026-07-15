import numpy as np

def gaussian(x, A, x0, sigma):
    return A * np.exp(-0.5 * ((x - x0) / sigma) ** 2)

def generate_pdos(vacancy, freq):
    # vacancy: 0, 10, 20, 30
    v = vacancy
    # base pristine peaks: low, E2g, high
    peak_low   = gaussian(freq, 1.0, 450, 120)
    peak_high  = gaussian(freq, 0.8, 2900, 100)
    # E2g parameters depend on vacancy
    center2 = 1350.0 - v * 1.3333
    sigma2  = 25.0 + v * 2.0
    amp2    = 2.0 * (1.0 - v / 60.0)
    peak_e2g = gaussian(freq, amp2, center2, sigma2)
    pdos = peak_low + peak_e2g + peak_high
    # intermediate region reduction factor
    factor = np.ones_like(freq)
    mask = (freq >= 500) & (freq <= 1500)
    factor[mask] = 1.0 - v / 100.0
    pdos = pdos * factor
    return np.maximum(pdos, 0.0)

def compute_cv(pdos, freq, temps):
    # freq in cm-1, pdos arbitrary; returns cv array
    hc_over_kb = 1.4388  # cm*K
    cv = np.zeros_like(temps, dtype=float)
    for i, T in enumerate(temps):
        if T == 0:
            continue
        x = freq * hc_over_kb / T
        x = np.clip(x, None, 700)   # avoid overflow
        expx = np.exp(x)
        integrand = pdos * x**2 * expx / (expx - 1)**2
        cv[i] = np.trapz(integrand, freq)
    return cv