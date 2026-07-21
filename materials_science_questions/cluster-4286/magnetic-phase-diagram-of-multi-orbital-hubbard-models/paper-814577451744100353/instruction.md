# AIAO staggered magnetization and charge gap from Hartree-Fock mean-field theory on a pyrochlore Kondo lattice model

## Problem background
Pyrochlore iridates such as Nd2Ir2O7 exhibit a metal–insulator transition driven by strong electron correlations and spin–orbit coupling. A prominent theoretical proposal is that an all‑in–all‑out (AIAO) magnetic order on the iridium sublattice is stabilised by Kondo coupling between itinerant Ir electrons and localised Nd moments, and that this coupling simultaneously influences the charge gap. Self‑consistent unrestricted Hartree–Fock mean‑field calculations on an effective Kondo lattice model can predict how the AIAO staggered magnetisation and the charge gap vary with the Hubbard U and the Kondo coupling J_K. This task asks you to recompute these quantities: for several values of U and J_K, determine the AIAO staggered magnetisation φ and the charge gap Δ as a function of the Kondo coupling, providing a direct numerical test of the mean‑field picture.

## Approach
The model consists of itinerant Ir electrons on the pyrochlore lattice subject to an on‑site Hubbard repulsion U, coupled via an exchange term of strength J_K to localised Nd spin‑1/2 moments that are treated as classical vectors. The calculation assumes q=0 magnetic order (the AIAO pattern) and uses a 32×32×32 superlattice to avoid finite‑size artifacts. The approach is to implement an unrestricted Hartree–Fock (UHF) self‑consistent loop: starting from an initial guess for the mean fields, the effective single‑particle Hamiltonian is diagonalised, the Fermi‑level occupation is determined, and the mean fields are updated. When convergence is reached, the AIAO staggered magnetisation is extracted as the appropriate Fourier component of the local spin density, and the charge gap is read off from the difference between the top of the valence band and the bottom of the conduction band. The computation is repeated for each desired set of (U, J_K) parameters.

## Reproduction target
Produce a CSV file `/app/outputs/hf_results.csv` containing the computed AIAO staggered magnetisation φ and charge gap Δ for each combination of the following parameters:
• Hubbard U ∈ {0.4, 0.5, 0.6, 0.7} (in units of the oxygen‑mediated hopping t_oxy)
• Kondo coupling J_K ∈ {0, 0.02, 0.04, 0.06, 0.08, 0.10} (same units)

Both φ and Δ are dimensionless numbers expressed in units of t_oxy. The exact set of J_K values given above is sufficient; use these points directly. Your output will be compared by a hidden verifier against independently determined reference results.

## Assets

- Python scientific computing stack: numpy scipy

## Workflow steps

### Step 1: Hartree-Fock mean-field calculation of AIAO order and charge gap
- Role: scored (load-bearing)
- Action: Implement a self-consistent unrestricted Hartree-Fock mean-field solver for the Kondo lattice model on the pyrochlore lattice, assuming q=0 magnetic order and using a 32x32x32 superlattice. For each combination of Hubbard U in {0.4, 0.5, 0.6, 0.7} (in units of the oxygen-mediated hopping t_oxy) and for a set of Kondo couplings J_K spanning the range where the AIAO order is sensitive (e.g., from 0 to a value where the gap saturates), compute the AIAO staggered magnetization phi and the charge gap Delta. Write the results to /app/outputs/hf_results.csv.
- Output file: `/app/outputs/hf_results.csv`
- Format: csv
- Contract: Header: U, J_K, phi, Delta. Each row gives one (U, J_K) combination with the computed phi and Delta (numeric, in units of the oxygen-mediated hopping t_oxy).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hf_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hf_results.csv
- path: `/app/outputs/hf_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV of computed AIAO staggered magnetization and charge gap for each (U,J_K) point, validated against hidden reference values and monotonic trends.
- schema:
  - `type`: table
  - `required_columns`: `U`, `J_K`, `phi`, `Delta`
  - `units`:
    - `U`: dimensionless (units of t_oxy)
    - `J_K`: dimensionless (units of t_oxy)
    - `phi`: dimensionless (staggered magnetization)
    - `Delta`: dimensionless (units of t_oxy)

Notes: The checker will compare the submitted phi and Delta against digitized gold data from the paper's Fig. 4 with appropriate tolerances and verify that, for each fixed U, both quantities increase monotonically with J_K.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hf_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "J_K",
          "phi",
          "Delta"
        ],
        "units": {
          "U": "dimensionless (units of t_oxy)",
          "J_K": "dimensionless (units of t_oxy)",
          "phi": "dimensionless (staggered magnetization)",
          "Delta": "dimensionless (units of t_oxy)"
        }
      },
      "description": "CSV of computed AIAO staggered magnetization and charge gap for each (U,J_K) point, validated against hidden reference values and monotonic trends."
    }
  ],
  "notes": "The checker will compare the submitted phi and Delta against digitized gold data from the paper's Fig. 4 with appropriate tolerances and verify that, for each fixed U, both quantities increase monotonically with J_K."
}
```

## How you are scored
A hidden autograder will inspect your `hf_results.csv`. For each (U, J_K) pair it will compare your computed φ and Δ to reference values obtained from the literature, with allowances for legitimate implementation‑dependent spread. It will also verify that for each fixed U, both φ and Δ exhibit the physically expected behaviour as J_K is varied (structural trend check). The final score is a weighted combination of point‑wise accuracy and trend consistency. Merely reporting the literature numbers without performing the self‑consistent calculation will not pass the trend checks and may violate point‑wise tolerances.
