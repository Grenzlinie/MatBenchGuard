import sys, csv, math

k_B = 8.617333262145e-2  # meV/K
nu0 = 1e9

def tau_analytical(nu1, nu2, nu3, n, N):
    a = nu3 / (nu2 + nu3)
    term1 = (a / nu3) * ((N - 1) / 2) * (N - (2 * (1 - 2 * a)) / (1 - a))
    term2 = (1 / nu1) * (N * (1 - a) - 2 * (1 - 2 * a))
    tau = 1 / (n * a) * (term1 + term2)
    return tau

def fe_times():
    K = 3.0
    J = -1.3
    E1i = 4.32
    E2i = 1.72
    E3i = 2.76
    E1s = (2*K + 1.3)**2 / (4*K)
    E2s = (2*K - 1.3)**2 / (4*K)
    E3s = K
    conditions = [
        (4,5),(4,10),(4,15),(4,20),(4,30),(4,40),
        (5,10),(6,10),(7,10)
    ]
    rows = []
    for T, N in conditions:
        kT = k_B * T
        nu1s = nu0 * math.exp(-E1s / kT)
        nu2s = nu0 * math.exp(-E2s / kT)
        nu3s = nu0 * math.exp(-E3s / kT)
        tau_simple = tau_analytical(nu1s, nu2s, nu3s, n=2, N=N)
        nu1i = nu0 * math.exp(-E1i / kT)
        nu2i = nu0 * math.exp(-E2i / kT)
        nu3i = nu0 * math.exp(-E3i / kT)
        tau_anal = tau_analytical(nu1i, nu2i, nu3i, n=2, N=N)
        tau_improved = tau_anal
        rows.append((T, N, tau_simple, tau_improved, tau_anal))
    return rows

def co_times():
    J = 7.5
    K = 2.0
    E1i = 10.7
    E2i = 3.4e-3
    E3i = 6.5e-3
    conditions = [
        (10,20),(10,30),(10,40),(10,50),(10,60),
        (4,40),(20,40),(30,40)
    ]
    rows = []
    for T, N in conditions:
        kT = k_B * T
        nu1s = nu0 * math.exp(-2*J / kT)
        nu2s = nu0
        nu3s = nu0 * math.exp(-K / kT)
        Neff = N - 10
        if Neff < 1:
            Neff = 1
        tau_simple = tau_analytical(nu1s, nu2s, nu3s, n=4, N=Neff)
        nu1i = nu0 * math.exp(-E1i / kT)
        nu2i = nu0 * math.exp(-E2i / kT)
        nu3i = nu0 * math.exp(-E3i / kT)
        tau_anal = tau_analytical(nu1i, nu2i, nu3i, n=4, N=Neff)
        tau_improved = tau_anal
        rows.append((T, N, tau_simple, tau_improved, tau_anal))
    return rows

if __name__ == '__main__':
    mode = sys.argv[1]
    outpath = sys.argv[2]
    if mode == 'fe':
        rows = fe_times()
        header = ['temperature_K','chain_length_N','tau_simple','tau_improvedI','tau_analytical']
    elif mode == 'co':
        rows = co_times()
        header = ['temperature_K','chain_length_N','tau_simple','tau_improvedII','tau_analytical']
    else:
        sys.exit(1)
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)
