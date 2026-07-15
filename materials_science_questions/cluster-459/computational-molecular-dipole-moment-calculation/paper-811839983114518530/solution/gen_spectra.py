import sys

def clusters_data():
    return [
        # motif, label, freq_eV, fwhm_eV, N_atoms
        ("Ih", "Ag147", 3.97, 1.53, 147),
        ("Ih", "Ag309", 3.90, 1.40, 309),
        ("Ih", "Ag561", 3.85, 1.26, 561),
        ("Ih", "Ag923", 3.81, 1.36, 923),
        ("Ih", "Ag1415", 3.79, 1.51, 1415),
        ("Ih", "Ag2057", 3.78, 1.48, 2057),
        ("Ih", "Ag2869", 3.77, 1.46, 2869),
        ("Ih", "Ag3871", 3.77, 1.44, 3871),
        ("i-Dh", "Ag85", 3.95, 1.52, 85),
        ("i-Dh", "Ag207", 3.87, 1.42, 207),
        ("i-Dh", "Ag409", 3.80, 1.33, 409),
        ("i-Dh", "Ag711", 3.74, 1.37, 711),
        ("i-Dh", "Ag1133", 3.69, 1.42, 1133),
        ("i-Dh", "Ag1695", 3.65, 1.38, 1695),
        ("i-Dh", "Ag2417", 3.62, 1.34, 2417),
        ("i-Dh", "Ag3319", 3.60, 1.31, 3319),
        ("m-Dh", "Ag75", 3.98, 1.54, 75),
        ("m-Dh", "Ag192", 3.90, 1.44, 192),
        ("m-Dh", "Ag389", 3.83, 1.35, 389),
        ("m-Dh", "Ag686", 3.77, 1.39, 686),
        ("m-Dh", "Ag1103", 3.72, 1.44, 1103),
        ("m-Dh", "Ag1660", 3.68, 1.40, 1660),
        ("m-Dh", "Ag2377", 3.65, 1.36, 2377),
        ("m-Dh", "Ag3274", 3.63, 1.33, 3274),
        ("TO", "Ag201", 3.55, 1.60, 201),
        ("TO", "Ag586", 3.63, 1.45, 586),
        ("TO", "Ag1289", 3.71, 1.40, 1289),
        ("TO", "Ag2406", 3.76, 1.48, 2406),
        ("TO", "Ag4033", 3.79, 1.52, 4033),
        ("c-TO", "Ag147", 4.15, 1.70, 147),
        ("c-TO", "Ag309", 4.05, 1.50, 309),
        ("c-TO", "Ag561", 3.95, 1.40, 561),
        ("c-TO", "Ag923", 3.86, 1.45, 923),
        ("c-TO", "Ag1415", 3.79, 1.55, 1415),
        ("c-TO", "Ag2057", 3.74, 1.60, 2057),
        ("c-TO", "Ag2869", 3.72, 1.62, 2869),
        ("c-TO", "Ag3871", 3.71, 1.62, 3871),
    ]

def generate_spectra():
    print("motif,cluster_label,energy_eV,sigma_per_atom")
    for motif, label, freq, fwhm, N in clusters_data():
        hwhm = 0.5 * fwhm
        for energy_eV in [round(2.4 + i*0.05, 2) for i in range(49)]:  # 2.4 to 4.8 inclusive
            sigma = (hwhm**2) / ((energy_eV - freq)**2 + hwhm**2)
            print(f"{motif},{label},{energy_eV:.2f},{sigma:.6f}")

def generate_summary():
    print("FWHM_eV,cluster_label,motif,plasmon_freq_eV")
    for motif, label, freq, fwhm, _ in clusters_data():
        print(f"{fwhm:.2f},{label},{motif},{freq:.2f}")

if __name__ == "__main__":
    if sys.argv[1] == "spectra":
        generate_spectra()
    elif sys.argv[1] == "summary":
        generate_summary()
    else:
        raise SystemExit("usage: gen_spectra.py spectra|summary")
