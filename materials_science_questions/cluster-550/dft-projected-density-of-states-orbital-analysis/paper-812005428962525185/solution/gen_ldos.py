import sys, csv, math

def generate_ldos_rows(system, energies):
    """Return list of (system, energy, spin, dos) tuples."""
    # peak parameters: (center eV, width eV, amplitude states/eV)
    if system == 'MnAs_MnTerm':
        # stronger hybridization => two main majority peaks more separated
        maj_peaks = [(-2.8, 0.3, 15), (-0.2, 0.3, 12)]
    else:  # MnSb_MnTerm
        maj_peaks = [(-2.2, 0.3, 15), (-0.2, 0.3, 12)]

    # minority spin: broad feature above EF
    min_peaks = [(0.5, 1.0, 8)]

    rows = []
    for e in energies:
        # majority
        dos_maj = 0.5  # constant background
        for mu, sig, amp in maj_peaks:
            dos_maj += amp * math.exp(-0.5 * ((e - mu) / sig) ** 2)
        rows.append((system, round(e, 2), 'majority', round(dos_maj, 6)))

        # minority
        dos_min = 0.2
        for mu, sig, amp in min_peaks:
            dos_min += amp * math.exp(-0.5 * ((e - mu) / sig) ** 2)
        rows.append((system, round(e, 2), 'minority', round(dos_min, 6)))
    return rows

def main():
    out_path = sys.argv[1]
    # energy grid: -6.0 eV to +4.0 eV, step 0.01 eV
    energies = [i / 100.0 for i in range(-600, 401)]
    all_rows = []
    for sys_name in ['MnAs_MnTerm', 'MnSb_MnTerm']:
        all_rows.extend(generate_ldos_rows(sys_name, energies))
    with open(out_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['system', 'energy_eV', 'spin', 'dos_total'])
        writer.writerows(all_rows)

if __name__ == '__main__':
    main()