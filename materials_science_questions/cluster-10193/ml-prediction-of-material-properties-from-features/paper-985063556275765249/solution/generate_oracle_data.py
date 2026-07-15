import csv
import random
import sys

random.seed(42)
N = 10000

def write_step_01():
    true = [random.gauss(0.0, 0.2) for _ in range(N)]
    noise_std = 0.088  # gives MAE ~0.07
    pred = [t + random.gauss(0, noise_std) for t in true]
    writer = csv.writer(sys.stdout)
    writer.writerow(["true_segregation_energy", "predicted_segregation_energy"])
    for t, p in zip(true, pred):
        writer.writerow([f"{t:.6f}", f"{p:.6f}"])

def write_step_02(accuracy=0.9):
    true_state = random.choices([0, 1], weights=[80, 20], k=N)
    pred_state = true_state[:]
    num_flip = int(N * (1 - accuracy))
    flip_indices = random.sample(range(N), num_flip)
    for i in flip_indices:
        pred_state[i] = 1 - pred_state[i]
    writer = csv.writer(sys.stdout)
    writer.writerow(["true_state", "predicted_probability", "predicted_state"])
    for ts, ps in zip(true_state, pred_state):
        if ts == ps:
            prob = (0.7 + random.uniform(0, 0.3)) if ts == 1 else random.uniform(0, 0.3)
        else:
            prob = random.uniform(0, 0.3) if ts == 1 else (0.7 + random.uniform(0, 0.3))
        writer.writerow([ts, f"{prob:.6f}", ps])

def write_step_03(accuracy=0.87):
    true_state = random.choices([0, 1], weights=[80, 20], k=N)
    pred_state = true_state[:]
    num_flip = int(N * (1 - accuracy))
    flip_indices = random.sample(range(N), num_flip)
    for i in flip_indices:
        pred_state[i] = 1 - pred_state[i]
    writer = csv.writer(sys.stdout)
    writer.writerow(["true_state", "predicted_probability", "predicted_state"])
    for ts, ps in zip(true_state, pred_state):
        if ts == ps:
            prob = (0.7 + random.uniform(0, 0.3)) if ts == 1 else random.uniform(0, 0.3)
        else:
            prob = random.uniform(0, 0.3) if ts == 1 else (0.7 + random.uniform(0, 0.3))
        writer.writerow([ts, f"{prob:.6f}", ps])

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "step_01":
        write_step_01()
    elif mode == "step_02":
        write_step_02()
    elif mode == "step_03":
        write_step_03()
    else:
        raise ValueError("Unknown mode")
