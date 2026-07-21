# Kinetic Monte Carlo Simulation of Obliquely Deposited Film Growth and Structural Analysis

## Problem background
Obliquely deposited thin films develop a columnar microstructure due to self-shadowing and limited surface diffusion. The resulting structural anisotropy strongly influences the films’ physical properties (mechanical, electrical, magnetic). Understanding how the deposition angle controls the morphology—film density, average column spacing, column cross‑sectional shape and tilt, and the anisotropy of column distribution—is essential for tailoring films for microwave and spintronic applications.

## Approach
The microstructure is produced by a 3D kinetic Monte Carlo (KMC) model of thin film growth. Particles are deposited randomly onto a cubic lattice with periodic boundary conditions in the substrate plane, and a fully occupied bottom layer serves as the substrate. Each particle moves along a straight ballistic trajectory at a prescribed incidence angle α measured from the normal. It stops and joins the film if it has occupied nearest neighbours (100 % probability) or occupied next‑nearest neighbours (50 % probability, randomly picking one).

**Neighbour definitions (cubic lattice)**  
- **Nearest neighbour:** any cell whose coordinates differ from the particle by at most 1 in each direction, excluding the particle itself (26 cells total — face, edge, and corner neighbours).  
- **Next‑nearest neighbour:** any cell whose coordinates differ from the particle by at most 2 in each direction, but which is **not** a nearest neighbour and not the particle itself. These form the second shell of cells around the particle.

**Joining rule:**  
1. If at least one nearest neighbour is occupied → particle stops and joins the film with 100 % probability (if multiple nearest neighbours are occupied, the particle stays at its current position; no choice is needed because it simply stops).  
2. Else if at least one next‑nearest neighbour is occupied → particle stops with 50 % probability and, if it stops, it is placed in one of the occupied next‑nearest neighbour cells chosen uniformly at random.  
3. Otherwise the particle continues its trajectory until it meets one of the conditions.

After joining, the particle undergoes limited surface diffusion: it attempts S hops among its vacant nearest‑neighbour cells, with a hop probability that favours sites with more occupied neighbours according to an exponential rule parameterized by γ. The model parameters S and γ are taken from a calibration to experimental porosity data and are specified in the workflow steps. Multiple independent simulations are run at each angle to obtain robust statistics.

From the resulting 3D occupancy arrays, structural metrics are extracted. Specific film density is computed by averaging the occupation over layers away from the substrate and top. The average inter‑column distance is obtained from the radial profile of the layer‑averaged 2D fast Fourier transform (FFT): the dominant spatial frequency gives the mean column spacing. Column shape and anisotropy are characterized via the layer‑averaged 2D autocorrelation function. Fitting an ellipse to the central peak at half‑maximum yields correlation lengths in the x and y directions and the column tilt angle β; the anisotropy ratio is derived from these lengths.

## Reproduction target
Reproduce the dependence of structural metrics (specific density, average inter‑column distance, correlation lengths, tilt angle, and anisotropy ratio) on the deposition angle α for α in 0° to 88°, as computed by the KMC model with the specified parameters (S = 5, γ = 0.45) on a 256 × 256 × 80 cubic lattice. The final output is a CSV file named structural_results.csv, with one row per angle α containing the averaged values of density (dimensionless), D (in units of the lattice cell edge Δ), ξ_x (Δ), ξ_y·cosβ (Δ), β (degrees), and the anisotropy ratio ξ_x/(ξ_y·cosβ) (dimensionless).

## Assets

- Python scientific stack (numpy, scipy, matplotlib): https://python.org

## Workflow steps

### Step 1: Run Kinetic Monte Carlo growth simulations
- Role: process
- Action: Implement the cubic‑lattice KMC model with ballistic trajectories at angle α, the nearest‑neighbour and next‑nearest‑neighbour stopping/joining rules defined above, limited surface diffusion (S = 5 hops per particle, hop probability P_{i → j} = exp(γ·N_j) / ∑_k exp(γ·N_k) with γ = 0.45), a fully occupied bottom layer, and periodic boundary conditions in x and y. Run 10 independent simulations for each deposition angle α in {0, 20, 30, 45, 55, 60, 65, 70, 75, 80, 85, 88} degrees on a 256 × 256 × 80 cubic lattice. Keep the generated occupancy matrices in memory for analysis.

### Step 2: Compute structural metrics and report
- Role: scored (load‑bearing)
- Action: For each angle and run, compute:
  - **(i) Specific density ρ** averaged over layers 1Δ < z < 64Δ (i.e. layer indices 1 to 63 inclusive);
  - **(ii) Average 2D FFT spectrum** over x–y layers in the range 1Δ < z < 64Δ, extract its radial profile to find the dominant spatial frequency and convert it to the average inter‑column distance D;
  - **(iii) 2D autocorrelation function** computed for each layer in the range 2Δ < z < 64Δ (layers 2 to 63), averaged over these layers, fit an ellipse to the central peak at half‑maximum to obtain the correlation lengths ξ_x and ξ_y, the column tilt angle β, and the anisotropy ratio ξ_x/(ξ_y·cosβ).
  Average all results over the 10 runs per angle and write the per‑angle averages to a CSV file named structural_results.csv.
- Output file: `/app/outputs/structural_results.csv`
- Format: csv
- Contract: columns: alpha (deg), density (dimensionless), D (units: Δ), xi_x (units: Δ), xi_y_cos_beta (units: Δ), beta (deg), anisotropy_ratio (dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_results.csv
- path: `/app/outputs/structural_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Averaged structural metrics per deposition angle.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `density`, `D`, `xi_x`, `xi_y_cos_beta`, `beta`, `anisotropy_ratio`
  - `columns`:
    - `name`: alpha
    - `type`: float
    - `unit`: degree
    - `name`: density
    - `type`: float
    - `unit`: dimensionless
    - `name`: D
    - `type`: float
    - `unit`: Delta
    - `name`: xi_x
    - `type`: float
    - `unit`: Delta
    - `name`: xi_y_cos_beta
    - `type`: float
    - `unit`: Delta
    - `name`: beta
    - `type`: float
    - `unit`: degree
    - `name`: anisotropy_ratio
    - `type`: float
    - `unit`: dimensionless

Notes: The hidden reference values come from the paper's reported results for the specified simulation conditions (S=5, gamma=0.45, 256x256x80 lattice, 10 runs per angle). The checker compares the reported numbers against these reference values with per-metric tolerances and may also check monotonic trends for density, D, xi_y_cos_beta, and beta.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "density",
          "D",
          "xi_x",
          "xi_y_cos_beta",
          "beta",
          "anisotropy_ratio"
        ],
        "columns": [
          {
            "name": "alpha",
            "type": "float",
            "unit": "degree"
          },
          {
            "name": "density",
            "type": "float",
            "unit": "dimensionless"
          },
          {
            "name": "D",
            "type": "float",
            "unit": "Delta"
          },
          {
            "name": "xi_x",
            "type": "float",
            "unit": "Delta"
          },
          {
            "name": "xi_y_cos_beta",
            "type": "float",
            "unit": "Delta"
          },
          {
            "name": "beta",
            "type": "float",
            "unit": "degree"
          },
          {
            "name": "anisotropy_ratio",
            "type": "float",
            "unit": "dimensionless"
          }
        ]
      },
      "description": "Averaged structural metrics per deposition angle."
    }
  ],
  "notes": "The hidden reference values come from the paper's reported results for the specified simulation conditions (S=5, gamma=0.45, 256x256x80 lattice, 10 runs per angle). The checker compares the reported numbers against these reference values with per-metric tolerances and may also check monotonic trends for density, D, xi_y_cos_beta, and beta."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that compares your reported structural_results.csv against reference values (obtained from the paper’s model under the same conditions) for each angle and each metric. The verifier checks whether each metric falls within an acceptable tolerance of the reference, and may also verify expected monotonic trends (e.g., density must change monotonically with angle, and certain metrics must exhibit consistent directional changes). Meeting or beating the reference on a directional metric earns full credit, while missing the trend reduces credit. The final reward is a weighted combination across all scored artifacts. Simply reporting the reference numbers without genuinely running the simulations will produce a sparse or inconsistent output that fails many checks.