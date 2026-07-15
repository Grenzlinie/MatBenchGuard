import csv
import math

def compute_breaking_force(genome_kb):
    if genome_kb == 0:
        # empty capsid: osmotic term zero, force = k_empty * D
        k_empty = 0.13  # N/m
        D = 6.5e-9      # m
        force_nN = k_empty * D * 1e9  # convert to nN
        return round(force_nN, 4)

    # parameters
    r0 = 29.5          # nm
    V0 = 87114         # nm^3
    k_empty = 0.13     # N/m
    D = 6.5            # nm
    F0 = 1.2e4         # pN/nm^2
    c_val = 0.30       # nm
    bp_len = 0.34      # nm per base pair

    # contour length in nm
    L_contour = genome_kb * 1000 * bp_len

    # volume change due to indentation
    factor = 3.0 / (16.0 * r0 * r0)
    V0_over_V = 1.0 + factor * D * D
    V = V0 / V0_over_V

    # interaxial spacing d
    inner = math.sqrt(2.0 * V / math.sqrt(3.0))
    d = inner / math.sqrt(L_contour)

    # osmotic pressure (pN/nm^2)
    Pi = F0 * math.exp(-d / c_val)

    # osmotic contribution to force (pN)
    osmotic_force_pN = Pi * (math.pi * r0 / 2.0) * D
    osmotic_force_nN = osmotic_force_pN / 1000.0  # 1 nN = 1000 pN

    # empty-capsid contribution (nN)
    empty_force_nN = k_empty * D * 1e-9  # D in m: k_empty (N/m) * D (m) -> N, then convert
    # but easier: k_empty * D_in_m = 0.13 * 6.5e-9 = 8.45e-10 N = 0.845 nN, so direct:
    empty_force_nN = 0.845

    total_force_nN = empty_force_nN + osmotic_force_nN
    return round(total_force_nN, 4)

conditions = [
    (0.0, 0.0),      # 0% fill
    (78.0, 37.7),    # 78% fill
    (94.0, 45.7),    # 94% fill
    (100.0, 48.5)    # 100% fill
]

rows = []
for percent, kb in conditions:
    force = compute_breaking_force(kb)
    rows.append((kb, percent, force))

with open('/app/outputs/model_predictions.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['genome_length_kb', 'genome_length_percent', 'predicted_breaking_force_nN'])
    for kb, percent, force in rows:
        writer.writerow([kb, percent, force])
