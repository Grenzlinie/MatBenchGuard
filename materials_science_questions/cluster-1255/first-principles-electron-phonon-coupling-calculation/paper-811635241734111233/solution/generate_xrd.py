import math

# Structure: P6_3/mmc PtH, a=2.70 A, c=4.53 A, wavelength 0.3344 A
a = 2.70
c = 4.53
wavelength = 0.3344

# Pt at Wyckoff 2c: (1/3, 2/3, 1/4) and (2/3, 1/3, 3/4)
# H at 2a: (0,0,0) and (0,0,1/2) - H scattering negligible, so omit from structure factor
# Pt scattering factor treated as constant (approximate atomic number as weight)
f_Pt = 78.0

# Index range for h,k,l
hkl_range = (
    [(h, k, l) for h in range(-3, 4) for k in range(-3, 4) for l in range(-4, 5)
     if h != 0 or k != 0 or l != 0]
)

peaks = []
for h, k, l in hkl_range:
    # d-spacing in hexagonal system
    d_inv_sq = (4.0/3.0)*(h*h + h*k + k*k)/(a*a) + (l*l)/(c*c)
    if d_inv_sq == 0:
        continue
    d = 1.0 / math.sqrt(d_inv_sq)
    # Bragg's law: n*lambda = 2d sin(theta) => theta = arcsin(lambda/(2d))
    sin_theta = wavelength / (2.0 * d)
    if sin_theta > 1.0 or sin_theta < -1.0:
        continue
    two_theta = 2.0 * math.degrees(math.asin(sin_theta))
    if two_theta > 80:  # limit to reasonable range
        continue

    # Structure factor F(hkl) for two Pt sites
    # Phase for first site: 2*pi*(h/3 + 2k/3 + l/4)
    # Phase for second site: 2*pi*(2h/3 + k/3 + 3l/4)
    # Factor: exp(i*phase1) + exp(i*phase2)
    phase1 = 2*math.pi * (h/3.0 + 2*k/3.0 + l/4.0)
    phase2 = 2*math.pi * (2*h/3.0 + k/3.0 + 3*l/4.0)
    # Compute sum of complex exponentials
    cr = math.cos(phase1) + math.cos(phase2)
    ci = math.sin(phase1) + math.sin(phase2)
    F_sq = f_Pt * f_Pt * (cr*cr + ci*ci)

    # Multiplicity: for hexagonal, systematic extinctions? P6_3/mmc has no general extinction for these sites,
    # but some conditions apply: for (h,k,l) as general positions, multiplicity is based on Laue class 6/mmm.
    # We'll approximate multiplicity as 1 for now; the relative intensities will still be meaningful.
    multiplicity = 1
    # Lorentz-polarization factor (simplified): LP = (1+cos^2(2theta))/ (sin^2(theta)cos(theta))
    theta_rad = two_theta / 2.0 * math.pi / 180.0
    LP = (1 + math.cos(two_theta * math.pi / 180.0)**2) / (math.sin(theta_rad)**2 * math.cos(theta_rad))
    intensity = F_sq * multiplicity * LP

    peaks.append((two_theta, intensity, h, k, l))

# Sort by two_theta
peaks.sort(key=lambda x: x[0])

# Normalize intensity
max_I = max(p[1] for p in peaks) if peaks else 1.0
# Filter very weak peaks
peaks = [p for p in peaks if p[1]/max_I > 0.01]

# Write CSV
print("two_theta,intensity")
for p in peaks:
    # Round to reasonable precision
    print(f"{p[0]:.3f},{p[1]/max_I:.4f}")
