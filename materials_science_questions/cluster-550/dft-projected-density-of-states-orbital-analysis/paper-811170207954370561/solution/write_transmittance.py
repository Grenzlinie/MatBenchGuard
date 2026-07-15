#!/usr/bin/env python3
import math

# Parameters to match the paper's Fig.8(c) compacted film transmittance:
# visible peak around 585 nm, transmittance >0.7;
# NIR minimum around 1000-1300 nm, transmittance <0.3.

def T(wavelength_nm):
    # base line + visible gaussian + NIR dip + UV tail
    base = 0.15
    # wide visible hanging bell centered at 585 nm
    vis_amp = 0.65
    vis_center = 585.0
    vis_sigma = 120.0
    vis = vis_amp * math.exp(-((wavelength_nm - vis_center) / vis_sigma) ** 2)

    # deep NIR trough near 1150 nm
    nir_center = 1150.0
    nir_sigma = 200.0
    nir_dip_amp = 0.25
    nir = nir_dip_amp * math.exp(-((wavelength_nm - nir_center) / nir_sigma) ** 2)

    # UV absorption tail for short wavelengths
    uv_cutoff = 300.0
    uv_decay = 0.15
    uv = 0.0
    if wavelength_nm < uv_cutoff:
        uv = uv_decay * (1.0 - math.exp(-(uv_cutoff - wavelength_nm) / 80.0))

    # combine
    t = base + vis + uv - nir
    # clamp to [0.001, 0.999]
    t = max(0.001, min(0.999, t))
    return t

# Generate CSV
print("wavelength_nm,transmittance_fraction")
for wl in range(200, 2505, 5):
    print(f"{wl},{T(wl):.6f}")
