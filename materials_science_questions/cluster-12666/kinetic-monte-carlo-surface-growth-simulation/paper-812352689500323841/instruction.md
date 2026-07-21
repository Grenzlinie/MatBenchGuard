# Kinetic Monte Carlo Surface Growth Scaling Exponents

## Problem background
Tetrahedral amorphous carbon (ta-C) films are ultra-thin protective coatings used in magnetic storage. The surface roughness of growing films often follows fractal scaling laws: at a given thickness, roughness varies with lateral measurement length scale through a roughness exponent α, while the time (or thickness) evolution of the root-mean-square roughness is governed by a growth exponent β. The paper proposes that energetic carbon ion deposition, followed by local flattening due to a thermal spike around the impact site, is the key mechanism that makes ta-C surfaces exceptionally smooth. A kinetic Monte Carlo simulation with a configurable thermal-spike radius was used to model this process and compute the resulting scaling exponents. Your task is to recreate this simulation and determine the exponents for different thermal-spike ranges.

## Approach
The simulation runs on a two-dimensional 512×512 lattice that represents the growing film surface. The growth proceeds monolayer by monolayer. A monolayer is defined as the deposition of **L × L** particles (L = 512), one per lattice site on average. For each particle, a lattice site is chosen uniformly at random, and its height is incremented by 1. Immediately after deposition, a thermal spike relaxation is applied: all sites whose **Manhattan distance** from the impact site is less than or equal to an integer radius N (including the impact site) are identified. The heights of these sites are replaced by the arithmetic mean of their current heights (floating‑point values are allowed). This random deposition plus thermal-spike flattening is repeated for a total of **30 monolayers**. Three separate simulations are run, using N = 1, N = 2, and N = 3 nearest neighbours, respectively. The full surface height array after the final monolayer may be saved as intermediate data for the analysis, but it is not a required output file.

From these height arrays, the analysis proceeds in two parts. First, the overall root-mean-square (RMS) roughness of the whole lattice is recorded after every monolayer. The growth exponent β is extracted from the scaling of roughness with film thickness (typically by fitting a power-law relation in the early growth regime). Second, on the final surface, the height–height correlation function H(r) is computed as a function of lateral separation r. At small r, H(r) behaves as a power law with exponent 2α; the roughness exponent α is obtained from the slope of a log–log plot of H(r) versus r. This analysis is performed for each of the three neighbour counts, yielding three pairs of (α, β).

## Reproduction target
For each thermal-spike radius (N = 1, 2, and 3 nearest neighbours), run the Monte Carlo simulation and extract the two scaling exponents: the growth exponent β and the roughness exponent α. Produce a comma-separated CSV file (`scaling_exponents.csv`) that contains one row per neighbour count, with columns `neighbor_count` (the integer N), `alpha` (the roughness exponent), and `beta` (the growth exponent).

## Assets

- Python scientific computing environment: numpy scipy matplotlib

## Workflow steps

### Step 1: Monte Carlo Simulation with Thermal Spike
- Role: process
- Action: Implement a kinetic Monte Carlo model on a 512×512 lattice. For each monolayer, deposit exactly 512×512 particles at random positions; after each deposition, apply thermal spike flattening using the average height of all sites within Manhattan distance ≤ N of the impact site. Run for 30 monolayers for each neighbour count N = 1, 2, 3. Keep the final surface height arrays in memory or in temporary files for Step 2.
- Evidence: Simulation completed; surface height arrays are available for analysis in Step 2.

### Step 2: Extract Scaling Exponents
- Role: scored (load-bearing)
- Action: From the simulated surface height arrays, compute the root-mean-square roughness for each monolayer. Analyze roughness vs. thickness to extract growth exponent β and compute the height–height correlation function to extract roughness exponent α for each neighbour count. Output a CSV file with the exponents.
- Output file: `/app/outputs/scaling_exponents.csv`
- Format: csv
- Contract: CSV with columns neighbor_count (int), alpha (float), beta (float). One row per neighbor count 1, 2, 3.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/scaling_exponents.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### scaling_exponents.csv
- path: `/app/outputs/scaling_exponents.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Scaling exponents for the kinetic Monte Carlo surface growth simulation.
- schema:
  - `type`: table
  - `required_columns`: `neighbor_count`, `alpha`, `beta`
  - `units`:
    - `alpha`: dimensionless
    - `beta`: dimensionless

Notes: The checker will verify that alpha and beta are within predetermined acceptable ranges and that both increase monotonically with neighbour count.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "scaling_exponents.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "neighbor_count",
          "alpha",
          "beta"
        ],
        "units": {
          "alpha": "dimensionless",
          "beta": "dimensionless"
        }
      },
      "description": "Scaling exponents for the kinetic Monte Carlo surface growth simulation."
    }
  ],
  "notes": "The checker will verify that alpha and beta are within predetermined acceptable ranges and that both increase monotonically with neighbour count."
}
```

## How you are scored
A hidden verifier will independently assess your results after submission. It reads `/app/outputs/scaling_exponents.csv` and checks the reported α and β values against hidden gold criteria derived from the paper's simulation. These checks include whether each exponent falls within an expected tolerance range and whether the set of exponents across neighbour counts satisfies internal consistency constraints (e.g., monotonic behaviour). The verifier also confirms that the CSV file has the correct structure (three rows, required columns). The final score is a weighted combination of these checks, with the exponent values carrying most of the weight. You do not need to know the target numbers; the verifier automatically compares your output to the hidden reference.