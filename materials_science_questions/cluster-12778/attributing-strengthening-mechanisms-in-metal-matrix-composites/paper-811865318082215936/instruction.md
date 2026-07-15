# Cr Diffusion Distance in Al at 400°C

## Problem background
Al‑Cr alloys are candidates for lightweight components at elevated temperatures because chromium diffuses very slowly in solid aluminium. After prolonged annealing at 400 °C, a powder‑metallurgy Al‑Cr‑Fe‑Ti alloy retains essentially unchanged room‑temperature mechanical properties, which is attributed to the kinetic limitation of Cr diffusion. A key quantitative piece of this explanation is the average distance a Cr atom can diffuse during the annealing treatment. This task isolates that diffusion‑distance calculation by computing the distance a Cr atom travels in solid Al under the reported annealing conditions and comparing it to the interparticle spacing of the strengthening Al₁₃(Cr,Fe)₂ spheroids.

## Approach
The average diffusion distance X is estimated from the relation X² = 2Dτ, where D is the diffusion coefficient of Cr in solid Al at 400 °C (4.3 × 10⁻¹⁷ cm² s⁻¹, a value from the public literature) and τ is the annealing time (200 hours). The calculation is performed in consistent units, the resulting X is converted to micrometers, and the value is compared to the reported average interparticle spacing L = 0.3 µm of the Al₁₃(Cr,Fe)₂ spheroids. No other data or external resources are required.

## Reproduction target
Using the given diffusion coefficient and annealing time, compute the average Cr diffusion distance X at 400 °C, express it in micrometers, and determine whether it is smaller than the interparticle spacing L = 0.3 µm. Write a single JSON file `/app/outputs/diffusion_distance.json` containing the computed X (float, in µm) and a boolean indicating the result of the comparison (X < L).

## Assets
No external datasets, models, or specialised packages are required. The calculation relies only on the numerical inputs stated in the step description and standard Python libraries.

## Workflow steps

### Step 1: Diffusion distance calculation
- Role: scored (load-bearing)
- Action: Compute the average diffusion distance X of Cr atoms in solid Al at 400°C for 200 h using the relation X² = 2Dτ, where D = 4.3×10⁻¹⁷ cm² s⁻¹ and τ = 200 h. Convert X to μm. Compare X to the reported interparticle spacing L = 0.3 μm and record whether X < L. Write a JSON file with the computed X (in μm) and the boolean result.
- Output file: `/app/outputs/diffusion_distance.json`
- Format: json
- Contract: {"X_μm": "float (computed diffusion distance in microns)", "less_than_L": "boolean (true if X_μm < 0.3)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/diffusion_distance.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### diffusion_distance.json
- path: `/app/outputs/diffusion_distance.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Average Cr diffusion distance X at 400°C for 200h and its comparison to the interparticle spacing L=0.3 µm. Contains fields: X_µm (float, in µm) and less_than_L (bool).
- schema:
  - `type`: object
  - `required`:
    - `X_μm`: float
    - `less_than_L`: bool
  - `items`: None
  - `required_columns`: None
  - `units`:
    - `X_μm`: µm

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "diffusion_distance.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "X_μm": "float",
          "less_than_L": "bool"
        },
        "items": null,
        "required_columns": null,
        "units": {
          "X_μm": "µm"
        }
      },
      "description": "Average Cr diffusion distance X at 400°C for 200h and its comparison to the interparticle spacing L=0.3 µm. Contains fields: X_µm (float, in µm) and less_than_L (bool)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently recomputes the diffusion distance from the same inputs (D and τ) and checks your boolean determination. Your `X_μm` value is compared to the recomputed value within a tolerance, and the `less_than_L` flag must agree with the verifier’s determination. The final reward is 1.0 if both checks pass and 0.0 otherwise.
