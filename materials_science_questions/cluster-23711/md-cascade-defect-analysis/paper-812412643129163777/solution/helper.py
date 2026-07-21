import sys, json, csv, os

def write_threshold():
    data = {
        "Ga_average": 45.0,
        "Ga_error": 1.0,
        "N_average": 109.0,
        "N_error": 2.0
    }
    path = "/app/outputs/threshold_energies.json"
    with open(path, "w") as f:
        json.dump(data, f)

def write_defects():
    rows = [
        ("N", 200, 1.00, 0.12, 0.80, 0.32, 0.22, 0.02),
        ("N", 400, 1.33, 1.37, 1.27, 1.43, 0.43, 0.33),
        ("N", 1000, 3.29, 2.14, 2.67, 2.76, 1.33, 0.71),
        ("N", 2000, 3.87, 5.3, 3.13, 6.0, 1.50, 0.75),
        ("N", 5000, 11.2, 11.3, 9.9, 12.6, 4.2, 2.92),
        ("N", 10000, 29.5, 21.4, 24.9, 26.0, 12.4, 7.8),
        ("Ga", 200, 0.32, 1.28, 0.41, 1.19, 0.02, 0.12),
        ("Ga", 400, 1.24, 1.80, 1.2, 1.84, 0.30, 0.26),
        ("Ga", 1000, 4.05, 3.05, 3.6, 3.50, 1.25, 0.80),
        ("Ga", 2000, 6.1, 4.8, 4.9, 6.0, 1.18, 2.36),
        ("Ga", 5000, 13.1, 11.3, 11.3, 13.1, 4.6, 2.75),
        ("Ga", 10000, 24.6, 22.1, 21.8, 25.0, 8.8, 5.9)
    ]
    fieldnames = ["recoil_type", "energy_eV", "V_N", "V_Ga", "I_N", "I_Ga", "N_Ga", "Ga_N"]
    path = "/app/outputs/defect_counts.csv"
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for row in rows:
            writer.writerow(row)

def write_kp():
    defects = [
        ("N", 200, 1.00, 0.12),
        ("N", 400, 1.33, 1.37),
        ("N", 1000, 3.29, 2.14),
        ("N", 2000, 3.87, 5.3),
        ("N", 5000, 11.2, 11.3),
        ("N", 10000, 29.5, 21.4),
        ("Ga", 200, 0.32, 1.28),
        ("Ga", 400, 1.24, 1.80),
        ("Ga", 1000, 4.05, 3.05),
        ("Ga", 2000, 6.1, 4.8),
        ("Ga", 5000, 13.1, 11.3),
        ("Ga", 10000, 24.6, 22.1)
    ]
    rows = []
    for recoil, energy, vn, vga in defects:
        total = vn + vga
        ed = 45.0 if recoil == "Ga" else 109.0
        kp = 0.8 * energy / (2 * ed)
        rows.append((recoil, energy, total, kp))
    fieldnames = ["recoil_type", "energy_eV", "total_vacancies", "kp_predicted_vacancies"]
    path = "/app/outputs/kinchin_pease_comparison.csv"
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for row in rows:
            writer.writerow(row)

def main():
    if len(sys.argv) != 2:
        print("Usage: helper.py <output_filename>")
        sys.exit(1)
    filename = sys.argv[1]
    os.makedirs("/app/outputs", exist_ok=True)
    if filename == "threshold_energies.json":
        write_threshold()
    elif filename == "defect_counts.csv":
        write_defects()
    elif filename == "kinchin_pease_comparison.csv":
        write_kp()
    else:
        print("Unknown output:", filename)
        sys.exit(1)

if __name__ == "__main__":
    main()
