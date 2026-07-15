#!/usr/bin/env python3
"""
Kamlet-Jacobs detonation calculator for C-H-N-O-F-S compounds.
Decomposition rule (priority):
  1. Form SF4 from S using F (if F >= 4 per S).
  2. Form HF from remaining H and F.
  3. Form CF4 from remaining C and F (if F >= 4 per C).
  4. Remaining H forms H2, remaining C and S become solid.
  5. N2 from all N.
The script reads atom counts, density (g/cm³) and condensed heat of formation
(kJ/mol) via command line, outputs JSON with density, delta_H_condensed,
detonation_P (GPa), detonation_D (m/s).
"""
import argparse, json, math

# Atomic masses (g/mol)
MASS = {
    'C': 12.0107,
    'H': 1.00794,
    'N': 14.0067,
    'O': 15.999,
    'F': 18.9984,
    'S': 32.065
}

# Gas-phase heats of formation (kJ/mol) at 298 K
DHF_GAS = {
    'SF4': -763.2,
    'HF':  -273.3,
    'CF4': -933.0,   # not used under current priority but kept for completeness
    'H2': 0.0,
    'N2': 0.0,
    'C_s': 0.0,
    'S_s': 0.0
}

def compute_detonation(C, H, N, O, F, S, rho, HOF_reac):
    """
    Returns P (GPa), D (m/s) using Kamlet-Jacobs equations.
    """
    # Priority 1: SF4
    SF4_moles = 0.0
    if S > 0 and F >= 4 * S:
        SF4_moles = S
        F -= 4 * S
        S = 0

    # Priority 2: HF
    HF_moles = min(H, F)
    H -= HF_moles
    F -= HF_moles

    # Priority 3: CF4
    CF4_moles = 0.0
    if C > 0 and F >= 4 * C:
        CF4_moles = C
        F -= 4 * C
        C = 0
    # Remaining C becomes solid carbon (C_s), S solid sulfur

    # Hydrogen leftover => H2
    H2_moles = H / 2.0

    # Nitrogen => N2
    N2_moles = N / 2.0

    # Total gas moles per mole of compound
    total_gas_moles = SF4_moles + HF_moles + CF4_moles + H2_moles + N2_moles
    if total_gas_moles == 0:
        return 0.0, 0.0

    # Molecular weight of compound
    Mw = (C * MASS['C'] + H * MASS['H'] + N * MASS['N'] +
          O * MASS['O'] + F * MASS['F'] + S * MASS['S'])

    # Moles of gas per gram of explosive
    N_per_g = total_gas_moles / Mw

    # Average molecular weight of gaseous products
    gas_mass = (SF4_moles * (MASS['S'] + 4*MASS['F']) +
                HF_moles   * (MASS['H'] + MASS['F']) +
                CF4_moles  * (MASS['C'] + 4*MASS['F']) +
                H2_moles   * (2*MASS['H']) +
                N2_moles   * (2*MASS['N']))
    M_avg = gas_mass / total_gas_moles

    # Heat of formation of products (kJ/mol)
    H_prod = (SF4_moles * DHF_GAS['SF4'] +
              HF_moles   * DHF_GAS['HF'] +
              CF4_moles  * DHF_GAS['CF4'] +
              H2_moles   * DHF_GAS['H2'] +
              N2_moles   * DHF_GAS['N2'] +
              C          * DHF_GAS['C_s'] +   # solid carbon
              S          * DHF_GAS['S_s'])    # solid sulfur

    # Heat release (kJ/mol) exothermic is positive
    Q_kJ = HOF_reac - H_prod
    Q_kcal = Q_kJ / 4.184
    Q_cal_per_g = Q_kcal * 1000.0 / Mw    # cal/g

    # Kamlet-Jacobs parameter phi
    phi = N_per_g * math.sqrt(M_avg * Q_cal_per_g)

    # Detonation pressure in GPa (original P in kbar = 15.58 * rho^2 * phi, 1 kbar = 0.1 GPa)
    P_GPa = 1.558 * rho**2 * phi
    # Detonation velocity in km/s converted to m/s
    D_kms = 1.01 * math.sqrt(phi) * (1.0 + 1.30 * rho)
    D_ms = D_kms * 1000.0

    return P_GPa, D_ms

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Kamlet-Jacobs detonation calculator')
    parser.add_argument('--C', type=float, required=True)
    parser.add_argument('--H', type=float, required=True)
    parser.add_argument('--N', type=float, required=True)
    parser.add_argument('--O', type=float, default=0.0)
    parser.add_argument('--F', type=float, required=True)
    parser.add_argument('--S', type=float, default=0.0)
    parser.add_argument('--density', type=float, required=True)
    parser.add_argument('--hof', type=float, required=True, help='Condensed heat of formation (kJ/mol)')
    parser.add_argument('--compound', type=str, required=True)
    parser.add_argument('--output', type=str, required=True)
    args = parser.parse_args()

    P, D = compute_detonation(args.C, args.H, args.N, args.O, args.F, args.S,
                               args.density, args.hof)

    result = {
        'compound': args.compound,
        'density': args.density,
        'delta_H_condensed': args.hof,
        'detonation_P': round(P, 2),
        'detonation_D': round(D, 0)  # integer m/s
    }

    with open(args.output, 'w') as f:
        json.dump(result, f, indent=2)
