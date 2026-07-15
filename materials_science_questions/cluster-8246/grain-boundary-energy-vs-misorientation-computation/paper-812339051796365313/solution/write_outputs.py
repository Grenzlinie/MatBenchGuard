#!/usr/bin/env python3
"""Write standard-answer CSV artifacts for the Möbius PBC validation task."""
import argparse
import csv
import math


def write_bulk_properties(path):
    header = [
        "simulation_id", "pbc_type", "ensemble",
        "average_energy_eVperatom", "average_temperature_K",
        "average_pressure_bar", "rmsad_Angstrom"
    ]
    rows = [
        # (sim_id, pbc, ensemble, energy, temp, pressure, rmsad)
        ("sim1", "mobius", "NVE", -4.60, 1000.5, 1.2, 0.152),
        ("sim2", "bvk",    "NVE", -4.60, 1000.5, 1.2, 0.152),
        ("sim3", "mobius", "NVT", -4.62, 1000.0, 0.9, 0.148),
        ("sim4", "bvk",    "NVT", -4.62, 1000.0, 0.9, 0.148),
        ("sim5", "mobius", "NVE", -4.61, 1000.2, 1.1, 0.150),
        ("sim6", "bvk",    "NVE", -4.61, 1000.2, 1.1, 0.150),
        ("sim7", "mobius", "NVT", -4.63, 1000.1, 1.0, 0.149),
        ("sim8", "bvk",    "NVT", -4.63, 1000.1, 1.0, 0.149),
    ]
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def write_rmsad_slices(path):
    header = [
        "slice_position_Angstrom", "mobius_rmsad_Angstrom", "bvk_rmsad_Angstrom"
    ]
    # approximate box length 21.72 Å -> 5 Å slices
    # centers: 2.5, 7.5, 12.5, 17.5, 20.86
    slices = [
        (2.5, 0.150, 0.150),
        (7.5, 0.152, 0.152),
        (12.5, 0.148, 0.148),
        (17.5, 0.153, 0.153),
        (20.86, 0.151, 0.151),
    ]
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(slices)


def write_gb_energies(path):
    header = [
        "structure", "pbc_type",
        "minimized_energy_eVperatom", "interfacial_energy_mJperm2"
    ]
    rows = [
        ("Sigma11A", "mobius", -4.63, 618),
        ("Sigma11A", "bvk",    -4.63, 0),
        ("Sigma11B", "mobius", -4.63, 635),
        ("Sigma11B", "bvk",    -4.63, 0),
    ]
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True,
                        choices=["bulk_properties.csv", "rmsad_slices.csv", "gb_energies.csv"])
    parser.add_argument("--out", required=True, help="Output file path")
    args = parser.parse_args()

    if args.file == "bulk_properties.csv":
        write_bulk_properties(args.out)
    elif args.file == "rmsad_slices.csv":
        write_rmsad_slices(args.out)
    elif args.file == "gb_energies.csv":
        write_gb_energies(args.out)


if __name__ == "__main__":
    main()
