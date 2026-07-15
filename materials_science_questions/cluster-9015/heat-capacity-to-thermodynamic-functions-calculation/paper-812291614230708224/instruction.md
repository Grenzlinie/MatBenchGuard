# Standard Entropy and Free Energy of Bismuth Compounds from Heat Capacity Data

## Problem background
Thermodynamic properties such as standard entropy and free energy of formation are central to understanding material stability and reactivity. For bismuth and bismuth trioxide, these quantities can be derived from low-temperature heat capacity measurements. The standard entropy at 298 K is obtained by combining a theoretical extrapolation of the unmeasured region near absolute zero with a numerical integration of measured heat capacity data from cryogenic temperatures up to room temperature. This entropy, together with known thermochemical data, then allows the calculation of the Gibbs free energy of formation of Bi₂O₃.

## Approach
The standard entropy is computed as the sum of two contributions: (1) a Debye-function extrapolation from 0 to 56.2 K using Debye temperatures θ = 147 K for Bi and θ = 97 K for Bi₂O₃, and (2) a numerical integration of Cp/T from 56.2 K to 298.1 K using the provided measured data points. Any reasonable numerical integration method (e.g., trapezoidal or Simpson's rule) may be employed. The free energy of formation of Bi₂O₃ is then calculated from the standard thermodynamic relation ΔG = ΔH − TΔS, using the standard entropy of O₂ (49.0 cal/(K·mol)) and the heat of formation ΔH = −136,000 cal, with T = 298 K. The workflow requires loading the heat capacity table, performing the Debye and integration steps for each compound, and finally applying the free‑energy formula.

## Reproduction target
From the provided heat capacity data for Bi and Bi₂O₃ and the given Debye temperatures, compute the standard entropies at 298 K (including the separate extrapolated and graphical contributions) and the standard Gibbs free energy of formation of Bi₂O₃. Write the entropy contributions and totals to /app/outputs/entropy_contributions.json and the free energy result to /app/outputs/free_energy.json.

## Assets

### Heat capacity data for Bi and Bi₂O₃
The following table gives the measured heat capacities from the source paper (Table II). Debye temperatures for the low‑temperature extrapolation are θ(Bi) = 147 K, θ(Bi₂O₃) = 97 K.

| T / K | Cp(Bi) / (cal·K⁻¹·mol⁻¹) | T / K | Cp(Bi) / (cal·K⁻¹·mol⁻¹) | T / K | Cp(Bi₂O₃) / (cal·K⁻¹·mol⁻¹) | T / K | Cp(Bi₂O₃) / (cal·K⁻¹·mol⁻¹) |
|-------|---------------------------|-------|---------------------------|-------|-------------------------------|-------|-------------------------------|
| 60.8  | 4.631                     | 176.8 | 5.899                     | 289.3 | 26.25                         | 118.6 | 16.86                         |
| 64.7  | 4.771                     | 187.7 | 5.924                     | 262.1 | 26.17                         | 129.2 | 17.80                         |
| 63.4  | 4.851                     | 198.9 | 5.976                     | 271.4 | 26.29                         | 143.1 | 18.93                         |
| 71.1  | 5.040                     | 208.8 | 5.974                     | 279.7 | 26.54                         | 155.7 | 19.96                         |
| 74.6  | 5.216                     | 218.8 | 5.980                     | 60.6  | 9.50                          | 166.4 | 20.85                         |
| 101.3 | 5.464                     | 258.1 | 5.874                     | 63.7  | 10.89                         | 175.8 | 21.49                         |
| 111.2 | 5.674                     | 266.3 | 6.058                     | 68.7  | 11.24                         | 188.5 | 22.35                         |
| 125.1 | 5.813                     | 272.8 | 6.083                     | 73.6  | 11.64                         | 198.2 | 22.95                         |
| 137.2 | 5.761                     | 285.3 | 6.139                     | 82.6  | 12.85                         | 134.7 | 18.24                         |
| 150.2 | 5.817                     | 295.2 | 6.089                     | 89.3  | 13.32                         | 213.3 | 23.87                         |
| 162.5 | 5.869                     | 298.2 | 6.104                     | 101.4 | 14.72                         | 238.4 | 24.88                         |
|       |                           |       |                           | 113.0 | 16.31                         |       |                               |

## Workflow steps

### Step 1: Compute standard entropy contributions
- Role: scored
- Action: Load the provided Cp vs T data for Bi and Bi2O3. For each compound, compute the Debye function contribution to the entropy for 0–56.2 K using the given Debye temperatures (θ=147 K for Bi, θ=97 K for Bi2O3). Numerically integrate Cp/T from 56.2 K to 298.1 K using the measured data points. Sum the two contributions to obtain the total standard entropy at 298 K. Write the results to /app/outputs/entropy_contributions.json.
- Output file: `/app/outputs/entropy_contributions.json`
- Format: json
- Contract: JSON object with top-level keys 'Bi' and 'Bi2O3', each containing an object with fields 'extrapolated_0_56.2_K' (float, unit: cal/(K·mol)), 'graphical_56.2_298.1_K' (float, unit: cal/(K·mol)), 'total_S_298_K' (float, unit: cal/(K·mol)).
- Scoring: scored by hidden verifier

### Step 2: Compute free energy of formation of Bi2O3
- Role: scored
- Action: Using the total entropy of Bi2O3 from step1, the total entropy of Bi from step1, the standard entropy of O2 (49.0 cal/(K·mol)), and the heat of formation of Bi2O3 (ΔH = -136,000 cal), calculate the standard free energy of formation at 298 K: ΔG = ΔH - 298*(S°(Bi2O3) - 2*S°(Bi) - 1.5*S°(O2)). Write the result to /app/outputs/free_energy.json.
- Output file: `/app/outputs/free_energy.json`
- Format: json
- Contract: JSON object with fields 'free_energy_Bi2O3' (float, unit: cal) and 'unit' (string, value 'cal').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/entropy_contributions.json`
- `/app/outputs/free_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### entropy_contributions.json
- path: `/app/outputs/entropy_contributions.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The computed entropy contributions and total standard entropy for Bi and Bi2O3. These values are compared against reference values within a hidden tolerance.
- schema:
  - `type`: object
  - `required`:
    - `Bi`:
      - `extrapolated_0_56.2_K`: float (cal/(K·mol))
      - `graphical_56.2_298.1_K`: float (cal/(K·mol))
      - `total_S_298_K`: float (cal/(K·mol))
    - `Bi2O3`:
      - `extrapolated_0_56.2_K`: float (cal/(K·mol))
      - `graphical_56.2_298.1_K`: float (cal/(K·mol))
      - `total_S_298_K`: float (cal/(K·mol))
  - `items`: object
  - `required_columns`:
  - `units`: object

### free_energy.json
- path: `/app/outputs/free_energy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The calculated standard free energy of formation of Bi2O3, compared to the reference within a hidden tolerance.
- schema:
  - `type`: object
  - `required`:
    - `free_energy_Bi2O3`: float (cal)
    - `unit`: string (value 'cal')
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: All required input parameters (Cp data, Debye temperatures, entropy of O2, heat of formation) are provided in the task instruction. The agent must perform numerical integration (e.g., trapezoidal or Simpson's rule) to obtain the graphical contributions. No external data downloads are needed beyond the inline table.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "entropy_contributions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Bi": {
            "extrapolated_0_56.2_K": "float (cal/(K·mol))",
            "graphical_56.2_298.1_K": "float (cal/(K·mol))",
            "total_S_298_K": "float (cal/(K·mol))"
          },
          "Bi2O3": {
            "extrapolated_0_56.2_K": "float (cal/(K·mol))",
            "graphical_56.2_298.1_K": "float (cal/(K·mol))",
            "total_S_298_K": "float (cal/(K·mol))"
          }
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "The computed entropy contributions and total standard entropy for Bi and Bi2O3. These values are compared against reference values within a hidden tolerance."
    },
    {
      "file": "free_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "free_energy_Bi2O3": "float (cal)",
          "unit": "string (value 'cal')"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "The calculated standard free energy of formation of Bi2O3, compared to the reference within a hidden tolerance."
    }
  ],
  "notes": "All required input parameters (Cp data, Debye temperatures, entropy of O2, heat of formation) are provided in the task instruction. The agent must perform numerical integration (e.g., trapezoidal or Simpson's rule) to obtain the graphical contributions. No external data downloads are needed beyond the inline table."
}
```

## How you are scored
A hidden verifier reads your two output files and compares each numeric field against reference values using absolute tolerances. The overall score (0.0–1.0) is a weighted combination: the entropy contributions for both Bi and Bi₂O₃ together account for half of the score, and the free energy of formation accounts for the other half. The verifier also checks internal consistency, such as that the total entropy equals the sum of the extrapolated and graphical contributions. Reporting a value without actually performing the integration will not satisfy the tolerance, so the computation must be genuinely executed.
