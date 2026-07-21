# Ferroelectric soft-mode domain-wall vibrations: restoring-force constants and dielectric response

## Problem background
Epitaxial ferroelectric thin films often contain periodic laminar c/a/c/a domain structures, where regions with different orientations of the spontaneous polarization alternate. Translational vibrations of the 90° domain walls separating these regions can couple to applied electric fields and are believed to contribute significantly to the dielectric and piezoelectric responses of the film. This task investigates the mechanical restoring forces that act on these domain walls when they are displaced collectively in characteristic vibration modes, and computes the resulting contribution to the film's permittivity. In particular, it aims to determine which collective modes exhibit the lowest restoring force (i.e., are "soft") and to quantify the associated dielectric enhancement.

## Approach
The restoring forces are derived within a linear elastic framework using a dislocation-disclination model of the internal stress sources at the domain-wall junctions. The elastic interaction energy between displaced walls is expressed in terms of an auxiliary function R(x,y) that depends on the domain period D, the c-domain width d, and the film thickness H. The resulting force constants for three important collective modes – the antiparallel motion of all c/a and a/c walls (h mode), and the two extreme modes at the Brillouin zone boundary corresponding to either the c domains (c mode) or the a domains (a mode) oscillating – are given by simple combinations of R. These force constants are then normalized by a factor involving the shear modulus G, Poisson's ratio ν, the misfit strains S_a and S_c, and the thickness H.

For the dielectric contribution, the equilibrium domain geometry (the c-domain fraction d/D and the normalized domain period D/H) is needed as a function of film thickness H and misfit strain S_r. This is obtained from the equilibrium domain-structure model of Pertsev and Zembilgotov (1995), which must be implemented by the agent using the publicly accessible paper. Once the geometry is known, the soft c-mode restoring force constant is evaluated and used to compute the dimensionless dielectric contribution Δε33. The whole workflow is purely computational, involving only the evaluation of closed-form formulas and an equilibrium model.

## Reproduction target
Compute the normalized restoring-force constants for the h, c, and a collective wall-vibration modes over a set of domain geometry parameters (c-domain fraction d/D and normalized domain period D/H). From these results, determine how the ordering of the force constants (which mode is softest) depends on the volume fraction of c domains. Also, compute the soft c-mode contribution to the dielectric permittivity as a function of the normalized film thickness for a fixed misfit strain, using the equilibrium domain geometry obtained from the Pertsev and Zembilgotov model.

## Assets

- Python 3 scientific stack: numpy, scipy (optional)
- Pertsev & Zembilgotov (1995) equilibrium domain-structure model: https://doi.org/10.1063/1.360484

## Workflow steps

### Step 1: Equilibrium domain geometry
- Role: process
- Action: Implement the equilibrium domain-structure model from Pertsev and Zembilgotov (1995). For the relative coherency strain S_r/S_r^0 = 0.5 used in this workflow, the model gives the c-domain fraction d/D = 0.7 (constant) and the normalized domain period D/H that depends on H/H0. The following approximate values can be used (intermediate values may be obtained by interpolation):
    | H/H0 | D/H  |
    |------|------|
    | 0.1  | 1.2  |
    | 1    | 2.0  |
    | 10   | 3.8  |
    | 100  | 6.5  |
    The agent may implement a general function for any S_r/S_r^0, but for the present task these specific geometry parameters suffice. Provide these values to step2.
- Evidence: none

### Step 2: Restoring-force constants
- Role: scored (load-bearing)
- Action: Implement the auxiliary function R(x,y) defined by Eq. (12):
  R(x,y) = ln( (cosh(4πy) - cos(2πx)) / (1 - cos(2πx)) ) - 8π^2 y^2 (cosh(4πy) cos(2πx) - 1) / (cosh(4πy) - cos(2πx))^2.
  Then compute the normalized force constants (already made dimensionless by the factor (1-ν)H/(G (S_c - S_a)^2)):
  k_h_norm = (√2/π) [ R(d/(2D), H/(2D)) + R(d/(2D)+0.5, H/(2D)) ],
  k_sc_norm = (√2/π) [ R(d/(2D), H/(2D)) - R(0.5, H/(2D)) ],
  k_sa_norm = (√2/π) [ R(d/(2D)+0.5, H/(2D)) - R(0.5, H/(2D)) ].
  Evaluate these for d/D ∈ {0.3, 0.5, 0.7} and D/H ∈ {0.1, 0.5, 1, 2, 5, 10}. Write the results to force_constants.csv.
- Output file: `/app/outputs/force_constants.csv`
- Format: csv
- Contract: Columns: mode (string, one of h, sc, sa), d_over_D (float), D_over_H (float), k_norm (float). The file must contain rows for all combinations of d_over_D and D_over_H listed above.
- Scoring: scored by hidden verifier

### Step 3: Dielectric contribution from soft c-mode
- Role: scored (load-bearing)
- Action: Using the equilibrium geometry model from step0 for S_r/S_r^0 = 0.5, obtain the c-domain fraction d/D (which equals 0.7) and the normalized domain period D/H at each normalized film thickness H/H0 = 0.1, 1, 10, 100. For each pair (d/D, D/H) compute the normalized c-mode restoring force constant k_sc_norm (using the formula from step1 with d/D and D/H) and then the dimensionless dielectric contribution Δε33_norm = (2√2) / (k_sc_norm * D/H). Write the results to dielectric_contribution.csv.
- Output file: `/app/outputs/dielectric_contribution.csv`
- Format: csv
- Contract: Columns: H_norm (float, H/H0), delta_epsilon_norm (float). The file must contain one row for each H_norm value in {0.1, 1, 10, 100}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/force_constants.csv`
- `/app/outputs/dielectric_contribution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### force_constants.csv
- path: `/app/outputs/force_constants.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Normalized restoring-force constants for the collective domain-wall vibration modes (h, c, a) as functions of c-domain fraction d/D and domain period D/H. The hidden verifier will check that the reported force constants satisfy the structural consistency implied by the model.
- schema:
  - `type`: table
  - `required_columns`: `mode`, `d_over_D`, `D_over_H`, `k_norm`
  - `units`:
    - `k_norm`: dimensionless

### dielectric_contribution.csv
- path: `/app/outputs/dielectric_contribution.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Soft c-mode contribution to the dielectric permittivity as a function of normalized film thickness for a fixed domain geometry (d/D = 0.7) and misfit strain (S_r/S_r^0 = 0.5).
- schema:
  - `type`: table
  - `required_columns`: `H_norm`, `delta_epsilon_norm`
  - `units`:
    - `delta_epsilon_norm`: dimensionless

Notes: The restoring-force constants k_norm are expected to be positive. The dielectric contribution should decrease with increasing film thickness and show the characteristic enhancement from the soft mode.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "force_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "d_over_D",
          "D_over_H",
          "k_norm"
        ],
        "units": {
          "k_norm": "dimensionless"
        }
      },
      "description": "Normalized restoring-force constants for the collective domain-wall vibration modes (h, c, a) as functions of c-domain fraction d/D and domain period D/H. The hidden verifier will check that the reported force constants satisfy the structural consistency implied by the model."
    },
    {
      "file": "dielectric_contribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "H_norm",
          "delta_epsilon_norm"
        ],
        "units": {
          "delta_epsilon_norm": "dimensionless"
        }
      },
      "description": "Soft c-mode contribution to the dielectric permittivity as a function of normalized film thickness for a fixed domain geometry (d/D = 0.7) and misfit strain (S_r/S_r^0 = 0.5)."
    }
  ],
  "notes": "The restoring-force constants k_norm are expected to be positive. The dielectric contribution should decrease with increasing film thickness and show the characteristic enhancement from the soft mode."
}
```

## How you are scored
A hidden verifier independently checks the two output CSV files you submit. For the force constants, it compares your reported normalized values to reference results and verifies that they satisfy the expected structural relationships predicted by the physical model. For the dielectric contribution, it compares your reported dimensionless permittivity values to reference curves. Each artifact contributes a weighted portion to the total score, which is reported as a single number between 0 and 1. You must produce the exact required columns and rows as specified in the output contract; missing or extra entries will reduce your score.
