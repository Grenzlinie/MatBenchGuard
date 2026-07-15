import os, json, math

T = 258.15
p = 900.0
chi = 0.1
T0 = 273.15
p0 = 1013.25
R = 8.314
M = 0.018
S = 1.20

Dp_cm2 = 0.211 * (T/T0)**1.94 * (p0/p)
Dp = Dp_cm2 * 1e-4
kp = chi * math.sqrt(R * T / (2*math.pi*M))

lambda_p = (Dp / kp) * 1e6
Rc = 4 * lambda_p / (S - 1)
lambda_c = 2*math.pi * math.sqrt(Rc * lambda_p / (S - 1))

out = {'lambda_c': lambda_c}
out_path = os.path.join(os.environ['OUTDIR'], 'step_05_theoretical_critical_spacing.json')
with open(out_path, 'w') as f:
    json.dump(out, f, indent=2)
