# Crumpling Transition Transfer-Matrix Analysis

## Problem background
The polymerized membrane undergoes a crumpling transition as the bending rigidity changes. A discretized version of this system — a triangular lattice embedded in a face-centered-cubic space — can be mapped to an Ising-spin model on a hexagonal lattice. However, the original folding rule that enforces valid fold angles is incompatible with periodic-boundary conditions, which limits finite-size scaling analyses. A modified folding rule, where a single defect (a release of the folding constraint) is distributed uniformly along the transfer-matrix strip, restores translational invariance without altering bulk thermodynamics. The defect parameters are set to \(p=0.7\) and \(K'=1.5K\). With this modification, the transfer matrix for a periodic strip of width \(L\) can be diagonalized in the \(k=0\), parity-even subspace. The objective is to determine the thermodynamic crumpling transition points \(K_c\) and the associated latent heats \(Q\) for the three distinct transitions that appear as the bending rigidity \(K\) varies. This is done by analyzing the free-energy gap between the two leading eigenvalues and applying finite-size scaling extrapolations.

## Approach
Implement the transfer-matrix formalism for the modified folding rule on a hexagonal strip. For each strip width \(L = 4, 5, 6, 7\), the transfer matrix \(T(K)\) is constructed on a dense grid of the bending rigidity \(K\) covering the regions where crumpling transitions occur. Diagonalization in the \(k=0\), parity-even subspace yields the two leading eigenvalues \(\Lambda_1, \Lambda_2\) and their corresponding eigenvectors. From these, compute the free-energy gap \(\Delta f(K,L) = (-\ln\Lambda_2 + \ln\Lambda_1)/(2L)\). The finite-size transition point \(K_c(L)\) is located by the extremum condition \(\partial_K \Delta f = 0\) (e.g., by scanning \(K\) and using numerical root-finding). At each \(K_c(L)\), the latent heat per unit cell is computed via the Hamer two-level perturbation scheme: the matrix elements \(V_{ij} = \langle i | \partial_K T | j \rangle\) are evaluated with the eigenvectors normalized such that \(\langle i | T | i \rangle = 1\), and \(Q(L) = |K_c(L)| \sqrt{(V_{11}-V_{22})^2 + 4 V_{12}V_{21}} / (2L)\). This yields finite-size estimates for the three transitions. Thermodynamic-limit values are obtained by linear least-squares extrapolation of \(K_c(L)\) and \(Q(L)\) versus \(1/L^2\). The uncertainties are estimated by combining fitting errors and the spread from fits using different subsets of \(L\) (e.g., \(4 \le L \le 7\) and \(5 \le L \le 7\)).

## Reproduction target
Produce two artifacts that capture the finite-size data and the extrapolated thermodynamic limits:

1. **`finite_size_data.csv`**: A CSV file with columns `transition` (integer 1, 2, or 3), `L` (integer), `K_c(L)` (float), and `Q(L)` (float). It must contain exactly 12 rows — one for each of the three transitions at each of the four widths \(L=4,5,6,7\).
2. **`extrapolated_results.json`**: A JSON object containing the extrapolated thermodynamic values and their errors. It must include the keys `K_c_1`, `K_c_1_err`, `Q_1`, `Q_1_err`, `K_c_2`, `K_c_2_err`, `Q_2`, `Q_2_err`, `K_c_3`, `K_c_3_err`, `Q_3`, `Q_3_err`, each a float.

The extrapolation must be performed as described in the workflow steps: linear fits in \(1/L^2\) with error estimation from fit uncertainties and the spread between fits using different \(L\) subsets. The entire analysis pipeline, from transfer-matrix diagonalization to extrapolation, must be executed; simply writing pre‑known numbers is not sufficient.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Transfer-Matrix Diagonalization
- Role: process
- Action: Implement the transfer matrix for the modified folding rule (defect parameters p=0.7, K'=1.5K) on a hexagonal strip of width L=4,5,6,7. Construct the matrix for a dense grid of bending rigidity K covering the three transition regions, diagonalize in the k=0 parity-even subspace, and save the two leading eigenvalues and eigenvectors.
- Evidence: `/app/outputs/eigenvalue_data.npz`

### Step 2: Finite-size transition points and latent heats
- Role: scored (load-bearing)
- Action: From the eigenvalue curves, compute the free-energy gap Δf(K,L). Locate Kc(L) via extremum condition ∂KΔf=0. Compute latent heat Q(L) via the Hamer perturbation formula at each Kc(L). Output a CSV with columns: transition (int, 1/2/3), L (int, 4/5/6/7), K_c(L) (float), Q(L) (float). The file must contain exactly 12 rows (3 transitions × 4 L values).
- Output file: `/app/outputs/finite_size_data.csv`
- Format: csv
- Contract: CSV with columns: transition (int), L (int), K_c(L) (float), Q(L) (float)
- Scoring: scored by hidden verifier

### Step 3: Thermodynamic extrapolation
- Role: scored
- Action: For each transition, perform linear least-squares extrapolation of Kc(L) vs 1/L² and Q(L) vs 1/L² to obtain thermodynamic-limit estimates and their errors. Write a JSON object with keys K_c_1, K_c_1_err, Q_1, Q_1_err, K_c_2, K_c_2_err, Q_2, Q_2_err, K_c_3, K_c_3_err, Q_3, Q_3_err (all floats).
- Output file: `/app/outputs/extrapolated_results.json`
- Format: json
- Contract: JSON object with required float keys: K_c_1, K_c_1_err, Q_1, Q_1_err, K_c_2, K_c_2_err, Q_2, Q_2_err, K_c_3, K_c_3_err, Q_3, Q_3_err
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/finite_size_data.csv`
- `/app/outputs/extrapolated_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### finite_size_data.csv
- path: `/app/outputs/finite_size_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Finite-size data for verification of the transfer-matrix pipeline and self-consistency check.
- schema:
  - `type`: table
  - `required_columns`: `transition`, `L`, `K_c(L)`, `Q(L)`

### extrapolated_results.json
- path: `/app/outputs/extrapolated_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Extrapolated transition points and latent heats to be compared with hidden reference values from the paper.
- schema:
  - `type`: object
  - `required`: `K_c_1`, `K_c_1_err`, `Q_1`, `Q_1_err`, `K_c_2`, `K_c_2_err`, `Q_2`, `Q_2_err`, `K_c_3`, `K_c_3_err`, `Q_3`, `Q_3_err`

Notes: Scoring checks self-consistency between the finite-size data and extrapolated results, then compares the extrapolated Kc and Q to the paper's reported numbers within tolerances. The finite-size CSV must have exactly 12 rows.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "finite_size_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "transition",
          "L",
          "K_c(L)",
          "Q(L)"
        ]
      },
      "description": "Finite-size data for verification of the transfer-matrix pipeline and self-consistency check."
    },
    {
      "file": "extrapolated_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "K_c_1",
          "K_c_1_err",
          "Q_1",
          "Q_1_err",
          "K_c_2",
          "K_c_2_err",
          "Q_2",
          "Q_2_err",
          "K_c_3",
          "K_c_3_err",
          "Q_3",
          "Q_3_err"
        ]
      },
      "description": "Extrapolated transition points and latent heats to be compared with hidden reference values from the paper."
    }
  ],
  "notes": "Scoring checks self-consistency between the finite-size data and extrapolated results, then compares the extrapolated Kc and Q to the paper's reported numbers within tolerances. The finite-size CSV must have exactly 12 rows."
}
```

## How you are scored
A hidden verifier checks your output artifacts. It first validates the structure and content of `finite_size_data.csv`: it must have exactly 12 rows and the required columns. The verifier then independently performs the linear least‑squares extrapolation of \(K_c\) and \(Q\) versus \(1/L^2\) using your finite-size data, and compares the resulting thermodynamic estimates to the values you reported in `extrapolated_results.json`. A large discrepancy between the verifier’s recomputed extrapolation and your JSON entries indicates an inconsistency that reduces the score.

After this internal‑consistency check, the verifier compares your extrapolated \(K_c\) and \(Q\) values (for all three transitions) to hidden reference numbers using tolerances that account for legitimate variations due to implementation details. The reward is weighted equally across the three transitions, with the transition point and latent heat each contributing half of a transition’s weight. Reporting numbers alone without executing the transfer‑matrix pipeline will yield a zero or very low score, because the verifier also expects the finite-size data to be consistent with a genuine computation.
