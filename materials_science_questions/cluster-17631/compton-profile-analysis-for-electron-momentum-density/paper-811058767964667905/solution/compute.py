import json, math

# Constants
h = 6.62607015e-34
m_e = 9.10938356e-31
eV_to_J = 1.602176634e-19

k_F_Al = 2.8  # nm⁻¹
k_V_Si = 2.9  # nm⁻¹
E_G_eV = 1.17

# Compute k_C for Si using h (as per paper)
k_V_Si_m = k_V_Si * 1e9  # nm⁻¹ to m⁻¹
E_G_J = E_G_eV * eV_to_J
term = 2 * m_e * E_G_J / (h * h)
k_C_Si_m = math.sqrt(k_V_Si_m**2 + term)
k_C_Si = k_C_Si_m / 1e9  # back to nm⁻¹

# Free-atom intensities (approximated from paper's thick curves)
free_atom_Al = {0.1:4.2, 0.5:4.6, 1.0:5.2, 2.0:6.2, 3.0:7.2, 4.0:8.2}
free_atom_Si = {0.1:4.0, 0.5:4.4, 1.0:5.0, 2.0:6.0, 3.0:7.0, 4.0:8.0}

s_vals = [0.1, 0.5, 1.0, 2.0, 3.0, 4.0]

def correction_Al(s):
    if s > 2 * k_F_Al:
        return 1.0
    x = s / k_F_Al
    return (3/4) * x - (1/16) * x**3

def gamma_Si(s, kV, kC):
    cos_phi = (kC**2 - kV**2 + s**2) / (2 * kC * s)
    cos_psi = (kV**2 - kC**2 + s**2) / (2 * kV * s)
    term1 = (kC**3 / (2 * kV**3)) * (1 - 1.5 * cos_phi + 0.5 * cos_phi**3)
    term2 = 0.5 * (1 - 1.5 * cos_psi + 0.5 * cos_psi**3)
    return term1 + term2

def correction_Si(s, kV, kC):
    if s <= kC - kV:
        return 0.0
    if s >= kC + kV:
        return 1.0
    g = gamma_Si(s, kV, kC)
    return 1.0 - g

result = []
for s in s_vals:
    corr_Al = correction_Al(s)
    free_Al = free_atom_Al[s]
    result.append({
        "material": "Al",
        "s": s,
        "free_atom_intensity": free_Al,
        "correction_factor": round(corr_Al, 6),
        "corrected_intensity": round(free_Al * corr_Al, 6)
    })
for s in s_vals:
    corr_Si = correction_Si(s, k_V_Si, k_C_Si)
    free_Si = free_atom_Si[s]
    result.append({
        "material": "Si",
        "s": s,
        "free_atom_intensity": free_Si,
        "correction_factor": round(corr_Si, 6),
        "corrected_intensity": round(free_Si * corr_Si, 6)
    })

with open('/app/outputs/corrected_compton_intensities.json', 'w') as f:
    json.dump(result, f, indent=2)
