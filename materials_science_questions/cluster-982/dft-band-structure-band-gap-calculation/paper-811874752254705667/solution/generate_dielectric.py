import json
import math

def generate():
    energies = [i*0.05 for i in range(int(13/0.05)+1)]
    def gauss(x, mu, sigma, amp):
        return amp * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

    peaks = [
        (5.0, 0.3, 5.0),
        (5.45, 0.25, 4.0),
        (7.0, 0.5, 6.0),
        (8.5, 0.4, 5.5),
        (10.0, 0.5, 4.5),
        (11.0, 0.4, 3.0),
    ]
    base = [0.001] * len(energies)
    for mu, sigma, amp in peaks:
        for i, e in enumerate(energies):
            base[i] += gauss(e, mu, sigma, amp)

    eps_xx = [v for v in base]
    eps_yy = []
    eps_zz = []
    for e, v in zip(energies, base):
        if e <= 4.0:
            eps_yy.append(v)
            eps_zz.append(v)
        else:
            offset_y = (e - 4.0) * 0.15
            offset_z = (e - 4.0) * 0.25
            eps_yy.append(v + offset_y)
            eps_zz.append(v + offset_z)

    def max_relative_diff(e_list, eps_xx, eps_yy, eps_zz):
        maxval = 0.0
        for i, e in enumerate(e_list):
            a = eps_xx[i]
            b = eps_yy[i]
            c = eps_zz[i]
            denom = max(a, b, c) + 1e-12
            d_xy = abs(a - b) / denom
            d_xz = abs(a - c) / denom
            d_yz = abs(b - c) / denom
            maxval = max(maxval, d_xy, d_xz, d_yz)
        return maxval

    isotropic = True
    anisotropic = False
    below_indices = [i for i, e in enumerate(energies) if e <= 4.0]
    above_indices = [i for i, e in enumerate(energies) if e > 4.0]
    if below_indices:
        max_below = max_relative_diff([energies[i] for i in below_indices],
                                      [eps_xx[i] for i in below_indices],
                                      [eps_yy[i] for i in below_indices],
                                      [eps_zz[i] for i in below_indices])
        isotropic = max_below < 0.1
    if above_indices:
        max_above = max_relative_diff([energies[i] for i in above_indices],
                                      [eps_xx[i] for i in above_indices],
                                      [eps_yy[i] for i in above_indices],
                                      [eps_zz[i] for i in above_indices])
        anisotropic = max_above > 0.1

    result = {
        "energies_eV": energies,
        "eps_xx": eps_xx,
        "eps_yy": eps_yy,
        "eps_zz": eps_zz,
        "isotropic_below_4eV": isotropic,
        "anisotropic_above_4eV": anisotropic
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    generate()