# MSCB Analytical Model: Stiffness, Strength, and Fracture Energy

## Problem background
Seashell nacre (mother‑of‑pearl) is a natural biocomposite composed of brittle aragonite platelets (hard phase) bonded by thin organic protein layers (soft phase). It exhibits exceptional toughness while maintaining high stiffness and strength, which is attributed to its hierarchical “brick‑and‑mortar” microstructure and the arch‑shaped macroscopic geometry of the shell. This task investigates an analytical model of an arch‑shaped multilayer curved beam under three‑point bending to understand how the arch shape and the layered internal structure jointly determine the effective stiffness, bending strength, and fracture energy, and to extract design principles for bioinspired ceramics.

## Approach
The model compares a homogeneous pure aragonite straight beam (PASB) and an arch‑shaped multilayer curved beam (MSCB) under three‑point bending. The MSCB has a parabolic central axis: y = 4δ x (L - x) / L², and its cross‑section consists of many alternating hard layers (aragonite) and soft layers (protein). The following formulas define the quantities that must be computed.

### Derived geometric parameters
- h2 = h2_over_H * H  (soft layer thickness)
- h1 = h2 * V_f / (1 - V_f)   (hard layer thickness, valid for V_f < 1)
- l = rho * h1               (hard layer length)

### Effective modulus ratio (tension‑shear chain model)
E_ratio = E / E1 = ((1 - Phi) * Phi * rho² * V_f²) / ((1 - V_f) * lambda + (1 - Phi) * Phi * rho² * V_f)
where lambda = E1 / G2 (ratio of hard‑layer elastic modulus to soft‑layer shear modulus).

### Cross‑section properties (MSCB)
I_z = (B * H / 12) * ((H - h2)*(H - 2*h2)*V_f + (3*H - 2*h2)*h2)
S_zmax = (B / 8) * (4*H*h2 - 4*h2² + (H - h2)² * V_f - (2/V_f)*(H - h2)*h2)

### Reference homogeneous beam (PASB)
I_z0 = B * H³ / 12
S_z0 = B * H² / 8

### Bending stiffness ratio
kappa = E_ratio * I_z / I_z0

### Stress at beam centre (x = L/2, φ = 0)
Bending moment at centre M = P L / 4, shear force Q = P/2, axial force N = 0.
sigma_max = M * H / (2 I_z) = P * H * L / (8 I_z)
tau_max = Q * S_zmax / (I_z * B) = P * S_zmax / (2 I_z * B)

### Critical loads and bending strength ratio
For PASB, brittle fracture occurs when sigma_max = sigma_b:
P0 = 8 * I_z0 * sigma_b / (H * L)

For MSCB, two failure modes:
- Hard‑layer fracture: P1 = 8 * I_z * sigma_b / (H * L)
- Interfacial shear failure: P2 = 2 * I_z * tau_s * B / S_zmax
Critical load: P_crit = min(P1, P2)
Bending strength ratio: chi = P_crit / P0

### Plastic region length
Consider the condition for interfacial yielding. Define
R = (16 * S_zmax² * sigma_b²) / (H² * L² * B² * tau_s²) - 1
If R >= 0:
    L_c = L - (L² / (4 * delta)) * sqrt(R)
Else:
    L_c = 0   (no plastic region forms before brittle fracture)

### Fracture energy
For PASB:
W_PASB = gamma * H * B

For MSCB (with crack deflection in the plastic region):
m = L_c / l   (number of zigzag cracks, using l > 0)
W_MSCB = m * (1/2) * Phi * rho * V_f * H * (1/3) * B * gamma
        = (m / 6) * Phi * rho * V_f * gamma * H * B

### Parameter grid
The following parameter values are fixed for all evaluations:
L = 0.01 m, B = 0.001 m, H = 0.002 m, sigma_b = 100e6 Pa, gamma = 1.0 J/m².

The remaining parameters are varied and all combinations (Cartesian product) must be evaluated:

- V_f : [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
- rho : [5, 10, 15, 20]
- Phi : [0.2, 0.4, 0.5, 0.6, 0.8]
- lambda : [10, 50, 100, 200, 500]
- h2_over_H : [0.001, 0.005, 0.01, 0.02, 0.05]
- delta : [0.0005, 0.001, 0.0015, 0.002]
- tau_s : [5e6, 10e6, 20e6, 30e6, 50e6]

## Reproduction target
Implement the analytical model described above. Using the prescribed parameter grid (ranges and fixed values for arch height, beam dimensions, volume fraction, aspect ratio, overlap ratio, modulus ratio, hard‑layer strength, interfacial shear strength, and surface energy), compute for each parameter combination the effective modulus ratio, cross‑sectional properties, bending stiffness ratio, maximum stresses, critical loads, bending strength ratio, plastic‑region length, and fracture energies. Write all input parameters and computed quantities to a CSV file ``/app/outputs/mscb_results.csv`` with the columns and units specified in the Output Contract. The file must contain one row per parameter combination; the order of rows does not affect scoring.

## Assets

- Python 3.x with numpy and pandas: python3, numpy, pandas

## Workflow steps

### Step 1: Compute MSCB quantities and write results CSV
- Role: scored (load-bearing)
- Action: Using the formulas and parameter grid provided in the Approach section, compute for every parameter combination the quantities E_ratio, I_z, S_zmax, kappa, sigma_max, tau_max, P1, P2, chi, L_c, W_PASB, and W_MSCB. Generate one row per combination in the output CSV file, with all input parameters and computed outputs in SI units as specified.
- Output file: `/app/outputs/mscb_results.csv`
- Format: csv
- Contract: CSV with columns: V_f (volume fraction), rho (aspect ratio), Phi (overlap ratio), lambda (modulus ratio E1/G2), h2_over_H (soft layer thickness fraction), delta (arch height), L (span), B (width), H (height), sigma_b (hard layer strength), tau_s (interfacial shear strength), gamma (surface energy), E_ratio, I_z, S_zmax, kappa, sigma_max, tau_max, P1, P2, chi, L_c, W_PASB, W_MSCB. All length-related quantities in m, forces in N, stresses in Pa, energy in J, and dimensionless quantities as raw numbers.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mscb_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mscb_results.csv
- path: `/app/outputs/mscb_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing all input parameters and the corresponding computed effective modulus ratio, cross‑sectional properties, bending stiffness ratio, stresses, critical loads, bending strength ratio, plastic zone length, and fracture energies. The checker will independently recompute every computed column for the same parameter grid and compare the agent's values to its own recomputed references within tolerance, and will also verify monotonic increasing trends for κ, χ, and W_MSCB with respect to V_f, ρ, Φ, and λ.
- schema:
  - `type`: table
  - `required_columns`: `V_f`, `rho`, `Phi`, `lambda`, `h2_over_H`, `delta`, `L`, `B`, `H`, `sigma_b`, `tau_s`, `gamma`, `E_ratio`, `I_z`, `S_zmax`, `kappa`, `sigma_max`, `tau_max`, `P1`, `P2`, `chi`, `L_c`, `W_PASB`, `W_MSCB`
  - `units`:
    - `V_f`: dimensionless
    - `rho`: dimensionless
    - `Phi`: dimensionless
    - `lambda`: dimensionless
    - `h2_over_H`: dimensionless
    - `delta`: m
    - `L`: m
    - `B`: m
    - `H`: m
    - `sigma_b`: Pa
    - `tau_s`: Pa
    - `gamma`: J/m^2
    - `E_ratio`: dimensionless
    - `I_z`: m^4
    - `S_zmax`: m^3
    - `kappa`: dimensionless
    - `sigma_max`: Pa
    - `tau_max`: Pa
    - `P1`: N
    - `P2`: N
    - `chi`: dimensionless
    - `L_c`: m
    - `W_PASB`: J
    - `W_MSCB`: J

Notes: The hidden reference values are recomputed by the checker using the same analytical formulas. The instruction provides the exact parameter grid (ranges and fixed values) so both agent and checker evaluate identical input points.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mscb_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "V_f",
          "rho",
          "Phi",
          "lambda",
          "h2_over_H",
          "delta",
          "L",
          "B",
          "H",
          "sigma_b",
          "tau_s",
          "gamma",
          "E_ratio",
          "I_z",
          "S_zmax",
          "kappa",
          "sigma_max",
          "tau_max",
          "P1",
          "P2",
          "chi",
          "L_c",
          "W_PASB",
          "W_MSCB"
        ],
        "units": {
          "V_f": "dimensionless",
          "rho": "dimensionless",
          "Phi": "dimensionless",
          "lambda": "dimensionless",
          "h2_over_H": "dimensionless",
          "delta": "m",
          "L": "m",
          "B": "m",
          "H": "m",
          "sigma_b": "Pa",
          "tau_s": "Pa",
          "gamma": "J/m^2",
          "E_ratio": "dimensionless",
          "I_z": "m^4",
          "S_zmax": "m^3",
          "kappa": "dimensionless",
          "sigma_max": "Pa",
          "tau_max": "Pa",
          "P1": "N",
          "P2": "N",
          "chi": "dimensionless",
          "L_c": "m",
          "W_PASB": "J",
          "W_MSCB": "J"
        }
      },
      "description": "CSV file containing all input parameters and the corresponding computed effective modulus ratio, cross‑sectional properties, bending stiffness ratio, stresses, critical loads, bending strength ratio, plastic zone length, and fracture energies. The checker will independently recompute every computed column for the same parameter grid and compare the agent's values to its own recomputed references within tolerance, and will also verify monotonic increasing trends for κ, χ, and W_MSCB with respect to V_f, ρ, Φ, and λ."
    }
  ],
  "notes": "The hidden reference values are recomputed by the checker using the same analytical formulas. The instruction provides the exact parameter grid (ranges and fixed values) so both agent and checker evaluate identical input points."
}
```

## How you are scored
After you submit, a hidden verifier will independently re‑implement the same analytical model using the same parameter grid and will compute the reference values for every computed column. Your submitted CSV will be compared to this hidden reference. Numeric columns are scored by relative (or absolute) error within hidden tolerances. The verifier will also examine the internal consistency of your results, such as whether the computed quantities exhibit the expected mathematical relationships (e.g., monotonic behaviour) with respect to the key parameters. The final score (a float between 0 and 1) is a weighted combination of numeric accuracy and consistency. Exact weights and tolerances are not disclosed.
