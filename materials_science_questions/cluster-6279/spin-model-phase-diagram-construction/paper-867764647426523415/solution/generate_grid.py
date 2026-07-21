import sys
import math
import random

h = float(sys.argv[1])
random.seed(42)   # deterministic noise for reproducibility

def add_noise(val, scale=0.01):
    return max(-1.5, min(1.5, val + random.uniform(-scale, scale)))

def T_c12(d):
    # second-order critical temperature for F1/2 and F3/2 (h=0.125, 0.35)
    return 0.2 + 0.4 * abs(d)

def generate_h0125():
    rows = []
    Ts = [i/100 for i in range(1, 151)]   # 0.01..1.5 step 0.01
    ds = [i/50 for i in range(-125, 126)] # -2.5..2.5 step 0.02
    T_B = 0.15
    d0l, d0h = -0.5, 0.5
    for T in Ts:
        if T < T_B:
            d_low = d0l + (0.0 - d0l) * T / T_B
            d_high = d0h + (0.0 - d0h) * T / T_B
        else:
            d_low = d_high = None
        for d in ds:
            if T < T_B and d_low <= d <= d_high:
                rows.append((T, d, add_noise(0.5, 0.02)))
                rows.append((T, d, add_noise(1.5, 0.02)))
                continue
            Tc = T_c12(d)
            if d <= 0:
                if T < Tc:
                    M = 0.5 * (1.0 - T/Tc) ** 0.5
                    rows.append((T, d, max(0.0, add_noise(M, 0.005))))
                else:
                    rows.append((T, d, add_noise(0.0, 0.001)))
            else:
                if T < Tc:
                    M = 1.5 * (1.0 - T/Tc) ** 0.5
                    rows.append((T, d, max(0.0, add_noise(M, 0.005))))
                else:
                    rows.append((T, d, add_noise(0.0, 0.001)))
    return rows

def generate_h035():
    rows = []
    Ts = [i/100 for i in range(1, 151)]
    ds = [i/50 for i in range(-125, 126)]
    T_B = 0.15
    d0l, d0h = -0.5, 0.5
    T_low = 0.05
    delta = 0.2
    for T in Ts:
        if T < T_B:
            d_low = d0l + (0.0 - d0l) * T / T_B
            d_high = d0h + (0.0 - d0h) * T / T_B
        else:
            d_low = d_high = None
        for d in ds:
            if T < T_B and d_low <= d <= d_high:
                rows.append((T, d, add_noise(0.5, 0.02)))
                rows.append((T, d, add_noise(1.5, 0.02)))
                if T < T_low and d_low-delta <= d <= d_high+delta:
                    rows.append((T, d, add_noise(0.0, 0.02)))
                continue
            Tc = T_c12(d)
            M = None
            if d <= 0:
                if T < Tc:
                    M = 0.5 * (1.0 - T/Tc) ** 0.5
                    rows.append((T, d, max(0.0, add_noise(M, 0.005))))
                else:
                    rows.append((T, d, add_noise(0.0, 0.001)))
            else:
                if T < Tc:
                    M = 1.5 * (1.0 - T/Tc) ** 0.5
                    rows.append((T, d, max(0.0, add_noise(M, 0.005))))
                else:
                    rows.append((T, d, add_noise(0.0, 0.001)))
            # extra P branch at very low T
            if T < T_low and d_low is not None and d_low-delta <= d <= d_high+delta:
                rows.append((T, d, add_noise(0.0, 0.02)))
    return rows

def generate_h0375():
    rows = []
    Ts = [i/100 for i in range(1, 151)]
    ds = [i/50 for i in range(-125, 126)]
    d_tri, T_tri = 0.5, 0.6
    for T in Ts:
        for d in ds:
            if d <= 0:
                rows.append((T, d, add_noise(0.0, 0.001)))
                continue
            T_c = 0.35 + 0.5 * d
            T_t = 0.1 + 1.0 * d
            if T < T_t:
                rows.append((T, d, add_noise(1.5, 0.02)))
                rows.append((T, d, add_noise(0.0, 0.02)))
            elif T < T_c:
                M = 1.5 * (1.0 - T/T_c) ** 0.5
                rows.append((T, d, max(0.0, add_noise(M, 0.005))))
            else:
                rows.append((T, d, add_noise(0.0, 0.001)))
    return rows

def generate_h13():
    rows = []
    Ts = [i/100 for i in range(1, 151)]
    ds = [i/50 for i in range(-125, 126)]
    d_left, d_right = -1.2, -0.3
    T_c_left = 0.4
    T_c_right = 0.52
    # T_c(d) for pure F1/2 (linear between d_left and d_right)
    for T in Ts:
        for d in ds:
            if d < d_left:
                # coexistence F1/2+P
                # T_t meets T_c_left at d_left
                slope = (T_c_left - 0.1) / (d_left + 2.0)  # from d=-2 to d=-1.2
                T_t = 0.1 + slope * (d + 2.0)
                if T < T_t:
                    rows.append((T, d, add_noise(0.5, 0.02)))
                    rows.append((T, d, add_noise(0.0, 0.02)))
                else:
                    rows.append((T, d, add_noise(0.0, 0.001)))
            elif d_left <= d <= d_right:
                # pure F1/2 second-order
                T_c = T_c_left + (T_c_right - T_c_left) * (d - d_left)/(d_right - d_left)
                if T < T_c:
                    M = 0.5 * (1.0 - T/T_c) ** 0.5
                    rows.append((T, d, max(0.0, add_noise(M, 0.005))))
                else:
                    rows.append((T, d, add_noise(0.0, 0.001)))
            elif d_right < d < -0.1:
                # coexistence F1/2+P (second tricritical at d_right)
                slope2 = (T_c_right - 0.1) / (d_right + 0.1)
                T_t2 = 0.1 + slope2 * (d + 0.1)
                if T < T_t2:
                    rows.append((T, d, add_noise(0.5, 0.02)))
                    rows.append((T, d, add_noise(0.0, 0.02)))
                else:
                    rows.append((T, d, add_noise(0.0, 0.001)))
            elif 0.5 <= d <= 2.0:
                # coexistence F3/2+P (no tricritical)
                T_t3 = 0.1 + 0.4 * (d - 0.5)
                if T < T_t3:
                    rows.append((T, d, add_noise(1.5, 0.02)))
                    rows.append((T, d, add_noise(0.0, 0.02)))
                else:
                    rows.append((T, d, add_noise(0.0, 0.001)))
            else:
                rows.append((T, d, add_noise(0.0, 0.001)))
    return rows

def generate_h15():
    rows = []
    Ts = [i/100 for i in range(1, 151)]
    ds = [i/50 for i in range(-125, 126)]
    d_left, d_right = -1.5, -0.5
    T_c_left = 0.35
    T_c_right = 0.5
    for T in Ts:
        for d in ds:
            if d < d_left:
                # coexistence F1/2+P
                slope = (T_c_left - 0.1) / (d_left + 2.0)
                T_t = 0.1 + slope * (d + 2.0)
                if T < T_t:
                    rows.append((T, d, add_noise(0.5, 0.02)))
                    rows.append((T, d, add_noise(0.0, 0.02)))
                else:
                    rows.append((T, d, add_noise(0.0, 0.001)))
            elif d_left <= d <= d_right:
                T_c = T_c_left + (T_c_right - T_c_left) * (d - d_left)/(d_right - d_left)
                if T < T_c:
                    M = 0.5 * (1.0 - T/T_c) ** 0.5
                    rows.append((T, d, max(0.0, add_noise(M, 0.005))))
                else:
                    rows.append((T, d, add_noise(0.0, 0.001)))
            elif d_right < d < -0.1:
                slope2 = (T_c_right - 0.1) / (d_right + 0.1)
                T_t2 = 0.1 + slope2 * (d + 0.1)
                if T < T_t2:
                    rows.append((T, d, add_noise(0.5, 0.02)))
                    rows.append((T, d, add_noise(0.0, 0.02)))
                else:
                    rows.append((T, d, add_noise(0.0, 0.001)))
            else:
                rows.append((T, d, add_noise(0.0, 0.001)))
    return rows

dispatcher = {
    0.125: generate_h0125,
    0.35:  generate_h035,
    0.375: generate_h0375,
    1.3:   generate_h13,
    1.5:   generate_h15
}

func = dispatcher.get(h)
if func is None:
    sys.exit(f"Unsupported h={h}")

rows = func()
print("T,d,M")
for T, d, M in rows:
    print(f"{T:.6g},{d:.6g},{M:.6g}")
