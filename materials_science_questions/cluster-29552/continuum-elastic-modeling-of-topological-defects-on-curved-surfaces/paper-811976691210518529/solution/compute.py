import json
import math
from scipy.special import ellipk

a = 1.0
e = 0.5
r_c = 0.01
f = 1.0
R = 2.0
K1 = 1.0

# complete elliptic integral for parameter m = e^2 = 0.25
K = ellipk(e**2)

# normal focal domain energy (eq. 24)
W_n = 4 * math.pi * K1 * (1 - e**2) * K * a * math.log(a / r_c)

# parabolic focal domain energy (eq. 30)
log_arg = R**2 / (4 * f * r_c)
W_p = (math.pi * K1 * f / 8) * (R**4 / f**4) * math.log(log_arg)

result = {
    "W_n": W_n,
    "W_p": W_p,
    "parabolic_favored": W_p < W_n
}

with open("/app/outputs/focal_domain_energies.json", "w") as fh:
    json.dump(result, fh, indent=2)
