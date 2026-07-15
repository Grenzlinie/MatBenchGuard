# MD Study of Cuboctahedron-to-Icosahedron Allotropic Transition in Pd Clusters

## Problem background
Palladium nanoparticles are known to undergo solid-state structural transitions in addition to melting. Understanding the thermodynamic stability and the conditions that drive a cuboctahedron (cub) to icosahedron (ico) transformation is important for applications where thermal stability is critical. Conventional melting criteria such as potential energy and specific heat capacity caloric curves, radial distribution function, and common neighbor analysis (CNA) have been used to study these transitions, but they may not uniquely distinguish surface melting from an allotropic change. This work investigates whether an analysis of caloric curves, CNA structure fractions, and surface energy can provide clearer signatures of the cub-to-ico allotropic transition in intermediate-sized Pd clusters, and how the stability of cub clusters depends on their size.

## Approach
The study employs molecular dynamics (MD) simulations using the LAMMPS code with an embedded atom method (EAM) potential for Pd. Cuboctahedron and icosahedron clusters are constructed for shell numbers n = 2, 4, 6, 8, 10 according to the magic number formula. Each cluster is first relaxed at 300 K and then heated to above the melting temperature. For the 8‑cub cluster, temperature‑resolved trajectories are saved. From these trajectories, caloric curves (average potential energy per atom and heat capacity) are computed. Common neighbor analysis is applied to obtain the fractions of fcc, hcp, and disordered atoms at each temperature. The cluster surface energy is calculated as γ_p = (U_p / E_c) × γ_b, using a fixed bulk cohesive energy E_c = 3.935 eV/atom and bulk surface energy γ_b = 2050 mJ/m². The same heating protocol is applied to cub clusters of different sizes (n = 2, 4, 6, 8, 10) to classify their stability: whether they transform to ico already during the 300 K relaxation, whether an allotropic transition appears below the melting point, or whether the cub structure remains stable up to melting. The analysis focuses on identifying transition signatures — a step change in potential energy, a minor peak in heat capacity, a drop in fcc fraction, and a local minimum in surface energy — without assuming a specific result.

## Reproduction target
The task is to reproduce the detection of the cuboctahedron-to-icosahedron allotropic transition in the 8‑shell cuboctahedron Pd cluster (2057 atoms) and to classify the size‑dependent stability of cub clusters with shell numbers 2, 4, 6, 8, 10. You must produce the following scored output files from your MD simulations:

- `step_03_caloric_curves.csv` : temperature‑dependent average potential energy per atom and heat capacity for the 8‑cub cluster.
- `step_04_cna_fractions.csv` : temperature‑dependent fractions of fcc, hcp, and disordered atoms for the 8‑cub cluster.
- `step_06_surface_energy.csv` : temperature‑dependent surface energy for the 8‑cub cluster.
- `step_07_size_classification.csv` : a classification of each cub cluster size as `transforms_during_relaxation`, `transforms_before_melting`, or `stable`.

The hidden verifier will independently recompute transition signatures from these submitted tables. The objective is to obtain the correct physical trends, not to match any specific reported numeric value.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/
- EAM potential for Pd (Foiles et al. 1986): https://www.ctcms.nist.gov/potentials/entry/1986--Foiles-S-M-Baskes-M-I-Daw-M-S--Pd/
- Python 3 with basic scientific libraries: python>=3.8, numpy, pandas

## Workflow steps

### Step 1: Generate initial cluster structures
- Role: process
- Action: Construct cuboctahedron and icosahedron Pd clusters for shell numbers n=2,4,6,8,10 using the magic number formula N_t = (1/3)(10n^3+15n^2+11n+3). Use the bulk lattice parameter implicit in the EAM potential. Write initial atomic coordinates in LAMMPS data format.
- Evidence: `/app/outputs/clusters_generated.txt`

### Step 2: Perform molecular dynamics simulations
- Role: process
- Action: For every cluster generated in step_01, run MD simulations using LAMMPS with the EAM potential. Each simulation first relaxes at 300 K for 300 ps in the NVT ensemble with a Nose-Hoover thermostat (timestep 3 fs), then heats from 300 K to at least 1500 K at a rate of 1.4e12 K/s. For the 8-cub cluster, save atomic trajectories (dump files) and per-atom potential energies at temperature intervals no coarser than 25 K. For the other cub clusters (n=2,4,6,8,10), record the final relaxed structure at 300 K and determine whether the cub structure transforms to icosahedron during relaxation or before melting.
- Evidence: `/app/outputs/simulation_summary.log`

### Step 3: Compute caloric curves for 8-cub cluster
- Role: scored (load-bearing)
- Action: From the 8-cub MD trajectory, compute the average potential energy per atom U_p and the specific heat capacity C_p = dU_p/dT + (3/2)R at each sampled temperature. Use R = 8.314 J/(mol·K).
- Output file: `/app/outputs/step_03_caloric_curves.csv`
- Format: csv
- Contract: Columns: temperature_K (float), total_potential_energy_eV_per_atom (float), heat_capacity_J_per_mol_K (float). Row for each temperature sample.
- Scoring: scored by hidden verifier

### Step 4: Perform common neighbor analysis for 8-cub cluster
- Role: scored (load-bearing)
- Action: Apply common neighbor analysis (CNA) to the 8-cub trajectory to compute the fractions of atoms classified as fcc, hcp, and disordered at each temperature.
- Output file: `/app/outputs/step_04_cna_fractions.csv`
- Format: csv
- Contract: Columns: temperature_K (float), fcc_fraction (float), hcp_fraction (float), disordered_fraction (float). Row for each temperature sample.
- Scoring: scored by hidden verifier

### Step 5: Compute surface energy for 8-cub cluster
- Role: scored (load-bearing)
- Action: Calculate the cluster surface energy gamma_p = (U_p / E_c) * gamma_b, where E_c = 3.935 eV/atom (cohesive energy of bulk Pd) and gamma_b = 2050 mJ/m^2. Use the average potential energy per atom from the caloric curve at each temperature.
- Output file: `/app/outputs/step_06_surface_energy.csv`
- Format: csv
- Contract: Columns: temperature_K (float), surface_energy_mJ_per_m2 (float). Row for each temperature sample.
- Scoring: scored by hidden verifier

### Step 6: Classify size-dependent stability of cub clusters
- Role: scored
- Action: For cub clusters with shell numbers n=2,4,6,8,10, assign a transition_type: 'transforms_during_relaxation' if the cub structure transforms to icosahedron already during the 300 K relaxation, 'transforms_before_melting' if an allotropic transition appears below the melting temperature, 'stable' if the cub structure remains stable up to the melting point.
- Output file: `/app/outputs/step_07_size_classification.csv`
- Format: csv
- Contract: Columns: shell_number (int), transition_type (string). One row per shell number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_caloric_curves.csv`
- `/app/outputs/step_04_cna_fractions.csv`
- `/app/outputs/step_06_surface_energy.csv`
- `/app/outputs/step_07_size_classification.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_caloric_curves.csv
- path: `/app/outputs/step_03_caloric_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Caloric curves for the 8-cub cluster; checker recomputes transition signatures (step change in U_p and minor peak in C_p near 1070 K).
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `total_potential_energy_eV_per_atom`, `heat_capacity_J_per_mol_K`
  - `units`:
    - `temperature_K`: K
    - `total_potential_energy_eV_per_atom`: eV/atom
    - `heat_capacity_J_per_mol_K`: J/(mol·K)

### step_04_cna_fractions.csv
- path: `/app/outputs/step_04_cna_fractions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CNA structure fractions for the 8-cub cluster; checker verifies fcc_fraction drop by at least 20% between 1000 K and 1100 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `fcc_fraction`, `hcp_fraction`, `disordered_fraction`
  - `units`:
    - `temperature_K`: K
    - `fcc_fraction`: fraction
    - `hcp_fraction`: fraction
    - `disordered_fraction`: fraction

### step_06_surface_energy.csv
- path: `/app/outputs/step_06_surface_energy.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Surface energy for the 8-cub cluster; checker confirms a local minimum in surface energy within the same temperature window as the allotropic transition.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `surface_energy_mJ_per_m2`
  - `units`:
    - `temperature_K`: K
    - `surface_energy_mJ_per_m2`: mJ/m²

### step_07_size_classification.csv
- path: `/app/outputs/step_07_size_classification.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Stability classification for cub clusters n=2,4,6,8,10; strings compared to the paper's reported classification.
- schema:
  - `type`: table
  - `required_columns`: `shell_number`, `transition_type`
  - `units`:
    - `shell_number`: integer
    - `transition_type`: string

Notes: The caloric, CNA, and surface energy CSVs must sample temperatures no coarser than 50 K to allow reliable peak/drop detection. The EAM potential must be the one from Foiles, Baskes, and Daw (1986). The bulk cohesive energy E_c is fixed at 3.935 eV/atom and bulk surface energy gamma_b at 2050 mJ/m^2 for the surface energy calculation, as used in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_caloric_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "total_potential_energy_eV_per_atom",
          "heat_capacity_J_per_mol_K"
        ],
        "units": {
          "temperature_K": "K",
          "total_potential_energy_eV_per_atom": "eV/atom",
          "heat_capacity_J_per_mol_K": "J/(mol·K)"
        }
      },
      "description": "Caloric curves for the 8-cub cluster; checker recomputes transition signatures (step change in U_p and minor peak in C_p near 1070 K)."
    },
    {
      "file": "step_04_cna_fractions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "fcc_fraction",
          "hcp_fraction",
          "disordered_fraction"
        ],
        "units": {
          "temperature_K": "K",
          "fcc_fraction": "fraction",
          "hcp_fraction": "fraction",
          "disordered_fraction": "fraction"
        }
      },
      "description": "CNA structure fractions for the 8-cub cluster; checker verifies fcc_fraction drop by at least 20% between 1000 K and 1100 K."
    },
    {
      "file": "step_06_surface_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "surface_energy_mJ_per_m2"
        ],
        "units": {
          "temperature_K": "K",
          "surface_energy_mJ_per_m2": "mJ/m²"
        }
      },
      "description": "Surface energy for the 8-cub cluster; checker confirms a local minimum in surface energy within the same temperature window as the allotropic transition."
    },
    {
      "file": "step_07_size_classification.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "shell_number",
          "transition_type"
        ],
        "units": {
          "shell_number": "integer",
          "transition_type": "string"
        }
      },
      "description": "Stability classification for cub clusters n=2,4,6,8,10; strings compared to the paper's reported classification."
    }
  ],
  "notes": "The caloric, CNA, and surface energy CSVs must sample temperatures no coarser than 50 K to allow reliable peak/drop detection. The EAM potential must be the one from Foiles, Baskes, and Daw (1986). The bulk cohesive energy E_c is fixed at 3.935 eV/atom and bulk surface energy gamma_b at 2050 mJ/m^2 for the surface energy calculation, as used in the paper."
}
```

## How you are scored
You are not scored simply for running simulations or writing output files. Each of the four scored artifacts listed in the output contract is evaluated independently by a hidden verifier. The verifier recomputes transition signatures from your submitted data (for example, detecting a minor peak in heat capacity, a drop in the fcc fraction, a local minimum in surface energy, or correct stability classifications) and compares them against well‑defined quantitative criteria. Your overall reward is a weighted combination of the scores from the four stages. Therefore it is not enough to report numbers that look plausible; your computed results must genuinely derive from a correct computational workflow and exhibit the expected physical trends. The specific reference values and tolerances are part of the hidden grading specification and are not disclosed here.
