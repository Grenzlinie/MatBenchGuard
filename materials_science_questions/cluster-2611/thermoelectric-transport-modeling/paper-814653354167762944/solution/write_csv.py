import csv

output_path = "/app/outputs/computed_properties.csv"
rows = [
    ["composition", "band_gap_eV", "static_dielectric_constant", "n0_static", "Seebeck_100K_uV_K", "ZT_300K"],
    ["GaN", "2.99", "3.959", "2.0", "269", "0.80"],
    ["Ga0.75In0.25N", "2.67", "3.990", "NaN", "218", "NaN"],
    ["Ga0.5In0.5N", "2.31", "3.993", "NaN", "120", "NaN"],
    ["Ga0.25In0.75N", "1.95", "4.037", "NaN", "154", "NaN"],
]
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
