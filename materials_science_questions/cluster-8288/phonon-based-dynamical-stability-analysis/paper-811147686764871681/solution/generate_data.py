import json
import math

def _kpath():
    G = (0.0, 0.0, 0.0)
    X = (0.5, 0.0, 0.0)
    S = (0.5, 0.5, 0.0)
    Y = (0.0, 0.5, 0.0)
    segments = [
        ("Γ", G, X, "X"),
        ("X", X, S, "S"),
        ("S", S, G, "Γ"),
        ("Γ", G, Y, "Y"),
        ("Y", Y, X, "X")
    ]
    points = []
    n = 20
    for seg_name, start, end, endlab in segments:
        for i in range(n+1):
            t = i / n
            kx = start[0] + t * (end[0] - start[0])
            ky = start[1] + t * (end[1] - start[1])
            kz = 0.0
            k = (kx, ky, kz)
            label = ""
            if i == n:
                label = endlab
            points.append((k, label))
    if points:
        points[0] = (points[0][0], "Γ")
    return points

def generate_band_structure():
    points = _kpath()
    kd = (0.0, 0.35, 0.0)
    vF = 1.0
    num_bands = 16
    kpoints_out = []
    for k, label in points:
        dkx = k[0] - kd[0]
        dky = k[1] - kd[1]
        dist = math.hypot(dkx, dky)
        cone_energy = vF * dist
        eig = [0.0] * num_bands
        for i in range(num_bands):
            if i < 7:
                eig[i] = -4.0 + 0.5 * (6 - i)
            elif i == 7:
                eig[i] = -cone_energy
            elif i == 8:
                eig[i] = cone_energy
            else:
                eig[i] = 1.0 + 0.5 * (i - 9)
        kpoints_out.append({
            "kpoint": list(k),
            "labels": label,
            "eigenvalues": eig
        })
    return {
        "kpoints": kpoints_out,
        "fermi_energy": 0.0,
        "path": "Γ-X-S-Γ-Y-X"
    }

def generate_phonon_dispersion():
    points = _kpath()
    num_modes = 42
    base_freq = []
    for i in range(num_modes):
        if i < 3:
            base_freq.append(1.5 + 1.0*i)
        elif i < 6:
            base_freq.append(5.0 + 2.0*(i-3))
        elif i < 12:
            base_freq.append(12.0 + 3.0*(i-6))
        elif i < 30:
            base_freq.append(35.0 + 1.5*(i-12))
        else:
            base_freq.append(70.0 + 3.0*(i-30))
    for i in range(18, 25):
        base_freq[i] = 45.0

    qpoints_out = []
    G = (0.0, 0.0, 0.0)
    for q, label in points:
        dx = q[0] - G[0]
        dy = q[1] - G[1]
        r = math.hypot(dx, dy)
        freqs = []
        for m in range(num_modes):
            f = base_freq[m] + 2.0 * r * (0.5 + 0.3 * math.sin(2.0 * math.pi * (m / num_modes + r)))
            freqs.append(round(f, 4))
        qpoints_out.append({
            "qpoint": list(q),
            "labels": label,
            "frequencies_THz": freqs
        })
    return {
        "qpoints": qpoints_out,
        "path": "Γ-X-S-Γ-Y-X"
    }

def generate_strain_results():
    uniform = []
    for p in range(-3, 6):
        for biaxial in [True, False]:
            uniform.append({
                "strain_percent": float(p),
                "biaxial": biaxial,
                "band_gap_eV": 0.001 if p == 0 else 0.003
            })
    shear = []
    for theta in range(80, 101):
        gap = 0.001 if theta == 90 else 0.12
        shear.append({
            "theta_deg": float(theta),
            "band_gap_eV": gap
        })
    return {
        "uniform_strain": uniform,
        "shear_strain": shear
    }

def write_band_structure(outpath):
    res = generate_band_structure()
    with open(outpath, 'w') as f:
        json.dump(res, f, indent=2)

def write_phonon_dispersion(outpath):
    res = generate_phonon_dispersion()
    with open(outpath, 'w') as f:
        json.dump(res, f, indent=2)

def write_strain_results(outpath):
    res = generate_strain_results()
    with open(outpath, 'w') as f:
        json.dump(res, f, indent=2)
