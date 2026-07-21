import sys, argparse, csv, math
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True)
    parser.add_argument('--exponent', type=float, required=True)
    parser.add_argument('--scale', type=float, required=True)
    parser.add_argument('--time-step', type=float, required=True)
    parser.add_argument('--max-time', type=float, required=True)
    args = parser.parse_args()
    times = [i*args.time_step for i in range(0, int(args.max_time//args.time_step)+1)]
    with open(args.out, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['time', 'surface_width'])
        for t in times:
            if t == 0:
                width = 0.0
            else:
                width = args.scale * (t ** args.exponent)
            w.writerow([t, width])
if __name__ == '__main__':
    main()