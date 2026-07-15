# Time-dependent Boltzmann solver for electron swarm parameters

## Problem background
Electron transport in nonthermal cold plasmas under an external electric field is governed by collisions with background gas atoms or molecules. At sufficiently high ionization degrees, electron-electron Coulomb interactions can significantly modify the electron velocity distribution and macroscopic swarm parameters such as drift velocity and mean energy. Accurate modeling of these effects is important for plasma device design. This task requires you to implement a time-dependent Boltzmann equation solver to compute steady-state electron swarm parameters in nitrogen (N2) gas for a fixed reduced electric field and several ionization degrees, using a well-known set of electron–N2 collision cross sections.

## Approach
The solver is based on a spatially homogeneous Boltzmann equation with a two-term Legendre expansion of the electron velocity distribution, including elastic, inelastic, and superelastic electron–N2 collisions as well as electron-electron Coulomb interactions in Fokker–Planck form. The equation for the isotropic part is discretized implicitly in speed and explicitly in time, yielding tridiagonal systems that are solved iteratively at each time step. You must fetch the required N2 cross-section data (momentum transfer, excitation, ionization, superelastic) from the LXCat database (Phelps set). The solver is run for a reduced electric field E/N = 10 Td at a gas temperature of 293 K, with three different ionization degree conditions: n_e/N = 0 (no electron-electron interactions), 1×10⁻⁵, and 1×10⁻⁴. For each condition, the solver is integrated forward in time until the distribution reaches steady state; the final steady-state drift velocity and mean electron energy are then extracted and saved.

## Reproduction target
Produce a CSV file named `swarm_parameters.csv` that contains the steady-state drift velocity (in cm/s) and mean electron energy (in eV) for N2 at E/N = 10 Td for three ionization degrees:

- `n_e/N = 0` (condition string: `no_ee`)
- `n_e/N = 1×10⁻⁵` (condition string: `ee_1e-5`)
- `n_e/N = 1×10⁻⁴` (condition string: `ee_1e-4`)

The file must have exactly three data rows and three columns: `condition`, `mean_energy_eV`, `drift_velocity_cm_s`. The values must correspond to the true steady-state (time‑converged) solution of the Boltzmann equation with the prescribed cross sections and Coulomb terms.

## Assets

- N2 electron-molecule cross sections (Phelps and Pitchford, 1985): https://www.lxcat.net

## Workflow steps

### Step 1: Fetch N2 cross-section data
- Role: process
- Action: Download the N2 electron-molecule collision cross sections (elastic momentum transfer, excitation, ionization, superelastic) from the LXCat Phelps database. Store them in a local table for use by the solver.
- Evidence: `/app/outputs/cross_section_fetch.log`

### Step 2: Run Boltzmann solver and output swarm parameters
- Role: scored (load-bearing)
- Action: Implement the time-dependent, spatially-homogeneous Boltzmann equation solver with two-term Legendre expansion (including elastic, inelastic, superelastic electron-atom collisions and electron-electron Coulomb Fokker–Planck terms) for N2 gas. Use the fetched cross sections and physical parameters (T=293 K, molecular mass, etc.) at a reduced electric field E/N = 10 Td. Run the solver for three ionization degrees: n_e/N = 0, 1e-5, and 1e-4. Integrate until steady state is reached. For each condition, extract the final steady-state drift velocity and mean electron energy. Write a CSV file with the results.
- Output file: `/app/outputs/swarm_parameters.csv`
- Format: csv
- Contract: CSV with three rows and columns: condition (string, one of 'no_ee', 'ee_1e-5', 'ee_1e-4'), mean_energy_eV (float), drift_velocity_cm_s (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/swarm_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### swarm_parameters.csv
- path: `/app/outputs/swarm_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Steady-state drift velocity and mean energy for three ionization degree conditions. The hidden reference values correspond to the paper's equilibrium plateaus at E/N=10 Td.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `mean_energy_eV`, `drift_velocity_cm_s`
  - `items`:
    - `condition`: string
    - `mean_energy_eV`: float
    - `drift_velocity_cm_s`: float

Notes: The agent must compute the swarm parameters by solving the Boltzmann equation with the specified cross sections and parameters. No Monte Carlo simulation is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "swarm_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "mean_energy_eV",
          "drift_velocity_cm_s"
        ],
        "items": {
          "condition": "string",
          "mean_energy_eV": "float",
          "drift_velocity_cm_s": "float"
        }
      },
      "description": "Steady-state drift velocity and mean energy for three ionization degree conditions. The hidden reference values correspond to the paper's equilibrium plateaus at E/N=10 Td."
    }
  ],
  "notes": "The agent must compute the swarm parameters by solving the Boltzmann equation with the specified cross sections and parameters. No Monte Carlo simulation is required."
}
```

## How you are scored
Your submitted `swarm_parameters.csv` will be evaluated by an automated hidden verifier. The verifier compares each reported mean energy and drift velocity to a hidden gold reference (the paper’s reported equilibrium plateau values for the identical conditions). Credit is awarded based on the closeness of your values to the reference, with a built-in tolerance that accounts for reasonable implementation differences. The verifier also checks that the drift velocity values satisfy a physically required structural order across the three ionization degree conditions (a monotonic trend). The final reward is a weighted combination of the per-condition value accuracy and the structural order check, with value accuracy receiving the dominant weight.
