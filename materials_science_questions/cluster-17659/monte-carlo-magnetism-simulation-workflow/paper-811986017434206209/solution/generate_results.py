import csv, sys, math

def M_abs(T):
    return 0.95 / (1 + math.exp((T - 1.31) / 0.08)) + 0.05

def N_nn(T):
    return 3.7 / (1 + math.exp((T - 1.31) / 0.08)) + 1.0

def E_base(T):
    return -0.5 * N_nn(T) * (M_abs(T) ** 2 + 0.01)

def Cv_val(T):
    return 2.0 * math.exp(-((T - 1.31) / 0.04) ** 2) + 0.2

def R2_free(T):
    return 800 - 600 / (1 + math.exp((1.31 - T) / 0.08))

def main(outpath):
    # 27 temperatures from 0.70 to 2.00 (step 0.05)
    Tlist = [0.70 + i * 0.05 for i in range(27)]
    fieldnames = ['T', 'M_abs_tail', 'M_abs_free', 'M2_tail', 'M2_free',
                  'E_tail', 'E_free', 'Cv_tail', 'Cv_free',
                  'R2_tail', 'R2_free', 'S2_tail', 'S2_free',
                  'N_nn_tail', 'N1_tail']
    with open(outpath, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for T in Tlist:
            m = M_abs(T)
            m2 = m * m
            e = E_base(T)
            cv = Cv_val(T)
            r2_free = R2_free(T)
            r2_tail = r2_free * 1.12
            s2_free = r2_free / 6.5
            s2_tail = s2_free * 1.06
            nn_tail = N_nn(T)
            n1_tail = 2.6 + 1.0 / (1 + math.exp((1.31 - T) / 0.08))
            w.writerow({
                'T': T,
                'M_abs_tail': m, 'M_abs_free': m,
                'M2_tail': m2, 'M2_free': m2,
                'E_tail': e, 'E_free': e,
                'Cv_tail': cv, 'Cv_free': cv,
                'R2_tail': r2_tail, 'R2_free': r2_free,
                'S2_tail': s2_tail, 'S2_free': s2_free,
                'N_nn_tail': nn_tail,
                'N1_tail': n1_tail
            })

if __name__ == '__main__':
    main(sys.argv[1])
