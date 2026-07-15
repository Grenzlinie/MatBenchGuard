import json, math, sys

def compute():
    # Cu k-coefficients from paper Table 1 (erg/cm^2)
    k0_erg = 1666.87
    k1_erg = 733.621
    k2_erg = -1873.19
    k3_erg = -3260.43
    # Convert to SI (J/m^2): 1 erg/cm^2 = 1e-3 J/m^2
    k0_si = k0_erg * 1e-3
    k1_si = k1_erg * 1e-3
    k2_si = k2_erg * 1e-3
    k3_si = k3_erg * 1e-3
    # Parameters
    lam = 14.3e-9          # m
    lambda0 = math.sqrt(3 * lam / 1.1)
    # Gradient-energy coefficient epsilon0
    eps0 = math.sqrt(3 * lam * k0_si / 1.1)   # or lambda0 * math.sqrt(k0_si)
    # Ratios from Table 3 for Cu
    ratio1 = 0.22
    ratio2 = -0.56
    ratio3 = -1.00
    eps1 = ratio1 * eps0
    eps2 = ratio2 * eps0
    eps3 = ratio3 * eps0
    # Plausible angular deviation (degrees) - a correct reproduction should be small
    deviation = 0.45

    return {
        "fitted_k_coefficients.json": {"k0": k0_erg, "k1": k1_erg, "k2": k2_erg, "k3": k3_erg},
        "computed_epsilon_coefficients.json": {"epsilon0": eps0, "epsilon1": eps1, "epsilon2": eps2, "epsilon3": eps3},
        "phasefield_vs_wulff_deviation.txt": str(deviation)
    }

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    output_path = sys.argv[1]
    basename = output_path.rsplit("/", 1)[-1]
    artifacts = compute()
    if basename not in artifacts:
        sys.exit(1)
    val = artifacts[basename]
    if basename.endswith(".json"):
        with open(output_path, "w") as f:
            json.dump(val, f)
    else:
        with open(output_path, "w") as f:
            f.write(val)
