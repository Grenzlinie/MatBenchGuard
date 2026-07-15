# Spin current in boundary-driven Heisenberg chain from MPS solution

## Problem background
We study spin transport in a boundary-driven isotropic Heisenberg spin-1/2 chain out of equilibrium. The chain of length N is coupled to two Lindblad reservoirs at zero temperature (forcing f=1) and subjected to magnetic fields at the boundaries with strength h and a twisting angle θ. An exact matrix-product-state (MPS) solution exists for the nonequilibrium steady state, yielding a closed analytic expression for the spin current J. The current depends on the chain length N, the reservoir coupling γ, the boundary field h, and the angle θ. Understanding how J changes with these parameters is the central computational task.

## Approach
We implement the MPS solution for the f=1 NESS. The method constructs auxiliary SU(2) operators S_z, S_+, S_- on a semi-infinite representation, together with their doubled counterparts T_z, T_+, T_-. The representation parameter p is fixed by the physical parameters γ and h. These operators define a transfer matrix B0 (tridiagonal) and boundary vectors ⟨0,0| and |ψ,ψ*⟩, where the coherent state |ψ⟩ involves a generalized binomial coefficient and the angle θ. The norm Z(N) = ⟨0,0|B0^N|ψ,ψ*⟩ is computed, from which the steady-state spin current is obtained as J = (2γ/(γ²+h²)) · Z(N-1)/Z(N). By evaluating J for many combinations of N, γ, h, and θ, one can observe how the current scales with system size and field strength.

## Reproduction target
Produce a CSV file `spin_current.csv` with columns N, h, gamma, theta, J. Compute the steady-state spin current J for each parameter combination listed in the table below using the MPS method. The output must contain exactly these rows (the ordering may differ).

| N   | h     | gamma  | theta |
|-----|-------|--------|-------|
| 10  | 0.0   | 1e-5   | 0.0   |
| 10  | 0.0   | 0.01   | 0.0   |
| 10  | 0.0   | 1.0    | 0.0   |
| 50  | 0.0   | 1e-5   | 0.0   |
| 50  | 0.0   | 0.01   | 0.0   |
| 50  | 0.0   | 1.0    | 0.0   |
| 100 | 0.0   | 1e-5   | 0.0   |
| 100 | 0.0   | 0.01   | 0.0   |
| 100 | 0.0   | 1.0    | 0.0   |
| 200 | 0.0   | 1e-5   | 0.0   |
| 200 | 0.0   | 0.01   | 0.0   |
| 200 | 0.0   | 1.0    | 0.0   |
| 500 | 0.0   | 1e-5   | 0.0   |
| 500 | 0.0   | 0.01   | 0.0   |
| 500 | 0.0   | 1.0    | 0.0   |
| 500 | -0.1  | 1e-5   | 0.0   |
| 500 | -0.05 | 1e-5   | 0.0   |
| 500 | -0.02 | 1e-5   | 0.0   |
| 500 | -0.01 | 1e-5   | 0.0   |
| 500 | 0.01  | 1e-5   | 0.0   |
| 500 | 0.05  | 1e-5   | 0.0   |
| 100 | -0.1  | 0.01   | 0.0   |
| 100 | -0.05 | 0.01   | 0.0   |
| 100 | 0.0   | 0.01   | 0.0   |
| 100 | 0.05  | 0.01   | 0.0   |
| 100 | -0.1  | 1.0    | 0.0   |
| 100 | 0.0   | 1.0    | 0.0   |
| 100 | 0.1   | 1.0    | 0.0   |
| 500 | 0.0   | 1e-5   | 0.1   |

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Construct MPS representation
- Role: process
- Action: Implement the matrix-product state solution for the f=1 NESS. Construct the auxiliary operators S_z, S_+, S_- and the doubled operators T_z, T_+, T_- using the complex representation parameter p = i/(2(γ-ih)). Build the transfer matrix B0 (tridiagonal) and the boundary vectors ⟨0,0|, |ψ,ψ*⟩. Truncate the semi-infinite auxiliary space to a finite dimension M (e.g., M=50). Save the matrices/vectors to mps_checkpoint.npy for later use.
- Evidence: `/app/outputs/mps_checkpoint.npy`

### Step 2: Compute spin current J
- Role: scored (load-bearing)
- Action: For each provided parameter combination (N, h, γ, θ) use the constructed MPS representation to compute the normalization Z(N) = ⟨0,0|B0^N|ψ,ψ*⟩, then evaluate J = (2γ/(γ²+h²)) * Z(N-1)/Z(N). Write all results to spin_current.csv.
- Output file: `/app/outputs/spin_current.csv`
- Format: csv
- Contract: CSV with columns: N (integer), h (float), gamma (float), theta (float), J (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spin_current.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spin_current.csv
- path: `/app/outputs/spin_current.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Steady-state spin current J computed from the MPS solution. The checker recomputes J for each row using its own reference implementation and scores based on relative error tolerance.
- schema:
  - `type`: table
  - `required_columns`: `N`, `h`, `gamma`, `theta`, `J`
  - `units`:
    - `N`: integer
    - `h`: float (coupling strength)
    - `gamma`: float (coupling rate)
    - `theta`: float (angle in radians)
    - `J`: float (spin current)

Notes: The parameter grid will be specified in the task instructions. The agent must produce J values for all requested combinations. The MPS representation construction step (step1) is a required intermediate; the evidence file mps_checkpoint.npy is not scored but must be produced to ensure the workflow was run.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spin_current.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "h",
          "gamma",
          "theta",
          "J"
        ],
        "units": {
          "N": "integer",
          "h": "float (coupling strength)",
          "gamma": "float (coupling rate)",
          "theta": "float (angle in radians)",
          "J": "float (spin current)"
        }
      },
      "description": "Steady-state spin current J computed from the MPS solution. The checker recomputes J for each row using its own reference implementation and scores based on relative error tolerance."
    }
  ],
  "notes": "The parameter grid will be specified in the task instructions. The agent must produce J values for all requested combinations. The MPS representation construction step (step1) is a required intermediate; the evidence file mps_checkpoint.npy is not scored but must be produced to ensure the workflow was run."
}
```

## How you are scored
A hidden verifier will independently compute the spin current for the same parameter combinations using its own reference implementation of the MPS formulas. For each row in your `spin_current.csv`, it compares your J value to the reference J, and the per-row reward reflects agreement within tolerance. The final score aggregates these rewards across all rows. Additionally, the verifier may check that your results exhibit the expected structural trends (e.g., scaling of J with N, asymmetry with respect to h) to confirm the reproduction.
