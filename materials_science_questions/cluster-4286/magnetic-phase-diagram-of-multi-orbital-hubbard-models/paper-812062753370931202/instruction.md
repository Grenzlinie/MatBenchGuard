# Strong coupling expansion coefficients of the antiferromagnetic state in the twisted Hubbard model

## Problem background
In the strong coupling regime of N=4 super Yang-Mills theory, the anomalous dimensions of single-trace operators with zero SU(2) spin can be described by a twisted half-filled Hubbard model. For the highest-energy (antiferromagnetic) state at finite length L, the anomalous dimension Δ(g,L) admits an expansion at large coupling g:

  Δ(g,L)/L = a1 · g + a2 + δ_L / g + O(1/g²)

where a1 = √2 / (L sin(π/(2L))) and a2 = 3/4 are known exactly. The subleading coefficient δ_L encodes the next-to-leading correction and must be extracted numerically from the Bethe Ansatz solution of the Hubbard model, known as the Lieb‑Wu equations. Computing δ_L for various L and extrapolating to the thermodynamic limit L→∞ tests the consistency with an independently known analytic constant, making it a clear, verifiable reproduction target.

## Approach
The Lieb‑Wu equations for the twisted half-filled Hubbard model relate the charge rapidities q_n and spin rapidities u_k via coupled nonlinear equations. For the antiferromagnetic state with length L = 4p (p integer), the required Bethe quantum numbers are:
- I_n = 0, 1, …, L−1 for the charge sector,
- J_k = −(2p−1)/2, …, (2p−1)/2 for the spin sector.
The twist parameter is φ = π/(2L).

To extract δ_L we solve these equations numerically at a sequence of large coupling values (g = 10, 11, …, 20) using a robust root‑finding method. From the converged Bethe roots we compute the energy Δ(g,L). Fitting Δ(g,L)/L to the strong‑coupling form a1·g + a2 + δ_L/g yields δ_L for each L. Repeating this for L = 8,12,16,20,24,28,32 gives a series that can be extrapolated to L→∞ using a simple polynomial or rational fit; the extrapolated value can be compared against the known analytic prediction from the continuum limit. Separately, the leading coefficient a1 and constant term a2 are computed from the analytical expressions to verify the exact terms of the expansion.

## Reproduction target
Produce two scored artifacts:

1. **delta_L_values.csv** – containing the fitted δ_L for L = 8,12,16,20,24,28,32 and the extrapolated infinite‑L limit (denoted as L=inf). The δ_L values must be computed to high precision; the verifier compares them against reference values using a tight absolute tolerance.

2. **leading_constant_report.json** – verifying that for each L the leading coefficient a1 = √2 / (L sin(π/(2L))) and the constant term a2 = 3/4 are correctly reproduced. The verifier checks that every a1 and a2 matches the exact formula within machine precision.

Reporting numbers from memory or external sources is not sufficient; you must run the full computational workflow described in the steps.

## Assets

- NumPy and SciPy: numpy scipy

## Workflow steps

### Step 1: Solve Lieb-Wu equations for antiferromagnetic state
- Role: process
- Action: For L = 8, 12, 16, 20, 24, 28, 32, set up the Lieb-Wu equations for the half-filled twisted Hubbard model with twist φ = π/(2L) and Bethe quantum numbers I_n = 0,1,…,L-1 for charge rapidities and J_k = -(2p-1)/2,…, (2p-1)/2 for spin rapidities (L=4p). Solve the coupled nonlinear equations iteratively at coupling values g = 10, 11, …, 20 using a root-finding method until convergence. Compute the energy Δ(g,L) from the converged roots. Save the raw energies as a CSV file with columns L, g, Delta.
- Evidence: `/app/outputs/raw_energies.csv`

### Step 2: Fit strong coupling expansion and extract δ_L
- Role: scored (load-bearing)
- Action: From raw_energies.csv, for each L fit Δ(g,L)/L = a1·g + a2 + δ_L/g. Extract the coefficient δ_L. Also extrapolate the infinite‑L limit of δ_L. Write the results to delta_L_values.csv with columns L (integer or string 'inf') and delta (float).
- Output file: `/app/outputs/delta_L_values.csv`
- Format: csv
- Contract: CSV table with columns: L (integer or the string 'inf' for the extrapolated limit), delta (float).
- Scoring: scored by hidden verifier

### Step 3: Verify exact leading and constant terms
- Role: scored
- Action: For each L in {8,12,16,20,24,28,32}, compute the exact leading coefficient a1 = √2 / (L sin(π/(2L))) and the exact constant term a2 = 3/4. Write the computed values to a JSON file with key "results" holding an array of objects, each containing L (integer), a1 (float), a2 (float).
- Output file: `/app/outputs/leading_constant_report.json`
- Format: json
- Contract: JSON object with key "results": array of objects with keys L (integer), a1 (float), a2 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_L_values.csv`
- `/app/outputs/leading_constant_report.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_L_values.csv
- path: `/app/outputs/delta_L_values.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of fitted next‑to‑next‑to‑leading order coefficients δ_L for the antiferromagnetic state at each L and the extrapolated infinite‑L limit.
- schema:
  - `type`: table
  - `required_columns`: `L`, `delta`

### leading_constant_report.json
- path: `/app/outputs/leading_constant_report.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed exact leading coefficient a1 and constant term a2 for the strong‑coupling expansion at each L.
- schema:
  - `type`: object
  - `required`:
    - `results`: array
  - `items`:
    - `L`: integer
    - `a1`: float
    - `a2`: float

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_L_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "delta"
        ]
      },
      "description": "Table of fitted next‑to‑next‑to‑leading order coefficients δ_L for the antiferromagnetic state at each L and the extrapolated infinite‑L limit."
    },
    {
      "file": "leading_constant_report.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "results": "array"
        },
        "items": {
          "L": "integer",
          "a1": "float",
          "a2": "float"
        }
      },
      "description": "Computed exact leading coefficient a1 and constant term a2 for the strong‑coupling expansion at each L."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently scores each output file. For `delta_L_values.csv`, it compares each submitted δ_L (finite L) and the extrapolated δ_∞ to hidden reference values using a predefined absolute tolerance; the smaller the deviation, the higher the score. For `leading_constant_report.json`, it verifies that all a1 and a2 entries are exactly equal to the analytical expressions. The overall reward is a weighted sum of these scores, with the main load‑bearing artifact (`delta_L_values.csv`) carrying the largest weight. There is no partial credit for missing, malformed, or empty artifacts. The reward is based solely on the artifacts you produce in `/app/outputs`.
