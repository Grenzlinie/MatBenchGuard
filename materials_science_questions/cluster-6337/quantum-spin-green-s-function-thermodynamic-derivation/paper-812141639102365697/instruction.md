# Self-Consistent Harmonic Approximation for 1D XY Model with J1-J2 Frustration

## Problem background
The one-dimensional spin-1 XY antiferromagnetic Heisenberg model with nearest-neighbor (J1) and next-nearest-neighbor (J2) exchange interactions exhibits frustration when both interactions are antiferromagnetic and J2 is comparable to J1. The competition between the two interactions can induce a helical ordering with a wave number that depends on the ratio δ = J2/J1. The self-consistent harmonic approximation (SCHA) is an analytical method that incorporates quantum and thermal fluctuations to obtain renormalized spin-wave dispersion, pair correlation functions, and the longitudinal susceptibility. Understanding how the dispersion relation's maximum shifts with δ, whether the correlation decays monotonically or oscillates, and where the susceptibility peaks as temperature varies reveals the physics of the frustration-driven transition.

## Approach
The SCHA replaces the original XY Hamiltonian with an effective quadratic Hamiltonian whose stiffness parameters ρ1 and ρ2 are determined self-consistently as functions of temperature and δ. Using the Villain representation, one assumes a spiral pitch α: antiparallel alignment when δ<0.25 (α=π), and helical ordering with α = arccos(1/(4δ)) when δ≥0.25. The effective Hamiltonian yields a renormalized dispersion ω(q) that depends on the stiffnesses. The self-consistency loop computes the boson occupation n(q) and the fluctuation averages that update ρ1 and ρ2 until convergence. After convergence, ω(q) is evaluated on a fine q grid. From the converged quantities, the in-plane pair correlation function |⟨cos(φ0−φl)⟩| for spin separations l is computed via an integral involving c(q) and n(q). The longitudinal susceptibility multiplied by temperature, χ_{1D}(q)T, is then obtained by Fourier transforming the correlation function. All results emerge numerically from the solution of the model for the specified sets of (δ,T).

## Reproduction target
Implement the SCHA solver for the 1D XY model with S=1, J1=1, and variable J2=δ. For the prescribed (δ,T) parameter sets, produce three CSV artifacts:
1) Spin-wave dispersion ω(q) (δ=0.1,0.3,0.6 at T=0.15 J1).
2) In-plane pair correlation function |⟨cos(φ0−φl)⟩| for l=0..50 (δ=0.24 at T=0.1,0.2,0.3 J1; δ=0.30 at T=0.02,0.08,0.12,0.2 J1).
3) Longitudinal susceptibility χ_{1D}(q)T (δ=0.10 at T=0.1,0.2,0.3 J1; δ=0.30 at T=0.1,0.2,0.3 J1).
The hidden verifier will evaluate the artifacts against the model's physical behaviour. Submit your self-consistent numerical results as CSV files under /app/outputs.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Self-consistent SCHA solution and spin-wave dispersion
- Role: scored
- Action: For each (δ, T) pair specified in the task (dispersion: δ=0.1,0.3,0.6 at T=0.15 J1), set up the 1D XY model with S=1, J1=1, J2=δ, use the spiral pitch α = arccos(1/(4δ)) for δ≥0.25 else α=π. Initialize spin stiffnesses ρ1=ρ2=1. Iteratively solve the SCHA coupled equations (fluctuation averages, renormalized stiffnesses, c(q), and boson occupation n(q) with ω(q)=2√[(J1+J2)c(q)]) on a finite lattice until convergence. On a fine q grid (0 to π, step ≤0.01) compute the spin-wave dispersion ω(q) and save to step_01_dispersion.csv.
- Output file: `/app/outputs/step_01_dispersion.csv`
- Format: csv
- Contract: CSV with columns: delta (float, frustration ratio), temperature (float, in units of J1), q (float, wavevector in radians), omega (float, spin-wave energy).
- Scoring: scored by hidden verifier

### Step 2: In-plane pair correlation function
- Role: scored (load-bearing)
- Action: Using the converged self-consistent SCHA solution (c(q), n(q)), compute |⟨cos(φ0-φl)⟩| for spin separations l = 0 to 50 according to the standard formula involving an integral over c(k) and n(k), for all specified (δ,T) pairs (δ=0.24 at T=0.1,0.2,0.3 J1; δ=0.30 at T=0.02,0.08,0.12,0.2 J1). Output to step_02_correlation.csv.
- Output file: `/app/outputs/step_02_correlation.csv`
- Format: csv
- Contract: CSV with columns: delta (float), temperature (float), separation_l (int), correlation (float, absolute value of the correlation).
- Scoring: scored by hidden verifier

### Step 3: Longitudinal susceptibility
- Role: scored
- Action: From the correlation function data (step_02_correlation.csv), compute the longitudinal susceptibility χ_{1D}(q)T (with gμ_B=1) by Fourier transform on a q grid from 0 to π with step ≤0.02, for the specified (δ,T) pairs (δ=0.10 at T=0.1,0.2,0.3 J1; δ=0.30 at T=0.1,0.2,0.3 J1). Save to step_03_susceptibility.csv.
- Output file: `/app/outputs/step_03_susceptibility.csv`
- Format: csv
- Contract: CSV with columns: delta (float), temperature (float), q (float, rad), chi_T (float, susceptibility×T).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_dispersion.csv`
- `/app/outputs/step_02_correlation.csv`
- `/app/outputs/step_03_susceptibility.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_dispersion.csv
- path: `/app/outputs/step_01_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Spin-wave dispersion ω(q) for δ=0.1, 0.3, 0.6 at T=0.15 J1. Contains the renormalised spin-wave energy ω as a function of wavevector q, frustration ratio δ, and temperature.
- schema:
  - `type`: table
  - `required_columns`: `delta`, `temperature`, `q`, `omega`
  - `units`:
    - `delta`: dimensionless
    - `temperature`: J1 units
    - `q`: radians
    - `omega`: J1 units

### step_02_correlation.csv
- path: `/app/outputs/step_02_correlation.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: In-plane pair correlation function |⟨cos(φ0−φl)⟩| for spin separations l=0..50, computed for specified (δ,T) pairs. Contains the absolute correlation value against separation distance.
- schema:
  - `type`: table
  - `required_columns`: `delta`, `temperature`, `separation_l`, `correlation`
  - `units`:
    - `delta`: dimensionless
    - `temperature`: J1 units
    - `separation_l`: lattice spacing
    - `correlation`: dimensionless

### step_03_susceptibility.csv
- path: `/app/outputs/step_03_susceptibility.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Longitudinal susceptibility multiplied by temperature, χ_{1D}(q)T, as a function of wavevector q for specified (δ,T) pairs. Obtained via Fourier transform of the correlation function.
- schema:
  - `type`: table
  - `required_columns`: `delta`, `temperature`, `q`, `chi_T`
  - `units`:
    - `delta`: dimensionless
    - `temperature`: J1 units
    - `q`: radians
    - `chi_T`: dimensionless (susceptibility × T)

Notes: The scored artifacts are checked against structural criteria (peak locations, monotonic vs. oscillatory decay, trend of peak shift). No absolute numeric tolerances are applied. The solver must implement the SCHA on a finite lattice; the checker does not validate internal convergence details.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_dispersion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta",
          "temperature",
          "q",
          "omega"
        ],
        "units": {
          "delta": "dimensionless",
          "temperature": "J1 units",
          "q": "radians",
          "omega": "J1 units"
        }
      },
      "description": "Spin-wave dispersion ω(q) for δ=0.1, 0.3, 0.6 at T=0.15 J1. Contains the renormalised spin-wave energy ω as a function of wavevector q, frustration ratio δ, and temperature."
    },
    {
      "file": "step_02_correlation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta",
          "temperature",
          "separation_l",
          "correlation"
        ],
        "units": {
          "delta": "dimensionless",
          "temperature": "J1 units",
          "separation_l": "lattice spacing",
          "correlation": "dimensionless"
        }
      },
      "description": "In-plane pair correlation function |⟨cos(φ0−φl)⟩| for spin separations l=0..50, computed for specified (δ,T) pairs. Contains the absolute correlation value against separation distance."
    },
    {
      "file": "step_03_susceptibility.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta",
          "temperature",
          "q",
          "chi_T"
        ],
        "units": {
          "delta": "dimensionless",
          "temperature": "J1 units",
          "q": "radians",
          "chi_T": "dimensionless (susceptibility × T)"
        }
      },
      "description": "Longitudinal susceptibility multiplied by temperature, χ_{1D}(q)T, as a function of wavevector q for specified (δ,T) pairs. Obtained via Fourier transform of the correlation function."
    }
  ],
  "notes": "The scored artifacts are checked against structural criteria (peak locations, monotonic vs. oscillatory decay, trend of peak shift). No absolute numeric tolerances are applied. The solver must implement the SCHA on a finite lattice; the checker does not validate internal convergence details."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the three CSV files. For each artifact, the verifier independently checks the required structural properties (peak locations, monotonic/oscillatory behavior, temperature-induced peak shift) and assigns a partial reward according to a predetermined weight. The final reward is the weighted sum across all artifacts. Simply reporting numbers is not sufficient; the artifacts must exhibit the correct qualitative trends and satisfy the structural criteria described in the output contract. The verifier does not disclose its tolerances, so aim for a self-consistent and accurate implementation.
