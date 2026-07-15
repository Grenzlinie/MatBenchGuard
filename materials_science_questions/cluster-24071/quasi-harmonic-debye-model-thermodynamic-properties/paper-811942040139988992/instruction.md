# Quasi-harmonic Debye model thermodynamic properties

## Problem background
Accurate interatomic potentials are crucial for predicting thermodynamic properties of metals. This task tests a polynomial pair potential derived from experimental phonon spectra against calorimetric data for the noble metals Cu, Ag, and Au. The target quantities — Debye temperature at 0 K, Grüneisen parameter, volume thermal expansion coefficient, and molar heat at constant volume — provide a demanding test of the potential's ability to describe anharmonic effects over a range of low temperatures. The goal is to compute these properties from first principles and compare them to known experimental trends, thereby evaluating the realism of the pair potential.

## Approach
The approach uses an anharmonic short-range interaction model together with the Esterling–Swaroop polynomial pair potential. The pair potential is piecewise polynomial across neighbour shells; its coefficients for Cu, Ag, and Au are obtained from the original Esterling–Swaroop publications (Assets). For each metal, the equilibrium distance r_e is determined by minimizing the total free energy, and the first minimum of the potential energy (bar_r_e) is located. From the potential, the second, third, and fourth spatial derivatives at r_e and the second derivative at bar_r_e are evaluated.

The Debye temperature is computed from the experimental isothermal bulk modulus K_T (retrieved from ultrasonic measurement papers) and r_e. The Grüneisen parameter follows from r_e and the potential derivatives. A characteristic lattice frequency ω_L is defined from the second derivative at bar_r_e and the atomic mass. Using ω_L, r_e derivatives, and the Debye temperature, auxiliary dimensionless parameters (including a temperature scale T_A) are calculated. The molar heat at constant volume C_v at each prescribed temperature is then obtained from low- or high-temperature limiting forms of anharmonic lattice dynamics, depending on the magnitude of k_B T relative to ω_L. The volume thermal expansion coefficient β is derived from C_v, r_e, and the potential derivatives. All computations are performed for Cu, Ag, and Au at temperatures 20, 50, 100, 150, 200, and 300 K.

## Reproduction target
Compute the Debye temperature Θ_D and Grüneisen parameter γ at T = 0 K for Cu, Ag, and Au. Then compute the volume thermal expansion coefficient β and the molar heat at constant volume C_v for each of the same three metals at the set of temperatures T ∈ {20, 50, 100, 150, 200, 300} K, using the pair potential polynomials and the experimental isothermal bulk moduli specified in the assets. Output all computed values in a single CSV file following the schema defined for `computed_properties.csv`.

## Assets

- Esterling and Swaroop pair potential coefficients for Cu (1979): 10.1002/pssb.2220960210
- Esterling and Swaroop pair potential coefficients for Ag and Au (1979): 10.1002/pssb.2220960232
- Overton & Gaffney, isothermal bulk modulus of Cu (1955): 10.1103/PhysRev.98.969
- Neighbours & Alers, isothermal bulk moduli of Ag and Au (1958): 10.1103/PhysRev.111.707

## Workflow steps

### Step 1: Extract pair potential coefficients and compute equilibrium properties
- Role: process
- Action: Obtain the polynomial pair potential coefficients C_{j,i} for Cu, Ag, Au from the Esterling and Swaroop papers. For each metal, determine the equilibrium distance r_e by minimizing the total free energy, and evaluate the second, third, and fourth spatial derivatives of the potential at r_e. Also determine the first-minimum distance bar_r_e of the potential energy.
- Evidence: `/app/outputs/potential_derivatives.json`

### Step 2: Compute Debye temperature and Grüneisen parameter
- Role: process
- Action: For each metal, retrieve the experimental isothermal bulk modulus K_T from the cited ultrasonic measurement papers (Overton & Gaffney 1955 for Cu; Neighbours & Alers 1958 for Ag and Au). Using K_T, the equilibrium distance r_e, and the potential derivatives, compute the Debye temperature Θ_D via the relation Θ_D = n (5 K_T r_e)^(1/2) / k_B. Compute the Grüneisen parameter γ from r_e and the potential derivatives.
- Evidence: `/app/outputs/debye_gamma.json`

### Step 3: Compute auxiliary quantities for anharmonic heat capacity
- Role: process
- Action: Using the potential derivatives, atomic mass, the Debye temperature from step 2, compute the characteristic lattice frequency ω_L = ħ sqrt(8 Φ''(bar_r_e)/m). Then compute the dimensionless parameters G = [Φ'''(r_e)]^2/[Φ''(r_e)]^3, K = Φ''''(r_e)/[Φ''(r_e)]^2, C_x = 0.125 (K - B G), α = 1 - A ω_L G, and the temperature scale T_A = Θ_D α (1 + 8 A ω_L C_x). Use A=0.04257 and B=0.2992.
- Evidence: `/app/outputs/auxiliary_parameters.json`

### Step 4: Compute molar heat C_v and volume thermal expansion β and assemble output CSV
- Role: scored (load-bearing)
- Action: For each metal (Cu, Ag, Au) and each temperature T in {20, 50, 100, 150, 200, 300} K, compute the molar heat at constant volume C_v using the low-temperature limit (C_v = (12/5) π^4 R (T/T_A)^3) when Θ ≪ ω_L and the high-temperature limit (C_v = 3R [1 - Θ C_x - 0.04166 (ω_L/Θ)^2]) when Θ ≫ ω_L, where Θ = k_B T. Then compute the volume thermal expansion coefficient β via β = - (C_v / (2 r_e N_A)) * [Φ'''(r_e) / (Φ''(r_e))^2]. Collect all computed results: Θ_D and γ from previous steps (with T_K=0.0) and the β and C_v values for each temperature. Write a CSV file 'computed_properties.csv' with columns: metal (Cu/Ag/Au), property (Theta_D, gamma, beta, C_v), T_K (numeric, use 0.0 for Θ_D and γ), value (numeric), unit (K for Theta_D, dimensionless for gamma, 1e-6/K for beta, J/(mol·K) for C_v). Include one row per metal per property per temperature.
- Output file: `/app/outputs/computed_properties.csv`
- Format: csv
- Contract: Columns: metal (string, one of Cu, Ag, Au), property (string, one of Theta_D, gamma, beta, C_v), T_K (float, temperature in K; 0.0 for Theta_D and gamma), value (float, numeric value), unit (string, e.g., K, dimensionless, 1e-6/K, J/(mol·K)). One row per metal-property-temperature combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.csv
- path: `/app/outputs/computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The final output containing the Debye temperature, Grüneisen parameter, volume thermal expansion coefficient, and molar heat at constant volume for Cu, Ag, Au at the specified temperatures.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `property`, `T_K`, `value`, `unit`
  - `items`: object
  - `units`:
    - `metal`: string, one of Cu, Ag, Au
    - `property`: string, one of Theta_D, gamma, beta, C_v
    - `T_K`: float, temperature in K (0.0 for Theta_D and gamma)
    - `value`: float, numeric value
    - `unit`: string, K for Theta_D, dimensionless for gamma, 1e-6/K for beta, J/(mol·K) for C_v

Notes: The agent must compute the values using the described methods with potential coefficients from the original Esterling–Swaroop papers and experimental bulk modulus data from the ultrasonic measurement references. The hidden comparison tolerances are not disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "property",
          "T_K",
          "value",
          "unit"
        ],
        "items": {},
        "units": {
          "metal": "string, one of Cu, Ag, Au",
          "property": "string, one of Theta_D, gamma, beta, C_v",
          "T_K": "float, temperature in K (0.0 for Theta_D and gamma)",
          "value": "float, numeric value",
          "unit": "string, K for Theta_D, dimensionless for gamma, 1e-6/K for beta, J/(mol·K) for C_v"
        }
      },
      "description": "The final output containing the Debye temperature, Grüneisen parameter, volume thermal expansion coefficient, and molar heat at constant volume for Cu, Ag, Au at the specified temperatures."
    }
  ],
  "notes": "The agent must compute the values using the described methods with potential coefficients from the original Esterling–Swaroop papers and experimental bulk modulus data from the ultrasonic measurement references. The hidden comparison tolerances are not disclosed."
}
```

## How you are scored
A hidden verifier reads your file `/app/outputs/computed_properties.csv` and independently extracts each reported value of Θ_D, γ, β, and C_v for every metal and temperature. It compares each one to a hidden reference gold value using appropriate, per‑quantity tolerances. The reward is proportional to the fraction of your reported values that fall within tolerance. Note that the verifier uses a hidden standard, so simply copying the paper's numbers is not sufficient — your computed values must genuinely match the reference within the concealed tolerances.
