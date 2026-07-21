import numpy as np
import json
import math

def generate_distribution(alpha, cutoff, total_spins=1024, max_c=200):
    c = np.arange(1, max_c+1, dtype=float)
    rf = c**(-alpha) * np.exp(-c/cutoff)
    rf /= rf.sum()
    # find scale such that sum(c*count) ~ total_spins
    def total_from_scale(s):
        counts = np.maximum(np.round(s * rf).astype(int), 0)
        return np.dot(c, counts)
    scale = total_spins / np.dot(c, rf) * 1.5  # initial guess
    for _ in range(200):
        cur_total = total_from_scale(scale)
        if abs(cur_total - total_spins) <= 1:
            break
        if cur_total < total_spins:
            scale *= 1.01
        else:
            scale *= 0.99
    counts = np.maximum(np.round(scale * rf).astype(int), 0)
    total = np.dot(c, counts)
    # fine adjust: add/remove from largest cluster size
    while total < total_spins:
        counts[-1] += 1
        total += c[-1]
    while total > total_spins and counts[-1] > 0:
        counts[-1] -= 1
        total -= c[-1]
    dist = []
    for i in range(len(c)):
        if counts[i] > 0:
            dist.append({"cluster_order": int(c[i]), "count": int(counts[i])})
    return dist

def main():
    demag_types = [
        ("AC", 2.5, 5),
        ("thermal", 1.8, 15),
        ("DC", 2.3, 6),
        ("natural", 1.5, 20)
    ]
    interaction_strengths = [
        (1.0, 2.0, 8),
        (1.1, 1.9, 10),
        (1.2, 1.7, 13),
        (1.3, 1.5, 18),
        (1.4, 1.3, 24)
    ]
    frequencies = [
        (0.07, 2.5, 5),
        (0.14, 2.8, 4),
        (0.21, 3.0, 3)
    ]
    virgin_curve_fields = [
        (0.0, 2.5, 5),
        (0.2, 2.3, 6),
        (0.4, 2.0, 8),
        (0.6, 1.8, 12),
        (0.8, 1.5, 18),
        (1.0, 1.2, 25)
    ]
    output = {}
    # demag_types
    output["demag_types"] = [{"demag_type": dt, "distribution": generate_distribution(a, c)} for dt, a, c in demag_types]
    # interaction_strengths
    output["interaction_strengths"] = [{"d": d, "distribution": generate_distribution(a, c)} for d, a, c in interaction_strengths]
    # frequencies
    output["frequencies"] = [{"frequency": f, "distribution": generate_distribution(a, c)} for f, a, c in frequencies]
    # virgin_curve_fields
    output["virgin_curve_fields"] = [{"applied_field_h": h, "distribution": generate_distribution(a, c)} for h, a, c in virgin_curve_fields]
    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
