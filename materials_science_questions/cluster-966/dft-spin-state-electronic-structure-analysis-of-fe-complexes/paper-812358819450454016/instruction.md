# Compute Effective Magnetic Moments for the 5T2g Term under Tetragonal Symmetry

## Scope note on excluded stages
The paper also uses the computed magnetic moments to fit experimental data for nine iron(II) complexes, yielding best‑fit parameters (k, λ, Δ). This fitting stage is excluded from the reproduction target because the original curve fitting was performed by visual comparison of plots, not by a defined computational algorithm, and the paper does not specify a reproducible numerical fitting procedure or loss function. The task therefore concentrates on reproducing the underlying theoretical magnetic moments, which are the verifiable computational core.

## Problem background
Octahedral iron(II) complexes with a high‑spin d⁶ configuration possess a ⁵T₂g ground term. When the octahedron is subjected to a low‑symmetry (tetragonal) ligand field, the orbital degeneracy is partially lifted. The simultaneous action of spin‑orbit coupling and the axial field creates a complex energy‑level pattern that determines the effective magnetic moment (μ_eff) of the complex. This moment depends on the orbital reduction factor k, the ratio v = Δ/λ between the axial splitting and the spin‑orbit coupling constant, and the reduced temperature kT/λ. Predicting μ_eff over a wide range of these parameters is essential for interpreting magnetic susceptibility data. This task asks you to compute μ_eff for a prescribed grid of (k, v, kT/λ) values using the perturbation‑matrix approach described below.

## Approach
The calculation proceeds in three stages:

1. **Basis construction.** Use the three real t₂g orbitals appropriate for tetragonal symmetry: |1⟩, |−1⟩ (the d_xz/d_yz pair) and |xy⟩ = (|2⟩ − |−2⟩)/√2. Combine them with the five spin projections M_S = −2,−1,0,1,2, giving a total of 15 basis states.

2. **Hamiltonian matrix.** The Hamiltonian that acts within the ⁵T₂g manifold is H = H_axial + λ L·S. The axial‑field term is diagonal in the orbital basis: it contributes +Δ/3 for the |±1⟩ orbitals and −2Δ/3 for the |xy⟩ orbital, independent of spin. The spin‑orbit operator λ L·S is evaluated in this basis using the standard angular‑momentum algebra for L = 2 (operators L_z, L₊, L₋) and S = 2. You can compute all matrix elements numerically. Because only the ratio v = Δ/λ appears in the final moments, you may set |λ| = 1 for the diagonalisation and treat λ as a negative constant (the sign is absorbed by the values of kT/λ used).

3. **Magnetic moment.** For each parameter set (k, v, kT/λ), diagonalise H to obtain the energies and eigenvectors. The effective magnetic moment is given by the operator μ_z = k L_z + 2 S_z. Compute μ_eff² as the Boltzmann average of μ_z² over the 15 states at the specified reduced temperature, then take the square root to obtain μ_eff in Bohr magnetons. Write the results to a CSV file.

## Reproduction target
Compute μ_eff for **every** combination of the following parameters:

- **k**: 1.0, 0.9, 0.8, 0.7
- **v**: 10, 5, 3, 2, 1, 0, −1, −2, −3, −5, −10
- **kT/λ**: 0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0 and the corresponding negative values (−0.1, −0.2, −0.3, −0.5, −0.75, −1.0, −1.5, −2.0, −3.0)

Produce a single CSV file `calculated_moments.csv` with columns:
- `k` (float)
- `v` (float)
- `kT_over_lambda` (float, positive or negative)
- `mu_eff` (float, in Bohr magnetons)

Row order may be arbitrary but must cover all 4 × 11 × 18 = 792 parameter sets exactly once.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute magnetic moments from perturbation matrix
- Role: scored (load-bearing)
- Action: Construct the 15×15 Hamiltonian matrix for the fifteen wavefunctions of the ^5T_{2g} term under a tetragonal axial potential plus spin-orbit coupling, using the Hamiltonian construction described in the Approach section above. For each parameter combination (k = 1.0,0.9,0.8,0.7; v = 10,5,3,2,1,0,-1,-2,-3,-5,-10; kT/λ = 0.1,0.2,0.3,0.5,0.75,1.0,1.5,2.0,3.0 and the corresponding negative values), diagonalize the matrix, obtain eigenvalues and eigenvectors, then compute the effective magnetic moment μ_eff using the operator (k L_z + 2 S_z) and Boltzmann averaging over the energy levels. Write the computed moments to a CSV file.
- Output file: `/app/outputs/calculated_moments.csv`
- Format: csv
- Contract: Columns: k (numeric, 1.0, 0.9, 0.8, 0.7), v (numeric, -10 to 10), kT_over_lambda (numeric, positive and negative values), mu_eff (numeric, magnetic moment in Bohr magnetons). Row order any consistent ordering.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calculated_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calculated_moments.csv
- path: `/app/outputs/calculated_moments.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed effective magnetic moments for all combinations of k, v, and kT/λ as listed in the parameter grid. The hidden checker compares each mu_eff to reference values with a tolerance; the tolerance is not disclosed in this public contract.
- schema:
  - `type`: table
  - `required_columns`: `k`, `v`, `kT_over_lambda`, `mu_eff`
  - `units`:
    - `mu_eff`: Bohr magneton

Notes: The scoring compares the agent’s mu_eff values to the paper‑reported reference values. The computed moments are deterministic, so an exact‑match policy with an appropriate tolerance is used. No internal implementation details or tolerances are exposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calculated_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "k",
          "v",
          "kT_over_lambda",
          "mu_eff"
        ],
        "units": {
          "mu_eff": "Bohr magneton"
        }
      },
      "description": "Computed effective magnetic moments for all combinations of k, v, and kT/λ as listed in the parameter grid. The hidden checker compares each mu_eff to reference values with a tolerance; the tolerance is not disclosed in this public contract."
    }
  ],
  "notes": "The scoring compares the agent’s mu_eff values to the paper‑reported reference values. The computed moments are deterministic, so an exact‑match policy with an appropriate tolerance is used. No internal implementation details or tolerances are exposed."
}
```

## How you are scored
A hidden verifier reads your `calculated_moments.csv`. It compares each μ_eff value against a set of reference values obtained from a correct solution of the Hamiltonian. The score is the fraction of parameter combinations for which your computed moment falls within an acceptable tolerance. You do not need to reproduce any particular published table; simply implement the physics faithfully and your results will naturally be close to the reference. The verifier does not reveal the tolerance or the reference values.
