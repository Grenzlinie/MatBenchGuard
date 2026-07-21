# Monte Carlo simulation of XY-model on Sierpinski gaskets

## Problem background
The classical XY-model on two-dimensional Sierpinski gaskets — self-similar fractal lattices with a non-integer fractal dimension and finite ramification — is studied to determine whether a Berezinskii-Kosterlitz-Thouless (BKT) phase transition can occur at finite temperature. The system is described by the Hamiltonian H = -J Σ_{⟨i,j⟩} cos(θ_i - θ_j), where θ_i is the angle variable on site i and the sum runs over nearest neighbors. Sierpinski gaskets are constructed iteratively; an order‑m gasket contains N = 3(3^m+1)/2 sites, with each interior site having four nearest neighbors. Analytical arguments and a harmonic approximation have suggested the absence of a finite‑temperature transition, but a full Monte Carlo study of the helicity modulus, heat capacity, and susceptibility as functions of lattice size and boundary condition is needed to establish the behavior. This reproduction computes those observables and analyzes their trends to address whether a BKT transition exists.

## Approach
The approach is a Metropolis Monte Carlo simulation of the XY Hamiltonian on Sierpinski gaskets. Lattices of several orders are generated, and two boundary conditions are considered: closed (the three corner sites are coupled to one another) and open (the corners are uncoupled). For each lattice, simulations start with all spins aligned at low temperature; at each temperature a fixed number of Monte Carlo steps per site is discarded for equilibration, followed by a production run of several MC links for statistics. The single‑spin angular trial range is dynamically adjusted to maintain an acceptance rate of roughly 50%. The final spin configuration at one temperature serves as the starting configuration for the next higher temperature. The temperature range covers low‑temperature ordered behavior up to the disordered paramagnetic regime. From the accumulated simulation averages (mean energy, mean squared energy, derivatives of H with respect to a uniform vector potential, and magnetization moments) three observables are computed: (1) heat capacity per site from energy fluctuations, (2) helicity modulus γ from a fluctuation formula analogous to ∂²F/∂A² (explicit expressions are given in Step 4), and (3) linear susceptibility per site from magnetization fluctuations. Statistical errors are estimated via block averaging.

## Reproduction target
Your task is to compute and report three observables for the XY-model on Sierpinski gaskets of orders m=4,5,6,7 with closed boundary conditions, and for order m=6 with open boundary conditions, over a temperature range from 0.1 to 2.0 (in units of J/k_B) with sufficient temperature points to resolve the temperature dependence (at least 15 points). Specifically, produce the following CSV files with the columns listed in the output contract:

- heat_capacity.csv: heat capacity per site and its error as a function of temperature for each (m, boundary condition).
- helicity_modulus.csv: helicity modulus γ (units of J) and its error as a function of temperature for each (m, boundary condition).
- susceptibility.csv: linear susceptibility per site and its error as a function of temperature for each (m, boundary condition).

The temperature values must be reported in the column "temperature_J_over_kB". The hidden verifier will use these files to assess whether the simulated observables exhibit the expected physical behavior for this system; you do not need to match any particular reference numbers.

## Assets

- Python scientific computing stack: numpy, scipy

## Workflow steps

### Step 1: Generate Sierpinski gasket lattices
- Role: process
- Action: Generate Sierpinski gasket lattices of orders m=4,5,6,7 with closed boundary conditions (three corner sites coupled) and order m=6 with open boundary conditions (corners uncoupled). Assign Cartesian coordinates to each site using an equilateral triangular grid: place the base of the largest triangle along the x‑axis with side length 1, so that the vector potential direction (see Step 4) can be taken as the x‑direction. Compute nearest‑neighbor lists and store the coordinates.

### Step 2: Run Metropolis Monte Carlo simulations
- Role: process
- Action: For each lattice, run Metropolis Monte Carlo simulations of Hamiltonian H=-J Σ_{⟨i,j⟩} cos(θ_i-θ_j). Starting from aligned phases (θ_i = 0), discard k MC steps per site for equilibration, then collect 7 MC links of k sps each (k chosen based on system size to control statistical errors; e.g., 120000–600000 depending on the order, as used in the paper). Dynamically tune the single‑spin angular trial range to maintain ~50% acceptance rate. Use the final configuration of a temperature as the start for the next higher temperature. Temperature range should cover T/J = 0.1 to 2.0 with at least 15 logarithmically or linearly spaced points. At each MC step accumulate the following quantities:
  - H and H² (for heat capacity)
  - Magnetization vector M = (Σ cos θ_i, Σ sin θ_i) and its squared magnitude M² (for susceptibility)
  - First and second derivatives of H with respect to a fictitious uniform vector potential a (see Step 4), evaluated at a=0:
    D1 = Σ_{⟨i,j⟩} sin(θ_i - θ_j) (x_j - x_i),
    D2 = Σ_{⟨i,j⟩} cos(θ_i - θ_j) (x_j - x_i)²,
    where x_i are the x-coordinates of the sites and a is proportional to the vector potential magnitude.
  These sums are accumulated during the production phase, and their averages ⟨D1⟩, ⟨D1²⟩, ⟨D2⟩ are recorded for each temperature.

### Step 3: Compute heat capacity per site
- Role: scored
- Action: From the accumulated simulation statistics, compute the heat capacity per site C = (⟨H²⟩ - ⟨H⟩²) / (N k_B T²) for each lattice and temperature. Estimate the statistical error of C via block‑averaging (e.g., 6 blocks per link, 42 blocks total as in the paper). Write results to a CSV file.
- Output file: `/app/outputs/heat_capacity.csv`
- Format: csv
- Contract: Columns: m (int, SG order), boundary_condition (string, 'closed' or 'open'), temperature_J_over_kB (float, temperature in units of J/k_B), heat_capacity_per_site (float, dimensionless), heat_capacity_error (float, estimated statistical error, dimensionless)
- Scoring: scored by hidden verifier

### Step 4: Compute helicity modulus
- Role: scored (load-bearing)
- Action: Compute the helicity modulus γ using the exact fluctuation formula for the XY-model with a uniform vector potential.

**Physical context and definition**
To probe the stiffness of the spin configuration, introduce a uniform vector potential A parallel to one side of the triangular gasket (chosen as the x‑axis). The effect on the Hamiltonian is a Peierls phase factor on each bond:

A_{ij} = (2π/Φ_0) ∫_{r_i}^{r_j} A·dr = a (x_j - x_i),

where a = (2π/Φ_0) |A| plays the role of a tunable parameter and Φ_0 = hc/(2e) is the flux quantum. For our purpose we simply treat a as a small auxiliary variable; the helicity modulus is defined as

γ = (∂²F/∂a²)_{a=0},

with F the Helmholtz free energy.

**Expression in terms of Monte Carlo averages**
Under periodic or appropriately twisted boundary conditions (here applied via the closed‑BC twist), the second derivative of the free energy can be rewritten as

γ = ⟨∂²H/∂a²⟩ - β [⟨(∂H/∂a)²⟩ - ⟨∂H/∂a⟩²],

with β = 1/(k_B T). For the Hamiltonian H(a) = -J Σ_{⟨i,j⟩} cos(θ_i - θ_j - a (x_j - x_i)), we have at a=0:

∂H/∂a|_{a=0}  = J Σ_{⟨i,j⟩} sin(θ_i - θ_j) (x_j - x_i),
∂²H/∂a²|_{a=0} = J Σ_{⟨i,j⟩} cos(θ_i - θ_j) (x_j - x_i)².

Therefore, the helicity modulus in units of J is obtained as

γ = J [⟨D2⟩ - β (⟨D1²⟩ - ⟨D1⟩²)],

where the instantaneous lattice sums are
D1 = Σ_{⟨i,j⟩} sin(θ_i - θ_j) (x_j - x_i),
D2 = Σ_{⟨i,j⟩} cos(θ_i - θ_j) (x_j - x_i)².

**Coordinate setup**
In your Sierpinski gasket construction (Step 1) orient the gasket so that its base lies on the x‑axis. Using equilateral triangles with side length 1, the coordinates of the three corners of the zeroth‑order triangle are e.g. (0,0), (1,0), (0.5, √3/2). Higher‑order gaskets are built by subdivision; the resulting site coordinates preserve the x‑axis orientation. The vector potential is taken along +x, so the bond difference (x_j - x_i) is simply the difference of the x‑coordinates of the two sites.

**Practical computation during simulation**
During each MC step (after equilibration), compute D1 and D2 for the current spin configuration using the pre‑computed neighbor list and the x‑coordinate differences. Accumulate the following four sums over the production phase:
- Σ D1
- Σ D1²
- Σ D2
- Number of measurements N_meas
After the run, compute averages:
⟨D1⟩ = Σ D1 / N_meas,
⟨D1²⟩ = Σ D1² / N_meas,
⟨D2⟩ = Σ D2 / N_meas.
Then γ = J * (⟨D2⟩ - β (⟨D1²⟩ - ⟨D1⟩²)).

**Error estimation**
Estimate the statistical error of γ using the same block‑averaging scheme as for the heat capacity (e.g., 6 blocks per link, 42 blocks total). For each block compute γ from the block’s averages; the standard deviation of the block values gives the error γ_error.

Write the results to a CSV file.
- Output file: `/app/outputs/helicity_modulus.csv`
- Format: csv
- Contract: Columns: m (int, SG order), boundary_condition (string, 'closed' or 'open'), temperature_J_over_kB (float, temperature in J/k_B), gamma (float, helicity modulus in units of J), gamma_error (float, estimated statistical error, in units of J)
- Scoring: scored by hidden verifier

### Step 5: Compute linear susceptibility per site
- Role: scored
- Action: Compute the linear susceptibility per site χ = (⟨M²⟩ - ⟨M⟩²) / (N² k_B T), where M is the magnitude of the magnetization vector M = sqrt((Σ cos θ_i)² + (Σ sin θ_i)²). Use the same block‑averaging method to obtain statistical errors. Write results to a CSV file.
- Output file: `/app/outputs/susceptibility.csv`
- Format: csv
- Contract: Columns: m (int, SG order), boundary_condition (string, 'closed' or 'open'), temperature_J_over_kB (float, temperature in J/k_B), susceptibility_per_site (float, dimensionless), susceptibility_error (float, estimated statistical error, dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/heat_capacity.csv`
- `/app/outputs/helicity_modulus.csv`
- `/app/outputs/susceptibility.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### heat_capacity.csv
- path: `/app/outputs/heat_capacity.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Heat capacity per site for each SG order and boundary condition. The checker verifies that variation across different system sizes is small (structural sanity check).
- schema:
  - `type`: table
  - `required_columns`: `m`, `boundary_condition`, `temperature_J_over_kB`, `heat_capacity_per_site`, `heat_capacity_error`
  - `units`:
    - `temperature_J_over_kB`: J/k_B
    - `heat_capacity_per_site`: dimensionless
    - `heat_capacity_error`: dimensionless

### helicity_modulus.csv
- path: `/app/outputs/helicity_modulus.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Helicity modulus; the paper's main claim is assessed through structural trends: for closed BC low‑T γ decreases monotonically with increasing m, and for open BC γ is approximately zero at all temperatures.
- schema:
  - `type`: table
  - `required_columns`: `m`, `boundary_condition`, `temperature_J_over_kB`, `gamma`, `gamma_error`
  - `units`:
    - `temperature_J_over_kB`: J/k_B
    - `gamma`: J
    - `gamma_error`: J

### susceptibility.csv
- path: `/app/outputs/susceptibility.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Linear susceptibility per site; the checker performs a structural audit (peak position trend) as a supporting sanity check.
- schema:
  - `type`: table
  - `required_columns`: `m`, `boundary_condition`, `temperature_J_over_kB`, `susceptibility_per_site`, `susceptibility_error`
  - `units`:
    - `temperature_J_over_kB`: J/k_B
    - `susceptibility_per_site`: dimensionless
    - `susceptibility_error`: dimensionless

Notes: Square‑lattice benchmark simulations are not required for scoring. The checker evaluates key trends (monotonic decrease, zero within error bars) rather than exact numeric agreement, to accommodate Monte Carlo noise and implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "heat_capacity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "boundary_condition",
          "temperature_J_over_kB",
          "heat_capacity_per_site",
          "heat_capacity_error"
        ],
        "units": {
          "temperature_J_over_kB": "J/k_B",
          "heat_capacity_per_site": "dimensionless",
          "heat_capacity_error": "dimensionless"
        }
      },
      "description": "Heat capacity per site for each SG order and boundary condition. The checker verifies that variation across different system sizes is small (structural sanity check)."
    },
    {
      "file": "helicity_modulus.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "boundary_condition",
          "temperature_J_over_kB",
          "gamma",
          "gamma_error"
        ],
        "units": {
          "temperature_J_over_kB": "J/k_B",
          "gamma": "J",
          "gamma_error": "J"
        }
      },
      "description": "Helicity modulus; the paper's main claim is assessed through structural trends: for closed BC low‑T γ decreases monotonically with increasing m, and for open BC γ is approximately zero at all temperatures."
    },
    {
      "file": "susceptibility.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "boundary_condition",
          "temperature_J_over_kB",
          "susceptibility_per_site",
          "susceptibility_error"
        ],
        "units": {
          "temperature_J_over_kB": "J/k_B",
          "susceptibility_per_site": "dimensionless",
          "susceptibility_error": "dimensionless"
        }
      },
      "description": "Linear susceptibility per site; the checker performs a structural audit (peak position trend) as a supporting sanity check."
    }
  ],
  "notes": "Square‑lattice benchmark simulations are not required for scoring. The checker evaluates key trends (monotonic decrease, zero within error bars) rather than exact numeric agreement, to accommodate Monte Carlo noise and implementation differences."
}
```

## How you are scored
A hidden verifier, which you never see, will independently examine each of your output CSV files. It does not rely on exact numeric agreement with any pre‑supplied gold table; instead it checks structural properties and ordering relations that should hold for a correct simulation. For example, it may check monotonicity of low‑temperature values across system sizes, whether an observable is approximately zero for a certain boundary condition, or whether the position of a downturn shifts consistently with lattice size. Tolerances are set to allow for the intrinsic run‑to‑run variation of Monte Carlo simulations. The helicity modulus (helicity_modulus.csv) carries the most weight, because it is the primary indicator of whether a BKT transition occurs. The heat capacity and susceptibility carry moderate weight as supporting checks. The verifier combines the individual stage scores into a final reward value between 0 and 1. Reporting numbers without actually running the required simulation is unlikely to satisfy the structural checks.