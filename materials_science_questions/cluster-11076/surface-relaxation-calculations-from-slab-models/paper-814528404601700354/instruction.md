# Determine critical cluster sizes for structural transition in bcc metals using a coordination-based model

## Problem background
Small metal clusters can adopt atomic structures that differ from their bulk crystalline forms because a large fraction of their atoms reside at the surface. For elements that crystallize in a body-centered cubic (bcc) structure in the bulk, very small clusters often favor close-packed (fcc-like) arrangements that minimize surface energy. As the cluster grows, the bulk energy contribution eventually dominates, driving a transition to the bcc structure above a certain critical size. Predicting that critical size is important for understanding cluster morphology in catalysis, nucleation, and nanomaterials. A simple model based on the coordination environment of each atom and the bulk cohesive energies of the two competing structures can predict this transition. This task asks you to compute the critical cluster sizes for six bcc metals using such a model.

## Approach
The central idea is a local binding energy that scales with the square root of the effective atomic coordination number Z_i relative to a bulk reference Z_b. For each atom in a cluster we count its nearest neighbors Z_i^1 and next‑nearest neighbors Z_i^2 and form an effective coordination Z_i = Z_i^1 + a Z_i^2, where the mixing parameter a differs for fcc and bcc lattices. Atoms with Z_i < 10 are defined as surface atoms. The model gives a structural‑stability condition: the difference between the bulk cohesive energies of the two structures (normalized by the bulk cohesive energy) must equal a purely geometric function that depends only on the cluster's surface atoms. The bulk energy difference is a constant C for a given metal, obtainable from published tables. By constructing fcc and bcc clusters shell‑by‑shell over a wide range of sizes N, you can compute the geometric function S(N) — a sum over surface atoms of (Z_i/Z_b)^(1/2) − 1, normalized by N. The structural transition occurs at the size where S(N) crosses C. This task implements that workflow: build clusters, compute S(N), obtain the material constants C for V, Cr, Nb, Mo, Ta, and W from the provided references, and determine the intersection N_crit for each metal.

## Reproduction target
1. Construct fcc and bcc clusters for sizes from 10 to 20 000 atoms, determine surface atoms and effective coordination numbers, and compute the right‑hand side function  
   S(N) = (1/N) [ Σ_{fcc surface} ((Z_i/Z_b)^(1/2)−1) − Σ_{bcc surface} ((Z_i/Z_b)^(1/2)−1) ]  
   where Z_b=12 for fcc and Z_b=8 for bcc. Output this curve as `step_01_rhs_curve.csv`.

2. Using the material constants C for V, Cr, Nb, Mo, Ta, and W derived from the bulk energy data in Pettifor (1970) and Hultgren et al. (1973), find the size N at which your S(N) curve intersects C. Output the resulting critical sizes as `step_02_critical_sizes.json`.

## Assets

- Pettifor, D.G., 'A study of the transition metals', J. Phys. C 3, 367 (1970) — structure energy differences ΔE_bs: 10.1088/0022-3719/3/2/014
- Hultgren, R. et al., 'Selected Values of the Thermodynamic Properties of the Elements', American Society of Metals, Cleveland (1973) — bulk cohesive energies E_coh,b
- Python 3: python3
- NumPy: numpy

## Workflow steps

### Step 1: Construct fcc and bcc cluster geometries and compute surface quantities
- Role: process
- Action: Build fcc and bcc clusters using a shell-by-shell addition method up to at least N=20000 atoms. For each cluster size, compute per-atom effective coordination numbers Z_i = Z_i^1 + a * Z_i^2 (where Z_i^1, Z_i^2 are nearest- and next-nearest neighbor counts, a_fcc=0.08, a_bcc=0.4). Identify surface atoms as those with Z_i < 10. Record the total atom count N, the number of surface atoms N_s, and the sum over surface atoms of ((Z_i/Z_b)^0.5 - 1) with Z_b=12 for fcc and Z_b=8 for bcc. This produces the geometry data needed for the RHS curve.
- Evidence: `/app/outputs/geometry_summary.json`

### Step 2: Compute the universal RHS curve of structural stability
- Role: scored (load-bearing)
- Action: For each cluster size N (from 10 to 20000, fine grid), compute the right-hand side of Eq. (2.7): S(N) = (1/N) * [ Σ_{fcc surface} ((Z_i/Z_b)^0.5 - 1) - Σ_{bcc surface} ((Z_i/Z_b)^0.5 - 1) ]. Use the geometry data from step_geometry. Output a CSV file with columns N and S.
- Output file: `/app/outputs/step_01_rhs_curve.csv`
- Format: csv
- Contract: CSV with header: N (integer cluster size), S (float, the computed RHS value). One row per cluster size.
- Scoring: scored by hidden verifier

### Step 3: Determine critical cluster sizes for bcc metals
- Role: scored
- Action: Using the RHS curve from step_rhs_curve and the material constants C = (E_coh,b(bcc) - E_coh,b(fcc))/E_coh,b obtained from the cited references (Pettifor 1970 and Hultgren 1973), find the intersection where S(N) crosses C for each metal (V, Cr, Nb, Mo, Ta, W). Output a JSON object mapping each metal symbol to the determined integer N_crit.
- Output file: `/app/outputs/step_02_critical_sizes.json`
- Format: json
- Contract: JSON object with keys "V", "Cr", "Nb", "Mo", "Ta", "W" and integer values for N_crit.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_rhs_curve.csv`
- `/app/outputs/step_02_critical_sizes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_rhs_curve.csv
- path: `/app/outputs/step_01_rhs_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The universal geometry-dependent curve S(N) from Eq. 2.7; the checker recomputes this curve independently and compares the S values with a relative tolerance of 1e-3.
- schema:
  - `type`: table
  - `required_columns`: `N`, `S`
  - `columns`:
    - `N`: integer cluster size
    - `S`: float, the computed right-hand side of Eq. 2.7
  - `units`:
    - `N`: atoms
    - `S`: dimensionless

### step_02_critical_sizes.json
- path: `/app/outputs/step_02_critical_sizes.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The critical cluster sizes N_crit for each of the six bcc metals; compared to the paper's reported values with a tolerance of 5% or absolute 50 atoms, whichever is larger, and internally cross-checked against the submitted RHS curve.
- schema:
  - `type`: object
  - `required`: `V`, `Cr`, `Nb`, `Mo`, `Ta`, `W`
  - `items`:
    - `type`: integer
  - `units`:
    - `value`: atoms

Notes: The task is scoped to the structural stability (Eq. 2.7) and critical size calculation only. All required material parameters are public and retrievable from the cited references. The cluster construction uses simple lattice geometries; no large external datasets are needed. The load-bearing step on the RHS curve forces the agent to actually perform the cluster construction rather than guessing the final N_crit numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_rhs_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "S"
        ],
        "columns": {
          "N": "integer cluster size",
          "S": "float, the computed right-hand side of Eq. 2.7"
        },
        "units": {
          "N": "atoms",
          "S": "dimensionless"
        }
      },
      "description": "The universal geometry-dependent curve S(N) from Eq. 2.7; the checker recomputes this curve independently and compares the S values with a relative tolerance of 1e-3."
    },
    {
      "file": "step_02_critical_sizes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "V",
          "Cr",
          "Nb",
          "Mo",
          "Ta",
          "W"
        ],
        "items": {
          "type": "integer"
        },
        "units": {
          "value": "atoms"
        }
      },
      "description": "The critical cluster sizes N_crit for each of the six bcc metals; compared to the paper's reported values with a tolerance of 5% or absolute 50 atoms, whichever is larger, and internally cross-checked against the submitted RHS curve."
    }
  ],
  "notes": "The task is scoped to the structural stability (Eq. 2.7) and critical size calculation only. All required material parameters are public and retrievable from the cited references. The cluster construction uses simple lattice geometries; no large external datasets are needed. The load-bearing step on the RHS curve forces the agent to actually perform the cluster construction rather than guessing the final N_crit numbers."
}
```

## How you are scored
A hidden verifier scores the two artifacts independently and combines the scores by weight.

**step_01_rhs_curve.csv** – The verifier recomputes the S(N) curve using the same construction rules (coordination‑counting, surface definition, a_fcc and a_bcc). It compares your submitted curve pointwise against its own reference curve with a required tolerance. The closer your curve, the higher the score.

**step_02_critical_sizes.json** – For each metal, the verifier intersects YOUR submitted curve with the correct material constant C and compares the resulting N_crit to a hidden reference value (the correct critical size). It also checks that your reported N_crit is internally consistent with your own curve. Accuracy is judged by how well your N_crit match the hidden reference.

The final reward is a weighted average of the curve similarity and the critical‑size accuracy across the six metals.
