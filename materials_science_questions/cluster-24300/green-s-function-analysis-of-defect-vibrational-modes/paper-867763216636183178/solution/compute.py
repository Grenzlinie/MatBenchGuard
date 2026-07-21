import csv, math, sys, os

OMEGA_R = 1.0
OMEGA_T = 1.4
OMEGA_MAX = 2.0
C = 0.25

T = 300.0
VS = 1200.0
KB = 1.380649e-23
PI = math.pi

def alpha(omega):
    o2 = omega * omega
    oR2 = OMEGA_R * OMEGA_R
    oT2 = OMEGA_T * OMEGA_T
    omax2 = OMEGA_MAX * OMEGA_MAX
    num = (o2 - oR2)**2 * (omax2 - o2)
    den = num + C * o2 * (o2 - oT2)**2
    return num / den if den != 0.0 else 0.0

def write_csv(path):
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['frequency', 'alpha'])
        npts = 1000
        for i in range(npts + 1):
            w = OMEGA_MAX * i / npts
            writer.writerow([w, alpha(w)])

def compute_G():
    # use classical limit (hbar*omega << kT) for all omega in [0,2]
    # G = (kB / (8*pi^2 * v_s^2)) * integral_0^omega_max omega^2 * alpha(omega) domega
    N = 20000
    dw = OMEGA_MAX / N
    s = 0.0
    for i in range(N):
        w = (i + 0.5) * dw   # midpoint
        s += (w * w) * alpha(w) * dw
    G = (KB / (8 * PI**2 * VS**2)) * s
    return G

def write_txt(path):
    G = compute_G()
    with open(path, 'w') as f:
        f.write(str(G))

if __name__ == '__main__':
    args = sys.argv
    if '--csv' in args:
        idx = args.index('--csv')
        write_csv(args[idx+1])
    if '--txt' in args:
        idx = args.index('--txt')
        write_txt(args[idx+1])