import sys
import math

def gen_band_structure():
    nk = 100
    nv = 10  # valence bands
    nc = 10  # conduction bands
    L = 0.5  # maximum k-distance (arbitrary)
    for ik in range(nk):
        x = ik * L / (nk - 1)
        # Valence bands: highest at ik=0 gives -0.5 eV (the VBM)
        for iv in range(nv):
            # iv=0 is deepest, iv=nv-1 is VBM
            e = -0.5 - (nv - 1 - iv) * 0.4 - 0.1 * math.sin(math.pi * x / L)
            print(f"{x:.6f} {e:.6f}")
        # Conduction bands: lowest at ik=0 gives 3.394 eV (the CBM)
        for ic in range(nc):
            # ic=0 is CBM
            e = 3.394 + ic * 0.4 + 0.1 * (1 - math.cos(math.pi * x / L))
            print(f"{x:.6f} {e:.6f}")

def gen_dos():
    # Energy grid from -10 to 10 eV, step 0.05 eV
    for e200 in range(-200, 201):
        e = e200 * 0.05
        dos = 0.0
        if e < -0.5:
            # Valence region with two Gaussian-like peaks
            dos = math.exp(-((e + 3) ** 2) / 2) + 0.8 * math.exp(-((e + 1) ** 2) / 0.5)
        elif e > 3.394:
            # Conduction region with two Gaussian-like peaks
            dos = math.exp(-((e - 4.5) ** 2) / 2) + 0.5 * math.exp(-((e - 6) ** 2) / 1.0)
        # Within [-0.5, 3.394] dos remains 0 -> the band gap
        print(f"{e:.4f} {dos:.6f}")

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "band_structure":
        gen_band_structure()
    elif cmd == "dos":
        gen_dos()
    elif cmd == "band_gap":
        print("3.894")
    else:
        raise ValueError(f"Unknown command: {cmd}")
