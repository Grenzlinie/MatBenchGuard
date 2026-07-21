import json

def write_island_stats(path):
    N = 25600
    total_cov = 0.2

    cases = [
        {"temp": 100.0, "dtype": "conventional",
         "others": [(2,0.01),(3,0.006),(4,0.004),(5,0.003),(6,0.002),(7,0.0015),(8,0.001),(9,0.0005),(10,0.0005)]},
        {"temp": 100.0, "dtype": "energetic",
         "others": [(2,0.012),(3,0.008),(4,0.005),(5,0.004),(6,0.003),(7,0.002),(8,0.0015),(9,0.001),(10,0.001),(11,0.0005)]},
        {"temp": 300.0, "dtype": "conventional",
         "others": [(2,0.028),(3,0.022),(4,0.018),(5,0.015),(6,0.012),(7,0.01),(8,0.008),(9,0.006),(10,0.005),(11,0.004),(12,0.003),(13,0.002)]},
        {"temp": 300.0, "dtype": "energetic",
         "others": [(2,0.029),(3,0.023),(4,0.018),(5,0.015),(6,0.012),(7,0.01),(8,0.008),(9,0.007),(10,0.006),(11,0.005),(12,0.004),(13,0.003)]},
        {"temp": 400.0, "dtype": "conventional",
         "others": [(2,0.035),(3,0.03),(4,0.025),(5,0.02),(6,0.015),(7,0.01),(8,0.008),(9,0.007),(10,0.005),(11,0.005),(12,0.005),(13,0.005)]},
        {"temp": 400.0, "dtype": "energetic",
         "others": [(2,0.036),(3,0.031),(4,0.026),(5,0.021),(6,0.016),(7,0.011),(8,0.009),(9,0.008),(10,0.006),(11,0.005),(12,0.003)]},
        {"temp": 450.0, "dtype": "conventional",
         "others": [(2,0.04),(3,0.035),(4,0.03),(5,0.025),(6,0.02),(7,0.015),(8,0.01),(9,0.008),(10,0.006),(11,0.001)]},
        {"temp": 450.0, "dtype": "energetic",
         "others": [(2,0.04),(3,0.035),(4,0.03),(5,0.025),(6,0.02),(7,0.015),(8,0.01),(9,0.008),(10,0.006),(11,0.001)]},
    ]

    res = []
    for case in cases:
        others = case["others"]
        sum_others = sum(cov for _, cov in others)
        cov1 = total_cov - sum_others
        full_dist = [(1, cov1)] + others
        dist_list = [{"size": s, "coverage": cov} for s, cov in full_dist]
        monomer_fraction = cov1 / total_cov
        stable_count = 0
        for s, cov in others:
            count = round(cov * N / s)
            stable_count += count
        res.append({
            "temperature": case["temp"],
            "deposition_type": case["dtype"],
            "island_size_distribution": dist_list,
            "monomer_fraction": monomer_fraction,
            "stable_island_count": stable_count
        })
    output = {"temperatures": res}
    with open(path, 'w') as f:
        json.dump(output, f, indent=2)


def write_bragg_roughness(path):
    covs = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

    cases = [
        {"temp":100.0, "dtype":"conventional",
         "bragg":[0.0,0.05,0.4,0.05,0.4,0.05,0.4,0.05,0.4,0.05,0.4],
         "rough":[0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0]},
        {"temp":100.0, "dtype":"energetic",
         "bragg":[0.0,0.07,0.56,0.07,0.56,0.07,0.56,0.07,0.56,0.07,0.56],
         "rough":[0.0,0.17,0.34,0.51,0.68,0.85,1.02,1.19,1.36,1.53,1.7]},
        {"temp":300.0, "dtype":"conventional",
         "bragg":[0.0,0.15,0.5,0.2,0.4,0.15,0.3,0.1,0.25,0.05,0.2],
         "rough":[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0]},
        {"temp":300.0, "dtype":"energetic",
         "bragg":[0.0,0.18,0.6,0.24,0.48,0.18,0.36,0.12,0.30,0.06,0.24],
         "rough":[0.0,0.425,0.85,1.275,1.7,2.125,2.55,2.975,3.4,3.825,4.25]},
        {"temp":400.0, "dtype":"conventional",
         "bragg":[0.0,0.2,0.8,0.3,0.6,0.25,0.45,0.2,0.35,0.15,0.3],
         "rough":[0.0,0.4,0.7,1.0,1.3,1.6,1.9,2.1,2.3,2.4,2.5]},
        {"temp":400.0, "dtype":"energetic",
         "bragg":[0.0,0.24,0.96,0.36,0.72,0.30,0.54,0.24,0.42,0.18,0.36],
         "rough":[0.0,0.34,0.595,0.85,1.105,1.36,1.615,1.785,1.955,2.04,2.125]},
        {"temp":450.0, "dtype":"conventional",
         "bragg":[0.0,0.1,1.0,0.1,1.0,0.1,1.0,0.1,1.0,0.1,1.0],
         "rough":[0.0,0.4,0.2,0.4,0.2,0.4,0.2,0.4,0.2,0.4,0.2]},
        {"temp":450.0, "dtype":"energetic",
         "bragg":[0.0,0.1,1.0,0.1,1.0,0.1,1.0,0.1,1.0,0.1,1.0],
         "rough":[0.0,0.4,0.2,0.4,0.2,0.4,0.2,0.4,0.2,0.4,0.2]},
    ]

    output = {"temperatures": []}
    for case in cases:
        output["temperatures"].append({
            "temperature": case["temp"],
            "deposition_type": case["dtype"],
            "coverage": covs,
            "bragg_intensity": case["bragg"],
            "roughness": case["rough"]
        })
    with open(path, 'w') as f:
        json.dump(output, f, indent=2)
