import sys
import csv
import math

# Crystal lattice parameters (Angstrom)
a = 6.09
b = 7.86
c = 30.48
Z = 4  # molecules per unit cell

# Surface energies at cutoff 19.9 A (Table 1) [meV/A^2]
gamma = {
    '001': 4.274,
    '100': 10.273,
    '110': 8.760,
    '010': 7.705
}

# Adhesion energy [meV/A^2]
sigma = 4.0

# Physical constants
kB_eVK = 8.617333262145e-5   # Boltzmann constant in eV/K
T_c = 298.0                  # substrate temperature [K]

# Beam pressures p_C at substrate (Torr) from Table 2
p_C = {160: 2.9e-8, 170: 6.3e-8, 180: 21e-8}

# Critical nucleus height observed experimentally (160 C, ref 17)
n_c_star_exp = 9.5

# Derived equilibrium vapor pressure p_eq from n_c* equation (7c)
# n_c* = (2 a b (2 gamma_001 - sigma)) / (Z Delta_mu)
# Solve for Delta_mu, then p_eq = p_C_160 * exp(-Delta_mu/(k_B T_c))
a_b = a * b
factor = 2 * a_b * (2 * gamma['001'] - sigma)  # numerator in meV
Delta_mu_meV = factor / (Z * n_c_star_exp)
kBT_meV = kB_eVK * 1000 * T_c   # k_B T_c in meV
p_eq = p_C[160] * math.exp(-Delta_mu_meV / kBT_meV)

# sqrt(a^2 + b^2) for {110} face calculations
sqrt_a2b2 = math.sqrt(a**2 + b**2)

# Precompute energy differences
# For convenience: gamma_110*sqrt(a^2+b^2) - a*gamma_010
diff_a = gamma['110'] * sqrt_a2b2 - a * gamma['010']
diff_b = gamma['110'] * sqrt_a2b2 - b * gamma['100']
diff_ab = diff_a - b * gamma['100']
# (2 gamma_001 - sigma)
effective_001 = 2 * gamma['001'] - sigma

def write_surface_energies(outdir):
    rows = []
    cutoffs = [9.0, 12.0, 15.0, 17.5, 19.9]
    # Table 1 values
    data = {
        9.0:  {'001': 2.269, '100': 8.734, '110': 7.242, '010': 6.350},
        12.0: {'001': 3.656, '100': 9.663, '110': 8.098, '010': 7.158},
        15.0: {'001': 3.967, '100': 9.951, '110': 8.458, '010': 7.410},
        17.5: {'001': 4.126, '100': 10.168, '110': 8.627, '010': 7.598},
        19.9: {'001': 4.274, '100': 10.273, '110': 8.760, '010': 7.705}
    }
    for cutoff in cutoffs:
        for face in ['001', '100', '110', '010']:
            rows.append({'cutoff': cutoff, 'face': face, 'surface_energy': data[cutoff][face]})
    with open(f"{outdir}/surface_energies.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['cutoff', 'face', 'surface_energy'])
        writer.writeheader()
        writer.writerows(rows)

def write_vapor_pressure(outdir):
    s = f"p_eq = {p_eq:.2e} Torr"
    with open(f"{outdir}/vapor_pressure_298K.txt", 'w') as f:
        f.write(s + '\n')

def write_critical_dimensions(outdir):
    rows = []
    for T_src in [160, 170, 180]:
        p_c_val = p_C[T_src]
        # supersaturation Delta_mu in eV
        delta_mu_eV = kB_eVK * T_c * math.log(p_c_val / p_eq)
        # critical dimensions (eqs 7a-7d)
        delta_mu_meV = delta_mu_eV * 1000.0
        n_a = (4 * c * diff_a) / (Z * delta_mu_meV)
        n_b = (4 * c * diff_b) / (Z * delta_mu_meV)
        n_c = (2 * a_b * effective_001) / (Z * delta_mu_meV)
        n_d = -(2 * c * diff_ab) / (Z * delta_mu_meV)
        rows.append({
            'source_temp_C': T_src,
            'n_a_star': n_a,
            'n_b_star': n_b,
            'n_c_star': n_c,
            'n_d_star': n_d,
            'supersaturation_eV': delta_mu_eV
        })
    with open(f"{outdir}/critical_dimensions.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['source_temp_C', 'n_a_star', 'n_b_star', 'n_c_star', 'n_d_star', 'supersaturation_eV'])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: compute.py <artifact_name> <output_dir>", file=sys.stderr)
        sys.exit(1)
    art = sys.argv[1]
    outdir = sys.argv[2]
    if art == 'surface_energies.csv':
        write_surface_energies(outdir)
    elif art == 'vapor_pressure_298K.txt':
        write_vapor_pressure(outdir)
    elif art == 'critical_dimensions.csv':
        write_critical_dimensions(outdir)
    else:
        print(f"Unknown artifact: {art}", file=sys.stderr)
        sys.exit(1)
