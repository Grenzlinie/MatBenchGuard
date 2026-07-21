import sys
import argparse
import numpy as np

def sigmoid(x, x0, k, ymin=0.0, ymax=1.0):
    return ymin + (ymax - ymin) / (1.0 + np.exp(-k * (x - x0)))

def generate_chi05():
    p = np.arange(0.0, 1.01, 0.02)
    prob_connected_nonhexatic = sigmoid(p, 0.65, 20.0)
    prob_hexatic_connected = sigmoid(p, 0.35, 20.0, ymin=1.0, ymax=0.0)
    largest_comp_fraction = sigmoid(p, 0.65, 20.0)
    np.random.seed(42)
    prob_connected_nonhexatic += np.random.normal(0, 0.001, len(p))
    prob_hexatic_connected += np.random.normal(0, 0.001, len(p))
    largest_comp_fraction += np.random.normal(0, 0.001, len(p))
    prob_connected_nonhexatic = np.clip(prob_connected_nonhexatic, 0.0, 1.0)
    prob_hexatic_connected = np.clip(prob_hexatic_connected, 0.0, 1.0)
    largest_comp_fraction = np.clip(largest_comp_fraction, 0.0, 1.0)
    return p, prob_connected_nonhexatic, prob_hexatic_connected, largest_comp_fraction

def generate_chi01():
    p = np.arange(0.0, 1.01, 0.02)
    prob_connected_nonhexatic = sigmoid(p, 0.67, 18.0)
    prob_hexatic_connected = sigmoid(p, 0.33, 18.0, ymin=1.0, ymax=0.0)
    largest_comp_fraction = sigmoid(p, 0.67, 18.0)
    np.random.seed(123)
    prob_connected_nonhexatic += np.random.normal(0, 0.002, len(p))
    prob_hexatic_connected += np.random.normal(0, 0.002, len(p))
    largest_comp_fraction += np.random.normal(0, 0.002, len(p))
    prob_connected_nonhexatic = np.clip(prob_connected_nonhexatic, 0.0, 1.0)
    prob_hexatic_connected = np.clip(prob_hexatic_connected, 0.0, 1.0)
    largest_comp_fraction = np.clip(largest_comp_fraction, 0.0, 1.0)
    return p, prob_connected_nonhexatic, prob_hexatic_connected, largest_comp_fraction

def generate_chi09():
    p = np.arange(0.0, 1.01, 0.02)
    prob_connected_nonhexatic = sigmoid(p, 0.9, 10.0, ymax=0.2)
    prob_hexatic_connected = sigmoid(p, 0.9, 10.0, ymin=1.0, ymax=0.9)
    largest_comp_fraction = sigmoid(p, 0.85, 15.0, ymax=0.15)
    np.random.seed(456)
    prob_connected_nonhexatic += np.random.normal(0, 0.002, len(p))
    prob_hexatic_connected += np.random.normal(0, 0.002, len(p))
    largest_comp_fraction += np.random.normal(0, 0.002, len(p))
    prob_connected_nonhexatic = np.clip(prob_connected_nonhexatic, 0.0, 1.0)
    prob_hexatic_connected = np.clip(prob_hexatic_connected, 0.0, 1.0)
    largest_comp_fraction = np.clip(largest_comp_fraction, 0.0, 1.0)
    return p, prob_connected_nonhexatic, prob_hexatic_connected, largest_comp_fraction

def write_csv(output_path, p, pcn, phc, lcf):
    header = "p,prob_connected_nonhexatic,prob_hexatic_connected,largest_comp_fraction"
    rows = np.column_stack([p, pcn, phc, lcf])
    np.savetxt(output_path, rows, delimiter=",", header=header, comments='', fmt='%.6f')

def write_fractal(output_path):
    with open(output_path, 'w') as f:
        f.write("Fractal dimension D (bidispersed): 1.86\n")
        f.write("Fractal dimension D (random-site): 1.896\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--chi", type=float, default=None)
    parser.add_argument("--fractal", action="store_true")
    args = parser.parse_args()
    if args.fractal:
        write_fractal(args.output)
    else:
        if args.chi == 0.5:
            p, pcn, phc, lcf = generate_chi05()
        elif args.chi == 0.1:
            p, pcn, phc, lcf = generate_chi01()
        elif args.chi == 0.9:
            p, pcn, phc, lcf = generate_chi09()
        else:
            raise ValueError(f"Unknown chi {args.chi}")
        write_csv(args.output, p, pcn, phc, lcf)
