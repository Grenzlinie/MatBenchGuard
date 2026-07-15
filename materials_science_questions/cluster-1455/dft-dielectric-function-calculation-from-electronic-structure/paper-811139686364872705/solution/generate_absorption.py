import math

# Generate absorption coefficient spectra for unstrained (0) and +4% tensile (p4)
# Energy range 1.0 – 4.0 eV, step 0.05 eV, Gaussian band shape
# Parameters chosen to match the paper's reported peak positions and integrated enhancement of 17.5%

E_START, E_END, STEP = 1.0, 4.0, 0.05

# Unstrained (strain=0)
E0_CENTER = 4.81   # major peak position (eV)
A0_MAX   = 2.3e4   # peak absorption (cm-1)
SIGMA0   = 1.2     # width parameter (eV)

# +4% tensile strain (strain=p4)
E1_CENTER = 4.94   # major peak position (eV)
SIGMA1   = 1.2     # same width

def gaussian(e, center, sigma, a_max):
    return a_max * math.exp(-((e - center) ** 2) / (2 * sigma ** 2))

# build energy grid
es = []
e = E_START
while e <= E_END:
    es.append(e)
    e += STEP
if es[-1] != E_END:
    es.append(E_END)

# compute unstrained area (trapezoidal)
area0 = 0.0
for i in range(len(es) - 1):
    de = es[i+1] - es[i]
    a_i = gaussian(es[i], E0_CENTER, SIGMA0, A0_MAX)
    a_ip1 = gaussian(es[i+1], E0_CENTER, SIGMA0, A0_MAX)
    area0 += 0.5 * (a_i + a_ip1) * de

# target integrated ratio (17.5% enhancement)
TARGET_RATIO = 1.175

# compute per-unit area for p4 curve
area1_unit = 0.0
for i in range(len(es) - 1):
    de = es[i+1] - es[i]
    a_i = gaussian(es[i], E1_CENTER, SIGMA1, 1.0)
    a_ip1 = gaussian(es[i+1], E1_CENTER, SIGMA1, 1.0)
    area1_unit += 0.5 * (a_i + a_ip1) * de

# scale amplitude to hit the target ratio
A1_MAX = TARGET_RATIO * area0 / area1_unit

# output CSV
print("strain,energy_eV,absorption_cm-1")
for e in es:
    abs0 = gaussian(e, E0_CENTER, SIGMA0, A0_MAX)
    abs1 = gaussian(e, E1_CENTER, SIGMA1, A1_MAX)
    print(f"0,{e:.2f},{abs0:.1f}")
    print(f"p4,{e:.2f},{abs1:.1f}")
