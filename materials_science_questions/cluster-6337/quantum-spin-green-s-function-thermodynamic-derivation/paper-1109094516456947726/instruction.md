# Quantum Correlations in a Cluster Spin Model with Three-Spin Interactions

## Problem background
This task investigates quantum correlations in a one-dimensional cluster spin-1/2 chain with three-spin interactions of XZX and YZY types, in the presence of a transverse magnetic field. By applying the Jordan-Wigner transformation, the spin model maps to free fermions and can be exactly diagonalized via Fourier transform and a Bogoliubov rotation. The ground state obtained in this way yields analytic expressions for single-site and two-site reduced density matrices, from which various quantum correlation measures and the magnetization can be evaluated. The main goal is to compute these quantities for a finite chain of length N=100 and explore their dependence on the coupling strengths and magnetic field.

## Approach
The approach uses an exact analytical diagonalization. First, the spin operators are expressed in terms of spinless fermion creation and annihilation operators via the Jordan-Wigner mapping. Exploiting translational invariance, a Fourier transform decouples the Hamiltonian into independent momentum modes. Each k-mode is then diagonalized by a Bogoliubov rotation, giving the ground state as a direct product over k with occupation amplitudes determined by the model parameters. From the ground state, one constructs the single-qubit reduced density matrix and the two-qubit (nearest- and next-nearest neighbor) reduced density matrices, which take an X-form. The necessary spin-spin correlation functions (both diagonal and off-diagonal) are expressed in terms of momentum-space sums involving the Bogoliubov angles. These quantities then feed into the formulas for magnetization, concurrence (via Wootters' method), quantum mutual information, quantum discord (by minimizing the conditional entropy over measurement basis parameters), and global entanglement (via the average single-qubit purity). All these computations must be carried out for a grid of magnetic fields and coupling ratios, as specified in the workflow steps.

## Reproduction target
For a chain of N=100 sites, compute the magnetization M^z, nearest-neighbor concurrence C(1,2), next-nearest-neighbor concurrence C(1,3), its first derivatives with respect to J_y and with respect to h (computed via finite differences), quantum mutual information I(1,3), quantum discord D(1,3), and global entanglement E_global. Evaluate these quantities for a parameter grid: h/J_x from -3.0 to 3.0 in steps of 0.1, for five fixed ratios J_y/J_x ∈ {-2, -1, 0, 1, 2} (with J_x set to 1 as the reference scale). Produce a single CSV file at /app/outputs/results.csv containing all results. The required columns, in order, are: J_y_over_J_x, h_over_J_x, magnetization, C_12, C_13, dC_dJ_y, dC_dh, I_13, D_13, E_global. Rows should be ordered first by J_y_over_J_x (ascending, from -2 to 2) and then by h_over_J_x (ascending, from -3.0 to 3.0). All columns are floating-point numbers.

## Assets

- Python 3 with NumPy and SciPy: numpy, scipy

## Workflow steps

### Step 1: Compute intermediate correlation functions
- Role: process
- Action: For each combination of J_y/J_x and h/J_x on the specified grid (J_y/J_x in [-2, -1, 0, 1, 2], h/J_x from -3.0 to 3.0 in steps of 0.1), implement the exact diagonalization of the cluster spin Hamiltonian (Eq. 1) using the Jordan-Wigner transformation, Fourier transform, and Bogoliubov rotation. Numerically evaluate the ground-state angle parameter sin^2(θ_k/2) and sin(θ_k) via A_k and B_k (Eq. 7). Compute the single-site occupation n_l, the auxiliary functions γ(p) and ξ(p) defined in Eq. (18), and the off-diagonal correlation functions ⟨σ1+ σ3+⟩ and ⟨σ1+ σ3−⟩ using Eqs. (19)-(20). These intermediates are needed for the scored step.
- Evidence: `/app/outputs/step_01_correlations.npy`

### Step 2: Evaluate headline correlation measures and write results.csv
- Role: scored (load-bearing)
- Action: Using the intermediate correlation functions from step_01, compute the magnetization M^z (Eq. 15), nearest-neighbour concurrence C(1,2) (Eq. 22 with appropriate matrix elements), next-nearest neighbour concurrence C(1,3) (Eq. 22), its derivatives dC/dJ_y and dC/dh via finite differences, quantum mutual information I(1,3) (Eq. 23), quantum discord D(1,3) (Eqs. 26,27), and global entanglement E_global (Eq. 29). Produce a CSV file /app/outputs/results.csv with columns: J_y_over_J_x, h_over_J_x, magnetization, C_12, C_13, dC_dJ_y, dC_dh, I_13, D_13, E_global. Rows cover h_over_J_x from -3.0 to 3.0 in steps of 0.1, for J_y_over_J_x in [-2, -1, 0, 1, 2].
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV file with header row: J_y_over_J_x, h_over_J_x, magnetization, C_12, C_13, dC_dJ_y, dC_dh, I_13, D_13, E_global. All columns are floating point numbers. Rows ordered by J_y_over_J_x, then by h_over_J_x.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV containing the computed magnetization, nearest and next-nearest neighbour concurrence, concurrence derivatives, quantum mutual information, quantum discord, and global entanglement for the cluster spin model across a grid of J_y/J_x and h/J_x values for N=100.
- schema:
  - `type`: table
  - `columns`:
    - `name`: J_y_over_J_x
    - `type`: float
    - `unit`: dimensionless ratio
    - `name`: h_over_J_x
    - `type`: float
    - `unit`: dimensionless ratio
    - `name`: magnetization
    - `type`: float
    - `unit`: dimensionless
    - `name`: C_12
    - `type`: float
    - `unit`: dimensionless
    - `name`: C_13
    - `type`: float
    - `unit`: dimensionless
    - `name`: dC_dJ_y
    - `type`: float
    - `unit`: 1/(coupling strength J_x)
    - `name`: dC_dh
    - `type`: float
    - `unit`: 1/(transverse field J_x)
    - `name`: I_13
    - `type`: float
    - `unit`: bits
    - `name`: D_13
    - `type`: float
    - `unit`: bits
    - `name`: E_global
    - `type`: float
    - `unit`: dimensionless

Notes: All quantities are computed from the exact analytic expressions derived in the paper. The checker independently recomputes the same quantities using the same formulas and compares column-wise with a relative tolerance of 1e-6. The C_12 column is expected to be zero (within machine epsilon) and is checked separately.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "columns": [
          {
            "name": "J_y_over_J_x",
            "type": "float",
            "unit": "dimensionless ratio"
          },
          {
            "name": "h_over_J_x",
            "type": "float",
            "unit": "dimensionless ratio"
          },
          {
            "name": "magnetization",
            "type": "float",
            "unit": "dimensionless"
          },
          {
            "name": "C_12",
            "type": "float",
            "unit": "dimensionless"
          },
          {
            "name": "C_13",
            "type": "float",
            "unit": "dimensionless"
          },
          {
            "name": "dC_dJ_y",
            "type": "float",
            "unit": "1/(coupling strength J_x)"
          },
          {
            "name": "dC_dh",
            "type": "float",
            "unit": "1/(transverse field J_x)"
          },
          {
            "name": "I_13",
            "type": "float",
            "unit": "bits"
          },
          {
            "name": "D_13",
            "type": "float",
            "unit": "bits"
          },
          {
            "name": "E_global",
            "type": "float",
            "unit": "dimensionless"
          }
        ]
      },
      "description": "CSV containing the computed magnetization, nearest and next-nearest neighbour concurrence, concurrence derivatives, quantum mutual information, quantum discord, and global entanglement for the cluster spin model across a grid of J_y/J_x and h/J_x values for N=100."
    }
  ],
  "notes": "All quantities are computed from the exact analytic expressions derived in the paper. The checker independently recomputes the same quantities using the same formulas and compares column-wise with a relative tolerance of 1e-6. The C_12 column is expected to be zero (within machine epsilon) and is checked separately."
}
```

## How you are scored
A hidden verifier will independently implement the same analytic expressions derived from the exact diagonalization of the cluster model. It will recompute each quantity for every row in your results.csv using the identical parameter grid and compare the values column‑by‑column with a relative tolerance. In addition, the verifier will apply a set of hidden consistency checks derived from the physical properties of the model, but the nature of these checks is not disclosed. Your reward is proportional to the fraction of rows that pass all verification criteria. Reporting numbers that happen to coincide with published values is not sufficient; correctness is judged exclusively by recomputation against the analytic ground truth.
