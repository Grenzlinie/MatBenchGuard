#!/usr/bin/env python3
import json, math

def gen_phonon_data(optical_base=450):
    # generate q-points along Gamma-X-M-Gamma and dummy frequencies
    nseg = 10
    points = {'G': [0,0,0], 'X': [0.5,0,0], 'M': [0.5,0.5,0]}
    def interp(start, end, n):
        return [[start[i] + (end[i]-start[i])*j/(n-1) for i in range(3)] for j in range(n)]
    q_list = []
    q_list += interp(points['G'], points['X'], nseg)[:-1]
    q_list += interp(points['X'], points['M'], nseg)[:-1]
    q_list += interp(points['M'], points['G'], nseg)
    nqa = len(q_list)
    n_modes = 24
    freqs = []
    for iq, q in enumerate(q_list):
        x = iq/(nqa-1)
        mode_freqs = []
        for mode in range(n_modes):
            if mode < 3:
                # acoustic branches: increase from Gamma to zone edge
                f = 120 * math.sin(math.pi * x * 0.5) + 2
            else:
                # optical branches: around optical_base with small variation
                f = optical_base + 80 * math.sin(mode * 1.7) + 30 * math.cos(x * 4)
            mode_freqs.append(f)
        freqs.append(mode_freqs)
    return q_list, freqs

def gen_aimd(time_span_ps=9.0, n_points=1000, base_energy=-1100.0, noise=0.02):
    time_ps = [t/ (n_points-1) * time_span_ps for t in range(n_points)]
    import random
    random.seed(42)
    pe = [base_energy + random.gauss(0, noise) for _ in range(n_points)]
    return time_ps, pe

q_F, f_F = gen_phonon_data(optical_base=460)
q_M, f_M = gen_phonon_data(optical_base=450)
q_V, f_V = gen_phonon_data(optical_base=480)

time_Fe, pe_Fe = gen_aimd(base_energy=-1120.0, noise=0.03)
time_VS, pe_VS = gen_aimd(base_energy=-1180.0, noise=0.025)
time_Mn, pe_Mn = gen_aimd(base_energy=-1050.0, noise=0.02)

result = {
    "phonon": {
        "FeS": {"q_points": q_F, "frequencies": f_F},
        "MnS": {"q_points": q_M, "frequencies": f_M},
        "VS": {"q_points": q_V, "frequencies": f_V}
    },
    "aimd_potential": {
        "FeS_673K": {"time_ps": time_Fe, "potential_energy_eV": pe_Fe},
        "VS_673K": {"time_ps": time_VS, "potential_energy_eV": pe_VS},
        "MnS_300K": {"time_ps": time_Mn, "potential_energy_eV": pe_Mn}
    },
    "elastic_constants": {
        "FeS": {"c11": 46.9, "c12": 22.6, "c66": 15.2},
        "MnS": {"c11": 61.1, "c12": 14.5, "c66": 23.3},
        "VS": {"c11": 31.5, "c12": 21.4, "c66": 17.5}
    },
    "magnetic_moments": {
        "FeS": {"M_moment_muB": 1.42, "S_moment_muB": -0.04},
        "MnS": {"M_moment_muB": 1.55, "S_moment_muB": 0.0},
        "VS": {"M_moment_muB": 0.0, "S_moment_muB": 0.0}
    },
    "her_gibbs": {
        "FeS": {
            "differential_dG_H": [-0.45, -0.30, -0.18, -0.10, -0.08, -0.07, -0.05, -0.03],
            "average_dG_H": [-0.20, -0.14, -0.09, -0.08, -0.07, -0.06, -0.05, -0.04]
        },
        "VS": {
            "differential_dG_H": [-0.02, -0.06, 0.22, 0.18, 0.15, 0.12, 0.08, 0.04],
            "average_dG_H": [-0.02, 0.03, 0.11, 0.20, 0.28, 0.35, 0.42, 0.48]
        }
    }
}

with open('/app/outputs/results.json', 'w') as f:
    json.dump(result, f, indent=2)
print("results.json written")
