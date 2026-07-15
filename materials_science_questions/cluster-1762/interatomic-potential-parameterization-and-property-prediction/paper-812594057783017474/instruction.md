# Generalized Morse Potential for Nanoparticle Cohesive Energy and Melting Point

## Problem background
Cohesive energy is the energy required to dissociate a solid into neutral atoms and is a key quantity for understanding thermodynamic stability. For nanoparticles, cohesive energy depends on particle size. Potential energy functions that describe pairwise interatomic interactions can be used to compute size-dependent cohesive energies. A generalized Morse potential with an extra integer parameter m includes additional interaction terms beyond the ordinary Morse potential, allowing the potential to be tuned to better reproduce experimental nanoparticle energetics. This task asks you to implement such a generalized Morse potential and use it to compute relative cohesive energies and melting point ratios for face-centered cubic metallic nanoparticles.

## Method
We use a generalized Morse potential between atom pairs:
U(r_ij) = (D/m) Σ_{k=1}^{2m} (-1)^k (2m - (k-1)) exp[-α k (r_ij/r_0 - 1)]

where r_0 is the equilibrium nearest-neighbor distance in the bulk, α is a dimensionless parameter, m a positive integer, and D an energy scale (set D=1 for convenience). The reduced nearest-neighbor distance is r* = r/r_0.

For a nanoparticle of n atoms in an FCC lattice, the total energy (in units of D) is
E_n(r*) = (n/(2m)) Σ_{k=1}^{2m} (-1)^k (2m - (k-1)) A_k(r*)

where A_k(r*) = (1/n) Σ_i Σ_{j≠i} exp[-α k (a_{ij} r* - 1)],
a_{ij} = r_ij / r, and r is the current nearest-neighbor distance. The equilibrium r_0* is obtained by minimizing E_n(r*) with respect to r*.

The per-atom cohesive energy relative to the bulk is
E_a/E_0 = P_0/(2m) Σ_{k=1}^{2m} (-1)^k (2m - (k-1)) A_k(r_0*)
with P_0 = 2m / Σ_{k=1}^{2m} (-1)^k (2m - (k-1)) A'_k(r_0*).

Here A'_k(r_0*) are the bulk interaction terms, i.e., the same A_k computed for an infinite FCC crystal (simulated by summing over neighbour shells up to convergence) at the bulk equilibrium r_0* that minimizes the bulk energy E_bulk(r*) = (1/(2m)) Σ_{k=1}^{2m} (-1)^k (2m - (k-1)) A'_k(r*). For the bulk, r_0* depends on α, and we precompute A'_k as a function of α.

The melting point ratio is taken as T_m/T_mbulk = E_a/E_0.


## Reproduction target
Produce two CSV files:

- relative_cohesive_energies.csv: For FCC nanoparticles of n=2000 and n=7000 atoms, compute the relative cohesive energy E_a/E_0 for each combination of m ∈ {2,3,4,5} and α ∈ {2.0, 2.4}. Each row corresponds to one (n, m, α) combination, and the file must have columns n, m, alpha, Ea_E0.
- melting_point_ratios.csv: For Au nanoparticles in FCC structure, compute the melting point ratio T_m/T_mbulk as a function of the number of atoms n for the following parameter sets: m=2 with α ∈ {2.6, 2.8, 3.0} and m=3 with α ∈ {2.3, 2.5, 2.8}. Convert nanoparticle diameter D (ranging from 1 to 20 nm) to n using the formula n = 0.74 (D/d)^3 + 1.82 (D/d)^2, where d = (√2/2)·a and a = 4.0782 Å (the Au lattice constant). The CSV must have columns m, alpha, n, Tm_Tmbulk, with one row per (m, α, n) combination.

You are to implement the energy minimization and compute these values from scratch, not from precomputed tables.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute bulk FCC interaction terms and equilibrium
- Role: process
- Action: For each required integer parameter m in {2,3,4,5}, for a face-centered cubic lattice, numerically determine the equilibrium reduced nearest-neighbor distance r0* that minimizes the bulk total energy over a range of α values at least from 1 to 5. Compute the bulk interaction term functions A'_k(r0*) as a function of α for each m, and store these curves for later use in P0 calculation.
- Evidence: `/app/outputs/bulk_terms.json`

### Step 2: Compute relative cohesive energies for nanoparticles
- Role: scored (load-bearing)
- Action: Construct an FCC nanoparticle of n atoms (use a spherical cut off from an ideal FCC lattice). For each (n,m,α), compute E_n(r*) via the formula in Method, minimize over r* (e.g., using a SciPy minimizer) to obtain r0*. Then compute the relative cohesive energy E_a/E_0 = P_0/(2m) Σ_{k=1}^{2m} (-1)^k (2m-(k-1)) A_k(r0*), where P_0 = 2m / Σ_{k=1}^{2m} (-1)^k (2m-(k-1)) A'_k(r0*) and A'_k(r0*) is obtained by interpolation from the bulk curves precomputed in step 1 for the same α. Output a CSV with columns n, m, alpha, Ea_E0.
- Output file: `/app/outputs/relative_cohesive_energies.csv`
- Format: csv
- Contract: Columns: n (integer), m (integer), alpha (float), Ea_E0 (float). One row per (n,m,alpha) combination.
- Scoring: scored by hidden verifier

### Step 3: Compute melting point ratios for Au nanoparticles
- Role: scored
- Action: For each (m,α) set: (2,2.6), (2,2.8), (2,3.0), (3,2.3), (3,2.5), (3,2.8), do the following: For Au FCC, atomic diameter d = (√2/2)·4.0782 Å. For a range of nanoparticle diameters D from 1 to 20 nm (step 0.5 nm or finer), compute n = int(round(0.74 (D/d)^3 + 1.82 (D/d)^2)). For each n, construct an FCC nanoparticle, minimize total energy over r* to find r0*, and evaluate T_m/T_mbulk = E_a/E_0 using the same formula as in Step 2 (with the corresponding P_0 from bulk A'_k). Output a CSV with columns m, alpha, n, Tm_Tmbulk.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_cohesive_energies.csv
- path: `/app/outputs/relative_cohesive_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed relative cohesive energies for FCC nanoparticles at n=2000 and 7000, for m=2,3,4,5 and α=2.0,2.4.
- schema:
  - `type`: table
  - `required_columns`: `n`, `m`, `alpha`, `Ea_E0`
  - `units`:
    - `Ea_E0`: dimensionless

### melting_point_ratios.csv
- path: `/app/outputs/melting_point_ratios.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed melting point ratios T_m/T_mbulk for Au nanoparticles. Checked for monotonicity, ordering, and range (structural audit).
- schema:
  - `type`: table
  - `required_columns`: `m`, `alpha`, `n`, `Tm_Tmbulk`
  - `units`:
    - `Tm_Tmbulk`: dimensionless

Notes: The checker will compare the agent's computed values to paper-reported gold values within a tolerance for relative_cohesive_energies.csv (exact_match policy). For melting_point_ratios.csv, the checker performs a structural audit (monotonicity, ordering, range) without requiring exact numeric matching.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_cohesive_energies.csv`
- `/app/outputs/melting_point_ratios.csv`

## Output contract
See the machine-readable output contract rendered by the builder.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_cohesive_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "m",
          "alpha",
          "Ea_E0"
        ],
        "units": {
          "Ea_E0": "dimensionless"
        }
      },
      "description": "Computed relative cohesive energies for FCC nanoparticles at n=2000 and 7000, for m=2,3,4,5 and α=2.0,2.4."
    },
    {
      "file": "melting_point_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "alpha",
          "n",
          "Tm_Tmbulk"
        ],
        "units": {
          "Tm_Tmbulk": "dimensionless"
        }
      },
      "description": "Computed melting point ratios T_m/T_mbulk for Au nanoparticles. Checked for monotonicity, ordering, and range (structural audit)."
    }
  ],
  "notes": "The checker will compare the agent's computed values to paper-reported gold values within a tolerance for relative_cohesive_energies.csv (exact_match policy). For melting_point_ratios.csv, the checker performs a structural audit (monotonicity, ordering, range) without requiring exact numeric matching."
}
```

## How you are scored
A hidden verifier will evaluate both output CSV files. It will compare the numeric values you compute against reference values obtained from a correct implementation of the generalized Morse potential. The verifier uses an appropriate tolerance to account for minor numerical differences, and your score is based on how many rows meet the accuracy requirements across all required combinations. The two files are weighted according to their importance. Simply reporting an accurate-looking number without performing the full numerical minimization and lattice summation will not pass, because the verifier checks multiple data points with consistent physics. You must produce complete files with the specified schema.
