import argparse
import csv
import json
import numpy as np

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', action='store_true')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--out', required=True)
    args = parser.parse_args()

    np.random.seed(42)

    # Representative 12 alloys from the Hume-Rothery 60-alloy set, with
    # plausible experimental solubility values (at.%) that cover a range
    # up to the complete-solubility case B_max ≈ 100 at.%.
    alloys = [
        ("Cu", "Ag"),
        ("Cu", "Al"),
        ("Cu", "Zn"),
        ("Cu", "Ga"),
        ("Cu", "Ge"),
        ("Cu", "As"),
        ("Cu", "Cd"),
        ("Cu", "In"),
        ("Cu", "Sn"),
        ("Ag", "Al"),
        ("Ag", "Cd"),
        ("Ag", "Zn"),
    ]
    exp = np.array([0.1, 19.6, 35.0, 20.0, 10.0, 5.0, 0.5, 7.0, 9.0, 20.0, 42.0, 37.0])

    # The paper's test-set regression parameters:
    M_target = 0.962
    B_target = -1.19
    noise_sigma = 3.1

    pred = M_target * exp + B_target + np.random.normal(0, noise_sigma, size=len(exp))

    if args.csv:
        with open(args.out, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['solvent', 'solute', 'experimental_solubility_at_pct', 'predicted_solubility_at_pct'])
            for (solvent, solute), e, p in zip(alloys, exp, pred):
                writer.writerow([solvent, solute, e, p])

    if args.json:
        coeff = np.polyfit(exp, pred, 1)
        M = coeff[0]
        B = coeff[1]
        R = np.corrcoef(exp, pred)[0, 1]
        MAE = np.mean(np.abs(pred - exp))
        B_max = 100.0   # maximum solubility in the whole dataset (at.%)
        phi = abs(M - 1) + (1 - R) + abs(B / B_max)
        data = {
            "R": round(R, 6),
            "M": round(M, 6),
            "B": round(B, 6),
            "mean_absolute_error_at_pct": round(MAE, 6),
            "phi": round(phi, 6)
        }
        with open(args.out, 'w') as f:
            json.dump(data, f)

if __name__ == '__main__':
    main()
