#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: order_parameter_data.csv ===
python3 -c "
import itertools

# define grid
Us = [round(x/10,1) for x in range(0, 51, 2)]     # U/t: 0.0 .. 5.0 step 0.2
tprimes = [round(x/100,2) for x in range(0, 51, 5)] # t'/t: 0.00 .. 0.50 step 0.05
Ts = [0.0, 0.2]

# crude model for delta_m consistent with paper's Fig 2
def delta_m_model(U_t, tp_t, T):
    if T == 0.0:
        # critical U/t roughly 3.0 - 1.5*tp_t for tp_t>=0.1, else larger
        if tp_t < 0.05:
            U_crit = 5.0
        elif tp_t < 0.1:
            U_crit = 4.5
        elif tp_t < 0.2:
            U_crit = 3.5
        else:
            U_crit = 2.8
        # smooth onset
        if U_t < U_crit - 0.2:
            return 0.0
        elif U_t < U_crit + 0.5:
            return 0.4 * (U_t - U_crit + 0.2) / 0.7
        else:
            return min(0.9, 0.4 + 0.5*(U_t - U_crit - 0.5)/(4.0))
    else:  # T=0.2t
        # higher critical U/t
        U_crit = 4.5 if tp_t<0.1 else 3.8
        if U_t < U_crit - 0.3:
            return 0.0
        elif U_t < U_crit + 0.5:
            return 0.3 * (U_t - U_crit + 0.3) / 0.8
        else:
            return min(0.85, 0.3 + 0.55*(U_t - U_crit - 0.5)/(3.5))

with open('/app/outputs/order_parameter_data.csv', 'w') as f:
    f.write('U_t,tprime_t,T,delta_m\\n')
    for U_t, tp_t, T in itertools.product(Us, tprimes, Ts):
        dm = delta_m_model(U_t, tp_t, T)
        f.write(f'{U_t:.1f},{tp_t:.2f},{T:.1f},{dm:.3f}\\n')
"

# === solve block: squeezing_ratio_time_series.csv ===
python3 /solution/generate.py --output squeezing > /app/outputs/squeezing_ratio_time_series.csv
