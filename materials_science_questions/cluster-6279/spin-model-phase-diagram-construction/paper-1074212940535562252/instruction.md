# Reproduce topological re-entrant phase transition in a generalized quasiperiodic modulated SSH model

## Problem background
The one-dimensional Su-Schrieffer-Heeger (SSH) model supports topological phases characterized by edge states and winding numbers. This task extends the standard SSH model by introducing a generalized quasiperiodic modulation on the intracell hopping term,

t₁' = t₁ + λ cos(2πα n + θ) / (1 – b cos(2πα n + θ)) .

Here t₁ is the unmodulated intracell hopping, t₂ = 1 is the intercell hopping (energy unit), λ is the modulation strength, b is a structure factor that controls whether the modulation is bounded (b < 1) or unbounded (b ≥ 1), α = (√5 – 1)/2 is the irrational frequency, θ = 0, and n indexes the primitive cells. The lattice has N = 610 primitive cells (1220 sites). The interplay between topology and quasiperiodic modulation is examined through three quantities: the real-space winding number ν, the logarithm of the bulk energy gap ln(ΔE), and the Lyapunov exponent γ. By computing these observables as λ is varied, one can investigate the topological phase diagram and the nature of any phase transitions.

## Approach
We will directly implement the model and compute the three topological/localization indicators for two representative parameter sets: bounded modulation (b = 0.9, t₁ = 0.8) and unbounded modulation (b = 1.5, t₁ = 1.2). For each λ ∈ [0, 6] (step 0.1), the following steps are performed:

1. Build the intracell hopping sequence t₁'_n from the modulation formula.
2. Lyapunov exponent γ: compute the average γ = |(1/N) Σ_{n=1}^{N} (ln|t₂| – ln|t₁'_n|)|, using t₂ = 1.
3. Open-boundary Hamiltonian (OBC): Construct the full N‑cell SSH Hamiltonian matrix with t₁'_n and t₂, diagonalize to obtain all eigenstates. From the eigenstates, construct the “Q” matrix as Q = Σ_j (|j⟩⟨j| – |Γ⁻¹j⟩⟨Γ⁻¹j|), where Γ is the chiral symmetry operator I_N ⊗ σ_z. Then compute the real-space winding number ν = (1/L') Tr'( Γ Q [Q, X] ), where X is the coordinate operator (diagonal matrix with site indices, repeated for sublattices) and the trace is taken over the central L' = L/2 = N block of the full matrix (rows and columns corresponding to the middle half of the chain). This yields an integer that distinguishes topological phases.
4. Periodic-boundary Hamiltonian (PBC): Construct the PBC Hamiltonian matrix (with t₁'_n and t₂, ensuring the hopping from site L back to site 1), diagonalize, and extract the bulk gap ΔE = E_{N+1} – E_N. Report ln(ΔE).

The computation is performed for each λ, and the three quantities are saved to separate CSV files for the bounded and unbounded cases.

## Reproduction target
Compute and save to two CSV files the winding number ν, the natural logarithm of the bulk gap ln(ΔE), and the Lyapunov exponent γ as functions of λ, for λ ranging from 0.0 to 6.0 in steps of 0.1, for two fixed parameter sets:

- Bounded case: b = 0.9, t₁ = 0.8 → `bounded_case_results.csv`
- Unbounded case: b = 1.5, t₁ = 1.2 → `unbounded_case_results.csv`

Each CSV must contain columns: `lambda`, `winding_number`, `ln_gap`, `lyapunov_exponent`. The winding number is expected to be an integer but should be stored as a float.

## Assets

- NumPy: https://numpy.org
- SciPy: https://scipy.org

## Workflow steps

### Step 1: Compute observables for bounded case
- Role: scored (load-bearing)
- Action: For bounded modulation (b=0.9, t1=0.8), implement the generalized quasiperiodic modulated SSH Hamiltonian and compute the real-space winding number ν, the logarithm of the bulk energy gap ln(ΔE), and the Lyapunov exponent γ as functions of the quasiperiodic modulation strength λ on the interval [0,6] with step 0.1. Save the results to bounded_case_results.csv.
- Output file: `/app/outputs/bounded_case_results.csv`
- Format: csv
- Contract: columns: lambda (float), winding_number (float), ln_gap (float), lyapunov_exponent (float). All values are computed for b=0.9, t1=0.8, λ from 0.0 to 6.0 step 0.1.
- Scoring: scored by hidden verifier

### Step 2: Compute observables for unbounded case
- Role: scored (load-bearing)
- Action: For unbounded modulation (b=1.5, t1=1.2), implement the generalized quasiperiodic modulated SSH Hamiltonian and compute the real-space winding number ν, the logarithm of the bulk energy gap ln(ΔE), and the Lyapunov exponent γ as functions of the quasiperiodic modulation strength λ on the interval [0,6] with step 0.1. Save the results to unbounded_case_results.csv.
- Output file: `/app/outputs/unbounded_case_results.csv`
- Format: csv
- Contract: columns: lambda (float), winding_number (float), ln_gap (float), lyapunov_exponent (float). All values are computed for b=1.5, t1=1.2, λ from 0.0 to 6.0 step 0.1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bounded_case_results.csv`
- `/app/outputs/unbounded_case_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bounded_case_results.csv
- path: `/app/outputs/bounded_case_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Scored artifact for the bounded case. The checker will recompute the Lyapunov exponent and winding number at sampled λ values and compare to the agent's values within tolerance, and verify the re-entrant sequence of ν.
- schema:
  - `type`: table
  - `required_columns`: `lambda`, `winding_number`, `ln_gap`, `lyapunov_exponent`
  - `units`:
    - `lambda`: dimensionless
    - `winding_number`: dimensionless
    - `ln_gap`: dimensionless
    - `lyapunov_exponent`: dimensionless

### unbounded_case_results.csv
- path: `/app/outputs/unbounded_case_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Scored artifact for the unbounded case. The checker will recompute the Lyapunov exponent and winding number at sampled λ values and compare to the agent's values within tolerance, and verify the re-entrant sequence of ν.
- schema:
  - `type`: table
  - `required_columns`: `lambda`, `winding_number`, `ln_gap`, `lyapunov_exponent`
  - `units`:
    - `lambda`: dimensionless
    - `winding_number`: dimensionless
    - `ln_gap`: dimensionless
    - `lyapunov_exponent`: dimensionless

Notes: The observed re-entrant phase transitions are verified via the sequence of winding numbers (type-I for bounded, type-II for unbounded) and the zero-crossings of the Lyapunov exponent at topological transitions, in addition to pointwise recomputations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bounded_case_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda",
          "winding_number",
          "ln_gap",
          "lyapunov_exponent"
        ],
        "units": {
          "lambda": "dimensionless",
          "winding_number": "dimensionless",
          "ln_gap": "dimensionless",
          "lyapunov_exponent": "dimensionless"
        }
      },
      "description": "Scored artifact for the bounded case. The checker will recompute the Lyapunov exponent and winding number at sampled λ values and compare to the agent's values within tolerance, and verify the re-entrant sequence of ν."
    },
    {
      "file": "unbounded_case_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "lambda",
          "winding_number",
          "ln_gap",
          "lyapunov_exponent"
        ],
        "units": {
          "lambda": "dimensionless",
          "winding_number": "dimensionless",
          "ln_gap": "dimensionless",
          "lyapunov_exponent": "dimensionless"
        }
      },
      "description": "Scored artifact for the unbounded case. The checker will recompute the Lyapunov exponent and winding number at sampled λ values and compare to the agent's values within tolerance, and verify the re-entrant sequence of ν."
    }
  ],
  "notes": "The observed re-entrant phase transitions are verified via the sequence of winding numbers (type-I for bounded, type-II for unbounded) and the zero-crossings of the Lyapunov exponent at topological transitions, in addition to pointwise recomputations."
}
```

## How you are scored
A hidden verifier will independently evaluate the two output CSV files. It will:
- Recompute the Lyapunov exponent at a random subset of λ values and compare to your reported values within a set tolerance.
- Recompute the winding number at sampled λ points by diagonalizing the Hamiltonian and applying the real-space winding number formula; your values must match within a tolerance.
- Check that the sequence of winding numbers across λ satisfies certain structural relations consistent with topological phase transitions (e.g., gap closings at transitions).
The two files are weighted equally, and the final score is a weighted combination. Reporting paper values without having run the computation will not earn full credit.
