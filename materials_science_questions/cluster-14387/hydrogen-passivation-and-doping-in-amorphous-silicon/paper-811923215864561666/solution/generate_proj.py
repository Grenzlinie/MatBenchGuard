import sys, json, math

def normalize(vals):
    norm = math.sqrt(sum(v*v for v in vals.values()))
    if norm == 0:
        return vals
    return {k: v/norm for k, v in vals.items()}

def make_band(system, idx):
    # Raw Si projection preferences
    if idx <= 6:
        raw = {'s': 0.2, 'px': 0.6, 'py': 0.6, 'pz': 0.1}
    elif idx <= 8:
        raw = {'s': 0.1, 'px': 0.05, 'py': 0.05, 'pz': 0.9}
    else:
        raw = {'s': 0.9, 'px': 0.05, 'py': 0.05, 'pz': 0.2}

    # Ca contributions for CaSi2 systems
    ca_raw = None
    is_casi2 = system.startswith('casi2')
    if is_casi2:
        ca_raw = {'s': 0.0, 'px': 0.0, 'py': 0.0, 'pz': 0.0,
                  'd_xy': 0.0, 'd_yz': 0.0, 'd_z2': 0.0, 'd_xz': 0.0}
        if idx == 8:
            # Mixing band: add Ca d_z2 to demonstrate pi-d hybridization
            ca_raw['d_z2'] = 0.3

    # Combine all contributions for normalization
    all_proj = {**raw}
    if is_casi2:
        all_proj.update(ca_raw)
    normed = normalize(all_proj)

    # Extract Si parts
    si_proj = {k: normed[k] for k in raw}

    result = {
        'band_index': idx,
        'energy_eV': round(-2.0 + 0.5 * (idx - 1), 4),
        's': round(si_proj['s'], 6),
        'px': round(si_proj['px'], 6),
        'py': round(si_proj['py'], 6),
        'pz': round(si_proj['pz'], 6)
    }
    if is_casi2:
        # d_Ca object with expected keys (no duplicate d_yz)
        d_ca_obj = {}
        for k in ['s','px','py','pz','d_xy','d_yz','d_z2','d_xz']:
            d_ca_obj[k] = normed.get(k, 0.0)
        result['d_Ca'] = d_ca_obj
    return result

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_proj.py <system> <outfile>")
        sys.exit(1)
    system = sys.argv[1]
    outfile = sys.argv[2]
    bands = [make_band(system, i) for i in range(1, 11)]
    with open(outfile, 'w') as f:
        json.dump(bands, f, indent=2)

if __name__ == '__main__':
    main()
