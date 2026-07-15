# Permeability of microcracked solids with crack connectivity

## Problem background
Evaluating the effective permeability of microcracked solids is important for predicting the durability of engineering materials such as concrete and rock. In realistic service conditions, microcracks are not necessarily isolated; they can partially interconnect, forming networks that may enhance the material's permeability before reaching full percolation. Classical micromechanics models treat cracks as separate inclusions and cannot directly account for such connectivity. This task addresses the challenge of incorporating finite crack connectivity into permeability estimates by extending the interaction direct derivative (IDD) method, a micromechanics scheme for composite materials, and by conducting numerical simulations on representative volume elements (RVE). The objective is to compute the effective relative permeability S/S₀ as a function of crack density and connectivity, and to quantify the geometry coefficient β that captures the connectivity-induced amplification effect.

## Approach
The analytical component is based on the IDD method. For two-dimensional cases, the method models each crack as a degenerated elliptical inclusion surrounded by an elliptical matrix atmosphere whose size is determined by the crack density. Using the dilute estimate for permeability, the IDD method provides explicit formulas for the relative permeability of solids with isolated, randomly oriented microcracks. To handle connectivity, the approach introduces a crack connectivity parameter φ (the fraction of the total crack area involved in interconnections) and hypothesizes that the connected crack network behaves like a network of isolated cracks with an amplified effective crack density ρ₂′ = (1 + β φ) ρ₂, where β is a geometry coefficient. The parameter β is not known a priori and must be calibrated from numerical experiments. The numerical component uses a Monte‑Carlo algorithm to generate 2D square RVEs containing randomly oriented rectilinear microcracks with half‑lengths sampled from a normal distribution N(10, 2.5²). For given target crack density ρ₂ and connectivity φ, multiple realizations are created. Each RVE is meshed with crack and matrix elements; a unit potential gradient is applied along one axis with null flux on the transverse boundaries, and the Laplace equation is solved via the finite element method to obtain the effective permeability components. The isotropic average of the directional permeabilities gives the effective S, and relative permeability S/S₀ is computed. From the numerical S/S₀ for connected cracks and the IDD prediction for isolated cracks at the same density, the ratio is formed, and β is solved such that the extended IDD formula matches the numerical result. The workflow produces three tables: one for isolated cracks (comparing numerical and IDD predictions), one for connected cracks including computed β values, and a summary table of β as a function of density and connectivity.

## Reproduction target
Implement the 2D simulation pipeline and analytical IDD computations as described. For crack density ρ₂ taking values 0.1, 0.2, …, 1.0 and connectivity φ taking values 0.0, 0.1, …, 0.8 (with φ=0 corresponding to isolated cracks), generate and analyze crack network RVEs. Specifically: (1) For isolated cracks (φ=0), compute the FEM‑averaged relative permeability S/S₀ and the IDD analytical prediction for each density, and output them in effective_permeability_isolated.csv. (2) For connected cracks, compute S/S₀ numerically for every (ρ₂, φ) pair, together with the corresponding IDD prediction for isolated cracks at the same density, and derive the geometry coefficient β by inverting the extended IDD relation. Output the results in effective_permeability_connected.csv. (3) Extract the β values into a separate summary table beta_vs_connectivity.csv. All output files must match the column schemas and paths specified in the workflow steps.

## Assets

- Python 3.x: https://www.python.org/
- NumPy: numpy
- SciPy: scipy
- NetworkX: networkx

## Workflow steps

### Step 1: Monte-Carlo RVE generation and FEM simulations
- Role: process
- Action: Generate 2D square RVEs (160×160) containing randomly oriented and positioned rectilinear microcracks with half-lengths sampled from N(10, 2.5²). For each crack density ρ₂ ∈ {0.1, 0.2, …, 1.0} and connectivity φ ∈ {0.0, 0.1, …, 0.8}, use Monte-Carlo algorithm to create 10 crack network realizations per (ρ₂, φ) satisfying target connectivity. For each realization, mesh matrix and crack elements, impose unit potential gradient along x and null flux on top/bottom boundaries, and solve Laplace equation via FEM to obtain effective permeability components Sₓ, Sᵧ. Compute isotropic average S = (Sₓ+Sᵧ)/2 and the relative permeability S/S₀, averaging over 10 realizations for each (ρ₂, φ). Output summary evidence of simulation runs.
- Evidence: `/app/outputs/simulation_summary.txt`

### Step 2: Compute IDD analytical predictions for isolated cracks
- Role: process
- Action: Using the analytical formulas for the 2D isotropic case (the IDD method with elliptical matrix atmosphere), compute the IDD-predicted relative permeability S/S₀ for each crack density ρ₂ considered (ρ₂ = 0.1, 0.2, …, 1.0).
- Evidence: none

### Step 3: Output isolated permeability table
- Role: scored
- Action: Write a CSV file with columns: crack_density, S_over_S0_numerical (the FEM-averaged relative permeability for isolated cracks, i.e., φ=0), S_over_S0_IDD (the IDD analytical prediction), num_realizations (the number of realizations used, default 10). One row per crack density from 0.1 to 1.0.
- Output file: `/app/outputs/effective_permeability_isolated.csv`
- Format: csv
- Contract: Columns: crack_density (float), S_over_S0_numerical (float), S_over_S0_IDD (float), num_realizations (int). One row per density.
- Scoring: scored by hidden verifier

### Step 4: Output connected permeability and beta table
- Role: scored (load-bearing)
- Action: For each pair of crack density ρ₂ (0.1 to 1.0) and connectivity φ (0.0 to 0.8) that was simulated, write a CSV with columns: crack_density, connectivity, S_over_S0_numerical (the FEM-averaged relative permeability for that pair), S_over_S0_IDD (the IDD prediction for the same density without connectivity), ratio_numerical_to_IDD (computed as S_over_S0_numerical / S_over_S0_IDD), beta (the geometry coefficient β computed by solving the extended IDD relation with ρ₂′ = (1+βφ)ρ₂ so that the extended IDD prediction matches the numerical S/S₀).
- Output file: `/app/outputs/effective_permeability_connected.csv`
- Format: csv
- Contract: Columns: crack_density (float), connectivity (float), S_over_S0_numerical (float), S_over_S0_IDD (float), ratio_numerical_to_IDD (float), beta (float). One row per (density, connectivity) pair.
- Scoring: scored by hidden verifier

### Step 5: Output beta summary table
- Role: scored
- Action: From the results of step04, extract the β values for each (ρ₂, φ) pair and write a CSV with columns: crack_density, connectivity, beta.
- Output file: `/app/outputs/beta_vs_connectivity.csv`
- Format: csv
- Contract: Columns: crack_density (float), connectivity (float), beta (float). One row per combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_permeability_isolated.csv`
- `/app/outputs/effective_permeability_connected.csv`
- `/app/outputs/beta_vs_connectivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_permeability_isolated.csv
- path: `/app/outputs/effective_permeability_isolated.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Relative permeability for isolated cracks: numerical (FEM) vs IDD prediction.
- schema:
  - `type`: table
  - `required_columns`: `crack_density`, `S_over_S0_numerical`, `S_over_S0_IDD`, `num_realizations`
  - `units`:
    - `crack_density`: dimensionless
    - `S_over_S0_numerical`: dimensionless
    - `S_over_S0_IDD`: dimensionless
    - `num_realizations`: count

### effective_permeability_connected.csv
- path: `/app/outputs/effective_permeability_connected.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Effective permeability for connected cracks, ratio to IDD, and β coefficient.
- schema:
  - `type`: table
  - `required_columns`: `crack_density`, `connectivity`, `S_over_S0_numerical`, `S_over_S0_IDD`, `ratio_numerical_to_IDD`, `beta`
  - `units`:
    - `crack_density`: dimensionless
    - `connectivity`: dimensionless
    - `S_over_S0_numerical`: dimensionless
    - `S_over_S0_IDD`: dimensionless
    - `ratio_numerical_to_IDD`: dimensionless
    - `beta`: dimensionless

### beta_vs_connectivity.csv
- path: `/app/outputs/beta_vs_connectivity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Geometry coefficient β vs connectivity and density.
- schema:
  - `type`: table
  - `required_columns`: `crack_density`, `connectivity`, `beta`
  - `units`:
    - `crack_density`: dimensionless
    - `connectivity`: dimensionless
    - `beta`: dimensionless

Notes: All quantities are dimensionless relative permeability ratios. The hidden checker will verify numerical S/S₀ against paper-reported values, IDD predictions against analytical recomputation, and β consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_permeability_isolated.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "crack_density",
          "S_over_S0_numerical",
          "S_over_S0_IDD",
          "num_realizations"
        ],
        "units": {
          "crack_density": "dimensionless",
          "S_over_S0_numerical": "dimensionless",
          "S_over_S0_IDD": "dimensionless",
          "num_realizations": "count"
        }
      },
      "description": "Relative permeability for isolated cracks: numerical (FEM) vs IDD prediction."
    },
    {
      "file": "effective_permeability_connected.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "crack_density",
          "connectivity",
          "S_over_S0_numerical",
          "S_over_S0_IDD",
          "ratio_numerical_to_IDD",
          "beta"
        ],
        "units": {
          "crack_density": "dimensionless",
          "connectivity": "dimensionless",
          "S_over_S0_numerical": "dimensionless",
          "S_over_S0_IDD": "dimensionless",
          "ratio_numerical_to_IDD": "dimensionless",
          "beta": "dimensionless"
        }
      },
      "description": "Effective permeability for connected cracks, ratio to IDD, and β coefficient."
    },
    {
      "file": "beta_vs_connectivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "crack_density",
          "connectivity",
          "beta"
        ],
        "units": {
          "crack_density": "dimensionless",
          "connectivity": "dimensionless",
          "beta": "dimensionless"
        }
      },
      "description": "Geometry coefficient β vs connectivity and density."
    }
  ],
  "notes": "All quantities are dimensionless relative permeability ratios. The hidden checker will verify numerical S/S₀ against paper-reported values, IDD predictions against analytical recomputation, and β consistency."
}
```

## How you are scored
Each output CSV is independently scored by a hidden verifier. For effective_permeability_isolated.csv, the verifier checks that the IDD predictions are correctly computed according to the analytical formulas and that the numerical S/S₀ values are consistent with the paper’s reported numerical results (checked against hidden reference values within reasonable tolerances). For effective_permeability_connected.csv, the verifier recomputes β from the submitted columns and verifies internal consistency: the ratio column must equal S_over_S0_numerical divided by S_over_S0_IDD, and the computed β must agree with the hidden reference β values. The verifier also checks that the submitted β values match those in beta_vs_connectivity.csv exactly. The final reward is a weighted sum of scores from these checks, rewarding accurate reproduction of the effective permeability and the connectivity‑amplification coefficient. Reporting numbers close to the paper’s reported values is necessary to receive full credit; trivial guesses or fabricated numbers will be detected by the hidden checks and tolerance thresholds.
