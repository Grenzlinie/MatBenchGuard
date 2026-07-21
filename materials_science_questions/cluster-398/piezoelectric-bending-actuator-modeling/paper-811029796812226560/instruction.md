# Piezoelectric bending actuator modeling using Hermite-type RPIM

## Problem background
Piezoelectric ceramics deform when an electric field is applied, making them suitable for micro-actuators and sensors. Accurate modeling of their coupled electro-mechanical behavior requires solving the two-dimensional governing equations that relate mechanical displacements, electric potential, and material constants. The Hermite-type radial point interpolation method (RPIM) is a meshless numerical technique that discretizes the problem domain with scattered nodes instead of a mesh, and constructs displacement and potential approximations using radial basis functions and polynomial terms, incorporating derivative information at the boundary. This task reproduces the numerical simulation of a PVDF bimorph actuator: a two-layer beam 10 μm long and 1 μm thick, subjected to an applied voltage. The goal is to compute the vertical (z-direction) displacement distribution within the bimorph, as well as the tip deflection of a dual-bimorph mirror device under a range of voltages.

## Approach
Implement the Hermite-type RPIM for two-dimensional piezoelectric coupling. Use PVDF material constants (c11=2.18e‑3 N/µm², c13=6.33e‑4, c33=2.18e‑3, c55=7.75e‑4, e31=4.6e‑8 N/(V·µm), e33=4.6e‑8, ξ11=ξ33=1.062e‑10 N/V²). Discretize the bimorph geometry (10 µm × 1 µm, two layers each 0.5 µm thick) with a set of nodes; include derivative (DB) boundary nodes where appropriate. Construct interpolation functions for the displacements u, w and the electric potential φ using a combination of radial basis functions, polynomial terms, and normal-derivative boundary contributions. Introduce correction coefficients μ and η to improve accuracy, and determine all unknown coefficients via a weighted least-squares procedure that enforces the governing equilibrium equations and the electrical/mechanical boundary conditions. Assemble the global stiffness matrix and solve the linear system for the nodal displacements and potential. For the bimorph under 1 V, extract w at the required (x,z) grid. For the dual-bimorph device, model the two coupled bimorph layers with the applied voltages and extract the tip displacement.

## Reproduction target
Produce two CSV files.
1) `w_displacements_1V.csv`: the z-displacement w (in µm) at coordinates x = 0.0, 1.0, …, 10.0 µm and z = 0.0, 0.5, 1.0 µm (33 rows) for a single 10 µm × 1 µm PVDF bimorph under 1 V.
2) `tip_displacements.csv`: the tip displacement (w at x=10 µm, z=0 of the top layer) in µm for the dual-bimorph mirror device (two identical bimorphs connected by a mirror) at applied voltages of 0, 1, 2, 5, 10, 15, 20, 25, and 50 V (9 rows).

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute bimorph w-displacements under 1V
- Role: scored (load-bearing)
- Action: Implement the Hermite-type RPIM for 2D piezoelectric equations using PVDF material constants (c11=2.18e-3 N/µm², c13=6.33e-4, c33=2.18e-3, c55=7.75e-4, e31=4.6e-8 N/(V·µm), e33=4.6e-8, ξ11=ξ33=1.062e-10 N/V²), bimorph geometry (length 10 µm, two layers each 0.5 µm thick), and boundary conditions with 1V applied. Discretize the domain with nodes, solve for displacements and potential, and extract z-direction displacement (w) at coordinates: z = 0.0, 0.5, 1.0 µm, for x = 0.0 to 10.0 µm in 1.0 µm steps. Write results to w_displacements_1V.csv.
- Output file: `/app/outputs/w_displacements_1V.csv`
- Format: csv
- Contract: CSV with columns: x (float, µm), z (float, µm), w (float, µm). Rows: for each combination of x in [0,1,...,10] and z in [0.0,0.5,1.0] (33 rows).
- Scoring: scored by hidden verifier

### Step 2: Compute dual-bimorph tip displacements under varying voltages
- Role: scored (load-bearing)
- Action: Using the same RPIM implementation, model the dual-bimorph mirror device consisting of two identical 10 µm × 1 µm bimorphs connected by a 1 µm mirror. For each applied voltage in [0, 1, 2, 5, 10, 15, 20, 25, 50] V, compute the tip displacement (w displacement at x=10 µm, z=0 µm of the top layer). Write results to tip_displacements.csv.
- Output file: `/app/outputs/tip_displacements.csv`
- Format: csv
- Contract: CSV with columns: voltage (float, V), tip_displacement (float, µm). Rows: one for each voltage in [0,1,2,5,10,15,20,25,50] (9 rows).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/w_displacements_1V.csv`
- `/app/outputs/tip_displacements.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### w_displacements_1V.csv
- path: `/app/outputs/w_displacements_1V.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: z-direction displacement of the PVDF bimorph at specified (x,z) grid points under 1V applied voltage.
- schema:
  - `type`: table
  - `required_columns`: `x`, `z`, `w`
  - `units`:
    - `x`: µm
    - `z`: µm
    - `w`: µm

### tip_displacements.csv
- path: `/app/outputs/tip_displacements.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Tip displacement (w at x=10 µm, z=0 µm) of the dual-bimorph device at different voltages.
- schema:
  - `type`: table
  - `required_columns`: `voltage`, `tip_displacement`
  - `units`:
    - `voltage`: V
    - `tip_displacement`: µm

Notes: The checker will compare each computed value to the paper-reported Hermite-type RPIM values with appropriate tolerances and verify monotonic trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "w_displacements_1V.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "z",
          "w"
        ],
        "units": {
          "x": "µm",
          "z": "µm",
          "w": "µm"
        }
      },
      "description": "z-direction displacement of the PVDF bimorph at specified (x,z) grid points under 1V applied voltage."
    },
    {
      "file": "tip_displacements.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "voltage",
          "tip_displacement"
        ],
        "units": {
          "voltage": "V",
          "tip_displacement": "µm"
        }
      },
      "description": "Tip displacement (w at x=10 µm, z=0 µm) of the dual-bimorph device at different voltages."
    }
  ],
  "notes": "The checker will compare each computed value to the paper-reported Hermite-type RPIM values with appropriate tolerances and verify monotonic trends."
}
```

## How you are scored
A hidden checker reads your output files. For `w_displacements_1V.csv`, it compares your w values point-by-point against a reference with a fixed absolute tolerance and checks that at each z level w increases monotonically with x. For `tip_displacements.csv`, it compares your tip displacement values against a reference with a stricter absolute tolerance and verifies that tip displacement increases monotonically with applied voltage. The final reward is based on the fraction of passing points across both files; full reward requires that all comparisons pass and the monotonic trends hold. Simply reporting known numbers is insufficient—your implementation must genuinely compute the displacements.
