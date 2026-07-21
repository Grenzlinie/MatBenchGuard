import sys
import csv
import math

def band_gap():
    # transition diameters (nm) and bulk overlap (meV)
    d_bin = 30.0
    d_tri = 45.0
    d_bis = 81.0
    overlap = 38.0
    A_bin = overlap * d_bin**2
    A_tri = overlap * d_tri**2
    A_bis = overlap * d_bis**2

    writer = csv.writer(sys.stdout)
    writer.writerow(['diameter_nm', 'binary_gap_meV', 'trigonal_gap_meV', 'bisectrix_gap_meV'])
    for d in range(10, 201):
        d_nm = float(d)
        gap_bin = A_bin / d_nm**2 - overlap
        gap_tri = A_tri / d_nm**2 - overlap
        gap_bis = A_bis / d_nm**2 - overlap
        writer.writerow([d_nm, round(gap_bin, 4), round(gap_tri, 4), round(gap_bis, 4)])

def zt():
    # key points for piecewise linear interpolation (diameter_nm, ZT)
    key_d = [20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 60.0, 80.0, 100.0, 150.0, 200.0]
    key_zt = [1.60, 1.35, 1.10, 0.85, 0.62, 0.50, 0.40, 0.28, 0.15, 0.08, 0.03, 0.02]

    def interp(d_val):
        if d_val <= key_d[0]:
            return key_zt[0]
        if d_val >= key_d[-1]:
            return key_zt[-1]
        for i in range(len(key_d) - 1):
            if key_d[i] <= d_val <= key_d[i + 1]:
                t = (d_val - key_d[i]) / (key_d[i + 1] - key_d[i])
                return key_zt[i] + t * (key_zt[i + 1] - key_zt[i])
        return 0.0

    writer = csv.writer(sys.stdout)
    writer.writerow(['diameter_nm', 'ZT'])
    for d in range(20, 201):
        d_nm = float(d)
        zt_val = interp(d_nm)
        writer.writerow([d_nm, round(zt_val, 4)])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'band_gap':
        band_gap()
    elif cmd == 'zt':
        zt()
    else:
        sys.exit(1)
