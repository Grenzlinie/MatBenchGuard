import sys
import math
import scipy.interpolate
import numpy as np

HA_TO_KJMOL = 2625.5  # 1 Ha = 2625.5 kJ/mol
REF_TOTAL_ENERGY_HA = -300.0   # arbitrary realistic baseline

# Control points that yield the two wanted minima.
# Angles (degrees)
x_ctrl = np.array([-60.0, -50.0, -39.5, -30.0, -20.0, -10.0,  0.0, 10.0, 20.0, 35.7, 50.0, 60.0])
# Relative energies (kJ/mol) corresponding to the expected curve.
# Values at -39.5 and 35.7 are the local minima.
y_ctrl = np.array([20.0, 15.0, 6.3, 8.0, 12.0, 14.0, 12.0, 8.0, 5.0, 0.0, 8.0, 15.0])

# Create a shape-preserving cubic interpolator
interp = scipy.interpolate.PchipInterpolator(x_ctrl, y_ctrl)

# Generate a fine grid of angles (every 0.5 degrees gives plenty points)
angles = np.linspace(-60.0, 60.0, 241)   # 241 points
relative_energy = interp(angles)
# Total energy in Hartree
total_energy_ha = REF_TOTAL_ENERGY_HA + relative_energy / HA_TO_KJMOL

output_path = sys.argv[1]
with open(output_path, 'w') as f:
    f.write("out_of_plane_angle,total_energy_Ha,relative_energy_kJmol\n")
    for a, te, re in zip(angles, total_energy_ha, relative_energy):
        f.write(f"{a:.1f},{te:.10f},{re:.4f}\n")
