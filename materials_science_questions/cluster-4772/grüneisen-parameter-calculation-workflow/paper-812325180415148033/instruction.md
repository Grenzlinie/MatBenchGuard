# Grüneisen parameter determination from high-pressure strain–pressure data for a crystalline polymer

## Problem background
High-pressure X‑ray diffraction studies on crystalline polyethylene reveal how lattice planes (110) and (200) compress under hydrostatic pressure. The measured negative strain versus pressure data can be modeled empirically to quantify the material’s linear compressibility and its pressure dependence. A central physical quantity derived from this analysis is the Grüneisen parameter γ₀, which links thermal expansion to lattice vibrations at atmospheric pressure. Reproducing the strain–pressure fits and computing γ₀ validates the quantitative analysis of the experimental observations.

## Approach
The negative strain –ε for each plane (110 and 200) is modeled as a cubic polynomial in pressure p:
–ε = A p – B p² + C p³.
A least‑squares fit (e.g., scipy’s curve_fit) to the experimental data yields the coefficients A, B, C for each plane. Volumetric strain ε_vol is then constructed from the plane strains using the relation derived from orthorhombic lattice constants (a=7.41 Å, b=4.95 Å):
ε_vol = 1.447·(ε₁₁₀ + 0.382·ε₂₀₀).
A second cubic least‑squares fit to ε_vol vs p gives A_v, B_v, C_v. Finally, the atmospheric‑pressure Grüneisen parameter is obtained from the volumetric coefficients:
γ₀ = –1/2 + (B_v / A_v).
The entire workflow uses only the provided numerical pressure–strain table and standard Python scientific libraries.

## Reproduction target
Using the pressure and strain data supplied in the assets, perform the cubic least‑squares fits described in the Approach for the (110) and (200) planes, compute the volumetric strain and its cubic fit, and calculate γ₀. Write all fitted coefficients (plane 110, plane 200, volumetric) and the γ₀ value to `/app/outputs/reproduced_results.json` in the schema specified in Step 2.

## Assets

- Pressure–strain data (Table I from source paper)
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Prepare strain–pressure data arrays
- Role: process
- Action: Extract the provided pressure p (in 10³ kg cm⁻²), –ε₁₁₀ (%) and –ε₂₀₀ (%) arrays from the task material. Create numerical arrays covering the full 0–14 000 kg cm⁻² range (13 data points).
- Evidence: `/app/outputs/data_log.txt`

### Step 2: Fit cubic polynomials and compute Grüneisen parameter
- Role: scored (load-bearing)
- Action: Perform least-squares fits using scipy.optimize.curve_fit (or equivalent) to obtain coefficients A, B, C for the model –ε = A p – B p² + C p³ for the (110) and (200) planes separately. Compute volumetric strain for each pressure from the raw strains as ε_vol = 1.447·(ε₁₁₀ + 0.382·ε₂₀₀) (derived from lattice constants a=7.41 Å, b=4.95 Å). Fit a cubic polynomial to ε_vol vs. p to obtain A_v, B_v, C_v. Finally, compute the Grüneisen parameter γ₀ = –1/2 + B_v / A_v. Write all coefficients and γ₀ to the output file.
- Output file: `/app/outputs/reproduced_results.json`
- Format: json
- Contract: {"type": "object", "required": ["plane_110","plane_200","volumetric","gamma_0"], "properties": {"plane_110": {"type": "object", "required": ["A","B","C"], "properties": {"A": {"type": "number"}, "B": {"type": "number"}, "C": {"type": "number"}}}, "plane_200": {"type": "object", "required": ["A","B","C"], "properties": {"A": {"type": "number"}, "B": {"type": "number"}, "C": {"type": "number"}}}, "volumetric": {"type": "object", "required": ["A_v","B_v","C_v"], "properties": {"A_v": {"type": "number"}, "B_v": {"type": "number"}, "C_v": {"type": "number"}}}, "gamma_0": {"type": "number"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_results.json
- path: `/app/outputs/reproduced_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted cubic polynomial coefficients for the (110) and (200) plane strain–pressure relations, volumetric strain polynomial coefficients, and the atmoshperic-pressure Grüneisen parameter γ₀.
- schema:
  - `type`: object
  - `required`: `plane_110`, `plane_200`, `volumetric`, `gamma_0`
  - `properties`:
    - `plane_110`:
      - `type`: object
      - `required`: `A`, `B`, `C`
      - `properties`:
        - `A`:
          - `type`: number
        - `B`:
          - `type`: number
        - `C`:
          - `type`: number
    - `plane_200`:
      - `type`: object
      - `required`: `A`, `B`, `C`
      - `properties`:
        - `A`:
          - `type`: number
        - `B`:
          - `type`: number
        - `C`:
          - `type`: number
    - `volumetric`:
      - `type`: object
      - `required`: `A_v`, `B_v`, `C_v`
      - `properties`:
        - `A_v`:
          - `type`: number
        - `B_v`:
          - `type`: number
        - `C_v`:
          - `type`: number
    - `gamma_0`:
      - `type`: number

Notes: The solver must fit cubic polynomials using the provided experimental data; no extrapolation or additional data should be used. The checker will compare against the paper's reported values with 5% relative tolerance for coefficients and 0.1 absolute tolerance for γ₀.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "plane_110",
          "plane_200",
          "volumetric",
          "gamma_0"
        ],
        "properties": {
          "plane_110": {
            "type": "object",
            "required": [
              "A",
              "B",
              "C"
            ],
            "properties": {
              "A": {
                "type": "number"
              },
              "B": {
                "type": "number"
              },
              "C": {
                "type": "number"
              }
            }
          },
          "plane_200": {
            "type": "object",
            "required": [
              "A",
              "B",
              "C"
            ],
            "properties": {
              "A": {
                "type": "number"
              },
              "B": {
                "type": "number"
              },
              "C": {
                "type": "number"
              }
            }
          },
          "volumetric": {
            "type": "object",
            "required": [
              "A_v",
              "B_v",
              "C_v"
            ],
            "properties": {
              "A_v": {
                "type": "number"
              },
              "B_v": {
                "type": "number"
              },
              "C_v": {
                "type": "number"
              }
            }
          },
          "gamma_0": {
            "type": "number"
          }
        }
      },
      "description": "Fitted cubic polynomial coefficients for the (110) and (200) plane strain–pressure relations, volumetric strain polynomial coefficients, and the atmoshperic-pressure Grüneisen parameter γ₀."
    }
  ],
  "notes": "The solver must fit cubic polynomials using the provided experimental data; no extrapolation or additional data should be used. The checker will compare against the paper's reported values with 5% relative tolerance for coefficients and 0.1 absolute tolerance for γ₀."
}
```

## How you are scored
A hidden verifier will independently compare the coefficients and γ₀ you report in `reproduced_results.json` to reference values. The verification checks numerical agreement within a tolerance that accounts for the deterministic fitting procedure. The final reward is a weighted combination of the per‑output scores; merely reporting the paper’s numbers is not sufficient—the verifier expects a correct computation from the given data.
