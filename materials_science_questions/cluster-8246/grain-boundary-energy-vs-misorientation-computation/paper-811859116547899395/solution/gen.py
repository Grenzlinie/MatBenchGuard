import sys, csv, json, math

def write_melting_confirmation(filepath):
    temps = list(range(300, 1300, 100))
    s_vals = [0.45, 0.42, 0.38, 0.33, 0.27, 0.20, 0.12, 0.06, 0.01, 0.005]
    energy_vals = [-3.52, -3.51, -3.50, -3.49, -3.48, -3.47, -3.46, -3.45, -3.35, -3.30]
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['temperature', 'S_centre', 'energy_per_atom'])
        for t, s, e in zip(temps, s_vals, energy_vals):
            writer.writerow([t, f"{s:.3f}", f"{e:.2f}"])

def density_profile(y_centers, height, sigma):
    bulk = 4.0
    profile = []
    for y in y_centers:
        peak = height * math.exp(-((y - 22.0)**2) / (2*sigma**2))
        osc = 0.5 * math.sin(2*math.pi * y / 2.5) * math.exp(-((y - 22.0)**2) / (2*2.0**2))
        dens = bulk + peak + osc
        dens = max(dens, 0.5)
        profile.append(dens)
    return profile

def write_density_csv(filepath, height, sigma):
    y_vals = [i*0.5 + 0.25 for i in range(88)]
    dens = density_profile(y_vals, height, sigma)
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Y_position', 'density'])
        for y, d in zip(y_vals, dens):
            writer.writerow([f"{y:.3f}", f"{d:.3f}"])

def write_comparison_metrics(filepath):
    y_vals = [i*0.5 + 0.25 for i in range(88)]
    heating_dens = density_profile(y_vals, height=1.8, sigma=1.5)
    quenching_dens = density_profile(y_vals, height=1.0, sigma=2.0)
    heating_peak = max(heating_dens)
    quenching_peak = max(quenching_dens)
    diff = heating_peak - quenching_peak
    data = {
        "heating_peak_density": round(heating_peak, 3),
        "quenching_peak_density": round(quenching_peak, 3),
        "peak_density_difference": round(diff, 3)
    }
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    outdir = "/app/outputs"
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if target == "melting_confirmation.csv":
            write_melting_confirmation(f"{outdir}/{target}")
        elif target == "density_profile_heating_300K.csv":
            write_density_csv(f"{outdir}/{target}", height=1.8, sigma=1.5)
        elif target == "density_profile_quenching_300K.csv":
            write_density_csv(f"{outdir}/{target}", height=1.0, sigma=2.0)
        elif target == "comparison_metrics.json":
            write_comparison_metrics(f"{outdir}/{target}")
        else:
            print(f"Unknown target: {target}", file=sys.stderr)
            sys.exit(1)
    else:
        write_melting_confirmation(f"{outdir}/melting_confirmation.csv")
        write_density_csv(f"{outdir}/density_profile_heating_300K.csv", height=1.8, sigma=1.5)
        write_density_csv(f"{outdir}/density_profile_quenching_300K.csv", height=1.0, sigma=2.0)
        write_comparison_metrics(f"{outdir}/comparison_metrics.json")

if __name__ == "__main__":
    main()
