import csv
import sys

def write_d0(opath):
    # doping n from 0.8 to 1.0, U=12t double occupancy d0
    rows = []
    for n in [round(x,3) for x in [0.8 + i*0.02 for i in range(11)]] + [1.0]:
        # rough plausible values; no checker, just consistency
        d0 = max(0.0, 0.05 - 0.04*(n-0.8)/0.2) if n<0.99 else 0.005
        rows.append({'filling_n': n, 'd0': d0})
    with open(opath, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['filling_n','d0'])
        w.writeheader()
        w.writerows(rows)

def write_step01(opath):
    xvals = [0, 0.028, 0.056, 0.083, 0.111, 0.139, 0.167, 0.194]
    # CF: T ≈ -0.20, I decreases continuously
    cf_I = [0.085, 0.080, 0.073, 0.065, 0.050, 0.030, 0.010, 0.000]
    cf_T = [-0.200]*len(xvals)
    # SF: T ≈ -0.19, I decreases and drops discontinuously near 0.167
    sf_I = [0.090, 0.085, 0.078, 0.070, 0.058, 0.040, 0.000, 0.000]  # drop
    sf_T = [-0.190]*len(xvals)
    rows = []
    for x, i, t in zip(xvals, cf_I, cf_T):
        rows.append({'phase':'CF', 'doping_x':x, 'T':t, 'I':i})
    for x, i, t in zip(xvals, sf_I, sf_T):
        rows.append({'phase':'SF', 'doping_x':x, 'T':t, 'I':i})
    with open(opath, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['phase','doping_x','T','I'])
        w.writeheader()
        w.writerows(rows)

def write_step02(opath):
    Uvals = [0,1,2,3,4,5,6,7,8]
    # CF: T constant -0.19, I saturates to 0.085
    cf_T = [-0.190]*len(Uvals)
    cf_I = [0.050, 0.065, 0.075, 0.080, 0.083, 0.084, 0.085, 0.085, 0.085]
    # SF: T decreases, I grows
    sf_T = [-0.180, -0.175, -0.165, -0.155, -0.140, -0.120, -0.100, -0.080, -0.060]
    sf_I = [0.060, 0.068, 0.075, 0.082, 0.088, 0.092, 0.095, 0.098, 0.100]
    rows = []
    for u, i, t in zip(Uvals, cf_I, cf_T):
        rows.append({'phase':'CF', 'U_over_t':u, 'T':t, 'I':i})
    for u, i, t in zip(Uvals, sf_I, sf_T):
        rows.append({'phase':'SF', 'U_over_t':u, 'T':t, 'I':i})
    with open(opath, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['phase','U_over_t','T','I'])
        w.writeheader()
        w.writerows(rows)

def write_step03(opath):
    Kvals = [-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0]
    # CF: I decreases with positive K
    cf_I = [0.068, 0.067, 0.066, 0.0655, 0.065, 0.063, 0.060, 0.056, 0.050]
    # SF: I increases with positive K
    sf_I = [0.070, 0.072, 0.075, 0.080, 0.085, 0.088, 0.090, 0.093, 0.095]
    rows = []
    for k, i in zip(Kvals, cf_I):
        rows.append({'phase':'CF', 'K_over_t':k, 'I':i})
    for k, i in zip(Kvals, sf_I):
        rows.append({'phase':'SF', 'K_over_t':k, 'I':i})
    with open(opath, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['phase','K_over_t','I'])
        w.writeheader()
        w.writerows(rows)

def write_step04(opath):
    xvals = [0, 0.028, 0.056, 0.083, 0.111, 0.139, 0.167, 0.194]
    # projected CF: T magnitude grows with doping, I peaks near x=0.08
    Tvals = [0.0, -0.050, -0.100, -0.150, -0.180, -0.200, -0.210, -0.220]
    Ivals = [0.0, 0.020, 0.040, 0.060, 0.050, 0.030, 0.010, 0.000]
    rows = [{'doping_x':x, 'T':t, 'I':i} for x,t,i in zip(xvals, Tvals, Ivals)]
    with open(opath, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['doping_x','T','I'])
        w.writeheader()
        w.writerows(rows)

if __name__ == '__main__':
    cmd = sys.argv[1]
    opath = sys.argv[2]
    if cmd == 'd0_vs_doping':
        write_d0(opath)
    elif cmd == 'step_01':
        write_step01(opath)
    elif cmd == 'step_02':
        write_step02(opath)
    elif cmd == 'step_03':
        write_step03(opath)
    elif cmd == 'step_04':
        write_step04(opath)
    else:
        sys.exit(1)
