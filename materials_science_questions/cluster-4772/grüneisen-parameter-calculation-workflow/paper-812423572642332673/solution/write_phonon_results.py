import csv, sys

def main(outdir):
    rows = [
        # GaN ambient
        ("GaN", "ambient", "Γ", "LO", 743.0, 0.91),
        ("GaN", "ambient", "Γ", "TO", 552.0, 1.00),
        # GaN high (52.2 GPa)
        ("GaN", "high", "Γ", "LO", 915.0, 0.91),
        ("GaN", "high", "Γ", "TO", 693.0, 1.00),
        # AlN ambient
        ("AlN", "ambient", "Γ", "LO", 902.0, 0.72),
        ("AlN", "ambient", "Γ", "TO", 655.0, 0.82),
        # AlN high (22.9 GPa)
        ("AlN", "high", "Γ", "LO", 971.0, 0.72),
        ("AlN", "high", "Γ", "TO", 712.0, 0.82),
    ]
    with open(f"{outdir}/phonon_results.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["compound", "pressure", "q_point", "mode", "frequency_cm1", "mode_gamma"])
        w.writerows(rows)

if __name__ == "__main__":
    main(sys.argv[1])
