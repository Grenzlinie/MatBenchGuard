import csv, math, os, sys

def main():
    if len(sys.argv) != 2:
        print("Usage: generate_curves.py {power_factor|seebeck|conductivity}", file=sys.stderr)
        sys.exit(1)
    mode = sys.argv[1]
    outdir = '/app/outputs'
    os.makedirs(outdir, exist_ok=True)

    # Sample parameters: doping (cm^-3), Si thickness (A), Ge thickness (A),
    # peak PF (W/mK^2), peak doping (cm^-3), PF shape width (log10),
    # Seebeck at 300K (V/K), conductivity (S/m)
    samples = {
        'JL254': {
            'doping_cm3': 0.8e19,
            'Si_A': 88, 'Ge_A': 22,
            'peak_pf': 0.28, 'n_peak': 2e19, 'sigma_pf': 0.3,
            'S_300': -250e-6,
            'conductivity': 12800
        },
        'JL255': {
            'doping_cm3': 1.0e19,
            'Si_A': 60, 'Ge_A': 15,
            'peak_pf': 0.24, 'n_peak': 1.8e19, 'sigma_pf': 0.3,
            'S_300': -230e-6,
            'conductivity': 16000
        },
        'JL256': {
            'doping_cm3': 1.2e19,
            'Si_A': 32, 'Ge_A': 8,
            'peak_pf': 0.20, 'n_peak': 1.5e19, 'sigma_pf': 0.3,
            'S_300': -210e-6,
            'conductivity': 19200
        }
    }

    if mode == 'power_factor':
        # generate PF vs carrier concentration at 300 K
        # concentrations from 1e17 to 1e21 cm^-3, logarithmic steps
        concentrations = [1e17, 2e17, 5e17, 1e18, 2e18, 5e18, 1e19, 2e19, 5e19, 1e20, 2e20, 5e20, 1e21]
        outpath = os.path.join(outdir, 'power_factor_vs_concentration.csv')
        with open(outpath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['sample', 'carrier_concentration_cm3', 'power_factor_WmK2'])
            for sample_name, params in samples.items():
                peak = params['peak_pf']
                n_peak = params['n_peak']
                sig = params['sigma_pf']
                for n in concentrations:
                    # compute PF using a log‑normal‑shaped peak
                    if sig > 0:
                        pf = peak * math.exp(-((math.log10(n) - math.log10(n_peak))**2 / (2 * sig**2)))
                    else:
                        pf = peak if n == n_peak else 0.0
                    pf = max(pf, 0.0)
                    writer.writerow([sample_name, n, pf])
        print("power_factor_vs_concentration.csv written.", file=sys.stderr)

    elif mode == 'seebeck':
        # Seebeck vs temperature (80‑300 K, step 10 K) for each sample's nominal doping
        temperatures = list(range(80, 310, 10))
        outpath = os.path.join(outdir, 'seebeck_vs_temperature.csv')
        with open(outpath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['sample', 'temperature_K', 'seebeck_uVK'])
            for sample_name, params in samples.items():
                S_300 = params['S_300']          # V/K at 300 K
                # model: |S| increases with decreasing T (non‑degenerate logarithmic trend)
                # S(T) = S_300 * (1 - a * ln(T/300))   with a > 0, so |S| larger at lower T
                a = 0.3
                for T in temperatures:
                    if T > 0:
                        factor = 1 - a * math.log(T / 300.0)
                    else:
                        factor = 1.0
                    S_V = S_300 * factor
                    S_uV = S_V * 1e6
                    writer.writerow([sample_name, T, S_uV])
        print("seebeck_vs_temperature.csv written.", file=sys.stderr)

    elif mode == 'conductivity':
        # electrical conductivity vs temperature (80‑300 K) with constant mobility (μ=100 cm²/Vs)
        # carrier concentration fixed → σ constant
        temperatures = list(range(80, 310, 10))
        outpath = os.path.join(outdir, 'conductivity_vs_temperature.csv')
        with open(outpath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['sample', 'temperature_K', 'conductivity_Sm'])
            for sample_name, params in samples.items():
                sigma = params['conductivity']
                for T in temperatures:
                    writer.writerow([sample_name, T, sigma])
        print("conductivity_vs_temperature.csv written.", file=sys.stderr)

    else:
        print(f"Unknown mode: {mode}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
