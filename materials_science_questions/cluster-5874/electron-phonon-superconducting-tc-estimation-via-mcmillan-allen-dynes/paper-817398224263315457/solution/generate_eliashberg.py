import json, math, sys

OUTPUT = sys.argv[1]

# Frequency grid 0-80 meV, step 0.5 meV
freq = [f/2.0 for f in range(0, 161)]  # 0.0,0.5,...,80.0

# Lorentzian helper
def lorentz(x, x0, gamma, amp):
    return amp * gamma**2 / ((x - x0)**2 + gamma**2)

# α²F as superposition of low‑ and high‑frequency contributions
a2F_raw = []
for f in freq:
    if f == 0.0:
        a2F_raw.append(0.0)
        continue
    val = 0.0
    # low‑f peak around 10 meV
    val += lorentz(f, 10.0, 3.0, 2.2)
    val += lorentz(f, 13.0, 3.5, 1.5)
    # high‑f broad distribution
    val += lorentz(f, 50.0, 12.0, 0.5)
    val += lorentz(f, 65.0, 10.0, 0.3)
    a2F_raw.append(val)
a2F_raw[0] = 0.0

# Compute cumulative λ = 2 ∫ α²F(ω)/ω dω via trapezoidal rule
cum_raw = [0.0]
for i in range(1, len(freq)):
    f_i = freq[i]
    f_prev = freq[i-1]
    if f_prev == 0.0:
        # 0‑contribution from the first step
        cum_raw.append(0.0)
        continue
    a_prev = a2F_raw[i-1] / f_prev
    a_i    = a2F_raw[i]   / f_i
    integ  = (a_prev + a_i) * (f_i - f_prev)
    cum_raw.append(cum_raw[-1] + integ)

total_raw = cum_raw[-1]
scale = 1.47 / total_raw if total_raw > 0 else 1.0

a2F = [a * scale for a in a2F_raw]
cum_lambda = [c * scale for c in cum_raw]

data = []
for f, a, c in zip(freq, a2F, cum_lambda):
    data.append({
        "frequency": round(f, 2),
        "a2F": round(a, 6),
        "cumulative_lambda": round(c, 6)
    })

with open(OUTPUT, 'w') as fh:
    json.dump(data, fh, indent=2)

print(f"Generated {len(data)} points, final λ = {cum_lambda[-1]:.4f}")
