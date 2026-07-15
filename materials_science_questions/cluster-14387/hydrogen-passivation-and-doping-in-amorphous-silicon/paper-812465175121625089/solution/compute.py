import csv, math, random

random.seed(12345)

# constants
HBAR_EVS = 6.582119569e-16
EV_AA2_TO_N_M = 16.02176634   # 1 eV/A^2 -> N/m
U_TO_KG = 1.66053906660e-27
FACTOR = HBAR_EVS * math.sqrt(EV_AA2_TO_N_M / U_TO_KG)  # ~0.064654 eV·(u·A^2/eV)^0.5
KB = 8.617333262145e-5  # eV/K

IMPURITY_MASSES = {
    'H': 1.00794,
    'D': 2.0141,
    'Mu': 0.1134
}

K_PARALLEL = 18.42  # eV/A^2
K_PERP_HA = 3.50    # eV/A^2

D_HA = 2.948   # A
D_QHA = 2.899  # A

def coth(x):
    if x == 0:
        return float('inf')
    ex = math.exp(2*x)
    return (ex + 1) / (ex - 1)

def hbar_omega_from_k_m(k, m):
    return FACTOR * math.sqrt(k / m)

def defect_energy_ha(m, T):
    hw_par = hbar_omega_from_k_m(K_PARALLEL, m)
    hw_perp = hbar_omega_from_k_m(K_PERP_HA, m)
    if T == 0:
        return 0.5 * (hw_par + 2*hw_perp)
    else:
        x_par = hw_par / (2 * KB * T)
        x_perp = hw_perp / (2 * KB * T)
        E = 0.5 * (hw_par * coth(x_par) + 2*hw_perp * coth(x_perp))
        return E

def kinetic_energy_ha(m, T):
    hw_par = hbar_omega_from_k_m(K_PARALLEL, m)
    hw_perp = hbar_omega_from_k_m(K_PERP_HA, m)
    if T == 0:
        return 0.25 * (hw_par + 2*hw_perp)
    else:
        x_par = hw_par / (2 * KB * T)
        x_perp = hw_perp / (2 * KB * T)
        KE = 0.25 * (hw_par * coth(x_par) + 2*hw_perp * coth(x_perp))
        return KE

def compute_sigmas(k_perp, k_par, m, T):
    hw_perp = hbar_omega_from_k_m(k_perp, m)
    hw_par = hbar_omega_from_k_m(k_par, m)
    c_perp = coth(hw_perp / (2 * KB * T))
    c_par = coth(hw_par / (2 * KB * T))
    sigma_perp = math.sqrt(hw_perp * c_perp / (2 * k_perp))
    sigma_par = math.sqrt(hw_par * c_par / (2 * k_par))
    return sigma_perp, sigma_par

def sample_angle_distribution(d_SiSi, k_perp, k_par, m, T, n_samples=1000000):
    sigma_perp, sigma_par = compute_sigmas(k_perp, k_par, m, T)
    half_d = d_SiSi / 2.0
    bin_width = 0.5
    low, high = 100.0, 180.5
    # create bin centers
    bin_centers = []
    angle_start = low
    while angle_start + bin_width/2 < high:
        center = angle_start + bin_width/2
        bin_centers.append(center)
        angle_start += bin_width
    bins = {c: 0 for c in bin_centers}
    for _ in range(n_samples):
        x = random.gauss(0, sigma_perp)
        y = random.gauss(0, sigma_perp)
        z = random.gauss(0, sigma_par)
        dot = x*x + y*y + z*z - half_d*half_d
        norm1 = math.sqrt(x*x + y*y + (half_d - z)**2)
        norm2 = math.sqrt(x*x + y*y + (-half_d - z)**2)
        cos_theta = dot / (norm1 * norm2)
        if cos_theta > 1.0:
            cos_theta = 1.0
        if cos_theta < -1.0:
            cos_theta = -1.0
        angle = math.degrees(math.acos(cos_theta))
        # find bin
        half_w = bin_width/2
        for center in bin_centers:
            if angle >= center - half_w and angle < center + half_w:
                bins[center] += 1
                break
    total = n_samples
    pdf_data = []
    for center in bin_centers:
        count = bins[center]
        pdf = count / (total * bin_width)
        pdf_data.append((center, pdf))
    return pdf_data

# --- Write defect_energies.csv ---
impurities = [('H', IMPURITY_MASSES['H']), ('D', IMPURITY_MASSES['D']), ('Mu', IMPURITY_MASSES['Mu'])]
temperatures = [0, 50, 100, 200, 300, 400]

with open('/app/outputs/defect_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['impurity', 'temperature_K', 'defect_energy_HA_eV'])
    for name, mass in impurities:
        for T in temperatures:
            E = defect_energy_ha(mass, T)
            writer.writerow([name, T, f'{E:.6f}'])

# --- Write kinetic_energies.csv (T=50 K) ---
T_KE = 50
with open('/app/outputs/kinetic_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['impurity', 'kinetic_energy_HA_eV'])
    for name, mass in impurities:
        KE = kinetic_energy_ha(mass, T_KE)
        writer.writerow([name, f'{KE:.6f}'])

# --- Write angle_dist_HA.csv ---
m_mu = IMPURITY_MASSES['Mu']
pdf_ha = sample_angle_distribution(D_HA, K_PERP_HA, K_PARALLEL, m_mu, T_KE, n_samples=1000000)
with open('/app/outputs/angle_dist_HA.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['angle_deg', 'pdf_HA'])
    for ang, pdf_val in pdf_ha:
        writer.writerow([f'{ang:.1f}', f'{pdf_val:.8f}'])

# --- Write angle_dist_QHA.csv ---
k_perp_qha = 13.84 * D_QHA - 37.30  # linear relation
pdf_qha = sample_angle_distribution(D_QHA, k_perp_qha, K_PARALLEL, m_mu, T_KE, n_samples=1000000)
with open('/app/outputs/angle_dist_QHA.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['angle_deg', 'pdf_QHA'])
    for ang, pdf_val in pdf_qha:
        writer.writerow([f'{ang:.1f}', f'{pdf_val:.8f}'])
