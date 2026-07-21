# Thermodynamic Equilibrium Constants and Partial Pressures for Bi2(Se1-xSx)3 Solid Solution

## Problem background
Bi2(Se1-xSx)3 ternary crystals are layered semiconductors whose electrical properties depend on stoichiometry and the vapour pressures of selenium and sulphur. Understanding the vapour‑solid phase equilibrium is essential for controlling free carrier concentration and native point defect density. A thermodynamic model that treats the mixed crystal as an ideal solid solution of Bi2Se3 and Bi2S3 is used to relate equilibrium partial pressures and defect chemistry. This task reproduces the thermodynamic computations that yield the equilibrium constants, minimum partial pressures for a range of compositions and temperatures, and the equilibrium constant for the defect incorporation reaction derived from experimental transport data.

## Approach
The core idea is to model the ternary crystal as an ideal solid solution, so that the activities of Bi2Se3 and Bi2S3 equal their respective mole fractions. Pure‑component equilibrium constants K_Bi2Se3 and K_Bi2S3 are first computed from published temperature‑dependent log‑linear relations (log10 K = A/T + B, with given A and B) for a range of temperatures. The overall equilibrium constant K1 for the congruent dissociation reaction is then built from these pure‑component constants and the composition x using the ideal‑solution expression; its negative logarithm pK1 is tabulated for a grid of compositions and temperatures. Minimum partial pressures of diatomic Se2 and S2 over the ternary crystal at the annealing temperature (700 K) are obtained by minimising the total vapour pressure, leading to expressions that involve the pure‑component equilibrium constants. Finally, the equilibrium constant K_R of the defect incorporation reaction is evaluated from experimental Hall coefficients (R_H) and vapour pressures: the carrier concentration N is derived from R_H via N = 1/(e·R_H) with e the elementary charge, an effective composition y is determined from the pressure ratio using the equilibrium constants, and K_R is given by 1/(N² · p_Se2^{(1−y)/2} · p_S2^{y/2}) with consistent units (m⁶·kPa^{-1/2}). All required thermochemical coefficients and the R_H values are provided in the workflow steps and must be hardcoded by the solver.

## Reproduction target
Compute the temperature‑dependent equilibrium constants of pure Bi2Se3 and Bi2S3, the overall pK1 for a series of compositions and temperatures, the minimum partial pressures of Se2 and S2 at 700 K, and the defect equilibrium constant K_R for the annealing conditions described. Output all computed quantities into a single JSON file `results.json` that contains the data for each component in a structured format. The file must follow the output contract exactly.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Compute pure component equilibrium constants
- Role: process
- Action: Compute the equilibrium constants K_Bi2Se3 and K_Bi2S3 for temperatures from 300 K to 800 K using the published log-linear relations: log10(K) = A/T + B with A1=-6566.4 K, B1=-15.6 for Bi2Se3 and A2=-6313.1 K, B2=-14.2 for Bi2S3. Keep these constants for use in subsequent steps.

### Step 2: Compute overall equilibrium constant pK1
- Role: process
- Action: For each composition x in [0.01, 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15] and temperature T in [300, 400, 500, 600, 700, 800] K, evaluate K1 = x^x * (1-x)^(1-x) * K_Bi2S3^x * K_Bi2Se3^(1-x) using the K constants from step 1, then compute pK1 = -log10(K1).

### Step 3: Compute minimum partial pressures
- Role: process
- Action: At T = 700 K and for x in [0.01, 0.05, 0.09, 0.13, 0.17], compute the minimum partial pressures p_Se2^min and p_S2^min (in kPa) using the explicit expressions
p_Se2_min = [ (3/2)*(1-x)*K_Bi2Se3 / (1 + (1-x)^(-2/3) * K_Bi2Se3^(-2/3) * x^(2/3) * K_Bi2S3^(2/3)) ]^(2/5)
p_S2_min  = [ (3/2)*x*K_Bi2S3 / (1 + (1-x)^(2/3) * K_Bi2Se3^(2/3) * x^(2/3) * K_Bi2S3^(-2/3)) ]^(2/5)
where K_Bi2Se3 and K_Bi2S3 are the pure-component equilibrium constants at 700 K obtained in step 1.

### Step 4: Compute defect equilibrium constant K_R
- Role: process
- Action: For each annealing condition, compute the carrier concentration N = 1 / (R_H * e) using the Hall coefficient after annealing and the elementary charge e = 1.602176634e-19 C. Determine the effective composition y from the pressure ratio p_S2/p_Se2 using the formula:
y = 1 / ( (p_Se2/p_S2)^(3/2) * (K_Bi2S3 / K_Bi2Se3) + 1 )
where K_Bi2Se3 and K_Bi2S3 are evaluated at 700 K (from step 1). Then evaluate K_R = 1 / ( N^2 * p_Se2^((1-y)/2) * p_S2^(y/2) ), ensuring consistent units (m^6·kPa^{-1/2}). The required experimental values are:
  - Sample 2, T2=645 K: R_H = 0.303e-6 m^3/(A·s), p_Se2 = 0.305 kPa, p_S2 = 0.480 kPa.
  - Sample 2, T2=675 K: R_H = 0.405e-6 m^3/(A·s), p_Se2 = 0.608 kPa, p_S2 = 0.950 kPa.
  - Sample 3, T2=645 K: R_H = 0.331e-6 m^3/(A·s), p_Se2 = 0.288 kPa, p_S2 = 2.079 kPa.
  - Sample 3, T2=675 K: R_H = 0.364e-6 m^3/(A·s), p_Se2 = 0.570 kPa, p_S2 = 4.000 kPa.
  - Sample 4, T2=645 K: R_H = 0.359e-6 m^3/(A·s), p_Se2 = 0.275 kPa, p_S2 = 3.300 kPa.
  - Sample 4, T2=675 K: R_H = 0.349e-6 m^3/(A·s), p_Se2 = 0.541 kPa, p_S2 = 6.350 kPa.

### Step 5: Assemble final results
- Role: scored (load-bearing)
- Action: Combine all computed quantities into a single JSON file with the following keys: 'K_Bi2Se3' (object mapping temperature in K to float), 'K_Bi2S3' (object mapping temperature to float), 'pK1' (array of objects each with x, T, pK1_value), 'min_partial_pressures' (array of objects each with x, pS2_min, pSe2_min), 'K_R' (array of objects each with sample_no, T2, N, K_R). All numeric values must be in the same units and precision as described in the paper.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with keys 'K_Bi2Se3', 'K_Bi2S3', 'pK1', 'min_partial_pressures', 'K_R' as described.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Master output file containing all reproduced thermodynamic quantities: pure-component equilibrium constants (K_Bi2Se3, K_Bi2S3), overall pK1 for varying x and T, minimum partial pressures at 700 K, and the defect equilibrium constant K_R.
- schema:
  - `type`: object
  - `required`:
    - `K_Bi2Se3`:
      - `type`: object
      - `description`: mapping of temperature (integer K) to K_Bi2Se3 (float)
      - `item_type`: float
    - `K_Bi2S3`:
      - `type`: object
      - `description`: mapping of temperature (integer K) to K_Bi2S3 (float)
      - `item_type`: float
    - `pK1`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `x`, `T`, `pK1_value`
        - `properties`:
          - `x`: float
          - `T`: integer
          - `pK1_value`: float
    - `min_partial_pressures`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `x`, `pS2_min`, `pSe2_min`
        - `properties`:
          - `x`: float
          - `pS2_min`: float
          - `pSe2_min`: float
    - `K_R`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `sample_no`, `T2`, `N`, `K_R`
        - `properties`:
          - `sample_no`: integer
          - `T2`: integer
          - `N`: float
          - `K_R`: float

Notes: All quantities are computed from the published thermochemical parameters and experimental transport data. The solver must hardcode the required experimental values (Table 1 of the source) and thermodynamic constants given in the problem statement.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "K_Bi2Se3": {
            "type": "object",
            "description": "mapping of temperature (integer K) to K_Bi2Se3 (float)",
            "item_type": "float"
          },
          "K_Bi2S3": {
            "type": "object",
            "description": "mapping of temperature (integer K) to K_Bi2S3 (float)",
            "item_type": "float"
          },
          "pK1": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "x",
                "T",
                "pK1_value"
              ],
              "properties": {
                "x": "float",
                "T": "integer",
                "pK1_value": "float"
              }
            }
          },
          "min_partial_pressures": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "x",
                "pS2_min",
                "pSe2_min"
              ],
              "properties": {
                "x": "float",
                "pS2_min": "float",
                "pSe2_min": "float"
              }
            }
          },
          "K_R": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "sample_no",
                "T2",
                "N",
                "K_R"
              ],
              "properties": {
                "sample_no": "integer",
                "T2": "integer",
                "N": "float",
                "K_R": "float"
              }
            }
          }
        }
      },
      "description": "Master output file containing all reproduced thermodynamic quantities: pure-component equilibrium constants (K_Bi2Se3, K_Bi2S3), overall pK1 for varying x and T, minimum partial pressures at 700 K, and the defect equilibrium constant K_R."
    }
  ],
  "notes": "All quantities are computed from the published thermochemical parameters and experimental transport data. The solver must hardcode the required experimental values (Table 1 of the source) and thermodynamic constants given in the problem statement."
}
```

## How you are scored
A hidden verifier will independently recompute each quantity using the same thermodynamic formulas and the same experimental inputs that are listed in this instruction. It compares your submitted numbers to the recomputed expected values with appropriate relative tolerances. The final reward is a weighted combination of the scores for each section of the results, reflecting how closely your reproduced quantities match the expectations. Submitting numbers produced by any other method, or merely reporting the expected values without genuine computation, will not earn credit.