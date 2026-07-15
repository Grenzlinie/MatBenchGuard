# Interatomic Potential Parameterization and Elastic Property Calculation for CsCl Structure Solids

## Problem background
The elastic constants of ionic solids reflect the underlying interatomic forces. In central-force models, Cauchy relations impose constraints among the second- and third-order elastic constants at zero temperature, but experimental measurements consistently exhibit deviations from these relations. This task addresses a theoretical investigation that incorporates a many-body term – via a Lundqvist-type potential – to explain the observed Cauchy discrepancies in CsCl-structure ionic crystals at 0 K. The goal is to compute, from first principles, the third-order elastic constants and the pressure derivatives of the second-order elastic constants for CsCl, CsBr, and CsI, using the model's parametric expressions and available experimental input data. The results quantify the role of the many-body interaction and allow comparison with previous models and with the limited experimental data for these compounds.

## Approach
The approach treats the crystal potential as a sum of the Coulomb energy, a short-range overlap repulsive energy extended up to next-nearest neighbours, and a three-body many-body term that depends on a function f(r) and its derivatives. The overlap repulsive potentials are approximated by two-parameter Born-Mayer forms, which reduce the six repulsive potential parameters to two basic unknowns plus a hardness parameter ϱ. Using the experimental second-order elastic constants (C11, C12, C44) and the equilibrium condition, a system of seven equations is set up for the seven unknown quantities (four repulsive parameters, two many-body parameters [f(r)]₀ and [a∂f/∂r]₀, and ϱ). This system is solved by successive approximation simultaneously for each compound and for two overlap models: (i) repulsion limited to nearest neighbours (NN) and (ii) repulsion extended to next-nearest neighbours (NNN). Once the primary parameter set is obtained, the remaining many-body second derivative [a²∂²f/∂r²]₀ is determined from the experimental pressure derivative of the bulk modulus, dK′/dp. The complete parameter set then enters the parametric expressions to compute all six third-order elastic constants (C111, C112, C166, C123, C144, C456) and the pressure derivatives dC44′/dp and dS′/dp. Finally, the linear combinations C111+2C112, C123+2C112, and C144+2C166 are calculated. All computations are to be performed using publicly available experimental input data (lattice constants, ionic radii, SOE constants, and dK′/dp) for CsCl, CsBr, and CsI.

## Reproduction target
Given the experimental input data for CsCl, CsBr, and CsI (provided as input_data.csv), implement the parameterization and computation described above. Produce three CSV files under `/app/outputs`:  
- `toe_constants.csv`: Six third-order elastic constants (C111, C112, C166, C123, C144, C456) in units of 10¹² dyn/cm², for each compound and each model (NN, NNN).  
- `pressure_derivatives.csv`: Pressure derivatives dC44′/dp and dS′/dp (dimensionless), for each compound and model.  
- `linear_combinations.csv`: Linear combinations C111+2C112, C123+2C112, and C144+2C166 in units of 10¹² dyn/cm², for each compound and model.  
The numbers must be computed from the fitted potential and not copied from the literature.

## Assets

- Experimental input data for CsCl, CsBr, CsI
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Fit model parameters using Born-Mayer approximation and SOE equations
- Role: process
- Action: Using the provided experimental input data (lattice constants, ionic radii, second-order elastic constants) for CsCl, CsBr, and CsI, approximate the overlap repulsive potentials as two-parameter Born-Mayer forms. Set up a system of equations (three second-order elastic constant expressions, the equilibrium condition, and the Born-Mayer algebraic relations among parameters) and solve by successive approximation to determine the seven unknown parameters: A1, B1, A2, B2, [f(r)]0, [a∂f/∂r]0, and the hardness parameter ϱ. Compute C1 = A1²/B1 and C2 = A2²/B2. Perform this for both nearest-neighbour (NN) and next-nearest-neighbour (NNN) overlap repulsion models.
- Evidence: `/app/outputs/fitted_parameters.csv`

### Step 2: Determine the many-body second derivative
- Role: process
- Action: Using the experimental pressure derivative of the bulk modulus (dK'/dp) and the fitted parameters from Step 1, determine the remaining unknown many-body second derivative [a²∂²f/∂r²]0 from the parametric expression relating dK'/dp to the model parameters. Compute for each compound and both NN and NNN models.
- Evidence: `/app/outputs/second_derivative.csv`

### Step 3: Calculate third-order elastic constants
- Role: scored (load-bearing)
- Action: Using the complete set of model parameters (including the second derivative from Step 2), compute all six third-order elastic constants (C111, C112, C166, C123, C144, C456) for CsCl, CsBr, and CsI with both NN and NNN overlap repulsion. Express values in units of 10^12 dyn/cm².
- Output file: `/app/outputs/toe_constants.csv`
- Format: csv
- Contract: compound (CsCl, CsBr, CsI), model (NN, NNN), C111, C112, C166, C123, C144, C456 (all numeric)
- Scoring: scored by hidden verifier

### Step 4: Calculate pressure derivatives dC44'/dp and dS'/dp
- Role: scored
- Action: Using the model parameters, compute the pressure derivatives dC44'/dp and dS'/dp (dimensionless) for each compound and both NN and NNN models.
- Output file: `/app/outputs/pressure_derivatives.csv`
- Format: csv
- Contract: compound (CsCl, CsBr, CsI), model (NN, NNN), dC44'_dp, dS'_dp (numeric)
- Scoring: scored by hidden verifier

### Step 5: Calculate linear combinations of TOE constants
- Role: scored
- Action: From the computed TOE constants, calculate the linear combinations C111+2C112, C123+2C112, and C144+2C166 for each compound and model, in units of 10^12 dyn/cm².
- Output file: `/app/outputs/linear_combinations.csv`
- Format: csv
- Contract: compound (CsCl, CsBr, CsI), model (NN, NNN), C111+2C112, C123+2C112, C144+2C166 (all numeric)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/toe_constants.csv`
- `/app/outputs/pressure_derivatives.csv`
- `/app/outputs/linear_combinations.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### toe_constants.csv
- path: `/app/outputs/toe_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Third-order elastic constants for CsCl, CsBr, CsI under NN and NNN repulsion models, to be compared against the paper-reported values with appropriate tolerances.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `compound`, `model`, `C111`, `C112`, `C166`, `C123`, `C144`, `C456`
  - `units`:
    - `C111`: 10^12 dyn/cm^2
    - `C112`: 10^12 dyn/cm^2
    - `C166`: 10^12 dyn/cm^2
    - `C123`: 10^12 dyn/cm^2
    - `C144`: 10^12 dyn/cm^2
    - `C456`: 10^12 dyn/cm^2

### pressure_derivatives.csv
- path: `/app/outputs/pressure_derivatives.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Pressure derivatives of the second-order elastic constants, compared against paper-reported values.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `compound`, `model`, `dC44'_dp`, `dS'_dp`
  - `units`:
    - `dC44'_dp`: dimensionless
    - `dS'_dp`: dimensionless

### linear_combinations.csv
- path: `/app/outputs/linear_combinations.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Linear combinations of third-order elastic constants, compared against paper-reported values.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `compound`, `model`, `C111+2C112`, `C123+2C112`, `C144+2C166`
  - `units`:
    - `C111+2C112`: 10^12 dyn/cm^2
    - `C123+2C112`: 10^12 dyn/cm^2
    - `C144+2C166`: 10^12 dyn/cm^2

Notes: All output values must be computed from the fitted potential model and experimental inputs, not copied from the literature. The hidden grading will compare the agent's values against the paper's reported results using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "toe_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "compound",
          "model",
          "C111",
          "C112",
          "C166",
          "C123",
          "C144",
          "C456"
        ],
        "units": {
          "C111": "10^12 dyn/cm^2",
          "C112": "10^12 dyn/cm^2",
          "C166": "10^12 dyn/cm^2",
          "C123": "10^12 dyn/cm^2",
          "C144": "10^12 dyn/cm^2",
          "C456": "10^12 dyn/cm^2"
        }
      },
      "description": "Third-order elastic constants for CsCl, CsBr, CsI under NN and NNN repulsion models, to be compared against the paper-reported values with appropriate tolerances."
    },
    {
      "file": "pressure_derivatives.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "compound",
          "model",
          "dC44'_dp",
          "dS'_dp"
        ],
        "units": {
          "dC44'_dp": "dimensionless",
          "dS'_dp": "dimensionless"
        }
      },
      "description": "Pressure derivatives of the second-order elastic constants, compared against paper-reported values."
    },
    {
      "file": "linear_combinations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "compound",
          "model",
          "C111+2C112",
          "C123+2C112",
          "C144+2C166"
        ],
        "units": {
          "C111+2C112": "10^12 dyn/cm^2",
          "C123+2C112": "10^12 dyn/cm^2",
          "C144+2C166": "10^12 dyn/cm^2"
        }
      },
      "description": "Linear combinations of third-order elastic constants, compared against paper-reported values."
    }
  ],
  "notes": "All output values must be computed from the fitted potential model and experimental inputs, not copied from the literature. The hidden grading will compare the agent's values against the paper's reported results using appropriate tolerances."
}
```

## How you are scored
A hidden verifier reads your produced CSV files and compares each numeric value against a set of reference values using appropriate absolute and relative tolerances. The per-file scores are combined into a final score in [0,1]. Only the three scored artifacts (toe_constants.csv, pressure_derivatives.csv, linear_combinations.csv) contribute to your reward; the intermediate process outputs serve as evidence that the required workflow was followed but are not scored directly. You do not need to know the reference values or the tolerances; implement the method accurately and the correct numbers will follow.
