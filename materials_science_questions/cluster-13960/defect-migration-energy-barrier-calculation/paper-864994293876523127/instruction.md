# Statistical Moment Method for Samarium-Doped Ceria Properties

## Problem background
Solid oxide fuel cells (SOFCs) require electrolyte materials with high oxygen ion conductivity. Samarium-doped ceria (SDC, Ce1-xSmxO2-x/2) exhibits enhanced ionic conductivity compared to pure ceria, with performance varying non‑monotonically with dopant concentration. The Statistical Moment Method (SMM) provides closed‑form analytical expressions for the structural and electrical properties of SDC, enabling efficient computation of lattice parameter, vacancy–dopant association energies, vacancy migration energies, and ionic conductivity without heavy numerical simulations. This task implements the SMM to reproduce these key quantities and analyze how Sm doping affects conduction.

## Approach
The SMM describes the crystal through anharmonic vibrations of Ce4+, Sm3+ and O2- ions. From the interatomic Buckingham potentials (provided below), the harmonic constants, frequencies, and nonlinear anharmonic parameters are derived. The temperature‑dependent nearest‑neighbor distance (and hence lattice parameter) is obtained by solving moment‑expansion equations for the ion displacements.

Helmholtz free energies are computed for Ce, Sm, and O ions in Ce1-xSmxO2-x/2, taking into account the preferential distribution of oxygen vacancies around Sm3+ ions. The total interaction potentials are expressed with combinatorial occupancy factors for different vacancy configurations (1NN or 2NN relative to Sm).

Association energies between an oxygen vacancy and a Sm dopant are obtained from the free‑energy differences of crystal layers with and without vacancy association. Vacancy migration energies are calculated as free‑energy differences between the initial state and the saddle‑point state, using interaction potentials that incorporate the oxygen ion exchange.

Three cation‑edge configurations (Ce–Ce, Ce–Sm, Sm–Sm) are considered, as well as three trapping configurations with 1, 2 or 3 Sm ions occupying first‑neighbour sites around the migrating vacancy. Finally, ionic conductivity at a given temperature is computed from an Arrhenius‑type expression, where the effective activation energy sums the association and migration contributions, and a pre‑exponential factor accounts for ion charge, jump distance, oscillation frequency, correlation factor, and formation entropy.

## Reproduction target
Implement the SMM pipeline and produce the following scored artifacts:

- `lattice_parameter.csv`: lattice parameter a as a function of dopant concentration x (from 0 to 0.4) at 300 K.
- `association_energies.csv`: oxygen vacancy–dopant association energies for vacancies at first nearest neighbour (1NN) and second nearest neighbour (2NN) positions relative to a Sm ion.
- `migration_energies.csv`: vacancy migration energies across the three possible cation edges: Ce–Ce, Ce–Sm, and Sm–Sm.
- `trapping_migration_energies.csv`: migration energies for three symmetric/asymmetric configurations with 1, 2, and 3 Sm ions occupying 1NN sites around the migrating vacancy.
- `conductivity.csv`: ionic conductivity σ at 1073 K as a function of x (0 to 0.4).

The aim is to obtain the quantitative dependence of these properties on Sm content, and to verify the expected relative trends: association energy at 1NN more negative than at 2NN; migration energy increasing with Sm coverage on the cation edge; and conductivity that first rises then decays, indicating an optimum doping level.

## Assets

- Buckingham potential parameters for Ce-O, Sm-O, O-O interactions

## Workflow steps

### Step 1: Build SMM model and compute intermediate quantities
- Role: process
- Action: Implement the Statistical Moment Method (SMM) to compute anharmonic vibrational parameters, temperature-dependent nearest-neighbor distance, total interaction potentials, and Helmholtz free energies for Ce, Sm, and O ions in Ce1-xSmxO2-x/2, using the provided Buckingham potential parameters. Save the derived model and free energy functions.
- Evidence: `/app/outputs/smm_model.pkl`

### Step 2: Compute lattice parameter vs. dopant concentration
- Role: scored
- Action: Using the SMM model, compute the lattice parameter a at T=300 K for dopant concentrations x from 0 to 0.4 in steps (e.g., 0, 0.05, 0.10, ..., 0.40). Write lattice_parameter.csv with columns x (float) and a (float, Angstrom).
- Output file: `/app/outputs/lattice_parameter.csv`
- Format: csv
- Contract: x: float (dopant concentration), a: float (lattice parameter in Angstrom)
- Scoring: scored by hidden verifier

### Step 3: Compute vacancy-dopant association energies
- Role: scored
- Action: Compute the oxygen vacancy-dopant association energy E_ass for vacancies at the first nearest neighbor (1NN) and second nearest neighbor (2NN) sites relative to a Sm ion. Write association_energies.csv with columns position (string '1NN' or '2NN') and E_ass (float, eV).
- Output file: `/app/outputs/association_energies.csv`
- Format: csv
- Contract: position: string (1NN or 2NN), E_ass: float (eV, negative)
- Scoring: scored by hidden verifier

### Step 4: Compute vacancy migration energies across cation edges
- Role: scored
- Action: Compute the vacancy migration energy E_m for the three possible cation edges: Ce–Ce, Ce–Sm, Sm–Sm. Write migration_energies.csv with columns edge (string) and E_m (float, eV).
- Output file: `/app/outputs/migration_energies.csv`
- Format: csv
- Contract: edge: string (Ce-Ce, Ce-Sm, Sm-Sm), E_m: float (eV)
- Scoring: scored by hidden verifier

### Step 5: Compute trapping migration energies
- Role: scored (load-bearing)
- Action: Compute the migration energy for three configurations of Sm ions at 1NN sites around the migrating vacancy: (1) 1 Sm ion, (2) 2 Sm ions, (3) 3 Sm ions, as described. Write trapping_migration_energies.csv with columns configuration (string 'config1', 'config2', 'config3') and E_m (float, eV).
- Output file: `/app/outputs/trapping_migration_energies.csv`
- Format: csv
- Contract: configuration: string (config1, config2, config3), E_m: float (eV)
- Scoring: scored by hidden verifier

### Step 6: Compute ionic conductivity
- Role: scored
- Action: Calculate the ionic conductivity sigma at T=1073 K for dopant concentrations x from 0 to 0.4 in steps. Use the effective activation energy from association and migration energies and the pre-exponential factor sigma0 provided in the instruction. Write conductivity.csv with columns x (float) and sigma (float, S/cm).
- Output file: `/app/outputs/conductivity.csv`
- Format: csv
- Contract: x: float (dopant concentration), sigma: float (S/cm)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_parameter.csv`
- `/app/outputs/association_energies.csv`
- `/app/outputs/migration_energies.csv`
- `/app/outputs/trapping_migration_energies.csv`
- `/app/outputs/conductivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_parameter.csv
- path: `/app/outputs/lattice_parameter.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Lattice parameter a as a function of Sm doping x at room temperature.
- schema:
  - `type`: table
  - `required_columns`: `x`, `a`
  - `units`:
    - `x`: None
    - `a`: Angstrom

### association_energies.csv
- path: `/app/outputs/association_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Vacancy-dopant association energies at 1NN and 2NN positions.
- schema:
  - `type`: table
  - `required_columns`: `position`, `E_ass`
  - `units`:
    - `position`: None
    - `E_ass`: eV

### migration_energies.csv
- path: `/app/outputs/migration_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Vacancy migration energies across Ce-Ce, Ce-Sm, and Sm-Sm edges.
- schema:
  - `type`: table
  - `required_columns`: `edge`, `E_m`
  - `units`:
    - `edge`: None
    - `E_m`: eV

### trapping_migration_energies.csv
- path: `/app/outputs/trapping_migration_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Migration energies for three trapping configurations (1,2,3 Sm ions at 1NN sites).
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `E_m`
  - `units`:
    - `configuration`: None
    - `E_m`: eV

### conductivity.csv
- path: `/app/outputs/conductivity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Ionic conductivity at T=1073 K as a function of Sm doping.
- schema:
  - `type`: table
  - `required_columns`: `x`, `sigma`
  - `units`:
    - `x`: None
    - `sigma`: S/cm

Notes: All scored values are compared to hidden paper-reported references within appropriate tolerances. Structural relations (e.g., E_ass_1NN < E_ass_2NN, E_m(Ce-Ce) < E_m(Ce-Sm) < E_m(Sm-Sm), conductivity peak near x=0.15) are also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_parameter.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "a"
        ],
        "units": {
          "x": null,
          "a": "Angstrom"
        }
      },
      "description": "Lattice parameter a as a function of Sm doping x at room temperature."
    },
    {
      "file": "association_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "position",
          "E_ass"
        ],
        "units": {
          "position": null,
          "E_ass": "eV"
        }
      },
      "description": "Vacancy-dopant association energies at 1NN and 2NN positions."
    },
    {
      "file": "migration_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "edge",
          "E_m"
        ],
        "units": {
          "edge": null,
          "E_m": "eV"
        }
      },
      "description": "Vacancy migration energies across Ce-Ce, Ce-Sm, and Sm-Sm edges."
    },
    {
      "file": "trapping_migration_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "E_m"
        ],
        "units": {
          "configuration": null,
          "E_m": "eV"
        }
      },
      "description": "Migration energies for three trapping configurations (1,2,3 Sm ions at 1NN sites)."
    },
    {
      "file": "conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "sigma"
        ],
        "units": {
          "x": null,
          "sigma": "S/cm"
        }
      },
      "description": "Ionic conductivity at T=1073 K as a function of Sm doping."
    }
  ],
  "notes": "All scored values are compared to hidden paper-reported references within appropriate tolerances. Structural relations (e.g., E_ass_1NN < E_ass_2NN, E_m(Ce-Ce) < E_m(Ce-Sm) < E_m(Sm-Sm), conductivity peak near x=0.15) are also verified."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s output. For every CSV artifact the verifier compares the submitted values against a hidden reference (derived from the paper’s own reported calculations) within appropriate tolerances. In addition, the verifier checks structural relationships such as the ordering of association energies and migration energies (e.g., E_ass(1NN) < E_ass(2NN), E_m(Ce–Ce) < E_m(Ce–Sm) < E_m(Sm–Sm)) and the qualitative shape of the conductivity versus doping curve (increase followed by a decrease). The individual stage scores are combined, weighted by their importance, to produce the final reward. Reporting the paper’s numbers without executing the SMM workflow will not satisfy the scoring criteria.
