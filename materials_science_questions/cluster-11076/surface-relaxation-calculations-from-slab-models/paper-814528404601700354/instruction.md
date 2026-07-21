# Determine critical cluster sizes for structural transition in bcc metals using a coordination-based model

## Problem background
Small metal clusters can adopt atomic structures that differ from their bulk crystalline forms because a large fraction of their atoms reside at the surface. For elements that crystallize in a body-centered cubic (bcc) structure in the bulk, very small clusters often favor close-packed (fcc-like) arrangements that minimize surface energy. As the cluster grows, the bulk energy contribution eventually dominates, driving a transition to the bcc structure above a certain critical size. Predicting that critical size is important for understanding cluster morphology in catalysis, nucleation, and nanomaterials. A simple model based on the coordination environment of each atom and the bulk cohesive energies of the two competing structures can predict this transition. This task asks you to compute the critical cluster sizes for six bcc metals using such a model.

## Approach
The central idea is a local binding energy that scales with the square root of the effective atomic coordination number Z_i relative to a bulk reference Z_b. For each atom in a cluster we count its nearest neighbors Z_i^1 and next‑nearest neighbors Z_i^2 and form an effective coordination Z_i = Z_i^1 + a Z_i^2, where the mixing parameter a differs for fcc and bcc lattices (a_fcc = 0.08, a_bcc = 0.4). Atoms with Z_i < 10 are defined as surface atoms. The model gives a structural‑stability condition: the difference between the bulk cohesive energies of the two structures (normalized by the bulk cohesive energy) must equal a purely geometric function S(N) that depends only on the cluster's surface atoms. This function is defined as

S(N) = (1/N) [ Σ_{fcc surface} ((Z_i/Z_b)^(1/2) − 1) − Σ_{bcc surface} ((Z_i/Z_b)^(1/2) − 1) ],

where Z_b = 12 for fcc and Z_b = 8 for bcc. The structural transition occurs at the size N where S(N) crosses the material constant

C = [E_coh,b(bcc) − E_coh,b(fcc)] / E_coh,b(bcc).

The values of C for six bcc metals are taken from the paper's Table I and are explicitly listed below.

## Cluster construction method (must match the hidden checker exactly)
To obtain S(N) you must construct clusters for fcc and bcc according to the following rules:

1. **Supercell generation**  
   - fcc: Start from a simple cubic grid of unit cells, each containing four atoms at fractional coordinates (0,0,0), (0.5,0.5,0), (0.5,0,0.5), (0,0.5,0.5). Use at least 25³ unit cells (approx. 62 500 atoms) to have enough atoms for N up to 20 000.  
   - bcc: Start from a similar grid, each unit cell containing two atoms at (0,0,0) and (0.5,0.5,0.5). Use at least 30³ unit cells (approx. 54 000 atoms).

2. **Cluster selection by distance from origin**  
   - Compute the Euclidean distance of each atom from the origin (0,0,0).  
   - Sort atoms by this distance in ascending order.  
   - For a given cluster size N, take the first N atoms from this sorted list. This yields a compact, roughly spherical cluster.

3. **Coordination counting**  
   - Use the following nearest-neighbor and next-nearest-neighbor distances (all in units of the cube edge length of the simple cubic grid, which is set to 1):  
     - fcc NN distance: √0.5 ≈ 0.7071; NNN distance: 1.0  
     - bcc NN distance: √3/2 ≈ 0.8660; NNN distance: 1.0  
   - Two atoms are considered neighbors if their distance falls within the range [d × (1 − tol), d × (1 + tol)] with tol = 1e−4.  
   - For every atom, count Z_i^1 (NN) and Z_i^2 (NNN).  
   - Compute effective coordination Z_i = Z_i^1 + a * Z_i^2, with a_fcc = 0.08, a_bcc = 0.4.  
   - An atom is a surface atom if Z_i < 10.

4. **Cumulative sum computation**  
   - Once the entire supercell has been analysed, take the ordered sequence of atoms (by distance from origin) and compute, for each N from 1 to the maximum cluster size (at least 20 000), the sum over surface atoms of (Z_i / Z_b)^(1/2) − 1.  
   - Store these cumulative sums separately for fcc and bcc.

5. **S(N) curve**  
   - For each N, S(N) = (cumulative_sum_fcc[N] − cumulative_sum_bcc[N]) / N.  
   - Output S(N) as described below.

The above construction matches the one used by the hidden verifier. Using any other method (e.g. shell-by-shell addition based on hops) will result in a different S(N) curve and a low score.

## Material constants C
The following values (derived from the paper's Table I) are the ratio of the bulk structural energy difference to the bulk cohesive energy:

| Metal | C        |
|-------|----------|
| V     | 0.0537   |
| Cr    | 0.0925   |
| Nb    | 0.0382   |
| Mo    | 0.0558   |
| Ta    | 0.0353   |
| W     | 0.0432   |

You must use these exact numbers when determining the critical sizes.

## Reproduction target
1. Construct fcc and bcc clusters for sizes from 1 to 20 000 atoms following the distance‑based selection method, compute the required cumulative sums, and output the S(N) curve as `step_01_rhs_curve.csv`.
2. For each metal, find the size N where your S(N) curve crosses the corresponding C. Output the critical sizes as `step_02_critical_sizes.json`.

## Assets

- Python 3: python3
- NumPy: numpy

All the necessary numeric parameters are given in this instruction. No external literature or databases are needed.

## Workflow steps

### Step 1: Compute the universal RHS curve S(N)
- Role: scored (load‑bearing)
- Action: Implement the cluster construction and coordination counting exactly as described in "Cluster construction method". Compute S(N) for N = 1, 2, …, 20000 (at least). Output a CSV file with columns N and S.
- Output file: `/app/outputs/step_01_rhs_curve.csv`
- Format: csv
- Contract: CSV with header: N (integer cluster size), S (float). One row per cluster size.
- Scoring: scored by hidden verifier

### Step 2: Determine critical cluster sizes for bcc metals
- Role: scored
- Action: Using the S(N) curve from Step 1 and the material constants C given above, find the integer N at which S(N) first becomes ≤ C. Output a JSON object mapping each metal symbol to that N.
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
    - `S`: float, the computed right‑hand side of Eq. 2.7
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
  "notes": "Accurate reproduction of the distance-based cluster construction is essential."
}
```