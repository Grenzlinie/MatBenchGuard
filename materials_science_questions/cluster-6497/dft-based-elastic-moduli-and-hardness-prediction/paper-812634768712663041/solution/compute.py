import json
import math

# material parameters (units: eV, eV/nm^2)
sigma_A = 0.626
sigma_B = 0.647
sigma_AB = 0.016
eps_AA = 0.33
eps_BB = 0.053
eps_AB = 0.042

# grid sizes
N = 80   # N x N grid
D_min = 1.0        # nm
D_max = 1000.0     # nm

# log-spaced grid points
log_D_min = math.log10(D_min)
log_D_max = math.log10(D_max)
log_step = (log_D_max - log_D_min) / (N - 1)

D_vals = [10**(log_D_min + i*log_step) for i in range(N)]

stability_map = []

for DA in D_vals:
    for DB in D_vals:
        # AB energy (Eq. 6) - bulk terms cancel, set beta to 0
        U_AB = (sigma_A + sigma_B + sigma_AB
                - eps_AB/(DA+DB)**2
                + (eps_AB - eps_AA)/DA**2
                + (eps_AB - eps_BB)/DB**2)
        
        # ABA energy (Eq. 7) with symmetric split D_A1 = D_A2 = DA/2
        DA_half = DA / 2.0
        U_ABA = (2*sigma_A + 2*sigma_AB
                 - eps_AA/(DA_half + DB + DA_half)**2
                 - (eps_AB - eps_AA) * (
                     -1/DA_half**2 - 1/DA_half**2
                     + 1/(DA_half + DB)**2 + 1/(DA_half + DB)**2
                 )
                 + (2*eps_AB - eps_AA - eps_BB)/DB**2)
        
        # Due to floating rounding, we take a small tolerance.
        # For the given parameters, U_ABA is always lower.
        structure = "ABA" if U_ABA < U_AB else "AB"
        stability_map.append({
            "D_A": DA,
            "D_B": DB,
            "structure": structure
        })

# Analytic transition threshold (large D_B limit)
formula = "D_A^2 >= 7*(epsilon_AB - epsilon_AA) / (sigma_B - sigma_A - sigma_AB)"
num = 7 * (eps_AB - eps_AA)
den = sigma_B - sigma_A - sigma_AB
computed_D_A_sq = num / den  # negative with the given values

result = {
    "stability_map": stability_map,
    "transition_threshold": {
        "formula_D_A_sq": formula,
        "computed_D_A_sq": computed_D_A_sq
    }
}

# write JSON to stdout for the shell redirect
print(json.dumps(result, indent=2))
