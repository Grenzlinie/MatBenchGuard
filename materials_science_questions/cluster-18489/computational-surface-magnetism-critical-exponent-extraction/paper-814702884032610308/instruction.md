# Ising Model MFRG Critical Exponents Computation via Transfer Matrix

## Problem background
The molecular-field renormalization group (MFRG) is a technique that attempts to improve the classical critical exponents obtained in mean-field theory by applying finite-size scaling ideas to clusters of different sizes. For the square Ising model, one considers three square clusters of linear size \(L\), \(L' = L-1\), and \(L'' = L-2\). Each cluster has an effective symmetry-breaking field \(b\) acting on its edge spins. By imposing scaling relations between the magnetizations of the clusters and expanding to leading order in the effective field, one obtains a set of fixed-point equations that involve a two-point correlation function \(\Theta(K)\), computed in zero external field and zero effective field. Solving these equations yields a finite-size fixed-point coupling \(K^*\) and, from the linearized renormalization-group flow, associated critical exponents \(y_t\) (thermal), \(y_h\) (bulk magnetic), \(y_{hs}\) (surface magnetic) and the ratio \(y_h/y_t\). The main computational challenge is evaluating \(\Theta(K)\) for clusters up to \(L = 11\), because a direct enumeration of all \(2^{L \times L}\) spin configurations becomes intractable. A transfer-matrix approach that tracks the external field \(h\) and effective field \(b\) perturbatively up to second order makes the computation feasible. The purpose of this task is to numerically implement that transfer-matrix method, compute the finite-size critical quantities for \(L = 3\) to \(11\), and then perform an extrapolation to infinite system size to obtain the corresponding infinite-Ising-model estimates.

## Approach
The core idea is a perturbative transfer-matrix technique applied to a square lattice of \(L \times L\) Ising spins. The partition function \(Z_L\) is expressed as a product of transfer matrices that are built column by column. In the presence of a small external field \(h\) and a small effective field \(b\) on the edge spins, \(Z_L\) is expanded to second order in \(h\) and \(b\). The required correlation function \(\Theta(K)\) is then obtained as the ratio of the mixed second-order expansion coefficient to the zeroth-order coefficient. During the transfer-matrix multiplications, the algorithm keeps track of the powers of \(h\) and \(b\) up to the desired order, which avoids an exponential explosion of configurations. Once the function compute_theta(L, K) is implemented, the MFRG fixed-point equations for a triplet \((L, L-1, L-2)\) reduce to two coupled equations involving \(\Theta\) evaluated at the same coupling \(K\). Solving these numerically yields \(K^*\). From the scaling relations that define the two renormalization steps \((K,h,b) \to (K',h',b')\) and \((K',h',b') \to (K'',h'',b'')\) one then calculates the critical exponents \(y_t\), \(y_h\), \(y_{hs}\) and \(y_h/y_t\). This computation is repeated for all \(L\) from 3 to 11. Finally, an extrapolation technique such as the alternating \(\varepsilon\)-algorithm is applied to the finite-size sequences to obtain infinite-system-size estimates, and uncertainties on these estimates are derived from the convergence behaviour.

## Reproduction target
Produce a single Comma-Separated Values (CSV) file at `/app/outputs/table_results.csv` with the following structure:

- The file must have a header row with columns: `L`, `L_prime`, `L_doubleprime`, `K_star`, `y_t`, `y_h`, `y_h_over_y_t`, `y_hs`.
- The next nine rows correspond to the finite-size data for \(L = 3, 4, \dots, 11\). In each row, \(L\) is the integer cluster size, \(L' = L-1\), \(L'' = L-2\). The remaining five columns contain the computed fixed-point coupling \(K^*\) and the critical exponents as floating-point numbers written to at least six decimal places.
- The tenth and final row is the extrapolated \(L \to \infty\) row. In this row, the `L` column contains the string `∞` (Unicode U+221E), while the `L_prime` and `L_doubleprime` columns are left empty. Each of the `K_star`, `y_t`, `y_h`, `y_h_over_y_t`, `y_hs` columns contains a string of the form `"<central_value>(<uncertainty>)"`, where the uncertainty refers to the last quoted decimal place(s) (for example, `"0.4406(1)"`).

All floating-point numbers should be output with sufficient precision to capture the converged digits of the transfer-matrix computation. The file must be pure CSV with no extra commentary.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement transfer-matrix Θ(K) function
- Role: process
- Action: Implement a function compute_theta(L, K) that uses a transfer-matrix technique with perturbative tracking of external field h and effective field b up to second order to compute the correlation function Θ(K) for a square Ising cluster of linear size L at coupling K.
- Evidence: none

### Step 2: Solve MFRG fixed-point equations
- Role: process
- Action: For each triplet (L, L-1, L-2) with L=3..11, use compute_theta to numerically solve the MFRG fixed-point equations for the fixed-point coupling K*, then compute critical exponents y_t, y_h, y_hs and ratio y_h/y_t using the scaling relations from the two-step renormalization.
- Evidence: none

### Step 3: Generate final results table
- Role: scored (load-bearing)
- Action: Assemble the finite-size results for L=3..11, apply the alternating ε-algorithm to extrapolate K*, y_t, y_h, y_hs, y_h/y_t to infinite system size, and produce a CSV file table_results.csv with the required columns and rows.
- Output file: `/app/outputs/table_results.csv`
- Format: csv
- Contract: CSV with header: L, L_prime, L_doubleprime, K_star, y_t, y_h, y_h_over_y_t, y_hs. Data rows: 10 rows. Rows 1-9: L, L_prime, L_doubleprime are integers (L=3..11, L'=L-1, L''=L-2); K_star, y_t, y_h, y_h_over_y_t, y_hs are floating-point numbers to at least six decimal places. The 10th row: L='∞', L_prime and L_doubleprime empty; the value columns are strings with the extrapolated value and uncertainty in parentheses (e.g., '0.4406(1)').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_results.csv
- path: `/app/outputs/table_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reproduction of the paper's Table 1: finite-size critical couplings and exponents for L=3..11 and the extrapolated infinite-size values.
- schema:
  - `type`: table
  - `required_columns`: `L`, `L_prime`, `L_doubleprime`, `K_star`, `y_t`, `y_h`, `y_h_over_y_t`, `y_hs`
  - `columns`:
    - `L`:
      - `type`: union[int, string]
      - `description`: Cluster size (3..11) or '∞' for the extrapolated row
    - `L_prime`:
      - `type`: union[int, empty]
      - `description`: L-1; empty for extrapolated row
    - `L_doubleprime`:
      - `type`: union[int, empty]
      - `description`: L-2; empty for extrapolated row
    - `K_star`:
      - `type`: union[float, string]
      - `description`: Fixed-point coupling; for extrapolated row a string with error e.g. '0.4406(1)'
    - `y_t`:
      - `type`: union[float, string]
      - `description`: Thermal exponent; for extrapolated row a string with error
    - `y_h`:
      - `type`: union[float, string]
      - `description`: Bulk magnetic exponent; for extrapolated row a string with error
    - `y_h_over_y_t`:
      - `type`: union[float, string]
      - `description`: Ratio y_h/y_t; for extrapolated row a string with error
    - `y_hs`:
      - `type`: union[float, string]
      - `description`: Surface magnetic exponent; for extrapolated row a string with error

Notes: The finite-size values for L=3..11 should match the paper's Table 1 within relative tolerances (tighter for L≤5). The extrapolated row's central values must lie within a factor of the paper's quoted uncertainties.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "L_prime",
          "L_doubleprime",
          "K_star",
          "y_t",
          "y_h",
          "y_h_over_y_t",
          "y_hs"
        ],
        "columns": {
          "L": {
            "type": "union[int, string]",
            "description": "Cluster size (3..11) or '∞' for the extrapolated row"
          },
          "L_prime": {
            "type": "union[int, empty]",
            "description": "L-1; empty for extrapolated row"
          },
          "L_doubleprime": {
            "type": "union[int, empty]",
            "description": "L-2; empty for extrapolated row"
          },
          "K_star": {
            "type": "union[float, string]",
            "description": "Fixed-point coupling; for extrapolated row a string with error e.g. '0.4406(1)'"
          },
          "y_t": {
            "type": "union[float, string]",
            "description": "Thermal exponent; for extrapolated row a string with error"
          },
          "y_h": {
            "type": "union[float, string]",
            "description": "Bulk magnetic exponent; for extrapolated row a string with error"
          },
          "y_h_over_y_t": {
            "type": "union[float, string]",
            "description": "Ratio y_h/y_t; for extrapolated row a string with error"
          },
          "y_hs": {
            "type": "union[float, string]",
            "description": "Surface magnetic exponent; for extrapolated row a string with error"
          }
        }
      },
      "description": "Reproduction of the paper's Table 1: finite-size critical couplings and exponents for L=3..11 and the extrapolated infinite-size values."
    }
  ],
  "notes": "The finite-size values for L=3..11 should match the paper's Table 1 within relative tolerances (tighter for L≤5). The extrapolated row's central values must lie within a factor of the paper's quoted uncertainties."
}
```

## How you are scored
A hidden verifier will check your submitted `table_results.csv` against a reference derived from the published work (which you do not have access to). First, it verifies that the file exists, has the correct columns, and that the rows conform to the specification (types, emptiness of `L_prime`/`L_doubleprime` for the infinite row, etc.). Structural defects reduce the score. Then, for each of the nine finite-size rows, the verifier compares your numerical values for `K_star`, `y_t`, `y_h`, `y_h_over_y_t`, and `y_hs` to the hidden reference values. The comparison uses a relative tolerance that is tighter for smaller system sizes and slightly relaxed for larger sizes, reflecting the expected behaviour of numerical algorithms. For the extrapolated infinite-size row, the checker verifies that each central value lies within a multiple of the reference uncertainty from the reported paper value; a correct reproduction will fall well inside this window. Your final reward is the fraction of all numerical cells that pass these checks, so you must produce accurate numbers for every column. Simply returning the expected format is not enough; the numbers must be the result of a faithful implementation of the MFRG transfer-matrix method.
