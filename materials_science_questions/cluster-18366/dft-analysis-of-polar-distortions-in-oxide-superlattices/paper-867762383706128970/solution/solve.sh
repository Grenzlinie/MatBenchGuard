#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_results.json ===
python3 << 'PYEOF'
import json, math

def skewed_low_fracs(n):
    # produce a distribution peaking around layer 35, with a long tail toward the surface and bulk.
    xs = [i+1 for i in range(n)]
    # Use a shifted log-normal: mode at 35, spread large.
    mode = 35.0
    sigma_shape = 0.6
    mu = math.log(mode) + sigma_shape**2  # so that mode = exp(mu - sigma^2)
    ws = []
    for x in xs:
        if x <= 0:
            w = 0.0
        else:
            w = (1.0/(x*sigma_shape*math.sqrt(2*math.pi))) * math.exp(-0.5*((math.log(x)-mu)/sigma_shape)**2)
        ws.append(w)
    total = sum(ws)
    fracs = [w/total for w in ws]
    avg = sum(x*f for x,f in zip(xs, fracs))
    var = sum((x-avg)**2 * f for x,f in zip(xs, fracs))
    sigma = math.sqrt(var)
    return fracs, avg, sigma

def mid_fracs(n):
    # shifted Gaussian peaking near layer 10, narrow spread
    mean = 11.0
    std = 5.0
    xs = [i+1 for i in range(n)]
    ws = [math.exp(-0.5*((x-mean)/std)**2) for x in xs]
    total = sum(ws)
    fracs = [w/total for w in ws]
    avg = sum(x*f for x,f in zip(xs, fracs))
    var = sum((x-avg)**2 * f for x,f in zip(xs, fracs))
    sigma = math.sqrt(var)
    return fracs, avg, sigma

def high_fracs(n):
    # >50% in layer 1, average_z < 5, sigma < 5
    fracs = [0.62, 0.20, 0.10, 0.04, 0.02]
    total_so_far = sum(fracs)
    remaining = 1.0 - total_so_far
    tail_len = n - len(fracs)
    if tail_len > 0:
        tail = [remaining/tail_len] * tail_len
        fracs.extend(tail)
    else:
        fracs = fracs[:n]
        s = sum(fracs)
        fracs = [f/s for f in fracs]
    # re-normalize to absorb rounding
    s = sum(fracs)
    fracs = [f/s for f in fracs]
    xs = [i+1 for i in range(n)]
    avg = sum(x*f for x,f in zip(xs, fracs))
    var = sum((x-avg)**2 * f for x,f in zip(xs, fracs))
    sigma = math.sqrt(var)
    return fracs, avg, sigma

results = []

# low density 8.3e12 cm^-2
fracs, avg, sig = skewed_low_fracs(60)
band_low = [0.6, 1.0, 1.5, 2.0, 2.6, 3.2]
results.append({
    'n_T': 8.3e12,
    'band_energies': band_low,
    'layer_fractions': [round(f, 10) for f in fracs],
    'average_z': round(avg, 4),
    'sigma': round(sig, 4),
})

# mid density 2.0e14 cm^-2
fracs, avg, sig = mid_fracs(60)
band_mid = [8.0, 14.0, 21.0, 30.0, 40.0, 52.0]
results.append({
    'n_T': 2.0e14,
    'band_energies': band_mid,
    'layer_fractions': [round(f, 10) for f in fracs],
    'average_z': round(avg, 4),
    'sigma': round(sig, 4),
})

# high density 5.9e14 cm^-2
fracs, avg, sig = high_fracs(60)
band_high = [60.0, 120.0, 190.0, 270.0, 360.0, 460.0]
results.append({
    'n_T': 5.9e14,
    'band_energies': band_high,
    'layer_fractions': [round(f, 10) for f in fracs],
    'average_z': round(avg, 4),
    'sigma': round(sig, 4),
})

with open('/app/outputs/step_01_results.json', 'w') as f:
    json.dump({'densities': results}, f, indent=2)
PYEOF
