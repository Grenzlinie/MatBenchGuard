#!/usr/bin/env python3
import argparse, csv, math

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--beta', type=float, required=True)
    parser.add_argument('--output', type=str, required=True)
    parser.add_argument('--A', type=float, default=1.0)
    parser.add_argument('--tmin', type=float, default=0.1)
    parser.add_argument('--tmax', type=float, default=1000)
    parser.add_argument('--npoints', type=int, default=100)
    args = parser.parse_args()
    ts = [args.tmin * (args.tmax/args.tmin)**(i/args.npoints) for i in range(args.npoints)]
    vs = [args.A * t**(-args.beta) for t in ts]
    with open(args.output, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['time', 'velocity'])
        for t, v in zip(ts, vs):
            writer.writerow([t, v])

if __name__ == '__main__':
    main()
