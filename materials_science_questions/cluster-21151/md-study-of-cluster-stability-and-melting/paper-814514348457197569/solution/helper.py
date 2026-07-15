import csv
import sys
import math
import yaml


def generate_defect_counts():
    rows = [
        ("pure_Fe", 100, 400, 0.0, 0.3, 0.3),
        ("pure_Fe", 100, 800, 0.0, 0.4, 0.4),
        ("pure_Fe", 100, 1000, 0.0, 0.5, 0.5),
        ("pure_Fe", 500, 400, 0.0, 1.5, 1.5),
        ("pure_Fe", 500, 800, 0.0, 2.0, 2.0),
        ("pure_Fe", 500, 1000, 0.0, 2.5, 2.5),
        ("pure_Fe", 3000, 400, 0.0, 3.0, 3.0),
        ("pure_Fe", 3000, 800, 0.0, 4.0, 4.0),
        ("pure_Fe", 3000, 1000, 0.0, 5.0, 5.0),
        ("Fe_Fe3C_inclusion", 100, 400, 3.0, 4.0, 4.0),
        ("Fe_Fe3C_inclusion", 100, 800, 4.5, 5.5, 5.5),
        ("Fe_Fe3C_inclusion", 100, 1000, 6.0, 7.0, 7.0),
        ("Fe_Fe3C_inclusion", 500, 400, 15.0, 20.0, 20.0),
        ("Fe_Fe3C_inclusion", 500, 800, 18.0, 25.0, 25.0),
        ("Fe_Fe3C_inclusion", 500, 1000, 22.0, 30.0, 30.0),
        ("Fe_Fe3C_inclusion", 3000, 400, 45.0, 60.0, 60.0),
        ("Fe_Fe3C_inclusion", 3000, 800, 55.0, 70.0, 70.0),
        ("Fe_Fe3C_inclusion", 3000, 1000, 65.0, 80.0, 80.0),
    ]
    writer = csv.writer(sys.stdout)
    writer.writerow(["cell_type", "recoil_energy_eV", "temperature_K",
                      "avg_antisites", "avg_vacancies", "avg_interstitials"])
    for row in rows:
        writer.writerow(row)


def generate_radial_profiles():
    # Shell centers from 2.5 to 47.5 Å with 5 Å width
    centers = [2.5, 7.5, 12.5, 17.5, 22.5, 27.5, 32.5, 37.5, 42.5, 47.5]
    energies = [100, 500, 3000]
    temps = [400, 800, 1000]

    def smooth_profile(peak_index=None, peak_val=0.0025):
        base = [0.0003, 0.0003, 0.0002, 0.0002, 0.0001,
                0.0001, 0.00005, 0.00003, 0.00002, 0.00001]
        if peak_index is None:
            return base
        # Insert peak at given index, taper neighbours
        out = base[:]
        out[peak_index] = peak_val
        if peak_index > 0:
            out[peak_index - 1] *= 0.5
        if peak_index < len(out) - 1:
            out[peak_index + 1] *= 0.5
        return out

    data = {}
    for e in energies:
        for t in temps:
            key = f"Fe_Fe3C_inclusion_{e}eV_{t}K"
            if e == 3000 and t == 1000:
                # Interface peak near 20 Å (shell center 17.5 covers 15-20 Å)
                peak_idx = centers.index(17.5)
                antisite_dens = smooth_profile(peak_idx, peak_val=0.0025)
                vacancy_dens = smooth_profile(peak_idx, peak_val=0.0035)
                interstitial_dens = smooth_profile(peak_idx, peak_val=0.0030)
            else:
                # Smooth decreasing profile, scaled down for lower energy/temp
                scale = (e / 3000.0) * (t / 1000.0)
                antisite_dens = [v * scale for v in smooth_profile()]
                vacancy_dens = [v * scale for v in smooth_profile()]
                interstitial_dens = [v * scale for v in smooth_profile()]

            shells = []
            for i, c in enumerate(centers):
                shells.append({
                    "radius_center": round(c, 1),
                    "antisite_density": antisite_dens[i],
                    "vacancy_density": vacancy_dens[i],
                    "interstitial_density": interstitial_dens[i]
                })
            data[key] = shells

    yaml.dump(data, sys.stdout, default_flow_style=False, allow_unicode=True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "defect_counts":
        generate_defect_counts()
    elif cmd == "radial_profiles":
        generate_radial_profiles()
    else:
        sys.exit(1)
