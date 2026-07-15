# Bimetallic Cluster Surface Segregation via Free-Energy Minimization

## Problem background
The surface composition of bimetallic nanocatalysts often differs markedly from their bulk composition. Atoms of different elements can preferentially occupy surface, edge, and corner sites depending on their relative surface energies and atomic sizes. Understanding and predicting this segregation is critical for catalysis, but full atomistic simulations are computationally expensive. A simpler statistical-mechanical model that uses site-specific energies and ideal mixing entropy can provide rapid predictions of segregation, and this task reproduces the free-energy minimization procedure for 201-atom cubo-octahedral clusters of ten bimetallic combinations at 600 K and 50%-50% overall composition. The model defines five distinct site types—bulk (coordination 12), (111) planar (coordination 9), (100) planar (coordination 8), edge (coordination 7), and corner (coordination 6)—and the quantities to be computed are the percentage of non-bulk sites occupied by the element with higher surface energy (surface fraction) and the percentage of edge+corner sites occupied by that element (edge-corner fraction).

## Approach
The core of the method is a five-state free-energy minimization for a binary cluster. For each system the free energy F = E – T S is built, where the configurational entropy S uses the ideal mixing formula (Stirling approximation). The energy E depends on site occupancies and on site energies (interaction energies per atom) for the pure metals at each site type. Two energy models are used: one ignores atomic size mismatch (the effective energy level simply reflects the difference between site energies of the two species), and the other introduces an empirical size correction that scales each effective site-energy difference by a factor involving the lattice constants of the two elements and the local dimensionality of the site (0 for corner, 1 for edge, 2 for planar (111) and (100) sites). The average lattice constant required by the correction is a composition-weighted arithmetic mean of the two pure-metal lattice constants. For each bimetallic combination and each model, the free energy is minimized with respect to the site occupancies of one species (the bulk occupancy is fixed by the overall composition constraint), yielding the equilibrium distribution of atoms. The site counts are fixed: 79 bulk, 56 (111) planar, 6 (100) planar, 36 edge, and 24 corner sites. Numerical optimization is performed using standard minimizers from SciPy.

## Reproduction target
Produce a CSV file (`segregation_results.csv`) that reports, for each of the ten bimetallic systems (Rh-Ag, Rh-Cu, Pd-Ag, Ni-Ag, Cu-Ag, Rh-Pd, Ni-Cu, Rh-Ni, Ni-Pd, Pd-Cu) at 600 K and 50%-50% total concentration: (a) the percentage of all non-bulk sites occupied by the element with higher surface energy using the model without size effect (NoSize_SurfaceFrac) and (b) its edge-corner fraction (NoSize_EdgeCornerFrac); and the same two percentages using the model with empirical size correction (Size_SurfaceFrac, Size_EdgeCornerFrac). All fractions are expressed as percentages with two decimal places. The output file must have exactly five columns: System, NoSize_SurfaceFrac, NoSize_EdgeCornerFrac, Size_SurfaceFrac, Size_EdgeCornerFrac.

## Assets

- Bundled site energies (provided as `/app/assets/site_energies.csv`; see Step 1)
- SciPy
- NumPy

## Workflow steps

### Step 1: Load site energies and lattice constants
- Role: process
- Action: Copy the provided bundled file `/app/assets/site_energies.csv` to `/app/outputs/site_energies.csv`. This CSV contains the bulk, (111) planar, (100) planar, edge, and corner site energies (in eV) for each of the nine fcc metals (Al, Ni, Cu, Rh, Pd, Ag, Ir, Pt, Au) and their lattice constants (in Å), taken from MD/MC-CEM calculations on the 201-atom cubo-octahedral cluster (paper Table 2).
- Evidence: `/app/outputs/site_energies.csv`

### Step 2: Free-energy minimization for bimetallic systems
- Role: process
- Action: For each of the 10 bimetallic systems (Rh-Ag, Rh-Cu, Pd-Ag, Ni-Ag, Cu-Ag, Rh-Pd, Ni-Cu, Rh-Ni, Ni-Pd, Pd-Cu), build the five-state partition function for a 201-atom cubo-octahedral cluster (site counts: bulk=79, (111)=56, (100)=6, edge=36, corner=24). Compute the free energy F = E - TS at T=600 K using Stirling’s approximation for configurational entropy. For each system, minimize F with respect to site occupancies for two energy models: the model without size effect (original energy expression) and the model with the empirical size correction (scaling by lattice-constant ratios with exponents d_i = 0 for corner, 1 for edge, 2 for (111) and (100) planar sites). Use the lattice constants given in Step 1 to compute the composition-weighted average lattice constant. Record the final occupancies or iteration details.
- Evidence: `/app/outputs/free_energy_log.txt`

### Step 3: Compute and output segregation fractions
- Role: scored (load-bearing)
- Action: From the minimized occupancies of Step 2, calculate for each system and each model: (a) surface fraction – percentage of all non-bulk sites (edge, corner, (111), (100)) occupied by the element with higher surface energy; (b) edge-corner fraction – percentage of edge+corner sites occupied by that element. Write the results to segregation_results.csv with exactly five columns: System, NoSize_SurfaceFrac, NoSize_EdgeCornerFrac, Size_SurfaceFrac, Size_EdgeCornerFrac. All fractions are percentages to two decimal places.
- Output file: `/app/outputs/segregation_results.csv`
- Format: csv
- Contract: CSV with columns: System (str), NoSize_SurfaceFrac (float, %), NoSize_EdgeCornerFrac (float, %), Size_SurfaceFrac (float, %), Size_EdgeCornerFrac (float, %). All numeric values to two decimal places.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/site_energies.csv`
- `/app/outputs/free_energy_log.txt`
- `/app/outputs/segregation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### segregation_results.csv
- path: `/app/outputs/segregation_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Segregation percentages for 10 bimetallic systems. Each row corresponds to a system. Surface fraction is the percentage of all non-bulk sites occupied by the element with higher surface energy. Edge-corner fraction is the percentage of edge+corner sites occupied by that element. Values are computed using the model without size effect (NoSize) and with size effect (Size). All fractions are percentages to two decimal places.
- schema:
  - `type`: table
  - `required_columns`: `System`, `NoSize_SurfaceFrac`, `NoSize_EdgeCornerFrac`, `Size_SurfaceFrac`, `Size_EdgeCornerFrac`
  - `units`:
    - `NoSize_SurfaceFrac`: percentage
    - `NoSize_EdgeCornerFrac`: percentage
    - `Size_SurfaceFrac`: percentage
    - `Size_EdgeCornerFrac`: percentage

Notes: The hidden checker compares each fraction to the corresponding paper-reported value (Table 4) with a tolerance of ±1.0 percentage points. Reward is the fraction of correct comparisons.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "segregation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "System",
          "NoSize_SurfaceFrac",
          "NoSize_EdgeCornerFrac",
          "Size_SurfaceFrac",
          "Size_EdgeCornerFrac"
        ],
        "units": {
          "NoSize_SurfaceFrac": "percentage",
          "NoSize_EdgeCornerFrac": "percentage",
          "Size_SurfaceFrac": "percentage",
          "Size_EdgeCornerFrac": "percentage"
        }
      },
      "description": "Segregation percentages for 10 bimetallic systems. Each row corresponds to a system. Surface fraction is the percentage of all non-bulk sites occupied by the element with higher surface energy. Edge-corner fraction is the percentage of edge+corner sites occupied by that element. Values are computed using the model without size effect (NoSize) and with size effect (Size). All fractions are percentages to two decimal places."
    }
  ],
  "notes": "The hidden checker compares each fraction to the corresponding paper-reported value (Table 4) with a tolerance of ±1.0 percentage points. Reward is the fraction of correct comparisons."
}
```

## How you are scored
A hidden verifier reads your `segregation_results.csv` and compares each of the 40 computed fractions (10 systems × 4 fractions) to a set of undisclosed reference values. For each fraction, the verifier checks whether your value is correct within a hidden numerical tolerance. The overall reward is the fraction of correct comparisons. To obtain full credit you must implement the free-energy minimization faithfully; simply copying or guessing the numbers will not pass the hidden tolerance checks. The verifier does not award partial credit for approximations that produce large deviations.
