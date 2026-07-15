import json, math, sys

v = 0.2

# hollow cavity hoop stress ww at r=a, ratios of applied compressive stress p
# simplified from Eq (6) in the paper
hollow_ww_0 = -(3 + 15*v) / (14 - 10*v)      # at w=0
hollow_ww_pi2 = (27 - 15*v) / (14 - 10*v)   # at w=pi/2

# internal pressure q under uniaxial compression (paper Eq. 13)
q = -2/3

# water-filled hoop stresses by superposition: ww_water = ww_hollow + q/2
water_ww_0 = hollow_ww_0 + q/2
water_ww_pi2 = hollow_ww_pi2 + q/2

# displacement ratio DeltaL1/DeltaL2 for cubic element model
# Eqs. (16) and (17) with D/L ratio, L=1 for simplicity
def displacement_ratio(DL):
    L = 1.0
    D = DL
    pi = math.pi
    denom = 4 - pi * D*D
    delta_L1 = (L - D) + 4*D / denom
    # the coefficient 0.667 in Eq. (17) is the absolute value of q/p = 2/3
    num = 4 - (2/3) * pi * D*D
    delta_L2 = (L - D) + (num / denom) * D
    return delta_L1 / delta_L2

dr_05 = displacement_ratio(0.5)
dr_667 = displacement_ratio(0.667)

# uniaxial tension: replace p by -p, and water cannot pressurize
# so both hollow and water-filled stresses are identical
tension_hollow_ww_0 = -hollow_ww_0
tension_water_ww_0 = tension_hollow_ww_0

result = {
    "hollow_ww_at_0": round(hollow_ww_0, 6),
    "hollow_ww_at_pi2": round(hollow_ww_pi2, 6),
    "water_ww_at_0": round(water_ww_0, 6),
    "water_ww_at_pi2": round(water_ww_pi2, 6),
    "internal_pressure_q": round(q, 6),
    "delta_L1_delta_L2_DL_0_5": round(dr_05, 6),
    "delta_L1_delta_L2_DL_0_667": round(dr_667, 6),
    "tension_hollow_ww_at_0": round(tension_hollow_ww_0, 6),
    "tension_water_ww_at_0": round(tension_water_ww_0, 6)
}

json.dump(result, sys.stdout, indent=2)
