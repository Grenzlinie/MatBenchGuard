# Modified Halpin-Tsai Model Prediction for CNT-Reinforced Nanocomposites

## Problem background
Carbon nanotube (CNT)-reinforced polymer nanocomposites are promising materials with significantly enhanced mechanical properties compared to pure polymers. Micromechanical models are used to predict the effective elastic modulus and tensile strength as functions of constituent properties and microstructural parameters. The Halpin-Tsai model is a widely used analytical approach, but it often overpredicts experimental data when CNTs are not perfectly aligned, straight, or uniformly dispersed. This work introduces a modified Halpin-Tsai model that incorporates three efficiency factors: random three-dimensional orientation, waviness (non-straight shape), and agglomeration of CNTs. The target is to compute the predicted elastic modulus (E) and tensile strength (S) of the CNT/epoxy nanocomposite for a range of CNT volume fractions using the modified equations and the given material parameters.

## Approach
The modified Halpin-Tsai model expresses both the composite elastic modulus (E) and tensile strength (S) using similar forms. For a given CNT volume fraction V_CNT, the predictions are computed as:

E = Em * (1 + 2*R*delta_E * V_CNT) / (1 - delta_E * V_CNT)

S = Sm * (1 + 2*R*delta_S * V_CNT) / (1 - delta_S * V_CNT)

where R = L_CNT / d_CNT is the CNT aspect ratio. The terms delta_E and delta_S incorporate the material moduli/strengths and the efficiency factors:

delta_E = ( (f_R * f_W * f_A * (E_CNT / Em)) - 1 ) / ( (f_R * f_W * f_A * (E_CNT / Em)) + 2*R )

delta_S = ( (f_R * f_W * f_A * (S_CNT / Em)) - 1 ) / ( (f_R * f_W * f_A * (S_CNT / Em)) + 2*R )

Here:
- Em = matrix elastic modulus (3.11 GPa)
- E_CNT = CNT elastic modulus (800 GPa)
- Sm = matrix tensile strength (64.51 MPa)
- S_CNT = CNT tensile strength (18 GPa)
- L_CNT = CNT length (2 μm); d_CNT = CNT diameter (30 nm)
- f_R = orientation factor for random 3D dispersion = 1/6
- f_W = waviness efficiency factor = 0.6
- f_A = agglomeration efficiency factor = exp(-alpha * (V_CNT^beta)), with alpha = 10, beta = 0.9

The model must be evaluated at CNT volume fractions V_CNT ranging from 0 to 0.07 in steps of 0.002.

## Reproduction target
Implement the modified Halpin-Tsai model using the provided material parameters and efficiency factors. Compute the elastic modulus (GPa) and tensile strength (MPa) for CNT volume fractions V_CNT from 0.0 to 0.07 in increments of 0.002. Write the results to a CSV file named `predictions.csv` with exactly three columns: `V_CNT`, `E_modulus (GPa)`, and `Tensile_strength (MPa)`. Each row corresponds to one volume fraction; the file should contain 36 data rows (including V_CNT=0 and V_CNT=0.07).

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Compute predicted elastic modulus and tensile strength
- Role: scored (load-bearing)
- Action: Implement the modified Halpin-Tsai micromechanical model incorporating orientation, waviness, and agglomeration efficiency factors. Use the given material parameters (Em=3.11 GPa, ECNT=800 GPa, Sm=64.51 MPa, SCNT=18 GPa, LCNT=2 µm, dCNT=30 nm, fR=1/6, fW=0.6, α=10, β=0.9). Compute the elastic modulus (GPa) and tensile strength (MPa) for CNT volume fractions V_CNT from 0 to 0.07 in steps of 0.002. Write a CSV file with columns V_CNT, E_modulus (GPa), Tensile_strength (MPa).
- Output file: `/app/outputs/predictions.csv`
- Format: csv
- Contract: CSV with header: V_CNT,E_modulus (GPa),Tensile_strength (MPa). V_CNT is dimensionless volume fraction (0.0, 0.002, ..., 0.07). E_modulus in GPa, Tensile_strength in MPa. Exactly 36 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions.csv
- path: `/app/outputs/predictions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file with three columns containing the computed elastic modulus and tensile strength for each CNT volume fraction. The checker recomputes the same analytical model and compares row-wise values.
- schema:
  - `type`: table
  - `required_columns`: `V_CNT`, `E_modulus (GPa)`, `Tensile_strength (MPa)`
  - `units`:
    - `V_CNT`: dimensionless
    - `E_modulus (GPa)`: GPa
    - `Tensile_strength (MPa)`: MPa

Notes: The model uses deterministic analytical expressions; no randomness. The checker will recompute the expected values using the same formulas and parameters, comparing each cell with an absolute tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "V_CNT",
          "E_modulus (GPa)",
          "Tensile_strength (MPa)"
        ],
        "units": {
          "V_CNT": "dimensionless",
          "E_modulus (GPa)": "GPa",
          "Tensile_strength (MPa)": "MPa"
        }
      },
      "description": "CSV file with three columns containing the computed elastic modulus and tensile strength for each CNT volume fraction. The checker recomputes the same analytical model and compares row-wise values."
    }
  ],
  "notes": "The model uses deterministic analytical expressions; no randomness. The checker will recompute the expected values using the same formulas and parameters, comparing each cell with an absolute tolerance."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently recomputes the expected elastic modulus and tensile strength for each CNT volume fraction using the same model equations and parameters. The verifier compares your `predictions.csv` against these expected values. Full credit is awarded if your predictions are in close agreement with the true computed values; credit decreases progressively as the deviation increases. The final reward is based solely on the correctness of predictions.csv.
