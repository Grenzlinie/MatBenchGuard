import sys
import numpy as np

# Constants
PI = np.pi

# Force constants (in 10^3 dyn/cm) and lattice/a (Angstrom), mass (u)
METALS = {
    'copper': {
        'A1': 35.228, 'A2': 1.875,
        'a2K1': -0.040, 'a2K2': -0.988,
        'aKe': 0.1113,
        'a': 3.616,       # Angstrom
        'M': 63.55        # atomic mass units
    },
    'silver': {
        'A1': 30.030, 'A2': 0.675,
        'a2K1': 0.280, 'a2K2': -1.402,
        'aKe': 1.346,
        'a': 4.08,
        'M': 107.87
    }
}

AMU_TO_G = 1.660539e-24   # g per u
ANG_TO_CM = 1e-8           # cm per Angstrom

def G_bross_bohn(u, v, w):
    """Bross-Bohn G(q) for fcc (Eq. 4)."""
    # Gamma point: electron-ion term vanishes due to q_i factors
    if abs(u) + abs(v) + abs(w) < 1e-12:
        return 0.0
    denom = u*u + v*v + w*w
    if denom < 1e-30:
        return 0.0
    # Cyclic permutations: (a,b,c) = (u,v,w), (v,w,u), (w,u,v)
    triples = [(u,v,w), (v,w,u), (w,u,v)]
    total = 0.0
    for a, b, c in triples:
        # First term with (a+b)/((a-b)^2 - c^2)
        d1 = (a-b)**2 - c**2
        if abs(d1) > 1e-30:
            t1 = (a+b)/d1 * (np.sin(a) + np.sin(b) - np.sin((a+b+c)/2) - np.sin((a+b-c)/2))
        else:
            t1 = 0.0
        # Second term with (a-b)/((a+b)^2 - c^2)
        d2 = (a+b)**2 - c**2
        if abs(d2) > 1e-30:
            t2 = (a-b)/d2 * (np.sin(a) - np.sin(b) - np.sin((a+b+c)/2) - np.sin((a-b-c)/2))
        else:
            t2 = 0.0
        total += t1 + t2
    return -2.0 / denom * total

def dynamical_matrix(params, a_cm, M_g, qx, qy, qz):
    # Unpack force constants in CGS (dyn/cm)
    A1 = params['A1'] * 1e3
    A2 = params['A2'] * 1e3
    K1_tilde = params['a2K1'] * 1e3   # a^{-2}K1
    K2_tilde = params['a2K2'] * 1e3   # a^{-2}K2
    aKe = params['aKe'] * 1e3
    
    # Phase angles
    phi1 = PI * qx
    phi2 = PI * qy
    phi3 = PI * qz
    C1 = np.cos(phi1); S1 = np.sin(phi1)
    C2 = np.cos(phi2); S2 = np.sin(phi2)
    C3 = np.cos(phi3); S3 = np.sin(phi3)
    
    # Bross-Bohn G
    Gq = G_bross_bohn(phi1, phi2, phi3)
    
    # Common factors
    cent1 = 2*A1 + 8*(K1_tilde + K2_tilde)
    
    # D11
    D11 = cent1 * (2 - C1*(C2 + C3)) + 4*A2*S1*S1 - 8*K1_tilde*(2*C1*C1 - C2*C2 - C3*C3) + PI*PI * aKe * qx*qx * Gq*Gq
    # D22 (cyclic: 1->2,2->3,3->1)
    D22 = cent1 * (2 - C2*(C3 + C1)) + 4*A2*S2*S2 - 8*K1_tilde*(2*C2*C2 - C3*C3 - C1*C1) + PI*PI * aKe * qy*qy * Gq*Gq
    # D33
    D33 = cent1 * (2 - C3*(C1 + C2)) + 4*A2*S3*S3 - 8*K1_tilde*(2*C3*C3 - C1*C1 - C2*C2) + PI*PI * aKe * qz*qz * Gq*Gq
    
    # Off-diagonal
    off_cent = 2*A1 - 16*K1_tilde
    D12 = off_cent * S1*S2 + PI*PI * aKe * qx*qy * Gq*Gq
    D23 = off_cent * S2*S3 + PI*PI * aKe * qy*qz * Gq*Gq
    D31 = off_cent * S3*S1 + PI*PI * aKe * qz*qx * Gq*Gq
    
    # Construct symmetric matrix
    D = np.array([[D11, D12, D31],
                  [D12, D22, D23],
                  [D31, D23, D33]])
    return D

def compute_frequencies(params, a_cm, M_g, qpoints):
    nu_all = []
    for qx, qy, qz in qpoints:
        D = dynamical_matrix(params, a_cm, M_g, qx, qy, qz)
        eigvals = np.linalg.eigvalsh(D)  # symmetric
        # angular frequency omega = sqrt(eigval), careful: eigenvalues should be positive
        # occasionally numerical noise may give small negative, clip to zero
        omega = np.sqrt(np.maximum(eigvals, 0))
        # frequency in Hz: nu = omega/(2*pi)
        nu_Hz = omega / (2*PI)
        # convert to 10^12 Hz
        nu_THz = nu_Hz * 1e-12
        # sort ascending
        nu_sorted = np.sort(nu_THz)
        nu_all.append((qx, qy, qz, nu_sorted[0], nu_sorted[1], nu_sorted[2]))
    return nu_all

def main():
    metal = sys.argv[1]
    outfile = sys.argv[2]
    params = METALS[metal]
    a_cm = params['a'] * ANG_TO_CM
    M_g = params['M'] * AMU_TO_G
    
    # Generate q vectors: qx from 0.0 to 1.0 in steps of 0.1
    qx_vals = np.arange(0.0, 1.01, 0.1)
    directions = {
        '100': lambda q: (q, 0.0, 0.0),
        '110': lambda q: (q, q, 0.0),
        '111': lambda q: (q, q, q)
    }
    qpoints = []
    for dir_name, func in directions.items():
        for q in qx_vals:
            qpoints.append(func(round(q, 10)))  # avoid float artifact
    
    results = compute_frequencies(params, a_cm, M_g, qpoints)
    
    with open(outfile, 'w') as f:
        f.write('qx\tqy\tqz\tfreq1\tfreq2\tfreq3\n')
        for qx, qy, qz, f1, f2, f3 in results:
            f.write(f'{qx:.6g}\t{qy:.6g}\t{qz:.6g}\t{f1:.6f}\t{f2:.6f}\t{f3:.6f}\n')

if __name__ == '__main__':
    main()
