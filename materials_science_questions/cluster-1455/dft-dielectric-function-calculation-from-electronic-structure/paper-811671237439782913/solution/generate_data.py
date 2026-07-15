import csv, math, sys, os

def write_bulk_band_structure(output_dir):
    # High-symmetry k-points and interpolated points along segments
    # Lattice constants (Å)
    a = 3.189
    c = 5.185
    # Reciprocal lattice Cartesian (for convenience, we define points in fractional coords)
    # Γ (0,0,0), A (0,0,0.5), L (0.5,0,0.5), M (0.5,0,0)
    # Convert to Cartesian: bx, by, bz for wurtzite
    b1 = [2*math.pi/a, -2*math.pi/(a*math.sqrt(3)), 0.0]
    b2 = [2*math.pi/a,  2*math.pi/(a*math.sqrt(3)), 0.0]
    b3 = [0.0, 0.0, 2*math.pi/c]
    def to_cart(x,y,z):
        return (x*b1[0]+y*b2[0]+z*b3[0],
                x*b1[1]+y*b2[1]+z*b3[1],
                x*b1[2]+y*b2[2]+z*b3[2])
    # Define paths
    segments = [
        ("Γ", (0,0,0)),
        ("A", (0,0,0.5)),
        ("L", (0.5,0,0.5)),
        ("M", (0.5,0,0)),
        ("Γ", (0,0,0))
    ]
    # Generate points along each segment
    num_points = 10  # per segment
    points = []
    for i in range(len(segments)-1):
        label0, frac0 = segments[i]
        label1, frac1 = segments[i+1]
        for j in range(num_points):
            t = j / num_points
            fx = frac0[0] + t*(frac1[0]-frac0[0])
            fy = frac0[1] + t*(frac1[1]-frac1[1])
            fz = frac0[2] + t*(frac1[2]-frac0[2])
            kx, ky, kz = to_cart(fx,fy,fz)
            # label: use the current endpoint for that point? We'll use the starting label except for the final point of last segment which gets the end label.
            if j < num_points-1:
                lbl = label0
            else:
                lbl = label1
            points.append((lbl, kx, ky, kz))
    # Ensure Γ appears exactly once, we can set it at start; but last segment returns to Γ, so it will have Γ labels. That's fine.
    # Band structure: 8 bands (4 valence, 4 conduction)
    # Reference energies at Γ (0,0,0) cartesian: kx=0,ky=0,kz=0 -> use first point with label Γ.
    bands = 8
    ref_energies = [-8.0, -6.0, -4.0, 0.0, 3.6, 5.0, 7.0, 9.0]
    with open(os.path.join(output_dir, "bulk_band_structure.csv"), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["band_index","energy","k_label","k_x","k_y","k_z"])
        for lbl, kx, ky, kz in points:
            # simple dispersion: shift energies by quadratic in k distance from Γ
            # find distance from Γ (which is at (0,0,0) in cartesian for this lattice? Actually Γ is (0,0,0) consistently)
            # We'll compute distance
            dist = math.sqrt(kx*kx+ky*ky+kz*kz)  # in Å^{-1}
            shift = 0.5 * (dist)**2  # arbitrary dispersion to vary bands
            for b in range(bands):
                energy = ref_energies[b] + shift * (1 if b<4 else -1)  # valence shift up, conduction shift down?
                writer.writerow([b, energy, lbl, kx, ky, kz])

def write_bulk_reflectivity(output_dir):
    # Reflectivity spectra with static dielectric constant 5.4
    # Low-energy reflectivity R = ((sqrt(eps)-1)/(sqrt(eps)+1))**2
    eps_static = 5.4
    n_static = math.sqrt(eps_static)
    R_static = ((n_static - 1)/(n_static + 1))**2  # ~0.1587
    # Energy range 0 to 10 eV
    energies = [0.05 + i*0.05 for i in range(200)]  # 0.05 to 10.0
    # Gaussian peak function
    def gauss(x, center, width, height):
        return height * math.exp(-((x-center)/width)**2)
    with open(os.path.join(output_dir, "bulk_reflectivity.csv"), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["R_parallel","R_perp","energy"])
        for e in energies:
            base = R_static
            # Add peaks to mimic Fig 2: peaks around 4.5 eV, 7 eV
            peak1 = gauss(e, 4.5, 0.3, 0.08)
            peak2 = gauss(e, 7.0, 0.5, 0.05)
            # For anisotropy, slightly different heights
            R_parallel = base + peak1 + peak2
            R_perp = base + peak1*1.05 + peak2  # small difference
            writer.writerow([R_parallel, R_perp, e])

def write_surface_band_structure(output_dir):
    # Surface Brillouin zone: Γ (0,0), J (π/a,0), K (π/a,π/a) in y? Actually: x is direction Γ-J, y is J-K.
    # For simplicity, define k_x, k_y in units of Å^{-1}
    a_slab = 3.189  # approximate lattice constant
    k_jx = math.pi / a_slab  # ~0.985
    k_ky = math.pi / a_slab
    # Paths
    # Segment Γ->J: (0,0) to (k_jx, 0)
    # Segment J->K: (k_jx, 0) to (k_jx, k_ky)
    num_pt = 30
    path = []
    # Γ to J
    for i in range(num_pt):
        t = i / (num_pt-1)
        kx = t * k_jx
        ky = 0.0
        path.append((kx, ky))
    # J to K
    for i in range(num_pt):
        t = i / (num_pt-1)
        kx = k_jx
        ky = t * k_ky
        path.append((kx, ky))
    # Total bands: 40. Define surface bands:
    # Two empty in-gap bands: indices 0 and 1
    # Two occupied surface resonances: indices 2 and 3
    # The rest are bulk-projected bands (indices 4-39)
    def empty_surface1(kx, ky):
        # branch 1: almost flat, starts at 2.7 at Γ, stays 2.7 along Γ-J and J-K
        return 2.7
    def empty_surface2(kx, ky):
        # branch 2: at Γ it is 2.7, along Γ-J it rises to 3.7 at J, then flat along J-K
        # along Γ-J (ky=0): linear increase with kx
        if ky == 0.0:
            return 2.7 + (3.7-2.7)*(kx/k_jx)  # linear
        else:
            # along J-K, kx = k_jx, fixed at 3.7
            return 3.7
    with open(os.path.join(output_dir, "surface_band_structure.csv"), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["band_index","energy","k_x","k_y","state_type"])
        for (kx, ky) in path:
            for band_idx in range(40):
                if band_idx == 0:
                    energy = empty_surface1(kx, ky)
                    stype = "surface"
                elif band_idx == 1:
                    energy = empty_surface2(kx, ky)
                    stype = "surface"
                elif band_idx == 2:
                    energy = -1.3
                    stype = "surface"
                elif band_idx == 3:
                    energy = -2.0
                    stype = "surface"
                else:
                    # bulk projected bands: generate some values that span the range
                    # Use a simple function to give a band structure look
                    # VBM at 0, CBM ~3.6. We'll assign energies such that there are no states in the gap except surface.
                    # So bulk bands: energies < 0 (occupied) or > 3.6 (unoccupied), but with some width.
                    # We'll use a sinusoidal around mean
                    base = -5.0 if band_idx < 20 else 5.0  # bands below VBM or above CBM
                    width = 2.0
                    energy = base + width * (math.sin(kx*2 + ky*3 + band_idx) * 0.5)
                    # ensure VBM at 0 and CBM at 3.6 for some points
                    # but for simplicity just ensure gap region 0-3.6 only has surface states
                    # we'll clamp: if energy > 0 and energy < 3.6: move it to 0 or 3.6 depending on side
                    if 0 < energy < 3.6:
                        if band_idx < 20:
                            energy = 0.0
                        else:
                            energy = 3.6
                    stype = "bulk"
                writer.writerow([band_idx, energy, kx, ky, stype])

def write_surface_dos(output_dir):
    # Energy grid from -6 to 6 eV, step 0.05 eV
    energies = []
    e = -6.0
    while e <= 6.0:
        energies.append(e)
        e += 0.05
    # Gaussian function
    def gauss(x, center, sigma):
        return math.exp(-0.5*((x-center)/sigma)**2) / (sigma*math.sqrt(2*math.pi))
    # Layer peaks based on paper
    with open(os.path.join(output_dir, "surface_dos.csv"), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["energy","layer1","layer2","layer3","total"])
        for energy in energies:
            l1 = 0.0
            l2 = 0.0
            l3 = 0.0
            # Surface resonance peaks at -1.3 and -2.0 eV (layer1)
            l1 += gauss(energy, -1.3, 0.2)*0.3
            l1 += gauss(energy, -2.0, 0.2)*0.3
            # In-gap surface states at 2.7 eV (layer1, layer2)
            l1 += gauss(energy, 2.7, 0.15)*0.2
            l2 += gauss(energy, 2.7, 0.15)*0.2
            # Extended states 2.7-3.7 (surface dangling bonds) -> layer1
            for ee in [2.7, 3.0, 3.3, 3.6]:
                l1 += gauss(energy, ee, 0.2)*0.1
            # Bulk bands: smooth bands with peaks near -6 to -4 and 5-7
            for ee in range(-6, -3, 1):
                l3 += gauss(energy, ee+0.5, 0.5)*0.5
            for ee in range(5, 8):
                l3 += gauss(energy, ee, 0.5)*0.3
            # Also layer2 some bulk contribution
            l2 += gauss(energy, 2.7, 0.3)*0.05
            total = l1 + l2 + l3
            writer.writerow([energy, l1, l2, l3, total])

def write_surface_dielectric_function(output_dir):
    # Energy 0 to 10 eV, step 0.05 eV
    energies = []
    e = 0.0
    while e <= 10.0:
        energies.append(e)
        e += 0.05
    def gauss(x, center, sigma, height):
        return height * math.exp(-((x-center)/sigma)**2)
    with open(os.path.join(output_dir, "surface_dielectric_function.csv"), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["energy","eps2_x","eps2_y"])
        for energy in energies:
            if energy < 2.7:
                eps2_x = 0.0
                eps2_y = 0.0
            else:
                # Onset at 2.7, sharp peak at 4 eV for x, also peaks at 5.5 eV for both
                eps2_x = gauss(energy, 4.0, 0.12, 0.9) + gauss(energy, 5.5, 0.3, 0.4) + gauss(energy, 7.0, 0.5, 0.2)
                eps2_y = gauss(energy, 4.0, 0.12, 0.3) + gauss(energy, 5.5, 0.3, 0.4) + gauss(energy, 7.0, 0.5, 0.2)
            writer.writerow([energy, eps2_x, eps2_y])

def main():
    if len(sys.argv) != 3:
        print("Usage: python gen.py <output_dir> <filename>")
        sys.exit(1)
    output_dir = sys.argv[1]
    filename = sys.argv[2]
    os.makedirs(output_dir, exist_ok=True)
    if filename == "bulk_band_structure.csv":
        write_bulk_band_structure(output_dir)
    elif filename == "bulk_reflectivity.csv":
        write_bulk_reflectivity(output_dir)
    elif filename == "surface_band_structure.csv":
        write_surface_band_structure(output_dir)
    elif filename == "surface_dos.csv":
        write_surface_dos(output_dir)
    elif filename == "surface_dielectric_function.csv":
        write_surface_dielectric_function(output_dir)
    else:
        print(f"Unknown file: {filename}")
        sys.exit(1)

if __name__ == "__main__":
    main()
