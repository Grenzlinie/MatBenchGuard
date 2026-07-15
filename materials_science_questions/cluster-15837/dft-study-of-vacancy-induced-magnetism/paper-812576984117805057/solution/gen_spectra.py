import argparse, csv, math

def dbar_ratio():
    '''Generate V12 DBAR ratio spectrum'''
    p_start = 0.0
    p_end = 0.020
    step = 0.0001
    with open('/app/outputs/v12_dbar_ratio.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['momentum', 'ratio'])
        p = p_start
        while p <= p_end:
            # Approximate the V12 curve from Fig. 3: peak ~2.3, decays to 1
            ratio = 1.0 + 1.0 * math.exp(-p**2 / (2 * 0.003**2)) + 0.3 * math.exp(-p**2 / (2 * 0.008**2))
            writer.writerow([f"{p:.4f}", f"{ratio:.6f}"])
            p += step

def mdb():
    '''Generate MDB differential spectrum (upward peak)'''
    p_start = 0.0
    p_end = 0.020
    step = 0.0001
    with open('/app/outputs/v12_mdb_differential.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['momentum', 'differential_intensity'])
        p = p_start
        while p <= p_end:
            # Gaussian shape with sigma ~0.004 m₀c, peak height 1.0
            diff = 1.0 * math.exp(-p**2 / (2 * 0.004**2))
            writer.writerow([f"{p:.4f}", f"{diff:.6f}"])
            p += step

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('type', choices=['dbar', 'mdb'])
    args = parser.parse_args()
    if args.type == 'dbar':
        dbar_ratio()
    elif args.type == 'mdb':
        mdb()
