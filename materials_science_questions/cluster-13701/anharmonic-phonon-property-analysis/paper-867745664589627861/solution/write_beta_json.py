#!/usr/bin/env python3
import argparse, json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--beta_highT', type=float, required=True)
    parser.add_argument('--beta_lowT', type=float, required=True)
    parser.add_argument('--output', type=str, required=True)
    args = parser.parse_args()
    data = {'beta_highT': args.beta_highT, 'beta_lowT': args.beta_lowT}
    with open(args.output, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    main()
