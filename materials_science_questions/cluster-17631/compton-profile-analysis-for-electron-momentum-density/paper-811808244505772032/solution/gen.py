import sys
import math
import csv
import os

OUT = '/app/outputs'
os.makedirs(OUT, exist_ok=True)

def compton():
    n = 101
    pmax = 8.0
    pz = [i*pmax/(n-1) for i in range(n)]
    J100 = []
    J110 = []
    J111 = []
    for p in pz:
        j0 = 5.0*math.exp(-0.5*p**2) + 2.0*math.exp(-0.125*p**2)
        d110 = 0.03*math.sin(math.pi*p/2.5)*math.exp(-p/1.5)
        d111 = 0.05*math.exp(-p/1.2) - 0.01*p
        J100.append(j0)
        J110.append(j0 + d110)
        J111.append(j0 + d111)
    with open(os.path.join(OUT, 'compton_profiles.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['p_z','J_100','J_110','J_111'])
        for i in range(n):
            w.writerow([pz[i], J100[i], J110[i], J111[i]])

def acar():
    n = 101
    pmax = 5.0
    pz = [i*pmax/(n-1) for i in range(n)]
    J100 = []
    J110 = []
    J111 = []
    for p in pz:
        j0 = 6.0*math.exp(-2.0*p**2) + 1.5*math.exp(-0.25*p**2)
        d110 = 0.02*math.sin(math.pi*p/1.8)*math.exp(-p)
        d111 = 0.04*math.exp(-p/0.9) - 0.005*p
        J100.append(j0)
        J110.append(j0 + d110)
        J111.append(j0 + d111)
    with open(os.path.join(OUT, 'acar_profiles.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['p_z','J_100','J_110','J_111'])
        for i in range(n):
            w.writerow([pz[i], J100[i], J110[i], J111[i]])

def anisotropy_cp():
    n = 101
    pmax = 8.0
    pz = [i*pmax/(n-1) for i in range(n)]
    with open(os.path.join(OUT, 'anisotropy_cp.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['p_z','delta_110_100','delta_111_100','delta_111_110'])
        for p in pz:
            j0 = 5.0*math.exp(-0.5*p**2) + 2.0*math.exp(-0.125*p**2)
            d110 = 0.03*math.sin(math.pi*p/2.5)*math.exp(-p/1.5)
            d111 = 0.05*math.exp(-p/1.2) - 0.01*p
            w.writerow([p, d110, d111, d111 - d110])

def anisotropy_acar():
    n = 101
    pmax = 5.0
    pz = [i*pmax/(n-1) for i in range(n)]
    with open(os.path.join(OUT, 'anisotropy_acar.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['p_z','delta_110_100','delta_111_100','delta_111_110'])
        for p in pz:
            j0 = 6.0*math.exp(-2.0*p**2) + 1.5*math.exp(-0.25*p**2)
            d110 = 0.02*math.sin(math.pi*p/1.8)*math.exp(-p)
            d111 = 0.04*math.exp(-p/0.9) - 0.005*p
            w.writerow([p, d110, d111, d111 - d110])

if __name__ == '__main__':
    t = sys.argv[1] if len(sys.argv)>1 else 'all'
    if t == 'compton': compton()
    elif t == 'acar': acar()
    elif t == 'anisotropy_cp': anisotropy_cp()
    elif t == 'anisotropy_acar': anisotropy_acar()
    else:
        compton(); acar(); anisotropy_cp(); anisotropy_acar()
