# Computation of fluorine binding energies and migration barriers on carbon nanotubes and graphene

## Problem background
Fluorination of carbon nanotubes is an important route for chemical functionalization and activation. Experiments have shown that the fluorine surface coverage and bonding type undergo a sharp transition as the temperature is raised. At low temperatures (below 200 °C) a semi-ionic fluorine phase forms with a maximum F/C ratio of about 0.25, while at higher temperatures (above 200–250 °C) a covalent phase appears with a higher F/C ratio of approximately 0.5. The origin of this temperature-dependent transition is not fully understood, but it has been proposed that it is controlled by the energy barrier for fluorine atoms to migrate on the carbon surface — specifically, the barrier for a pair of fluorine atoms to pass through a particular (1,3) second‑neighbour configuration. In this reproduction task you will use first‑principles DFT calculations to determine the binding energies of fluorine on carbon nanotube and graphene surfaces, as well as the migration barriers for fluorine pair rearrangements. These quantities directly control the surface coverage and its temperature dependence; the results will allow you to assess whether the migration barriers can account for the experimentally observed transition.

## Approach
The calculations are performed within the local density approximation (LDA) of density functional theory, using an open‑source plane‑wave pseudopotential code (Quantum ESPRESSO) with LDA pseudopotentials taken from the SSSP solids set. The carbon substrates are modelled as periodic systems: an armchair (8,8) carbon nanotube with 192 carbon atoms, and a graphene sheet with 128 carbon atoms separated by more than 8 Å of vacuum. Fluorinated configurations are built by attaching fluorine atoms to specific carbon sites in the nanotube (single F; F₂ pairs at (1,2), (1,4_cis), and (1,3); C₄F; C₂F) and on graphene (single F). After a full geometry relaxation of each system, the binding energy per fluorine atom is obtained as (E_fluorinated – E_pristine – N_F · E_F₂ / 2) / N_F, where E_F₂ is the energy of an isolated F₂ molecule calculated separately in a large box. The C–F bond character is characterised by reporting the relaxed bond length. Migration barriers for the pair transitions (1,2)→(1,3) and (1,4_cis)→(1,3) are determined via constrained geometry scans. The constraint fixes the difference of the squared distances between the migrating fluorine atom and each of two neighbouring carbon atoms, parameterising the path; all other degrees of freedom are relaxed. The energy barrier is taken as the maximum energy along the scanned path.

## Reproduction target
Produce two CSV files that capture the key energetic and structural quantities that govern the temperature‑driven coverage transition:

1. `binding_energies_bond_lengths.csv` – For each of the seven fluorinated configurations on the (8,8) nanotube (single F, F₂ (1,2), F₂ (1,4_cis), F₂ (1,3), C₄F, C₂F) and for single F on graphene, report the binding energy per fluorine atom (in eV) and the characteristic C–F bond length (in Å).

2. `migration_barriers.csv` – For the transitions (1,2)→(1,3) and (1,4_cis)→(1,3) on both the graphene sheet and the (8,8) nanotube, report the energy barrier (in eV).

All values must be obtained with the LDA plane‑wave pseudopotential methodology described above. The relative ordering of the binding energies across different coverages (from isolated fluorine to dense layers) and the comparison between barriers on the curved nanotube and on flat graphene are essential parts of the target.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP LDA pseudopotentials (solids set): https://www.materialscloud.org/discover/sssp/table/solids

## Workflow steps

### Step 1: Relax pristine carbon substrates
- Role: process
- Action: Perform LDA geometry optimization of the pristine (8,8) carbon nanotube (192 atoms) and the pristine graphene sheet (128 atoms) using the chosen DFT code. Save the relaxed total energies and geometries for later use.
- Evidence: `/app/outputs/pristine_systems_info.json`

### Step 2: Compute isolated F₂ reference energy
- Role: process
- Action: Perform a single-point energy calculation of an isolated F₂ molecule in a large periodic box using the same DFT settings. Save the total energy for use in binding-energy formulas.
- Evidence: `/app/outputs/f2_energy.txt`

### Step 3: Compute binding energies and C–F bond lengths
- Role: scored (load-bearing)
- Action: Construct the seven fluorinated configurations on the (8,8) nanotube (single F, F₂ (1,2), F₂ (1,4_cis), F₂ (1,3), C₄F, C₂F) and single F on graphene. For each, perform a full geometry optimization with the same DFT settings. Extract the binding energy per fluorine atom as (E_fluorinated − E_pristine − N_F·E_F₂/2)/N_F and the characteristic C–F bond length(s). Write a CSV file with columns: system, configuration, binding_energy_per_F_eV, C_F_bond_length_Angstrom.
- Output file: `/app/outputs/binding_energies_bond_lengths.csv`
- Format: csv
- Contract: Columns: system (string), configuration (string), binding_energy_per_F_eV (float), C_F_bond_length_Angstrom (float). Rows for 'nanotube' configurations: F, F₂(1,2), F₂(1,4_cis), F₂(1,3), C₄F, C₂F; and for 'graphene': F.
- Scoring: scored by hidden verifier

### Step 4: Compute fluorine pair migration barriers
- Role: scored
- Action: For the transitions (1,2)→(1,3) and (1,4_cis)→(1,3) on both graphene and the (8,8) nanotube, perform constrained geometry scans. Use a constraint on the difference of squared distances between the migrating F and two neighboring C atoms, varying the constraint to obtain the energy profile while relaxing other degrees of freedom. Determine the energy barrier as the maximum energy along the path. Write a CSV file with columns: system, transition, barrier_eV.
- Output file: `/app/outputs/migration_barriers.csv`
- Format: csv
- Contract: Columns: system (string, 'graphene' or 'nanotube'), transition (string, '(1,2)→(1,3)' or '(1,4_cis)→(1,3)'), barrier_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies_bond_lengths.csv`
- `/app/outputs/migration_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies_bond_lengths.csv
- path: `/app/outputs/binding_energies_bond_lengths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed binding energies per F atom (eV) and C–F bond lengths (Å) for all required fluorinated configurations on (8,8) nanotube and graphene.
- schema:
  - `type`: table
  - `required_columns`: `system`, `configuration`, `binding_energy_per_F_eV`, `C_F_bond_length_Angstrom`
  - `units`:
    - `binding_energy_per_F_eV`: eV
    - `C_F_bond_length_Angstrom`: Å
  - `items`: object
  - `required`: object

### migration_barriers.csv
- path: `/app/outputs/migration_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed migration energy barriers (eV) for fluorine pair transitions (1,2)→(1,3) and (1,4_cis)→(1,3) on graphene and (8,8) nanotube.
- schema:
  - `type`: table
  - `required_columns`: `system`, `transition`, `barrier_eV`
  - `units`:
    - `barrier_eV`: eV
  - `items`: object
  - `required`: object

Notes: The checker compares agent-reported values to paper-derived hidden reference values with tolerances and also verifies relative trends (binding energies increase with fluorine density; nanotube barriers exceed graphene barriers).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies_bond_lengths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "configuration",
          "binding_energy_per_F_eV",
          "C_F_bond_length_Angstrom"
        ],
        "units": {
          "binding_energy_per_F_eV": "eV",
          "C_F_bond_length_Angstrom": "Å"
        },
        "items": {},
        "required": {}
      },
      "description": "Computed binding energies per F atom (eV) and C–F bond lengths (Å) for all required fluorinated configurations on (8,8) nanotube and graphene."
    },
    {
      "file": "migration_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "transition",
          "barrier_eV"
        ],
        "units": {
          "barrier_eV": "eV"
        },
        "items": {},
        "required": {}
      },
      "description": "Computed migration energy barriers (eV) for fluorine pair transitions (1,2)→(1,3) and (1,4_cis)→(1,3) on graphene and (8,8) nanotube."
    }
  ],
  "notes": "The checker compares agent-reported values to paper-derived hidden reference values with tolerances and also verifies relative trends (binding energies increase with fluorine density; nanotube barriers exceed graphene barriers)."
}
```

## How you are scored
A hidden verifier will independently score each output artifact after you submit your files.
- For `binding_energies_bond_lengths.csv`, the verifier compares your computed binding energies and bond lengths to established reference values within tolerances and checks that the relative ordering of binding energies and bond lengths across configurations is consistent with well-established physical expectations for this system.
- For `migration_barriers.csv`, the verifier compares your reported barriers for the four transitions to reference barriers and verifies that the relative ordering of barriers across systems follows expected physical trends.
The weighted combination of these scores yields a final reward between 0.0 and 1.0. Simply reporting the paper’s numbers without running the computation will not suffice; the verifier expects values that are consistent with a genuine rerun of the DFT workflow.
