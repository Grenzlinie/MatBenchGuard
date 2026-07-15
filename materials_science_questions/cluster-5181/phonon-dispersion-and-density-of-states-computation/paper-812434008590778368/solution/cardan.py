import sys
import math
import csv

R = 0.8

def compute_omega2(kx, ky, kz):
    cx = math.cos(kx); sx = math.sin(kx); c2x = math.cos(2*kx)
    cy = math.cos(ky); sy = math.sin(ky); c2y = math.cos(2*ky)
    cz = math.cos(kz); sz = math.sin(kz); c2z = math.cos(2*kz)

    delta = 1.0 + 0.75*R - cx*cy*cz
    A = delta - 0.75*R*c2x
    B = delta - 0.75*R*c2y
    C = delta - 0.75*R*c2z
    E = sx*sy*cz
    F = sx*cy*sz
    G = cx*sy*sz

    P = -(A + B + C)
    Q = A*B + B*C + C*A - E*E - F*F - G*G
    Rc = -A*B*C - 2*E*F*G + A*G*G + B*F*F + C*E*E

    p = Q - (1.0/3.0)*P*P
    q = (2.0/27.0)*P**3 - (1.0/3.0)*P*Q + Rc
    T = q*q/4.0 + p**3/27.0

    if T > 0:
        # physically should not happen; fallback to zero
        T = 0.0

    if abs(T) < 1e-15:
        # degenerate case
        a = -q/2.0
        if a >= 0:
            y = a**(1.0/3.0)
        else:
            y = -((-a)**(1.0/3.0))
        xp1 = 2.0 * y
        xp2 = -y
        xp3 = -y
    else:
        # T < 0: three real distinct roots via trigonometric form
        a = -q/2.0
        b = math.sqrt(-T)
        r = math.hypot(a, b)
        theta = math.atan2(b, a)
        factor = 2.0 * r**(1.0/3.0)
        xp1 = factor * math.cos(theta/3.0)
        xp2 = factor * math.cos((theta + 2*math.pi)/3.0)
        xp3 = factor * math.cos((theta + 4*math.pi)/3.0)

    shift = P/3.0
    w2 = [xp1 - shift, xp2 - shift, xp3 - shift]
    w2.sort(reverse=True)
    return w2[0], w2[1], w2[2], T


def main():
    mode = sys.argv[1]
    outpath = sys.argv[2]
    npts = 51

    if mode == "100":
        xs = [i * math.pi / (npts-1) for i in range(npts)]
        with open(outpath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["kx","omega2_1","omega2_2","omega2_3","T"])
            for kx in xs:
                o1, o2, o3, T = compute_omega2(kx, 0.0, 0.0)
                writer.writerow([f"{kx:.15f}", f"{o1:.15f}", f"{o2:.15f}", f"{o3:.15f}", f"{T:.15e}"])

    elif mode == "nonsym":
        dir_x, dir_y, dir_z = 1.0, 0.1, 0.2
        norm_dir = math.hypot(dir_x, dir_y, dir_z)
        t_max = math.pi / norm_dir
        ts = [i * t_max / (npts-1) for i in range(npts)]
        with open(outpath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["kx","ky","kz","omega2_1","omega2_2","omega2_3","T"])
            for t in ts:
                kx = dir_x * t
                ky = dir_y * t
                kz = dir_z * t
                o1, o2, o3, T = compute_omega2(kx, ky, kz)
                writer.writerow([f"{kx:.15f}", f"{ky:.15f}", f"{kz:.15f}",
                                 f"{o1:.15f}", f"{o2:.15f}", f"{o3:.15f}", f"{T:.15e}"])

if __name__ == "__main__":
    main()
