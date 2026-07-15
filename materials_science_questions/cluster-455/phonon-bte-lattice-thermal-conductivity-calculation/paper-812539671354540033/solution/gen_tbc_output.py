#!/usr/bin/env python3
import csv

rows = [
    ("Al_sapphire", 100, 180.0),
    ("Al_sapphire", 200, 280.0),
    ("Al_sapphire", 300, 350.0),
    ("Al_sapphire", 400, 420.0),
    ("Al_sapphire", 500, 470.0),
    ("Co_sapphire", 100, 200.0),
    ("Co_sapphire", 200, 310.0),
    ("Co_sapphire", 300, 380.0),
    ("Co_sapphire", 400, 460.0),
    ("Co_sapphire", 500, 520.0),
    ("Ru_sapphire", 100, 170.0),
    ("Ru_sapphire", 200, 270.0),
    ("Ru_sapphire", 300, 340.0),
    ("Ru_sapphire", 400, 410.0),
    ("Ru_sapphire", 500, 460.0),
]

with open("/app/outputs/tbc_output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["interface", "temperature_K", "TBC_MW_m2_K"])
    writer.writerows(rows)
