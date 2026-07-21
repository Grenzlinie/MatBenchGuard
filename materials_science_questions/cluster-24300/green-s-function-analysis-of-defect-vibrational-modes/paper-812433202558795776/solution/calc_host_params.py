import json, math

r0_cm = 2.282e-8  # cm
k = 1.441e11      # dyn/cm^2
e_esu = 4.803e-10 # esu
alpha = 1.7627

K = 1.0 / k  # bulk modulus
e2 = e_esu * e_esu
term1 = (3.0 * r0_cm * K) * (8.0 * r0_cm**3 / e2)
A = term1 + (2.0 * alpha) / (3.0 * math.sqrt(3.0))
B = -alpha / (3.0 * math.sqrt(3.0))

output = {"A": A, "B": B}
with open("/app/outputs/host_params.json", "w") as f:
    json.dump(output, f)
