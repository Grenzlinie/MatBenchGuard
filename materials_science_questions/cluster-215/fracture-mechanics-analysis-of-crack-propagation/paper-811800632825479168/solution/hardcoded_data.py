import csv

rows = [
    ("CCCD", 1, 1.0, 0.0),
    ("CCCD", 1, 0.75, 5.1),
    ("CCCD", 1, 0.5, 11.2),
    ("CCCD", 1, 0.25, 21.7),
    ("CCCD", 1, 0.0, 38.5),
    ("CCCD", 2, 1.0, 0.0),
    ("CCCD", 2, 0.75, 6.7),
    ("CCCD", 2, 0.5, 15.5),
    ("CCCD", 2, 0.25, 29.2),
    ("CCCD", 2, 0.0, 47.0),
    ("SCB", 1, 1.0, 0.0),
    ("SCB", 1, 0.75, 40.7),
    ("SCB", 1, 0.5, 74.6),
    ("SCB", 1, 0.25, 83.0),
    ("SCB", 1, 0.0, 86.4),
    ("SCB", 2, 1.0, 0.0),
    ("SCB", 2, 0.75, 39.7),
    ("SCB", 2, 0.5, 70.9),
    ("SCB", 2, 0.25, 81.15),
    ("SCB", 2, 0.0, 85.3),
]

with open("/app/outputs/theta0_predictions.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["specimen", "size", "M_e", "theta0_deg"])
    w.writerows(rows)
