# Power-law scaling between loss phase angle and configurational distance in a binary Lennard-Jones glass former

## Problem background
Glassy materials are archetypal non‑equilibrium solids. Their mechanical dissipation—how much energy they lose under oscillatory deformation—depends sensitively on preparation history (cooling rate, aging, strain amplitude, and more). A long‑standing challenge is whether a single structural order parameter can unify this seemingly disparate, history‑dependent behaviour. This task addresses that question using the configurational distance ISD_min, a metric that quantifies the minimum displacement between inherent structures while respecting particle indistinguishability. The goal is to compute the relationship between the loss phase angle δ (a measure of dissipation) and ISD_min for the Kob‑Andersen binary Lennard‑Jones glass former across several non‑equilibrium protocols, both above and below the ideal glass transition temperature T0.

## Approach
We use molecular dynamics simulations of dynamic mechanical spectra (MD‑DMS): a sinusoidal shear strain is applied, and the stress response is recorded. The phase lag δ between stress and strain, together with the storage and loss moduli, characterise dissipation. ISD_min is computed from particle trajectories by solving the optimal assignment problem (Hungarian algorithm) between time‑separated configurations; it captures inherent structural changes independent of particle labels. First, equilibrium runs at multiple temperatures determine T0 by fitting the α‑relaxation times to a Vogel‑Fulcher‑Tammann (VFT) form. Then, non‑equilibrium MD‑DMS simulations are performed under at least two distinct preparation protocols (e.g., different cooling rates or strain amplitudes) at temperatures spanning both sides of T0. For each run, δ and ISD_min are extracted. The compiled data are used to fit a power‑law model δ ∝ (ISD_min)^b for temperatures above T0.

## Reproduction target
Produce two artifacts:
1. `data.csv` – a table of raw (condition, temperature, ISD_min, δ) points. At least 10 rows are required, with at least two distinct condition labels, and temperatures must include values both above and below the fitted T0.
2. `fit_results.json` – the exponent `b` and the R² of the power‑law fit restricted to the points where temperature > T0.

The analysis must use the Kob‑Andersen binary Lennard‑Jones potential (80% A / 20% B, density 1.2) and the Hungarian algorithm for ISD_min. The T0 value must be obtained from independent equilibrium MD‑DMS runs as described in Step 1.

## Assets

- LAMMPS: https://lammps.sandia.gov
- SciPy: scipy
- NumPy: numpy
- Kob-Andersen binary Lennard-Jones interaction parameters

## Workflow steps

### Step 1: Determine ideal glass transition temperature T0 from equilibrium MD-DMS
- Role: process
- Action: Run equilibrium MD-DMS simulations of the Kob-Andersen binary Lennard-Jones mixture at several temperatures above the glass transition. Extract the α-relaxation time τ_α from the peak of the loss modulus. Fit the τ_α(T) data to a Vogel-Fulcher-Tammann (VFT) function τ = τ0 exp(D T0 / (T – T0)) to obtain the divergent temperature T0.
- Evidence: `/app/outputs/t0_fit_results.json`

### Step 2: Perform non-equilibrium MD-DMS across preparation protocols
- Role: process
- Action: Run MD-DMS simulations for the Kob-Andersen model under at least two distinct non-equilibrium conditions (e.g., different cooling rates or strain amplitudes). For each condition, simulate at multiple temperatures spanning both above and below the T0 obtained in step_01. Collect the raw stress response and particle position trajectories.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 3: Compute δ and ISD_min and compile data.csv
- Role: scored (load-bearing)
- Action: For each non-equilibrium simulation from step_02, extract the loss phase angle δ by fitting the stress signal to a sinusoidal function, and compute the inherent structural minimum displacement ISD_min using the Hungarian algorithm on particle positions. Assemble all (condition, temperature, ISD_min, δ) data points into a CSV file. The file must contain at least 10 rows and cover at least two distinct condition labels, with temperatures both above and below T0.
- Output file: `/app/outputs/data.csv`
- Format: csv
- Contract: CSV with columns: condition (string), temperature (float, LJ units), ISD_min (float, LJ units), delta (float, radians). No missing values. At least 10 rows; at least 2 unique condition values.
- Scoring: scored by hidden verifier

### Step 4: Fit power-law relation for T > T0
- Role: scored
- Action: Read data.csv, filter rows where temperature > T0 (the value determined in step_01). Fit the power-law model δ = a * ISD_min^b using nonlinear least squares (log‑log linear regression is acceptable). Write the fitted exponent b and the R² of the fit to fit_results.json.
- Output file: `/app/outputs/fit_results.json`
- Format: json
- Contract: JSON object with keys: exponent_b (float, dimensionless), R_squared (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/data.csv`
- `/app/outputs/fit_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### data.csv
- path: `/app/outputs/data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw dissipation data: loss phase angle δ versus configurational distance ISD_min for multiple conditions and temperatures.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `temperature`, `ISD_min`, `delta`
  - `columns`:
    - `condition`:
      - `type`: string
      - `unit`: 
    - `temperature`:
      - `type`: float
      - `unit`: Lennard-Jones units
    - `ISD_min`:
      - `type`: float
      - `unit`: Lennard-Jones units
    - `delta`:
      - `type`: float
      - `unit`: radians
  - `notes`: At least 10 rows; at least 2 distinct condition values.

### fit_results.json
- path: `/app/outputs/fit_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Fitted power-law exponent and quality of the δ ∝ ISD_min^b relation for temperatures above T0.
- schema:
  - `type`: object
  - `required_fields`: `exponent_b`, `R_squared`
  - `fields`:
    - `exponent_b`:
      - `type`: number
      - `unit`: dimensionless
    - `R_squared`:
      - `type`: number
      - `unit`: dimensionless

Notes: The checker will recompute the power-law exponent from data.csv using a log‑log linear regression on the subset of points with temperature > T0 (hidden threshold). It will then compare the recomputed exponent to the paper‑reported reference value. The fit_results.json exponent_b must be consistent with the recomputed value (within a narrow tolerance) to earn a consistency bonus.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "temperature",
          "ISD_min",
          "delta"
        ],
        "columns": {
          "condition": {
            "type": "string",
            "unit": ""
          },
          "temperature": {
            "type": "float",
            "unit": "Lennard-Jones units"
          },
          "ISD_min": {
            "type": "float",
            "unit": "Lennard-Jones units"
          },
          "delta": {
            "type": "float",
            "unit": "radians"
          }
        },
        "notes": "At least 10 rows; at least 2 distinct condition values."
      },
      "description": "Raw dissipation data: loss phase angle δ versus configurational distance ISD_min for multiple conditions and temperatures."
    },
    {
      "file": "fit_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required_fields": [
          "exponent_b",
          "R_squared"
        ],
        "fields": {
          "exponent_b": {
            "type": "number",
            "unit": "dimensionless"
          },
          "R_squared": {
            "type": "number",
            "unit": "dimensionless"
          }
        }
      },
      "description": "Fitted power-law exponent and quality of the δ ∝ ISD_min^b relation for temperatures above T0."
    }
  ],
  "notes": "The checker will recompute the power-law exponent from data.csv using a log‑log linear regression on the subset of points with temperature > T0 (hidden threshold). It will then compare the recomputed exponent to the paper‑reported reference value. The fit_results.json exponent_b must be consistent with the recomputed value (within a narrow tolerance) to earn a consistency bonus."
}
```

## How you are scored
A hidden verifier scores the submission by recomputing the power‑law exponent from the `data.csv` file. It filters rows with temperature > T0 (with T0 fixed to a hidden value derived from the paper) and performs a log‑log linear regression of δ versus ISD_min. The recomputed exponent is compared against a hidden reference. The verifier also checks that `fit_results.json` contains an exponent consistent with the recomputed value and that the reported R² is plausible. No credit is given for simply reporting the paper's numbers; the raw data must trace back to simulations run under the specified protocol.
