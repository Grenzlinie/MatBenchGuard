# Colloidal equilibrium in insulating crystals: electrostatic energy and phase properties

## Problem background
In insulating compounds where only ions of one sign are mobile, diffusive decomposition into chemically ordered precipitates creates locally charged domains. Electrostatic repulsion between these charged precipitates competes with interfacial energy, potentially preventing coarsening and stabilising a mesoscopic "crystalline colloidal" state. The model predicts that the equilibrium precipitate volume fraction, miscibility gap, and precipitate radius may depend on the overall stoichiometry in a non-trivial way, challenging the conventional lever rule. The task is to compute, for a fixed material parameter, how these equilibrium quantities vary with the stoichiometry.

## Approach
The model considers a distribution of spherical precipitates of a second phase embedded in a matrix. To minimise Coulomb repulsion, the precipitates are assumed to be arranged on a face-centred cubic (fcc) macrolattice. The total free energy includes a bulk chemical contribution, an interfacial term, and an electrostatic energy that depends on the composition mismatch and the precipitate arrangement through a dimensionless lattice-sum constant α(ω), where ω is the precipitate volume fraction.

First, α(ω) is computed for the fcc lattice, either by performing a reciprocal-space summation or by using an asymptotic expansion valid at small ω. Then, for a fixed material constant ξ that controls the balance between electrostatic/interfacial and chemical driving forces, the free energy is minimised with respect to two internal variables: the precipitate volume fraction ω and the normalised composition gap x (the ratio of the actual composition difference to the composition difference in the absence of electrostatic effects). This minimisation yields the equilibrium values ω_eq and x_eq as functions of ω₀, a parameter proportional to the average stoichiometry. Finally, the equilibrium reduced precipitate radius R_eq/R₀₀ is derived from ω_eq and x_eq. The entire calculation is repeated for a range of ω₀ to obtain the requested curves.

## Reproduction target
For the material constant ξ = 0.5, compute the equilibrium volume fraction ω_eq, the normalised miscibility gap parameter x_eq, and the reduced precipitate radius R_eq/R₀₀ as functions of the stoichiometry parameter ω₀. Provide the results as a CSV file named equilibrium_curves.csv with columns omega0, omega_eq, x_eq, and R_eq_norm, for ω₀ ranging from 0.0 to 0.5 in steps of 0.01. All quantities are dimensionless. Write the file to /app/outputs.

## Assets

- Python 3 with NumPy and SciPy: python3

## Workflow steps

### Step 1: Compute α(ω) for the fcc precipitate macrolattice
- Role: process
- Action: Implement the dimensionless lattice‑sum constant α(ω) for spherical precipitates arranged on a face‑centered cubic (fcc) macrolattice. Either evaluate the reciprocal‑lattice sum directly or use the asymptotic expansion α(ω) ≈ 6/5 − √π ω^{1/3}, producing a callable function of the precipitate volume fraction ω.
- Evidence: none

### Step 2: Compute equilibrium curves for ξ=0.5
- Role: scored (load-bearing)
- Action: For the fixed material constant ξ=0.5 and for each volume‑fraction parameter ω0 from 0 to 0.5 in steps of 0.01, minimise the free energy functional derived from the paper (using the α(ω) function from Step1) to obtain the equilibrium precipitate volume fraction ω_eq and the normalised miscibility gap x_eq. Then compute the normalised equilibrium radius R_eq/R00 = x_eq^{-2/3} α(ω_eq)^{-1/3}. Write the results to equilibrium_curves.csv.
- Output file: `/app/outputs/equilibrium_curves.csv`
- Format: csv
- Contract: CSV with header and four columns: omega0 (float), omega_eq (float), x_eq (float), R_eq_norm (float). Each row corresponds to one ω0 value; units are dimensionless.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_curves.csv
- path: `/app/outputs/equilibrium_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium precipitate volume fraction, miscibility gap parameter, and reduced radius as functions of the stoichiometry parameter ω0 for ξ=0.5.
- schema:
  - `type`: table
  - `required_columns`: `omega0`, `omega_eq`, `x_eq`, `R_eq_norm`
  - `description`: Each row contains the dimensionless equilibrium parameters for a given ω0.

Notes: The hidden checker compares each row’s omega_eq, x_eq, and R_eq_norm against paper‑derived reference values using absolute tolerances (±0.02 for omega_eq and x_eq, ±0.05 for R_eq_norm). Rows that fall within tolerances earn proportional credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega0",
          "omega_eq",
          "x_eq",
          "R_eq_norm"
        ],
        "description": "Each row contains the dimensionless equilibrium parameters for a given ω0."
      },
      "description": "Equilibrium precipitate volume fraction, miscibility gap parameter, and reduced radius as functions of the stoichiometry parameter ω0 for ξ=0.5."
    }
  ],
  "notes": "The hidden checker compares each row’s omega_eq, x_eq, and R_eq_norm against paper‑derived reference values using absolute tolerances (±0.02 for omega_eq and x_eq, ±0.05 for R_eq_norm). Rows that fall within tolerances earn proportional credit."
}
```

## How you are scored
A hidden verifier reads your equilibrium_curves.csv and compares the submitted omega_eq, x_eq, and R_eq_norm values at each ω₀ against pre-established reference values. The reward is proportional to the fraction of rows for which all three quantities are within acceptable margins of the references. The verification accounts for legitimate numerical differences that arise from different implementation choices; simply fabricating numbers or reporting values without running the required computation will not satisfy the checker.
