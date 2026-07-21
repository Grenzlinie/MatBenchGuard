import json
from model import compute_G

# Material constants for a 2-μm ZnO film
v_s = 6000.0              # sound velocity (m/s)
K2  = 0.16                # electromechanical coupling constant

# Compute efficiency for the two drift conditions
G_zero       = compute_G(0.0)                # v_D = 0
G_supersonic = compute_G(1.5 * v_s)          # v_D = 1.5 v_s

result = {"G_zero": G_zero, "G_supersonic": G_supersonic}
with open("/app/outputs/step_01_efficiency.json", "w") as f:
    json.dump(result, f, indent=2)
print(f"G_zero       = {G_zero:.6f}")
print(f"G_supersonic = {G_supersonic:.6f}")