# Indentation Modulus Scaling Model for Aligned CNT Arrays

## Problem background
Aligned carbon nanotube (CNT) arrays are promising for next-generation materials due to their strong mechanical anisotropy. Nanoindentation experiments reveal that the effective indentation modulus of these arrays depends highly non-linearly on the CNT volume fraction as the inter-CNT spacing changes. A theoretical scaling model was developed to capture this behavior by relating the indentation modulus to the inter-CNT spacing and a minimum spacing parameter.

Your task is to compute the predicted indentation modulus from this scaling model for three CNT volume fractions using provided inter-CNT spacing values and a baseline modulus. The output will be evaluated against independently held reference criteria.

## Approach
The model assumes that the indentation modulus E at a given CNT volume fraction Vf is proportional to the square of a normalized spacing term:

Expected modulus = E_1% * ( (Gamma_1% - Gamma_min) / (Gamma(Vf) - Gamma_min) )^2

where:
- E_1% is the measured indentation modulus at Vf=1% (provided as 4 MPa).
- Gamma_1% is the inter-CNT spacing at Vf=1% (78.0 nm).
- Gamma(Vf) is the inter-CNT spacing at the target volume fraction (given for 10% and 20% below).
- Gamma_min is the minimum inter-CNT spacing, taken as a fixed constant of 5 nm.

You will implement this formula and compute the predicted modulus E for Vf = 1%, 10%, and 20% using the inter-CNT spacings:
- At Vf =  1%: Gamma = 78.0 nm
- At Vf = 10%: Gamma = 18.5 nm
- At Vf = 20%: Gamma = 10.3 nm

No external data download or complex fitting is required; only the provided parameter values and the simple algebraic formula.

## Reproduction target
Produce a CSV file named `predicted_moduli.csv` with two columns:
- Vf (percent): the three volume fractions 1, 10, 20.
- predicted_E (MPa): the computed indentation modulus from the scaling law.

Use Gamma_min = 5 nm and the baseline E_1% = 4 MPa. The three Gamma values are listed in the Approach. The output should contain one row for each volume fraction, with floating-point values. The predicted results will be compared to independently held reference criteria by a hidden verifier.

## Assets
No external datasets, models, or tools are required. The task can be completed with only standard Python libraries (e.g., `math`, `csv`). All required numerical parameters are provided in the Approach section above.

## Workflow steps

### Step 1: Compute predicted indentation modulus from scaling model
- Role: scored (load-bearing)
- Action: Implement the provided scaling law for indentation modulus as a function of CNT volume fraction, using the given inter-CNT spacing values and baseline modulus, and compute the predicted modulus E for Vf = 1%, 10%, 20% at a minimum inter-CNT spacing of 5 nm.
- Output file: `/app/outputs/predicted_moduli.csv`
- Format: csv
- Contract: CSV with header 'Vf' (percent) and 'predicted_E' (MPa). One row for each volume fraction: 1, 10, 20.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_moduli.csv
- path: `/app/outputs/predicted_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Predicted indentation modulus for CNT volume fractions 1%, 10%, 20% from the scaling model.
- schema:
  - `type`: table
  - `required_columns`: `Vf`, `predicted_E`
  - `units`:
    - `Vf`: percent
    - `predicted_E`: MPa

Notes: The model parameters (inter-CNT spacing values and baseline modulus at Vf=1%) are provided in the instruction. The agent must use the scaling law with a minimum inter-CNT spacing of 5 nm to compute the predicted indentation modulus.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Vf",
          "predicted_E"
        ],
        "units": {
          "Vf": "percent",
          "predicted_E": "MPa"
        }
      },
      "description": "Predicted indentation modulus for CNT volume fractions 1%, 10%, 20% from the scaling model."
    }
  ],
  "notes": "The model parameters (inter-CNT spacing values and baseline modulus at Vf=1%) are provided in the instruction. The agent must use the scaling law with a minimum inter-CNT spacing of 5 nm to compute the predicted indentation modulus."
}
```

## How you are scored
A hidden verifier will independently score the artifact you write. It will read `predicted_moduli.csv`, extract the three predicted values, and compare them against pre-defined reference criteria. Each predicted value must be derived from the provided scaling law and parameters; it is not enough to report a number without the correct computation. The final reward is a weighted combination of the scores from each workflow stage. Do not fabricate values; the checker expects results that follow the specified formula and inputs.
