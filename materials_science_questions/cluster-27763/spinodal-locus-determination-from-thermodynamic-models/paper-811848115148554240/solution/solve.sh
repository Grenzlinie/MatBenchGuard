#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: elementary_coefficients.json ===
cat > /app/outputs/elementary_coefficients.json <<'FFEOF'
{
  "0.7": {
    "B20": {"value": -17.71, "error": 0.05},
    "B11": {"value": -11.77, "error": 0.05},
    "B02": {"value": -17.71, "error": 0.05},
    "B30": {"value": 11.10, "error": 0.1},
    "B21": {"value": 7.90, "error": 0.1},
    "B12": {"value": 7.90, "error": 0.1},
    "B03": {"value": 11.10, "error": 0.1},
    "B40": {"value": -18.66, "error": 0.3},
    "B31": {"value": -12.54, "error": 0.3},
    "B22": {"value": -8.20, "error": 0.3},
    "B13": {"value": -12.54, "error": 0.3},
    "B04": {"value": -18.66, "error": 0.3}
  },
  "1.0": {
    "B20": {"value": -8.04, "error": 0.03},
    "B11": {"value": -3.12, "error": 0.03},
    "B02": {"value": -8.04, "error": 0.03},
    "B30": {"value": 5.06, "error": 0.08},
    "B21": {"value": 2.56, "error": 0.08},
    "B12": {"value": 2.56, "error": 0.08},
    "B03": {"value": 5.06, "error": 0.08},
    "B40": {"value": -3.27, "error": 0.2},
    "B31": {"value": -1.58, "error": 0.2},
    "B22": {"value": -0.57, "error": 0.2},
    "B13": {"value": -1.58, "error": 0.2},
    "B04": {"value": -3.27, "error": 0.2}
  },
  "1.15": {
    "B20": {"value": -5.62, "error": 0.03},
    "B11": {"value": -1.06, "error": 0.03},
    "B02": {"value": -5.62, "error": 0.03},
    "B30": {"value": 3.18, "error": 0.06},
    "B21": {"value": 1.19, "error": 0.06},
    "B12": {"value": 1.19, "error": 0.06},
    "B03": {"value": 3.18, "error": 0.06},
    "B40": {"value": -1.53, "error": 0.15},
    "B31": {"value": -0.54, "error": 0.15},
    "B22": {"value": -0.071, "error": 0.15},
    "B13": {"value": -0.54, "error": 0.15},
    "B04": {"value": -1.53, "error": 0.15}
  },
  "1.31": {
    "B20": {"value": -3.76, "error": 0.02},
    "B11": {"value": 0.41, "error": 0.02},
    "B02": {"value": -3.76, "error": 0.02},
    "B30": {"value": 1.76, "error": 0.05},
    "B21": {"value": 0.39, "error": 0.05},
    "B12": {"value": 0.39, "error": 0.05},
    "B03": {"value": 1.76, "error": 0.05},
    "B40": {"value": -0.52, "error": 0.1},
    "B31": {"value": -0.082, "error": 0.1},
    "B22": {"value": 0.095, "error": 0.1},
    "B13": {"value": -0.082, "error": 0.1},
    "B04": {"value": -0.52, "error": 0.1}
  }
}
FFEOF

# === solve block: spinodal_T1.15.csv ===
python3 -c '
import json, math

coeff = json.load(open("/app/outputs/elementary_coefficients.json"))
T = 1.15
B = coeff["1.15"]
B20 = B["B20"]["value"]; B11 = B["B11"]["value"]; B02 = B["B02"]["value"]
B30 = B["B30"]["value"]; B21 = B["B21"]["value"]; B12 = B["B12"]["value"]; B03 = B["B03"]["value"]
B40 = B["B40"]["value"]; B31 = B["B31"]["value"]; B22 = B["B22"]["value"]; B13 = B["B13"]["value"]; B04 = B["B04"]["value"]

def B2(y):
    return y*y*B20 + 2*y*(1-y)*B11 + (1-y)*(1-y)*B02

def B3(y):
    return y**3*B30 + 3*y*y*(1-y)*B21 + 3*y*(1-y)**2*B12 + (1-y)**3*B03

def B4(y):
    return y**4*B40 + 4*y**3*(1-y)*B31 + 6*y*y*(1-y)**2*B22 + 4*y*(1-y)**3*B13 + (1-y)**4*B04

def P(rho, y):
    return rho * T * (1 + B2(y)*rho + B3(y)*rho*rho + B4(y)*rho**3)

def mu1(rho, y):
    # beta mu1 up to B4 (Eq.5)
    return math.log(y*rho) + 2*rho*(y*B20 + (1-y)*B11) \
           + 1.5*rho*rho*(y*y*B30 + 2*y*(1-y)*B21 + (1-y)*(1-y)*B12) \
           + (4/3)*rho**3*(y**3*B40 + 3*y*y*(1-y)*B31 + 3*y*(1-y)**2*B22 + (1-y)**3*B13)

def dP_drho(rho, y, h=1e-6):
    return (P(rho+h, y) - P(rho-h, y)) / (2*h)

def dP_dy(rho, y, h=1e-6):
    return (P(rho, y+h) - P(rho, y-h)) / (2*h)

def dmu1_dy(rho, y, h=1e-6):
    return (mu1(rho, y+h) - mu1(rho, y-h)) / (2*h)

def stability(rho, y):
    # Eq.4: (dP/drho) * (dmu1/dy - (1/rho)*dP/dy) - ((1-y)/rho**2) * (dP/dy)**2
    return dP_drho(rho, y) * (dmu1_dy(rho, y) - dP_dy(rho, y)/rho) \
           - (1-y)/(rho*rho) * dP_dy(rho, y)**2

# Generate spinodal points as a function of y
points = []
for y in [i/200 for i in range(1, 200)]:  # avoid exactly 0/1
    # find rho by bisection
    rho_low = 0.001
    rho_high = 0.5
    if stability(rho_low, y) * stability(rho_high, y) > 0:
        # no root in this interval; skip
        continue
    for _ in range(50):
        rho_mid = (rho_low + rho_high) / 2
        fmid = stability(rho_mid, y)
        if fmid == 0:
            break
        if stability(rho_low, y) * fmid < 0:
            rho_high = rho_mid
        else:
            rho_low = rho_mid
    rho_root = (rho_low + rho_high) / 2
    if 0 < rho_root < 0.5:
        points.append((round(rho_root, 6), round(y, 6)))

# Ensure symmetry by taking only up to y=0.5 and mirroring
half_points = [(r, y) for r,y in points if y <= 0.5]
full_points = half_points + [(r, 1-y) for r,y in reversed(half_points[:-1])]

with open("/app/outputs/spinodal_T1.15.csv", "w") as f:
    f.write("rho,y1\n")
    for r, y in full_points:
        f.write(f"{r},{y}\n")
'
