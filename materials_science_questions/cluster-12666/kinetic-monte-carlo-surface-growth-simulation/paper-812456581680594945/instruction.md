# Thermodynamic Monte Carlo Modeling of Microporous Material Formation

## Problem background
This task simulates the formation of microporous clusters on a lattice, combining Monte Carlo moves with a thermodynamic bias that favors configurations of lower free energy (as determined by surface energy and configurational entropy). A regular lattice of initially occupied cells is progressively emptied, and the probability of emptying a given cell depends on the local free-energy change of the porous cluster. The goal is to compute percolation thresholds, tortuosity curves, and structural parameters (internal surface area and free energy) for both 2D square and 3D cubic lattices, and to compare the results produced by a purely random vacancy process with those obtained under thermodynamically limited conditions. No external dataset is needed; the simulation is driven entirely by the defined physical parameters.

## Approach
Implement a Monte Carlo pore formation algorithm on a lattice. In the thermodynamic mode, each step empties an occupied cell with probability proportional to exp(-ΔG/(R_g T)), where ΔG is the change in total free energy if that cell were emptied, and R_g = 8.314 J/(mol·K). The total free energy G_Σ of a configuration with N0 total cells and Np empty cells is:

G_Σ = σ A_p + R_g T (N0 - Np) Σ_{m=0}^{n} [ ξ*(m) ln ξ*(m) - ξ(m) ln ξ(m) ]

where σ = 70 J/m² (surface tension), T = 300 K, n is the lattice coordination (4 for 2D square, 6 for 3D cube). A_p = Σ_{m=0}^{n} m N_f(m) is the internal surface area (number of empty–occupied neighbour contacts). N_f(m) is the number of occupied cells having exactly m empty neighbours. ξ*(m) = N_f(m) / (N0 - Np) is the actual distribution. ξ(m) is the maximum-entropy Poisson-like reference distribution:

ξ(m) = p_p^m (1 - p_p^{n-m}) (1 - p_p) / (1 - p_p^{n+1})    with p_p = Np / N0.

To evaluate ΔG when a candidate occupied cell with m0 empty neighbours is emptied:
- Mark the cell as empty; increase Np by 1.
- Update N_f(m) counts: for each occupied neighbour of the cell, its number of empty neighbours increases by 1; adjust the histogram.
- Recompute A_p and ξ*(m) for the new configuration using the formulas above.
- ΔG = G_Σ(new) − G_Σ(old).

The probability that a particular occupied cell is selected is exp(-ΔG/(R_g T)) / Z, where Z is the sum of exp(-ΔG/(R_g T)) over all occupied cells (normalisation). The agent may approximate this by a full scan each step or by pre‑computing weights using expected changes.

In the random mode, every occupied cell is equally likely to be emptied each step, independent of energy; no free‑energy calculation is required.

Simulations are run for a 2D square 100×100 lattice and for 3D cubes of sizes 10×10×10 and 18×18×18, with periodic recording of the occupancy configurations. Percolation thresholds are extracted as the number of empty cells at the moment a spanning cluster first connects opposite faces (head and bottom). For 3D cubes, tortuosity is evaluated from the percolating cluster geometry: classify empty cells relative to the percolation direction and compute inverse tortuosity as 1/τ = (N_{p+} − N_{p-}) / N_p, where N_{p+} is the number of forward‑connected empty cells and N_{p-} the number causing backward motion within the percolating cluster. Additionally, for cubes with N0 = 1000, 5000, and 10000, the simulation is stopped at exactly 20% microporosity; the internal surface area A_p and the total free energy G_Σ are computed from the final configuration. Both modes are run on all system sizes to enable direct comparison.

## Reproduction target
Produce the following three CSV files in /app/outputs:

1. `percolation_thresholds.csv`
   - Columns: `system` (e.g., `2D_100x100`, `3D_10x10x10`, `3D_18x18x18`), `method` (`thermo` or `random`), `threshold` (number of empty cells at spanning cluster onset).

2. `tortuosity_vs_microporosity.csv`
   - Columns: `cube_size` (`10x10x10` or `18x18x18`), `microporosity` (fraction of empty cells), `inverse_tortuosity` (dimensionless, computed from the percolating cluster geometry). Each row corresponds to one measurement at a given porosity for a thermodynamic 3D cube.

3. `structural_parameters.csv`
   - Columns: `N0` (int, total initial cells), `method` (`thermo` or `random`), `internal_surface_area` (float, cell units), `free_energy` (float, in J). All rows correspond to configurations with exactly 20% microporosity.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Thermodynamic Monte Carlo simulation
- Role: process
- Action: Implement and run the thermodynamically-biased Monte Carlo simulation (temperature 300 K, surface tension 70 J/m^2) for a 2D 100x100 square lattice and 3D cubes of sizes 10x10x10 and 18x18x18, recording percolation thresholds and saving configurations at multiple porosities; also run on cubes of N0=1000, 5000, 10000 cells, stopping at exactly 20% microporosity and saving the final configurations.
- Evidence: `/app/outputs/thermo_sim.log`

### Step 2: Random Monte Carlo simulation
- Role: process
- Action: Implement the purely random vacancy process for the same lattice sizes as the thermodynamic simulation. Record percolation thresholds for 2D 100x100 and 3D 10x10x10 and 18x18x18; also run on cubes of N0=1000, 5000, 10000, saving the configuration at 20% microporosity.
- Evidence: `/app/outputs/random_sim.log`

### Step 3: Percolation threshold extraction
- Role: scored (load-bearing)
- Action: From the simulation records, extract the percolation threshold (number of empty cells at spanning cluster onset) for each system and method. Write the results to percolation_thresholds.csv.
- Output file: `/app/outputs/percolation_thresholds.csv`
- Format: csv
- Contract: system (string, e.g. '2D_100x100'), method (string, 'thermo' or 'random'), threshold (float, number of empty cells)
- Scoring: scored by hidden verifier

### Step 4: Tortuosity analysis
- Role: scored
- Action: Using the thermodynamic configurations saved for 3D cubes at various porosities, identify percolating clusters, classify empty cells, and compute inverse tortuosity. Write one row per measurement to tortuosity_vs_microporosity.csv.
- Output file: `/app/outputs/tortuosity_vs_microporosity.csv`
- Format: csv
- Contract: cube_size (string, e.g. '10x10x10'), microporosity (float), inverse_tortuosity (float)
- Scoring: scored by hidden verifier

### Step 5: Structural parameters comparison
- Role: scored
- Action: From the 20%-porosity snapshots of both thermodynamic and random clusters on N0=1000, 5000, 10000, compute internal surface area and free energy (using the formula that combines surface energy and configurational entropy). Write the results to structural_parameters.csv.
- Output file: `/app/outputs/structural_parameters.csv`
- Format: csv
- Contract: N0 (int), method (string, 'thermo' or 'random'), internal_surface_area (float), free_energy (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/percolation_thresholds.csv`
- `/app/outputs/tortuosity_vs_microporosity.csv`
- `/app/outputs/structural_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### percolation_thresholds.csv
- path: `/app/outputs/percolation_thresholds.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Percolation threshold for each lattice and method (thermodynamic and random).
- schema:
  - `required_columns`: `system`, `method`, `threshold`
  - `units`:
    - `threshold`: number of empty cells

### tortuosity_vs_microporosity.csv
- path: `/app/outputs/tortuosity_vs_microporosity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Inverse tortuosity at various microporosities for thermodynamic 3D cubes.
- schema:
  - `required_columns`: `cube_size`, `microporosity`, `inverse_tortuosity`
  - `units`:
    - `microporosity`: fraction
    - `inverse_tortuosity`: dimensionless

### structural_parameters.csv
- path: `/app/outputs/structural_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Internal surface area and free energy at 20% microporosity for different system sizes and both methods.
- schema:
  - `required_columns`: `N0`, `method`, `internal_surface_area`, `free_energy`
  - `units`:
    - `internal_surface_area`: cell units or area
    - `free_energy`: J

Notes: All outputs are compared to hidden gold values from the paper with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "percolation_thresholds.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "required_columns": [
          "system",
          "method",
          "threshold"
        ],
        "units": {
          "threshold": "number of empty cells"
        }
      },
      "description": "Percolation threshold for each lattice and method (thermodynamic and random)."
    },
    {
      "file": "tortuosity_vs_microporosity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "required_columns": [
          "cube_size",
          "microporosity",
          "inverse_tortuosity"
        ],
        "units": {
          "microporosity": "fraction",
          "inverse_tortuosity": "dimensionless"
        }
      },
      "description": "Inverse tortuosity at various microporosities for thermodynamic 3D cubes."
    },
    {
      "file": "structural_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "required_columns": [
          "N0",
          "method",
          "internal_surface_area",
          "free_energy"
        ],
        "units": {
          "internal_surface_area": "cell units or area",
          "free_energy": "J"
        }
      },
      "description": "Internal surface area and free energy at 20% microporosity for different system sizes and both methods."
    }
  ],
  "notes": "All outputs are compared to hidden gold values from the paper with appropriate tolerances."
}
```

## How you are scored
A hidden verifier scores each output file independently. For `percolation_thresholds.csv` and `tortuosity_vs_microporosity.csv`, your reported values are compared to reference values obtained from a correct implementation; numeric accuracy determines the score. For `structural_parameters.csv`, the verifier checks numeric agreement against reference values. The final reward is a weighted combination of the scores from all three artifacts. Simply reporting plausible numbers without actually running the complete simulation will not satisfy the verifier's checks.
