# Transfer-Matrix Detection of Phase Transitions in Hard-Core Triangular Lattice Gases

## Problem background
Determining the existence and nature of phase transitions in hard‑core lattice gases is a classic problem in statistical mechanics. For a triangular lattice with exclusion up to second or third neighbours, the close‑packed states are perfectly ordered and well defined. The transfer‑matrix method applied to semi‑infinite lattice strips bent into tori can reveal singularities in thermodynamic quantities — notably the isothermal compressibility — as the torus circumference n is increased. A rapidly growing compressibility peak, shifting with n, signals a phase transition. The target is to compute these compressibility curves and, from the largest‑n results, extract transition parameters (chemical potential, reduced pressure, density gap) to characterise the transition.

## Approach
The method constructs a transfer matrix for a given torus width n and a given model of hard‑core exclusion. Each matrix element corresponds to allowed configurations of a row of n sites, consistent with the exclusion constraints. The largest eigenvalue λ₀ is found numerically as a function of the reduced chemical potential μ/kT. The grand potential per site follows from Ω = −kT ln λ₀. Subsequent numerical differentiation gives the density ρ and the isothermal compressibility kT ∂ρ/∂μ. Two hard‑core models are studied:
• Case B: second‑neighbour exclusion (maximum close‑packed density ρ₀ = 1/4) on tori of even circumference n = 2,4,…,12.
• Case C: third‑neighbour exclusion (ρ₀ = 1/7) on tori of circumference n = 7,14.
For each model the compressibility is computed over a dense range of μ/kT that spans the expected transition region. The data for the largest n are saved; from these, the dominant compressibility peak identifies the transition, and the integrated (or equal‑area) analysis yields the reduced pressure p/(ρ₀kT) and the density gap Δρ/ρ₀.

## Reproduction target
Produce three output artifacts:
  1. a CSV file `case_B_compressibility_n12.csv` with columns (mu_kT, compressibility) for case B at n=12,
  2. a CSV file `case_C_compressibility_n14.csv` with columns (mu_kT, compressibility) for case C at n=14,
  3. a CSV file `transition_parameters.csv` with columns (case, mu_kT, p_over_rho0kT, density_gap) containing the estimated transition location, reduced pressure, and density gap for each case.
The transition chemical potential is defined as the μ/kT at the compressibility maximum; the reduced pressure and density gap follow from the eigenvalue data and the density jump or equal‑area construction.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Case B compressibility (n=12)
- Role: scored
- Action: Implement the transfer-matrix method for the triangular lattice gas with second-neighbour exclusion (case B). Construct the transfer matrices for even torus circumferences n = 2,4,6,8,10,12 over a fine grid of μ/kT values. From the largest eigenvalue, compute the grand potential and then derive the isothermal compressibility kT ∂ρ/∂μ as a function of μ/kT. For n=12, write the compressibility data as a CSV.
- Output file: `/app/outputs/case_B_compressibility_n12.csv`
- Format: csv
- Contract: Two columns: mu_kT (float), compressibility (float)
- Scoring: scored by hidden verifier

### Step 2: Case C compressibility (n=14)
- Role: scored
- Action: Implement the transfer-matrix method for the triangular lattice gas with third-neighbour exclusion (case C). Construct transfer matrices for torus circumferences n=7 and n=14 over a fine grid of μ/kT values. Compute the isothermal compressibility from the largest eigenvalue. For n=14, write the compressibility data as a CSV.
- Output file: `/app/outputs/case_C_compressibility_n14.csv`
- Format: csv
- Contract: Two columns: mu_kT (float), compressibility (float)
- Scoring: scored by hidden verifier

### Step 3: Transition parameters
- Role: scored (load-bearing)
- Action: From the compressibility curves for n=12 (case B) and n=14 (case C), locate the dominant compressibility peak. Estimate the transition chemical potential (μ/kT)* as the peak position. Use the transfer-matrix eigenvalue information to evaluate the reduced pressure p/(ρ0 kT) at that μ/kT. Determine the density jump (gap) ρ*/ρ0 from the discontinuity in the density vs. chemical potential relation, or by the Maxwell equal-area construction (or equivalent finite‑n estimate). Report the three parameters for both case B and case C in a CSV table.
- Output file: `/app/outputs/transition_parameters.csv`
- Format: csv
- Contract: Columns: case (string, 'B' or 'C'), mu_kT (float), p_over_rho0kT (float), density_gap (float). One row per case.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/case_B_compressibility_n12.csv`
- `/app/outputs/case_C_compressibility_n14.csv`
- `/app/outputs/transition_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### case_B_compressibility_n12.csv
- path: `/app/outputs/case_B_compressibility_n12.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Compressibility kT ∂ρ/∂μ vs. μ/kT for case B at n=12.
- schema:
  - `type`: table
  - `required_columns`: `mu_kT`, `compressibility`
  - `units`:
    - `mu_kT`: dimensionless
    - `compressibility`: dimensionless

### case_C_compressibility_n14.csv
- path: `/app/outputs/case_C_compressibility_n14.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Compressibility kT ∂ρ/∂μ vs. μ/kT for case C at n=14.
- schema:
  - `type`: table
  - `required_columns`: `mu_kT`, `compressibility`
  - `units`:
    - `mu_kT`: dimensionless
    - `compressibility`: dimensionless

### transition_parameters.csv
- path: `/app/outputs/transition_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Estimated transition parameters for cases B and C.
- schema:
  - `type`: table
  - `required_columns`: `case`, `mu_kT`, `p_over_rho0kT`, `density_gap`
  - `units`:
    - `mu_kT`: dimensionless
    - `p_over_rho0kT`: dimensionless
    - `density_gap`: dimensionless

Notes: Compressibility curves are verified by structural audit (peak existence and location consistency). Transition parameters are compared to hidden reference values with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "case_B_compressibility_n12.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "mu_kT",
          "compressibility"
        ],
        "units": {
          "mu_kT": "dimensionless",
          "compressibility": "dimensionless"
        }
      },
      "description": "Compressibility kT ∂ρ/∂μ vs. μ/kT for case B at n=12."
    },
    {
      "file": "case_C_compressibility_n14.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "mu_kT",
          "compressibility"
        ],
        "units": {
          "mu_kT": "dimensionless",
          "compressibility": "dimensionless"
        }
      },
      "description": "Compressibility kT ∂ρ/∂μ vs. μ/kT for case C at n=14."
    },
    {
      "file": "transition_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "mu_kT",
          "p_over_rho0kT",
          "density_gap"
        ],
        "units": {
          "mu_kT": "dimensionless",
          "p_over_rho0kT": "dimensionless",
          "density_gap": "dimensionless"
        }
      },
      "description": "Estimated transition parameters for cases B and C."
    }
  ],
  "notes": "Compressibility curves are verified by structural audit (peak existence and location consistency). Transition parameters are compared to hidden reference values with tolerances."
}
```

## How you are scored
The hidden verifier evaluates each declared artifact. The two compressibility CSV files are checked for correct format, presence of a clear compressibility peak consistent with the reported transition, and internal consistency. The transition parameters CSV is compared to a hidden reference (a known correct set of values derived from the method) within predetermined tolerances. The final reward is a weighted combination of the per‑step scores, with the transition parameters carrying the highest weight. Reporting values without correctly executing the computational workflow will not receive full credit.
