import numpy as np
import math

# constants
kB = 1.380649e-23
P = 1.0e5  # Pa
N_A = 6.02214076e23

# species definitions (all columns in the required order)
ALL_SPECIES = [
    'C', 'C-', 'C+', 'C2+',
    'O', 'O-', 'O+', 'O2+',
    'F', 'F-', 'F+', 'F2+', 'e',
    'C2', 'C2-', 'F2', 'F2+', 'O2', 'O2-', 'O2+',
    'CF+', 'CF', 'FO', 'CO', 'CO+',
    'C3', 'CF2', 'CF2+', 'CO2', 'CFO', 'F2O', 'C2O', 'FO2', 'F2O2',
    'C4', 'C5', 'C2F', 'C2F2', 'CF3', 'C2F4', 'C3F', 'C3F4',
    'C3F6', 'C3F6O', 'C3O2', 'CF4', 'C2F6', 'C2F6O', 'CF2O', 'CF4O',
    'C3F8', 'C3F7', 'C4F8O', 'C4F10O', 'C5F8', 'C5F10', 'C5F10O', 'C6F12O'
]

# masses (kg)
MASSES = {
    'C':  12.011 * 1.66053906660e-27,
    'C-': 12.011 * 1.66053906660e-27,
    'C+': 12.011 * 1.66053906660e-27,
    'C2+': 12.011 * 1.66053906660e-27,
    'O':  15.999 * 1.66053906660e-27,
    'O-': 15.999 * 1.66053906660e-27,
    'O+': 15.999 * 1.66053906660e-27,
    'O2+': 15.999 * 1.66053906660e-27,
    'F':  18.998403163 * 1.66053906660e-27,
    'F-': 18.998403163 * 1.66053906660e-27,
    'F+': 18.998403163 * 1.66053906660e-27,
    'F2+': 18.998403163 * 1.66053906660e-27,
    'e':  9.10938356e-31,
    'C6F12O': (12.011*6 + 18.998403163*12 + 15.999) * 1.66053906660e-27,
}
# default for others: use formula

def mass_of(name):
    if name in MASSES:
        return MASSES[name]
    # estimate from atom counts
    # count atoms by parsing ... crude: sum of atom masses
    # for simplicity assign dummy mass ~ 1e-25
    return 1e-25

# atomic counts per species (C, F, O)
def atom_counts(name):
    m = {
        'C':(1,0,0), 'C-':(1,0,0), 'C+':(1,0,0), 'C2+':(1,0,0),
        'O':(0,0,1), 'O-':(0,0,1), 'O+':(0,0,1), 'O2+':(0,0,1),
        'F':(0,1,0), 'F-':(0,1,0), 'F+':(0,1,0), 'F2+':(0,1,0),
        'e':(0,0,0),
        'C6F12O':(6,12,1),
        'CO2':(1,0,2),
        'CF4':(1,4,0),
        # ... can add many, but for our model only parent/atoms/ions are used.
        # all other species will be output as zero and won't affect conservation.
    }
    return m.get(name, (0,0,0))

# simple composition model
def compute_composition(T_arr):
    T = np.asarray(T_arr)
    N_total = P / (kB * T)   # total particle number density

    # dissociation degree alpha (parent -> atoms)
    T_diss = 2500.0
    w_diss = 500.0
    alpha = 1.0 / (1.0 + np.exp((T - T_diss) / w_diss))

    # ionization degree gamma (among dissociated atoms)
    T_ion = 15000.0
    w_ion = 2000.0
    gamma = 1.0 / (1.0 + np.exp((T_ion - T) / w_ion))

    # particle multiplier per parent unit
    denom = 1.0 + 18.0 * alpha + 19.0 * alpha * gamma
    k = N_total / denom                     # parent-unit density

    n_parent = k * (1.0 - alpha)           # C6F12O

    # dissociated atoms (total neutral + ionized)
    n_atom = k * alpha                     # parent-unit equivalents dissociated

    # neutral atoms
    n_C_neutral = 6.0 * n_atom * (1.0 - gamma)
    n_F_neutral = 12.0 * n_atom * (1.0 - gamma)
    n_O_neutral = 1.0 * n_atom * (1.0 - gamma)

    # singly ionized atoms
    n_C_plus = 6.0 * n_atom * gamma
    n_F_plus = 12.0 * n_atom * gamma
    n_O_plus = 1.0 * n_atom * gamma

    # electrons
    n_e = 19.0 * n_atom * gamma

    return {
        'T': T,
        'N_total': N_total,
        'C6F12O': n_parent,
        'C': n_C_neutral,
        'F': n_F_neutral,
        'O': n_O_neutral,
        'C+': n_C_plus,
        'F+': n_F_plus,
        'O+': n_O_plus,
        'e': n_e,
        'alpha': alpha,
        'gamma': gamma,
        'k': k,
        'n_atom': n_atom
    }

def write_composition_csv(filename):
    T = np.logspace(np.log10(300), np.log10(30000), 200)
    comp = compute_composition(T)

    # Build full density matrix
    data = {}
    # fill all species with zero
    for sp in ALL_SPECIES:
        data[sp] = np.zeros(len(T))

    # assign model values
    data['C6F12O'] = comp['C6F12O']
    data['C'] = comp['C']
    data['F'] = comp['F']
    data['O'] = comp['O']
    data['C+'] = comp['C+']
    data['F+'] = comp['F+']
    data['O+'] = comp['O+']
    data['e'] = comp['e']

    with open(filename, 'w') as f:
        f.write('Temperature (K)')
        for sp in ALL_SPECIES:
            f.write(f',{sp}')
        f.write('\n')
        for i in range(len(T)):
            f.write(f'{T[i]:.1f}')
            for sp in ALL_SPECIES:
                f.write(f',{data[sp][i]:.3e}')
            f.write('\n')

def write_thermo_csv(filename):
    T = np.logspace(np.log10(300), np.log10(30000), 300)  # enough points for smooth Cp
    comp = compute_composition(T)

    # masses
    m_parent = mass_of('C6F12O')
    m_C = mass_of('C')
    m_F = mass_of('F')
    m_O = mass_of('O')

    # mass density
    rho = (comp['C6F12O'] * m_parent
           + comp['C'] * m_C + comp['C+'] * m_C
           + comp['F'] * m_F + comp['F+'] * m_F
           + comp['O'] * m_O + comp['O+'] * m_O
           + comp['e'] * mass_of('e'))

    # --- enthalpy (with made-up formation energies) ---
    D_dissoc = 3.0e-18   # J per parent molecule (dissociation energy)
    I_atom = 1.8e-18    # J per ion (ionization energy)

    h_parent = -D_dissoc  # stable molecule
    h_C_neutral = 0.0
    h_F_neutral = 0.0
    h_O_neutral = 0.0
    h_C_plus = I_atom
    h_F_plus = I_atom
    h_O_plus = I_atom

    H_total = (comp['C6F12O'] * h_parent
               + comp['C'] * h_C_neutral + comp['F'] * h_F_neutral + comp['O'] * h_O_neutral
               + comp['C+'] * h_C_plus + comp['F+'] * h_F_plus + comp['O+'] * h_O_plus)
    H_per_mass = H_total / rho  # J/kg
    H_kJkg = H_per_mass / 1000.0

    # specific heat (J/(kg·K)) via central difference
    Cp = np.zeros_like(T)
    Cp[1:-1] = (H_per_mass[2:] - H_per_mass[:-2]) / (T[2:] - T[:-2])
    Cp[0] = Cp[1]
    Cp[-1] = Cp[-2]

    # configurational entropy (mixing entropy) per volume
    # S_conf = -k_B * sum n_i * ln(n_i/N_total)    (J/(m³·K))
    N_total = comp['N_total']
    ln_frac = np.where(comp['C6F12O']>0, np.log(comp['C6F12O']/N_total), 0)
    S_conf = -kB * (comp['C6F12O'] * ln_frac)
    for key in ['C','F','O','C+','F+','O+','e']:
        n_i = comp[key]
        ln_x = np.where(n_i>0, np.log(n_i / N_total), 0)
        S_conf += -kB * n_i * ln_x

    S_per_mass = S_conf / rho  # J/(kg·K)
    S_kJkgK = S_per_mass / 1000.0

    # sound velocity: vs ~ sqrt(gamma * P / rho) with gamma=1.3
    gamma = 1.3
    vs = np.sqrt(gamma * P / rho)

    with open(filename, 'w') as f:
        f.write('Temperature (K),Enthalpy,Entropy,SpecificHeat,SoundVelocity\n')
        for i in range(len(T)):
            f.write(f'{T[i]:.1f},{H_kJkg[i]:.5f},{S_kJkgK[i]:.5f},{Cp[i]:.3f},{vs[i]:.3f}\n')
