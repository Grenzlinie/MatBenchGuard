import sys, math

def write_tdos():
    # energy -10 to 10 eV, step 0.05 eV
    for i in range(400):
        e = -10.0 + i * 0.05
        # valence band: broad peak at -1 eV
        vb = 10.0 * math.exp(-((e + 1.0) ** 2) / (2.0 * 2.0 ** 2))
        # defect state: sharp peak at +3.0 eV
        defect = 0.5 * math.exp(-((e - 3.0) ** 2) / (2.0 * 0.5 ** 2))
        dos = vb + defect
        print(f"{e:.3f} {dos:.6f}")

def write_absorption():
    # energy 0 to 10 eV, step 0.05 eV
    for i in range(200):
        e = i * 0.05
        # dominant absorption peak at 5.3 eV
        a = math.exp(-((e - 5.3) ** 2) / (2.0 * 0.5 ** 2))
        print(f"{e:.3f} {a:.6f}")

if __name__ == "__main__":
    if sys.argv[1] == "tdos":
        write_tdos()
    elif sys.argv[1] == "absorption":
        write_absorption()
    else:
        sys.exit(1)