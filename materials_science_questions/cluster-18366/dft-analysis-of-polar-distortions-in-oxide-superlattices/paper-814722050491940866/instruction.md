# Energetic decomposition of domain wall competition in strained ultrathin ferroelectric films

## Problem background
Ferroelectric ultrathin films can host nanoscale domains whose functional properties are highly sensitive to the orientation and morphology of the domain walls. One promising route to tune these walls is through epitaxial strain, but the precise mechanism by which strain controls whether walls lie along (100) or (110) planes or become labyrinthine remains an open challenge. This task investigates that competition in a model PbTiO₃ thin film, using a first‑principles‑derived effective Hamiltonian to compute the total internal energy and its decomposition for three distinct domain‑wall configurations as a function of misfit strain at low temperature.

## Approach
We model a (001) PbTiO₃ film of ∼4.8 nm thickness under open‑circuit electrical boundary conditions. A first‑principles‑derived effective Hamiltonian that includes local soft modes (electric dipoles), oxygen‑octahedra tiltings, and homogeneous as well as inhomogeneous strain serves as the energy model. Epitaxial strain is imposed by fixing the in‑plane lattice constants to simulate different misfit values. The system is represented by a 12×12×12 supercell, and Monte Carlo simulations are used to anneal the configuration down to 6 K. For each misfit strain in the compressive range we initialize three different out‑of‑plane domain morphologies: (100)‑type walls, (110)‑type walls, and a wandering/labyrinthine pattern. After convergence, the total internal energy and its constituents—short‑range dipolar, local‑mode self‑energy plus strain–local‑mode coupling, and long‑range dipole‑dipole interactions—are extracted. Comparing these energies across strains and configurations reveals the driving forces behind the observed domain‑wall morphology trends.

## Reproduction target
Compute the total internal energy (relative to the paraelectric phase) and its decomposition into three contributions (short‑range dipolar, self‑strain, and long‑range dipole‑dipole) for the three domain wall configurations—(100)‑type, (110)‑type, and wandering—at a temperature of 6 K for misfit strains ranging from –3.0 % to –1.0 % in steps no larger than 0.2 %. Output the results to the file `domain_energies.csv` as specified in the workflow steps. The analysis should capture how the balance of the energy components changes with strain and domain morphology.

## Assets

- PbTiO3 effective Hamiltonian parameters: https://doi.org/10.1103/PhysRevB.52.6301

## Workflow steps

### Step 1: Implement effective Hamiltonian and MC simulation framework
- Role: process
- Action: Implement the first-principles-derived effective Hamiltonian for PbTiO3 thin films, incorporating the 28.5% reduction of the on-site harmonic parameter, open-circuit electrical boundary conditions (depolarization field), and epitaxial strain constraints. Set up a 12×12×12 supercell and a Monte Carlo annealing loop for cooling runs.
- Evidence: none

### Step 2: Run MC simulations for strain scan and three domain morphologies
- Role: process
- Action: For each misfit strain value in the range -3.0% to -1.0% (in steps of 0.2%), initialize the system into three distinct out-of-plane domain wall configurations: (100)-type walls, (110)-type walls, and a wandering/labyrinthine pattern. Perform Monte Carlo sweeps (up to 320,000 sweeps) to cool the system to 6 K, allowing local modes, oxygen tiltings, and free strain components to relax. Collect the converged total internal energy and its constituents (short-range dipolar, local-mode self-energy + strain-dipole coupling, long-range dipole-dipole) for each configuration and strain.
- Evidence: none

### Step 3: Output energy vs strain data
- Role: scored (load-bearing)
- Action: Compile the simulation results into a CSV file with columns: strain (misfit strain in percent, e.g. -1.8), configuration (string: '100-type', '110-type', 'wandering'), total_energy (meV per five atoms), short_range_energy (meV), self_strain_energy (meV, sum of local-mode self-energy and strain–local-mode coupling), long_range_dipole_energy (meV). All energies are referenced to the paraelectric phase.
- Output file: `/app/outputs/domain_energies.csv`
- Format: csv
- Contract: CSV with columns: strain (float, percent), configuration (string: '100-type', '110-type', 'wandering'), total_energy (float, meV per five atoms), short_range_energy (float, meV), self_strain_energy (float, meV), long_range_dipole_energy (float, meV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/domain_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### domain_energies.csv
- path: `/app/outputs/domain_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Energy decomposition of the three domain wall morphologies (100-type, 110-type, wandering) as a function of misfit strain at 6 K. The checker compares the energy differences and component ordering against hidden reference values to verify the strain-driven competition and the window for wandering walls.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `configuration`, `total_energy`, `short_range_energy`, `self_strain_energy`, `long_range_dipole_energy`
  - `units`:
    - `strain`: percent
    - `total_energy`: meV per five-atom cell
    - `short_range_energy`: meV per five-atom cell
    - `self_strain_energy`: meV per five-atom cell
    - `long_range_dipole_energy`: meV per five-atom cell

Notes: The solver must implement the effective Hamiltonian and run MC simulations from scratch; no precomputed energies are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "domain_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "configuration",
          "total_energy",
          "short_range_energy",
          "self_strain_energy",
          "long_range_dipole_energy"
        ],
        "units": {
          "strain": "percent",
          "total_energy": "meV per five-atom cell",
          "short_range_energy": "meV per five-atom cell",
          "self_strain_energy": "meV per five-atom cell",
          "long_range_dipole_energy": "meV per five-atom cell"
        }
      },
      "description": "Energy decomposition of the three domain wall morphologies (100-type, 110-type, wandering) as a function of misfit strain at 6 K. The checker compares the energy differences and component ordering against hidden reference values to verify the strain-driven competition and the window for wandering walls."
    }
  ],
  "notes": "The solver must implement the effective Hamiltonian and run MC simulations from scratch; no precomputed energies are provided."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads `domain_energies.csv`. The verifier checks whether the predicted total energy differences between the three configurations as a function of strain follow a physically meaningful ordering (e.g., which domain type is most stable in different strain regimes) and whether the decomposition into short‑range, self‑strain, and long‑range dipole contributions exhibits the expected relative magnitudes for the different domain morphologies. Comparisons are made against a hidden reference derived from the paper's reported findings, with tolerances that account for numerical implementation differences. The final reward is the weighted combination of these checks, so simply reporting values that match the hidden reference is not enough—the trend and component ordering must be internally consistent and physically plausible.
