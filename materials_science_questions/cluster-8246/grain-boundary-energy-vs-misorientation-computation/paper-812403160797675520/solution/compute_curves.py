import sys
import numpy as np

def main():
    out_path = sys.argv[1]

    N = 1000
    eps_cases = {
        'expansion': (0.1, 0.05),
        'contraction': (-0.1, -0.05),
    }

    # Half-cylinder plane indices: 0 .. N-2 inclusive (N-1 planes)
    l = np.arange(0, N - 1, dtype=np.float64)
    # Left geometry factor (plan view weight)
    w_left = np.sqrt(1.0 - (1.0 - l / (N - 2))**2)
    # Right geometry factor
    w_right = np.sqrt(1.0 - (l / (N - 2))**2)

    # Fine f grid for accurate averaging
    f_step = 0.0001
    f_start = 0.898          # ensure 0.9, 0.901,... are included
    f_stop = 1.102 + f_step   # inclusive stop
    f_fine = np.arange(f_start, f_stop, f_step)

    # Smoothing kernel width ~0.01 (101 points)
    kernel_len = 101
    kernel = np.ones(kernel_len) / kernel_len

    def compute_I_bar(eps1, eps2):
        # Y = left sum + two boundary planes + right sum
        # Phase contributions
        phase_left = l[np.newaxis, :] * f_fine[:, np.newaxis]          # shape (nf, N-1)
        term_left = np.sum(w_left * np.exp(1j * 2 * np.pi * phase_left), axis=1)

        boundary = (np.exp(1j * 2 * np.pi * f_fine * (N - 1 + eps2))
                    + np.exp(1j * 2 * np.pi * f_fine * (N + eps2 + eps1)))

        shift = N + 1 + 2 * eps2 + eps1
        phase_right = (l[np.newaxis, :] + shift) * f_fine[:, np.newaxis]
        term_right = np.sum(w_right * np.exp(1j * 2 * np.pi * phase_right), axis=1)

        Y = term_left + boundary + term_right
        I_raw = np.abs(Y)**2
        # Local averaging
        I_smooth = np.convolve(I_raw, kernel, mode='same')
        return I_smooth

    # Target f values: 0.9 to 1.1 inclusive, step 0.001
    target_f = np.arange(0.9, 1.100000001, 0.001)
    # Find indices in fine grid
    indices = [np.argmin(np.abs(f_fine - fv)) for fv in target_f]

    # Compute both cases
    results = {}
    for case_name, (e1, e2) in eps_cases.items():
        I_sm = compute_I_bar(e1, e2)
        results[case_name] = I_sm[indices]

    # Write CSV
    with open(out_path, 'w') as f:
        f.write('f,I_bar_expansion,I_bar_contraction\n')
        for i, fv in enumerate(target_f):
            f.write(f'{fv:.3f},{results["expansion"][i]:.10e},{results["contraction"][i]:.10e}\n')

if __name__ == '__main__':
    main()
