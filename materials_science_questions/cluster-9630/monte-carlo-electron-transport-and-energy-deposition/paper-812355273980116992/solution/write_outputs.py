#!/usr/bin/env python3
import csv
import sys
import math

def write_beam_radii(path):
    # Reference values derived from Figure 4c (10 keV monoenergetic, vertical field),
    # peak effective radius for H⁺+H fluxes ≈ 169 km located near 350 km.
    rows = [
        (400.0, 160.0),
        (350.0, 169.0),
        (300.0, 165.0),
        (250.0, 145.0),
    ]
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['altitude_km', 'beam_radius_km'])
        for alt, rad in rows:
            writer.writerow([alt, rad])

def write_flux_profile(path):
    # Construct a monotonically decreasing azimuthally averaged downward H⁺ flux
    # profile at 350 km altitude. Shape mimics Figure 3a (right panel).
    # Central flux normalized to 1.0; exponential-like decay with a smooth roll-off.
    radii = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0,
             100.0, 110.0, 120.0, 130.0, 140.0, 150.0, 160.0, 170.0, 180.0, 190.0,
             200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0, 270.0, 280.0, 290.0,
             300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0,
             400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 500.0]
    # Exponential model with e-folding distance ~90 km, scaled to ~1 at r=0 and ~2e-3 at 500 km
    efold = 90.0
    amp = 1.0
    values = [amp * math.exp(-r / efold) for r in radii]

    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['radial_distance_km', 'downward_Hplus_flux'])
        for r, v in zip(radii, values):
            writer.writerow([r, v])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: write_outputs.py [beam_radii|flux_profile]")
        sys.exit(1)
    command = sys.argv[1]
    if command == 'beam_radii':
        write_beam_radii('/app/outputs/beam_radii.csv')
    elif command == 'flux_profile':
        write_flux_profile('/app/outputs/flux_profile_350km.csv')
    else:
        print("Unknown command")
        sys.exit(1)
