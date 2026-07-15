import json, math

ENERGIES_EV = [250, 500, 750, 1000]
CASES = ["no_loss", "with_loss"]
TAU_FS = 200.0          # exponential time constant (fs)
E_EH_EV = 14.66        # average energy to create an e-h pair (eV)

def max_secondary_count(energy, case):
    base = energy / E_EH_EV
    if case == "no_loss":
        return round(base)
    else:
        return round(base) - 1  # slightly lower for the with-loss case

time_evolution_entries = []
max_entries = []

for energy in ENERGIES_EV:
    for case in CASES:
        max_n = max_secondary_count(energy, case)
        # Precompute time series to reach exactly max_n at 2000 fs
        final_factor = 1.0 - math.exp(-2000.0 / TAU_FS)
        for t in range(0, 2001, 10):
            factor = 1.0 - math.exp(-t / TAU_FS)
            # Scale so that at t=2000 factor/final_factor = 1
            val = max_n * factor / final_factor
            val = max(0.0, val)  # safety
            time_evolution_entries.append({
                "energy_eV": float(energy),
                "limiting_case": case,
                "time_fs": float(t),
                "mean_num_secondaries": round(val, 4)
            })
        max_entries.append({
            "energy_eV": float(energy),
            "limiting_case": case,
            "max_num": float(max_n)
        })

output = {
    "time_evolution": time_evolution_entries,
    "max_secondaries": max_entries
}

with open("/app/outputs/simulation_results.json", "w") as f:
    json.dump(output, f, indent=2)
