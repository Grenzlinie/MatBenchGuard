import numpy as np
from scipy.integrate import quad
import json

# parameters
nu = 0.3
mu = 1.0
mu1 = 20.0
epsilon0 = 1.0  # (alpha1 - alpha) * DeltaT, cancels in normalization
R = 1.0
a = 1.0
D = 3.0

# inclusion center at (D, 0) = (3,0)
# crack from -a to a along x-axis

# plane strain Lame constant lambda = 2 * nu / (1 - 2*nu) * mu
lam1 = 2 * nu / (1 - 2*nu) * mu1
C1 = epsilon0 * (mu1 + lam1) / (mu1 + lam1 + mu)

def sigma_yy(x):
    r = D - x   # x <= a < D, so r positive
    return 2 * mu * C1 * R**2 / (r**2)

def integrand_right(x):
    return sigma_yy(x) * np.sqrt((1 + x) / (1 - x))

def integrand_left(x):
    return sigma_yy(x) * np.sqrt((1 - x) / (1 + x))

I_right, _ = quad(integrand_right, -1, 1, limit=200, epsabs=1e-8)
I_left, _ = quad(integrand_left, -1, 1, limit=200, epsabs=1e-8)

F_right = I_right / np.pi
F_left = I_left / np.pi

result = {
    "tip_A": {
        "mode_I": round(F_left, 6),
        "mode_II": 0.0
    },
    "tip_B": {
        "mode_I": round(F_right, 6),
        "mode_II": 0.0
    }
}

with open('/app/outputs/sif_results.json', 'w') as f:
    json.dump(result, f, indent=2)
