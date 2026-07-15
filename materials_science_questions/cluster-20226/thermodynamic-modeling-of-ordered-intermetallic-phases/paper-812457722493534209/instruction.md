# Five-State Model Surface Segregation in Bimetallic Clusters

## Problem background
Bimetallic nanoparticles are widely used as catalysts, and their catalytic activity depends strongly on the composition of the outermost atomic layers. Because the surface and edge-corner sites of a nanoparticle can be enriched in one component relative to the bulk, predicting this segregation is essential for understanding and designing better catalysts. A five‑state statistical‑mechanical model, combined with atomistic site energies, provides a computationally inexpensive way to predict surface segregation in binary clusters with a well‑defined cubo‑octahedral shape. This task asks you to implement that model and compute the predicted surface and edge‑corner segregation fractions for three binary systems, both with and without an empirical correction for atomic size mismatch. The resulting fractions remain an open quantity for you to determine by direct free‑energy minimization.

## Approach
The model treats a binary cluster (elements A and B) with five distinct site types: corner (6‑fold coordinated), edge (7‑fold), (100) planar surface (8‑fold), (111) planar surface (9‑fold), and bulk (12‑fold). For a 201‑atom truncated cubo‑octahedron the numbers of each site type are fixed by geometry. The free energy is written as the sum of the site‑occupancy‑weighted site energies minus the configurational entropy (ideal mixing). The heat of mixing is assumed to be zero, so the only interactions between unlike atoms enter through the site energies themselves. The free energy depends on the numbers of A atoms in the first four site types (the bulk occupancy follows from the fixed total composition). The equilibrium occupancies are found by minimizing the free energy with respect to these independent variables.

Two variants of the energy formula are used. In the “without size” model, the effective site energy difference that drives segregation is simply the difference between the two pure‑metal site energy sets. In the “with size” model, an empirical size‑mismatch correction is applied. The correction assigns a scaling exponent dᵢ to each site type: 0 for corner, 1 for edge, and 2 for planar surface sites. Each pure‑metal site energy difference is divided by (a₀)ᵈⁱ of that metal, where a₀ is the fcc lattice constant, and the whole bracketed expression is multiplied by a composition‑weighted average lattice constant raised to the same exponent. The average lattice constant is the arithmetic average weighted by the total number of A and B atoms in the cluster. This correction increases the driving force for segregation when the larger atom also has the lower surface energy, and opposes it when the larger atom has the higher surface energy.

The site energies for the four metals (Ni, Cu, Rh, Pd) in a 201‑atom cluster are taken from the provided resource (MD/MC‑CEM relaxed‑cluster energies). The lattice constants needed for the size correction are also provided. You will perform the free‑energy minimization for three 50‑50 systems at 600 K: Rh‑Ni, Ni‑Pd, Pd‑Cu, each with and without the size correction, and report the resulting surface and edge‑corner fractions.

## Reproduction target
Your goal is to compute, for each of the three binary systems (Rh‑Ni, Ni‑Pd, Pd‑Cu) at a 50‑50 composition and 600 K, the surface fraction and the edge‑corner fraction of the higher‑surface‑energy element. For every system you must perform two calculations: one using the free energy model without the size correction, and one using the model with the size correction. The surface fraction is the percentage of all non‑bulk sites (corner, edge, (100), (111)) occupied by the element with the higher surface energy. The edge‑corner fraction is the percentage of corner plus edge sites occupied by that same element. Write the six resulting pairs of values to the CSV file `step_02_segregation_results.csv` as described in the output contract. Ensure that your implementation correctly minimizes the free energy to obtain the equilibrium site occupancies; the reported fractions must be derived from those occupancies.

## Assets

- MD/MC-CEM site energies for 201-atom clusters of Ni, Cu, Rh, Pd
- Pure-metal fcc lattice constants for Ni, Cu, Rh, Pd

## Workflow steps

### Step 1: Compute surface segregation fractions
- Role: scored (load-bearing)
- Action: Implement the five-state free energy model (ideal mixing entropy, zero heat of mixing) for a 201-atom truncated cubo-octahedral binary cluster. Use the provided site energies and lattice constants, the geometric site counts for the cluster (obtain from standard cubo-octahedron geometry), and the empirical size-correction formula (dimensional scaling with exponents d_i = 0, 1, 2 for corner, edge, planar surface sites and composition-weighted average lattice constant). Minimize the free energy for 50-50 composition at 600 K to find equilibrium site occupancies. For each of the three binary systems (Rh-Ni, Ni-Pd, Pd-Cu) and for both model types (without size effect and with size effect), compute the surface fraction (percentage of non-bulk sites occupied by the higher-surface-energy element) and edge-corner fraction (corner + edge sites). Write results to the output CSV.
- Output file: `/app/outputs/step_02_segregation_results.csv`
- Format: csv
- Contract: CSV with columns: system (string: 'Rh-Ni', 'Ni-Pd', 'Pd-Cu'), model_type (string: 'without_size' or 'with_size'), surface_fraction (float, percentage 0-100), edge_corner_fraction (float, percentage 0-100). Exactly 6 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_segregation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_segregation_results.csv
- path: `/app/outputs/step_02_segregation_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Segregation fractions (surface and edge-corner) predicted by the free energy model for the three binary systems, both with and without size correction. The checker compares each value to the paper's reference within tolerances and verifies ordering.
- schema:
  - `type`: table
  - `required_columns`: `system`, `model_type`, `surface_fraction`, `edge_corner_fraction`
  - `units`:
    - `surface_fraction`: percentage
    - `edge_corner_fraction`: percentage

Notes: The segregation results file must contain exactly 6 rows (3 systems × 2 model types). All values are floating-point numbers in the appropriate units.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_segregation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "model_type",
          "surface_fraction",
          "edge_corner_fraction"
        ],
        "units": {
          "surface_fraction": "percentage",
          "edge_corner_fraction": "percentage"
        }
      },
      "description": "Segregation fractions (surface and edge-corner) predicted by the free energy model for the three binary systems, both with and without size correction. The checker compares each value to the paper's reference within tolerances and verifies ordering."
    }
  ],
  "notes": "The segregation results file must contain exactly 6 rows (3 systems × 2 model types). All values are floating-point numbers in the appropriate units."
}
```

## How you are scored
A hidden verifier will read your submitted CSV file and independently check each reported value. The verifier compares your surface_fraction and edge_corner_fraction for every system‑model_type combination to the paper’s reference results, using appropriate numerical tolerances that account for legitimate implementation differences. In addition, the verifier will verify that the relative ordering of surface fractions among the three systems, and the change in each system when the size correction is turned on, follow the expected physical trends. Your score is a weighted combination of these checks; merely reporting plausible numbers without a correct underlying minimization will not pass. The verifier does not disclose its reference values or tolerances.
