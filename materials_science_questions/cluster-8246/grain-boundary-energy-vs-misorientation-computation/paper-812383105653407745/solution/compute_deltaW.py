import csv, sys, math

def delta_W(G, nu, gamma, b, n, L, alpha_deg, f, N):
    alpha_rad = math.radians(alpha_deg)
    alpha2 = alpha_rad / 2.0
    sin_alpha2 = math.sin(alpha2)
    cos_alpha2 = math.cos(alpha2)
    sin_alpha = math.sin(alpha_rad)
    D = G / (2 * math.pi * (1 - nu))
    B = n * b
    r0 = B
    H = N * L * sin_alpha2
    h = []
    for i in range(1, N+1):
        hi = (2*i - 1) / 2.0 * L * sin_alpha2
        h.append(hi)
    W_el_sum = 0.0
    cos2 = cos_alpha2**2
    sin2 = sin_alpha2**2
    for i in range(N):
        hi = h[i]
        twohi_minus_r0 = 2*hi - r0
        if twohi_minus_r0 <= 0:
            self_term = 0.0
        else:
            self_term = math.log(twohi_minus_r0 / r0) - 2*hi*(hi - r0) / (twohi_minus_r0**2)
        inter_sum = 0.0
        for j in range(N):
            if j == i:
                continue
            hj = h[j]
            sign_factor = (-1)**(i+j)
            factor = cos2 + sign_factor * sin2
            sum_h = hi + hj
            diff_h = abs(hi - hj)
            term = math.log(sum_h / diff_h) - 2*hi*hj / (sum_h**2)
            inter_sum += factor * term
        W_el_sum += self_term + inter_sum
    W_el = D * B*B / 2.0 * W_el_sum
    W_s = gamma * (N * L - H)
    W_f = -math.pi * D * B * (1 + nu) * f * L * N * N * sin_alpha
    return W_el + W_s + W_f

def main():
    G = 100e9
    nu = 0.3
    gamma_surf = 0.6
    b = 0.4e-9
    L = 10e-9

    rows = []
    # sweep 1: misfit parameter f with n=1,2,3, default N=100, alpha=90°
    f_values = [0.001, 0.002, 0.003, 0.004, 0.005]
    n_values = [1, 2, 3]
    alpha_deg = 90
    N_def = 100
    for f in f_values:
        for n in n_values:
            dw = delta_W(G, nu, gamma_surf, b, n, L, alpha_deg, f, N_def)
            H_nm = N_def * L * math.sin(math.radians(alpha_deg)/2) * 1e9
            rows.append([f, n, round(H_nm, 3), alpha_deg, dw])

    # sweep 2: film thickness H, adjust N, f=0.004, n=1
    H_targets = [200, 400, 600, 800, 1000]
    f_h = 0.004
    n_h = 1
    L_sin_nm = L * math.sin(math.radians(alpha_deg)/2) * 1e9
    for H_target in H_targets:
        N = int(round(H_target / L_sin_nm))
        if N < 1:
            N = 1
        dw = delta_W(G, nu, gamma_surf, b, n_h, L, alpha_deg, f_h, N)
        H_eff_nm = N * L_sin_nm
        rows.append([f_h, n_h, round(H_eff_nm, 3), alpha_deg, dw])

    # sweep 3: facet angle alpha, f=0.003, n=1, N=100
    alpha_values = [60, 90, 120, 150]
    f_a = 0.003
    n_a = 1
    N_a = 100
    for alpha_deg in alpha_values:
        dw = delta_W(G, nu, gamma_surf, b, n_a, L, alpha_deg, f_a, N_a)
        H_nm = N_a * L * math.sin(math.radians(alpha_deg)/2) * 1e9
        rows.append([f_a, n_a, round(H_nm, 3), alpha_deg, dw])

    writer = csv.writer(sys.stdout)
    writer.writerow(['misfit_parameter', 'Burgers_vector_n', 'film_thickness_nm', 'angle_deg', 'delta_W_J'])
    for row in rows:
        writer.writerow(row)

if __name__ == '__main__':
    main()
