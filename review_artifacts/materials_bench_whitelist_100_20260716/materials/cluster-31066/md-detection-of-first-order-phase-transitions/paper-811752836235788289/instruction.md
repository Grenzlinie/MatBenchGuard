# Dynamic Monte Carlo Yields of Patchy-Rectangle Crystals

## Problem background
Many proteins and nanoscale building blocks crystallize via pathways that can involve amorphous intermediates or direct formation of ordered nuclei. Understanding how the balance between orientationally specific interactions (which encode the target crystal structure) and nonspecific attractions (which can drive generic association) influences these dynamical pathways and yields is an open challenge. This work addresses that question by studying a model of patchy rectangular monomers in two dimensions. The monomers can form a square crystal lattice of tetramers through directional bonds, while a concentric nonspecific force field provides an isotropic attraction that does not by itself stabilize the crystal order. By varying the strengths of these two interactions, the model can exhibit distinct assembly routes, from classical nucleation to nonclassical liquid-like intermediates, and the resulting crystal yield may be affected in a nontrivial way. The target quantity is a scaled crystal yield that rewards large, compact crystals.

## Approach
We simulate a two-dimensional system of hard rectangles of short edge length a and aspect ratio 2.2. Each monomer carries three chemically selective patches (E, S, L) placed a/2 from the nearest vertices. Directional bonds form when L‑L or E‑S patches approach within a/5, each contributing an energy -ε_d kT. A nonspecific pairwise interaction is modelled by a concentric rectangular force field extending 2a/5 beyond the monomer sides; any overlap of these fields gives an energy -ε_n kT. The system is evolved using the virtual‑move Monte Carlo algorithm, which approximates overdamped diffusive dynamics by allowing collective translations and rotations. Simulations are run in the canonical (NVT) ensemble with N = 600 monomers at 10.91% area coverage, periodic boundary conditions, starting from randomly dispersed and oriented monomers. For each (ε_d, ε_n) pair considered, we record the fractions of monomers with exactly two (f_p) and exactly three (f_c) directional bonds after the yield has plateaued. The scaled crystal yield is computed as f_c_scaled = f_c * (f_c/(f_p+f_c))^2. By gathering data over a range of interaction strengths, one can map how the scaled yield changes with ε_n at fixed ε_d and determine the parameter regime that produces the highest yield.

## Reproduction target
Your task is to run dynamic virtual‑move Monte Carlo simulations for the following combinations of specific interaction strength ε_d and nonspecific interaction strength ε_n:

- ε_d ∈ {4, 6, 8, 10}
- For each ε_d, use ε_n ∈ {0, 1, 2, 3, 4, 5}

For every (ε_d, ε_n) pair, perform at least 5 independent simulations (distinct random seeds), each starting from a random dispersion of monomers. After the crystal yield has reached a steady plateau, record f_p and f_c per seed and compute f_c_scaled. Write the results to `/app/outputs/yield_data.csv` with one row per seed. The file must contain the columns epsilon_d, epsilon_n, seed, f_p, f_c, f_c_scaled. The process step (Step 1) requires you to implement the model and algorithm; this scored step produces the CSV that will be evaluated by the hidden verifier.

## Assets

- Python (>=3.8): https://python.org
- Virtual-move Monte Carlo algorithm (Whitelam & Geissler, J. Chem. Phys. 2007): https://doi.org/10.1063/1.2770276

## Workflow steps

### Step 1: Implement the patchy-rectangle model and virtual-move Monte Carlo simulator
- Role: process
- Action: Write code implementing the 2D model: hard rectangles of short edge a and aspect ratio 2.2; three patches E, S, L at a/2 from vertices; directional bonds when L-L or E-S patches closer than a/5, energy -epsilon_d*kT; nonspecific attraction via concentric rectangular force field extending 2a/5 beyond monomer sides, energy -epsilon_n*kT when overlapping. Implement the virtual-move Monte Carlo algorithm for canonical (NVT) dynamics as described in the reference, supporting N=600 monomers at 10.91% area coverage and periodic boundary conditions.
- Evidence: `/app/outputs/simulation_code.py`

### Step 2: Run dynamic simulations and compute scaled yields
- Role: scored (load-bearing)
- Action: For each (epsilon_d, epsilon_n) combination specified in the instruction, run the dynamic Monte Carlo simulation starting from randomly dispersed monomers, using at least 5 independent seeds. After reaching a yield plateau, record the fraction of monomers with exactly two directional bonds (f_p) and exactly three directional bonds (f_c). Compute f_c_scaled = f_c * (f_c/(f_p+f_c))^2. Write a CSV with one row per seed.
- Output file: `/app/outputs/yield_data.csv`
- Format: csv
- Contract: Columns: epsilon_d (float), epsilon_n (float), seed (int), f_p (float), f_c (float), f_c_scaled (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/yield_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### yield_data.csv
- path: `/app/outputs/yield_data.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file with one row per independent simulation seed, containing the interaction parameters and the measured fractions of monomers in partially crystalline and crystalline states, along with the computed scaled crystal yield. The checker will compute the per-condition mean scaled yield and compare it to the paper’s reference value using a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `epsilon_d`, `epsilon_n`, `seed`, `f_p`, `f_c`, `f_c_scaled`

Notes: The agent is expected to run dynamic simulations for the specified list of (epsilon_n, epsilon_d) pairs and per-seed counts. The equilibrium phase diagram is not required for scoring; only the dynamic yield data is scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "yield_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "epsilon_d",
          "epsilon_n",
          "seed",
          "f_p",
          "f_c",
          "f_c_scaled"
        ]
      },
      "description": "CSV file with one row per independent simulation seed, containing the interaction parameters and the measured fractions of monomers in partially crystalline and crystalline states, along with the computed scaled crystal yield. The checker will compute the per-condition mean scaled yield and compare it to the paper’s reference value using a relative tolerance."
    }
  ],
  "notes": "The agent is expected to run dynamic simulations for the specified list of (epsilon_n, epsilon_d) pairs and per-seed counts. The equilibrium phase diagram is not required for scoring; only the dynamic yield data is scored."
}
```

## How you are scored
A hidden verifier will read your `yield_data.csv`. It groups the rows by (ε_d, ε_n) and, for each group, computes the mean f_c_scaled. Each mean is then compared to a hidden reference value that corresponds to the paper's reported scaled yield for the same condition. The comparison uses a predefined relative tolerance (not disclosed). Your score is the fraction of (ε_d, ε_n) conditions for which your mean lies within tolerance of the reference. The closer your simulated yields are to the expected values across the parameter grid, the higher your final reward. No other outputs are scored.
