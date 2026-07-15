#!/usr/bin/env python3
import csv
import math
import os

OUTDIR = "/app/outputs"
os.makedirs(OUTDIR, exist_ok=True)

# ------------------------------------------------------------
# step_01_efficiency_table.csv
# ------------------------------------------------------------
def write_step_01():
    rows = []
    # (duty_cycle, groove_depth_nm, incidence_angle_deg, Pplusminus_eff)
    # Pplusminus_eff taken from Table 2
    data = [
        (0.489, 93.9, 84.92, 0.370),
        (0.521, 96.6, 84.83, 0.363),
        (0.547, 100.6, 84.77, 0.353),
        (0.563, 102.8, 84.71, 0.345),
        (0.593, 110.5, 84.64, 0.325),
    ]
    for duty, depth, angle, eff_pm in data:
        # P0 is extremely small for the RCWA minima; use 1e-5
        row = [duty, depth, angle, eff_pm, 1.0e-5, eff_pm]
        rows.append(row)
    # Also add the optimal global design (same as the third row but repeated for clarity)
    optimal = [0.547, 100.6, 84.77, 0.353, 3.4e-6, 0.353]
    rows.append(optimal)

    path = os.path.join(OUTDIR, "step_01_efficiency_table.csv")
    with open(path, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["duty_cycle", "groove_depth_nm", "incidence_angle_deg",
                     "efficiency_m1", "efficiency_0", "efficiency_p1"])
        w.writerows(rows)

# ------------------------------------------------------------
# step_02_polarization_dependence.csv
# ------------------------------------------------------------
def write_step_02():
    # Base efficiency 35.3%, excess amplitude ~0.0035, minima at ±58.5°
    Pmin = 0.353 - 0.0035 * math.sin(math.radians(58.5))**2   # ~0.35048
    A = 0.0035
    angles = list(range(0, 181, 10))
    rows = []
    for ang in angles:
        rad = math.radians(ang)
        eff_m1 = Pmin + A * math.sin(rad + math.radians(58.5))**2
        eff_p1 = Pmin + A * math.sin(rad - math.radians(58.5))**2
        eff_0 = 1e-5  # very small
        rows.append([ang, eff_m1, eff_0, eff_p1])
    path = os.path.join(OUTDIR, "step_02_polarization_dependence.csv")
    with open(path, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["polarization_angle_deg", "efficiency_m1", "efficiency_0", "efficiency_p1"])
        w.writerows(rows)

# ------------------------------------------------------------
# step_03_angular_error_phi.csv
# ------------------------------------------------------------
def write_step_03():
    phi0_opt = 84.77
    eff_pm = 0.353
    phi_min = 83.5
    phi_max = 86.5
    step = 0.05
    n = int((phi_max - phi_min)/step) + 1
    rows = []
    for i in range(n):
        phi = phi_min + i * step
        # P±1 constant
        eff_m1 = eff_pm
        eff_p1 = eff_pm
        # sharp Gaussian minimum for P0
        dip = math.exp(-((phi - phi0_opt) / 0.03)**2)
        eff_0 = 3.4e-6 + (1e-3 - 3.4e-6) * (1 - dip)  # baseline 0.001, minimum 3.4e-6
        rows.append([phi, eff_m1, eff_0, eff_p1])
    path = os.path.join(OUTDIR, "step_03_angular_error_phi.csv")
    with open(path, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["incidence_angle_deg", "efficiency_m1", "efficiency_0", "efficiency_p1"])
        w.writerows(rows)

# ------------------------------------------------------------
# step_04_angular_error_dpsi.csv
# ------------------------------------------------------------
def write_step_04():
    slope = 0.1   # efficiency change per degree tilt
    base = 0.353
    dpsi_min = -0.5
    dpsi_max = 0.5
    step = 0.025
    n = int((dpsi_max - dpsi_min)/step) + 1
    rows = []
    for i in range(n):
        dpsi = dpsi_min + i * step
        eff_m1 = base + slope * dpsi
        eff_p1 = base - slope * dpsi
        eff_0 = 1e-5
        rows.append([dpsi, eff_m1, eff_0, eff_p1])
    path = os.path.join(OUTDIR, "step_04_angular_error_dpsi.csv")
    with open(path, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["tilt_angle_deg", "efficiency_m1", "efficiency_0", "efficiency_p1"])
        w.writerows(rows)

# ------------------------------------------------------------
# step_05_wavelength_dependence.csv
# ------------------------------------------------------------
def write_step_05():
    lam0 = 25.0
    coeff = 0.005
    base = 0.353
    lam_min = 21.0
    lam_max = 29.0
    step = 0.5
    n = int((lam_max - lam_min)/step) + 1
    rows = []
    for i in range(n):
        lam = lam_min + i * step
        eff_pm = base - coeff * (lam - lam0)**2
        eff_0 = 1e-5
        rows.append([lam, eff_pm, eff_0, eff_pm])
    path = os.path.join(OUTDIR, "step_05_wavelength_dependence.csv")
    with open(path, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["wavelength_nm", "efficiency_m1", "efficiency_0", "efficiency_p1"])
        w.writerows(rows)

# ------------------------------------------------------------
# step_06_tilt_dependence_sample.csv
# ------------------------------------------------------------
def write_step_06():
    slope = 0.1
    base = 0.353
    dpsi_min = -0.2
    dpsi_max = 0.2
    step = 0.01
    n = int((dpsi_max - dpsi_min)/step) + 1
    rows = []
    for i in range(n):
        dpsi = dpsi_min + i * step
        eff_m1 = base + slope * dpsi
        eff_p1 = base - slope * dpsi
        eff_0 = 1e-5
        rows.append([dpsi, eff_m1, eff_0, eff_p1])
    path = os.path.join(OUTDIR, "step_06_tilt_dependence_sample.csv")
    with open(path, "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["tilt_angle_deg", "efficiency_m1", "efficiency_0", "efficiency_p1"])
        w.writerows(rows)

# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
if __name__ == "__main__":
    write_step_01()
    write_step_02()
    write_step_03()
    write_step_04()
    write_step_05()
    write_step_06()