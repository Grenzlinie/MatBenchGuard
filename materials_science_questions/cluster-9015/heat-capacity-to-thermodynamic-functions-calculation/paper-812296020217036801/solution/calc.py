import sys
import numpy as np

def main():
    mode = sys.argv[2]
    outpath = sys.argv[4]
    
    if mode == 'tdv':
        produce_tdv(outpath)
    elif mode == 'exact':
        produce_exact(outpath)
    elif mode == 'noisy':
        produce_noisy(outpath)
    elif mode == 'recover':
        produce_recover(outpath)
    else:
        raise ValueError(f"Unknown mode {mode}")

def K1(T):
    return 1.0 / T

def K2(T, theta=298.15):
    return theta/T + np.log(T/theta) - 1

def K3(T, theta=298.15):
    return T/2 - theta**2/(2*T) - theta*np.log(T/theta)

def K4(T, theta=298.15):
    return T**2/6 + theta**2*(0.5 - np.log(T/theta)) - 2*theta**3/(3*T)

def compute_RlnK(T, params):
    dS, dH, dCp, db, dc = params
    k1 = K1(T)
    k2 = K2(T)
    k3 = K3(T)
    k4 = K4(T)
    return dS - dH*k1 + dCp*k2 + db*k3 + dc*k4

def create_temp_arrays():
    temp_C = np.arange(0, 105, 5)
    temp_K = temp_C + 273.15
    return temp_C, temp_K

def produce_tdv(outpath):
    temp_C, temp_K = create_temp_arrays()
    k1 = K1(temp_K)
    k2 = K2(temp_K)
    k3 = K3(temp_K)
    k4 = K4(temp_K)
    
    # Intervals: 20°C steps
    start_temps = [0,20,40,60,80]
    end_temps   = [20,40,60,80,100]
    interval_labels = []
    delta_K1 = []
    xs, ys = [], []
    
    for s, e in zip(start_temps, end_temps):
        i = np.where(temp_C == s)[0][0]
        j = np.where(temp_C == e)[0][0]
        dK1 = k1[j] - k1[i]
        dK2 = k2[j] - k2[i]
        dK3 = k3[j] - k3[i]
        dK4 = k4[j] - k4[i]
        ratio_2_1 = dK2 / dK1
        ratio_3_1 = dK3 / dK1
        ratio_4_1 = dK4 / dK1
        interval_labels.append(f"{s}-{e}")
        delta_K1.append(dK1)
        xs.append(ratio_3_1)
        ys.append(ratio_4_1)
    
    # Now second differences for x, y pairs (for Z diagnostics)
    # But the step says compute auxiliary variables x,y for each interval pair.
    # We'll output the given interval parameters: interval, ΔK1, x (Δ(ΔK3/ΔK1)/Δ(ΔK2/ΔK1)) and y similar.
    # Actually the method of intervals uses these x,y for the second-difference pairs.
    # We'll compute them for each adjacent pair:
    pair_labels = []
    pair_x = []
    pair_y = []
    for idx in range(len(ratio_2_1)-1):
        d_ratio2 = ratio_2_1[idx+1] - ratio_2_1[idx]
        d_ratio3 = ratio_3_1[idx+1] - ratio_3_1[idx]
        d_ratio4 = ratio_4_1[idx+1] - ratio_4_1[idx]
        pair_labels.append(f"{start_temps[idx]}-{end_temps[idx]} vs {start_temps[idx+1]}-{end_temps[idx+1]}")
        pair_x.append(d_ratio3 / d_ratio2)
        pair_y.append(d_ratio4 / d_ratio2)
    
    # Write combined CSV
    with open(outpath, 'w') as f:
        f.write("type,label,temp_C,K1,K2,K3,K4,Delta_K1,x,y\n")
        # temperature rows
        for i in range(len(temp_C)):
            f.write(f"temperature,,{temp_C[i]},{k1[i]:.10f},{k2[i]:.10f},{k3[i]:.10f},{k4[i]:.10f},,,,\n")
        # interval rows (first-level)
        for i in range(len(interval_labels)):
            f.write(f"interval_20C,{interval_labels[i]},,,,,,{delta_K1[i]:.10f},{xs[i]:.10f},{ys[i]:.10f}\n")
        # pair rows
        for i in range(len(pair_labels)):
            f.write(f"pair,{pair_labels[i]},,,,,,,{pair_x[i]:.10f},{pair_y[i]:.10f}\n")

def produce_exact(outpath):
    params_A = (-20.0, -1000.0, -15.0, 4.0, -0.0055)
    params_B = (-20.0, 0.0, -15.0, 0.6, -0.0008)
    temp_C, temp_K = create_temp_arrays()
    with open(outpath, 'w') as f:
        f.write("set,temp_C,RlnK\n")
        for tC, tK in zip(temp_C, temp_K):
            rlnk_A = compute_RlnK(tK, params_A)
            rlnk_B = compute_RlnK(tK, params_B)
            f.write(f"A,{tC},{rlnk_A:.10f}\n")
            f.write(f"B,{tC},{rlnk_B:.10f}\n")

def add_noise_exact(outpath):
    params_A = (-20.0, -1000.0, -15.0, 4.0, -0.0055)
    params_B = (-20.0, 0.0, -15.0, 0.6, -0.0008)
    temp_C, temp_K = create_temp_arrays()
    np.random.seed(42)
    noises_A = []
    noises_B = []
    # Pre-generate noises
    for tC, tK in zip(temp_C, temp_K):
        rlnk_A = compute_RlnK(tK, params_A)
        rlnk_B = compute_RlnK(tK, params_B)
        noises_A.append(np.random.normal(0, abs(rlnk_A)/1500))
        noises_B.append(np.random.normal(0, abs(rlnk_B)/1500))
    # Reset seed to same for deterministic get_rlnk
    np.random.seed(42)
    with open(outpath, 'w') as f:
        f.write("set,temp_C,RlnK_noisy\n")
        for i, (tC, tK) in enumerate(zip(temp_C, temp_K)):
            # recompute exact for consistency (not needed but safe)
            rlnk_A = compute_RlnK(tK, params_A) + noises_A[i]
            rlnk_B = compute_RlnK(tK, params_B) + noises_B[i]
            f.write(f"A,{tC},{rlnk_A:.10f}\n")
            f.write(f"B,{tC},{rlnk_B:.10f}\n")

def produce_noisy(outpath):
    # same as add_noise_exact but writing noisy only
    add_noise_exact(outpath)

def produce_recover(outpath):
    params_A = (-20.0, -1000.0, -15.0, 4.0, -0.0055)
    params_B = (-20.0, 0.0, -15.0, 0.6, -0.0008)
    temp_C, temp_K = create_temp_arrays()
    
    # Generate noisy data with seed 42 (same as in produce_noisy)
    np.random.seed(42)
    noisy_A = []
    noisy_B = []
    for tK in temp_K:
        rlnk_A = compute_RlnK(tK, params_A)
        rlnk_B = compute_RlnK(tK, params_B)
        noisy_A.append(rlnk_A + np.random.normal(0, abs(rlnk_A)/1500))
        noisy_B.append(rlnk_B + np.random.normal(0, abs(rlnk_B)/1500))
    noisy_A = np.array(noisy_A)
    noisy_B = np.array(noisy_B)
    
    # Method of intervals recovery
    result = []
    for set_name, noisy in [('A', noisy_A), ('B', noisy_B)]:
        # Compute interval ratios
        intervals = [(0,20),(20,40),(40,60),(60,80),(80,100)]
        ratios = []
        DeltaK2_over_DeltaK1 = []
        DeltaK3_over_DeltaK1 = []
        DeltaK4_over_DeltaK1 = []
        for (s,e) in intervals:
            i = np.where(temp_C == s)[0][0]
            j = np.where(temp_C == e)[0][0]
            dR = noisy[j] - noisy[i]
            dK1 = K1(temp_K[j]) - K1(temp_K[i])
            dK2 = K2(temp_K[j]) - K2(temp_K[i])
            dK3 = K3(temp_K[j]) - K3(temp_K[i])
            dK4 = K4(temp_K[j]) - K4(temp_K[i])
            ratios.append(dR / dK1)
            DeltaK2_over_DeltaK1.append(dK2 / dK1)
            DeltaK3_over_DeltaK1.append(dK3 / dK1)
            DeltaK4_over_DeltaK1.append(dK4 / dK1)
        ratios = np.array(ratios)
        DeltaK2_over_DeltaK1 = np.array(DeltaK2_over_DeltaK1)
        DeltaK3_over_DeltaK1 = np.array(DeltaK3_over_DeltaK1)
        DeltaK4_over_DeltaK1 = np.array(DeltaK4_over_DeltaK1)
        
        # Second differences to form Z, x, y
        d_ratio = np.diff(ratios)
        d_K2ratio = np.diff(DeltaK2_over_DeltaK1)
        Z = d_ratio / d_K2ratio
        x = np.diff(DeltaK3_over_DeltaK1) / d_K2ratio
        y = np.diff(DeltaK4_over_DeltaK1) / d_K2ratio
        
        # Fit Z = DeltaCp + Delta_b * x + Delta_c * y
        A_fit = np.column_stack([np.ones(len(x)), x, y])
        betas, _, _, _ = np.linalg.lstsq(A_fit, Z, rcond=None)
        DeltaCp_fit = betas[0]
        Delta_b_fit = betas[1]
        Delta_c_fit = betas[2]
        
        # Correct R ln K
        RlnK_corrected = noisy - (DeltaCp_fit * K2(temp_K) + Delta_b_fit * K3(temp_K) + Delta_c_fit * K4(temp_K))
        # Fit RlnK' = DeltaS - DeltaH * K1
        X_fit = np.column_stack([np.ones(len(temp_K)), K1(temp_K)])
        betas2, _, _, _ = np.linalg.lstsq(X_fit, RlnK_corrected, rcond=None)
        DeltaS_fit = betas2[0]
        DeltaH_fit = -betas2[1]  # because K1 coefficient is -DeltaH
        
        result.append((set_name, DeltaS_fit, DeltaH_fit, DeltaCp_fit, Delta_b_fit, Delta_c_fit))
    
    with open(outpath, 'w') as f:
        f.write("set,DeltaS,DeltaH,DeltaCp,Delta_b,Delta_c\n")
        for row in result:
            f.write(f"{row[0]},{row[1]:.10f},{row[2]:.10f},{row[3]:.10f},{row[4]:.10f},{row[5]:.10f}\n")

if __name__ == "__main__":
    main()
