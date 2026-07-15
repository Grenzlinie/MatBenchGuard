# Landau free-energy magnetocaloric effect in Ni-Mn-Cu-Ga and Ni-Mn-In alloys

## Problem background
Ferromagnetic shape memory alloys such as Ni-Mn-Cu-Ga and Ni-Mn-In undergo both magnetic and structural phase transitions. The coupling between magnetization and lattice strain gives rise to a magnetocaloric effect (MCE), where an applied magnetic field changes the entropy. The nature of the MCE—whether it is a normal effect with a negative entropy change or an inverse effect with a positive one—depends on the character of the magneto-structural interaction. This task aims to reproduce the field-induced entropy change and refrigerant capacity from a phenomenological Landau free energy model to elucidate the underlying physical mechanisms.

## Approach
The simulations are built on a dimensionless Landau free energy expanded in powers of the magnetization ¯M̄ and the tetragonal strain ¯ē₃, with terms that describe the ferromagnetic, martensitic, and magneto-structural interactions. For each composition and magnetic field, the equilibrium order parameters (¯M̄, ¯ē₃) are found by solving the coupled equations that minimize the free energy. The field-induced isothermal entropy change Δ¯S̄ is then computed from the shifts in ¯M̄² and ¯ē₃², and the refrigerant capacity is obtained by integrating Δ¯S̄ between the zero-field and field-shifted first-order transition temperatures. The approach is applied to two alloy systems, Ni₂Mn₁₋ₓCuₓGa and Ni₂Mn₁₊ₓIn₁₋ₓ, each with a distinct set of free-energy parameters.

## Reproduction target
Produce the dimensionless field-induced entropy change Δ¯S̄ as a function of reduced temperature for Ni₂Mn₀.₇₄Cu₀.₂₆Ga and Ni₂Mn₁.₃₇In₀.₆₃ at a fixed dimensionless magnetic field ¯H̄=0.005. In addition, compute the refrigerant capacity ¯RC̅ as a function of composition x for Ni₂Mn₁₋ₓCuₓGa (x = 0.20, 0.22, 0.24, 0.26, 0.28, 0.30) and for Ni₂Mn₁₊ₓIn₁₋ₓ (x = 0.34, 0.36, 0.37, 0.38, 0.40, 0.42) at the same field. The results should capture the temperature dependence, sign, and composition trends of the magnetocaloric effect as predicted by the Landau model.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Solve coupled equilibrium equations for order parameters
- Role: process
- Action: Implement the dimensionless Landau free energy for Ni₂Mn₁₋ₓCuₓGa and Ni₂Mn₁₊ₓIn₁₋ₓ using the parameter sets given in the paper. For each alloy composition (x=0.26, x=0.37, and the scanned x ranges) and for magnetic fields H̄=0 and H̄=0.005, numerically minimize the free energy or solve the coupled equilibrium equations to obtain the equilibrium dimensionless magnetization M̄ and tetragonal strain ē₃ as functions of reduced temperature t. Identify the first-order transition temperatures TA (at H̄=0) and TB (at H̄≠0). Save the resulting arrays of (t, M̄, ē₃, TA, TB) for all required compositions and fields.
- Evidence: `/app/outputs/order_parameters.npz`

### Step 2: Calculate field-induced entropy change ΔS̄ for Ni₂Mn₀.₇₄Cu₀.₂₆Ga
- Role: scored (load-bearing)
- Action: Using the M̄ and ē₃ arrays from Step 1 for x=0.26 and H̄=0.005, compute the isothermal field‑induced entropy change ΔS̄ as the sum of the ferromagnetic contribution (proportional to the change in M̄²) and the martensitic contribution (proportional to the change in ē₃²). Output a CSV file with columns `reduced_temperature` and `delta_S`.
- Output file: `/app/outputs/delta_S_CuGa.csv`
- Format: csv
- Contract: Two columns: reduced_temperature (float), delta_S (float)
- Scoring: scored by hidden verifier

### Step 3: Calculate field-induced entropy change ΔS̄ for Ni₂Mn₁.₃₇In₀.₆₃
- Role: scored (load-bearing)
- Action: Using the M̄ and ē₃ arrays from Step 1 for x=0.37 and H̄=0.005, compute ΔS̄ as the sum of ferromagnetic and martensitic contributions. Output a CSV file with columns `reduced_temperature` and `delta_S`.
- Output file: `/app/outputs/delta_S_In.csv`
- Format: csv
- Contract: Two columns: reduced_temperature (float), delta_S (float)
- Scoring: scored by hidden verifier

### Step 4: Calculate refrigerant capacity RC̄ vs x for Ni₂Mn₁₋ₓCuₓGa series
- Role: scored (load-bearing)
- Action: From the full temperature scans obtained in Step 1 for compositions x in [0.20, 0.22, 0.24, 0.26, 0.28, 0.30] at H̄=0.005, compute the refrigerant capacity RC̄ by integrating ΔS̄ between TB and TA. Output a CSV with columns `x` and `RC_bar`.
- Output file: `/app/outputs/RC_CuGa.csv`
- Format: csv
- Contract: Two columns: x (float), RC_bar (float)
- Scoring: scored by hidden verifier

### Step 5: Calculate refrigerant capacity RC̄ vs x for Ni₂Mn₁₊ₓIn₁₋ₓ series
- Role: scored (load-bearing)
- Action: From the full temperature scans obtained in Step 1 for compositions x in [0.34, 0.36, 0.37, 0.38, 0.40, 0.42] at H̄=0.005, compute RC̄ by integrating ΔS̄ between TB and TA. Output a CSV with columns `x` and `RC_bar`.
- Output file: `/app/outputs/RC_In.csv`
- Format: csv
- Contract: Two columns: x (float), RC_bar (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_S_CuGa.csv`
- `/app/outputs/delta_S_In.csv`
- `/app/outputs/RC_CuGa.csv`
- `/app/outputs/RC_In.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_S_CuGa.csv
- path: `/app/outputs/delta_S_CuGa.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Dimensionless entropy change ΔS̄ vs. reduced temperature t for Ni₂Mn₀.₇₄Cu₀.₂₆Ga at H̄=0.005. Must show a negative ΔS̄ with a large peak in the transition region.
- schema:
  - `type`: table
  - `required_columns`: `reduced_temperature`, `delta_S`
  - `units`:
    - `reduced_temperature`: dimensionless
    - `delta_S`: dimensionless

### delta_S_In.csv
- path: `/app/outputs/delta_S_In.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Dimensionless entropy change ΔS̄ vs. reduced temperature t for Ni₂Mn₁.₃₇In₀.₆₃ at H̄=0.005. Must show a positive ΔS̄ (inverse MCE) in the transition region.
- schema:
  - `type`: table
  - `required_columns`: `reduced_temperature`, `delta_S`
  - `units`:
    - `reduced_temperature`: dimensionless
    - `delta_S`: dimensionless

### RC_CuGa.csv
- path: `/app/outputs/RC_CuGa.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Refrigerant capacity RC̄ vs. composition x for Ni₂Mn₁₋ₓCuₓGa at H̄=0.005. Must peak near x=0.25.
- schema:
  - `type`: table
  - `required_columns`: `x`, `RC_bar`
  - `units`:
    - `x`: dimensionless composition
    - `RC_bar`: dimensionless

### RC_In.csv
- path: `/app/outputs/RC_In.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Refrigerant capacity RC̄ vs. composition x for Ni₂Mn₁₊ₓIn₁₋ₓ at H̄=0.005. Must peak near x=0.375.
- schema:
  - `type`: table
  - `required_columns`: `x`, `RC_bar`
  - `units`:
    - `x`: dimensionless composition
    - `RC_bar`: dimensionless

Notes: The task verifies the sign and composition dependence of the magnetocaloric effect (normal for CuGa, inverse for In) and the refrigerant capacity trends predicted by the Landau free energy model. Only the core model predictions are required; the later Maxwell relation analysis (Section 6 of the paper) is excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_S_CuGa.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "reduced_temperature",
          "delta_S"
        ],
        "units": {
          "reduced_temperature": "dimensionless",
          "delta_S": "dimensionless"
        }
      },
      "description": "Dimensionless entropy change ΔS̄ vs. reduced temperature t for Ni₂Mn₀.₇₄Cu₀.₂₆Ga at H̄=0.005. Must show a negative ΔS̄ with a large peak in the transition region."
    },
    {
      "file": "delta_S_In.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "reduced_temperature",
          "delta_S"
        ],
        "units": {
          "reduced_temperature": "dimensionless",
          "delta_S": "dimensionless"
        }
      },
      "description": "Dimensionless entropy change ΔS̄ vs. reduced temperature t for Ni₂Mn₁.₃₇In₀.₆₃ at H̄=0.005. Must show a positive ΔS̄ (inverse MCE) in the transition region."
    },
    {
      "file": "RC_CuGa.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "RC_bar"
        ],
        "units": {
          "x": "dimensionless composition",
          "RC_bar": "dimensionless"
        }
      },
      "description": "Refrigerant capacity RC̄ vs. composition x for Ni₂Mn₁₋ₓCuₓGa at H̄=0.005. Must peak near x=0.25."
    },
    {
      "file": "RC_In.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "RC_bar"
        ],
        "units": {
          "x": "dimensionless composition",
          "RC_bar": "dimensionless"
        }
      },
      "description": "Refrigerant capacity RC̄ vs. composition x for Ni₂Mn₁₊ₓIn₁₋ₓ at H̄=0.005. Must peak near x=0.375."
    }
  ],
  "notes": "The task verifies the sign and composition dependence of the magnetocaloric effect (normal for CuGa, inverse for In) and the refrigerant capacity trends predicted by the Landau free energy model. Only the core model predictions are required; the later Maxwell relation analysis (Section 6 of the paper) is excluded."
}
```

## How you are scored
A hidden verifier independently scores each scored artifact (entropy change curves and refrigerant capacity tables) by comparing the submitted results against reference expectations derived from the same model parameters. The verifier checks the shape, sign, peak location, and relative trends of the reported quantities without requiring exact numerical agreement. Each scored step contributes a portion of the final reward, with the main entropy-change and refrigerant-capacity outputs carrying the largest weight. Reporting a single number is not sufficient; the verifier evaluates the full numerical curves and tables.
