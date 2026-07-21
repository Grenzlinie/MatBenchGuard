#!/usr/bin/env python3
import sys
import math
import csv
import os

def compute_deflection(R1, R2, hp, hb, hm, s11E, sb, sm, nu, d31, V, r, with_bonding):
    # All units in SI (m, m^2/N, C/N, V)
    if with_bonding:
        C5 = sm * (1+nu) * (1 - (R2/R1)**2) * (hp*hb + hb**2)
        C6 = sb * (4*hm*hb + 2*hm**2 + hm*hp)
        C7 = 4 * (s11E**2) * (sb**2) * (hm**4)
        C8 = (sb**2)*(sm**2)*(hp**4) + s11E*sb*(sm**2)*(4*hp*hb**3 + 4*hp**3*hb + 6*hp**2*hb**2) + (s11E**2)*(sm**2)*(hb**4)
        C9 = s11E*(sb**2)*sm*(2*hp**3*hm + 2*hp*hm**3 + 6*hp**2*hb*hm + 6*hp*hb**2*hm + 6*hp*hb*hm**2 + 3*hp**2*hm**2) + (s11E**2)*sb*sm*(8*hb*hm**3 + 8*hb**3*hm + 12*hb**2*hm**2)
        denominator = C7 + (1+nu)**2 * (1 - (R2/R1)**2)**2 * C8 + 4*(1+nu)*(1 - (R2/R1)**2)*C9
        if r <= R2:
            omega = (3*(1+nu)*d31*s11E*sb*sm*(C5+C6) * ( (1 - (R2/R1)**2)*r**2 + 2*R2**2*math.log(R2/R1) ) * V) / denominator
        else:
            if r == 0:
                raise ValueError("r=0 but r>R2? shouldn't happen")
            omega = (3*(1+nu)*d31*s11E*sb*sm*(C5+C6) * ( 2*R2**2*math.log(r) - (R2**2/R1**2)*r**2 - 2*R2**2*math.log(R1) + R2**2 ) * V) / denominator
    else:
        C10 = 2*hm**2 + 2*hm*hp
        C11 = 4*s11E*hm**4
        C12 = sm**2 * hp**4
        C13 = s11E*sm*(2*hp**3*hm + 2*hp*hm**3 + 3*hp**2*hm**2)
        denominator = C11 + (1+nu)**2 * (1 - (R2/R1)**2)**2 * C12 + 4*(1+nu)*(1 - (R2/R1)**2)*C13
        if r <= R2:
            omega = (3*(1+nu)*d31*s11E*sm*C10 * ( (1 - (R2/R1)**2)*r**2 + 2*R2**2*math.log(R2/R1) ) * V) / denominator
        else:
            omega = (3*(1+nu)*d31*s11E*sm*C10 * ( 2*R2**2*math.log(r) - (R2**2/R1**2)*r**2 - 2*R2**2*math.log(R1) + R2**2 ) * V) / denominator
    return omega  # in meters

def generate_deflection_profile(outdir, filename, R1_m, R2_m, hp_m, hb_m, hm_m, s11E, sb, sm, nu, d31):
    voltages = [25, 50, 75, 100]
    r_values = [i*0.1 for i in range(0, 101)]  # 0 to 10 mm in mm, but compute in m
    r_m = [rv * 1e-3 for rv in r_values]  # convert to meters
    models_str = [('with_bonding', True), ('without_bonding', False)]
    rows = []
    for V in voltages:
        for model_str, with_bonding in models_str:
            for idx, rv_m in enumerate(r_m):
                omega_m = compute_deflection(R1_m, R2_m, hp_m, hb_m, hm_m, s11E, sb, sm, nu, d31, V, rv_m, with_bonding)
                omega_mm = omega_m * 1e3  # convert to mm
                rows.append([r_values[idx], V, model_str, omega_mm])
    filepath = os.path.join(outdir, filename)
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['r', 'voltage', 'model', 'deflection'])
        for row in rows:
            writer.writerow(row)

def generate_central_deflections(outdir, filename):
    # partial CPUA (Table 1)
    R1 = 0.01
    R2_p = 0.008
    hp_p = 0.2e-3
    hb_p = 0.025e-3
    # half CPUA (Table 2)
    R2_h = 0.005
    hp_h = 0.16e-3
    hb_h = 0.01e-3
    hm = 0.1e-3
    s11E = 1.82e-11
    sb = 1.934e-10
    sm = 1.01e-11
    nu = 0.31
    d31 = -270e-12
    voltages = [25, 50, 75, 100]
    rows = []
    for V in voltages:
        for cpu_type, R2, hp, hb in [('partial', R2_p, hp_p, hb_p), ('half', R2_h, hp_h, hb_h)]:
            for with_bonding in [True, False]:
                model_str = 'with_bonding' if with_bonding else 'without_bonding'
                r = 0.0
                omega_m = compute_deflection(R1, R2, hp, hb, hm, s11E, sb, sm, nu, d31, V, r, with_bonding)
                omega_mm = omega_m * 1e3
                rows.append([cpu_type, V, model_str, omega_mm])
    filepath = os.path.join(outdir, filename)
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['cpu_type', 'voltage', 'model', 'central_deflection'])
        for row in rows:
            writer.writerow(row)

if __name__ == '__main__':
    step = sys.argv[1]
    outdir = sys.argv[2]
    if step == 'step01':
        R1 = 0.01; R2 = 0.008; hp = 0.2e-3; hb = 0.025e-3; hm = 0.1e-3
        s11E = 1.82e-11; sb = 1.934e-10; sm = 1.01e-11; nu = 0.31; d31 = -270e-12
        filename = 'step_01_deflections_partial.csv'
        generate_deflection_profile(outdir, filename, R1, R2, hp, hb, hm, s11E, sb, sm, nu, d31)
    elif step == 'step02':
        R1 = 0.01; R2 = 0.005; hp = 0.16e-3; hb = 0.01e-3; hm = 0.1e-3
        s11E = 1.82e-11; sb = 1.934e-10; sm = 1.01e-11; nu = 0.31; d31 = -270e-12
        filename = 'step_02_deflections_half.csv'
        generate_deflection_profile(outdir, filename, R1, R2, hp, hb, hm, s11E, sb, sm, nu, d31)
    elif step == 'step03':
        filename = 'step_03_central_deflections.csv'
        generate_central_deflections(outdir, filename)
    else:
        print("Invalid step", file=sys.stderr)
        sys.exit(1)
