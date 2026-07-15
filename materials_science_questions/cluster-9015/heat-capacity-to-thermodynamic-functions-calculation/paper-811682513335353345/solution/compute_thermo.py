import sys
import csv
import math

# Haas-Fisher polynomial coefficients (Table 3, signed as used)
COEFFS = {
    'HT': dict(a0=604.0, a1=-0.581, a2=3.49e-4, a3=-7120.0, a4=2.047e6),
    'LT': dict(a0=520.3, a1=-0.454, a2=2.461e-4, a3=-6110.0, a4=1.621e6),
}

# Temperature grid: HT from 180 to 570 K step 10, with 298.15 inserted
T_HT = [180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290,
        298.15, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400,
        410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530,
        540, 550, 560, 570]
# LT adds the four lower points
T_LT = [140, 150, 160, 170] + T_HT

T_MIN = {'HT': 180.0, 'LT': 140.0}


def cp(T, c):
    """Heat capacity Cp(T) for given coefficients."""
    return (c['a0'] + c['a1'] * T + c['a2'] * T*T +
            c['a3'] * T**(-0.5) + c['a4'] * T**(-2))


def integral_f(T, c):
    """Antiderivative of Cp(T) for enthalpy."""
    return (c['a0'] * T + (c['a1'] / 2) * T*T + (c['a2'] / 3) * T**3 +
            2 * c['a3'] * T**0.5 - c['a4'] * T**(-1))


def integral_g(T, c):
    """Antiderivative of Cp(T)/T for entropy."""
    return (c['a0'] * math.log(T) + c['a1'] * T + (c['a2'] / 2) * T*T -
            2 * c['a3'] * T**(-0.5) - (c['a4'] / 2) * T**(-2))


writer = csv.writer(sys.stdout)
writer.writerow(['Phase', 'T_K', 'Cp_J_mol_K', 'H_diff_J_mol', 'S_diff_J_mol_K'])

for phase in ('HT', 'LT'):
    T_list = T_HT if phase == 'HT' else T_LT
    tmin = T_MIN[phase]
    c = COEFFS[phase]
    F0 = integral_f(tmin, c)
    G0 = integral_g(tmin, c)
    for T in T_list:
        Cp = cp(T, c)
        H_diff = integral_f(T, c) - F0
        S_diff = integral_g(T, c) - G0
        writer.writerow([phase, f'{T:.2f}'.rstrip('0').rstrip('.') if T == int(T) else f'{T:.2f}',
                         f'{Cp:.4f}', f'{H_diff:.4f}', f'{S_diff:.4f}'])
