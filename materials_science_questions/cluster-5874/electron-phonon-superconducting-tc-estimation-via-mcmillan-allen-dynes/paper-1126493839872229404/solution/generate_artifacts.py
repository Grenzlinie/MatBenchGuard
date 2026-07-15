import sys, os, csv, math

def gen_specific_heat(filepath):
    a = 0.5
    b = 0.02
    Ts = range(1, 21)  # 1 to 20 K
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T', 'CV_T'])
        for T in Ts:
            cv_t = a/T + b*T**2
            writer.writerow([T, cv_t])

def gen_impurity_spectral(filepath):
    def lorentz(x, x0, gamma, amp):
        return amp * gamma**2 / ((x-x0)**2 + gamma**2)
    omegas = [-2.0 + i*0.02 for i in range(201)]  # -2 to 2 eV, step 0.02 -> 201 points
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['omega', 'A_d'])
        for w in omegas:
            val = (lorentz(w, -0.5, 0.05, 1.0) +
                   lorentz(w, 0.5, 0.05, 1.0) +
                   lorentz(w, -1.0, 0.3, 0.3) +
                   lorentz(w, 1.0, 0.3, 0.3))
            writer.writerow([w, val])

def gen_thermal_conductivity(filepath):
    Ts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]  # at least 8 points
    C = 1.0
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T', 'kappa_f'])
        for T in Ts:
            kappa = C / (T**2)
            writer.writerow([T, kappa])

if __name__ == '__main__':
    basename = os.path.basename(sys.argv[1])
    if 'specific_heat' in basename:
        gen_specific_heat(sys.argv[1])
    elif 'impurity_spectral' in basename:
        gen_impurity_spectral(sys.argv[1])
    elif 'thermal_conductivity' in basename:
        gen_thermal_conductivity(sys.argv[1])
    else:
        raise ValueError(f'Unknown output file: {basename}')
