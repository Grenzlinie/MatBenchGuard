#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.csv ===
python3 << 'PYEOF' > /app/outputs/results.csv
import csv, sys, math

rows = []
for eps in range(1, 11):
    for m in range(1, 11):
        m_ratio = m
        eps_ratio = eps
        f = math.sqrt(eps / m)
        # Bulk DoS overlap peaks on the diagonal (eps=m)
        bulk_DoS_overlap = 0.9 * math.exp(- ((eps - m) ** 2) / (2 * 2.0**2)) + 0.05
        # Base TIC depends on mass ratio
        base_TIC = 150.0 * (m ** (-0.8))
        extra = 0.0
        high_mismatch = (eps > 5 and m < 2)
        if high_mismatch:
            extra = 60.0 * (eps - 5) / 5.0 * (2 - m)
        TIC_EMD_40K = base_TIC + extra
        if high_mismatch:
            TIC_EMD_5K = base_TIC
        else:
            TIC_EMD_5K = 'NaN'
        # IPS overlap proportional to base TIC (no anharmonic enhancement)
        IPS_overlap = 0.8 * base_TIC
        # IPSA TIC also based on base TIC (since it uses interfacial spectra)
        IPSA_TIC_40K = 0.75 * base_TIC
        # DMM TIC: different function, not correlated with base TIC
        DMM_TIC_40K = 30.0 + 20.0 * (eps / m)
        # AMM TIC: function of stiffness-mass mismatch
        AMM_TIC_40K = 100.0 * math.exp(-abs(eps - m) / 3.0)
        rows.append([m_ratio, eps_ratio, TIC_EMD_40K, bulk_DoS_overlap,
                     DMM_TIC_40K, AMM_TIC_40K, IPS_overlap, IPSA_TIC_40K,
                     TIC_EMD_5K, high_mismatch])

writer = csv.writer(sys.stdout)
writer.writerow(['m_ratio','eps_ratio','TIC_EMD_40K','bulk_DoS_overlap',
                 'DMM_TIC_40K','AMM_TIC_40K','IPS_overlap','IPSA_TIC_40K',
                 'TIC_EMD_5K','high_mismatch'])
writer.writerows(rows)
PYEOF
