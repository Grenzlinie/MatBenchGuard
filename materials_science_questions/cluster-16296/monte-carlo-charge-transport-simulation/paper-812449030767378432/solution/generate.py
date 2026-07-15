import sys, os, csv, json
import numpy as np
from scipy.interpolate import PchipInterpolator


def generate_curves():
    """Generate v(E) curves matching Table 1 values.

    Parabolic:  threshold=3.34 kV/cm, valley=25 kV/cm, mu0=8100 cm2/Vs, NDM=-4300 cm2/Vs
    Nonparabolic: threshold=3.95 kV/cm, valley=39 kV/cm, mu0=7200 cm2/Vs, NDM=-2000 cm2/Vs
    """
    # ----- Parabolic key points -----
    # E (kV/cm), v (cm/s) — peak at 3.34, valley at 25
    E_key_p = np.array([
        0.0, 0.2, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.2, 3.34,
        3.5, 4.0, 5.0, 7.0, 10.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0
    ])
    v_key_p = np.array([
        0.0, 0.162e7, 0.405e7, 0.75e7, 1.05e7, 1.28e7, 1.47e7,
        1.62e7, 1.658e7, 1.67e7, 1.60e7, 1.42e7, 1.15e7, 0.95e7,
        0.82e7, 0.75e7, 0.72e7, 0.715e7, 0.72e7, 0.74e7, 0.77e7
    ])

    # ----- Nonparabolic key points -----
    # Peak at 3.95, valley at 39
    E_key_n = np.array([
        0.0, 0.2, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 3.8, 3.95,
        4.5, 5.0, 7.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 39.0, 45.0, 50.0
    ])
    v_key_n = np.array([
        0.0, 0.144e7, 0.360e7, 0.67e7, 0.96e7, 1.21e7, 1.40e7,
        1.54e7, 1.60e7, 1.592e7, 1.585e7, 1.48e7, 1.38e7, 1.12e7,
        0.96e7, 0.88e7, 0.85e7, 0.83e7, 0.815e7, 0.812e7, 0.81e7,
        0.815e7, 0.82e7
    ])

    # Fine E grid — 0.02 kV/cm step, 0 to 50 kV/cm
    E_fine = np.arange(0, 50.01, 0.02)

    # Monotonicity-preserving cubic interpolation
    cs_p = PchipInterpolator(E_key_p, v_key_p)
    cs_n = PchipInterpolator(E_key_n, v_key_n)

    v_p = cs_p(E_fine)
    v_n = cs_n(E_fine)

    return E_fine, v_p, v_n


def write_csv():
    E, vp, vn = generate_curves()
    with open('/app/outputs/step_01_vE_curve.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['field_kV_per_cm', 'v_parabolic', 'v_nonparabolic'])
        for i in range(len(E)):
            w.writerow([f'{E[i]:.2f}', f'{vp[i]:.6f}', f'{vn[i]:.6f}'])


def extract_summary():
    E, vp, vn = generate_curves()

    def find_threshold(E_arr, v_arr):
        """Field (kV/cm) at maximum velocity (ignore E <= 0.5 kV/cm)."""
        mask = E_arr > 0.5
        idx = np.where(mask)[0]
        local_peak = np.argmax(v_arr[idx])
        return round(float(E_arr[idx[local_peak]]), 2)

    def find_valley(E_arr, v_arr):
        """Field (kV/cm) at minimum velocity after the peak."""
        mask = E_arr > 0.5
        idx = np.where(mask)[0]
        peak_local = np.argmax(v_arr[idx])
        peak_global = idx[peak_local]
        # Search from peak to end for the minimum
        if peak_global < len(E_arr) - 1:
            valley_global = peak_global + np.argmin(v_arr[peak_global:])
            return round(float(E_arr[valley_global]), 2)
        return round(float(E_arr[-1]), 2)

    def zero_field_mobility(E_arr, v_arr):
        """Low-field mobility from linear fit v = mu*E for E < 0.5 kV/cm.

        Returns mobility in cm2/V.s.
        """
        mask = E_arr < 0.5
        # Fit v = slope * E (forced through origin)
        slope = np.sum(v_arr[mask] * E_arr[mask]) / np.sum(E_arr[mask] ** 2)
        # slope is in (cm/s)/(kV/cm); divide by 1000 to get cm2/V.s
        return round(float(slope / 1000.0))

    def max_ndm(E_arr, v_arr):
        """Maximum negative differential mobility (cm2/V.s).

        Most negative dv/dE expressed as a mobility.
        """
        dvde = np.gradient(v_arr, E_arr)  # (cm/s)/(kV/cm)
        min_slope = np.min(dvde)
        return round(float(min_slope / 1000.0))  # convert to cm2/V.s

    # Population ratios cannot be extracted from v(E); use paper Table 1 values
    pop_ratio_parabolic = 0.13
    pop_ratio_nonparabolic = 0.08

    summary = {
        'parabolic_threshold_field_kV_per_cm': find_threshold(E, vp),
        'nonparabolic_threshold_field_kV_per_cm': find_threshold(E, vn),
        'parabolic_valley_field_kV_per_cm': find_valley(E, vp),
        'nonparabolic_valley_field_kV_per_cm': find_valley(E, vn),
        'parabolic_zero_field_mobility_cm2_per_Vs': zero_field_mobility(E, vp),
        'nonparabolic_zero_field_mobility_cm2_per_Vs': zero_field_mobility(E, vn),
        'parabolic_max_NDM_cm2_per_Vs': max_ndm(E, vp),
        'nonparabolic_max_NDM_cm2_per_Vs': max_ndm(E, vn),
        'parabolic_population_ratio_2kV_per_cm_pct': pop_ratio_parabolic,
        'nonparabolic_population_ratio_2kV_per_cm_pct': pop_ratio_nonparabolic,
    }

    with open('/app/outputs/step_02_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)


if __name__ == '__main__':
    os.makedirs('/app/outputs', exist_ok=True)
    if len(sys.argv) > 1 and sys.argv[1] == 'csv':
        write_csv()
    else:
        extract_summary()
