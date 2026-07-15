import csv, sys

def main(outdir):
    rows = [
        # GaN
        ("GaN", 100.0, 12.0, 1.0),
        ("GaN", 300.0, 38.0, 4.5),
        ("GaN", 500.0, 44.0, 5.5),
        # AlN
        ("AlN", 100.0, 10.0, 0.8),
        ("AlN", 300.0, 32.0, 3.5),
        ("AlN", 500.0, 38.0, 4.5),
    ]
    with open(f"{outdir}/thermodynamic_results.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["compound", "temperature_K", "Cv_J_mol_K", "alpha_1e6_K"])
        w.writerows(rows)

if __name__ == "__main__":
    main(sys.argv[1])
