# 3D Packing Simulation of Bimodal Gypsum Powders via FCC Lattice and Drop-and-Roll Algorithm

## Problem background
Unfired gypsum composites gain strength from crystallization contacts between dihydrate particles. The number of contacts in a pressed powder compact depends strongly on the packing arrangement of the particles. For a bimodal mixture of large (coarse) and small (fine) particles, proper granulation can increase the number of contacts and thereby enhance the final strength. This work addresses the computational prediction of such packing quality: a three-dimensional model in which large particles are placed on a face-centered cubic (FCC) lattice to form a coarse skeleton, and small particles are then packed into the interstitial voids. The model computes two topological quantities — the average coordination number (number of contacting neighbors per particle) and the voidness (porosity, i.e., void volume relative to the unit cell volume) — as functions of the diameter ratio between the two particle sizes and the volume fraction occupied by the large particles. The goal is to compute these quantities over a range of conditions to understand how they influence packing and to identify granulometry regimes that maximize contacts.

## Approach
The core of the reproduction is a particle packing simulation based on the 'drop-and-roll' algorithm. The procedure is:
1) Construct a unit cell with a face-centered cubic lattice of large spherical particles. The size of the large particles is set from the desired large-particle volume fraction and the diameter ratio.
2) Small particles, whose diameter is determined from the ratio, are sequentially introduced above the cell, fall under gravity until they make first contact with a large particle or the cell boundary, and then roll along the contacting surfaces until they reach a mechanically stable position where they are simultaneously in contact with three surfaces (other large particles, small particles already placed, or the cell floor). This process fills the interstitial pores of the coarse skeleton.
3) After the unit cell is filled, the simulation computes the average coordination number for all particles (considering contacts where the center-to-center distance equals the sum of radii within a small tolerance) and the voidness (the fraction of the unit cell volume that is not occupied by particle material).
The simulation is run for multiple combinations of diameter ratio (d_large / d_small) and large-particle volume fraction, as specified in the workflow step.

## Reproduction target
Your submission must produce a CSV file with the computed coordination number and voidness for every prescribed (diameter_ratio, large_volume_fraction) pair. The exact list of parameter pairs is provided in the workflow step; it includes a range of diameter ratios and large-particle volume fractions that cover the conditions studied in the source work. The output file must contain exactly one row per condition, with the columns described in the output contract.

## Assets
- Python 3 (≥3.8) with standard numerical libraries such as NumPy. No external datasets, pre-trained models, or proprietary tools are required; the simulation is implemented from scratch in Python.

## Workflow steps

### Step 1: Parametric packing simulation and coordination/voidness computation
- Role: scored (load-bearing)
- Action: Implement the FCC coarse lattice and the drop-and-roll fine-particle placement algorithm. Run the simulation for the following diameter ratios (d_large/d_small): 2, 3, 4, 5, 7, 10 and large-particle volume fractions: 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7. For each of the 42 (diameter_ratio, large_volume_fraction) combinations, fill the unit cell, compute the average coordination number and the voidness (porosity). Write the results to packing_results.csv.
- Output file: `/app/outputs/packing_results.csv`
- Format: csv
- Contract: CSV with columns: diameter_ratio (float), large_volume_fraction (float), coordination_number (float), voidness (float). One row per requested condition.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/packing_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### packing_results.csv
- path: `/app/outputs/packing_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed coordination number and voidness for each input condition (diameter ratio, large-particle volume fraction).
- schema:
  - `type`: table
  - `required_columns`: `diameter_ratio`, `large_volume_fraction`, `coordination_number`, `voidness`
  - `units`:
    - `diameter_ratio`: dimensionless
    - `large_volume_fraction`: dimensionless
    - `coordination_number`: dimensionless
    - `voidness`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "packing_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "diameter_ratio",
          "large_volume_fraction",
          "coordination_number",
          "voidness"
        ],
        "units": {
          "diameter_ratio": "dimensionless",
          "large_volume_fraction": "dimensionless",
          "coordination_number": "dimensionless",
          "voidness": "dimensionless"
        }
      },
      "description": "Computed coordination number and voidness for each input condition (diameter ratio, large-particle volume fraction)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier has access to the expected values of coordination number and voidness for each of the requested input conditions. It will read your `packing_results.csv`, and for each row compare your computed `coordination_number` and `voidness` against the expected values within hidden tolerances. The reward is the fraction of rows where both quantities are within tolerance. If the file is missing, not a valid CSV, or does not contain all required rows, the reward is 0. You do not need to match any particular reported figure or table; you only need to run the simulation faithfully according to the described algorithm.
