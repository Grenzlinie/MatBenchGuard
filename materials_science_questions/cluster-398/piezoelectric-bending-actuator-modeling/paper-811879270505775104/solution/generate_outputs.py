import math, csv, json, os

# ---------- physical constants ----------
k_B = 1.380649e-23          # J/K
T   = 300.0                 # K
beta = 1.0 / (k_B * T)      # J^-1
e_charge = 1.602176634e-19  # C

# ---------- motor parameters (true values after self-consistency correction) ----------
Delta_q = 0.9 * e_charge    # C
# elastic moduli (N/m)
d1 = 0.046
d2 = 0.068
c_mod = 0.046               # renamed to avoid clash with variable c
# motor area changes (m^2)
Delta_a_z = 4.5e-18
Delta_a_c = -0.75e-18
# motor density (m^-2)
n = 9.0e15
# cell dimensions (m)
L = 50e-6
R = 5e-6
# linear membrane capacitance (F)
C_lin = 20.0e-12

# ---------- derived constants ----------
g_val = 1.0 / (4*d1 - 4*c_mod + d2)
b1 = 2 * g_val * (Delta_a_z * (2*d1 - c_mod) + Delta_a_c * (2*c_mod - d2))
b2 = 0.27          # paper's corrected value
b1_n = b1 * n

# motor charge scaling
beta_Delta_q = Delta_q / (k_B * T)   # V^{-1}
V_half = -20e-3                        # half-activation potential (V)
b3 = beta_Delta_q * V_half - 0.5 * b2

# lateral membrane area and total motor number
area_lateral = 2 * math.pi * R * L
N = n * area_lateral

# ---------- utilities ----------
def make_output_dir():
    os.makedirs("/app/outputs", exist_ok=True)

# ---------- JSON output ----------
def write_json():
    P_half = 0.5
    alpha_half = 1.0 / (1.0 + b2 * P_half * (1 - P_half))
    # nonlinear c11 at P=0.5
    c11_max = alpha_half * beta * N * (Delta_q**2) * P_half * (1 - P_half)
    c12_max = alpha_half * beta * n * L * Delta_q * b1 * P_half * (1 - P_half)
    c22_max = (L / (2*math.pi*R)) * (4*g_val + alpha_half * beta * n * (b1**2) * P_half * (1 - P_half))
    k_max = c12_max / math.sqrt((c11_max + C_lin) * c22_max)

    data = {
        "c11_max": c11_max,
        "c12_max": c12_max,
        "c22_max": c22_max,
        "k_max": k_max,
        "alpha_at_half": alpha_half,
        "b2": b2,
        "b1_n": b1_n
    }
    with open(os.path.join("/app/outputs", "step_01_coefficients.json"), "w") as f:
        json.dump(data, f, indent=2)

# ---------- CSV output ----------
def write_csv():
    # fine grid for solving V_m = f(P)
    n_fine = 50000
    startP = 1e-6
    endP = 1 - 1e-6
    stepP = (endP - startP) / (n_fine - 1)
    P_fine = [startP + i*stepP for i in range(n_fine)]
    V_fine = [(b2*P - math.log(1.0/P - 1) + b3) / beta_Delta_q for P in P_fine]

    target_V_mV = list(range(-150, 51))   # mV, inclusive of +50 mV
    rows = []
    for v_mV in target_V_mV:
        v_volt = v_mV * 1e-3
        # find index where V_fine >= v_volt
        idx = 0
        for i, v in enumerate(V_fine):
            if v >= v_volt:
                idx = i
                break
        else:
            idx = n_fine - 1
        if idx == 0:
            P = P_fine[0]
        elif V_fine[idx] == v_volt:
            P = P_fine[idx]
        else:
            v0 = V_fine[idx-1]
            v1 = V_fine[idx]
            p0 = P_fine[idx-1]
            p1 = P_fine[idx]
            if v1 == v0:
                P = p0
            else:
                P = p0 + (p1 - p0) * (v_volt - v0) / (v1 - v0)
        P = max(0.0, min(1.0, P))

        alpha_val = 1.0 / (1.0 + b2 * P * (1 - P))
        dP_dV = alpha_val * beta_Delta_q * P * (1 - P)
        c11_nonlin = alpha_val * beta * N * (Delta_q**2) * P * (1 - P)
        c12_val = alpha_val * beta * n * L * Delta_q * b1 * P * (1 - P)
        c22_val = (L / (2*math.pi*R)) * (4*g_val + alpha_val * beta * n * (b1**2) * P * (1 - P))
        total_c11 = c11_nonlin + C_lin
        denom = math.sqrt(total_c11 * c22_val) if total_c11 * c22_val > 0 else 0
        k_val = c12_val / denom if denom != 0 else 0
        rows.append([v_mV, P, dP_dV, alpha_val, c11_nonlin, c12_val, c22_val, k_val])

    with open(os.path.join("/app/outputs", "step_02_voltage_dependence.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["V_m", "P_ell", "dP_dV", "alpha", "c11", "c12", "c22", "k"])
        for row in rows:
            formatted = [
                row[0],
                f"{row[1]:.6e}",
                f"{row[2]:.6e}",
                f"{row[3]:.6e}",
                f"{row[4]:.6e}",
                f"{row[5]:.6e}",
                f"{row[6]:.6e}",
                f"{row[7]:.6e}"
            ]
            writer.writerow(formatted)

# ---------- main ----------
if __name__ == "__main__":
    make_output_dir()
    write_json()
    write_csv()