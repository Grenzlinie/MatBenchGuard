# Adhesive Joint Fracture Energy Prediction using In-Situ Failure Model

## Problem background
Adhesive bonds are used extensively to join structural components, but the fracture behaviour of the adhesive layer often limits joint performance. A predictive understanding of how bulk adhesive properties translate into the fracture energy of a bonded joint is central to designing reliable adhesive joints. The in‑situ failure model links the adhesive joint fracture energy, G_IC(joint), to three measurable bulk properties: yield stress σ_y, Young's modulus E, and bulk fracture energy G_IC(bulk). The central open question is whether the model, after its parameters are calibrated, can accurately reproduce experimentally observed joint fracture energies for a specific elastomer‑epoxy adhesive system across a range of temperatures.

## Approach
The model is built on a plastic‑zone concept. It approximates the crack‑tip stress distribution as a piecewise power‑law decay, leading to a parametric relation that expresses G_IC(joint) as G_IC(joint) = M (σ_y²/E)^(1−m) G_IC(bulk)^m. The exponent m and the factor M capture the stress‑regime and are expected to differ between high‑temperature (T > 0 °C) and low‑temperature (T ≤ 0 °C) conditions. To apply the model, we use published experimental data from Bascom & Cottington (1976) for an elastomer‑epoxy adhesive at six temperatures: 50, 37, 25, 0, −20, and −40 °C. The data comprise σ_y, E, G_IC(bulk), and the measured G_IC(joint). The reproduction proceeds in three stages: (1) compile these experimental quantities; (2) transform the model to a log‑log linear form and, for each temperature group, perform ordinary least‑squares regression to determine m and M; (3) evaluate the fitted model at each temperature to obtain predicted joint fracture energies. The comparison between the predicted and the independently measured G_IC(joint) reveals how well the model captures the temperature dependence of adhesive joint failure.

## Reproduction target
Produce a set of predicted adhesive joint fracture energies (in kJ/m²) for the six temperature conditions (50, 37, 25, 0, −20, −40 °C) of the elastomer‑epoxy system studied by Bascom & Cottington. First, fit the model parameters m and M for the high‑temperature (T > 0 °C) and low‑temperature (T ≤ 0 °C) subsets using the experimental data. Then, evaluate the fitted model to compute the predicted G_IC(joint) for each temperature. The fitted parameters are written to fitted_parameters.json, and the predicted values are output to predicted_GIC_joint.csv, with one row per temperature.

## Assets

- Bascom & Cottington (1976) bulk adhesive properties and joint fracture data: 10.1080/00218467608075081
- NumPy: numpy
- Pandas: pandas

## Workflow steps

### Step 1: Compile experimental data
- Role: process
- Action: Obtain the measured bulk adhesive properties (yield stress σ_y, Young's modulus E, bulk fracture energy G_IC(bulk)) and the measured adhesive joint fracture energy G_IC(joint) at six temperatures (50, 37, 25, 0, -20, -40 °C) from Bascom & Cottington (1976) Table I. Tabulate the data for subsequent fitting.
- Evidence: `/app/outputs/compiled_data.csv`

### Step 2: Fit in-situ failure model parameters
- Role: scored
- Action: For the compiled data, separate into high-temperature (T > 0°C) and low-temperature (T ≤ 0°C) groups. Transform the model to log-log form: log(G_IC(joint)/G_IC(bulk)) = log M + (1-m) log(σ_y^2/(E G_IC(bulk))). Perform ordinary least-squares linear regression on each group to obtain the slope and intercept, from which m and M are derived. Write the fitted parameters to fitted_parameters.json.
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: JSON object with keys: high_temp_m (float), high_temp_M (float), low_temp_m (float), low_temp_M (float). Values are dimensionless or in consistent units derived from the data.
- Scoring: scored by hidden verifier

### Step 3: Compute predicted joint fracture energy
- Role: scored (load-bearing)
- Action: Using the fitted parameters from fitted_parameters.json and the bulk properties for each temperature, compute the predicted adhesive joint fracture energy via G_IC(joint) = M * (σ_y^2/E)^(1-m) * G_IC(bulk)^m. Write the results (one row per temperature) to predicted_GIC_joint.csv.
- Output file: `/app/outputs/predicted_GIC_joint.csv`
- Format: csv
- Contract: Columns: temperature_C (integer), predicted_GIC_joint_kJm2 (float). One row per temperature.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.json`
- `/app/outputs/predicted_GIC_joint.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted model parameters for high- and low-temperature regimes. The checker compares each parameter to the paper's approximate values with a tolerance.
- schema:
  - `type`: object
  - `required_keys`: `high_temp_m`, `high_temp_M`, `low_temp_m`, `low_temp_M`
  - `keys`:
    - `high_temp_m`:
      - `type`: number
    - `high_temp_M`:
      - `type`: number
    - `low_temp_m`:
      - `type`: number
    - `low_temp_M`:
      - `type`: number

### predicted_GIC_joint.csv
- path: `/app/outputs/predicted_GIC_joint.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Predicted adhesive joint fracture energy (kJ/m²) computed from the fitted model. The checker compares each predicted value to the hidden measured G_IC(joint) using a relative or absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `predicted_GIC_joint_kJm2`
  - `columns`:
    - `temperature_C`:
      - `type`: integer
    - `predicted_GIC_joint_kJm2`:
      - `type`: float
  - `row_count`: 6

Notes: The fitted parameters serve as consistency evidence. The main load-bearing scored artifact is the predicted G_IC(joint). Both artifacts are verified against hidden gold values derived from the paper.

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
        "required_keys": [
          "high_temp_m",
          "high_temp_M",
          "low_temp_m",
          "low_temp_M"
        ],
        "keys": {
          "high_temp_m": {
            "type": "number"
          },
          "high_temp_M": {
            "type": "number"
          },
          "low_temp_m": {
            "type": "number"
          },
          "low_temp_M": {
            "type": "number"
          }
        }
      },
      "description": "Fitted model parameters for high- and low-temperature regimes. The checker compares each parameter to the paper's approximate values with a tolerance."
    },
    {
      "file": "predicted_GIC_joint.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_C",
          "predicted_GIC_joint_kJm2"
        ],
        "columns": {
          "temperature_C": {
            "type": "integer"
          },
          "predicted_GIC_joint_kJm2": {
            "type": "float"
          }
        },
        "row_count": 6
      },
      "description": "Predicted adhesive joint fracture energy (kJ/m²) computed from the fitted model. The checker compares each predicted value to the hidden measured G_IC(joint) using a relative or absolute tolerance."
    }
  ],
  "notes": "The fitted parameters serve as consistency evidence. The main load-bearing scored artifact is the predicted G_IC(joint). Both artifacts are verified against hidden gold values derived from the paper."
}
```

## How you are scored
Your submission is evaluated by an automated verifier that holds hidden reference values (the gold‑standard measured G_IC(joint) and the expected fitted parameters). It reads fitted_parameters.json and predicted_GIC_joint.csv, checks that they contain the required fields, then compares your numbers against the hidden gold using undisclosed tolerances. Each scored artifact contributes a weighted fraction to a single reward in [0, 1]. Simply copying values from a publication is not sufficient; the verifier ensures that only an honest implementation of the described fitting and prediction workflow can produce results that match the hidden references within the required tolerance. The closer your outputs agree, the higher your score.
