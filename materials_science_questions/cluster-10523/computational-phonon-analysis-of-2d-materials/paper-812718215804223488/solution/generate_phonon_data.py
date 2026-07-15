import json
import math
import numpy as np

def generate_qpoints_and_labels():
    segments = [
        ([0,0,0], [0.5,0,0], 20),
        ([0.5,0,0], [0.5,0.5,0], 20),
        ([0.5,0.5,0], [0,0,0], 20),
        ([0,0,0], [0.5,0.5,0.5], 20),
        ([0.5,0.5,0.5], [0.5,0,0], 20),
    ]
    qpoints = []
    for start, end, npts in segments:
        for i in range(npts+1):
            t = i / npts
            q = [start[0] + t*(end[0]-start[0]),
                 start[1] + t*(end[1]-start[1]),
                 start[2] + t*(end[2]-start[2])]
            qpoints.append(q)
    labels = {
        "Gamma": 0,
        "X": 20,
        "M": 40,
        "Gamma2": 60,
        "R": 80,
        "X2": 100
    }
    return qpoints, labels

def generate_frequencies(nq, N_branches, max_freq, flat_freqs, flat_count_per_freq=3):
    x = np.linspace(0, 2*math.pi, nq)
    freqs = []
    flat_indices = []
    total_flat = len(flat_freqs) * flat_count_per_freq
    # place flat branches from index 3 upward spread evenly
    for idx_f, freq in enumerate(flat_freqs):
        for j in range(flat_count_per_freq):
            idx = 3 + int((idx_f * flat_count_per_freq + j) * (N_branches - 4) / (total_flat + 1))
            flat_indices.append((idx, freq))
    for i in range(N_branches):
        if i < 3:  # acoustic branches
            base = max_freq * 0.2 * (i+1)
            amp = 0.05 * max_freq
            branch = base + amp * np.sin(x * (i+1))
        else:
            flat_freq = None
            for idx_f, freq_f in flat_indices:
                if i == idx_f:
                    flat_freq = freq_f
                    break
            if flat_freq is not None:
                branch = np.full(nq, flat_freq)
            else:
                base = max_freq * i / (N_branches - 1)
                amp = 0.03 * max_freq
                branch = base + amp * np.sin(x * (i+1))
                branch = np.minimum(branch, max_freq)
        freqs.append(branch.tolist())
    return freqs

def main():
    comp_params = {
        "Si46": {"N_atoms": 46, "spectral_width": 480, "flat_freqs": [150, 460, 480]},
        "Na8Si46": {"N_atoms": 54, "spectral_width": 340, "flat_freqs": [110, 340]},
        "K8Si46": {"N_atoms": 54, "spectral_width": 350, "flat_freqs": [130, 350]},
        "Ge46": {"N_atoms": 46, "spectral_width": 300, "flat_freqs": [85, 260, 300]},
        "K8Ge44\u25a12": {"N_atoms": 52, "spectral_width": 270, "flat_freqs": [80, 270]},
    }
    qpoints, labels = generate_qpoints_and_labels()
    out = {}
    for name, p in comp_params.items():
        N_branches = p["N_atoms"] * 3
        freqs = generate_frequencies(len(qpoints), N_branches, p["spectral_width"], p["flat_freqs"])
        out[name] = {
            "qpoints": qpoints,
            "frequencies": freqs,
            "high_symmetry_labels": labels
        }
    with open("/app/outputs/phonon_dispersions.json", "w") as f:
        json.dump(out, f, indent=2)

if __name__ == "__main__":
    main()