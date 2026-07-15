# Strengthening Mechanism Attribution in Nano-martensitic Ti Alloy

## Problem background
Titanium alloys are important lightweight structural materials. A promising approach to enhance their strength is to create a hierarchical nano-martensitic microstructure in metastable titanium alloys. A recent study developed a Ti-2.8Cr-4.5Zr-5.2Al alloy with a duplex microstructure consisting of equiaxed primary α grains and nanoscale α' martensite lamellae embedded in a β matrix. To understand the mechanical properties of this alloy, it is necessary to quantify the contributions of different strengthening mechanisms—solid solution, dislocation, precipitation, and interface strengthening—to the overall yield strength. This task requires computing those contributions from the measured microstructural parameters using classical strengthening models.

## Approach
The total yield strength is modeled as a sum of four independent strengthening contributions: solid solution strengthening, dislocation strengthening, precipitation strengthening, and interface strengthening. Each contribution is estimated using well-known micromechanical models:
- Solid solution strengthening from alloying elements.
- Dislocation strengthening (forest hardening) related to the dislocation density.
- Precipitation strengthening via the Orowan mechanism and the coefficient of thermal expansion (CTE) mismatch effect.
- Interface strengthening that captures the Hall–Petch effect for the primary α grains and interlamellar spacing strengthening for the α'/β lamellae.
The microstructural parameters (grain size, lamella thickness, volume fractions, dislocation density) are taken from the experimental characterization of the water-quenched alloy and are provided in the workflow step. Standard physical constants (shear modulus, Burgers vector, Taylor factor) are employed. The agent must implement these models, compute each contribution, sum them to obtain the total yield strength, and output the results in a structured JSON file.

## Reproduction target
Compute the total yield strength and the individual strengthening contributions for the water-quenched (WQ) Ti-2.8Cr-4.5Zr-5.2Al alloy using the classical strengthening models (solid solution, dislocation, precipitation, and interface) with the microstructural parameters provided in the workflow step. Write the results to `/app/outputs/step_01_prediction.json` containing the following fields: `yield_strength_MPa`, `interface_strengthening_MPa`, `dislocation_strengthening_MPa`, `solid_solution_strengthening_MPa`, `precipitation_strengthening_MPa`.

## Assets
No external datasets or software are required beyond standard scientific computing packages. All necessary microstructural parameters are specified in the workflow step. Standard physical constants (e.g., shear modulus, Burgers vector, Taylor factor) can be obtained from general materials science references.

## Workflow steps

### Step 1: Compute yield strength and strengthening contributions
- Role: scored (load-bearing)
- Action: Implement the classical strengthening model (Hall‑Petch for primary α, interlamellar spacing strengthening for α'/β lamellae, Orowan, CTE mismatch, and solid solution) using the microstructural parameters from the paper (α_p grain diameter ~2.9 μm, volume fraction ~30%; α' lamella thickness ~20 nm, volume fraction ~58.7%; β lamella thickness ~22 nm; dislocation density ~1.2×10¹⁴ m⁻²; and standard material constants). Compute the contributions from solid solution, dislocation, precipitation, and interface strengthening, and sum them to obtain the total yield strength. Output the results to step_01_prediction.json.
- Output file: `/app/outputs/step_01_prediction.json`
- Format: json
- Contract: {"type": "object", "required": ["yield_strength_MPa", "interface_strengthening_MPa", "dislocation_strengthening_MPa", "solid_solution_strengthening_MPa", "precipitation_strengthening_MPa"], "properties": {"yield_strength_MPa": {"type": "number", "unit": "MPa"}, "interface_strengthening_MPa": {"type": "number", "unit": "MPa"}, "dislocation_strengthening_MPa": {"type": "number", "unit": "MPa"}, "solid_solution_strengthening_MPa": {"type": "number", "unit": "MPa"}, "precipitation_strengthening_MPa": {"type": "number", "unit": "MPa"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_prediction.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_prediction.json
- path: `/app/outputs/step_01_prediction.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed total yield strength and individual strengthening contributions for the water-quenched Ti-2.8Cr-4.5Zr-5.2Al alloy.
- schema:
  - `type`: object
  - `required`:
    - `yield_strength_MPa`: number (MPa)
    - `interface_strengthening_MPa`: number (MPa)
    - `dislocation_strengthening_MPa`: number (MPa)
    - `solid_solution_strengthening_MPa`: number (MPa)
    - `precipitation_strengthening_MPa`: number (MPa)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `yield_strength_MPa`: MPa
    - `interface_strengthening_MPa`: MPa
    - `dislocation_strengthening_MPa`: MPa
    - `solid_solution_strengthening_MPa`: MPa
    - `precipitation_strengthening_MPa`: MPa

Notes: The task omits the diffusion distance calculation and phase-field simulation stages, as they are supporting analyses and not required for the main quantitative claim. The strengthening model evaluation is self-contained and verifiable by recomputing from the same microstructural parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_prediction.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "yield_strength_MPa": "number (MPa)",
          "interface_strengthening_MPa": "number (MPa)",
          "dislocation_strengthening_MPa": "number (MPa)",
          "solid_solution_strengthening_MPa": "number (MPa)",
          "precipitation_strengthening_MPa": "number (MPa)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "yield_strength_MPa": "MPa",
          "interface_strengthening_MPa": "MPa",
          "dislocation_strengthening_MPa": "MPa",
          "solid_solution_strengthening_MPa": "MPa",
          "precipitation_strengthening_MPa": "MPa"
        }
      },
      "description": "Computed total yield strength and individual strengthening contributions for the water-quenched Ti-2.8Cr-4.5Zr-5.2Al alloy."
    }
  ],
  "notes": "The task omits the diffusion distance calculation and phase-field simulation stages, as they are supporting analyses and not required for the main quantitative claim. The strengthening model evaluation is self-contained and verifiable by recomputing from the same microstructural parameters."
}
```

## How you are scored
A hidden verifier independently recomputes the total yield strength from the same microstructural parameters and a reference implementation of the strengthening models. It reads your `step_01_prediction.json` and compares your reported values to its recomputed values. Full credit is awarded when the absolute differences are within pre-set tolerances; reporting an arbitrary number without correct theoretical computation will not pass the verifier.
