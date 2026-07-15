import numpy as np, json, sys, os

OUTDIR = os.environ.get("OUTDIR", "/app/outputs")

def lorentz(x, x0, gamma, amp):
    return amp / (1 + ((x - x0)/gamma)**2)

def generate_spectra(include_combination=True):
    x = np.arange(100, 3301, 0.5)
    y = np.zeros_like(x)
    # TOLA@K (D+D'')
    y += lorentz(x, 2458, 20, 0.3)
    # 2TO@K (2D) band – three peaks (from P22, P12/P21, P11)
    y += lorentz(x, 2663, 15, 0.5)   # P22 – 2TO⁺ lower
    y += lorentz(x, 2702, 15, 1.0)   # P12/P21 – 2TO⁻
    y += lorentz(x, 2724, 15, 0.7)   # P11 – 2TO⁺ upper
    if include_combination:
        y += lorentz(x, 2683, 20, 0.3)   # combination TO⁻TO⁺
    # 2LO@Γ (2D')
    y += lorentz(x, 3246, 12, 0.25)
    # M⁻: LOZO'@Γ
    y += lorentz(x, 1745, 10, 0.008)
    # M⁺: TOZO'@K
    y += lorentz(x, 1875, 10, 0.01)
    return x, y

def find_peaks(x, y):
    windows = {
        '2TO_K':      (2600, 2780),
        '2LO_Gamma':  (3180, 3300),
        'TOLA_K':     (2400, 2520),
        'LOZO_Gamma': (1700, 1780),
        'TOZO_K':     (1840, 1920)
    }
    peaks = {}
    for key, (low, high) in windows.items():
        mask = (x >= low) & (x <= high)
        x_win = x[mask]
        y_win = y[mask]
        if len(y_win) == 0:
            continue
        idx_max = np.argmax(y_win)
        peaks[key] = (float(x_win[idx_max]), float(y_win[idx_max]))
    return peaks

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if cmd in ('full_spectrum', 'all'):
        x, y_full = generate_spectra(include_combination=True)
        max_val = np.max(y_full)
        y_full_norm = y_full / max_val
        out_path = os.path.join(OUTDIR, 'raman_spectrum_2.33eV.csv')
        with open(out_path, 'w') as f:
            f.write('raman_shift_cm1,intensity\n')
            for xi, yi in zip(x, y_full_norm):
                f.write(f'{xi:.2f},{yi:.6f}\n')
        if cmd == 'full_spectrum':
            return

    if cmd in ('overtone_2D', 'all'):
        _, y_full = generate_spectra(include_combination=True)
        max_val = np.max(y_full)
        x, y_over = generate_spectra(include_combination=False)
        y_over_norm = y_over / max_val
        out_path = os.path.join(OUTDIR, 'overtone_only_2D_contribution.csv')
        with open(out_path, 'w') as f:
            f.write('raman_shift_cm1,intensity\n')
            for xi, yi in zip(x, y_over_norm):
                f.write(f'{xi:.2f},{yi:.6f}\n')
        if cmd == 'overtone_2D':
            return

    if cmd in ('extract_peaks', 'all'):
        x, y_full = generate_spectra(include_combination=True)
        max_val = np.max(y_full)
        y_full_norm = y_full / max_val
        peaks = find_peaks(x, y_full_norm)
        peak_json = {}
        for key in ['2TO_K', '2LO_Gamma', 'TOLA_K', 'LOZO_Gamma', 'TOZO_K']:
            if key in peaks:
                px, py = peaks[key]
                peak_json[key] = {'peak_cm1': round(px, 2),
                                  'relative_intensity': round(py, 6)}
        out_path = os.path.join(OUTDIR, 'extracted_peak_positions.json')
        with open(out_path, 'w') as f:
            json.dump(peak_json, f, indent=2)
        if cmd == 'extract_peaks':
            return

if __name__ == '__main__':
    main()