# MD tensile testing of hydrogenated graphene mechanical properties

## Problem background
Hydrogen functionalization transforms graphene's $sp^2$ bonds to $sp^3$, which can dramatically alter its mechanical behaviour. Understanding how the critical strain and ultimate strength of hydrogenated graphene depend on hydrogen coverage, chiral orientation (armchair vs. zigzag), number of layers, and patterning (random vs. patterned hydrogen attachment) is essential for applications such as nano‑resonators and composite fillers. This task aims to characterise these dependencies through classical molecular dynamics simulations.

## Approach
The mechanical response is studied by performing uniaxial tensile tests on atomic models of hydrogenated graphene via classical molecular dynamics (MD) using the Adaptive Intermolecular Reactive Empirical Bond Order (AIREBO) potential, which allows covalent bond breaking and forming.

A baseline pristine graphene sheet (50 Å × 50 Å, 1005 carbon atoms) is tested. Hydrogen atoms are attached to carbon sites following two protocols:
- **Random hydrogenation**: hydrogen coverage is varied from 0 % to 100 % (in steps of 10 %). Neighbouring hydrogen atoms are attached on opposite sides of the sheet. Configurations are generated for single‑layer and double‑layer, each in armchair and zigzag loading orientations.
- **Patterned hydrogenation**: the sheet is fully hydrogenated except for a central graphene nanoribbon, producing four edge‑configuration combinations: armchair‑armchair (A‑A), armchair‑zigzag (A‑Z), zigzag‑armchair (Z‑A), and zigzag‑zigzag (Z‑Z).

Each sample is relaxed at 300 K, then subjected to incremental uniaxial tensile loading (0.0005 nm displacement per increment with 1000‑timestep relaxation per increment) until failure. The force‑strain curves are recorded, from which the critical strain (strain at failure) and, where applicable, the ultimate strength are extracted.

## Reproduction target
Using the workflow above, produce two CSV files:

1. `random_critical_strain.csv` — the critical strain (dimensionless fraction) as a function of hydrogen coverage (0.0, 0.1, …, 1.0) for each of the four configurations: single‑layer armchair (`sl_armchair`), single‑layer zigzag (`sl_zigzag`), double‑layer armchair (`dl_armchair`), and double‑layer zigzag (`dl_zigzag`).

2. `patterned_properties.csv` — for each of the four patterned configurations (`A‑A`, `A‑Z`, `Z‑A`, `Z‑Z`), report the critical strain (dimensionless fraction) and the ultimate strength (eV / Å).

The files must adhere to the schema defined in the Output contract.

## Assets

- LAMMPS: https://lammps.org/

## Workflow steps

### Step 1: Generate hydrogenated graphene samples
- Role: process
- Action: Generate atomic structure files for all required hydrogenated graphene samples: single‑layer and double‑layer, armchair and zigzag orientations, with random hydrogen coverages from 0% to 100% in steps of 10%, and the four patterned configurations (A‑A, A‑Z, Z‑A, Z‑Z). Use a 50 Å × 50 Å graphene sheet containing 1005 carbon atoms; attach hydrogen atoms randomly with neighbours on opposite sides as described in the paper. Write LAMMPS‑readable data files.
- Evidence: none

### Step 2: Run MD tensile simulations
- Role: process
- Action: For every generated sample, execute a LAMMPS MD tensile test using the AIREBO potential at 300 K. Apply incremental displacement (0.0005 nm per step) to boundary atoms, with 1000 timestep relaxation between increments, as detailed in the paper. Save the force‑strain data (force vs. strain) for each simulation.
- Evidence: none

### Step 3: Extract random hydrogenation critical strains
- Role: scored (load-bearing)
- Action: From the force‑strain curves of the randomly hydrogenated samples, determine the critical strain (strain at failure) for each coverage and configuration. Compile a CSV file with columns: coverage, sl_armchair, sl_zigzag, dl_armchair, dl_zigzag, where values are the critical strain as a fraction (dimensionless).
- Output file: `/app/outputs/random_critical_strain.csv`
- Format: csv
- Contract: CSV with columns: coverage (float, 0.0 to 1.0), sl_armchair (float), sl_zigzag (float), dl_armchair (float), dl_zigzag (float). Critical strain values are dimensionless fractions.
- Scoring: scored by hidden verifier

### Step 4: Extract patterned hydrogenation properties
- Role: scored
- Action: From the force‑strain curves of the patterned samples, determine the critical strain and ultimate strength for each of the four configurations (A‑A, A‑Z, Z‑A, Z‑Z). Compile a CSV file with columns: configuration, critical_strain, ultimate_strength, where critical_strain is a fraction and ultimate_strength is in eV/Å.
- Output file: `/app/outputs/patterned_properties.csv`
- Format: csv
- Contract: CSV with columns: configuration (string, one of A‑A, A‑Z, Z‑A, Z‑Z), critical_strain (float, dimensionless fraction), ultimate_strength (float, eV/Å).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/random_critical_strain.csv`
- `/app/outputs/patterned_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### random_critical_strain.csv
- path: `/app/outputs/random_critical_strain.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical strain (strain at failure) as a function of hydrogen coverage for random hydrogenation, for single‑layer armchair, single‑layer zigzag, double‑layer armchair, and double‑layer zigzag configurations. Checked by comparing to paper‑reported values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `coverage`, `sl_armchair`, `sl_zigzag`, `dl_armchair`, `dl_zigzag`
  - `units`:
    - `coverage`: dimensionless fraction 0‑1
    - `sl_armchair`: dimensionless strain fraction
    - `sl_zigzag`: dimensionless strain fraction
    - `dl_armchair`: dimensionless strain fraction
    - `dl_zigzag`: dimensionless strain fraction

### patterned_properties.csv
- path: `/app/outputs/patterned_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical strain and ultimate strength for the four patterned edge configurations (A‑A, A‑Z, Z‑A, Z‑Z). Checked by comparing to paper‑reported values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `critical_strain`, `ultimate_strength`
  - `units`:
    - `configuration`: string
    - `critical_strain`: dimensionless strain fraction
    - `ultimate_strength`: eV/Å

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "random_critical_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "coverage",
          "sl_armchair",
          "sl_zigzag",
          "dl_armchair",
          "dl_zigzag"
        ],
        "units": {
          "coverage": "dimensionless fraction 0‑1",
          "sl_armchair": "dimensionless strain fraction",
          "sl_zigzag": "dimensionless strain fraction",
          "dl_armchair": "dimensionless strain fraction",
          "dl_zigzag": "dimensionless strain fraction"
        }
      },
      "description": "Critical strain (strain at failure) as a function of hydrogen coverage for random hydrogenation, for single‑layer armchair, single‑layer zigzag, double‑layer armchair, and double‑layer zigzag configurations. Checked by comparing to paper‑reported values with tolerance."
    },
    {
      "file": "patterned_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "critical_strain",
          "ultimate_strength"
        ],
        "units": {
          "configuration": "string",
          "critical_strain": "dimensionless strain fraction",
          "ultimate_strength": "eV/Å"
        }
      },
      "description": "Critical strain and ultimate strength for the four patterned edge configurations (A‑A, A‑Z, Z‑A, Z‑Z). Checked by comparing to paper‑reported values with tolerance."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently score your submitted artifacts. For `random_critical_strain.csv`, it compares the reported critical strains against expected reference values for each coverage and configuration; for `patterned_properties.csv`, it compares your critical strain and ultimate strength values against reference data. All comparisons use a relative tolerance to account for legitimate differences between implementations. Simply reporting the paper's numbers is not sufficient — the verifier expects values that could plausibly arise from a genuine re‑execution of the described computational protocol.
