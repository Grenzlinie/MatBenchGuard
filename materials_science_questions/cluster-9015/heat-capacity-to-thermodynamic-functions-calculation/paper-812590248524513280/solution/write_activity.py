import csv, sys, math

out = sys.argv[1]
epsv = {1400: 2.655, 1600: 2.878}  # epsilon_Al^P from paper (Table 2, Fig. 9)
rows = []
for t_C in [1400, 1600]:
    eps = epsv[t_C]
    for wt_Al in [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]:
        log10_gamma = eps * wt_Al
        gamma_P = 10 ** log10_gamma
        rows.append({
            "T_C": t_C,
            "wt_Al": wt_Al,
            "gamma_P": gamma_P,
            "log10_gamma_P": log10_gamma
        })

with open(out, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=["T_C", "wt_Al", "gamma_P", "log10_gamma_P"])
    w.writeheader()
    w.writerows(rows)
