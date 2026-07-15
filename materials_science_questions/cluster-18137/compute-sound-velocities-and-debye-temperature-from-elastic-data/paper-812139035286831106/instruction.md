# Compute Heat Capacity and Deviations for Crystalline Polyethylene Using Continuum Models

## Problem background
The heat capacity of crystalline polymers at low temperatures is dominated by lattice vibrations. Continuum approximations such as the Debye and Tarasov models are often used, but their validity can be limited, especially when chain bending stiffness and anisotropy are significant. This task investigates the heat capacity of crystalline polyethylene, testing the Debye and Tarasov approximations and a refined continuum model that separately accounts for chain stretching and bending contributions. The target is to compute the constant-volume heat capacity c_V(T) for 100% crystalline polyethylene over 1–200 K from three models and compare their percentage deviations from published experimental data.

## Approach
Implement the three models using generalized Debye functions:
- Debye model: a single Debye temperature Θ3 = 260 K determined from the low-temperature T³ law.
- Tarasov model: fits two parameters Θ1 and Θ3 to the experimental c_V data via nonlinear least squares over the full temperature range.
- Extended model: incorporates separate stretching and bending contributions, each with its own Θ3 and Θ1 parameters. Use the fixed best-fit values: Θ3s=996.6 K, Θ1s=996.9 K, Θ3b=188.7 K, Θ1b=910.9 K.

Using the provided experimental c_V dataset for crystalline polyethylene, compute the theoretical c_V at every integer temperature T = 1,…,200 K for each model. For each model, calculate the absolute percentage deviation 100×(c_V_model − c_V_exp) / c_V_exp. The computations require integration of the Debye functions; use appropriate numerical libraries (numpy, scipy).

## Reproduction target
Compute the theoretical constant-volume heat capacity c_V(T) for integer temperatures 1–200 K using the three models (Debye, Tarasov, and the extended model with the given fixed parameters). For each model, compute the percentage deviation from the experimental c_V values. Write a single CSV file with columns: T (int, K), exp_cV (float, cal/mol·K), Debye_cV (float), Debye_dev_percent (float), Tarasov_cV (float), Tarasov_dev_percent (float), Modified_cV (float), Modified_dev_percent (float).

## Assets

- Experimental heat capacity of crystalline polyethylene (Wunderlich & Baur 1970)
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Load experimental heat capacity data
- Role: process
- Action: Read the provided CSV file containing temperature T (K) and experimental constant-volume heat capacity c_V (cal/mol·K) for 100% crystalline polyethylene. Verify the data covers the range 1–200 K.
- Evidence: none

### Step 2: Fit Tarasov model parameters
- Role: process
- Action: Implement the Tarasov heat capacity formula using generalized Debye functions D1 and D3. Fit the two parameters Θ1 and Θ3 to the experimental c_V data over the full 1–200 K range using nonlinear least squares. Record the optimal parameter values.
- Evidence: `/app/outputs/fitted_tarasov_params.json`

### Step 3: Compute heat capacity and deviations for all three models
- Role: scored (load-bearing)
- Action: For integer temperatures T = 1,2,...,200 K, compute: (1) c_V from the Debye model using Θ3 = 260 K, (2) c_V from the Tarasov model using the fitted Θ1 and Θ3 from the previous step, (3) c_V from the modified model using the parameters Θ3s=996.6 K, Θ1s=996.9 K, Θ3b=188.7 K, Θ1b=910.9 K. For each model compute the percentage deviation 100*(c_V_model - c_V_exp)/c_V_exp. Write all results to a single CSV file.
- Output file: `/app/outputs/step_01_heat_capacity_comparison.csv`
- Format: csv
- Contract: Columns: T (int, 1..200), exp_cV (float, cal/mol·K), Debye_cV (float), Debye_dev_percent (float), Tarasov_cV (float), Tarasov_dev_percent (float), Modified_cV (float), Modified_dev_percent (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_heat_capacity_comparison.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_heat_capacity_comparison.csv
- path: `/app/outputs/step_01_heat_capacity_comparison.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: The CSV contains the experimental c_V values and the computed c_Vs plus absolute percentage deviations for the Debye, Tarasov, and modified models over the temperature range 1–200 K.
- schema:
  - `type`: table
  - `required_columns`: `T`, `exp_cV`, `Debye_cV`, `Debye_dev_percent`, `Tarasov_cV`, `Tarasov_dev_percent`, `Modified_cV`, `Modified_dev_percent`
  - `units`:
    - `T`: K
    - `exp_cV`: cal/mol·K
    - `Debye_cV`: cal/mol·K
    - `Debye_dev_percent`: %
    - `Tarasov_cV`: cal/mol·K
    - `Tarasov_dev_percent`: %
    - `Modified_cV`: cal/mol·K
    - `Modified_dev_percent`: %

Notes: The checker will compare the reported deviation values (especially the modified model deviations) against hidden gold from the paper’s Table 2 using a threshold_or_better policy, and will also check structural relationships (e.g., that the modified model outperforms Debye and Tarasov).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_heat_capacity_comparison.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "exp_cV",
          "Debye_cV",
          "Debye_dev_percent",
          "Tarasov_cV",
          "Tarasov_dev_percent",
          "Modified_cV",
          "Modified_dev_percent"
        ],
        "units": {
          "T": "K",
          "exp_cV": "cal/mol·K",
          "Debye_cV": "cal/mol·K",
          "Debye_dev_percent": "%",
          "Tarasov_cV": "cal/mol·K",
          "Tarasov_dev_percent": "%",
          "Modified_cV": "cal/mol·K",
          "Modified_dev_percent": "%"
        }
      },
      "description": "The CSV contains the experimental c_V values and the computed c_Vs plus absolute percentage deviations for the Debye, Tarasov, and modified models over the temperature range 1–200 K."
    }
  ],
  "notes": "The checker will compare the reported deviation values (especially the modified model deviations) against hidden gold from the paper’s Table 2 using a threshold_or_better policy, and will also check structural relationships (e.g., that the modified model outperforms Debye and Tarasov)."
}
```

## How you are scored
A hidden verifier inspects your output CSV. It validates the file format and column structure, and checks that the computed deviations follow expected physical trends. The verifier compares your deviation values against independently derived reference values; a better match earns a higher score. Simply reporting numbers from the literature is not sufficient — the verifier expects you to compute the heat capacities from the models and the supplied experimental data.
