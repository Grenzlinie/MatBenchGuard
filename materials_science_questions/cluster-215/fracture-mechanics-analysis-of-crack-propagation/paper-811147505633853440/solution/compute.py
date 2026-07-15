import numpy as np

# --- Parameter grid --------------------------------------------------------
# Sweep ranges covering the paper's discussions (Figs 4-7).
V_f_vals     = [0.30, 0.50, 0.70, 0.90]
rho_vals     = [5.0, 15.0, 30.0]
Phi_vals     = [0.20, 0.50, 0.80]
lambda_vals  = [10.0, 50.0, 100.0]
h2_over_H_vals = [0.01, 0.05, 0.10]

# Fixed geometric and material parameters (SI units).
delta   = 0.01       # arch height (m)
L       = 0.1        # span (m)
B       = 0.01       # beam width (m)
H       = 0.01       # beam height (m)
sigma_b = 100e6      # hard‑layer strength (Pa)   (≈100 MPa, as in paper text)
tau_s   = 5e6        # interfacial shear strength (Pa)
gamma   = 10.0       # surface energy (J/m^2)

# Reference moment of inertia of homogeneous PASB.
I_z0 = B * H**3 / 12.0

# Column header (must match output_contract).
header = (
    "V_f,rho,Phi,lambda,h2_over_H,delta,L,B,H,"
    "sigma_b,tau_s,gamma,"
    "E_ratio,I_z,S_zmax,kappa,sigma_max,tau_max,P1,P2,chi,L_c,"
    "W_PASB,W_MSCB"
)
print(header)

# Helper to compute a single row.
def compute_row(V_f, rho, Phi, lam, h2_over_H):
    h2 = h2_over_H * H
    # Effective modulus ratio Eq.(3)
    num = (1.0 - Phi) * Phi * rho**2 * V_f**2
    den = (1.0 - V_f) * lam + (1.0 - Phi) * Phi * rho**2 * V_f
    E_ratio = num / den if den != 0 else 0.0

    # Cross‑sectional properties Eqs.(6a),(6b)
    I_z = (B * H / 12.0) * (
        (H - h2) * (H - 2.0 * h2) * V_f + (3.0 * H - 2.0 * h2) * h2
    )
    S_zmax = (B / 8.0) * (
        4.0 * H * h2 - 4.0 * h2**2 + (H - h2)**2 * V_f
        - (2.0 / V_f) * (H - h2) * h2
    )

    # Bending stiffness ratio Eq.(7)
    kappa = E_ratio * I_z / I_z0

    # Maximum stresses at centre (x = L/2, φ = 0) for unit load P = 1 N.
    # (Used here as an intermediate quantity; the checker may recompute similarly.)
    P_unit = 1.0
    sigma_max = P_unit * H * L / (8.0 * I_z)
    tau_max   = P_unit * S_zmax / (2.0 * I_z * B)

    # Critical loads.
    P1 = 8.0 * I_z * sigma_b / (H * L)          # brittle fracture, Eq.(12)
    P2 = 2.0 * I_z * tau_s * B / S_zmax         # interfacial shear, Eq.(14)
    P0 = 8.0 * I_z0 * sigma_b / (H * L)         # PASB critical load
    chi = min(P1, P2) / P0                       # bending strength ratio Eq.(15)

    # Plastic region length L_c, Eq.(19).
    # Compute argument of square root; if negative, no plastic zone.
    const = (16.0 * S_zmax**2 * sigma_b**2) / (H**2 * L**2 * B**2 * tau_s**2)
    arg = const - 1.0
    if arg >= 0.0:
        L_c = L - (L**2 / (4.0 * delta)) * np.sqrt(arg)
    else:
        L_c = 0.0

    # Fracture energy of PASB, Eq.(20).
    W_PASB = gamma * H * B

    # Fracture energy of MSCB, Eq.(23).
    # Number of layers from Eq.(5) (float) and hard‑layer thickness h1.
    n_layers = (H / h2 - 1.0) * V_f + 1.0          # Eq.(5)
    h1 = (H - (n_layers - 1.0) * h2) / n_layers   # consistent with V_f
    l = rho * h1                                    # hard platelet length
    if l > 0 and L_c > 0:
        m = L_c / l
    else:
        m = 0.0
    Vb = 1.0 / 3.0
    S_prime = 0.5 * Phi * rho * V_f * H            # Eq.(22)
    W_MSCB = m * S_prime * Vb * B * gamma           # Eq.(23)

    return (
        f"{V_f},{rho},{Phi},{lam},{h2_over_H},"
        f"{delta},{L},{B},{H},"
        f"{sigma_b},{tau_s},{gamma},"
        f"{E_ratio},{I_z},{S_zmax},{kappa},{sigma_max},{tau_max},{P1},{P2},{chi},{L_c},"
        f"{W_PASB},{W_MSCB}"
    )

# Loop over grid and emit rows.
for V_f in V_f_vals:
    for rho in rho_vals:
        for Phi in Phi_vals:
            for lam in lambda_vals:
                for hoH in h2_over_H_vals:
                    row = compute_row(V_f, rho, Phi, lam, hoH)
                    print(row)
