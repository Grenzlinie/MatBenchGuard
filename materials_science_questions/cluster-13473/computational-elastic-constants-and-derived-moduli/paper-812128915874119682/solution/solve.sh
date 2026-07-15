#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fitted_KT_params.json ===
cat > /app/outputs/fitted_KT_params.json << 'FFEOF'
{
  "beta_lambda_3": {
    "a_chi": 0.511,
    "b_chi": 0.748,
    "l0_star": 1.487
  },
  "beta_lambda_2": {
    "a_chi": 0.419,
    "b_chi": 0.748,
    "l0_star": 1.4278
  }
}
FFEOF

# === solve block: scaling_data.csv ===
python3 << 'PYEOF'
import csv, math

L = 28
chi6_vals = [100, 200, 300, 450, 650, 900, 1200]

params = {
    3: {'a_chi': 0.511, 'b_chi': 0.748, 'l0_star': 1.487},
    2: {'a_chi': 0.419, 'b_chi': 0.748, 'l0_star': 1.4278},
}

rows = []
for beta in [2, 3]:
    p = params[beta]
    a, b, l0s = p['a_chi'], p['b_chi'], p['l0_star']
    for chi6 in chi6_vals:
        if chi6 <= a:
            raise ValueError("chi6 must be > a")
        l0 = l0s + (b / math.log(chi6 / a)) ** 2
        xi6 = chi6 ** (4.0 / 7.0)
        chi6_scaled = chi6 / (L ** 1.75)
        xi6_over_L = xi6 / L
        rows.append([beta, L, round(l0, 6), xi6, chi6, chi6_scaled, xi6_over_L])

with open('/app/outputs/scaling_data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['beta_lambda','L','l0','xi6','chi6','chi6_scaled','xi6_over_L'])
    w.writerows(rows)
PYEOF

# === solve block: order_parameter_histograms_beta1.5.csv ===
python3 << 'PYEOF'
import csv, math

def gauss_pdf(x, mu, sigma):
    return (1.0/(sigma*math.sqrt(2*math.pi))) * math.exp(-0.5 * ((x-mu)/sigma)**2)

def mixture_pdf(x):
    w1, w2 = 0.4, 0.6
    p1 = gauss_pdf(x, 0.05, 0.05)   # peak near zero
    p2 = gauss_pdf(x, 0.55, 0.05)   # peak near 0.55
    return w1 * p1 + w2 * p2

# transition l0 values from the paper (approximate)
configs = [(196, 1.395), (400, 1.375), (784, 1.370)]
nbins = 50
bin_edges = [i*0.02 for i in range(nbins+1)]  # 0.0 to 1.0

with open('/app/outputs/order_parameter_histograms_beta1.5.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['N','l0','psi6_bin_low','psi6_bin_high','count'])
    total_counts = 10000
    for N, l0 in configs:
        for i in range(nbins):
            low = bin_edges[i]
            high = bin_edges[i+1]
            center = 0.5 * (low + high)
            prob = mixture_pdf(center)
            cnt = max(1, int(total_counts * prob * (high-low)))  # scale by bin width
            w.writerow([N, l0, round(low,2), round(high,2), cnt])
PYEOF

# === solve finalize ===
echo 'All oracle artifacts written.'
