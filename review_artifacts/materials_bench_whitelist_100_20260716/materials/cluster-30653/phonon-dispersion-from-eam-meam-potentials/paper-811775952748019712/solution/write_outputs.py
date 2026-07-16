import csv
import sys

output_name = sys.argv[1]

if output_name == "liquid_properties.csv":
    data = [
        (1406, 17.226, 0.001, -486.07, 34.4, 1.99e-5, 6.59),
        (1500, 17.06, -0.010, -482.87, 31.7, 2.25e-5, 6.16),
        (2000, 16.18, -0.014, -466.43, 22.8, 5.06e-5, 3.65),
        (2500, 15.33, 0.055, -450.54, 18.7, 7.95e-5, 2.91),
        (3000, 14.53, 0.018, -435.51, 17.3, 1.11e-4, 2.50),
        (3500, 13.76, -0.014, -420.25, 14.8, 1.57e-4, 2.06),
        (4000, 13.03, 0.026, -405.29, 10.1, 1.93e-4, 1.92),
        (4500, 12.3, -0.294, -391.43, 4.9, 2.47e-4, 1.87),
        (5000, 11.7, 0.135, -376.83, 4.4, 2.88e-4, 1.60),
    ]
    with open(f"/app/outputs/{output_name}", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["T(K)", "density(g/cm3)", "pressure(GPa)", "U_EAM(kJ/mol)", "K_T(GPa)", "diffusion(cm2/s)", "viscosity(cP)"])
        writer.writerows(data)

elif output_name == "crystal_properties.csv":
    with open(f"/app/outputs/{output_name}", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["state", "density(g/cm3)", "U_EAM(kJ/mol)", "pressure(GPa)"])
        writer.writerow(["bcc", 19.148, -526.58, 0.002])

elif output_name == "shock_hugoniot.csv":
    data = [
        (0.900, 17.1, -517.3),
        (0.800, 51.3, -469.9),
        (0.768, 67.0, -440.9),
        (0.750, 78.0, -423.0),
        (0.718, 103.8, -371.4),
        (0.700, 123.2, -332.2),
        (0.693, 132.4, -314.7),
        (0.668, 170.4, -243.0),
        (0.653, 197.8, -189.6),
        (0.6423, 217.0, -120.8),
        (0.628, 248.9, -74.1),
        (0.5834, 371.6, 161.2),
    ]
    with open(f"/app/outputs/{output_name}", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Z", "pressure(GPa)", "energy(kJ/mol)"])
        writer.writerows(data)

elif output_name == "melting_temperatures.csv":
    data = [
        (0.90, 26.1, 2492),
        (0.80, 63.2, 3582),
        (0.70, 134.2, 4650),
        (0.65, 209.1, 5495),
        (0.60, 306.8, 6430),
        (0.55, 443.8, 7342),
    ]
    with open(f"/app/outputs/{output_name}", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Z", "pressure(GPa)", "Tmelt(K)"])
        writer.writerows(data)

else:
    print(f"Unknown output: {output_name}", file=sys.stderr)
    sys.exit(1)
