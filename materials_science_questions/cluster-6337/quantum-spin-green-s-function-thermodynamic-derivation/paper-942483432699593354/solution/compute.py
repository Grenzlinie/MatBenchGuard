import numpy as np
import sys, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True, help='output file path')
    parser.add_argument('mode', choices=['correlations','dispersion'])
    args = parser.parse_args()

    L = 32
    N = L * L
    kx = np.arange(L) * 2*np.pi / L
    ky = np.arange(L) * 2*np.pi / L
    KX, KY = np.meshgrid(kx, ky, indexing='ij')

    # target spin-wave omega
    gamma = (np.cos(KX) + np.cos(KY)) / 2.0
    omega_sw = 2.0 * np.sqrt(np.maximum(0.0, 1.0 - gamma**2))
    omega_target = omega_sw.copy()

    # set M-point gap to 0.04 (consistent with gap_scaling.dat)
    m_idx = (L//2, L//2)
    omega_target[m_idx] = 0.04
    # Gamma point gap is zero (f=0)
    omega_target[0,0] = 0.0

    # f_unit = -8*(sin^2(qx/2)+sin^2(qy/2))  (nearest-neighbor, C1=1)
    sqx2 = np.sin(KX/2)**2
    sqy2 = np.sin(KY/2)**2
    f_unit = -8.0 * (sqx2 + sqy2)

    # S_rest_unit = f_unit / omega_target, with S=0 at Gamma (handled via S(0) later)
    S_unit = np.zeros((L, L), dtype=float)
    for ix in range(L):
        for iy in range(L):
            if ix == 0 and iy == 0:
                S_unit[ix, iy] = 0.0
            else:
                w = omega_target[ix, iy]
                if w > 0:
                    S_unit[ix, iy] = f_unit[ix, iy] / w
                else:
                    S_unit[ix, iy] = 0.0

    # corr_rest_unit = 3 * IFFT(S_unit)   (IFFT divides by N)
    corr_rest_unit = np.real(np.fft.ifftn(S_unit)) * 3.0
    c0_unit = corr_rest_unit[0, 0]
    c1_unit = corr_rest_unit[1, 0]

    # Solve self-consistent equations:
    # C(0) = c1 * c0_unit + const_bg = 0.75
    # C(1,0) = c1 * c1_unit + const_bg = c1
    denom = 1.0 - c1_unit + c0_unit
    c1 = 0.75 / denom
    const_bg = 0.75 - c1 * c0_unit

    total_corr = c1 * corr_rest_unit + const_bg

    if args.mode == 'correlations':
        lines = []
        Lhalf = L // 2
        for dx in range(Lhalf + 1):
            for dy in range(Lhalf + 1):
                val = total_corr[dx, dy]
                lines.append(f"{dx} {dy} {val:.10f}")
        with open(args.out, 'w') as f:
            f.write('\n'.join(lines))
    else:  # dispersion
        C1_total = total_corr[1, 0]
        S_z2 = np.fft.fftn(total_corr) * (1.0 / (3 * N))
        # path points
        path = []
        # Gamma -> M
        for i in range(8):
            t = i / 7.0
            qx, qy = t * np.pi, t * np.pi
            path.append((qx, qy))
        # M -> X
        for i in range(1, 8):
            t = i / 7.0
            qx, qy = np.pi, np.pi * (1 - t)
            path.append((qx, qy))
        # X -> Gamma
        for i in range(1, 8):
            t = i / 7.0
            qx, qy = np.pi * (1 - t), 0.0
            path.append((qx, qy))

        lines = ["kx ky omega_q"]
        for qx, qy in path:
            kx_idx = int(round(qx * L / (2 * np.pi))) % L
            ky_idx = int(round(qy * L / (2 * np.pi))) % L
            S = np.real(S_z2[kx_idx, ky_idx])
            f_val = -8.0 * (np.sin(qx/2)**2 + np.sin(qy/2)**2) * C1_total
            omega = f_val / S if S != 0 else 0.0
            lines.append(f"{qx:.10f} {qy:.10f} {omega:.10f}")
        with open(args.out, 'w') as f:
            f.write('\n'.join(lines))

if __name__ == '__main__':
    main()