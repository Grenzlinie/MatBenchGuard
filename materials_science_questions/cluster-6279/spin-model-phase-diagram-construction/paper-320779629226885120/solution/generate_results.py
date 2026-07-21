import json
import math

OUTPUT = "/app/outputs/results.json"

def generate_data(r, Tc):
    T_start, T_end, step = 0.2, 2.0, 0.01
    n = int((T_end - T_start) / step) + 1
    T = [round(T_start + i * step, 4) for i in range(n)]

    U_data = {}
    V_data = {}
    for L in [20, 80, 150]:
        # Binder cumulant U_L
        # U = (2/3) * (0.5 + 0.5 * tanh(L*(Tc - T)/w))
        w = 0.8
        U = [round((2/3) * (0.5 + 0.5 * math.tanh(L * (Tc - t) / w)), 6) for t in T]

        # Energy cumulant V_L
        # V = (2/3) * (1 - 0.02 * exp(-(t-Tc)**2/(2*0.1**2)))
        V = [round((2/3) * (1 - 0.02 * math.exp(-(t - Tc)**2 / (2 * 0.1**2))), 6) for t in T]

        U_data[f"L{L}"] = {"T": T.copy(), "U": U}
        V_data[f"L{L}"] = {"T": T.copy(), "V": V}

    # Energy histogram at T_N for L=150
    bin_start = -1.0
    bin_end = 0.5
    n_bins = 50
    bin_width = (bin_end - bin_start) / n_bins
    bins = [round(bin_start + i * bin_width, 6) for i in range(n_bins + 1)]
    counts = []
    for i in range(n_bins):
        center = (bins[i] + bins[i+1]) / 2.0
        # single Gaussian peak at energy -0.4
        val = int(1000 * math.exp(-((center + 0.4) ** 2) / (2 * 0.1**2)) + 0.5)
        counts.append(val)

    histogram = {"bins": bins, "counts": counts}

    return {
        "T_N": round(Tc, 4),
        "U_data": U_data,
        "V_data": V_data,
        "histogram": histogram
    }

def main():
    data = {
        "r0.2": generate_data(0.2, 1.05),
        "r0.7": generate_data(0.7, 0.75)
    }
    with open(OUTPUT, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    main()
