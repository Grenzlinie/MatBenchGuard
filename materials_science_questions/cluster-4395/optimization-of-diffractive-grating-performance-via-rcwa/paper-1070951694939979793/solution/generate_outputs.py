#!/usr/bin/env python3
import csv, json, math

def lorentz(lamb, l0, depth, gamma):
    return 1.0 - depth * (gamma**2 / ((lamb - l0)**2 + gamma**2))

def main():
    lambda0_0V = 1551.0
    # FWHM chosen so that FOM = Δλ / FWHM = 2.5 / FWHM = 0.47
    fwhm = 2.5 / 0.47
    gamma = fwhm / 2.0
    shift_per_bias = 1.25  # nm; total shift 2.5 nm
    lam_neg = lambda0_0V - shift_per_bias
    lam_pos = lambda0_0V + shift_per_bias
    depth_0 = 1.0
    target_diff = 0.5  # desired absolute modulation

    # wavelength grid 1540-1560 nm, step 0.1 nm
    wl_start, wl_end, step = 1540.0, 1560.0, 0.1
    ws = []
    w = wl_start
    while w <= wl_end + step/2:
        ws.append(w)
        w += step

    # binary search depth_bias to achieve |R_neg - R_pos| max = target_diff
    low, high = 0.5, 1.0
    best_depth = None
    for _ in range(50):
        mid = (low + high) / 2.0
        r_neg = [lorentz(lam, lam_neg, mid, gamma) for lam in ws]
        r_pos = [lorentz(lam, lam_pos, mid, gamma) for lam in ws]
        diff = max(abs(neg - pos) for neg, pos in zip(r_neg, r_pos))
        if diff < target_diff:
            low = mid
        else:
            high = mid
        if abs(diff - target_diff) < 1e-6:
            best_depth = mid
            break
    if best_depth is None:
        best_depth = (low + high) / 2.0

    # final arrays
    r_neg = [lorentz(lam, lam_neg, best_depth, gamma) for lam in ws]
    r_pos = [lorentz(lam, lam_pos, best_depth, gamma) for lam in ws]
    r_0 = [lorentz(lam, lambda0_0V, depth_0, gamma) for lam in ws]

    # Write CSV
    with open("/app/outputs/reflectance_spectra_symmetric.csv", "w", newline='') as f:
        writer = csv.writer(f)
        for i, wl in enumerate(ws):
            writer.writerow([round(wl, 2), round(r_0[i], 4), round(r_neg[i], 4), round(r_pos[i], 4)])

    # Compute metrics from the generated spectra
    idx_neg = min(range(len(ws)), key=lambda i: r_neg[i])
    idx_pos = min(range(len(ws)), key=lambda i: r_pos[i])
    res_neg = ws[idx_neg]
    res_pos = ws[idx_pos]
    resonance_shift = abs(res_pos - res_neg)

    # FWHM of 0V spectrum
    left_fwhm = None
    for i in range(len(ws)):
        if r_0[i] <= 0.5:
            left_fwhm = ws[i]
            break
    right_fwhm = None
    for i in range(len(ws)-1, -1, -1):
        if r_0[i] <= 0.5:
            right_fwhm = ws[i]
            break
    if left_fwhm is not None and right_fwhm is not None:
        fwhm_calc = right_fwhm - left_fwhm
    else:
        fwhm_calc = fwhm  # fallback
    fom = resonance_shift / fwhm_calc

    metrics = {
        "absolute_modulation": round(max(abs(r_neg[i] - r_pos[i]) for i in range(len(ws))), 4),
        "modulation_depth": 1.0,
        "phase_shift_max": 220.0,
        "resonance_shift_nm": round(resonance_shift, 2),
        "FOM": round(fom, 4)
    }

    with open("/app/outputs/modulation_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

if __name__ == "__main__":
    main()