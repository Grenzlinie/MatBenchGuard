# Digital-Image-Based Triangular Spring Network for Elastic Moduli of 2D Composites

## Problem background
In this task, we study the elastic properties of a two-dimensional continuum composite consisting of an elastic matrix with randomly centered circular holes (voids). As the area fraction of the holes increases, the effective Young's modulus and Poisson ratio of the sheet decrease, eventually vanishing at a geometric percolation threshold. The challenge is to compute the normalized Young's modulus and Poisson ratio of such a composite as a function of the remaining matrix area fraction, and to determine the critical area fraction at which the rigid matrix first disconnects.

## Approach
We employ a digital-image-based triangular spring network method. The continuous sheet is discretized into a periodic triangular lattice of hexagonal pixels. Nearest-neighbor pixels are connected by linear springs, with three different force constants arranged in an alternating pattern that preserves macroscopic isotropy. Circular holes are introduced by randomly placing overlapping circles of a fixed diameter; any pixel whose center falls inside a hole is marked as a hole, and springs connected to hole pixels are assigned zero stiffness. The effective elastic response is probed by applying a small uniaxial strain in one direction (both tensile and compressive) and relaxing the node positions and the perpendicular unit-cell length by conjugate-gradient minimization of the total harmonic spring energy. From the relaxed energy per unit area and the equilibrium perpendicular cell length, we extract the Young's modulus and Poisson ratio of the hole-containing sheet. To normalize the results, we first compute analytic expressions for the moduli of the perfect (hole-free) lattice for each set of spring constants. The simulation is repeated for many independent random hole configurations at each matrix area fraction, and the average moduli are reported. Additionally, a lattice burning algorithm is used on the digital hole-matrix images to estimate the geometric percolation threshold.

## Reproduction target
Compute, for each of the three spring‑constant sets (α,β,γ) = (1,1,1), (1,1,4), (1,6,7), the normalized Young's modulus E/E₀ (where E₀ is the modulus of the perfect lattice) and the Poisson ratio σ as functions of the matrix area fraction p, covering a range from low p (near the percolation threshold) up to p ≈ 1.0 (nearly no holes). Average results over 10 independent random hole configurations per p value. Additionally, estimate the critical matrix area fraction p_c at which the matrix ceases to percolate, using the same hole-matrix images.

## Assets

- Python scientific stack (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Generate random hole configurations on triangular lattice
- Role: process
- Action: For each target matrix area fraction p (e.g., 10 values between 0.3 and 1.0) and for each of the three spring-constant sets (α,β,γ) = (1,1,1), (1,1,4), (1,6,7), generate 10 independent random configurations of overlapping circular holes of diameter 11 pixels on a 210×210 periodic triangular lattice of hexagonal pixels. Place hole centers randomly, and for each pixel mark it as matrix or hole based on whether its center lies inside any hole. Compute the actual area fraction p from pixel counts. This step provides the digital images used in later simulation and percolation steps.
- Evidence: none

### Step 2: Compute perfect-lattice elastic moduli analytically
- Role: process
- Action: For each spring-constant set (α,β,γ) = (1,1,1), (1,1,4), (1,6,7), calculate the area bulk modulus K_o, shear modulus μ_o, Young's modulus E_o, and Poisson ratio σ_o using the analytical formulas for the perfect triangular lattice with three spring types that preserve isotropy.
- Evidence: `/app/outputs/perfect_moduli.json`

### Step 3: Simulate elastic response per configuration
- Role: process
- Action: For each hole configuration and spring set, construct the nearest-neighbor spring network: assign spring constants α, β, γ to matrix–matrix bonds according to the alternating pattern that ensures isotropy, and set force constant to zero for any bond involving a hole pixel. Apply a uniaxial strain of magnitude ~10⁻³ in the x-direction (both tensile and compressive). Relax node positions and the perpendicular unit-cell length using conjugate-gradient minimization of the total harmonic spring energy. Record the equilibrium total energy per unit area and perpendicular cell length. Average the tensile and compressive results to obtain the Young's modulus E and Poisson ratio σ for that configuration.
- Evidence: `/app/outputs/raw_moduli.csv`

### Step 4: Compute geometric percolation threshold
- Role: scored
- Action: Implement a lattice burning algorithm on the digital hole-matrix images generated in the configuration step. For a range of matrix area fraction p around the critical region, determine the percolation probability across multiple configurations and estimate the critical matrix area fraction p_c. Write the result to percolation_threshold.csv.
- Output file: `/app/outputs/percolation_threshold.csv`
- Format: csv
- Contract: Columns: p_c (float, critical matrix area fraction).
- Scoring: scored by hidden verifier

### Step 5: Compute average elastic moduli and normalized ratios
- Role: scored (load-bearing)
- Action: For each spring set and each p, compute the mean and standard error of E/E_o and σ from the 10 configuration replicates using the raw moduli from the simulation step and the perfect moduli from step 2. Write the averaged results to simulation_results.csv.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: Columns: set_id (string, one of '111','114','167'), p (float, area fraction), E_over_E0 (float, normalized Young's modulus), sigma (float, Poisson ratio).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/percolation_threshold.csv`
- `/app/outputs/simulation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### percolation_threshold.csv
- path: `/app/outputs/percolation_threshold.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The estimated critical matrix area fraction (percolation threshold) for the system of overlapping circular holes.
- schema:
  - `type`: table
  - `required_columns`: `p_c`
  - `units`:
    - `p_c`: dimensionless

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Averaged Young's modulus ratio and Poisson ratio vs matrix area fraction for three spring-constant sets, as computed from the triangular spring network simulations.
- schema:
  - `type`: table
  - `required_columns`: `set_id`, `p`, `E_over_E0`, `sigma`
  - `units`:
    - `p`: dimensionless
    - `E_over_E0`: dimensionless
    - `sigma`: dimensionless

Notes: The checker will compare simulation_results.csv entries against a hidden reference derived from the paper's interpolation formula and expected trends. The percolation threshold is compared to the paper-reported value within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "percolation_threshold.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "p_c"
        ],
        "units": {
          "p_c": "dimensionless"
        }
      },
      "description": "The estimated critical matrix area fraction (percolation threshold) for the system of overlapping circular holes."
    },
    {
      "file": "simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "set_id",
          "p",
          "E_over_E0",
          "sigma"
        ],
        "units": {
          "p": "dimensionless",
          "E_over_E0": "dimensionless",
          "sigma": "dimensionless"
        }
      },
      "description": "Averaged Young's modulus ratio and Poisson ratio vs matrix area fraction for three spring-constant sets, as computed from the triangular spring network simulations."
    }
  ],
  "notes": "The checker will compare simulation_results.csv entries against a hidden reference derived from the paper's interpolation formula and expected trends. The percolation threshold is compared to the paper-reported value within a tolerance."
}
```

## How you are scored
Your work will be evaluated by a hidden verifier that independently scrutinizes each required output artifact. For the percolation threshold, the reported value will be compared to a hidden reference within a tolerance. For the elastic moduli, the verifier will check that the E/E₀ vs p curve decreases monotonically and approaches unity at p≈1, that the Poisson ratio for the isotropic spring set remains constant and for the other sets approaches a value near 1/3 at low p, and that the quantitative values of E/E₀ and σ fall within acceptable relative deviations from theoretical expectations (including the known initial slope and effective medium theory limits). The final reward is a weighted combination of these checks; simply reporting numbers without executing the simulation will not pass.
