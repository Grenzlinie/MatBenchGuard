# ZT Calculation from Transport Properties for Thermoelectric Materials

## Problem background
Solid-state thermoelectric materials hold promise for energy harvesting and exhaust heat recovery, but they often suffer from lattice defects that degrade performance at high temperatures. This work explores molten (liquid) salts and chalcogenides as a thermally durable alternative. The goal is to evaluate the thermoelectric figure of merit ZT for three candidate materials — Bi<sub>2</sub>Te<sub>3</sub>, CuI, and AgI — in the molten state at 1000 K. ZT combines the electrical conductivity σ, the Seebeck coefficient α, and the total thermal conductivity κ to quantify how efficiently a temperature difference can be converted into electricity. A ZT above 0.1 is considered promising for high-temperature applications.

## Approach
We estimate the thermal conductivity κ as the sum of an electronic contribution κ<sub>e</sub> and an atomic‑motion contribution κ<sub>a</sub>. The electronic part follows the Wiedemann–Franz law, κ<sub>e</sub> = L·σ·T, with the Lorenz number L = 2.45×10<sup>−8</sup> W·Ω/K<sup>2</sup>. The atomic‑motion part is given by the Regel model, κ<sub>a</sub> = 64·Ā<sup>−1.04</sup> W/m·K, where Ā is the average atomic weight of the compound. The total thermal conductivity κ = κ<sub>e</sub> + κ<sub>a</sub> is then used to compute the dimensionless figure of merit ZT = (α<sup>2</sup> · σ · T) / κ. The required input values — the electrical conductivity σ, the Seebeck coefficient α at 1000 K, and the average atomic weight for each material — are provided directly in the workflow steps; no external datasets or models need to be fetched.

## Reproduction target
Given the measured electrical conductivity and Seebeck coefficient for molten Bi<sub>2</sub>Te<sub>3</sub>, CuI, and AgI at 1000 K, compute the electronic thermal conductivity κ<sub>e</sub>, the atomic‑motion thermal conductivity κ<sub>a</sub>, the total κ, and the figure of merit ZT for each material. Write all computed quantities to a single JSON file. The main verification condition is that the computed ZT for CuI exceeds 0.1, while the ZT of Bi<sub>2</sub>Te<sub>3</sub> and AgI should remain below 0.01. No other materials or temperatures are required.

## Assets
No external assets are required. All necessary input data (σ, α, and the average atomic weights) are supplied in the workflow step. No datasets, pre‑trained models, or additional tools need to be downloaded.

## Workflow steps

### Step 1: Compute thermoelectric properties and figure of merit ZT
- Role: scored (load-bearing)
- Action: For each molten material (Bi2Te3, CuI, AgI), using the electrical conductivity σ (in (Ω·cm)^-1) at 1000 K (Bi2Te3: 1800, CuI: 1.0, AgI: 0.05), Seebeck coefficient α (in μV/K) at 1000 K (Bi2Te3: 10, CuI: 755, AgI: 500), the material's average atomic weight Ā (Bi2Te3: 160.152, CuI: 95.225, AgI: 117.385), and temperature T = 1000 K, compute:
- electronic thermal conductivity κ_e = L · σ · T with L = 2.45×10^-8 W·Ω/K²
- atomic-motion thermal conductivity κ_a = 64 · Ā^{-1.04} W/m·K
- total thermal conductivity κ = κ_e + κ_a
- dimensionless figure of merit ZT = (α² · σ · T) / κ
All quantities must be written to results.json as an array of objects, one per material.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Array of objects with properties: material (string), sigma (number in (Ω·cm)^{-1}), alpha (number in μV/K), kappa_e (number in W/m·K), kappa_a (number in W/m·K), kappa_total (number in W/m·K), ZT (number dimensionless). All fields required.
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
- target_policy: threshold_or_better
- description: Computed thermoelectric transport properties and figure of merit for Bi2Te3, CuI, and AgI at 1000 K. The checker recomputes ZT from these values and verifies that CuI ZT exceeds 0.1, while Bi2Te3 and AgI ZT remain below 0.01.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `material`:
        - `type`: string
      - `sigma`:
        - `type`: number
        - `units`: (Ω·cm)^{-1}
      - `alpha`:
        - `type`: number
        - `units`: μV/K
      - `kappa_e`:
        - `type`: number
        - `units`: W/m·K
      - `kappa_a`:
        - `type`: number
        - `units`: W/m·K
      - `kappa_total`:
        - `type`: number
        - `units`: W/m·K
      - `ZT`:
        - `type`: number
        - `units`: dimensionless
    - `required`: `material`, `sigma`, `alpha`, `kappa_e`, `kappa_a`, `kappa_total`, `ZT`

Notes: The agent is provided explicit values of σ and α for each material at 1000 K in the instructions; no external data fetch is required. The scored target focuses on the paper's main claim of CuI ZT > 0.1.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "material": {
              "type": "string"
            },
            "sigma": {
              "type": "number",
              "units": "(Ω·cm)^{-1}"
            },
            "alpha": {
              "type": "number",
              "units": "μV/K"
            },
            "kappa_e": {
              "type": "number",
              "units": "W/m·K"
            },
            "kappa_a": {
              "type": "number",
              "units": "W/m·K"
            },
            "kappa_total": {
              "type": "number",
              "units": "W/m·K"
            },
            "ZT": {
              "type": "number",
              "units": "dimensionless"
            }
          },
          "required": [
            "material",
            "sigma",
            "alpha",
            "kappa_e",
            "kappa_a",
            "kappa_total",
            "ZT"
          ]
        }
      },
      "description": "Computed thermoelectric transport properties and figure of merit for Bi2Te3, CuI, and AgI at 1000 K. The checker recomputes ZT from these values and verifies that CuI ZT exceeds 0.1, while Bi2Te3 and AgI ZT remain below 0.01."
    }
  ],
  "notes": "The agent is provided explicit values of σ and α for each material at 1000 K in the instructions; no external data fetch is required. The scored target focuses on the paper's main claim of CuI ZT > 0.1."
}
```

## How you are scored
A hidden verifier will read your `results.json`. It will recompute the thermal conductivity components and ZT for each material using the same formulas and the input values you report. The verifier then checks whether the computed ZT for CuI exceeds 0.1 and whether the ZT values for Bi<sub>2</sub>Te<sub>3</sub> and AgI are below 0.01. The verifier does not compare your numbers to a single exact target; it uses a tolerance that accommodates minor numerical differences. The final reward is based on how many of these conditions your submission meets. Simply writing the expected conclusion is not sufficient — your computed values must actually satisfy the required inequalities.
