# Crumpling energy of a single 2D sheet from rotational spring-slider model

## Problem background
Evaporation of liquid droplets that contain suspended two-dimensional (2D) material sheets can drive crumpling and self-assembly into aggregation-resistant particles. A rotational spring–mechanical slider model has been proposed to quantify the out-of-plane deformation energy and van der Waals binding energy of a single sheet during droplet evaporation. This task focuses on the single-sheet case. By computing the total energy of the system as a function of droplet curvature and identifying the critical sheet area for folding, we can understand the conditions under which the sheet stays folded or unfolds. The outcome is a numerical evaluation of the energy contributions and the critical parameters that mark the folding transition.

## Approach
The rotational spring model describes the out-of-plane strain energy of the sheet via a rotational spring constant that depends on the sheet's area, bending stiffness, Young's modulus, thickness, and the evaporation pressure. The following equations define the model:

- Droplet radius: R_d = 1/κ_d (where κ_d is curvature).
- Projected area: A_pr = (B R_d / P_t)^{1/4} π L_g / 2.
- Projected area on droplet surface: A_s = 2π R_d^2 [1 - cos(L_g/(2 R_d))].
- Deformed area: A_def = A_pr + (π A_g / 4) - A_s.
- Nominal compressive strain: ε_s = (A_pr - A_def)/A_def (negative).
- Rotational angle: θ_t = π(1 + ε_s).
- Critical angle for binding energy: θ_t^c = π / (1 + (E/(P_t A_pr^2))^{1/9} t^{4/9}).
- Spring constant: k_s = 2 B (A_g / t^2) sqrt(P_t / E).
- Spring energy: E_s^{spring} = ½ k_s (θ_t - π)^2.
- Slider (binding) energy: E_b^{slider} = (Γ_b/2) A_def [sin(θ_t^c/2) - sin(θ_t/2)] if θ_t < θ_t^c, else 0.
- Potential energy: E_p = P_t [A_def (R_d + sqrt(A_def) cos(θ_t/2)/2) + A_s R_d].
- Total energy: E_tot = E_s^{spring} + E_b^{slider} + E_p.

The critical sheet area for folding is derived from the energy balance:
A_g^c = η (B / P_t)^{2/3} with η = 98.82 for highly localized deformation.

The procedure numerically evaluates the energies over a range of droplet curvatures, determines the critical area, and finds the curvature (if any) where dE_tot/dκ_d = 0. This reveals whether the sheet will remain folded or bounce back.

## Reproduction target
Implement the rotational spring–mechanical slider model for a single square graphene sheet. Using the material parameters B=2.38e-19 J, E=1 TPa, t=0.34 nm, Γ_b=−0.232 J/m², and a sheet size L_g=40 nm under an evaporation pressure P_t=10 atm, compute the total energy and its components as a function of droplet curvature from 0 to 0.1 nm⁻¹. Then determine the critical area for folding from the model's area–pressure–bending stiffness relation, and numerically find the curvature where the derivative of the total energy with respect to curvature is zero (if any). For each point, also report the rotational angle and critical angle. The results are written into two files: `energy_vs_curvature.csv` and `critical_condition.txt`.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute energy vs. curvature
- Role: scored
- Action: For a single square graphene sheet with L_g=40 nm, P_t=10 atm, B=2.38e-19 J, E=1 TPa, t=0.34 nm, Γ_b=−0.232 J/m², compute the total energy E_tot = E_s^{spring} + E_b^{slider} + E_p as a function of droplet curvature κ_d from 0 to 0.1 nm⁻¹ (at least 20 equally spaced points). Use the paper's formulas for spring constant k_s, critical angle θ_t^c, rotational angle θ_t, spring energy, slider energy, and potential energy. Output the curvature (nm⁻¹), total_energy (J), spring_energy (J), slider_energy (J), potential_energy (J), rotational_angle (rad), critical_angle (rad) as a CSV.
- Output file: `/app/outputs/energy_vs_curvature.csv`
- Format: csv
- Contract: Columns: curvature_1_per_nm, total_energy_J, spring_energy_J, slider_energy_J, potential_energy_J, rotational_angle_rad, critical_angle_rad. At least 20 rows covering curvatures from 0 to 0.1 nm⁻¹.
- Scoring: scored by hidden verifier

### Step 2: Determine critical parameters
- Role: scored
- Action: From the same model, compute the critical area A_g^c using Eq. 22 with η=98.82. Numerically find the curvature κ_d^E where dE_tot/dκ_d=0 (if any); if no root exists, output 'No root'. Also output the rotational angle θ_t and critical angle θ_t^c at that curvature (if a root exists).
- Output file: `/app/outputs/critical_condition.txt`
- Format: txt
- Contract: Line 1: A_g_c = <value> nm²
Line 2: kappa_d_E = <value> nm⁻¹ (or 'No root')
Line 3: theta_t at kappa_d_E = <value> rad (if root exists)
Line 4: theta_t^c = <value> rad
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_vs_curvature.csv`
- `/app/outputs/critical_condition.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_vs_curvature.csv
- path: `/app/outputs/energy_vs_curvature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Energy components and angles as a function of droplet curvature. The checker compares the total energy values at sampled curvatures to hidden gold values using MAPE within 10%.
- schema:
  - `type`: table
  - `required_columns`: `curvature_1_per_nm`, `total_energy_J`, `spring_energy_J`, `slider_energy_J`, `potential_energy_J`, `rotational_angle_rad`, `critical_angle_rad`

### critical_condition.txt
- path: `/app/outputs/critical_condition.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Critical area and root information. The checker compares A_g_c to the paper's Eq. 22 value within 2% and verifies that kappa_d_E is 'No root' (expected for these parameters).
- schema:
  - `type`: text
  - `description`: Four lines: A_g_c (nm²), kappa_d_E (nm⁻¹ or 'No root'), theta_t at that curvature (rad, if root exists), theta_t^c (rad).

Notes: The hidden gold values are extracted from the paper's Fig. 5a and Eq. 22. The solver must implement the model equations; no external datasets are needed. The agent's discretisation and root-finding choices are free as long as the output exceeds the minimum number of points.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_vs_curvature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "curvature_1_per_nm",
          "total_energy_J",
          "spring_energy_J",
          "slider_energy_J",
          "potential_energy_J",
          "rotational_angle_rad",
          "critical_angle_rad"
        ]
      },
      "description": "Energy components and angles as a function of droplet curvature. The checker compares the total energy values at sampled curvatures to hidden gold values using MAPE within 10%."
    },
    {
      "file": "critical_condition.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Four lines: A_g_c (nm²), kappa_d_E (nm⁻¹ or 'No root'), theta_t at that curvature (rad, if root exists), theta_t^c (rad)."
      },
      "description": "Critical area and root information. The checker compares A_g_c to the paper's Eq. 22 value within 2% and verifies that kappa_d_E is 'No root' (expected for these parameters)."
    }
  ],
  "notes": "The hidden gold values are extracted from the paper's Fig. 5a and Eq. 22. The solver must implement the model equations; no external datasets are needed. The agent's discretisation and root-finding choices are free as long as the output exceeds the minimum number of points."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that examines each scored output independently. For `energy_vs_curvature.csv`, the verifier compares your computed total energy values at a set of curvature points to reference values using an appropriate error metric; your numbers must fall within an acceptable margin. For `critical_condition.txt`, the verifier checks the reported critical area against the expected value derived from the model's equation and confirms whether the curvature where dE/dκ=0 exists or is reported as 'No root'; it also validates the rotational angle condition at that point. The scores from both stages are combined with weights to produce the final reward. Submitting approximate or guessed values will not pass; you must faithfully implement the model and compute the quantities from the given parameters.
