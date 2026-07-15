# Ground-state configurations and binding energies of Cu-Ni and Cu-Pd 55-atom bimetallic clusters using embedded-atom method

## Problem background
Bimetallic clusters of transition and noble metals exhibit surface segregation and ordering phenomena that influence their catalytic and material properties. The embedded-atom method (EAM) is a classical interatomic potential suitable for studying metallic cohesion in clusters. For Cu-Ni and Cu-Pd systems, it is of interest to determine the ground‑state atomic configurations and relative stabilities (icosahedral versus cuboctahedral) of 55‑atom clusters, and to quantify how the binding energy varies with the spatial distribution of Cu atoms.

## Approach
The embedded-atom method (EAM) expresses the total energy as a sum of an embedding energy for each atom, which depends on the local electron density, and a repulsive pair interaction. The Foiles–Baskes–Daw parameterization for Cu, Ni, and Pd is used, with atomic densities taken from Hartree‑Fock calculations and embedding functions derived from the universal equation of state. For each mixed‑composition cluster, perfect icosahedral and cuboctahedral geometries of 55 atoms are constructed using concentration‑averaged nearest‑neighbor distances. A large number of random atomic configurations (Cu/Ni or Cu/Pd assignments) are generated for each composition and structure. For every configuration the total EAM energy is computed, and the state with the lowest energy is identified as the ground state. The binding energy per atom and the average radial distance of Cu atoms (a measure of surface segregation) are recorded. The data for all sampled configurations of the Cu‑Ni clusters are collected to examine the relationship between binding energy and Cu radial position.

## Reproduction target
Implement the Foiles–Baskes–Daw embedded‑atom method for Cu, Ni, and Pd. Construct ideal icosahedral and cuboctahedral 55‑atom clusters for the compositions Cu13Ni42, Cu27Ni28, Cu13Pd42, and Cu27Pd28. For each of these eight systems, generate at least 350 random atomic configurations and compute the total EAM energy. From the resulting energy landscape, extract the ground‑state configuration (tuple of Cu counts per shell) and binding energy per atom, and write them to `ground_state_configs.csv`. For the four Cu‑Ni systems only, also produce a file `binding_energy_vs_r_Cu_55.csv` containing the binding energy per atom and average Cu radial distance for every sampled configuration. The tabulated data suffices; no plots are required.

## Assets

- EAM parameters for Cu, Ni, Pd (Foiles, Baskes, Daw, 1986): 10.1103/PhysRevB.33.7983
- Atomic electron densities for Cu, Ni, Pd: 10.1016/0092-640X(74)90016-3
- Universal equation of state (Rose et al., 1984): 10.1103/PhysRevB.29.2963

## Workflow steps

### Step 1: Geometry setup and distance averaging
- Role: process
- Action: Construct ideal icosahedral and cuboctahedral clusters of 55 atoms using the shell geometries and connectivity data provided in the instruction. For pure Cu, Ni, Pd clusters, determine equilibrium nearest-neighbor distances d_A, d_B by reference to the EAM equilibrium or to the values from the Foiles-Baskes-Daw parameterization. For each mixed composition (Cu13Ni42, Cu27Ni28, Cu13Pd42, Cu27Pd28), compute the concentration-averaged nearest-neighbor distance bar{d} = (N_Cu/N)*d_Cu + (N_other/N)*d_other and fix the cluster geometry accordingly. Output the shell radii, site types, and nearest-neighbor connectivity information.
- Evidence: `/app/outputs/geometry_info.json`

### Step 2: Random configuration generation
- Role: process
- Action: For each of the eight systems (Cu13Ni42, Cu27Ni28, Cu13Pd42, Cu27Pd28 in icosahedral and cuboctahedral structures), randomly generate at least 350 distinct atomic states by assigning Cu atoms to shell sites consistent with the composition and cluster geometry. Record each state as a tuple of Cu counts per shell and a unique sample identifier.
- Evidence: `/app/outputs/config_log.txt`

### Step 3: EAM total energy calculation
- Role: process
- Action: Implement the Foiles-Baskes-Daw embedded-atom method using the atomic densities, embedding functions, and pair potentials from the public references. For every generated atomic state in each system, compute the total energy within the fixed cluster geometry. Store the energy for each state alongside its configuration identifier.
- Evidence: `/app/outputs/energies.json`

### Step 4: Ground-state selection and binding energy
- Role: scored (load-bearing)
- Action: For each system, identify the atomic state with the lowest total energy (ground state). Compute the binding energy per atom (total energy divided by 55). Output one row per system to ground_state_configs.csv, including the system label, composition, structure, size, atomic configuration tuple, binding energy per atom (eV), and the average Cu radial distance computed from the shell radii.
- Output file: `/app/outputs/ground_state_configs.csv`
- Format: csv
- Contract: Columns: system (string, e.g. Cu27Ni28_ico), composition (string), structure (ico or cubo), size (int, 55), atomic_config (string representing tuple of Cu counts per shell, e.g. '(0,0,15,12)'), binding_energy_per_atom (float, eV), average_Cu_radial_distance (float, unit: inner crust radius).
- Scoring: scored by hidden verifier

### Step 5: Binding energy vs Cu radial distance for Cu-Ni
- Role: scored
- Action: For all sampled atomic states of Cu13Ni42 and Cu27Ni28 in both icosahedral and cuboctahedral structures, compute the average radial distance of Cu atoms (r_Cu) using the shell radii and the Cu counts per shell. Output binding_energy_vs_r_Cu_55.csv with all rows (at least 350 per system), each containing the system, structure, composition, sample_id, average_Cu_radial_distance, and binding_energy_per_atom (eV).
- Output file: `/app/outputs/binding_energy_vs_r_Cu_55.csv`
- Format: csv
- Contract: Columns: system (string), structure (ico or cubo), composition (string), sample_id (string or int), average_Cu_radial_distance (float, unit: inner crust radius), binding_energy_per_atom (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ground_state_configs.csv`
- `/app/outputs/binding_energy_vs_r_Cu_55.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ground_state_configs.csv
- path: `/app/outputs/ground_state_configs.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Ground-state atomic configuration, binding energy, and average Cu radial distance for each system. The checker compares the configuration tuple exactly and the binding energy within tolerance against the paper-reported reference.
- schema:
  - `type`: table
  - `required_columns`: `system`, `composition`, `structure`, `size`, `atomic_config`, `binding_energy_per_atom`, `average_Cu_radial_distance`
  - `units`:
    - `binding_energy_per_atom`: eV
    - `average_Cu_radial_distance`: inner crust radius

### binding_energy_vs_r_Cu_55.csv
- path: `/app/outputs/binding_energy_vs_r_Cu_55.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Binding energy per atom vs. average Cu radial distance for all sampled configurations of Cu-Ni 55-atom clusters. The checker verifies that the ground-state configuration (from ground_state_configs.csv) corresponds to the maximum binding energy in this set and that icosahedral binding energies are higher than cuboctahedral for the same composition.
- schema:
  - `type`: table
  - `required_columns`: `system`, `structure`, `composition`, `sample_id`, `average_Cu_radial_distance`, `binding_energy_per_atom`
  - `units`:
    - `binding_energy_per_atom`: eV
    - `average_Cu_radial_distance`: inner crust radius

Notes: Only the 55-atom clusters (sizes 55) are required. The ground-state configurations are deterministic given the public EAM parameters; binding energy tolerance accounts for minor implementation differences. The ordering and elastic-energy analyses are not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ground_state_configs.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "composition",
          "structure",
          "size",
          "atomic_config",
          "binding_energy_per_atom",
          "average_Cu_radial_distance"
        ],
        "units": {
          "binding_energy_per_atom": "eV",
          "average_Cu_radial_distance": "inner crust radius"
        }
      },
      "description": "Ground-state atomic configuration, binding energy, and average Cu radial distance for each system. The checker compares the configuration tuple exactly and the binding energy within tolerance against the paper-reported reference."
    },
    {
      "file": "binding_energy_vs_r_Cu_55.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "structure",
          "composition",
          "sample_id",
          "average_Cu_radial_distance",
          "binding_energy_per_atom"
        ],
        "units": {
          "binding_energy_per_atom": "eV",
          "average_Cu_radial_distance": "inner crust radius"
        }
      },
      "description": "Binding energy per atom vs. average Cu radial distance for all sampled configurations of Cu-Ni 55-atom clusters. The checker verifies that the ground-state configuration (from ground_state_configs.csv) corresponds to the maximum binding energy in this set and that icosahedral binding energies are higher than cuboctahedral for the same composition."
    }
  ],
  "notes": "Only the 55-atom clusters (sizes 55) are required. The ground-state configurations are deterministic given the public EAM parameters; binding energy tolerance accounts for minor implementation differences. The ordering and elastic-energy analyses are not scored."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the two output files (`ground_state_configs.csv` and `binding_energy_vs_r_Cu_55.csv`) and independently checks your results. The verifier compares your reported ground‑state configurations and binding energies to reference results derived from the paper’s procedures, using appropriate tolerances to account for implementation‑dependent differences. It also checks that your data satisfy expected structural and consistency relations, such as the relative stability ordering between icosahedral and cuboctahedral clusters and the agreement between the ground‑state entry and the binding‑energy‑versus‑distance data. Each scored artifact carries a weight, and the final reward is a weighted sum of the individual stage scores. Reporting numbers without correctly executing the workflow will not satisfy the verifier.
