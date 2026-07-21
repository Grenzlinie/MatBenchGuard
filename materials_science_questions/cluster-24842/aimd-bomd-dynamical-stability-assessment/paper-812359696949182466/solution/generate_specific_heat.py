import csv
import math
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate synthetic specific-heat CSV')
    parser.add_argument('--T0', type=float, required=True, help='Peak temperature (K)')
    parser.add_argument('--T-min', type=float, required=True, help='Minimum temperature in range')
    parser.add_argument('--T-max', type=float, required=True, help='Maximum temperature in range')
    parser.add_argument('--step', type=float, default=5, help='Temperature step')
    parser.add_argument('--sigma', type=float, default=30, help='Width of Gaussian peak (K)')
    parser.add_argument('--amplitude', type=float, default=1.0, help='Peak amplitude of C_v/C_0')
    parser.add_argument('--baseline', type=float, default=0.2, help='Baseline C_v/C_0 value')
    parser.add_argument('--output', required=True, help='Output CSV file')
    args = parser.parse_args()

    with open(args.output, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['temperature_K', 'normalized_specific_heat'])
        T = args.T_min
        while T <= args.T_max:
            # Gaussian peak model: C_v/C_0 = baseline + amplitude * exp(-(T - T0)^2 / (2*sigma^2))
            C = args.baseline + args.amplitude * math.exp(-((T - args.T0) ** 2) / (2 * args.sigma ** 2))
            writer.writerow([f"{T:.1f}", f"{C:.6f}"])
            T += args.step

if __name__ == '__main__':
    main()
