# Molecular Dynamics Detection of Phase Transitions in Fullerene Crystals

## Problem background
C76 fullerene crystals exhibit temperature-dependent phase transitions arising from orientational ordering of the anisotropic D2-symmetric molecules. Molecular dynamics (MD) simulations with an atom-atom Buckingham potential can reproduce the experimentally observed face-centered cubic (fcc) and hexagonal phases and capture how their structures evolve with temperature. The goal is to compute the crystal lattice constants at room temperature and the temperature-dependent evolution of lattice parameters and potential energies, providing insight into the solid-state behavior of higher fullerenes.

## Approach
The simulation workflow begins by optimizing the geometry of a single chiral C76(D2) molecule at the semi-empirical MNDO-PM3 level to obtain rigid-body atomic coordinates. Using these coordinates, rigid-body MD cooling simulations are performed for fcc and hcp initial configurations with random molecular orientations. The intermolecular interactions are described by an atom-atom Buckingham potential with specified parameters. The systems are cooled in steps from high temperature (900 K) to low temperatures (50–100 K), with the pressure controlled to 1 atm. From the equilibrated trajectories, lattice constants, c/a ratios, and potential energies are extracted as functions of temperature. The resulting curves and lattice parameters illuminate the orientational ordering transitions and the structural characteristics of the observed phases.

## Reproduction target
Run the MD cooling protocol described in the workflow steps and produce the following three scored artifacts:

1. **`lattice_constants_300K.csv`**: lattice constants a and c (and c/a ratio for hexagonal phases) inferred from equilibrated trajectories at 300 K for each observed crystal phase (fcc, hex1, hex2).
2. **`ca_ratio_vs_T.csv`**: the c/a lattice parameter ratio as a function of temperature for any hexagonal phases observed (hex1, hex2).
3. **`potential_energy_vs_T.csv`**: the potential energy per molecule as a function of temperature for all observed phases (fcc, hex1, hex2).

The hidden verifier will compare the values and trends in these CSV files to reference expectations derived from the original study.

## Assets

- MOPAC (or equivalent MNDO-PM3 code): https://github.com/openmopac/MOPAC
- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/
- Python scientific stack: numpy,scipy,matplotlib

## Workflow steps

### Step 1: Geometry optimization of C76(D2)
- Role: process
- Action: Optimize the atomic geometry of a single chiral C76(D2) molecule using the MNDO-PM3 semi-empirical method (e.g., with MOPAC) to obtain the rigid-body coordinates used in MD. This is a required step to generate the molecular structure.
- Evidence: `/app/outputs/optimized_geometry.xyz`

### Step 2: MD cooling simulations
- Role: process
- Action: Set up rigid-body MD simulations for fcc and hcp initial configurations of C76(D2) crystals. Use the atom-atom Buckingham potential with parameters A=1.9128e6 Å⁶·J/mol, B=4.3112e7 J/mol, C=3.0612 Å⁻¹, cutoff 15 Å. Integrate equations of motion (e.g., Gear predictor-corrector with 2 fs timestep), control pressure to 1 atm (e.g., Parrinello-Rahman), thermostat via velocity scaling, and cool from 900 K down to low temperatures (100 K for hcp, 50 K for fcc) in steps. Equilibrate at each temperature and record trajectories (cell parameters, atomic positions, potential energies).
- Evidence: `/app/outputs/md_log.txt`

### Step 3: Lattice constants at 300 K
- Role: scored
- Action: From the equilibrated MD trajectories at 300 K, determine the crystal phase (fcc, hex1, hex2) and compute the lattice constants a and c. Output a CSV with one row per phase.
- Output file: `/app/outputs/lattice_constants_300K.csv`
- Format: csv
- Contract: phase (string: fcc, hex1, hex2), a_Angstrom (float), c_Angstrom (float; empty for fcc), c_a_ratio (float; empty for fcc)
- Scoring: scored by hidden verifier

### Step 4: c/a ratio vs temperature
- Role: scored (load-bearing)
- Action: For the hexagonal phases (hex1 and hex2) observed in the simulations, compute the lattice parameter ratio c/a at each sampled temperature. Output a CSV with columns phase, T_K, c_a_ratio.
- Output file: `/app/outputs/ca_ratio_vs_T.csv`
- Format: csv
- Contract: phase (string: hex1 or hex2), T_K (float), c_a_ratio (float)
- Scoring: scored by hidden verifier

### Step 5: Potential energy vs temperature
- Role: scored (load-bearing)
- Action: From the MD trajectories, extract the potential energy per molecule at each temperature for the fcc, hex1, and hex2 phases. Output a CSV with columns phase, T_K, potential_energy_per_mol_J.
- Output file: `/app/outputs/potential_energy_vs_T.csv`
- Format: csv
- Contract: phase (string: fcc, hex1, hex2), T_K (float), potential_energy_per_mol_J (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_constants_300K.csv`
- `/app/outputs/ca_ratio_vs_T.csv`
- `/app/outputs/potential_energy_vs_T.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_constants_300K.csv
- path: `/app/outputs/lattice_constants_300K.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Simulated lattice constants at 300 K for fcc, hex1, hex2 phases. Missing values for c and c/a for fcc should be empty. The checker compares against hidden reference lattice constants within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `a_Angstrom`, `c_Angstrom`, `c_a_ratio`
  - `units`:
    - `a_Angstrom`: Angstrom
    - `c_Angstrom`: Angstrom
    - `c_a_ratio`: dimensionless

### ca_ratio_vs_T.csv
- path: `/app/outputs/ca_ratio_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature dependence of the lattice ratio c/a for hexagonal phases. The checker re-derives transition temperatures from these curves and compares them to hidden reference transition temperatures.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `T_K`, `c_a_ratio`
  - `units`:
    - `T_K`: Kelvin
    - `c_a_ratio`: dimensionless

### potential_energy_vs_T.csv
- path: `/app/outputs/potential_energy_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Potential energy per molecule versus temperature for each phase. The checker re-derives transition temperatures (orientational/structural) from these curves and compares to hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `T_K`, `potential_energy_per_mol_J`
  - `units`:
    - `T_K`: Kelvin
    - `potential_energy_per_mol_J`: J/mol

Notes: The hex1 phase may not appear in every simulation; scoring focuses on fcc and hex2. The agent is expected to acquire sufficient computational resources (e.g., remote HPC or GPU-accelerated MD) for the production MD runs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_constants_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "a_Angstrom",
          "c_Angstrom",
          "c_a_ratio"
        ],
        "units": {
          "a_Angstrom": "Angstrom",
          "c_Angstrom": "Angstrom",
          "c_a_ratio": "dimensionless"
        }
      },
      "description": "Simulated lattice constants at 300 K for fcc, hex1, hex2 phases. Missing values for c and c/a for fcc should be empty. The checker compares against hidden reference lattice constants within tolerances."
    },
    {
      "file": "ca_ratio_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "T_K",
          "c_a_ratio"
        ],
        "units": {
          "T_K": "Kelvin",
          "c_a_ratio": "dimensionless"
        }
      },
      "description": "Temperature dependence of the lattice ratio c/a for hexagonal phases. The checker re-derives transition temperatures from these curves and compares them to hidden reference transition temperatures."
    },
    {
      "file": "potential_energy_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "T_K",
          "potential_energy_per_mol_J"
        ],
        "units": {
          "T_K": "Kelvin",
          "potential_energy_per_mol_J": "J/mol"
        }
      },
      "description": "Potential energy per molecule versus temperature for each phase. The checker re-derives transition temperatures (orientational/structural) from these curves and compares to hidden reference values."
    }
  ],
  "notes": "The hex1 phase may not appear in every simulation; scoring focuses on fcc and hex2. The agent is expected to acquire sufficient computational resources (e.g., remote HPC or GPU-accelerated MD) for the production MD runs."
}
```

## How you are scored
An automated hidden verifier will inspect each of the three output CSV files independently and assign weighted scores. For the lattice constants at 300 K, the verifier checks how close your computed a and c values come to expected reference lattice parameters. For the temperature-dependent files (c/a ratio and potential energy), the verifier re-derives phase transition signatures (e.g., inflection points or discontinuities) from your submitted data and compares them to reference transition temperatures and structural trends. The final reward is a combination of these checks, emphasizing the accurate reproduction of the fcc and hex2 phases. Simply reporting numbers without performing the MD simulations will not produce the consistent temperature-dependent curves the verifier requires.
