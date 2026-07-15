# Nucleation Free-Energy Barrier Calculation for Twinned FCC Crystals

## Problem background
For twinned face-centered-cubic crystals, twin planes create re-entrant troughs and convex ridges that can significantly enhance crystal growth rate. Classical nucleation theory is applied to compute the energy barriers for two-dimensional (2D) nucleation on flat {111} and {100} surfaces, on a {111}/{111} trough (elliptical and semicircular shapes), and for layer advance across a ridge. The barriers are expressed in terms of the nearest-neighbor bond energy and the driving force per atom. This task computes these nucleation barriers and their relative magnitudes, with the flat {111} case as the reference. The outcome quantifies how much easier or harder nucleation is at these geometric features compared to a flat {111} face.

## Approach
Use a broken-bond model with first-nearest-neighbor interactions (bond energy φ, atomic diameter d) and classical nucleation theory. For a flat face, the free-energy change of a circular nucleus is ΔG = (area) * Δμ + (perimeter) * ε, where ε is the step line energy and Δμ is the driving force per unit area. The step energy is obtained from the number of broken bonds per unit length (e.g., ε_{111}=2φ/d, ε_{100}=φ/d), and Δμ is related to the driving force per atom Δμ_a by the area per atom on each surface. For nucleation on a trough, two possible shapes are considered: an elliptical nucleus and a semicircular nucleus. Their shapes are determined by a force balance among the step energies and the groove line energy ε_g, which itself is derived from the broken-bond count at the re-entrant edge. The groove energy yields a contact angle that defines the elliptical or semicircular geometry. The nucleation barrier ΔG* for each case is obtained as a function of φ and Δμ_a. For layer advance across the ridge, a one-dimensional nucleation process at the step edge (substep) is modelled analogously, yielding another barrier expression. Finally, for all five cases — circular nucleus on {111}, circular on {100}, elliptical on trough, semicircular on trough, and layer advance across ridge — compute the barrier formula (as a string in standard mathematical notation) and the percentage relative to the flat {111} circular barrier. The percentage is a pure number independent of φ and Δμ_a.

## Reproduction target
Write a JSON file `nucleation_barriers.json` containing an array of five objects. Each object must have three fields: `nucleus_type` (one of "circular_{111}", "circular_{100}", "elliptical_trough", "semicircular_trough", "layer_advance_ridge"), `barrier_formula` (a string describing the nucleation barrier ΔG* in terms of φ and Δμ_a, using standard arithmetic operators and the constant π, with multiplication denoted by `*` when needed; e.g., `2*sqrt(3)*π*φ^2/Δμ_a`), and `percentage` (a number giving the barrier as a percentage of the flat {111} circular barrier). The barrier formulas must be derived from the broken-bond model and classical nucleation theory following the approach described above. The percentages must be consistent with those formulas and should match the values obtained when the formulas are evaluated numerically.

## Assets

- Python 3 with standard math libraries: python3

## Workflow steps

### Step 1: Compute all nucleation barriers
- Role: scored (load-bearing)
- Action: Implement the broken-bond model and classical nucleation theory to derive step energies for {111} and {100} surfaces, driving forces per unit area, groove line energy, the contact angle for the elliptical trough nucleus, boundary line energy for the semicircular trough nucleus, and the layer-advance barrier on the ridge. From these, compute the nucleation barrier formulas (in terms of φ and Δμ_a) and their percentages relative to the flat {111} barrier for the five cases in Table 1: circular nucleus on {111}, circular nucleus on {100}, elliptical nucleus on trough, semicircular nucleus on trough, and layer advance across ridge. Write the results to nucleation_barriers.json.
- Output file: `/app/outputs/nucleation_barriers.json`
- Format: json
- Contract: [{"nucleus_type": "circular_{111}" | "circular_{100}" | "elliptical_trough" | "semicircular_trough" | "layer_advance_ridge", "barrier_formula": string, "percentage": number}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nucleation_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nucleation_barriers.json
- path: `/app/outputs/nucleation_barriers.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: A JSON array of five objects, each giving the nucleus type, the analytic barrier formula, and the corresponding percentage relative to the flat {111} case. The checker will parse each barrier formula, evaluate it numerically with φ=1, Δμ_a=1, compute the fraction against the reference flat {111} barrier, and compare the resulting fraction to the reported percentage (and to the hidden gold percentages) with a tolerance of ±0.5.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `nucleus_type`, `barrier_formula`, `percentage`
    - `properties`:
      - `nucleus_type`:
        - `type`: string
        - `enum`: `circular_{111}`, `circular_{100}`, `elliptical_trough`, `semicircular_trough`, `layer_advance_ridge`
      - `barrier_formula`:
        - `type`: string
        - `description`: Formula for ΔG* expressed in terms of φ and Δμ_a, using standard mathematical notation.
      - `percentage`:
        - `type`: number
        - `description`: The nucleation barrier expressed as a percentage of the flat {111} barrier.

Notes: The derivation of intermediate quantities (step energies, driving forces, groove energy, contact angle) is considered part of the implementation and is not required as separate output files. The agent may use any symbolic or numeric implementation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nucleation_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "nucleus_type",
            "barrier_formula",
            "percentage"
          ],
          "properties": {
            "nucleus_type": {
              "type": "string",
              "enum": [
                "circular_{111}",
                "circular_{100}",
                "elliptical_trough",
                "semicircular_trough",
                "layer_advance_ridge"
              ]
            },
            "barrier_formula": {
              "type": "string",
              "description": "Formula for ΔG* expressed in terms of φ and Δμ_a, using standard mathematical notation."
            },
            "percentage": {
              "type": "number",
              "description": "The nucleation barrier expressed as a percentage of the flat {111} barrier."
            }
          }
        }
      },
      "description": "A JSON array of five objects, each giving the nucleus type, the analytic barrier formula, and the corresponding percentage relative to the flat {111} case. The checker will parse each barrier formula, evaluate it numerically with φ=1, Δμ_a=1, compute the fraction against the reference flat {111} barrier, and compare the resulting fraction to the reported percentage (and to the hidden gold percentages) with a tolerance of ±0.5."
    }
  ],
  "notes": "The derivation of intermediate quantities (step energies, driving forces, groove energy, contact angle) is considered part of the implementation and is not required as separate output files. The agent may use any symbolic or numeric implementation."
}
```

## How you are scored
A hidden verifier will read your `nucleation_barriers.json`. It checks that all five required nucleus types are present and correctly named, then parses each `barrier_formula`. For each entry, the formula is evaluated numerically with test values (e.g., φ=1, Δμ_a=1) to obtain a numerical ΔG*. The verifier also computes the flat {111} barrier value from its own reference formula in the same way and forms the fraction (ΔG*_case / ΔG*_flat). It compares this fraction to a hidden gold percentage value for that case. Your reported `percentage` field is also compared directly to the gold. Each comparison uses a tolerance that accounts for minor implementation differences. The per-entry scores are combined into a total reward between 0 (incorrect or missing) and 1 (all entries within tolerance). Simply writing down the paper's numbers is not sufficient—the formulas must be correct and the percentages consistent with the underlying physics.
