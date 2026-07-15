import csv
import math

f = 0.12
eps_inf_par = 6.70
eps_inf_perp = 6.52
wT_par = 783.0
wL_par = 964.0
wT_perp = 798.0
wL_perp = 966.4

S_par = eps_inf_par * ((wL_par / wT_par)**2 - 1)
S_perp = eps_inf_perp * ((wL_perp / wT_perp)**2 - 1)

L_par_values = [i/10.0 for i in range(11)]  # 0.0, 0.1, ..., 1.0

rows = []
for Lp in L_par_values:
    L_perp = (1.0 - Lp) / 2.0

    # --- axial (parallel) ---
    # TO pole condition
    denom_TO_par = 1.0 - (1.0 - f) * Lp
    C_TO_par = - (1.0 - f) * Lp / denom_TO_par
    # LO zero condition (additional Fröhlich mode)
    K_par = f + (1.0 - f) * Lp
    if Lp == 1.0:
        # limit: solution tends to wT_par
        C_LO_par = float('-inf')
        omega_L_par = wT_par
    else:
        denom_LO_par = 1.0 - K_par
        C_LO_par = - K_par / denom_LO_par
        # compute frequency: solve eps_h(omega) = C
    if C_TO_par == eps_inf_par:
        omega_T_par = 0.0  # degenerate, shouldn't happen
    else:
        omega_T_par = wT_par * math.sqrt(max(0.0, 1.0 - S_par / (C_TO_par - eps_inf_par)))
    if Lp != 1.0:
        omega_L_par = wT_par * math.sqrt(max(0.0, 1.0 - S_par / (C_LO_par - eps_inf_par)))

    # --- planar (perpendicular) ---
    denom_TO_perp = 1.0 - (1.0 - f) * L_perp
    C_TO_perp = - (1.0 - f) * L_perp / denom_TO_perp
    K_perp = f + (1.0 - f) * L_perp
    denom_LO_perp = 1.0 - K_perp
    C_LO_perp = - K_perp / denom_LO_perp if denom_LO_perp != 0.0 else float('-inf')
    if denom_LO_perp == 0.0:
        omega_L_perp = wT_perp
    else:
        if C_TO_perp != eps_inf_perp:
            omega_T_perp = wT_perp * math.sqrt(max(0.0, 1.0 - S_perp / (C_TO_perp - eps_inf_perp)))
        else:
            omega_T_perp = 0.0
        omega_L_perp = wT_perp * math.sqrt(max(0.0, 1.0 - S_perp / (C_LO_perp - eps_inf_perp)))
    # handle Lp=1 special case already done, but in planar L_perp=0, finiteness holds.
    # recompute planar values in a clean way:
    # (the above logic is messy, let's rewrite cleanly below before final)
    # We'll use a cleaner implementation.

    # Let's just recompute properly: above is for illustration; we'll use a concise loop.
    # Actually we'll replace with neat final code.

# *** CLEAN FINAL IMPLEMENTATION ***
# Because the above is confusing, I'll write the real script content below.

EOF
