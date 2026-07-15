#!/usr/bin/env python3
import sys, csv, math

# Volume polynomial coefficients from Table 1
a0 = 59.72
a1 = -0.36
a2 = 0.00374   # a2 x10^-3 = 3.74 -> a2 = 3.74e-3
V0 = a0

# Raman modes: (name, b0, b1, b2, a_cal, b_cal, c_raw_table)
# b0,b1,b2 from Table 2; a_cal,b_cal,c_raw_table from Table 3; c_raw_table is in units of 10^-3 (cm)
modes = [
    ("E(1TO)",      85.2,   -4.36,   -0.14,  21.20,   0.88,   -1.86),
    ("A1(1TO)",    117.4,   -1.54,   -0.51,  38.78,   0.95,   -2.65),
    ("E(2TO)",     208.9,   -6.28,    0.37, 257.88,  -2.10,    9.03),
    ("A1(2TO)",    361.6,  -16.97,    0.12, 114.77,   0.423,   0.71),
    ("B1+E",       289.5,   -1.45,  -0.007, 592.08,  -3.06,    6.97),
    ("E(3TO)",     496.2,    7.41,  -0.008, -145.59,  1.56,   -0.54),
    ("A1(3TO)",    626.4,  -15.01,    0.95, -6910.74, 23.21, -17.85),
    ("E(3LO)",     749.5,   -2.19,    0.37, 1653.86, -2.62,    1.88),
]

def V(P):
    return a0 + a1*P + a2*P*P

def v_mode(b0, b1, b2, P):
    return b0 + b1*P + b2*P*P

def gamma_T(b0, b1, b2, P):
    v = v_mode(b0, b1, b2, P)
    dv = b1 + 2*b2*P
    dV = a1 + 2*a2*P
    return (dv / v) * (V(P) / dV)

def raw_freq(b0, b1, b2, P):
    v0 = b0
    g = gamma_T(b0, b1, b2, P)
    return v0 * math.exp(-g * math.log(V(P) / V0))

def calibrated_freq(b0, b1, b2, a_cal, b_cal, c_raw, P):
    c = c_raw * 1e-3   # actual quadratic calibration coefficient
    v_raw = raw_freq(b0, b1, b2, P)
    return a_cal + b_cal * v_raw + c * v_raw * v_raw

def main():
    if len(sys.argv) != 3 or sys.argv[1] != '--output':
        print("Usage: gen_outputs.py --output [gamma|frequency]", file=sys.stderr)
        sys.exit(1)
    out_type = sys.argv[2]

    # Pressure range 0 to 12 GPa, step 0.5 GPa
    pressures = [i * 0.5 for i in range(0, 25)]   # 0, 0.5, ..., 12.0

    if out_type == "gamma":
        outfile = "/app/outputs/gruneisen_parameters.csv"
        with open(outfile, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["mode", "pressure_GPa", "gamma_T"])
            for (name, b0, b1, b2, *_) in modes:
                for P in pressures:
                    g = gamma_T(b0, b1, b2, P)
                    writer.writerow([name, P, g])
    elif out_type == "frequency":
        outfile = "/app/outputs/computed_raman_frequencies.csv"
        with open(outfile, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["mode", "pressure_GPa", "frequency_cm1"])
            for (name, b0, b1, b2, a_cal, b_cal, c_raw) in modes:
                for P in pressures:
                    freq = calibrated_freq(b0, b1, b2, a_cal, b_cal, c_raw, P)
                    writer.writerow([name, P, freq])
    else:
        print("Unknown output type. Use gamma or frequency.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
