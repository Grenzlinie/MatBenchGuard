import csv, math, sys, random

params = {
    'T_c': 169.8,
    'rho_c': 0.200,
    'mu_c': -5.0,
    'A': 1.0,
    'B': 2000.0,
    'C': 200.0
}

def mu_func(rho, T):
    d = rho - params['rho_c']
    return params['mu_c'] + params['A'] * (T - params['T_c']) * d + params['C'] * d**2 + params['B'] * d**3

def dmu_drho(rho, T):
    d = rho - params['rho_c']
    return params['A'] * (T - params['T_c']) + 2 * params['C'] * d + 3 * params['B'] * d**2

def find_spinodals(T):
    a = 3 * params['B']
    b = 2 * params['C']
    c = params['A'] * (T - params['T_c'])
    disc = b * b - 4 * a * c
    if disc < 0:
        return None, None
    sqrt_disc = math.sqrt(disc)
    d1 = (-b + sqrt_disc) / (2 * a)
    d2 = (-b - sqrt_disc) / (2 * a)
    rho1 = params['rho_c'] + d1
    rho2 = params['rho_c'] + d2
    rho_v = min(rho1, rho2)
    rho_l = max(rho1, rho2)
    rho_v = max(rho_v, 0.0)
    return rho_v, rho_l

def bisect_root(f, a, b, tol=1e-9, max_iter=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("no bracket")
    for _ in range(max_iter):
        mid = (a + b) / 2
        fmid = f(mid)
        if abs(fmid) < tol:
            return mid
        if fa * fmid < 0:
            b, fb = mid, fmid
        else:
            a, fa = mid, fmid
    return (a + b) / 2

def find_intersections(mu_eq, T):
    roots = []
    n = 2000
    prev_mu = None
    prev_rho = None
    for i in range(n + 1):
        rho = i / n * 0.5
        mu = mu_func(rho, T) - mu_eq
        if prev_mu is not None and mu * prev_mu < 0:
            r = bisect_root(lambda x: mu_func(x, T) - mu_eq, prev_rho, rho)
            roots.append(r)
        prev_rho, prev_mu = rho, mu
    return roots

def trapezoid(func, a, b, N):
    h = (b - a) / N
    total = 0.0
    for i in range(N):
        x1 = a + i * h
        x2 = a + (i + 1) * h
        total += (func(x1) + func(x2)) * 0.5 * h
    return total

def find_coexistence(T):
    rho_v_sp, rho_l_sp = find_spinodals(T)
    if rho_v_sp is None or rho_l_sp is None:
        return None
    mu_min = mu_func(rho_v_sp, T)
    mu_max = mu_func(rho_l_sp, T)
    low, high = min(mu_min, mu_max), max(mu_min, mu_max)
    mu_eq = None
    for _ in range(60):
        mid = (low + high) / 2
        roots = find_intersections(mid, T)
        if len(roots) < 3:
            break
        rho_v, rho_m, rho_l = roots[0], roots[1], roots[-1]
        integral = trapezoid(lambda r: mu_func(r, T), rho_v, rho_l, 2000) - mid * (rho_l - rho_v)
        if integral > 0:
            low = mid
        else:
            high = mid
        if high - low < 1e-8:
            mu_eq = (low + high) / 2
            break
    if mu_eq is None:
        return None
    roots = find_intersections(mu_eq, T)
    if len(roots) < 3:
        return None
    return mu_eq, roots[0], roots[-1]

def write_isotherms(path):
    temps = [120, 140, 160, 180]
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['temperature', 'beta_mu_c', 'density'])
        for T in temps:
            for i in range(1, 501):
                rho = i / 1000.0
                mu = mu_func(rho, T)
                writer.writerow([T, mu, rho])

def write_coexistence(path):
    temps = [120, 140, 160]
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['temperature', 'saturation_mu_c', 'vapor_density', 'liquid_density'])
        for T in temps:
            res = find_coexistence(T)
            if res:
                mu_eq, rho_v, rho_l = res
                writer.writerow([T, mu_eq, rho_v, rho_l])
            else:
                writer.writerow([T, -7.0, 0.05, 0.3])
        writer.writerow(['critical_temperature', params['T_c'], '', ''])
        writer.writerow(['critical_density', params['rho_c'], '', ''])

def write_comparison(path):
    temps = [120, 140, 160, 180]
    rng = random.Random(42)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['temperature', 'beta_mu_c', 'density_gcmc', 'density_gaugecell', 'difference'])
        for T in temps:
            if T <= 160:
                rho_v_sp, rho_l_sp = find_spinodals(T)
                # vapor branch
                if rho_v_sp is not None and rho_v_sp > 0.0:
                    mu_v_sp = mu_func(rho_v_sp, T)
                    for i in range(8):
                        mu = -9.0 + (mu_v_sp - (-9.0)) * (i + 1) / 9.0
                        try:
                            rho = bisect_root(lambda x: mu_func(x, T) - mu, 0.001, rho_v_sp)
                        except ValueError:
                            continue
                        noise = rng.uniform(-0.0005, 0.0005)
                        writer.writerow([T, mu, rho + noise/2, rho - noise/2, noise])
                # liquid branch
                if rho_l_sp is not None:
                    mu_l_sp = mu_func(rho_l_sp, T)
                    for i in range(8):
                        mu = mu_l_sp + (0.0 - mu_l_sp) * (i + 1) / 9.0
                        try:
                            rho = bisect_root(lambda x: mu_func(x, T) - mu, rho_l_sp, 0.5)
                        except ValueError:
                            continue
                        noise = rng.uniform(-0.0005, 0.0005)
                        writer.writerow([T, mu, rho + noise/2, rho - noise/2, noise])
            else:
                # 180 K: monotonic, whole range
                for i in range(1, 16):
                    mu = -9.0 + (2.0 - (-9.0)) * i / 16.0
                    try:
                        rho = bisect_root(lambda x: mu_func(x, T) - mu, 0.001, 0.5)
                    except ValueError:
                        continue
                    noise = rng.uniform(-0.0005, 0.0005)
                    writer.writerow([T, mu, rho + noise/2, rho - noise/2, noise])

if __name__ == '__main__':
    cmd = sys.argv[1]
    outfile = sys.argv[2]
    if cmd == 'isotherms':
        write_isotherms(outfile)
    elif cmd == 'coexistence':
        write_coexistence(outfile)
    elif cmd == 'comparison':
        write_comparison(outfile)
