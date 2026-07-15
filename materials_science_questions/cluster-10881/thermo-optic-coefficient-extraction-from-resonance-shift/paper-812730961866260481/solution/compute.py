import numpy as np

# Constants in SI (meters)
LAMBDA0 = 250e-6          # 250 um
DN_EFF0 = 0.0062
LAMBDA_C = 1.55e-6        # not directly used, but included for clarity
DELTA_LAMBDA0 = 39.6e-9
N_PERIODS = 100
SIGMA_LAMBDA_PER_STEP = 0.01e-6   # 0.01 um = 1e-8 m per step
SIGMA_DN_PER_STEP = 1e-6          # riu per step

dn_values = [0, 1e-6, -1e-6, 3e-6, -3e-6]
ms = list(range(-10, 11))

# Wavelength grid around 1550 nm (1.55e-6 m) in meters
lambda_start = 1.5e-6   # 1500 nm
lambda_end = 1.6e-6     # 1600 nm
lambda_step = 0.01e-9   # 0.01 nm
wavelengths = np.arange(lambda_start, lambda_end + lambda_step, lambda_step)

def compute_I_dB(lambda_val, Lambda1, Lambda2, dn_eff1, dn_eff2):
    # detuning and coupling for section 1
    delta1 = np.pi * (dn_eff1 / lambda_val - 1.0 / Lambda1)
    kappa1 = (DELTA_LAMBDA0 / lambda_val**2) * dn_eff1
    # section 2
    delta2 = np.pi * (dn_eff2 / lambda_val - 1.0 / Lambda2)
    kappa2 = (DELTA_LAMBDA0 / lambda_val**2) * dn_eff2
    
    # lengths
    L1 = N_PERIODS * Lambda1
    L2 = N_PERIODS * Lambda2
    
    # delta_beta
    deltabeta1 = 2.0 * np.sqrt(delta1**2 + kappa1**2)
    deltabeta2 = 2.0 * np.sqrt(delta2**2 + kappa2**2)
    
    # C, S
    C1 = np.cos(deltabeta1 * L1)
    S1 = np.sin(deltabeta1 * L1)
    C2 = np.cos(deltabeta2 * L2)
    S2 = np.sin(deltabeta2 * L2)
    
    # Delta, K (guard against division by zero)
    if deltabeta1 == 0:
        Delta1, K1 = 0.0, 0.0
    else:
        Delta1 = 2.0 * delta1 / deltabeta1
        K1 = 2.0 * kappa1 / deltabeta1
    if deltabeta2 == 0:
        Delta2, K2 = 0.0, 0.0
    else:
        Delta2 = 2.0 * delta2 / deltabeta2
        K2 = 2.0 * kappa2 / deltabeta2
    
    # Intensity (Eq 5b)
    term1 = C1*C2 - (Delta1*Delta2 + K1*K2) * S1*S2
    term2 = Delta1*S1*C2 + Delta2*C1*S2
    I = term1**2 + term2**2
    # I should be between 0 and 1; avoid log(0)
    I_dB = 10.0 * np.log10(I) if I > 0 else -100
    return I_dB

def compute_depth(dn, m):
    # Effective temperatures: half1: T0 + m, half2: T0 - m
    dn_eff1_base = DN_EFF0 - dn
    dn_eff2_base = DN_EFF0 + dn
    
    Lambda1 = LAMBDA0 + SIGMA_LAMBDA_PER_STEP * m
    Lambda2 = LAMBDA0 - SIGMA_LAMBDA_PER_STEP * m
    dn_eff1 = dn_eff1_base + SIGMA_DN_PER_STEP * m
    dn_eff2 = dn_eff2_base - SIGMA_DN_PER_STEP * m
    
    # Compute I_dB for all wavelengths and find minimum
    I_dB_vec = np.array([compute_I_dB(wl, Lambda1, Lambda2, dn_eff1, dn_eff2) for wl in wavelengths])
    I_min = np.min(I_dB_vec)
    return I_min

# Reference depths for m=0 for each dn
ref_depths = {}
for dn in dn_values:
    ref_depths[dn] = compute_depth(dn, 0)

# Output CSV header
print("dn,m,DeltaI_m")

# Compute DeltaI_m and print
for dn in dn_values:
    ref = ref_depths[dn]
    for m in ms:
        depth = compute_depth(dn, m)
        delta = depth - ref
        # Print dn as plain decimal to match expected float format
        print(f"{dn:.6f},{m},{delta:.6f}")
