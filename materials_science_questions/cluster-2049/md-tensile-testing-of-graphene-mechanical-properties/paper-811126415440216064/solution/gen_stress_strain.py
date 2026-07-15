import sys
import csv

def generate_curve(young_modulus, strain_peaks):
    """
    young_modulus: GPa
    strain_peaks: list of (strain, stress) waypoints from 0.02 onwards.
                  The first element is the elastic limit (0.02, young*0.02).
                  Subsequent waypoints define crests, valleys, and failure.
    """
    # initial elastic points up to 0.02
    init_strains = []
    init_stresses = []
    s = 0.0
    step = 0.002
    while s <= 0.02 + 1e-9:
        init_strains.append(s)
        init_stresses.append(young_modulus * s)
        s += step

    # build waypoints starting at 0.02
    wpts = [(0.02, young_modulus * 0.02)] + strain_peaks
    strains = []
    stresses = []
    for i in range(len(wpts) - 1):
        s1, v1 = wpts[i]
        s2, v2 = wpts[i+1]
        num_steps = max(10, int((s2 - s1) / 0.002))
        for j in range(num_steps):
            t = (j + 1) / num_steps
            strain_val = s1 + t * (s2 - s1)
            stress_val = v1 + t * (v2 - v1)
            strains.append(strain_val)
            stresses.append(stress_val)
    return init_strains + strains, init_stresses + stresses

# Conditions: (thickness_nm, temperature_K, young_modulus, strain_peaks)
# strain_peaks define the post-elastic shape: crests, dips, final zero.
conditions = [
    (1, 200, 260, [(0.10, 30), (0.14, 28), (0.20, 42), (0.25, 0)]),
    (1, 300, 250, [(0.12, 32), (0.16, 28), (0.22, 40), (0.27, 0)]),
    (1, 500, 230, [(0.14, 28), (0.18, 25), (0.24, 35), (0.28, 0)]),
    (1, 700, 200, [(0.15, 22), (0.20, 19), (0.25, 28), (0.30, 0)]),
    (1, 900, 150, [(0.18, 14), (0.23, 12), (0.28, 18), (0.32, 0)]),
    (2, 300, 130, [(0.10, 26), (0.14, 20), (0.20, 24), (0.28, 0)]),
    (3, 300, 110, [(0.10, 22), (0.15, 18), (0.21, 20), (0.30, 0)]),
    (4, 300, 100, [(0.12, 20), (0.17, 17), (0.22, 18.5), (0.32, 0)]),
    (5, 300, 98,  [(0.14, 19.8), (0.19, 17.0), (0.24, 18.0), (0.33, 0)]),
    (6, 300, 97,  [(0.15, 19.7), (0.20, 17.0), (0.25, 17.8), (0.34, 0)]),
]

outpath = sys.argv[1]
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['thickness_nm', 'temperature_K', 'strain', 'stress_GPa'])
    for thick, temp, young, peaks in conditions:
        strains, stresses = generate_curve(young, peaks)
        for s, val in zip(strains, stresses):
            writer.writerow([thick, temp, round(s, 6), round(val, 4)])
