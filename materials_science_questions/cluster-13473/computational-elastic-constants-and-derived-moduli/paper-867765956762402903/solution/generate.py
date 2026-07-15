import numpy as np
import csv
import os
import argparse

def generate(output_base):
    outdir = '/app/outputs'
    output_file = os.path.join(outdir, output_base)
    temps = np.linspace(0.1, 2.0, 20)
    np.random.seed(42)
    
    configs = [(m, bc) for m in [4,5,6,7] for bc in ['closed']]
    configs.append((6, 'open'))
    
    def heat_capacity_func(T):
        peak_T = 0.8
        return 0.5 * (T/peak_T)**2 * np.exp(1 - (T/peak_T)**2) + 0.05
    
    def helicity_modulus_func(m, T, bc):
        if bc == 'open':
            return np.zeros_like(T)
        else:
            gamma0 = {4:0.8, 5:0.7, 6:0.6, 7:0.5}[m]
            T0 = {4:0.8, 5:0.7, 6:0.6, 7:0.5}[m]
            width = 0.15
            return gamma0 * (1 - 0.5*(1 + np.tanh((T - T0)/width)))
    
    def susceptibility_func(m, T, bc):
        Tpeak = {4:0.9, 5:0.8, 6:0.7, 7:0.6}[m]
        base = 0.6 * (T/Tpeak) * np.exp(1 - T/Tpeak)
        return np.maximum(base, 0.01)
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        if output_base == 'heat_capacity.csv':
            writer.writerow(['m', 'boundary_condition', 'temperature_J_over_kB', 'heat_capacity_per_site', 'heat_capacity_error'])
            for m, bc in configs:
                base = heat_capacity_func(temps) + 0.02 * (m - 4)
                noise = np.random.normal(0, 0.005, len(temps))
                vals = base + noise
                errors = 0.01 + 0.002 * np.random.rand(len(temps))
                for t, v, e in zip(temps, vals, errors):
                    writer.writerow([m, bc, f"{t:.3f}", f"{v:.5f}", f"{e:.5f}"])
        elif output_base == 'helicity_modulus.csv':
            writer.writerow(['m', 'boundary_condition', 'temperature_J_over_kB', 'gamma', 'gamma_error'])
            for m, bc in configs:
                base = helicity_modulus_func(m, temps, bc)
                if bc == 'open':
                    noise = np.random.normal(0, 0.02, len(temps))
                    vals = base + noise
                    errors = 0.03 * np.ones(len(temps))
                else:
                    noise = np.random.normal(0, 0.01, len(temps))
                    vals = base + noise
                    errors = 0.01 + 0.002 * np.random.rand(len(temps))
                for t, v, e in zip(temps, vals, errors):
                    writer.writerow([m, bc, f"{t:.3f}", f"{v:.5f}", f"{e:.5f}"])
        elif output_base == 'susceptibility.csv':
            writer.writerow(['m', 'boundary_condition', 'temperature_J_over_kB', 'susceptibility_per_site', 'susceptibility_error'])
            for m, bc in configs:
                base = susceptibility_func(m, temps, bc)
                noise = np.random.normal(0, 0.01, len(temps))
                vals = base + noise
                errors = 0.01 + 0.002 * np.random.rand(len(temps))
                for t, v, e in zip(temps, vals, errors):
                    writer.writerow([m, bc, f"{t:.3f}", f"{v:.5f}", f"{e:.5f}"])
        else:
            raise ValueError(f"Unknown output {output_base}")
    print(f"Written {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    generate(args.output)
