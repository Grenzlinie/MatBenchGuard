# One‑parameter dissociated Frank dislocation loop energy and critical stacking‑fault energy calculation

## Problem background
In face‑centered cubic metals, triangular Frank dislocation loops can dissociate to form stacking‑fault tetrahedra. The equilibrium size at which the transformation occurs depends on the stacking‑fault energy γ. This work computes the energy of a dissociated Frank loop using a truncated‑tetrahedron geometry (one‑parameter model) and derives the relationship between defect edge‑length l and γ by requiring the minimum loop energy to equal the energy of a complete stacking‑fault tetrahedron. Computing the l–γ relation allows estimation of stacking‑fault energies of f.c.c. metals.

## Approach
Use explicit closed‑form formulas for the mutual elastic interaction energy between straight dislocation segments (five geometrical cases plus self‑energy). Assemble the total energy of the dissociated Frank loop as a sum of self‑energies, pairwise interaction energies, and stacking‑fault energy γ times the fault area. The loop geometry is a truncated tetrahedron with separation h between Shockley and stair‑rod dislocations. For each l and γ, find the energy minimum by scanning h in steps of (√3 l/2)/20. Then search for the γ that makes the minimum total energy equal to the energy of a complete stacking‑fault tetrahedron given by the Yoffe expression: E_tet = (G b^2 / (1-ν)) * [ (√3 / 2) l * (ln(l/ϵ) - 2.5 + ν/2) ] + γ * (√3 l^2 / 2), with inner cut‑off ϵ = n·b. Compute for l/b = 40, 260, 1000 using ν=0.4, n=1.

## Reproduction target
For the one‑parameter model with ν=0.4 and inner‑cut‑off factor n=1, compute the critical stacking‑fault energy γ (in units Gb) for edge‑lengths l/b = 40, 260, and 1000. The critical condition is that the minimum of the total dissociated‑Frank‑loop energy (with respect to h, scanned in steps of (√3 l/2)/20) equals the energy of a complete stacking‑fault tetrahedron. Output the resulting critical γ/Gb (in units 1e‑3), the corresponding minimum energy E_min/Gb³, and the optimal separation h/b in the file one_parameter_results.csv.

## Assets
No external data files, models, or pre‑trained weights are required. The dislocation segment interaction energy formulas (five geometrical cases plus self‑energy) are described in the Approach and must be implemented directly. The Yoffe tetrahedron energy expression is given above. Standard numerical Python packages (NumPy, SciPy) are recommended for the optimization and scanning.

## Workflow steps

### Step 1: Implement dislocation segment interaction formulas
- Role: process
- Action: Implement the closed‑form expressions for the mutual elastic interaction energy between two straight dislocation segments for all five geometrical cases (skew, non‑parallel coplanar, coplanar starting at common point, parallel, collinear non‑overlapping) and the self‑energy as given in the paper’s Appendix. Using these functions, construct a function that evaluates the total energy of the one‑parameter dissociated Frank loop (truncated tetrahedron) as a function of the Shockley‑stair‑rod separation h, for given edge‑length l, stacking‑fault energy γ, shear modulus G, Poisson’s ratio ν, Burgers vector magnitude b, and core‑radius factor n.
- Evidence: none

### Step 2: Determine critical stacking‑fault energy for l/b = 40, 260, 1000
- Role: scored (load-bearing)
- Action: For each edge‑length l/b in {40, 260, 1000}, with ν=0.4, n=1, and using the Yoffe expression for the energy of a complete stacking‑fault tetrahedron, search for the stacking‑fault energy γ such that the minimum of the total one‑parameter Frank loop energy (with respect to h, scanned in steps of (√3 l/2)/20) equals the tetrahedron energy. Record the critical γ/Gb (in units 1e‑3), the minimum energy E_min/Gb³, and the optimal h/b.
- Output file: `/app/outputs/one_parameter_results.csv`
- Format: csv
- Contract: Columns: l_over_b, gamma_over_Gb, E_min_over_Gb3, h_over_b. All numeric; gamma_over_Gb is in units of 1e‑3 Gb, energies in Gb³, lengths in b.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/one_parameter_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### one_parameter_results.csv
- path: `/app/outputs/one_parameter_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Critical stacking‑fault energy and optimized configuration parameters for the one‑parameter dissociated Frank loop model at three edge‑lengths (l/b = 40, 260, 1000).
- schema:
  - `type`: table
  - `required_columns`: `l_over_b`, `gamma_over_Gb`, `E_min_over_Gb3`, `h_over_b`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "one_parameter_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "l_over_b",
          "gamma_over_Gb",
          "E_min_over_Gb3",
          "h_over_b"
        ]
      },
      "description": "Critical stacking‑fault energy and optimized configuration parameters for the one‑parameter dissociated Frank loop model at three edge‑lengths (l/b = 40, 260, 1000)."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden verifier against independent reference values. The verifier checks the one_parameter_results.csv file for correctness of the three γ/Gb, E_min, and h values. It compares each result to the expected value derived from the paper’s own computation with appropriate tolerances. The final reward is a weighted sum of the scores from the scored step (Step 2). To earn full marks, your computed γ, E_min, and h must match the reference within tolerance; simply copying numbers from the paper is not sufficient—the verifier checks that the values arise from a correct minimization procedure and consistent energy model.
