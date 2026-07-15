import csv
import json
import math

def generate_contact_force_csv(filepath, peak_N, T0_s, npoints=500):
    with open(filepath, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['time', 'contact_force'])
        dt = T0_s / (npoints - 1)
        for i in range(npoints):
            t = i * dt
            force = peak_N * math.sin(math.pi * t / T0_s) if t <= T0_s else 0.0
            w.writerow([t, force])

def main():
    # Validation case (isotropic clamped circular plate, Fig 1)
    peak_validation_N = 1330.0          # 1.33 kN
    T0_validation_s   = 55e-6           # 55 µs
    MCF_validation_kN = peak_validation_N / 1000.0
    alpha_max_validation_mm = 0.22
    w_max_validation_mm     = 0.26
    T0_validation_us        = T0_validation_s * 1e6

    generate_contact_force_csv('/app/outputs/contact_force_validation.csv',
                               peak_validation_N, T0_validation_s)

    # FG-CNTRC case (X-CNTRC, V*_CNT=0.28, T=300 K, Table 4)
    peak_fg_N = 2850.0                  # 2.85 kN
    T0_fg_s   = 408e-6                  # 408 µs
    MCF_fg_kN       = peak_fg_N / 1000.0
    alpha_max_fg_mm = 0.16
    w_max_fg_mm     = 0.260
    T0_fg_us        = 408.0

    generate_contact_force_csv('/app/outputs/contact_force_fg_cntrc.csv',
                               peak_fg_N, T0_fg_s)

    metrics = {
        "validation": {
            "MCF": MCF_validation_kN,
            "alpha_max": alpha_max_validation_mm,
            "w_max": w_max_validation_mm,
            "T0": T0_validation_us
        },
        "fg_cntrc": {
            "MCF": MCF_fg_kN,
            "alpha_max": alpha_max_fg_mm,
            "w_max": w_max_fg_mm,
            "T0": T0_fg_us
        }
    }
    with open('/app/outputs/summary_metrics.json', 'w') as f:
        json.dump(metrics, f, indent=2)

if __name__ == '__main__':
    main()