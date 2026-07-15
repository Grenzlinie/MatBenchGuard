#!/usr/bin/env python3
import argparse, json, math, random, csv, os

def generate_exafs(output_path):
    k_vals = [2.0 + 0.05 * i for i in range(201)]
    random.seed(42)

    def compute_chi(components, noise_amp=0):
        chi = []
        for k in k_vals:
            s = 0.0
            for amp, freq, phase, damp in components:
                s += amp * math.sin(freq * k + phase) * math.exp(-damp * k)
            if noise_amp > 0:
                s += random.gauss(0, noise_amp)
            chi.append(s)
        return chi

    # Define component parameters (amp, freq, phase, damp) for each edge / composition.
    comp_cu50_cu = [(1.0, 5.5, 0.0, 0.2), (0.8, 8.0, 1.2, 0.3), (0.6, 10.5, 2.0, 0.4)]
    comp_cu45ag10_cu = [(1.0, 5.5, 0.0, 0.2), (0.8, 8.0, 1.2, 0.3), (0.6, 10.5, 2.0, 0.4)]
    comp_cu50_zr = [(0.9, 3.0, 0.5, 0.25), (0.7, 6.0, 2.0, 0.35), (0.5, 9.0, 3.0, 0.5)]
    comp_cu45ag10_zr = [(1.0, 4.0, 1.0, 0.2), (0.6, 7.0, 3.0, 0.3), (0.4, 11.0, 4.0, 0.6)]
    comp_cu40ag20_cu = [(1.2, 5.5, 0.0, 0.1), (0.5, 7.0, 0.0, 0.1)]
    comp_cu40ag20_zr = [(0.8, 3.5, 0.8, 0.3), (0.6, 6.5, 2.5, 0.4)]
    comp_cu45ag10_ag = [(0.7, 4.5, 0.2, 0.15), (0.5, 7.5, 1.5, 0.25)]
    comp_cu40ag20_ag = [(0.8, 4.2, 0.4, 0.2), (0.6, 7.2, 1.8, 0.3)]

    data = {}
    data["Cu50Zr50_Cu_K"] = {"k": k_vals, "chi": compute_chi(comp_cu50_cu, noise_amp=0)}
    data["Cu50Zr50_Zr_K"] = {"k": k_vals, "chi": compute_chi(comp_cu50_zr, noise_amp=0)}
    data["Cu45Zr45Ag10_Cu_K"] = {"k": k_vals, "chi": compute_chi(comp_cu45ag10_cu, noise_amp=0.01)}
    data["Cu45Zr45Ag10_Zr_K"] = {"k": k_vals, "chi": compute_chi(comp_cu45ag10_zr, noise_amp=0)}
    data["Cu45Zr45Ag10_Ag_K"] = {"k": k_vals, "chi": compute_chi(comp_cu45ag10_ag, noise_amp=0)}
    data["Cu40Zr40Ag20_Cu_K"] = {"k": k_vals, "chi": compute_chi(comp_cu40ag20_cu, noise_amp=0)}
    data["Cu40Zr40Ag20_Zr_K"] = {"k": k_vals, "chi": compute_chi(comp_cu40ag20_zr, noise_amp=0)}
    data["Cu40Zr40Ag20_Ag_K"] = {"k": k_vals, "chi": compute_chi(comp_cu40ag20_ag, noise_amp=0)}

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

def generate_voronoi(output_path):
    rows = []
    def add(composition, center, index, frac):
        rows.append((composition, center, index, frac))

    # Cu50Zr50 Cu-centered
    cu50_cu = {"<0 3 6 0>": 0.15, "<0 2 8 0>": 0.08, "<0 2 8 1>": 0.09, "<0 4 4 0>": 0.12,
               "<0 3 6 1>": 0.10, "<0 1 10 2>": 0.09, "<0 2 8 2>": 0.08, "<0 1 10 1>": 0.07, "others": 0.22}
    total = sum(cu50_cu.values())
    for idx, frac in cu50_cu.items():
        add("Cu50Zr50", "Cu", idx, frac/total)
    # Cu50Zr50 Zr-centered
    cu50_zr = {"<0 3 6 0>": 0.05, "<0 2 8 0>": 0.04, "<0 2 8 1>": 0.04, "<0 4 4 0>": 0.05, "others": 0.82}
    total = sum(cu50_zr.values())
    for idx, frac in cu50_zr.items():
        add("Cu50Zr50", "Zr", idx, frac/total)
    # Cu45Zr45Ag10
    cu45_cu = {"<0 3 6 0>": 0.13, "<0 2 8 0>": 0.07, "<0 2 8 1>": 0.11, "<0 4 4 0>": 0.11,
               "<0 3 6 1>": 0.09, "<0 1 10 2>": 0.08, "<0 2 8 2>": 0.07, "<0 1 10 1>": 0.07, "others": 0.27}
    total = sum(cu45_cu.values())
    for idx, frac in cu45_cu.items():
        add("Cu45Zr45Ag10", "Cu", idx, frac/total)
    cu45_zr = {"<0 3 6 0>": 0.04, "<0 2 8 0>": 0.03, "<0 2 8 1>": 0.04, "<0 4 4 0>": 0.04, "others": 0.85}
    total = sum(cu45_zr.values())
    for idx, frac in cu45_zr.items():
        add("Cu45Zr45Ag10", "Zr", idx, frac/total)
    cu45_ag = {"<0 2 8 0>": 0.20, "<0 3 6 0>": 0.15, "<0 2 8 1>": 0.18, "<0 4 4 0>": 0.14, "others": 0.33}
    total = sum(cu45_ag.values())
    for idx, frac in cu45_ag.items():
        add("Cu45Zr45Ag10", "Ag", idx, frac/total)
    # Cu40Zr40Ag20
    cu40_cu = {"<0 3 6 0>": 0.14, "<0 2 8 0>": 0.07, "<0 2 8 1>": 0.10, "<0 4 4 0>": 0.11,
               "<0 3 6 1>": 0.09, "<0 1 10 2>": 0.08, "<0 2 8 2>": 0.08, "others": 0.33}
    total = sum(cu40_cu.values())
    for idx, frac in cu40_cu.items():
        add("Cu40Zr40Ag20", "Cu", idx, frac/total)
    cu40_zr = {"<0 3 6 0>": 0.04, "<0 2 8 0>": 0.03, "<0 2 8 1>": 0.04, "others": 0.89}
    total = sum(cu40_zr.values())
    for idx, frac in cu40_zr.items():
        add("Cu40Zr40Ag20", "Zr", idx, frac/total)
    cu40_ag = {"<0 2 8 0>": 0.22, "<0 3 6 0>": 0.14, "<0 2 8 1>": 0.16, "<0 4 4 0>": 0.15, "others": 0.33}
    total = sum(cu40_ag.values())
    for idx, frac in cu40_ag.items():
        add("Cu40Zr40Ag20", "Ag", idx, frac/total)

    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["composition", "center_type", "voronoi_index", "fraction"])
        for row in rows:
            writer.writerow(row)

def generate_ag_coord(output_path):
    data = {"Cu45Zr45Ag10": 1.4, "Cu40Zr40Ag20": 1.8}
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["exafs", "voronoi", "ag_coord"])
    parser.add_argument("outfile")
    args = parser.parse_args()
    if args.mode == "exafs":
        generate_exafs(args.outfile)
    elif args.mode == "voronoi":
        generate_voronoi(args.outfile)
    elif args.mode == "ag_coord":
        generate_ag_coord(args.outfile)
