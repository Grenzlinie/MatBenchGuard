import sys, csv, json, math

def f_dis(phi, chiN):
    return 0.005 * chiN + 2.0 * (phi - 0.5) ** 2

def melting_chiN_HexII(phi):
    if phi <= 0.45:
        val = 20.0 - 40.0 * (phi - 0.3) ** 2
        return max(val, 12.0)
    return 12.0

def melting_chiN_Lam(phi):
    if 0.35 <= phi <= 0.65:
        val = 14.5 - 100.0 * (phi - 0.5) ** 2
        return max(val, 12.0)
    return 12.0

def melting_chiN_Hex(phi):
    if phi >= 0.55:
        val = 20.0 - 40.0 * (phi - 0.67) ** 2
        return max(val, 12.0)
    return 12.0

def grand_potentials(phi, chiN):
    base = f_dis(phi, chiN)
    d = 0.05
    # offset = d * (melting_chiN - 10)
    off_HexII = d * (melting_chiN_HexII(phi) - 10.0)
    off_Lam   = d * (melting_chiN_Lam(phi)   - 10.0)
    off_Hex   = d * (melting_chiN_Hex(phi)   - 10.0)
    # f_phase = base + offset - d*(chiN - 10)
    fac = d * (chiN - 10.0)
    return {
        'Dis': base,
        'Lam': base + off_Lam   - fac,
        'Hex': base + off_Hex   - fac,
        'Hex_II': base + off_HexII - fac
    }

def stable_phase(phi, chiN):
    pots = grand_potentials(phi, chiN)
    # order: prefer ordered over Dis on tie
    order = ['Hex_II', 'Hex', 'Lam']
    min_val = pots['Dis']
    best = 'Dis'
    for ph in order:
        if pots[ph] < min_val:
            min_val = pots[ph]
            best = ph
    return best

# grid
phi_vals = [round(x, 2) for x in [0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85]]
chiN_vals = [12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]

if len(sys.argv) < 2:
    sys.exit(1)
mode = sys.argv[1]

if mode == 'stable_csv':
    writer = csv.writer(sys.stdout)
    writer.writerow(['phi_A_tot', 'chiN', 'phase'])
    for phi in phi_vals:
        for chiN in chiN_vals:
            phase = stable_phase(phi, chiN)
            writer.writerow([phi, chiN, phase])
elif mode == 'grand_json':
    obj = {}
    for phi in phi_vals:
        for chiN in chiN_vals:
            key = f"({phi:.2f},{chiN:.1f})"
            pots = grand_potentials(phi, chiN)
            obj[key] = pots
    json.dump(obj, sys.stdout, indent=2)
else:
    sys.exit(1)
