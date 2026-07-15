import numpy as np
import csv
import math

k_B_eV = 8.617333262145e-5
Ry_eV = 13.605693122994
k_B_Ry = k_B_eV / Ry_eV
T = 300.0

Z_d_data = {'V': 3.50, 'Cr': 4.50, 'Mn': 5.50, 'Fe': 6.50}
R_d_data = {'V': 1.85, 'Cr': 1.70, 'Mn': 1.63, 'Fe': 1.51}
Omega_a_data = {'V': 93.54, 'Cr': 81.54, 'Mn': 82.59, 'Fe': 79.48}
n_d_data = {'V': 20.95, 'Cr': 9.52, 'Mn': 21.23, 'Fe': 41.63}
Nc_map = {'bcc': 8, 'fcc': 12, 'hcp': 12}

def shells_bcc(a, max_n=15):
    sites = []
    for nx in range(-max_n, max_n+1):
        for ny in range(-max_n, max_n+1):
            for nz in range(-max_n, max_n+1):
                dx = nx
                dy = ny
                dz = nz
                sites.append((dx*dx + dy*dy + dz*dz) * a*a)
                dx = nx + 0.5
                dy = ny + 0.5
                dz = nz + 0.5
                sites.append((dx*dx + dy*dy + dz*dz) * a*a)
    dist_sq = np.array(sites)
    dist_sq.sort()
    shells = []
    tol = 1e-9 * a*a
    i = 0
    while i < len(dist_sq):
        val = dist_sq[i]
        count = 1
        j = i+1
        while j < len(dist_sq) and abs(dist_sq[j] - val) < tol:
            count += 1
            j += 1
        if val > 0:
            dist = math.sqrt(val)
            shells.append((dist, count))
        i = j
    return shells[:max_shells]

def shells_fcc(a, max_n=15):
    sites = []
    for nx in range(-max_n, max_n+1):
        for ny in range(-max_n, max_n+1):
            for nz in range(-max_n, max_n+1):
                for (ox, oy, oz) in [(0,0,0),(0,0.5,0.5),(0.5,0,0.5),(0.5,0.5,0)]:
                    dx = nx + ox
                    dy = ny + oy
                    dz = nz + oz
                    sites.append((dx*dx + dy*dy + dz*dz) * a*a)
    dist_sq = np.array(sites)
    dist_sq.sort()
    shells = []
    tol = 1e-9 * a*a
    i = 0
    while i < len(dist_sq):
        val = dist_sq[i]
        count = 1
        j = i+1
        while j < len(dist_sq) and abs(dist_sq[j] - val) < tol:
            count += 1
            j += 1
        if val > 0:
            dist = math.sqrt(val)
            shells.append((dist, count))
        i = j
    return shells[:max_shells]

def shells_hcp(a, max_n=15):
    c = a * math.sqrt(8.0/3.0)
    a1 = np.array([a, 0.0, 0.0])
    a2 = np.array([a*0.5, a*math.sqrt(3.0)/2, 0.0])
    a3 = np.array([0.0, 0.0, c])
    sites = []
    max_range = 10
    for u in range(-max_range, max_range+1):
        for v in range(-max_range, max_range+1):
            for w in range(-max_range, max_range+1):
                frac = np.array([u, v, w])
                coord = a1*frac[0] + a2*frac[1] + a3*frac[2]
                sites.append(np.dot(coord, coord))
                frac2 = np.array([u + 2.0/3.0, v + 1.0/3.0, w + 0.5])
                coord2 = a1*frac2[0] + a2*frac2[1] + a3*frac2[2]
                sites.append(np.dot(coord2, coord2))
    dist_sq = np.array(sites)
    dist_sq.sort()
    shells = []
    tol = 1e-9 * a*a
    i = 0
    while i < len(dist_sq):
        val = dist_sq[i]
        count = 1
        j = i+1
        while j < len(dist_sq) and abs(dist_sq[j] - val) < tol:
            count += 1
            j += 1
        if val > 0:
            dist = math.sqrt(val)
            shells.append((dist, count))
        i = j
    return shells[:max_shells]

def Ud(R, Z_d, R_d, N_eff):
    term1 = - (Z_d * (1 - Z_d/10) * math.sqrt(12.0 / N_eff) * (56.12 / math.pi) * R_d**3 / R**5)
    term2 = (450.0 / math.pi**2) * Z_d * R_d**6 / R**8
    term3 = math.sqrt(1.0/137.0) / R**3
    return term1 + term2 + term3

elements = ['V','Cr','Mn','Fe']
structures = ['bcc','fcc','hcp']
methods = ['Nc','extended']
max_shells = 15

shells = {}
for el in elements:
    Omega = Omega_a_data[el]
    a_bcc = (2*Omega)**(1/3)
    a_fcc = (4*Omega)**(1/3)
    a_hcp = (math.sqrt(2)*Omega)**(1/3)
    shells[(el,'bcc')] = shells_bcc(a_bcc, max_n=15)[:max_shells]
    shells[(el,'fcc')] = shells_fcc(a_fcc, max_n=15)[:max_shells]
    shells[(el,'hcp')] = shells_hcp(a_hcp, max_n=15)[:max_shells]

free_ene = {}
for el in elements:
    Z_d = Z_d_data[el]
    R_d = R_d_data[el]
    n_d = n_d_data[el]
    S_const = (math.pi**2 / 3) * k_B_Ry**2 * n_d * T
    for struct in structures:
        sh_list = shells[(el, struct)]
        for method in methods:
            cumul = - T * S_const
            cum_list = []
            for R, N in sh_list:
                if method == 'Nc':
                    U = Ud(R, Z_d, R_d, Nc_map[struct])
                else:
                    U = Ud(R, Z_d, R_d, N)
                cumul += 0.5 * U * N
                cum_list.append(cumul)
            free_ene[(el, struct, method)] = cum_list

with open('/app/outputs/free_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['element','structure','shell','method','N_atoms','interatomic_distance','pair_potential_Ud','cumulative_free_energy_Fd'])
    for el in elements:
        for struct in structures:
            sh_list = shells[(el, struct)]
            for method in methods:
                cum_list = free_ene[(el, struct, method)]
                Z_d = Z_d_data[el]
                R_d = R_d_data[el]
                for i, (R, N) in enumerate(sh_list):
                    if method == 'Nc':
                        U_val = Ud(R, Z_d, R_d, Nc_map[struct])
                    else:
                        U_val = Ud(R, Z_d, R_d, N)
                    writer.writerow([el, struct, i+1, method, N, R, U_val, cum_list[i]])

with open('/app/outputs/energy_differences.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['element','method','shell','delta_F_fcc_bcc','delta_F_fcc_hcp'])
    for el in elements:
        for method in methods:
            fcc_cum = free_ene[(el, 'fcc', method)]
            bcc_cum = free_ene[(el, 'bcc', method)]
            hcp_cum = free_ene[(el, 'hcp', method)]
            num_shells = min(len(fcc_cum), len(bcc_cum), len(hcp_cum), max_shells)
            for i in range(num_shells):
                sh = i+1
                delta_fcc_bcc = fcc_cum[i] - bcc_cum[i]
                delta_fcc_hcp = fcc_cum[i] - hcp_cum[i]
                writer.writerow([el, method, sh, delta_fcc_bcc, delta_fcc_hcp])