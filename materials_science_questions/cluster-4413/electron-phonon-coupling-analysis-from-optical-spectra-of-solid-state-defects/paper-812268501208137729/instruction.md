# Crystal‑field analysis of Er³⁺ in Er₂O₃ powder

## Problem background
Crystal-field analysis is essential for understanding the optical properties of rare-earth ions in solid-state hosts. This task addresses a crystal-field analysis of Er³⁺ ions occupying C₂ symmetry sites in Er₂O₃ powder. The objective is to determine the one-electron crystal-field Hamiltonian parameters by fitting a model to 22 experimentally observed Stark energy levels. The resulting parameters quantify the local crystal-field interaction and enable the derivation of reduced crystal-field strength parameters, which characterise the overall crystal-field effect and allow comparison across different hosts and material forms.

## Approach
The analysis is based on a one-electron crystal-field Hamiltonian expressed in terms of real (B_q^k) and imaginary (S_q^k) parameters multiplied by spherical tensor operators C_q^k. For the C₂ symmetry of the Er³⁺ site, the Hamiltonian includes terms with k = 2, 4, 6 and the allowed q values, with the coordinate system rotated so that the imaginary parameter S_2^2 is fixed to zero. Numerical computation of the matrix elements of the C_q^k operators in the 4f¹¹ basis is required.

A nonlinear least-squares fit is performed using the Nelder–Mead algorithm to determine the 14 crystal-field parameters by minimising the root‑mean‑square deviation between the calculated and the provided observed Stark energies. An initial guess for the parameters is taken from a related study of Er³⁺ in Y₂O₃ single crystal (see Assets).

After the fit, the Stark energy levels of the ⁴I_15/2, ⁴I_13/2, ⁴I_9/2, and ⁴S_3/2 multiplets are computed from the fitted Hamiltonian. Finally, reduced crystal-field strength parameters S_cf², S_cf⁴, S_cf⁶ and the overall strength N_V are derived from the fitted B_q^k and S_q^k values using the standard formulas.

## Reproduction target
Implement the crystal-field Hamiltonian for C₂ symmetry, compute the required matrix elements, and fit the Hamiltonian to the 22 observed Stark energies provided in the task instructions, using the initial guess from Er³⁺ in Y₂O₃. The fitting must yield the 14 fitted crystal-field parameters (B_q^k and S_q^k) and the rms deviation between the calculated and observed energies. Using the fitted parameters, compute the Stark energy levels for the four multiplets and report them in a CSV file. From the fitted parameters, derive the crystal-field strength parameters S_cf², S_cf⁴, S_cf⁶, and N_V. The task is evaluated on whether the fitted parameters and derived quantities fall within acceptable ranges, and whether the rms deviation computed from the calculated levels meets a predefined threshold.

## Assets

### Observed Stark energy levels of Er³⁺ in Er₂O₃

The following 22 experimentally observed Stark energies (in cm⁻¹) are provided as the target for the fit.

| multiplet   | level_index | energy_cm1 |
|-------------|-------------|------------|
| 4I15/2      | 1           | 0          |
| 4I15/2      | 2           | 36         |
| 4I15/2      | 3           | 69         |
| 4I15/2      | 4           | 86         |
| 4I15/2      | 5           | 162        |
| 4I15/2      | 6           | 263        |
| 4I15/2      | 7           | 484        |
| 4I15/2      | 8           | 503        |
| 4I13/2      | 1           | 6507       |
| 4I13/2      | 2           | 6544       |
| 4I13/2      | 3           | 6584       |
| 4I13/2      | 4           | 6594       |
| 4I13/2      | 5           | 6684       |
| 4I13/2      | 6           | 6835       |
| 4I13/2      | 7           | 6861       |
| 4I9/2       | 1           | 12305      |
| 4I9/2       | 2           | 12419      |
| 4I9/2       | 3           | 12494      |
| 4I9/2       | 4           | 12585      |
| 4I9/2       | 5           | 12614      |
| 4S3/2       | 1           | 18220      |
| 4S3/2       | 2           | 18316      |
- Initial crystal‑field parameters for Er³⁺ in Y₂O₃ single crystal: 10.1063/1.462395

## Workflow steps

### Step 1: Define crystal‑field Hamiltonian and compute matrix elements
- Role: process
- Action: Set up the one‑electron crystal‑field Hamiltonian for C₂ symmetry, numerically compute matrix elements of the tesseral spherical tensor operators C_q^k, and fix the coordinate rotation such that S_2^2 = 0.
- Evidence: none

### Step 2: Fit crystal‑field parameters with Nelder‑Mead optimization
- Role: scored (load-bearing)
- Action: Using the provided 22 observed Stark energies and the initial guess from Er³⁺ in Y₂O₃, perform a nonlinear least‑squares fit via the Nelder‑Mead algorithm to minimize the root‑mean‑square deviation between calculated and observed energies. Save the final fitted parameters and the achieved rms deviation.
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: JSON object with keys: B0_2, B2_2, B0_4, B2_4, B4_4, S2_4, S4_4, B0_6, B2_6, B4_6, B6_6, S2_6, S4_6, S6_6 (real numbers, unit cm⁻¹), and rms_deviation (float, cm⁻¹).
- Scoring: scored by hidden verifier

### Step 3: Compute calculated Stark energy levels
- Role: scored
- Action: Using the fitted Hamiltonian parameters from step 2, compute the Stark energy levels for the ⁴I_15/2, ⁴I_13/2, ⁴I_9/2, and ⁴S_3/2 multiplets. Save the list of calculated levels in a CSV file.
- Output file: `/app/outputs/calculated_stark_levels.csv`
- Format: csv
- Contract: CSV table with columns: multiplet (string, e.g., '4I15/2'), level_index (integer starting at 1), calculated_energy_cm1 (float, unit cm⁻¹).
- Scoring: scored by hidden verifier

### Step 4: Calculate crystal‑field strength parameters
- Role: scored
- Action: From the fitted crystal‑field parameters, compute the reduced strength parameters S_cf^k (k = 2, 4, 6) and the overall strength N_V using the published formulas. Save the values in a JSON file.
- Output file: `/app/outputs/strength_parameters.json`
- Format: json
- Contract: JSON object with keys: Scf2, Scf4, Scf6, NV (all floats, unit cm⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.json`
- `/app/outputs/calculated_stark_levels.csv`
- `/app/outputs/strength_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted crystal‑field parameters and the associated rms deviation from the fit to 22 Stark levels.
- schema:
  - `type`: object
  - `required`:
    - `B0_2`: float
    - `B2_2`: float
    - `B0_4`: float
    - `B2_4`: float
    - `B4_4`: float
    - `S2_4`: float
    - `S4_4`: float
    - `B0_6`: float
    - `B2_6`: float
    - `B4_6`: float
    - `B6_6`: float
    - `S2_6`: float
    - `S4_6`: float
    - `S6_6`: float
    - `rms_deviation`: float
  - `units`:
    - `all_parameters`: cm⁻¹
    - `rms_deviation`: cm⁻¹

### calculated_stark_levels.csv
- path: `/app/outputs/calculated_stark_levels.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Calculated Stark energies for the four multiplets. The verifier recomputes the rms deviation between these calculated energies and the hidden observed energies.
- schema:
  - `type`: table
  - `required_columns`: `multiplet`, `level_index`, `calculated_energy_cm1`
  - `units`:
    - `calculated_energy_cm1`: cm⁻¹

### strength_parameters.json
- path: `/app/outputs/strength_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reduced crystal‑field strength parameters S_cf², S_cf⁴, S_cf⁶ and the overall strength N_V derived from the fitted parameters.
- schema:
  - `type`: object
  - `required`:
    - `Scf2`: float
    - `Scf4`: float
    - `Scf6`: float
    - `NV`: float
  - `units`:
    - `all`: cm⁻¹

Notes: The observed Stark energies are provided as a data table in the instruction. The initial guess parameters must be retrieved from the literature reference Chang et al. (1982).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "B0_2": "float",
          "B2_2": "float",
          "B0_4": "float",
          "B2_4": "float",
          "B4_4": "float",
          "S2_4": "float",
          "S4_4": "float",
          "B0_6": "float",
          "B2_6": "float",
          "B4_6": "float",
          "B6_6": "float",
          "S2_6": "float",
          "S4_6": "float",
          "S6_6": "float",
          "rms_deviation": "float"
        },
        "units": {
          "all_parameters": "cm⁻¹",
          "rms_deviation": "cm⁻¹"
        }
      },
      "description": "Fitted crystal‑field parameters and the associated rms deviation from the fit to 22 Stark levels."
    },
    {
      "file": "calculated_stark_levels.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "multiplet",
          "level_index",
          "calculated_energy_cm1"
        ],
        "units": {
          "calculated_energy_cm1": "cm⁻¹"
        }
      },
      "description": "Calculated Stark energies for the four multiplets. The verifier recomputes the rms deviation between these calculated energies and the hidden observed energies."
    },
    {
      "file": "strength_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Scf2": "float",
          "Scf4": "float",
          "Scf6": "float",
          "NV": "float"
        },
        "units": {
          "all": "cm⁻¹"
        }
      },
      "description": "Reduced crystal‑field strength parameters S_cf², S_cf⁴, S_cf⁶ and the overall strength N_V derived from the fitted parameters."
    }
  ],
  "notes": "The observed Stark energies are provided as a data table in the instruction. The initial guess parameters must be retrieved from the literature reference Chang et al. (1982)."
}
```

## How you are scored
Your submission is evaluated automatically by a hidden verifier that scores each output artifact independently: fitted_parameters.json, calculated_stark_levels.csv, and strength_parameters.json.

- For the fitted parameters (fitted_parameters.json) and the strength parameters (strength_parameters.json), the verifier compares your reported values to hidden reference values within permitted numerical tolerances. Full credit is awarded when all values lie within those tolerances.
- For the calculated Stark levels (calculated_stark_levels.csv), the verifier recomputes the root‑mean‑square deviation between your calculated energies and a hidden set of observed energies and awards credit if the rms deviation is at or below a predetermined threshold.

The final reward is a weighted combination of the scores from all three artifacts. Simply reporting numbers copied from a publication without performing the genuine implementation and fit will not satisfy the tolerances or threshold and will not earn credit.
