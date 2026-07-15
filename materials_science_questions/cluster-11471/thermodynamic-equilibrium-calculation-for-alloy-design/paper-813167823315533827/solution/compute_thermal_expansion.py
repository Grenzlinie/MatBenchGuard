import math, csv

# Constants from the paper and standard references
rho_gr = 2.25          # g/cm³, density of graphite
rho_Fe = 7.87          # g/cm³, density of iron
alpha_gr = 1.0e-6      # /K, thermal expansion of graphite
alpha_Fe = 12.0e-6     # /K, thermal expansion of iron

# Austenite intrinsic thermal expansion (approx.)
alpha_gamma_T = 20.0e-6   # /K

# Lattice expansion of austenite due to carbon (Ridley & Stuart 1970)
# a(nm) = 0.3573 + 0.0033*wt%C  =>  dε/dC = 0.0033/0.3573 ≈ 9.24e-3 per wt% C
depsilon_dC = 9.24e-3   # strain per wt% C

# Fe-C phase diagram solubility (Chipman 1972) fit
# C_gamma (wt%) = A * exp(-B/T) with T in K
A_sol = 23.1
B_sol = 3400.0

# Total carbon content of the alloy (wt%) corresponding to f_gr0 ≈ 0.10 vol frac at room T
C_tot = 3.08

# A1 transformation temperature
A1_C = 727.0
A1_K = A1_C + 273.15

# Calculate initial graphite volume fraction at room T (all carbon as graphite)
m_gr_mass0 = C_tot / 100.0          # mass fraction graphite
f_gr0 = (m_gr_mass0 / rho_gr) / (m_gr_mass0 / rho_gr + (1 - m_gr_mass0) / rho_Fe)

def C_gamma(T_K):
    """Carbon solubility in austenite at temperature T_K (K), wt%"""
    if T_K < A1_K:
        return 0.0               # below A1, solubility in ferrite is negligible
    return A_sol * math.exp(-B_sol / T_K)

def dC_dT_analytical(T_K):
    """Derivative of carbon solubility with temperature (wt%/K) from the analytical formula"""
    return A_sol * (B_sol / (T_K**2)) * math.exp(-B_sol / T_K)

rows = []
for T_C in range(200, 950, 50):
    if T_C <= A1_C:
        # Low temperature: matrix is pearlitic steel, B = α_Fe
        alpha_B = alpha_Fe
        # Graphite volume fraction constant (no dissolution)
        f_gr = f_gr0
        rho = f_gr * rho_gr + (1 - f_gr) * rho_Fe
        alpha_C = (alpha_gr * (rho_gr / rho) * f_gr
                   + alpha_Fe * (rho_Fe / rho) * (1 - f_gr))
    else:
        T_K = T_C + 273.15
        Cg = C_gamma(T_K)

        # Mass fraction of graphite
        if Cg >= C_tot:
            m_gr_mass = 0.0
        else:
            m_gr_mass = (C_tot - Cg) / (100.0 - Cg)

        # Volume fraction of graphite
        if m_gr_mass <= 0.0:
            f_gr = 0.0
        else:
            f_gr = (m_gr_mass / rho_gr) / ((m_gr_mass / rho_gr) + ((1 - m_gr_mass) / rho_Fe))

        # df_gr/dT by central difference (ΔT = 1 K)
        T_K_plus = T_K + 1.0
        T_K_minus = T_K - 1.0
        Cg_plus = C_gamma(T_K_plus)
        Cg_minus = C_gamma(T_K_minus)

        def m_gr_mass_fcn(Cg_val):
            if Cg_val >= C_tot:
                return 0.0
            return (C_tot - Cg_val) / (100.0 - Cg_val)

        def f_gr_fcn(m_gr_val):
            if m_gr_val <= 0.0:
                return 0.0
            return (m_gr_val / rho_gr) / ((m_gr_val / rho_gr) + ((1 - m_gr_val) / rho_Fe))

        m_gr_plus = m_gr_mass_fcn(Cg_plus)
        m_gr_minus = m_gr_mass_fcn(Cg_minus)
        f_gr_plus = f_gr_fcn(m_gr_plus)
        f_gr_minus = f_gr_fcn(m_gr_minus)
        df_gr_dT = (f_gr_plus - f_gr_minus) / 2.0

        rho = f_gr * rho_gr + (1 - f_gr) * rho_Fe

        # alpha_B for austenite matrix (with carbon effect)
        dC_dT_val = dC_dT_analytical(T_K)
        alpha_B = alpha_gamma_T + depsilon_dC * dC_dT_val

        # alpha_C with plastic deformation term (equation 2)
        term1 = df_gr_dT * (rho_gr - rho_Fe) / (3.0 * rho)
        term2 = alpha_gr * (rho_gr / rho) * f_gr
        term3 = alpha_Fe * (rho_Fe / rho) * (1 - f_gr)
        alpha_C = term1 + term2 + term3

    # Convert to 10⁻⁶ /K for output
    rows.append((T_C, round(alpha_B / 1e-6, 3), round(alpha_C / 1e-6, 3)))

# Write CSV
with open('/app/outputs/step_01_thermal_expansion.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['temperature_C', 'alpha_B', 'alpha_C'])
    for temp, b, c in rows:
        writer.writerow([temp, b, c])