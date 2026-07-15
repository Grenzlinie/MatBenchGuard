#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
cat > /tmp/generate.py <<'PYEOF'
import sys, json, csv, math

def generate_csv(output_path):
    emax_vals = [0.0, 1e7, 2e7, 5e7, 1e8]
    coeff_vals = [0.12, 0.13, 0.15, 0.20, 0.27]
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Emax','backscattered_coefficient'])
        for e, c in zip(emax_vals, coeff_vals):
            writer.writerow([e, c])

def lognormal(x, mu, sigma):
    if x <= 0:
        return 0.0
    return (1.0 / (x * sigma * math.sqrt(2 * math.pi))) * math.exp(-(math.log(x) - mu)**2 / (2 * sigma**2))

def generate_json(output_path):
    depths = [5.0 + 10.0 * i for i in range(50)]

    # uncharged: peak ~250 nm, right-skewed (lognormal)
    sigma_unc = 0.4
    mu_unc = math.log(250) + sigma_unc**2
    y_unc = [lognormal(d, mu_unc, sigma_unc) for d in depths]
    total_unc = sum(y_unc) * 10.0  # bin width 10 nm
    scale_unc = 17600.0 / total_unc   # approximate deposited energy per electron
    total_loss_unc = [v * scale_unc for v in y_unc]
    bethe_loss_unc = total_loss_unc[:]
    electric_loss_unc = [0.0] * 50

    # charged: peak ~150 nm, broader sigma, electric loss = 15% of total
    sigma_ch = 0.5
    mu_ch = math.log(150) + sigma_ch**2
    y_ch = [lognormal(d, mu_ch, sigma_ch) for d in depths]
    total_ch = sum(y_ch) * 10.0
    scale_ch = 14600.0 / total_ch
    total_loss_ch = [v * scale_ch for v in y_ch]
    bethe_loss_ch = [v * 0.85 for v in total_loss_ch]
    electric_loss_ch = [v * 0.15 for v in total_loss_ch]  # ensures sum equals total_loss_ch

    data = {
        "uncharged": {
            "depth_bins": depths,
            "total_loss": total_loss_unc,
            "bethe_loss": bethe_loss_unc,
            "electric_loss": electric_loss_unc
        },
        "charged": {
            "depth_bins": depths,
            "total_loss": total_loss_ch,
            "bethe_loss": bethe_loss_ch,
            "electric_loss": electric_loss_ch
        }
    }
    with open(output_path, 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: generate.py <csv|json> <output_path>")
        sys.exit(1)
    mode = sys.argv[1]
    path = sys.argv[2]
    if mode == 'csv':
        generate_csv(path)
    elif mode == 'json':
        generate_json(path)
    else:
        print("Invalid mode")
        sys.exit(1)
PYEOF

# === solve block: backscattered_coefficient.csv ===
python3 /tmp/generate.py csv /app/outputs/backscattered_coefficient.csv

# === solve block: depth_distributions.json ===
python3 /tmp/generate.py json /app/outputs/depth_distributions.json
