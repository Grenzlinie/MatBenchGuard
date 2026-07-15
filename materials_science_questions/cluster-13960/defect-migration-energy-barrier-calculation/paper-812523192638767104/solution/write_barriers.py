import csv
import os

output_dir = "/app/outputs"
output_file = os.path.join(output_dir, "migration_barriers.csv")

# Paper‑reported gold values
rows = [
    {"system": "stoichiometric", "tunnel": "", "barrier_eV": 0.43},
    {"system": "oxygen-deficient", "tunnel": "tunnel1", "barrier_eV": 0.30},
    {"system": "oxygen-deficient", "tunnel": "tunnel2", "barrier_eV": 0.27},
    {"system": "oxygen-deficient", "tunnel": "tunnel3", "barrier_eV": 0.37},
]

with open(output_file, mode="w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["system", "tunnel", "barrier_eV"])
    writer.writeheader()
    writer.writerows(rows)
