# Critical Plane Prediction for Composite Laminae under Multiaxial Cyclic Loading

## Problem background
Continuous fiber-reinforced composites under multiaxial cyclic loading experience complex failure processes. Predicting the orientation of the fracture plane that ultimately causes failure is essential for fatigue design. This task focuses on a model that classifies planes within a unidirectional lamina into two types: Type I planes that cut the fibers and Type II planes that run parallel to the fibers. For each type, an effective stress is defined, and the plane with the larger maximum effective stress is taken as the critical plane. The goal is to implement the model and compute, for given lamina stress states and material strengths, the type of the critical plane and its orientation angles.

## Approach
The model defines effective stresses on each plane type based on the multiaxial stress state in the lamina, characterised by biaxiality ratios λ (σ12/σ22) and ς (σ11/σ22) and the cyclic stress ratios R22 and R12. For a Type I plane, the effective stress is the normal tensile stress on the plane, normalized by the static tensile strength along the fiber direction (σ_I^f). Its maximum over all orientations is obtained from piecewise closed-form expressions that depend on the biaxiality factors r1, r2 and the loading regime (σ22 nonzero, σ22 zero but σ11 nonzero, or pure shear). The plane orientation at this maximum is given by a formula involving λ and ς. For a Type II plane, the effective stress is the Euclidean sum of the normalized tensile stress (using transverse tensile strength σ_II^f) and the normalized shear stress (using in-plane shear strength τ_II^f). Its maximum is also found from piecewise expressions, and the maximizing orientation γ is determined by the loading case. The critical plane is the one yielding the larger maximum effective stress; its type and orientation (β for Type I, γ for Type II) are the prediction.

You must hardcode the lamina static strengths: σ_I^f = 980 MPa, σ_II^f = 48 MPa, τ_II^f = 70 MPa. For the ±55° filament-wound specimens under global biaxiality ratios λ_globe = 0.5, 1, 2 and global cyclic stress ratios R_globe = 0 and −1, the lamina-level biaxiality ratios λ and ς are derived from a laminate stress analysis and are provided as follows. The sign of σ12 (positive for (+) plies, negative for (−) plies) is also needed. For each ply and each R_globe, the lamina cyclic stress ratios R22 and R12 equal R_globe.

| λ_globe | ply | λ   | ς   |
|---------|-----|------|-----|
| 0.5     | (+) | −1.4 | 3.0 |
| 0.5     | (−) | 0.5  | −0.5|
| 1.0     | (+) | −2.8 | 9.2 |
| 1.0     | (−) | 0.4  | −1.3|
| 2.0     | (+) | 5.2  | −25 |
| 2.0     | (−) | 0.2  | −2.2|

The implementation should cover the complete set of piecewise cases for maximum effective stresses (including special forms when a stress component is zero) and the corresponding orientation formulas. Use the maximizing orientation rules for Type I (β from a tan⁻¹ expression; γ = π/2) and Type II (β = 0; γ from the appropriate case).

## Reproduction target
Compute the critical plane type (I or II) and the orientation angles β_c (radians) and γ_c (radians) for each of the 12 lamina loading conditions described above (both plies at each global loading and both R_globe values). Because the model formulas use σ22_max as a scale factor and its absolute value is not provided, assume σ22_max = 1.0 for normalization; thus the computed max_sigma_I_eq and max_sigma_II_eq are dimensionless effective stresses. Record both dimensionless effective stress maxima. Output the results to /app/outputs/critical_plane_predictions.csv with the columns condition_id, critical_plane_type, beta_c, gamma_c, max_sigma_I_eq, max_sigma_II_eq.

## Assets

- Python 3 with numpy: numpy

## Workflow steps

### Step 1: Define input conditions and material properties
- Role: process
- Action: Hardcode the lamina static strengths: σ_I^f = 980 MPa, σ_II^f = 48 MPa, τ_II^f = 70 MPa. For the ±55° filament-wound specimen conditions (global biaxiality ratios λ_globe = 0.5, 1, 2 and global stress ratios R_globe = 0 and -1), define the lamina biaxiality ratios λ and ς from the provided stress table, and set the lamina cyclic stress ratios R22 = R_globe, R12 = R_globe. Create a list of condition dictionaries, each with a unique condition_id, λ, ς, R22, R12, and the sign of σ12 (if positive or negative) as needed to determine the maximizing orientation cases. To obtain dimensionless effective stresses, assume a unit stress scale by setting σ22_max = 1.0.
- Evidence: none

### Step 2: Compute critical plane predictions
- Role: scored (load-bearing)
- Action: Implement the analytical model for effective stresses on Type I and Type II planes. For Type I, use the normal stress on a plane cutting fibers and compute the maximum tensile stress using the piecewise closed-form expressions that depend on biaxiality ratios and cyclic stress ratios, normalizing by σ_I^f. For Type II, use the normal and shear stresses on planes parallel to fibers and compute the maximum effective stress as the Euclidean sum of normalized tensile and shear components, using the piecewise expressions. Assume a unit stress scale by setting σ22_max = 1.0 so that the computed effective stresses are dimensionless. For each loading condition, determine the critical plane type (I or II) as the one with the larger maximum effective stress, and record the corresponding orientation angles (β for Type I from the maximizing formula, γ = π/2; γ for Type II from the maximizing formula, β = 0). Write the predictions to /app/outputs/critical_plane_predictions.csv with columns: condition_id, critical_plane_type, beta_c (radians), gamma_c (radians), max_sigma_I_eq (dimensionless), max_sigma_II_eq (dimensionless).
- Output file: `/app/outputs/critical_plane_predictions.csv`
- Format: csv
- Contract: condition_id (string), critical_plane_type (string: 'I' or 'II'), beta_c (float, radians), gamma_c (float, radians), max_sigma_I_eq (float, MPa), max_sigma_II_eq (float, MPa)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_plane_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_plane_predictions.csv
- path: `/app/outputs/critical_plane_predictions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of predicted critical plane type and orientation for each loading condition. The reference values are computed by the checker using the same analytical model and public input parameters. Effective stresses are dimensionless because σ22_max is set to 1.0.
- schema:
  - `type`: table
  - `required_columns`: `condition_id`, `critical_plane_type`, `beta_c`, `gamma_c`, `max_sigma_I_eq`, `max_sigma_II_eq`
  - `units`:
    - `beta_c`: radians
    - `gamma_c`: radians
    - `max_sigma_I_eq`: dimensionless
    - `max_sigma_II_eq`: dimensionless

Notes: The task omits the derivation of lamina elastic constants and the classical laminate stress analysis; lamina-level stress states are provided directly. Only the ±55° filament-wound specimen conditions are included because their cyclic stress ratios are explicitly stated. The computation is deterministic and uses only standard Python libraries. Effective stresses are dimensionless: σ22_max is assumed to be 1.0.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_plane_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition_id",
          "critical_plane_type",
          "beta_c",
          "gamma_c",
          "max_sigma_I_eq",
          "max_sigma_II_eq"
        ],
        "units": {
          "beta_c": "radians",
          "gamma_c": "radians",
          "max_sigma_I_eq": "dimensionless",
          "max_sigma_II_eq": "dimensionless"
        }
      },
      "description": "Table of predicted critical plane type and orientation for each loading condition. The reference values are computed by the checker using the same analytical model and public input parameters. Effective stresses are dimensionless because σ22_max is set to 1.0."
    }
  ],
  "notes": "The task omits the derivation of lamina elastic constants and the classical laminate stress analysis; lamina-level stress states are provided directly. Only the ±55° filament-wound specimen conditions are included because their cyclic stress ratios are explicitly stated. The computation is deterministic and uses only standard Python libraries. Effective stresses are dimensionless: σ22_max is assumed to be 1.0."
}
```

## How you are scored
A hidden verifier independently implements the same analytical model using the identical input conditions and material strengths. For every condition, it recomputes the maximum effective stresses and the critical plane type and orientation. It checks that the reported critical_plane_type matches the recomputed one exactly, and that beta_c, gamma_c, max_sigma_I_eq, and max_sigma_II_eq fall within hidden tolerance bands. The verifier also confirms internal consistency (e.g., the chosen critical plane type corresponds to the larger of the two maximum effective stresses). Your reward is the fraction of conditions that pass all checks.
