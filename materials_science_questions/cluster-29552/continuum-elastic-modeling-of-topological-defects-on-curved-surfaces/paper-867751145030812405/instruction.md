# Polynomial Approximation of Disclination Profiles and Free Energy Comparison in Landau–de Gennes Theory

## Problem background
Disclination lines are topological defects in nematic liquid crystals. In the director formalism they possess a singular core, but the Landau-de Gennes theory allows for a smooth core in which biaxiality is induced. This work analyses a rectilinear n = 1/2 disclination line with equal elastic constants (L₂ = 0) and constructs an approximate analytic description of the transverse profile functions R(s) and S(s). The goal is to compare the free energy per unit length of the smooth disclination to that of a singular-core disclination, and thereby determine – as a function of the dimensionless material parameter β – which configuration is energetically favoured.

## Approach
The description is based on the Landau-de Gennes effective theory for nematic liquid crystals. An axially symmetric ansatz for the order parameter tensor Q is used, reducing the Euler-Lagrange equations to a pair of coupled ODEs for the profile functions R(s) and S(s) (with s a scaled radial coordinate).

A **polynomial-matching approximation** is constructed: small-s polynomial expansions are matched at two radii s₁ and s₂ to the leading large-s asymptotic forms, enforcing C¹ continuity. This yields algebraic relations that determine the matching parameters (r₁, s₁, w₀, s₂) and a cubic equation for the central value w₀ = S(0). The resulting piecewise C¹ functions R(s) and S(s) provide a smooth disclination profile valid for all s.

Using this approximate profile, the **free energy per unit length** of the smooth disclination inside a cylinder of large radius L is computed by numerical integration of the Landau-de Gennes free energy density. The corresponding **singular-core** free energy is modelled with a core of radius R_c = 3 ξ₀ / (2 √(1+β)) (zero energy inside the core). The difference ΔF(β) = F_smooth − F_singular (in dimensionless units) quantifies the energetic competition between the two configurations.

## Reproduction target
Implement the polynomial-matching approximation and carry out the following computations:

1. **Core value w₀** – evaluate S(s=0) for two representative values of the parameter β (0.1 and 1.0). Write the results to `/app/outputs/w0_values.json` as a JSON object with keys `beta_0.1` and `beta_1.0`.

2. **Free energy difference ΔF(β)** – for β ranging from 0.01 to 0.20 in steps of 0.01, compute the dimensionless free energy difference per unit length (smooth minus singular) using the polynomial profile, an integration cutoff of L = 35, and the singular-core model described above. Output the resulting table to `/app/outputs/free_energy_difference.csv` with columns `beta` and `delta_F`.

These two artifacts together capture the key quantities needed to analyse the smooth-to-singular transition.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Construct polynomial-matching approximation
- Role: process
- Action: Implement the polynomial-matching approximation for the disclination profile functions R(s) and S(s) in the Landau–de Gennes theory (equal elastic constants L2=0). Derive small-s and large-s expansions, impose C^1 matching conditions at radii s1 and s2, solve the algebraic equations to obtain parameters r1, s1, w0 (via the cubic equation) and s2. Assemble piecewise C^1 functions R(s) and S(s) valid for all s≥0 as functions of the parameter β.
- Evidence: none

### Step 2: Compute core value w0
- Role: scored
- Action: Using the polynomial-matching approximation, evaluate S(s=0)=w0 for β=0.1 and β=1.0. Write a JSON file containing these two values.
- Output file: `/app/outputs/w0_values.json`
- Format: json
- Contract: JSON object with keys 'beta_0.1' (float) and 'beta_1.0' (float).
- Scoring: scored by hidden verifier

### Step 3: Compute free energy difference ΔF(β)
- Role: scored (load-bearing)
- Action: For each β from 0.01 to 0.2 in steps of 0.01: (i) integrate the Landau–de Gennes free energy density (using the approximate R(s), S(s)) over s from 0 to L=35 to obtain the smooth free energy per unit length F_b(β); (ii) compute the singular-core free energy F_c(β) using the model core radius R_c = 3ξ0/(2√(1+β)) and zero energy inside; (iii) output the difference ΔF = (F_b − F_c) in units of (9π/4) a η0^2 ξ0^2. Write a CSV file with columns 'beta' and 'delta_F'.
- Output file: `/app/outputs/free_energy_difference.csv`
- Format: csv
- Contract: CSV file with two columns: 'beta' (float) and 'delta_F' (float, dimensionless units).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/w0_values.json`
- `/app/outputs/free_energy_difference.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### w0_values.json
- path: `/app/outputs/w0_values.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Central value w0 of the smooth disclination profile S(s) at s=0 for β=0.1 and β=1.0, computed from the polynomial-matching approximation.
- schema:
  - `type`: object
  - `required`:
    - `beta_0.1`: float
    - `beta_1.0`: float

### free_energy_difference.csv
- path: `/app/outputs/free_energy_difference.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Free energy difference per unit length ΔF(β) = F_smooth - F_singular (in units of (9π/4) a η0^2 ξ0^2) for β from 0.01 to 0.2 in steps of 0.01. The checker locates the β where ΔF crosses zero and validates the sign trend.
- schema:
  - `type`: table
  - `required_columns`: `beta`, `delta_F`
  - `units`:
    - `delta_F`: dimensionless

Notes: The w0 values are compared to the paper's approximate values with absolute tolerance 0.001. For the free energy CSV, the checker interpolates the zero crossing to obtain the critical β and compares to the paper's reported value ~0.12 (tolerance 0.015); it also verifies that ΔF > 0 at low β (0.01) and ΔF < 0 at high β (0.2).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "w0_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "beta_0.1": "float",
          "beta_1.0": "float"
        }
      },
      "description": "Central value w0 of the smooth disclination profile S(s) at s=0 for β=0.1 and β=1.0, computed from the polynomial-matching approximation."
    },
    {
      "file": "free_energy_difference.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "beta",
          "delta_F"
        ],
        "units": {
          "delta_F": "dimensionless"
        }
      },
      "description": "Free energy difference per unit length ΔF(β) = F_smooth - F_singular (in units of (9π/4) a η0^2 ξ0^2) for β from 0.01 to 0.2 in steps of 0.01. The checker locates the β where ΔF crosses zero and validates the sign trend."
    }
  ],
  "notes": "The w0 values are compared to the paper's approximate values with absolute tolerance 0.001. For the free energy CSV, the checker interpolates the zero crossing to obtain the critical β and compares to the paper's reported value ~0.12 (tolerance 0.015); it also verifies that ΔF > 0 at low β (0.01) and ΔF < 0 at high β (0.2)."
}
```

## How you are scored
A hidden verifier reads your submitted artifacts and scores each one independently:

- **w0_values.json** – the verifier compares your computed w₀ values to expected values within a tolerance. Getting these close to the exact result demonstrates that the polynomial-matching approximation has been implemented correctly.

- **free_energy_difference.csv** – the verifier checks that the ΔF trend is physically plausible: ΔF > 0 at small β, ΔF < 0 at large β, and that ΔF crosses zero at some intermediate β. It also locates the crossing point and compares it to a reference value.

Both artifacts contribute to a final reward in [0,1]; you must produce accurate, well-formatted outputs. No credit is given for simply reporting numbers — the verifier independently assesses the correctness of your results.
