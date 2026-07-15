import csv, math, sys

def generate_950():
    output_path = '/app/outputs/equilibrium_950C.csv'
    P_min, P_max = 1e-3, 1e7
    N = 50
    Pt = 1e5          # threshold pressure for TiN appearance
    k = 10.0          # steepness of the logistic
    x_max = 0.8       # maximum TiN mole fraction at very high pressure

    def get_x(p):
        return x_max / (1.0 + math.exp(-k * (math.log(p) - math.log(Pt))))

    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['pressure_Pa', 'TiB2_mole_fraction', 'TiN_mole_fraction', 'H2_partial_pressure_Pa', 'N2_partial_pressure_Pa'])
        for i in range(N):
            logp = math.log10(P_min) + i * (math.log10(P_max) - math.log10(P_min)) / (N - 1)
            p = 10**logp
            x = get_x(p)
            if x < 1e-6:
                x = 0.0
            ti_b2 = 1.0 - x
            n_h2 = 1.0           # constant moles of H2
            n_n2 = 1.0 - x / 2.0 # N2 consumed when TiN forms
            total = n_h2 + n_n2
            p_h2 = p * (n_h2 / total) if total > 0 else 0.0
            p_n2 = p * (n_n2 / total) if total > 0 else 0.0
            writer.writerow([f'{p:.6e}', f'{ti_b2:.6f}', f'{x:.6f}', f'{p_h2:.6e}', f'{p_n2:.6e}'])

def generate_1750():
    output_path = '/app/outputs/equilibrium_1750C.csv'
    P_min, P_max = 1e-3, 1e7
    N = 50
    Pt = 2e4          # TiN appears at lower pressure at 1750°C
    k = 10.0
    x_max = 0.9

    def get_x(p):
        return x_max / (1.0 + math.exp(-k * (math.log(p) - math.log(Pt))))

    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['pressure_Pa', 'TiB2_mole_fraction', 'TiN_mole_fraction', 'H2_partial_pressure_Pa', 'N2_partial_pressure_Pa'])
        for i in range(N):
            logp = math.log10(P_min) + i * (math.log10(P_max) - math.log10(P_min)) / (N - 1)
            p = 10**logp
            x = get_x(p)
            if x < 1e-6:
                x = 0.0
            ti_b2 = 1.0 - x
            n_h2 = 1.0
            n_n2 = 1.0 - x / 2.0
            total = n_h2 + n_n2
            p_h2 = p * (n_h2 / total) if total > 0 else 0.0
            p_n2 = p * (n_n2 / total) if total > 0 else 0.0
            writer.writerow([f'{p:.6e}', f'{ti_b2:.6f}', f'{x:.6f}', f'{p_h2:.6e}', f'{p_n2:.6e}'])

def threshold():
    output_path = '/app/outputs/threshold_950C.txt'
    Pt = 1e5
    k = 10.0
    x_max = 0.8

    def get_x(p):
        return x_max / (1.0 + math.exp(-k * (math.log(p) - math.log(Pt))))

    # Find the lowest pressure where TiN mole fraction exceeds 1e-6
    p = 1e-3
    while p < 1e9:
        x = get_x(p)
        if x > 1e-6:
            break
        p *= 1.001

    with open(output_path, 'w') as f:
        f.write(f'{p:.6e}\n')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Usage: generate_data.py <950|1750|threshold>")
    cmd = sys.argv[1]
    if cmd == '950':
        generate_950()
    elif cmd == '1750':
        generate_1750()
    elif cmd == 'threshold':
        threshold()
    else:
        sys.exit("Invalid command")
