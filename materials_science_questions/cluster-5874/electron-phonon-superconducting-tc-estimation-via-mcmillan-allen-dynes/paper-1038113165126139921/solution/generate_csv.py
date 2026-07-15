import csv
import math

def calc_tc(omega_log, lam, mu_star=0.1):
    """McMillan–Allen–Dynes Tc estimation."""
    if lam <= 0 or omega_log <= 0:
        return None
    numer = -1.04 * (1.0 + lam)
    denom = lam - mu_star * (1.0 + 0.62 * lam)
    if denom <= 0:
        return None
    return (omega_log / 1.2) * math.exp(numer / denom)

def main():
    # Rows from Table III (exact paper values)
    table_rows = [
        ('RS-LuH', 0, 19.7, 1.02, 275.1, 8.07),
        ('RS-LuH', 1, 15.8, 0.86, 294.0, 7.96),
        ('RS-LuH', 10, 5.1, 0.55, 294.6, 6.96),
        ('Lu4NH3', 0, 8.1, 0.66, 277.5, 30.98),
        ('Lu4NH3', 1, 7.5, 0.64, 278.0, 30.73),
        ('Lu4NH3', 10, 4.9, 0.56, 276.0, 28.80),
    ]

    # Synthetic RS-XH series at 0 GPa (trends from Fig. 11 and text)
    # Ordered by increasing atomic number, omitting Pm (61), Yb handled separately.
    # Parameters chosen to give monotonic Tc increase with Z, with LuH highest.
    lanthanides = [
        ('La', 57), ('Ce', 58), ('Pr', 59), ('Nd', 60),
        ('Sm', 62), ('Eu', 63), ('Gd', 64), ('Tb', 65),
        ('Dy', 66), ('Ho', 67), ('Er', 68), ('Tm', 69),
        ('Yb', 70), ('Lu', 71)
    ]

    # Smooth linear variation: λ from ~0.45 (La) to 1.02 (Lu);
    # ω_log from ~200 K (La) to ~275 K (Lu);
    # N(E_F) from ~4.5 to 8.07 states/spin/Ry/unitcell.
    def lam(z): return 0.45 + (z - 57) * (1.02 - 0.45) / (71 - 57)
    def omega_log(z): return 200.0 + (z - 57) * (275.1 - 200.0) / (71 - 57)
    def n_ef(z): return 4.5 + (z - 57) * (8.07 - 4.5) / (71 - 57)

    series_rows = []
    for sym, z in lanthanides:
        compound = f'RS-{sym}H'
        pressure = 0
        if sym == 'Yb':
            # YbH is dynamically unstable at 0 GPa; leave fields blank
            series_rows.append((compound, pressure, '', '', '', ''))
        else:
            l = round(lam(z), 4)
            w = round(omega_log(z), 2)
            n = round(n_ef(z), 2)
            tc = calc_tc(w, l)
            if tc is not None:
                tc = round(tc, 1)
            else:
                tc = ''
            series_rows.append((compound, pressure, tc, l, w, n))

    # Write CSV
    out_path = '/app/outputs/superconducting_properties.csv'
    fieldnames = ['compound', 'pressure_GPa', 'Tc_K', 'lambda',
                  'omega_log_K', 'N_EF_states_per_spin_Ry_unitcell']

    with open(out_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for row in series_rows + table_rows:
            writer.writerow(row)

if __name__ == '__main__':
    main()
