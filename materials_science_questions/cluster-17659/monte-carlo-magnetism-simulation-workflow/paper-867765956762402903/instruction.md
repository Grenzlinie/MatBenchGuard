# Monte Carlo Simulation of XY-Model on Sierpinski Gaskets

## Problem background
The classical XY-model on two-dimensional Sierpinski gaskets — fractal lattices with non-integer dimension and finite order of ramification — is a prototypical system for studying how fractal geometry affects continuous-symmetry phase transitions. On regular two-dimensional lattices the model exhibits a Berezinskii-Kosterlitz-Thouless (BKT) transition driven by vortex-antivortex unbinding, but it is unknown whether such a transition survives on a finitely ramified fractal. This task investigates the thermodynamic behavior of the XY Hamiltonian on Sierpinski gaskets by computing the helicity modulus (spin-wave stiffness) as a function of temperature and system size. The helicity modulus quantifies the system’s resistance to a uniform twist; its temperature and size dependence is the decisive probe of the absence or presence of a finite-temperature phase transition.

## Approach
Use Metropolis Monte Carlo simulations to study the classical XY Hamiltonian H = -J Σ cos(θ_i - θ_j) on two-dimensional Sierpinski gaskets. Construct lattices of several orders m (increasing number of sites) with closed boundary conditions, where the three corner sites are coupled to each other, and also for one size with open boundary conditions (corners uncoupled). Simulate over a dense temperature sweep, starting from a fully aligned spin configuration. At each temperature, discard an initial equilibration segment, then collect multiple long production runs. Maintain a roughly 50% acceptance rate by dynamically adjusting the single-spin trial angular range. From the recorded energies and the moments of the Hamiltonian derivative with respect to a uniform vector potential, compute the helicity modulus via the free-energy second-derivative expression and the heat capacity per site from energy fluctuations. The trend of the low-temperature helicity modulus with increasing system size under closed boundary conditions, together with its contrast against the open boundary case, provides the assessment of the phase transition.

## Reproduction target
Produce a CSV file `simulation_results.csv` containing the helicity modulus and heat capacity for Sierpinski gaskets of orders m = 4, 5, 6, 7 with closed boundary conditions, and for order m = 6 with open boundary conditions. The file must have columns: m (integer), boundary_condition (string: 'closed' or 'open'), temperature (float, units: k_B/J), helicity_modulus (float, units: J), heat_capacity (float, dimensionless). The temperature range should extend from low (aligned) to high (disordered) values and be sufficiently dense to capture the full temperature dependence of the helicity modulus.

## Assets

- Python 3: python3
- NumPy: numpy

## Workflow steps

### Step 1: Generate Sierpinski gasket lattices
- Role: process
- Action: Generate Sierpinski gasket lattices for orders m=4,5,6,7 with closed boundary conditions, and order m=6 with open boundary conditions. Determine site coordinates and nearest-neighbor lists.
- Evidence: `/app/outputs/lattice_info.json`

### Step 2: Run Monte Carlo simulations
- Role: process
- Action: For each lattice, run Metropolis Monte Carlo simulation of the XY Hamiltonian H = -J Σ cos(θ_i - θ_j). Start from aligned phases, discard equilibration MC steps per site, then collect multiple links of MC steps per site. Dynamically tune single-spin trial angular range to maintain ~50% acceptance. Record per-site energy, energy squared, and the moments required for the helicity modulus (∂H/∂A) at each temperature. Save raw data.
- Evidence: `/app/outputs/simulation_raw_data.npy`

### Step 3: Compute helicity modulus and heat capacity
- Role: scored (load-bearing)
- Action: From the raw simulation data, compute the helicity modulus using the free-energy second-derivative expression and the heat capacity per site from energy fluctuations. Output a CSV file with columns: m, boundary_condition, temperature, helicity_modulus, heat_capacity.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: columns: m (int), boundary_condition (string: 'closed' or 'open'), temperature (float, units: k_B/J), helicity_modulus (float, units: J), heat_capacity (float, dimensionless). One row per temperature per simulation.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Helicity modulus and heat capacity per site for XY-model on Sierpinski gaskets, used to assess absence of finite-temperature phase transition via size dependence of the helicity modulus at low temperature and the effect of boundary conditions.
- schema:
  - `type`: table
  - `required_columns`: `m`, `boundary_condition`, `temperature`, `helicity_modulus`, `heat_capacity`
  - `units`:
    - `temperature`: k_B/J
    - `helicity_modulus`: J
    - `heat_capacity`: dimensionless

Notes: Square lattice benchmark simulations, which were used for comparison in the paper, are not required for this reproduction; only Sierpinski gasket results are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "boundary_condition",
          "temperature",
          "helicity_modulus",
          "heat_capacity"
        ],
        "units": {
          "temperature": "k_B/J",
          "helicity_modulus": "J",
          "heat_capacity": "dimensionless"
        }
      },
      "description": "Helicity modulus and heat capacity per site for XY-model on Sierpinski gaskets, used to assess absence of finite-temperature phase transition via size dependence of the helicity modulus at low temperature and the effect of boundary conditions."
    }
  ],
  "notes": "Square lattice benchmark simulations, which were used for comparison in the paper, are not required for this reproduction; only Sierpinski gasket results are scored."
}
```

## How you are scored
A hidden verifier independently evaluates the artifacts you submit. Each workflow stage’s output contributes to a weighted overall reward (a float between 0 and 1). The verifier reads your `simulation_results.csv` and performs a structural audit: it checks that the helicity modulus data for closed boundary conditions shows a systematic size dependence consistent with the expected physical behavior and that the open-boundary result is consistent, without revealing the reference values. The verifier also validates that the CSV matches the required schema. No single number you report is sufficient; the hidden checker verifies that the structure and trends of your results align with the physical prediction.
