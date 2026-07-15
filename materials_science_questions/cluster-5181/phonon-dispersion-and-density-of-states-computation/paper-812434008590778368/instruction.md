# Compute phonon dispersion for BCC lattice using Cardan's cubic solution

## Problem background
Phonon dispersion relations in crystalline solids are obtained by solving a cubic secular equation derived from a 3×3 dynamical matrix.  For arbitrary wave‑vector directions the secular determinant does not factorise easily, and numerical diagonalisation is the usual tool.  Cardan’s algebraic solution for cubic equations offers a non‑iterative, closed‑form route that yields the three squared frequencies ω² and a degeneracy parameter T.  With this method, the nature of the transverse branches (degenerate or distinct) can be read directly from T without inspecting the eigenvector composition.  The approach is demonstrated here for a monatomic body‑centred cubic lattice with first‑ and second‑neighbor harmonic interactions (force‑constant ratio 0.8).

## Approach
The dynamical matrix D(k) for a BCC lattice is first constructed from the wave‑vector components kx, ky, kz using the explicit sin/cos expressions for the matrix elements A…G (all expressed in convenient dimensionless units, lattice constant taken as a=1).  The cubic secular equation det(D − ω²I)=0 then yields the coefficients P, Q, R.  Shifting the variable eliminates the quadratic term, giving a depressed cubic whose discriminant is the degeneracy parameter T = q²/4 + p³/27.  For T ≤ 0 all three roots are real; the case T>0 corresponds to unphysical complex frequencies and does not occur for physical crystals.  When T<0 the three real roots are obtained from a trigonometric form that directly yields the squared frequencies, with the largest root associated with the quasi‑longitudinal mode.  T=0, corresponding to degenerate transverse branches, occurs along high‑symmetry directions.  The agent will implement a solver that (a) builds D(k) for any given k, (b) computes the cubic coefficients and T, and (c) returns the three real ω² values sorted descending.  This solver is then used to generate dispersion data along two prescribed directions.

### Formulas for the BCC dynamical matrix and Cardan solver

**Dynamical matrix elements** (lattice constant a=1, second-neighbor force constant ratio R=0.8; all elements in units where the overall scale factor 8σ/(3m) is omitted – the absolute scale cancels when checking relative tolerances):

- Define: c_x = cos(kx), s_x = sin(kx), c_2x = cos(2·kx), and similarly for y and z.
- δ = 1 + 0.75·R − cos(kx)·cos(ky)·cos(kz)

  A = δ − 0.75·R·cos(2·kx)
  B = δ − 0.75·R·cos(2·ky)
  C = δ − 0.75·R·cos(2·kz)
  E = sin(kx)·sin(ky)·cos(kz)
  F = sin(kx)·cos(ky)·sin(kz)
  G = cos(kx)·sin(ky)·sin(kz)

**Cubic secular equation** det(D − ω² I) = 0 gives:
  x³ + P x² + Q x + R = 0,   where x = ω².
  P = −(A + B + C)
  Q = A·B + B·C + C·A − E² − F² − G²
  R = −A·B·C − 2·E·F·G + A·G² + B·F² + C·E²

**Depressed cubic** (after the shift x' = x + P/3):
  (x')³ + p·x' + q = 0
  p = Q − P²/3
  q = 2·P³/27 − P·Q/3 + R

**Degeneracy parameter**
  T = q²/4 + p³/27

**Cardan root formulas for physical (T ≤ 0) cases**

  - If T = 0 (degenerate transverse branches, e.g. high‑symmetry direction):
      Let u = (−q/2)^{1/3}  (real cube root).
      The three x' roots: 2·u,  −u,  −u.
      Then ω² = x' − P/3.

  - If T < 0 (three distinct real roots, non‑symmetry direction):
      r = √(−p³/27)   (r > 0)
      θ = arccos( −q / (2·r) )   (θ ∈ [0, π])
      x'₁ = 2·r^{1/3}·cos(θ/3)
      x'₂ = 2·r^{1/3}·cos((θ + 2π)/3)
      x'₃ = 2·r^{1/3}·cos((θ + 4π)/3)
      ω²_i = x'_i − P/3.
      The root with the largest x' (x'₁, because cos(θ/3) > cos((θ+2π)/3) and cos((θ+4π)/3) for θ∈[0,π]) corresponds to the quasi‑longitudinal mode.

In all cases, sort the final ω² values in descending order before output.

## Reproduction target
Compute the squared phonon frequencies ω² and the degeneracy parameter T at a dense set of wave‑vectors along two directions: (1) the high‑symmetry [100] direction with k = (kx, 0, 0), kx ∈ [0, π] (at least 50 points); (2) a non‑symmetry direction [1, 0.1, 0.2] with k = t·(1, 0.1, 0.2), where t is chosen so that |k| reaches a zone‑boundary‑like limit (at least 50 points).  For each k, output the three real squared frequencies sorted descending (longitudinal branch first) together with T.  The results must be written to the CSV files /app/outputs/dispersion_100.csv and /app/outputs/dispersion_nonsym.csv, following the column schemas specified in the workflow steps.  The computed frequencies must be real and positive, the longitudinal mode must have the highest frequency, and the degeneracy parameter T must correctly indicate whether the two lower branches are degenerate or distinct for the respective direction.

## Assets

- Python scientific computing environment (numpy): numpy

## Workflow steps

### Step 1: Implement dynamical matrix and Cardan solver
- Role: process
- Action: Implement the dynamical matrix elements A, B, C, E, F, G for a BCC lattice with first- and second-neighbor interactions (force constant ratio R=0.8, lattice constant a=1), using the formulas from the paper. Implement the Cardan algebraic solver that computes the three real squared frequencies ω² and the degeneracy parameter T from the wavevector components kx, ky, kz. Validate the solver by checking that for k along [100] the analytical expectations (omega2_1 = A, omega2_2 = B = C) hold and T = 0.
- Evidence: `/app/outputs/solver_validation.txt`

### Step 2: Dispersion along [100] symmetry direction
- Role: scored (load-bearing)
- Action: Generate a set of wavevectors along the [100] direction: k = (k_x, 0, 0) with k_x uniformly sampled from 0 to π (units where a=1), using at least 50 points. For each k, compute the three squared frequencies ω² using the Cardan solver built in step 1, sort descending (longitudinal first), and compute the degeneracy parameter T. Write the results to /app/outputs/dispersion_100.csv.
- Output file: `/app/outputs/dispersion_100.csv`
- Format: csv
- Contract: kx (float), omega2_1 (float), omega2_2 (float), omega2_3 (float), T (float)
- Scoring: scored by hidden verifier

### Step 3: Dispersion along non-symmetry direction [1,0.1,0.2]
- Role: scored (load-bearing)
- Action: Generate a set of wavevectors along the direction d = (1, 0.1, 0.2): k = t * d with t uniformly sampled from 0 to a value that reaches a zone-boundary-like limit (e.g., until |k| ≈ π), using at least 50 points. For each k, compute the three squared frequencies ω² using the Cardan solver, sort descending (longitudinal first), and compute T. Write the results to /app/outputs/dispersion_nonsym.csv.
- Output file: `/app/outputs/dispersion_nonsym.csv`
- Format: csv
- Contract: kx (float), ky (float), kz (float), omega2_1 (float), omega2_2 (float), omega2_3 (float), T (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dispersion_100.csv`
- `/app/outputs/dispersion_nonsym.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dispersion_100.csv
- path: `/app/outputs/dispersion_100.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Squared phonon frequencies ω² and degeneracy parameter T along the [100] direction. The checker will recompute ω² and T from the provided kx values, verify that omega2_2 ≈ omega2_3 and T ≈ 0 (transverse branches degenerate), and compare all ω² values within a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `kx`, `omega2_1`, `omega2_2`, `omega2_3`, `T`
  - `column_types`:
    - `kx`: float
    - `omega2_1`: float
    - `omega2_2`: float
    - `omega2_3`: float
    - `T`: float

### dispersion_nonsym.csv
- path: `/app/outputs/dispersion_nonsym.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Squared phonon frequencies ω² and degeneracy parameter T along the non-symmetry direction [1,0.1,0.2]. The checker will recompute ω² and T from the provided (kx,ky,kz) values, verify that all ω² are positive, omega2_1 > omega2_2 > omega2_3, and T < 0, and compare all ω² values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `kx`, `ky`, `kz`, `omega2_1`, `omega2_2`, `omega2_3`, `T`
  - `column_types`:
    - `kx`: float
    - `ky`: float
    - `kz`: float
    - `omega2_1`: float
    - `omega2_2`: float
    - `omega2_3`: float
    - `T`: float

Notes: The checker independently implements the same BCC dynamical matrix (force constant ratio 0.8, lattice constant a=1) and Cardan's solution. It reads the agent's CSV, extracts the k-points, recomputes ω² and T, then checks agreement. No external data is required; the checker's hidden gold is its own recomputation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dispersion_100.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx",
          "omega2_1",
          "omega2_2",
          "omega2_3",
          "T"
        ],
        "column_types": {
          "kx": "float",
          "omega2_1": "float",
          "omega2_2": "float",
          "omega2_3": "float",
          "T": "float"
        }
      },
      "description": "Squared phonon frequencies ω² and degeneracy parameter T along the [100] direction. The checker will recompute ω² and T from the provided kx values, verify that omega2_2 ≈ omega2_3 and T ≈ 0 (transverse branches degenerate), and compare all ω² values within a relative tolerance."
    },
    {
      "file": "dispersion_nonsym.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx",
          "ky",
          "kz",
          "omega2_1",
          "omega2_2",
          "omega2_3",
          "T"
        ],
        "column_types": {
          "kx": "float",
          "ky": "float",
          "kz": "float",
          "omega2_1": "float",
          "omega2_2": "float",
          "omega2_3": "float",
          "T": "float"
        }
      },
      "description": "Squared phonon frequencies ω² and degeneracy parameter T along the non-symmetry direction [1,0.1,0.2]. The checker will recompute ω² and T from the provided (kx,ky,kz) values, verify that all ω² are positive, omega2_1 > omega2_2 > omega2_3, and T < 0, and compare all ω² values within tolerance."
    }
  ],
  "notes": "The checker independently implements the same BCC dynamical matrix (force constant ratio 0.8, lattice constant a=1) and Cardan's solution. It reads the agent's CSV, extracts the k-points, recomputes ω² and T, then checks agreement. No external data is required; the checker's hidden gold is its own recomputation."
}
```

## How you are scored
A hidden verifier independently reconstructs the same BCC dynamical matrix and Cardan solver used by your workflow.  For each CSV file, it reads the k‑point coordinates you submitted, recomputes the squared frequencies ω² and the degeneracy parameter T, and compares them with your values within a strict relative tolerance.  In addition, it verifies physical consistency: all ω² are positive, the longitudinal mode is the highest‑frequency branch, and the degeneracy parameter T is consistent with the observed branch structure.  The two scored steps (dispersion_100.csv and dispersion_nonsym.csv) each carry a substantial weight; the total reward is a weighted combination of the per‑step agreement.  Reporting values that deviate from the recomputed ones or failing the physical‑consistency checks reduces your score.
