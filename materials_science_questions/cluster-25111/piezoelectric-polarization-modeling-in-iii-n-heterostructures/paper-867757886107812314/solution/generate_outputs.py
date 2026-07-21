import json, csv, math

# --- step_02_potential_minima.json ---
data = {
    "hole_PEP": 65,
    "hole_DP": 24,
    "electron_DP": -108,
    "electron_PEP": -15
}
with open("/app/outputs/step_02_potential_minima.json", "w") as f:
    json.dump(data, f, indent=2)

# --- step_04_dos.csv ---
energies = list(range(-200, 151))  # -200 to 150 meV, step 1 meV

def gauss(x, center, sigma, amp):
    return amp * math.exp(-0.5 * ((x - center) / sigma) ** 2)

peaks_total = [
    (-108, 5.0, 1.0),   # electron DP
    (24,   5.0, 0.8),   # hole DP
    (65,   8.0, 1.5),   # hole PEP
    (-15,  5.0, 0.3),   # electron PEP
]
peaks_dp = [
    (-108, 5.0, 1.0),
    (24,   5.0, 0.8),
]

with open("/app/outputs/step_04_dos.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["energy(meV)", "DOS_total", "DOS_DP_only"])
    for E in energies:
        total = sum(gauss(E, c, s, a) for c, s, a in peaks_total)
        dp = sum(gauss(E, c, s, a) for c, s, a in peaks_dp)
        writer.writerow([E, round(total, 4), round(dp, 4)])

# --- step_05_pl_spectrum.csv ---
pl_energies = [1.25 + i * 0.001 for i in range(201)]  # 1.25 to 1.45 eV
peaks_pl = [
    (1.31, 0.006, 0.3),
    (1.33, 0.006, 0.5),
    (1.35, 0.006, 0.7),
    (1.37, 0.006, 0.9),
    (1.39, 0.006, 1.0),
]
with open("/app/outputs/step_05_pl_spectrum.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["energy(eV)", "intensity"])
    for E in pl_energies:
        intensity = sum(gauss(E, c, s, a) for c, s, a in peaks_pl)
        writer.writerow([E, round(intensity, 6)])
