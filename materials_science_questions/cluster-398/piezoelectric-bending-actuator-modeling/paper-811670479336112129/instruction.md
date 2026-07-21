# Critical buckling temperature of piezoelectric composite beam

## Problem background
This task investigates thermal buckling of laminated composite beams that incorporate surface-bonded piezoelectric actuator layers. When a beam is subjected to a uniform temperature rise, thermal expansion induces compressive axial forces. If these forces become large enough, the beam may buckle—suddenly deflect laterally—leading to structural failure. Piezoelectric layers, when an external voltage is applied, generate additional axial forces that can either increase or decrease the buckling resistance. The goal is to compute the critical temperature rise ΔT_cr (in °C) at which buckling occurs for several beam configurations under different mechanical boundary conditions and applied voltages. Understanding how geometry, material layup, boundary conditions, and actuator voltage influence buckling temperature is essential for designing smart composite structures with controllable thermal stability.

## Approach
The analysis is based on first-order shear deformation (Timoshenko) beam theory, which accounts for transverse shear effects. The beam is treated as a laminated composite with each layer defined by its material elastic constants, ply angle, and thickness. The displacement field includes axial displacement u, lateral deflection w, and cross-section rotation φ. The governing equations are derived from the principle of minimum total potential energy. To determine the buckling condition, the adjacent-equilibrium criterion is employed: a small perturbation is superimposed on the flat prebuckling state and the stability equations are solved. For a beam under uniform temperature rise and applied piezoelectric voltage, the prebuckling axial force is uniform, and the critical buckling force satisfies a transcendental equation whose smallest root yields a stability parameter μ_min depending only on the boundary condition. The critical temperature rise is then obtained by balancing the thermal force resultant (proportional to the temperature change and the laminate’s thermal expansion properties) and the piezoelectric force resultant (proportional to the applied voltage and piezoelectric constant) against the beam’s bending stiffness, coupling stiffness, and transverse shear stiffness. All laminate stiffness coefficients (A11, B11, D11, A55) are computed from the individual ply properties using standard lamination theory. The workflow will implement this analytical model: first compute the stiffness coefficients for each beam configuration, then for every required combination of boundary condition, voltage, and thickness solve for ΔT_cr and write the results to a CSV file.

## Reproduction target
You must compute the critical buckling temperature rise ΔT_cr (in °C) for the following configurations and write the results to `/app/outputs/critical_buckling_temperatures.csv`:

1. **Aluminium beam with surface-bonded PZT-5A layers** (total thickness 0.01 m, actuator layer thickness 0.001 m, length 0.25 m). Compute ΔT_cr for all five boundary conditions: S-S, C-C, C-S, C-R, S-R, and each of the five voltages: 0, 200, -200, 500, -500 V.
2. **Three-layered cross-ply (0/90/0) glass-epoxy beam with two PZT-5A layers** (total thickness 0.0045 m, actuator thickness 0.001 m, length 0.25 m). Same five boundary conditions and five voltages as above.
3. **Antisymmetric four-layered (0/90/0/90) glass-epoxy beam with one PZT-5A layer on the top surface** (total thickness 0.004 m, actuator thickness 0.001 m, length 0.25 m). Compute ΔT_cr for boundary conditions C-C and C-R, and all five voltages.
4. **Same antisymmetric four-layered beam as in 3, but with two PZT-5A layers** (top and bottom surfaces). Same boundary conditions and voltages as in 3.
5. **Thickness study for the three-layered cross-ply (0/90/0) glass-epoxy beam with two PZT-5A layers** at three total beam thicknesses: 0.003 m, 0.0045 m, and 0.006 m (actuator thickness remains 0.001 m, length 0.25 m). Compute ΔT_cr for all five boundary conditions at 0 V only.

The output CSV must contain the columns: `beam_type`, `layup_description`, `boundary_condition`, `voltage_V`, `thickness_m`, `delta_T_cr_C`. Use the provided material properties for aluminium, glass-epoxy, and PZT-5A (elastic constants, thermal expansion coefficients, piezoelectric constant, shear correction factor k=5/6) and the analytical μ_min values: μ_min L = π for S-S and C-R, 2π for C-C, 4.49341 for C-S, and π/2 for S-R. The beam width c cancels in the final equation and need not be specified explicitly.

## Assets

- Material constants and beam geometry for aluminium, PZT-5A, and glass-epoxy

## Workflow steps

### Step 1: Compute laminate stiffness coefficients
- Role: process
- Action: For each beam configuration (aluminium beam with surface-bonded PZT-5A layers, three-layer (0/90/0) glass-epoxy beam with two PZT-5A layers, four-layer (0/90/0/90) glass-epoxy beam with one PZT-5A layer on top, the same with two PZT-5A layers top/bottom, and the three-layer cross-ply beam at three total thicknesses 0.003, 0.0045, 0.006 m), compute the laminate extensional stiffness A11, bending-extension coupling B11, bending stiffness D11, and transverse shear stiffness A55 using first-order shear deformation theory formulas with the assigned material properties, ply angles, and thicknesses. Write results to stiffness_coefficients.csv.
- Evidence: `/app/outputs/stiffness_coefficients.csv`

### Step 2: Compute critical buckling temperatures
- Role: scored (load-bearing)
- Action: Using the stiffness coefficients from step_01, compute the critical buckling temperature rise ΔT_cr for all configurations: (a) aluminium beam with surface-bonded PZT-5A layers, five boundary conditions (S-S, C-C, C-S, C-R, S-R) and five voltages (0, ±200, ±500 V); (b) three-layered cross-ply (0/90/0) glass-epoxy beam with two piezoelectric layers, same BCs and voltages; (c) antisymmetric four-layered (0/90/0/90) glass-epoxy beam with one piezoelectric layer, BCs C-C and C-R, five voltages; (d) same antisymmetric beam with two piezoelectric layers, BCs C-C and C-R, five voltages; (e) three-layered cross-ply beam with two piezoelectric layers at three thicknesses (0.003, 0.0045, 0.006 m) and all five BCs at 0 V. For each case: use the analytical boundary condition buckling parameter μ_min (μ_min L = π for S-S and C-R, 2π for C-C, 4.49341 for C-S, π/2 for S-R), compute thermal force resultant N^T and piezoelectric force resultant N^E, and solve the buckling condition N^T+N^E = μ^2(D11 - B11^2/A11) / (1 + μ^2/A55(D11 - B11^2/A11)) for ΔT_cr. Write results to critical_buckling_temperatures.csv.
- Output file: `/app/outputs/critical_buckling_temperatures.csv`
- Format: csv
- Contract: CSV with columns: beam_type (string, one of: 'aluminium', 'three-layer-cross-ply', 'four-layer-antisymmetric-1piezo', 'four-layer-antisymmetric-2piezo', 'thickness-study-three-layer-cross-ply'), layup_description (string), boundary_condition (string: 'S-S','C-C','C-S','C-R','S-R'), voltage_V (float), thickness_m (float), delta_T_cr_C (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_buckling_temperatures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_buckling_temperatures.csv
- path: `/app/outputs/critical_buckling_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Contains the computed critical buckling temperature rise ΔT_cr for all beam configurations, boundary conditions, voltages, and thicknesses specified in the task. Each row is a configuration; the checked value is delta_T_cr_C.
- schema:
  - `type`: table
  - `required_columns`: `beam_type`, `layup_description`, `boundary_condition`, `voltage_V`, `thickness_m`, `delta_T_cr_C`
  - `units`:
    - `voltage_V`: V
    - `thickness_m`: m
    - `delta_T_cr_C`: degree Celsius

Notes: Only the critical buckling temperatures are scored. The intermediate stiffness coefficients are a required process step but are not part of the scored contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_buckling_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "beam_type",
          "layup_description",
          "boundary_condition",
          "voltage_V",
          "thickness_m",
          "delta_T_cr_C"
        ],
        "units": {
          "voltage_V": "V",
          "thickness_m": "m",
          "delta_T_cr_C": "degree Celsius"
        }
      },
      "description": "Contains the computed critical buckling temperature rise ΔT_cr for all beam configurations, boundary conditions, voltages, and thicknesses specified in the task. Each row is a configuration; the checked value is delta_T_cr_C."
    }
  ],
  "notes": "Only the critical buckling temperatures are scored. The intermediate stiffness coefficients are a required process step but are not part of the scored contract."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/critical_buckling_temperatures.csv` and compares each `delta_T_cr_C` value against a hidden reference value (the correct critical temperature for that configuration). Each row is evaluated independently; a row is considered correct if the absolute difference between your computed value and the reference is within a prescribed tolerance. Your final score is the fraction of rows that pass this check (a number between 0 and 1). The intermediate stiffness coefficients file is inspected only for process evidence and does not directly contribute to the score. Submitting the correct numbers without executing the required analysis will not satisfy the scoring criteria because the verifier checks the entire pipeline's output consistency.
