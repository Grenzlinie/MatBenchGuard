# Arlequin Coupling: Displacement of a Periodic Particle-Continuum System

## Problem background
The Arlequin method is a flexible framework for coupling different physical models in overlapping domains using Lagrange multipliers. This task focuses on coupling a one-dimensional discrete particle model (a chain of harmonic springs) with a continuum model (a linear elastic bar). The coupling is achieved by introducing an overlap region where the two descriptions coexist, and a constraint couples the displacements via a chosen norm. The quality of the coupling depends on whether the constraint is based on the L² norm, H¹ seminorm, or H¹ norm. In this work we study the H¹ seminorm and H¹ norm coupling strategies for a periodic spring system with two alternating stiffness constants. The objective is to compute the displacement at the rightmost particle, which illuminates the numerical behaviour of the method under different coupling regularisations.

## Approach
The problem geometry consists of a total domain Ω = (0,3). A particle model of m = 8 harmonic springs with periodic stiffnesses k₁ = 100, k₂ = 1 and equilibrium length l = 0.25 occupies Ω_d = (1,3), while a continuum linear elastic bar occupies Ω_c = (0,2). The two models overlap on Ω_o = (1,2). Weight functions α_c(x) and α_d(x) = 1−α_c(x) linearly blend the models’ contributions in the overlap; α_c(x) = 1− (x−1) on [1,2].

First, an effective Young’s modulus E for the continuum is derived by homogenisation of the periodic spring cell: E = (k₁ k₂ / (k₁ + k₂)) × 2l. The continuum is discretised with 4 linear finite elements on Ω_c (mesh size h = 0.5). The particle displacements w are converted to a continuous field Πw by linear interpolation. The coupling constraint is enforced via a Lagrange multiplier defined on the same mesh as the continuum (continuum coupling). The coupling term measures the mismatch between u and Πw on Ω_o in the H¹ space, weighted by parameters β₁ and β₂. Two coupling regimes are considered: H¹ seminorm (β₁ = 0, β₂ = 1) and H¹ norm (β₁ = 1, β₂ = 1).

The mixed finite element formulation yields a saddle-point linear system for the continuum displacement u_h, the particle displacements w_h, and the Lagrange multipliers λ_h. Solving this system for the two (β₁,β₂) sets gives the coupled displacement field. The particle displacement at the right endpoint x = 3 is extracted for each case.

## Reproduction target
Compute the particle displacement at x = 3 for the periodic spring/continuum system described above, under H¹ seminorm coupling (β₁ = 0, β₂ = 1) and H¹ norm coupling (β₁ = 1, β₂ = 1). Store the two values in `/app/outputs/displacement_results.json` with keys `h1_seminorm_z3` and `h1_norm_z3`.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Homogenization to compute effective Young's modulus
- Role: process
- Action: Compute the continuum Young's modulus E from the periodic spring constants using the energy equivalence formula for a representative cell of two springs (k1=100, k2=1, equilibrium length l=0.25). The formula gives E = (k1*k2/(k1+k2)) * 2l. Save the computed modulus for use in the next step.
- Evidence: `/app/outputs/homogenized_modulus.txt`

### Step 2: Solve Arlequin coupled problem and extract displacements
- Role: scored (load-bearing)
- Action: Assemble the finite element discretization of the 1D Arlequin saddle-point system for the given geometry (Ω_c=(0,2), Ω_d=(1,3), overlap Ω_o=(1,2)), springs (m=8, periodic k1=100, k2=1, l=0.25), continuum modulus E from step_homogenize, mesh size h=0.5 (4 linear elements on Ω_c) with continuum coupling for the Lagrange multiplier space, and linear weight functions α_c, α_d. Solve the resulting linear system for two coupling parameter sets: (β1=0, β2=1) and (β1=1, β2=1). Extract the particle displacement at the rightmost node (x=3) for each case and write them to the output file.
- Output file: `/app/outputs/displacement_results.json`
- Format: json
- Contract: {"h1_seminorm_z3": float, "h1_norm_z3": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/displacement_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### displacement_results.json
- path: `/app/outputs/displacement_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The particle displacement at x=3 for H1 seminorm and H1 norm coupling, computed at mesh size h=0.5. The checker compares each value to hidden paper-reported references within an absolute tolerance.
- schema:
  - `type`: object
  - `required`:
    - `h1_seminorm_z3`: float
    - `h1_norm_z3`: float
  - `units`:
    - `h1_seminorm_z3`: dimensionless (normalized displacement)
    - `h1_norm_z3`: dimensionless (normalized displacement)

Notes: The solver must implement the Arlequin saddle-point assembly and solution as described. The homogenized modulus must be computed from the given spring parameters. No external datasets are required; the problem setup is fully specified in the instruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "displacement_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "h1_seminorm_z3": "float",
          "h1_norm_z3": "float"
        },
        "units": {
          "h1_seminorm_z3": "dimensionless (normalized displacement)",
          "h1_norm_z3": "dimensionless (normalized displacement)"
        }
      },
      "description": "The particle displacement at x=3 for H1 seminorm and H1 norm coupling, computed at mesh size h=0.5. The checker compares each value to hidden paper-reported references within an absolute tolerance."
    }
  ],
  "notes": "The solver must implement the Arlequin saddle-point assembly and solution as described. The homogenized modulus must be computed from the given spring parameters. No external datasets are required; the problem setup is fully specified in the instruction."
}
```

## How you are scored
The completed task is evaluated by a hidden verifier that inspects the output files you write under `/app/outputs`. For the scored displacement file, the verifier reads the two displacement values and compares them to independently determined reference values using an absolute tolerance. If both displacements lie within the tolerance, full credit is awarded for that stage; otherwise a fraction is given based on how many are within tolerance. The overall reward is the weighted sum of the stage scores (here the displacement file is the only scored stage, so it carries all the weight). Simply reporting a number without correctly constructing and solving the Arlequin system will not meet the tolerance. No additional information about the reference values or the tolerance is provided.
