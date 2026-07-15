import sys, json, math
import numpy as np

def compute():
    n1 = 10
    Nc = 20
    a0 = 1.0
    a = 4.0
    d = 2 * n1 * a0 + 2 * a0  # 22 a0
    eta = 1.7 * a0
    tau = -a0

    Omega_TO = 362.0
    eta_z = 22.0
    chi_z = 1.36
    Rz = 4
    eta_x = 22.0
    chi_x = 1.08
    Rx = 2

    omega_LO = 392.0
    Delta = omega_LO**2 - Omega_TO**2  # 22620
    B = math.sqrt(Delta)

    ks = [2*m+1 for m in range(n1)]  # 1,3,...,19
    nks = len(ks)

    Omega_z = np.zeros(nks)
    Omega_x = np.zeros(nks)
    Bk = np.zeros(nks)
    for idx, k in enumerate(ks):
        kappa_dimless = k / 11.0
        arg_z = (kappa_dimless / chi_z) ** Rz
        Omega_z[idx] = Omega_TO - eta_z * (1 - math.exp(-arg_z))
        arg_x = (kappa_dimless / chi_x) ** Rx
        Omega_x[idx] = Omega_TO - eta_x * (1 - math.exp(-arg_x))

        x = math.pi * k * eta / d
        if x < 1e-8:
            factor = 1.0
        else:
            factor = math.sin(x) / x
        Bk[idx] = B * factor

    def field_profile(C):
        Cs = C[:nks]
        Cg = C[nks:]
        Nmono = 40
        Ez_arb = np.zeros(Nmono)
        Ex_arb = np.zeros(Nmono)
        for z_mono in range(Nmono):
            if z_mono < 2*n1:
                for idx_k, k in enumerate(ks):
                    ang = math.pi * k * (z_mono + 1) / 22.0
                    Ez_arb[z_mono] += Cs[idx_k] * Bk[idx_k] * math.sin(ang)
                    Ex_arb[z_mono] += Cg[idx_k] * Bk[idx_k] * math.sin(ang)
        return Ez_arb, Ex_arb

    freq_results = []
    fields_results = []
    abs_max_arb = 0.0
    theta_range = np.arange(0, 91, 1)
    for theta_deg in theta_range:
        theta = math.radians(theta_deg)
        cos_t = math.cos(theta)
        sin_t = math.sin(theta)
        M = np.zeros((2*nks, 2*nks), dtype=np.float64)
        for i in range(nks):
            M[i, i] = Omega_z[i]**2 + Bk[i]**2
            M[i+nks, i+nks] = Omega_x[i]**2
        for i in range(nks):
            for j in range(i+1, nks):
                k_i = ks[i]
                k_j = ks[j]
                h = (4.0 / math.pi**2) * Bk[i] * Bk[j] / (k_i * k_j)
                M[i, j] = -h * sin_t**2
                M[j, i] = M[i, j]
                M[i+nks, j+nks] = h * sin_t**2
                M[j+nks, i+nks] = M[i+nks, j+nks]
        for i in range(nks):
            for j in range(nks):
                k_i = ks[i]
                k_j = ks[j]
                h = (4.0 / math.pi**2) * Bk[i] * Bk[j] / (k_i * k_j)
                M[i, j+nks] = h * sin_t * cos_t
                M[j+nks, i] = M[i, j+nks]
                M[i+nks, j] = M[i, j+nks]
                M[j, i+nks] = M[i, j+nks]

        eigvals, eigvecs = np.linalg.eigh(M)
        idx_sort = np.argsort(eigvals)
        eigvals = eigvals[idx_sort]
        eigvecs = eigvecs[:, idx_sort]

        for mode_i, val in enumerate(eigvals):
            freq = math.sqrt(max(val, 0.0))
            freq_results.append({
                "theta_deg": float(theta_deg),
                "mode_index": mode_i,
                "frequency_cm-1": float(freq)
            })

        if theta_deg == 0 or theta_deg == 90:
            for mode_i in range(2*nks):
                C = eigvecs[:, mode_i]
                Ez_arb, Ex_arb = field_profile(C)
                if theta_deg == 0:
                    abs_max_arb = max(abs_max_arb, np.max(np.abs(Ez_arb)))
                fields_results.append({
                    "theta_deg": float(theta_deg),
                    "mode_index": mode_i,
                    "Ez_arb": Ez_arb.tolist(),
                    "Ex_arb": Ex_arb.tolist()
                })

    target_max = 0.40
    scale = target_max / abs_max_arb if abs_max_arb > 0 else 1.0

    fields_final = []
    for item in fields_results:
        for z_mono in range(40):
            Ez_val = item["Ez_arb"][z_mono] * scale
            Ex_val = item["Ex_arb"][z_mono] * scale
            fields_final.append({
                "mode_index": item["mode_index"],
                "z_monolayer": z_mono,
                "Ez_meV_per_A": Ez_val,
                "Ex_meV_per_A": Ex_val
            })

    return {
        "frequencies": freq_results,
        "fields": fields_final
    }

if __name__ == "__main__":
    output_path = sys.argv[1]
    data = compute()
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
