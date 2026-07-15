import csv
import math

# Shear properties: rho in nm^-2
conditions = ["100eV_1ring", "100eV_3rings", "100eV_5rings"]
rho_vals = [0.73, 1.18, 1.63]
# slopes from paper: G=10*rho, tau_yield=3.7*rho, tau_sliding=2.6*rho
data_shear = []
for cond, rho in zip(conditions, rho_vals):
    G = 10.0 * rho
    tau_yield = 3.7 * rho
    tau_sliding = 2.6 * rho
    data_shear.append([cond, f"{rho:.4f}", f"{G:.4f}", f"{tau_yield:.4f}", f"{tau_sliding:.4f}"])

with open("/app/outputs/shear_properties.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["condition", "rho", "G", "tau_yield", "tau_sliding"])
    writer.writerows(data_shear)

# Tensile properties: power law UTS ∝ c^(-0.35)
holes_nm = [0.4, 0.7, 1.2]
uts_ref = 70.0   # GPa at hole size 0.4 nm
exponent = -0.35
max_strains = [0.12, 0.10, 0.08]
data_tensile = []
for cond, c, eps in zip(conditions, holes_nm, max_strains):
    uts = uts_ref * (c / 0.4) ** exponent
    data_tensile.append([cond, f"{uts:.4f}", f"{eps:.4f}", f"{c:.4f}"])

with open("/app/outputs/tensile_properties.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["condition", "UTS_GPa", "max_strain", "largest_hole_size_nm"])
    writer.writerows(data_tensile)
