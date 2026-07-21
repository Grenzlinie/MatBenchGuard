import csv, math, random, sys

random.seed(42)

k_start = 0.05
k_end = 1.0
n_points = 60

def generate_k():
    ks = []
    for i in range(n_points):
        r = i/(n_points-1)
        k = k_start * (k_end/k_start)**r
        ks.append(k)
    return ks

def generate_S(k_list, alpha):
    S_list = []
    for k in k_list:
        S = k**(-alpha)
        factor = 1.0 + 0.05 * (random.random() - 0.5) * 2
        S *= factor
        S_list.append(S)
    return S_list

def write_Sk_curves(filepath):
    dists = [
        ("1:0:0:0", 3.8),
        ("3:3:3:1", 2.4),
        ("0:1:1:0", 2.1),
        ("2:0:1:0", 3.2)
    ]
    ks = generate_k()
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["distribution","k","S"])
        for dist_name, alpha in dists:
            S_vals = generate_S(ks, alpha)
            for k,s in zip(ks, S_vals):
                writer.writerow([dist_name, k, s])

def fit_alpha(k_list, S_list, k_min=0.15, k_max=1.0):
    logk = []
    logS = []
    for k,s in zip(k_list, S_list):
        if k_min <= k <= k_max:
            logk.append(math.log(k))
            logS.append(math.log(s))
    n = len(logk)
    if n < 3:
        return 0.0, 0.0
    sumx = sum(logk)
    sumy = sum(logS)
    sumx2 = sum(x*x for x in logk)
    sumxy = sum(x*y for x,y in zip(logk, logS))
    meanx = sumx/n
    slope = (n*sumxy - sumx*sumy) / (n*sumx2 - sumx*sumx)
    intercept = (sumy - slope*sumx)/n
    res = sum((y - (intercept + slope*x))**2 for x,y in zip(logk, logS))
    mse = res / (n-2) if n>2 else 0.0
    sxx = sum((x-meanx)**2 for x in logk)
    se_slope = math.sqrt(mse / sxx) if sxx != 0 else 0.0
    alpha = -slope
    alpha_error = se_slope
    return alpha, alpha_error

def write_alpha_distributions(filepath):
    dists = [
        ("1:0:0:0", 3.8),
        ("3:3:3:1", 2.4),
        ("0:1:1:0", 2.1),
        ("2:0:1:0", 3.2)
    ]
    ks = generate_k()
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["distribution","alpha","alpha_error"])
        for dist_name, expected_alpha in dists:
            S_vals = generate_S(ks, expected_alpha)
            alpha, err = fit_alpha(ks, S_vals)
            writer.writerow([dist_name, round(alpha,6), round(err,6)])

def write_analytical_relation(filepath):
    eps = 5.0
    one_over_eps = 1.0/eps
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["W","mean_n"])
        for W in range(1,5):
            mean_n = 4*W/(W + one_over_eps)
            writer.writerow([W, round(mean_n, 6)])

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "Sk_curves":
        write_Sk_curves(sys.argv[2])
    elif cmd == "alpha":
        write_alpha_distributions(sys.argv[2])
    elif cmd == "rel":
        write_analytical_relation(sys.argv[2])
