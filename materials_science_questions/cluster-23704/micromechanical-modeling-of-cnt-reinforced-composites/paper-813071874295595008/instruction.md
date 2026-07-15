# Tensile strength of CNT/polymer nanocomposites: Pukanszky model with network effects

## Problem background
Polymer/CNT nanocomposites can achieve enhanced tensile strength through the formation of interphase regions around the nanoparticles and the development of a percolating filler network. The Pukanszky model is a well-known framework for predicting tensile strength of filler-reinforced composites; it expresses relative strength as an exponential function of filler volume fraction with a parameter B that reflects the stress transfer efficiency. This work extends the Pukanszky model by decomposing the B parameter into an interphase contribution (B_I) and a network contribution (B_N), linking B_N to network density, network strength, and percolation threshold. The extension provides a way to quantify the roles of filler network properties on tensile strength.

## Approach
Implement the extended Pukanszky model. For the interphase contribution, compute a theoretical maximum B (B_max) based on CNT radius and matrix strength, using relationships that connect specific surface area to interphase thickness and strength. For the network contribution, define B_N in terms of aspect ratio, network density, and network strength; alternatively, relate B_N to percolation threshold and network strength. Fit the model to experimental relative tensile strength vs. filler volume fraction data from four published nanocomposites to obtain B values. For systems where the fitted B exceeds B_max, attribute the excess to the network contribution and set B_N = B - B_max; for others, assume equal contributions B_I = B_N = B/2. Then, perform parametric sweeps to evaluate how B_N and relative strength depend on aspect ratio, network density, percolation threshold, and network strength at specified fixed conditions.

## Reproduction target
Using the extracted data, fit the Pukanszky model to obtain B parameters for chitosan/MWCNT, polysilsesquioxane/MWCNT, PVA/MWCNT, and PET/MWCNT nanocomposites, and write the fitted B, B_max, B_I, B_N to a JSON file. Then, compute parametric sweeps to produce two CSV files: one for B_N and relative strength as functions of aspect ratio (alpha) and network density (N) at fixed filler fraction, matrix strength, and network strength; and one for B_N and relative strength as functions of percolation threshold (phi_p) and network strength (sigma_N) at fixed filler fraction, matrix strength, and network density. The target is to produce these artifacts with correct values and trends.

## Assets

- Tensile strength data for chitosan/MWCNT nanocomposites (Liu et al. 2009): https://doi.org/10.1016/j.carbpol.2008.10.031
- Tensile strength data for polysilsesquioxane/MWCNT nanocomposites (Yuen et al. 2008): https://doi.org/10.1002/app.28301
- Tensile strength data for PVA/MWCNT nanocomposites (Mi et al. 2007): https://doi.org/10.1016/j.compositesa.2007.04.003
- Tensile strength data for PET/MWCNT nanocomposites (Santoro et al. 2010): https://doi.org/10.1002/mame.201000103

## Workflow steps

### Step 1: Prepare experimental tensile strength data
- Role: process
- Action: Extract the filler volume fraction (phi_f) and relative tensile strength (sigma_R) from the four reference papers (chitosan/MWCNT, polysilsesquioxane/MWCNT, PVA/MWCNT, PET/MWCNT) into structured tables for model fitting.
- Evidence: `/app/outputs/data_extraction_log.txt`

### Step 2: Fit Pukanszky model and compute B parameters
- Role: scored (load-bearing)
- Action: Implement the Pukanszky model. For chitosan/MWCNT and polysilsesquioxane/MWCNT, compute B_max using the known formula with CNT radius R=15 nm and matrix strengths (69.1 MPa and 75 MPa, respectively). Fit ln(sigma_Reduced) vs phi_f to obtain B via linear regression. Set B_I = B_max, B_N = B - B_max. For PVA/MWCNT and PET/MWCNT, fit B similarly and set B_I = B_N = B/2. Output all computed quantities as specified.
- Output file: `/app/outputs/fitted_B_parameters.json`
- Format: json
- Contract: JSON object with keys chitosan, polysilsesquioxane, PVA, PET. Each value is an object with numeric fields: B, B_max, B_I, B_N.
- Scoring: scored by hidden verifier

### Step 3: Parametric sweep of B_N and relative strength with aspect ratio and network density
- Role: scored
- Action: Using the derived expressions for B_N and sigma_R (with B_I=10), evaluate over a grid: aspect ratio alpha from 100 to 1000 step 100, network density N from 100 to 500 step 100. Fixed parameters: phi_f=0.02, sigma_m=40 MPa, sigma_N=40 GPa. Write CSV with columns alpha, N, B_N, sigma_R.
- Output file: `/app/outputs/parametric_sweep_alpha_N.csv`
- Format: csv
- Contract: CSV with columns: alpha (integer), N (integer), B_N (float), sigma_R (float). One row per (alpha, N) combination.
- Scoring: scored by hidden verifier

### Step 4: Parametric sweep of B_N and relative strength with percolation threshold and network strength
- Role: scored
- Action: Using the derived expressions for B_N and sigma_R (with B_I=10), evaluate over a grid: percolation threshold phi_p from 0.001 to 0.005 step 0.001, network strength sigma_N from 20 to 60 GPa step 10. Fixed parameters: phi_f=0.02, sigma_m=40 MPa, N=300. Write CSV with columns phi_p, sigma_N, B_N, sigma_R.
- Output file: `/app/outputs/parametric_sweep_phi_sigmaN.csv`
- Format: csv
- Contract: CSV with columns: phi_p (float), sigma_N (float), B_N (float), sigma_R (float). One row per (phi_p, sigma_N) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_B_parameters.json`
- `/app/outputs/parametric_sweep_alpha_N.csv`
- `/app/outputs/parametric_sweep_phi_sigmaN.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_B_parameters.json
- path: `/app/outputs/fitted_B_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted B parameters for the four experimental systems.
- schema:
  - `type`: object
  - `required`: `chitosan`, `polysilsesquioxane`, `PVA`, `PET`
  - `items`:
    - `type`: object
    - `required`: `B`, `B_max`, `B_I`, `B_N`
    - `properties`:
      - `B`: number
      - `B_max`: number
      - `B_I`: number
      - `B_N`: number

### parametric_sweep_alpha_N.csv
- path: `/app/outputs/parametric_sweep_alpha_N.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Parametric sweep of B_N and sigma_R vs aspect ratio and network density.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `N`, `B_N`, `sigma_R`
  - `columns`:
    - `alpha`: integer
    - `N`: integer
    - `B_N`: float
    - `sigma_R`: float

### parametric_sweep_phi_sigmaN.csv
- path: `/app/outputs/parametric_sweep_phi_sigmaN.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Parametric sweep of B_N and sigma_R vs percolation threshold and network strength.
- schema:
  - `type`: table
  - `required_columns`: `phi_p`, `sigma_N`, `B_N`, `sigma_R`
  - `columns`:
    - `phi_p`: float
    - `sigma_N`: float
    - `B_N`: float
    - `sigma_R`: float

Notes: Hidden checker compares agent-reported values to paper-reported reference values for B parameters and for B_N and sigma_R at specific grid points, with tolerances, and checks agreement with monotonic trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_B_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "chitosan",
          "polysilsesquioxane",
          "PVA",
          "PET"
        ],
        "items": {
          "type": "object",
          "required": [
            "B",
            "B_max",
            "B_I",
            "B_N"
          ],
          "properties": {
            "B": "number",
            "B_max": "number",
            "B_I": "number",
            "B_N": "number"
          }
        }
      },
      "description": "Fitted B parameters for the four experimental systems."
    },
    {
      "file": "parametric_sweep_alpha_N.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "N",
          "B_N",
          "sigma_R"
        ],
        "columns": {
          "alpha": "integer",
          "N": "integer",
          "B_N": "float",
          "sigma_R": "float"
        }
      },
      "description": "Parametric sweep of B_N and sigma_R vs aspect ratio and network density."
    },
    {
      "file": "parametric_sweep_phi_sigmaN.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi_p",
          "sigma_N",
          "B_N",
          "sigma_R"
        ],
        "columns": {
          "phi_p": "float",
          "sigma_N": "float",
          "B_N": "float",
          "sigma_R": "float"
        }
      },
      "description": "Parametric sweep of B_N and sigma_R vs percolation threshold and network strength."
    }
  ],
  "notes": "Hidden checker compares agent-reported values to paper-reported reference values for B parameters and for B_N and sigma_R at specific grid points, with tolerances, and checks agreement with monotonic trends."
}
```

## How you are scored
Each output artifact (fitted_B_parameters.json, parametric_sweep_alpha_N.csv, parametric_sweep_phi_sigmaN.csv) will be scored independently by a hidden verifier. The verifier compares your fitted B parameters to reference values and checks your sweep values at multiple grid points against expected values with tolerances. It also verifies that your computed data shows the correct monotonic dependencies: B_N and relative strength should increase with alpha and N, decrease with phi_p, and increase with sigma_N. The final reward is a weighted sum of these checks. Simply reporting a plausible value without running the required fitting and sweeps will not pass because the verifier evaluates many grid points and the expected dependencies.
