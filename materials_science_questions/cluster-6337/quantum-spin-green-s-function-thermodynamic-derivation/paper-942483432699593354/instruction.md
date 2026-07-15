# Single-Mode Approximation Excitation Dispersion of 2D Heisenberg Antiferromagnet

## Problem background
Obtaining the dynamical excitation spectrum of quantum spin systems is a difficult numerical problem, especially for large sizes. The Single-Mode Approximation (SMA) provides a variational upper bound for the lowest excitation energy at a given momentum. When combined with quantum Monte Carlo (QMC) simulations—such as Stochastic Series Expansion (SSE) or projector QMC—it offers a computationally efficient way to estimate the dispersion. The problem is to apply the SMA+QMC method to the two-dimensional antiferromagnetic Heisenberg model on a square lattice and compute the excitation dispersion along a high-symmetry path, as well as the finite-size scaling of the energy gap at the M point.

## Approach
The SMA constructs a trial excited state by acting the Fourier-transformed spin operator on the ground state. The resulting dispersion is given by the ratio of the expectation value of the double commutator of the Hamiltonian with the spin operator to the equal-time spin structure factor. In the SSE QMC framework, this double commutator can be measured by sampling spin configurations and using a specific estimator based on randomly chosen non-identity operators. In the projector QMC framework (applicable to SU(2)-symmetric Hamiltonians), the double commutator simplifies to a weighted sum of spin-spin correlations, which can be obtained directly from valence-bond loop configurations. The agent must implement either method and simulate the square-lattice Heisenberg model with nearest-neighbor interactions (coupling J=1) and periodic boundary conditions. The simulations for lattice sizes L=16, 32, and 64 produce the raw correlations and structure factors needed to compute the SMA numerator and denominator.

## Reproduction target
The reproduction target is to produce three scored artifacts:
1. The raw spin-spin correlations for L=32 (file correlations_L32.dat).
2. The SMA excitation dispersion omega(q) for L=32 along the path Gamma(0,0) -> M(pi,pi) -> X(pi,0) -> Gamma(0,0) (file dispersion_L32.dat).
3. The M-point gap for L=16, 32, 64 to demonstrate finite-size scaling (file gap_scaling.dat).
These artifacts will be independently verified by a hidden checker. No external datasets are required; the procedure is entirely computational.

## Assets

- Standard numerical computing packages: numpy scipy mpi4py

## Workflow steps

### Step 1: Implement QMC code with SMA measurement
- Role: process
- Action: Develop a program that performs a Quantum Monte Carlo simulation (projector QMC or SSE) for the 2D antiferromagnetic Heisenberg model on a square lattice. Implement the Single-Mode Approximation measurement: compute the numerator f(q) using either the double-commutator SSE estimator or the spin-spin correlation formula for projector QMC, and compute the denominator S_z^2(q) from equal-time correlations. The code must support periodic boundary conditions and square lattices of sizes up to 64x64.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Run simulations for L=16, 32, 64 and collect raw data
- Role: process
- Action: Execute the SMA+QMC code for lattice sizes L=16, 32, and 64. Collect the spin-spin correlation functions <S_i·S_j> and the SMA numerator/denominator estimators for the required q-points. Store the raw data (correlations matrices, structure factor S_z^2(q), etc.) in a format suitable for post-processing.
- Evidence: none

### Step 3: Output raw spin-spin correlations for L=32
- Role: scored
- Action: From the L=32 simulation data, extract the equal-time spin-spin correlation <S_i·S_j> for all displacement vectors (dx,dy) up to L/2. Write a three-column file (dx, dy, correlation) to /app/outputs/correlations_L32.dat. The correlation must be the SU(2)-invariant <S_i·S_j> if using projector QMC, or <S_i^z S_j^z> if using SSE; use the same correlation type that is consistent with the dispersion computation.
- Output file: `/app/outputs/correlations_L32.dat`
- Format: txt
- Contract: Three whitespace-separated columns: dx (integer), dy (integer), corr (real number). dx and dy range from 0 to L/2.
- Scoring: scored by hidden verifier

### Step 4: Compute SMA dispersion for L=32
- Role: scored (load-bearing)
- Action: From the L=32 simulation data, compute the SMA numerator f(q) and denominator S_z^2(q) for momentum points along the path Γ(0,0)→M(π,π)→X(π,0)→Γ(0,0). Use the appropriate formula (the double-commutator estimator or the spin-spin correlation formula). Calculate ω(q)=f(q)/S_z^2(q). Write the dispersion to /app/outputs/dispersion_L32.dat with columns kx, ky, omega_q.
- Output file: `/app/outputs/dispersion_L32.dat`
- Format: csv
- Contract: Whitespace-separated columns: kx (real), ky (real), omega_q (real). At least 8 points along the path, including the exact Γ(0,0) and M(π,π).
- Scoring: scored by hidden verifier

### Step 5: Compute M-point gap scaling for L=16,32,64
- Role: scored
- Action: For each lattice size L=16, 32, 64, extract the SMA energy gap ω at the M point (q=(π,π)) from the simulation data. Write /app/outputs/gap_scaling.dat with columns L, gap_at_M.
- Output file: `/app/outputs/gap_scaling.dat`
- Format: txt
- Contract: Whitespace-separated columns: L (integer), gap_at_M (real, positive). Contains exactly three rows (L=16,32,64).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/correlations_L32.dat`
- `/app/outputs/dispersion_L32.dat`
- `/app/outputs/gap_scaling.dat`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### correlations_L32.dat
- path: `/app/outputs/correlations_L32.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Raw spin-spin correlations for L=32, used by the checker to independently recompute f(q) and verify internal consistency.
- schema:
  - `type`: table
  - `required_columns`: `dx`, `dy`, `corr`
  - `units`:
    - `dx`: lattice units
    - `dy`: lattice units
    - `corr`: dimensionless

### dispersion_L32.dat
- path: `/app/outputs/dispersion_L32.dat`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: SMA excitation dispersion for L=32 along the high-symmetry path. Checked against spin-wave theory and internal consistency with correlations.
- schema:
  - `type`: table
  - `required_columns`: `kx`, `ky`, `omega_q`
  - `units`:
    - `kx`: radians
    - `ky`: radians
    - `omega_q`: energy (units of J)

### gap_scaling.dat
- path: `/app/outputs/gap_scaling.dat`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Finite-size scaling of the M-point gap. The gap is expected to vanish in the thermodynamic limit.
- schema:
  - `type`: table
  - `required_columns`: `L`, `gap_at_M`
  - `units`:
    - `L`: lattice size
    - `gap_at_M`: energy (units of J)

Notes: The checker will verify the L=32 dispersion against the spin-wave theory formula for the Heisenberg model and also recompute f(q) from the raw correlations to confirm internal consistency. The gap scaling data must show a decreasing trend with increasing L, with the L=64 gap below a hidden threshold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "correlations_L32.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "dx",
          "dy",
          "corr"
        ],
        "units": {
          "dx": "lattice units",
          "dy": "lattice units",
          "corr": "dimensionless"
        }
      },
      "description": "Raw spin-spin correlations for L=32, used by the checker to independently recompute f(q) and verify internal consistency."
    },
    {
      "file": "dispersion_L32.dat",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "kx",
          "ky",
          "omega_q"
        ],
        "units": {
          "kx": "radians",
          "ky": "radians",
          "omega_q": "energy (units of J)"
        }
      },
      "description": "SMA excitation dispersion for L=32 along the high-symmetry path. Checked against spin-wave theory and internal consistency with correlations."
    },
    {
      "file": "gap_scaling.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "gap_at_M"
        ],
        "units": {
          "L": "lattice size",
          "gap_at_M": "energy (units of J)"
        }
      },
      "description": "Finite-size scaling of the M-point gap. The gap is expected to vanish in the thermodynamic limit."
    }
  ],
  "notes": "The checker will verify the L=32 dispersion against the spin-wave theory formula for the Heisenberg model and also recompute f(q) from the raw correlations to confirm internal consistency. The gap scaling data must show a decreasing trend with increasing L, with the L=64 gap below a hidden threshold."
}
```

## How you are scored
Your submitted artifacts will be evaluated by an automated verifier. It will read each scored output file, recompute intermediate quantities where applicable, and compare against hidden reference data. Each scored stage has an assigned weight, and the final reward is a weighted sum (a float between 0 and 1). Simply reporting numbers that appear plausible is not sufficient—the verifier checks internal consistency (e.g., recomputing the dispersion from the raw correlations) and verifies that the required formats, columns, and data ranges are respected.
