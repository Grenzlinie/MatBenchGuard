# Grain boundary energy vs misorientation angle computation

## Problem background
In polar ice sheets, deformation and recrystallization are controlled by grain boundary energy. Subgrain boundaries—low-angle dislocation walls—and high-angle grain boundaries exhibit different structures and energies. The energy of a subgrain boundary increases with the crystallographic misorientation between adjacent grains, and at some critical angle it becomes comparable to the energy of high-angle grain boundaries. In this task you will compute upper-bound estimates of grain boundary energy for basal and nonbasal dislocations in ice using a simple dislocation model. By computing the energy at several misorientation angles, you will determine the misorientation threshold at which the boundary energy reaches a value typical of high-angle grain boundaries. Your results will help quantify the role of different dislocation types in the deformation of Antarctic ice.

## Approach
The energy model is based on the elastic energy of individual dislocations and their spacing. For a small-angle tilt boundary, the dislocation spacing D is related to the Burgers vector magnitude b and misorientation angle θ by Frank's formula: D = b / (2 sin(θ/2)). The energy per unit area γ is approximately the energy of a single dislocation γ_d divided by D, with γ_d ≈ G b² / 2, where G is the shear modulus of ice (4 × 10⁹ N m⁻²). This yields the upper-bound estimate γ ≈ (G b² / 2) / D.

You will compute γ for basal dislocations (b = 4.52 Å) at misorientations θ = 0.5°, 3°, and 5°, and for nonbasal dislocations with two different Burgers vectors (b = 7.36 Å and b = 8.63 Å) at θ = 0.5° and 4°. All calculations must be performed in SI units, then converted to mJ m⁻² for energy and degrees for angles.

Finally, you will determine the threshold misorientation angle at which γ equals 65 mJ m⁻²—a typical high-angle grain boundary energy—for the basal case (b = 4.52 Å) and for a nonbasal case using the average Burgers vector 8.0 Å. These threshold angles are found by solving γ(θ) = 65 mJ m⁻².

## Reproduction target
Produce a single JSON file named `energy_estimates.json` that contains:
- the computed grain boundary energies (in mJ m⁻²) for the seven specified (dislocation type, misorientation) pairs;
- the two threshold misorientation angles (in degrees) where γ = 65 mJ m⁻² for the basal and nonbasal (average b=8.0 Å) cases.

The JSON file must have exactly the keys listed in the output contract, and all values must be positive numbers. The computation is self-contained; no external data or models are needed.

## Assets
No external datasets, models, or tools beyond standard Python libraries are required. All necessary physical constants and formulas are provided in the instructions. You may use the built-in `math` module for trigonometric and arithmetic operations and `json` for writing the output file.

## Workflow steps

### Step 1: Compute grain boundary energy estimates
- Role: scored (load-bearing)
- Action: Compute upper-bound grain boundary energies using the approximation γ ≈ (G b² / 2) / D with dislocation spacing D = b / (2 sin(θ/2)). Use shear modulus G = 4×10⁹ N/m². For basal dislocations (b = 4.52 Å) compute γ at misorientations θ = 0.5°, 3°, 5°. For nonbasal dislocations use b = 7.36 Å and b = 8.63 Å, computing γ at θ = 0.5° and 4°. Then determine the threshold misorientation angle where γ = 65 mJ/m² for the basal case (b = 4.52 Å) and for a nonbasal case (average b = 8.0 Å). Convert all energies to mJ/m² and angles to degrees. Store all nine values in a single JSON file with the keys specified in the output schema.
- Output file: `/app/outputs/energy_estimates.json`
- Format: json
- Contract: Object with keys: basal_energy_0.5deg, basal_energy_3deg, basal_energy_5deg, nonbasal_energy_0.5deg_b7.36, nonbasal_energy_4deg_b7.36, nonbasal_energy_0.5deg_b8.63, nonbasal_energy_4deg_b8.63, threshold_angle_basal, threshold_angle_nonbasal. All values are positive numbers (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_estimates.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_estimates.json
- path: `/app/outputs/energy_estimates.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed grain boundary energies and GB‑subGB threshold misorientation angles using the simple upper‑bound model.
- schema:
  - `type`: object
  - `required`: `basal_energy_0.5deg`, `basal_energy_3deg`, `basal_energy_5deg`, `nonbasal_energy_0.5deg_b7.36`, `nonbasal_energy_4deg_b7.36`, `nonbasal_energy_0.5deg_b8.63`, `nonbasal_energy_4deg_b8.63`, `threshold_angle_basal`, `threshold_angle_nonbasal`
  - `properties`:
    - `basal_energy_0.5deg`:
      - `type`: number
      - `minimum`: 0
      - `description`: Grain boundary energy for basal dislocations at 0.5° misorientation in mJ/m²
    - `basal_energy_3deg`:
      - `type`: number
      - `minimum`: 0
      - `description`: Grain boundary energy for basal dislocations at 3° misorientation in mJ/m²
    - `basal_energy_5deg`:
      - `type`: number
      - `minimum`: 0
      - `description`: Grain boundary energy for basal dislocations at 5° misorientation in mJ/m²
    - `nonbasal_energy_0.5deg_b7.36`:
      - `type`: number
      - `minimum`: 0
      - `description`: Grain boundary energy for nonbasal dislocations with b=7.36 Å at 0.5° in mJ/m²
    - `nonbasal_energy_4deg_b7.36`:
      - `type`: number
      - `minimum`: 0
      - `description`: Grain boundary energy for nonbasal dislocations with b=7.36 Å at 4° in mJ/m²
    - `nonbasal_energy_0.5deg_b8.63`:
      - `type`: number
      - `minimum`: 0
      - `description`: Grain boundary energy for nonbasal dislocations with b=8.63 Å at 0.5° in mJ/m²
    - `nonbasal_energy_4deg_b8.63`:
      - `type`: number
      - `minimum`: 0
      - `description`: Grain boundary energy for nonbasal dislocations with b=8.63 Å at 4° in mJ/m²
    - `threshold_angle_basal`:
      - `type`: number
      - `minimum`: 0
      - `description`: Threshold misorientation angle where γ reaches 65 mJ/m² for basal dislocations (b=4.52 Å) in degrees
    - `threshold_angle_nonbasal`:
      - `type`: number
      - `minimum`: 0
      - `description`: Threshold misorientation angle where γ reaches 65 mJ/m² for nonbasal dislocations (b=8.0 Å) in degrees

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_estimates.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "basal_energy_0.5deg",
          "basal_energy_3deg",
          "basal_energy_5deg",
          "nonbasal_energy_0.5deg_b7.36",
          "nonbasal_energy_4deg_b7.36",
          "nonbasal_energy_0.5deg_b8.63",
          "nonbasal_energy_4deg_b8.63",
          "threshold_angle_basal",
          "threshold_angle_nonbasal"
        ],
        "properties": {
          "basal_energy_0.5deg": {
            "type": "number",
            "minimum": 0,
            "description": "Grain boundary energy for basal dislocations at 0.5° misorientation in mJ/m²"
          },
          "basal_energy_3deg": {
            "type": "number",
            "minimum": 0,
            "description": "Grain boundary energy for basal dislocations at 3° misorientation in mJ/m²"
          },
          "basal_energy_5deg": {
            "type": "number",
            "minimum": 0,
            "description": "Grain boundary energy for basal dislocations at 5° misorientation in mJ/m²"
          },
          "nonbasal_energy_0.5deg_b7.36": {
            "type": "number",
            "minimum": 0,
            "description": "Grain boundary energy for nonbasal dislocations with b=7.36 Å at 0.5° in mJ/m²"
          },
          "nonbasal_energy_4deg_b7.36": {
            "type": "number",
            "minimum": 0,
            "description": "Grain boundary energy for nonbasal dislocations with b=7.36 Å at 4° in mJ/m²"
          },
          "nonbasal_energy_0.5deg_b8.63": {
            "type": "number",
            "minimum": 0,
            "description": "Grain boundary energy for nonbasal dislocations with b=8.63 Å at 0.5° in mJ/m²"
          },
          "nonbasal_energy_4deg_b8.63": {
            "type": "number",
            "minimum": 0,
            "description": "Grain boundary energy for nonbasal dislocations with b=8.63 Å at 4° in mJ/m²"
          },
          "threshold_angle_basal": {
            "type": "number",
            "minimum": 0,
            "description": "Threshold misorientation angle where γ reaches 65 mJ/m² for basal dislocations (b=4.52 Å) in degrees"
          },
          "threshold_angle_nonbasal": {
            "type": "number",
            "minimum": 0,
            "description": "Threshold misorientation angle where γ reaches 65 mJ/m² for nonbasal dislocations (b=8.0 Å) in degrees"
          }
        }
      },
      "description": "Computed grain boundary energies and GB‑subGB threshold misorientation angles using the simple upper‑bound model."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently recomputes the expected energy values and threshold angles using the same formulas and constants. The verifier compares your reported values against the reference results. A reward is assigned based on the accuracy of each value relative to the reference; larger deviations result in a lower score. The exact tolerances are predetermined and are generous enough to accommodate minor rounding differences, but you must follow the given formulas and unit conversions precisely to achieve the best score.
