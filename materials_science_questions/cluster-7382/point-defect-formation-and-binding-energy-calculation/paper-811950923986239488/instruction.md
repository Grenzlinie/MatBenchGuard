# Valence-Force-Field Study of Cluster Stability in Dilute Ge(C,Sn) Alloys

## Problem background
Doping germanium (Ge) with small carbon (C) and large tin (Sn) impurities creates substantial compressive and tensile strain, respectively, owing to the large lattice-constant mismatch with the host. This strain energy makes it thermodynamically favorable for the impurities to self-assemble into clusters that partially cancel their opposing deformations. Previous theoretical work has considered the formation of small 1C4Sn (filled tetrahedral) clusters, which lower the strain energy compared to a random alloy. An open question is whether larger 4C10Sn clusters, built around empty tetrahedral cells, can be even more favorable because they largely deform bond angles instead of bond lengths and thereby achieve a greater net reduction in Helmholtz free energy. In this task, you will determine, for Ge-rich C_x Sn_y Ge_{1-x-y} alloys at 773 K, the concentration region where the alloy with 4C10Sn clusters has a lower Helmholtz free energy than the alloy with 1C4Sn clusters.

## Approach
The Helmholtz free energy of each alloy configuration (random, 1C4Sn clusters, 4C10Sn clusters) is modelled as the sum of a strain energy term computed within the valence-force-field (VFF) model and a configurational entropy term. The VFF model uses bond-stretching and bond-bending elastic constants from Keating (1966) and Martins & Zunger (1984) to compute the strain energies of isolated C and Sn substitutional impurities, as well as the cluster motifs 1C4Sn and 4C10Sn. For compositions that satisfy x ≥ 0.4y (a necessary condition for the clusters to incorporate a majority of C atoms), the per-atom strain energies are expressed as weighted combinations of these motif energies. Together with the appropriate configurational entropy expressions for each configuration, this gives the Helmholtz free energy per host atom as a function of the C fraction x and the Sn fraction y. The comparison is carried out on a grid of (x,y) points within x ∈ [0,0.02], y ∈ [0,0.05] and x ≥ 0.4y, at a temperature of 773 K. For each grid point, you will evaluate the free energy for the three configurations and identify the one with the lowest value.

### Configurational entropy expressions
The configurational entropy per host atom (in units of the gas constant R) is given by:

- Random alloy:
  S_random = R [x ln x + y ln y + (1 - x - y) ln(1 - x - y)]

- Alloy with all Sn atoms in 1C4Sn clusters (valid when x ≥ 0.4y):
  S_1C4Sn = R [ (x - 0.25 y) ln((x - 0.25 y)/(1 - 1.25 y))
                + (1 - x - y) ln((1 - x - y)/(1 - 1.25 y))
                + 0.25 y ln(0.5 y) + (0.5 - 0.25 y) ln(1 - 0.5 y) ]

- Alloy with all Sn atoms in 4C10Sn clusters (valid when x ≥ 0.4y):
  S_4C10Sn = R [ (1 - x - y) ln((1 - x - y)/(1 - 1.4 y))
                + (x - 0.4 y) ln((x - 0.4 y)/(1 - 1.4 y))
                + 0.1 y ln(2.7 y) + (0.037 - 0.1 y) ln(1 - 2.7 y) ]
  (The constant 0.037 approximates 1/27, because each 4C10Sn cluster occupies 27 tetrahedral cells.)

The Helmholtz free energy per host atom for a given configuration is then
F = U_strain(x,y) - T S(x,y), where U_strain is the strain energy contribution
from step_01 and the entropy terms are taken from the appropriate expression above.

## Reproduction target
Produce a CSV file (`free_energy_data.csv`) containing the free energy data and the identified lowest-energy configuration for at least 50 (x,y) points on the indicated grid. The CSV must have columns: x (float), y (float), f_random (float, eV per host atom), f_1C4Sn (float, eV per host atom), f_4C10Sn (float, eV per host atom), min_config (string, one of 'random', '1C4Sn', '4C10Sn').

## Assets

- Keating 1966: bond-stretching and bond-bending elastic constants: 10.1103/PhysRev.145.637
- Martins & Zunger 1984: elastic constants and lattice parameters: 10.1103/PhysRevB.30.6217
- NumPy: numpy

## Workflow steps

### Step 1: Compute per-motif strain energies
- Role: process
- Action: Implement the valence-force-field (VFF) model using published bond-stretching and bond-bending elastic constants to compute the strain energy of an isolated substitutional C atom, an isolated substitutional Sn atom, a 1C4Sn (filled tetrahedral) cluster, and a 4C10Sn (empty-cell) cluster in a germanium diamond lattice. Write the resulting energies (u_1C, u_1Sn, u_1C4Sn, u_4C10Sn, in eV) to an evidence JSON file.
- Evidence: `/app/outputs/strain_energies.json`

### Step 2: Free energy comparison and stability region
- Role: scored (load-bearing)
- Action: Using the strain energies from step_01 and the configurational entropy formulas for the random alloy, the 1C4Sn-cluster alloy, and the 4C10Sn-cluster alloy, compute the Helmholtz free energy per host atom at T=773 K for each configuration on a grid of (x,y) with x ∈ [0, 0.02], y ∈ [0, 0.05] satisfying x ≥ 0.4y. For each grid point, determine which configuration has the minimum free energy. Output a CSV file with columns x, y, f_random, f_1C4Sn, f_4C10Sn, min_config.
- Output file: `/app/outputs/free_energy_data.csv`
- Format: csv
- Contract: CSV columns: x (float, atomic fraction C), y (float, atomic fraction Sn), f_random (float, eV per atom), f_1C4Sn (float, eV per atom), f_4C10Sn (float, eV per atom), min_config (string, one of 'random','1C4Sn','4C10Sn')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energy_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energy_data.csv
- path: `/app/outputs/free_energy_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing free energy data per composition and the minimum-energy cluster configuration.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `f_random`, `f_1C4Sn`, `f_4C10Sn`, `min_config`
  - `columns`:
    - `x`: float
    - `y`: float
    - `f_random`: float
    - `f_1C4Sn`: float
    - `f_4C10Sn`: float
    - `min_config`: string

Notes: The checker compares the min_config column against a digitized reference stability boundary and scores the classification accuracy.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energy_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "f_random",
          "f_1C4Sn",
          "f_4C10Sn",
          "min_config"
        ],
        "columns": {
          "x": "float",
          "y": "float",
          "f_random": "float",
          "f_1C4Sn": "float",
          "f_4C10Sn": "float",
          "min_config": "string"
        }
      },
      "description": "CSV file containing free energy data per composition and the minimum-energy cluster configuration."
    }
  ],
  "notes": "The checker compares the min_config column against a digitized reference stability boundary and scores the classification accuracy."
}
```

## How you are scored
A hidden verifier will read your `free_energy_data.csv` and compare the `min_config` column for each evaluated point against a reference stability boundary derived from the original findings. Points that match the expected configuration are counted as correct. Points within a narrow neighbourhood of the boundary are scored leniently to account for numerical differences. The final reward is the fraction of valid grid points that are correctly classified.
