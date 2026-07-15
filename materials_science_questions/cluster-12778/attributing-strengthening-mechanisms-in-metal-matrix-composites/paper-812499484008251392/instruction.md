# Reproducing Response Surface Optimization of FSP Parameters for Tensile Strength

## Problem background
The development of aluminium matrix composites reinforced with waste-derived collagen and ceramic particles via friction stir processing (FSP) offers a way to repurpose industrial waste while improving mechanical properties. The tensile strength of such a composite depends strongly on the FSP process parameters: number of tool passes, tool rotational speed, and transverse speed. A Box-Behnken experimental design can be used to explore this relationship, and a quadratic response surface model can be built to predict tensile strength as a function of these three factors. The computational challenge is to find the parameter combination that maximizes tensile strength and to quantify the resulting improvement over the base material.

## Approach
The approach is a three-stage computational pipeline. First, a second-order polynomial regression model (including all linear, quadratic, and two-way interaction terms) is fitted to the 17 experimentally measured tensile strengths using ordinary least squares. Second, the fitted model is used to search for the parameter values—with the number of tool passes limited to integer values 1, 2, or 3, rotational speed between 800 and 1000 rpm, and transverse speed between 15 and 25 mm/min—that maximize the predicted tensile strength. Third, the obtained predicted tensile strength is compared to the known experimental confirmation test result (162.89 MPa) to calculate the percentage deviation, and to the known base material tensile strength (135 MPa) to compute the percentage improvement.

## Reproduction target
Your objective is to compute the optimal FSP parameters and the associated performance metrics.

- Fit a quadratic regression model to the provided Box-Behnken design matrix (17 runs) with the three factors (number of tool passes, rotational speed, transverse speed) and measured tensile strengths.
- Using the fitted model, find the parameter combination (tool passes as an integer in {1,2,3}, rotational speed in [800,1000] rpm, transverse speed in [15,25] mm/min) that maximizes predicted tensile strength. Write the optimal parameters and the predicted maximum tensile strength to `/app/outputs/optimum_parameters.json`.
- Using the fixed experimental confirmation tensile strength (162.89 MPa) and base material tensile strength (135 MPa), compute the percentage deviation between the model prediction and the experimental result, and the percentage improvement of the composite over the base material. Write these metrics to `/app/outputs/model_comparison.json`.

## Assets

- NumPy: numpy
- SciPy: scipy

## Design matrix

The Box-Behnken design matrix (17 runs) is given below. Each row provides the three FSP parameters and the measured tensile strength.

| Number of tool pass | Rotational speed (rpm) | Transverse speed (mm/min) | Tensile strength (MPa) |
|---|---|---|---|
| 1 | 800 | 20 | 161.36 |
| 3 | 900 | 25 | 155.30 |
| 2 | 900 | 20 | 158.96 |
| 1 | 1000 | 20 | 165.80 |
| 3 | 1000 | 20 | 141.84 |
| 2 | 800 | 15 | 140.10 |
| 2 | 900 | 20 | 158.88 |
| 3 | 800 | 20 | 147.33 |
| 1 | 900 | 25 | 170.40 |
| 2 | 1000 | 15 | 135.56 |
| 2 | 800 | 25 | 154.64 |
| 2 | 900 | 20 | 158.80 |
| 2 | 900 | 20 | 159.04 |
| 1 | 900 | 15 | 155.00 |
| 2 | 1000 | 25 | 158.10 |
| 2 | 900 | 20 | 159.04 |
| 3 | 900 | 15 | 132.80 |

## Workflow steps

### Step 1: Fit Response Surface Model
- Role: process
- Action: Fit a second-order polynomial regression model to the experimental tensile strength data using the FSP parameters (number of tool passes, rotational speed, transverse speed) as predictor variables, including all linear, quadratic, and interaction terms. Use ordinary least squares. Save the fitted model coefficients as evidence.
- Evidence: `/app/outputs/model_coefficients.json`

### Step 2: Optimize FSP Parameters for Maximum Tensile Strength
- Role: scored (load-bearing)
- Action: Using the fitted quadratic model, determine the parameter combination (tool passes as integer in {1,2,3}, rotational speed in [800,1000] rpm, transverse speed in [15,25] mm/min) that maximizes predicted tensile strength. Write the optimal parameters and the predicted tensile strength to optimum_parameters.json.
- Output file: `/app/outputs/optimum_parameters.json`
- Format: json
- Contract: {"optimum_parameters": {"tool_passes": integer, "rotational_speed": float, "transverse_speed": float}, "predicted_tensile_strength": float}
- Scoring: scored by hidden verifier

### Step 3: Compute Model Comparison Metrics
- Role: scored
- Action: Using the predicted tensile strength from step_1 and the fixed experimental values: base material tensile strength = 135 MPa, confirmation experiment tensile strength = 162.89 MPa, compute deviation_percentage = (predicted_tensile_strength - 162.89) / predicted_tensile_strength * 100 and improvement_percentage = (162.89 - 135) / 135 * 100. Write the results to model_comparison.json.
- Output file: `/app/outputs/model_comparison.json`
- Format: json
- Contract: {"experimental_tensile_strength": 162.89, "predicted_tensile_strength": float, "deviation_percentage": float, "improvement_percentage": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimum_parameters.json`
- `/app/outputs/model_comparison.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimum_parameters.json
- path: `/app/outputs/optimum_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimal friction stir process parameters and the predicted tensile strength at those settings, to be compared against the paper's reported optimum.
- schema:
  - `type`: object
  - `required`:
    - `optimum_parameters`:
      - `tool_passes`: integer
      - `rotational_speed`: float
      - `transverse_speed`: float
    - `predicted_tensile_strength`: float
  - `units`:
    - `rotational_speed`: rpm
    - `transverse_speed`: mm/min
    - `predicted_tensile_strength`: MPa

### model_comparison.json
- path: `/app/outputs/model_comparison.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Comparison metrics: model deviation from experimental confirmation and composite improvement over base material.
- schema:
  - `type`: object
  - `required`:
    - `experimental_tensile_strength`: float
    - `predicted_tensile_strength`: float
    - `deviation_percentage`: float
    - `improvement_percentage`: float
  - `units`:
    - `experimental_tensile_strength`: MPa
    - `predicted_tensile_strength`: MPa
    - `deviation_percentage`: %
    - `improvement_percentage`: %

Notes: Hardness improvement is not included because there is no accompanying regression model for hardness. The task focuses solely on the tensile strength modeling and optimization.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimum_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "optimum_parameters": {
            "tool_passes": "integer",
            "rotational_speed": "float",
            "transverse_speed": "float"
          },
          "predicted_tensile_strength": "float"
        },
        "units": {
          "rotational_speed": "rpm",
          "transverse_speed": "mm/min",
          "predicted_tensile_strength": "MPa"
        }
      },
      "description": "Optimal friction stir process parameters and the predicted tensile strength at those settings, to be compared against the paper's reported optimum."
    },
    {
      "file": "model_comparison.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "experimental_tensile_strength": "float",
          "predicted_tensile_strength": "float",
          "deviation_percentage": "float",
          "improvement_percentage": "float"
        },
        "units": {
          "experimental_tensile_strength": "MPa",
          "predicted_tensile_strength": "MPa",
          "deviation_percentage": "%",
          "improvement_percentage": "%"
        }
      },
      "description": "Comparison metrics: model deviation from experimental confirmation and composite improvement over base material."
    }
  ],
  "notes": "Hardness improvement is not included because there is no accompanying regression model for hardness. The task focuses solely on the tensile strength modeling and optimization."
}
```

## How you are scored
A hidden verifier inspects each of the two scored output files independently. It checks whether your reported optimal parameters and predicted tensile strength fall within an acceptable range of the true optimum, and whether the deviation and improvement percentages computed from your predicted strength match expected values. The final reward (0 to 1) is a weighted sum of these checks, with the accurate determination of the optimal parameters and predicted strength carrying the greatest weight. Simply writing down the paper’s numbers without correct computation will not earn credit.
