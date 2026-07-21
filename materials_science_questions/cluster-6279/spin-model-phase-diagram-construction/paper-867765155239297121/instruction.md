# Mean-Field Phase Diagram and Tricritical Points for Antagonistic Nematogens

## Problem background
This task addresses the phase behavior of antagonistic nematogens – molecules whose interactions favor both parallel and mutually perpendicular orientations – under an external field that disfavours alignment along the field axis. The model consists of uniaxial hard spheres with a pure fourth-order anisotropic pair potential (no P2 term) and a disorienting field of strength W > 0 that penalizes orientation parallel to the field. A mean-field theory predicts that at sufficiently strong fields a new nematic phase with fourfold rotational symmetry (denoted N_{+4}) may appear at intermediate densities, separating a low-density planar uniaxial phase from a high-density biaxial phase. The task is to compute the phase diagram and determine the tricritical points where the transition into the biaxial phase changes order, and to verify the existence of the N_{+4} phase by examining order parameters.

## Approach
Use the mean-field free-energy functional for a single-particle orientational distribution on the unit sphere, including the hard-sphere reference free energy (Carnahan–Starling) and an anisotropic contribution from the pure P4 pair interaction. The disorienting field couples to the second Legendre polynomial of cos θ. Minimization yields a self-consistent integral equation for the equilibrium distribution and order parameters S_z (uniaxial order along the field axis), S_x (biaxial order in the plane), and S_xy (fourfold in-plane order). Solve this equation by numerical quadrature and iteration. For each specified field strength, scan a dense grid of packing fraction η and reduced temperature T*, compute the free energy and order parameters, and apply a common-tangent construction to map coexistence regions, continuous transitions, tricritical points, and critical end points. Finally, extract the tricritical coordinates and a one-dimensional slice of order parameters at a fixed field and temperature to confirm the structural signature of the N_{+4} phase.

## Reproduction target
For the system with A2 = 0 and four field strengths W/A4 = 1, 2, 5, 50, compute the tricritical point coordinates (reduced temperature T*, packing fraction η, and reduced pressure P*) and write them as a CSV. Separately, for W/A4 = 2 and fixed reduced temperature T* = 1.5, compute the order parameters S_z, S_x, and S_xy as functions of η over a range that covers the putative N_{+4} regime and write the results to a CSV. These outputs allow verification of the tricritical behaviour and the existence of the N_{+4} phase.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Implement self-consistent mean-field solver
- Role: process
- Action: Implement the mean-field free energy functional and the self-consistent equation for the single-particle orientational distribution of uniaxial hard spheres with a pure P4 anisotropic interaction (A2=0) and a disorienting field W>0. Use numerical quadrature over the orientational sphere and iterate to convergence to obtain the equilibrium orientational distribution, the order parameters S_z, S_x, S_xy, and the free energy contribution ΔF at given packing fraction η, reduced temperature T*, and field strength W/A4.
- Evidence: `/app/outputs/solver.log`

### Step 2: Phase diagram scan and common-tangent analysis
- Role: process
- Action: For each field strength W/A4 = 1, 2, 5, 50, perform a dense grid scan over packing fraction η and reduced temperature T*. At every grid point use the solver to compute ΔF and the order parameters. Apply a common-tangent construction to determine phase coexistence (binodals) and trace second-order transition lines. Identify the tricritical point where the N_{+4}/N_b transition changes from second- to first-order, and locate critical end points. Save the full free-energy landscapes and phase boundaries for downstream extraction.
- Evidence: `/app/outputs/phase_scan.npz`

### Step 3: Extract tricritical point coordinates
- Role: scored (load-bearing)
- Action: From the phase-diagram analysis, extract the tricritical temperature T*, density η, and pressure P* for the four field strengths (W/A4 = 1,2,5,50) and write them to a CSV file.
- Output file: `/app/outputs/tricritical_points.csv`
- Format: csv
- Contract: Columns: W_over_A4 (float), T_star (float), eta (float), P_star (float). One row per field strength.
- Scoring: scored by hidden verifier

### Step 4: Compute order parameters at W/A4=2, T*=1.5
- Role: scored
- Action: For the field strength W/A4=2 and reduced temperature T*=1.5, compute the order parameters S_z, S_x, S_xy as functions of η over a range covering the N_{+4} phase. Write the results to a CSV file.
- Output file: `/app/outputs/order_parameters_W2_T15.csv`
- Format: csv
- Contract: Columns: eta (float), S_z (float), S_x (float), S_xy (float). Multiple rows covering a dense η sweep.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tricritical_points.csv`
- `/app/outputs/order_parameters_W2_T15.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tricritical_points.csv
- path: `/app/outputs/tricritical_points.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Tricritical point coordinates for four disorienting field strengths.
- schema:
  - `type`: table
  - `required_columns`: `W_over_A4`, `T_star`, `eta`, `P_star`

### order_parameters_W2_T15.csv
- path: `/app/outputs/order_parameters_W2_T15.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Order parameters vs. packing fraction at W/A4=2, T*=1.5, confirming the N_{+4} phase region.
- schema:
  - `type`: table
  - `required_columns`: `eta`, `S_z`, `S_x`, `S_xy`

Notes: The verifier compares the tricritical points to hidden reference values with appropriate tolerances, and checks the order-parameter slice for the structural signature of the N_{+4} phase (contiguous η interval with S_z<−0.2, |S_x|<0.05, S_xy>0.1, and S_xy→0 at extremes).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tricritical_points.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "W_over_A4",
          "T_star",
          "eta",
          "P_star"
        ]
      },
      "description": "Tricritical point coordinates for four disorienting field strengths."
    },
    {
      "file": "order_parameters_W2_T15.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "eta",
          "S_z",
          "S_x",
          "S_xy"
        ]
      },
      "description": "Order parameters vs. packing fraction at W/A4=2, T*=1.5, confirming the N_{+4} phase region."
    }
  ],
  "notes": "The verifier compares the tricritical points to hidden reference values with appropriate tolerances, and checks the order-parameter slice for the structural signature of the N_{+4} phase (contiguous η interval with S_z<−0.2, |S_x|<0.05, S_xy>0.1, and S_xy→0 at extremes)."
}
```

## How you are scored
Each scored artifact is independently assessed by a hidden verifier. The tricritical point CSV is compared against reference values with appropriate tolerances for T*, η, and P*. The order-parameter CSV undergoes a structural audit: the verifier checks that a contiguous interval of η exists where S_z is sufficiently negative, |S_x| is near zero, and S_xy is clearly positive, with S_xy approaching zero at the extremes of the sweep. The final reward is a weighted combination of the per‑artifact scores; reporting correct numbers alone is not sufficient – the underlying computation must be sound and produce the required structural features.
