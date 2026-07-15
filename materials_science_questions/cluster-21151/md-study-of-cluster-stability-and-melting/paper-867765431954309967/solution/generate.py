import csv
import math
import random
import sys

def sigmoid(t, center, width, scale, offset):
    return offset + scale / (1 + math.exp(-(t - center) / width))

def generate_traces(filename, n_neighbors=5, n_steps=200, dt=1.0):
    random.seed(42)
    times = [i * dt for i in range(n_steps)]
    target_trace = []
    for t in times:
        val = sigmoid(t, center=100.0, width=5.0, scale=100.0, offset=20.0)
        val += random.gauss(0, 1.5)
        target_trace.append(max(0, val))
    neighbors = []
    for i in range(n_neighbors):
        c = 100.0 + random.uniform(-3, 3)
        w = 5.0 + random.uniform(-0.5, 0.5)
        s = 100.0 + random.uniform(-5, 5)
        o = 20.0 + random.uniform(-2, 2)
        trace = []
        for t in times:
            val = sigmoid(t, c, w, s, o)
            val += random.gauss(0, 1.5)
            trace.append(max(0, val))
        neighbors.append(trace)
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        header = ['time', 'target_IC'] + [f'neighbor_{j+1}_IC' for j in range(n_neighbors)]
        writer.writerow(header)
        for idx, t in enumerate(times):
            row = [t, target_trace[idx]] + [neighbors[j][idx] for j in range(n_neighbors)]
            writer.writerow(row)

def generate_coherence(filename):
    rows = [
        {'temperature': 1400.0, 'coherence_length': 4.0},
        {'temperature': 1300.0, 'coherence_length': 6.0}
    ]
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['temperature', 'coherence_length'])
        for row in rows:
            writer.writerow([row['temperature'], row['coherence_length']])

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'traces'
    output = sys.argv[2] if len(sys.argv) > 2 else '/app/outputs/ic_traces.csv'
    if mode == 'traces':
        generate_traces(output)
    elif mode == 'coherence':
        generate_coherence(output)
