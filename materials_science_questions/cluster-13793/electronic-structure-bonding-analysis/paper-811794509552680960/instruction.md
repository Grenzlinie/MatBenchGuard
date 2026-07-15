# Ground-state structure and mechanical properties of PdN

## Problem background
The hypothetical 4d transition-metal mononitride PdN is of interest for its potential refractory and mechanical properties. Its ground-state crystal structure and elastic/mechanical behavior are not firmly established. Four candidate phases are considered: zinc-blende, rock-salt, cesium chloride, and wurtzite. Determining the most stable structure and computing the full set of elastic constants and derived mechanical properties for that phase provides fundamental data for understanding the material and serves as a testbed for the first-principles methodology.

## Approach
We use density-functional theory (DFT) within the local density approximation (LDA) as implemented in the Siesta code. Troullier-Martins norm-conserving pseudopotentials are generated for Pd and N. Total-energy calculations are performed for each of the four candidate structures over a range of lattice constants, fully relaxing atomic positions. The resulting energy-volume curves are fitted to Murnaghan's equation of state to extract equilibrium lattice parameters, bulk moduli, and minimum total energies. The energetic ordering of the phases is determined from these minima. For the phase predicted to be the most stable, the elastic constants C11, C12, and C44 are computed using the volume-conserving strain technique. From these, together with the bulk modulus, a complete set of mechanical and thermo-elastic properties is derived following standard relationships: shear modulus (Voigt-Reuss-Hill average), Young's modulus, Poisson's ratio, Zener anisotropy factor, Kleinman parameter, Lamé constants, longitudinal, transverse, and average sound velocities, and Debye temperature. The whole workflow is executed by the solver, with no pre-computed inputs provided.

## Reproduction target
Compute the total energy vs. volume for PdN in the zinc-blende, rock-salt, cesium chloride, and wurtzite structures. Fit these data to obtain the equilibrium lattice constants, bulk moduli, pressure derivatives, and minimum total energies for each phase. Determine the energetic ordering of the four phases and report the absolute energy difference between the wurtzite and zinc-blende structures. For the most stable phase, compute the three independent elastic constants (C11, C12, C44) and then derive all the listed mechanical and thermal properties. The required outputs are the CSV files `equilibrium_properties.csv` and `elastic_properties_ZB.csv`, whose exact schemas are defined in the workflow steps and output contract below.

## Assets

- Siesta DFT code: https://departments.icmab.es/leem/siesta/
- Python scientific stack: numpy scipy matplotlib

## Workflow steps

### Step 1: Generate pseudopotentials for Pd and N
- Role: process
- Action: Generate Troullier-Martins norm-conserving pseudopotentials for Pd and N using specified atomic configurations and cut-off radii, with LDA exchange-correlation.
- Evidence: none

### Step 2: DFT total-energy scans for four structures
- Role: process
- Action: Run Siesta DFT calculations for ZB, RS, CsCl, and WZ structures over a range of lattice constants, relaxing atomic positions, and collect total energy vs. lattice constant data.
- Evidence: `/app/outputs/energy_volume_data.csv`

### Step 3: Extract equilibrium structural properties
- Role: scored
- Action: Fit Murnaghan equation of state to the energy-volume data to obtain equilibrium lattice constants, bulk modulus, pressure derivative, and minimum total energy for each structure. Determine energetic ordering and compute the energy difference between WZ and ZB.
- Output file: `/app/outputs/equilibrium_properties.csv`
- Format: csv
- Contract: CSV with columns: structure, a0 (angstrom), B (GPa), Bprime (dimensionless), E0 (eV/atom), energy_above_ground (eV/atom, relative to ZB). For WZ rows, additional columns: c0 (angstrom), u (dimensionless), c_a (dimensionless).
- Scoring: scored by hidden verifier

### Step 4: Compute elastic constants of ZB
- Role: process
- Action: Apply the volume-conserving strain technique: generate a set of small distortive strains for the ZB cell at equilibrium a0, run DFT, and fit energy-strain data to obtain C11, C12, C44.
- Evidence: `/app/outputs/elastic_raw.csv`

### Step 5: Derive mechanical and thermo-elastic properties for ZB
- Role: scored (load-bearing)
- Action: From C11, C12, C44 and the bulk modulus B (from step 3), compute all derived properties using the formulas given in the paper: shear modulus G (Voigt-Reuss-Hill average), Young's modulus E, Poisson's ratio nu, Zener anisotropy A, Kleinman parameter zeta, Lamé constants lambda and mu, longitudinal, transverse, and average sound velocities, and Debye temperature.
- Output file: `/app/outputs/elastic_properties_ZB.csv`
- Format: csv
- Contract: CSV with one row, columns: C11, C12, C44 (GPa), G (GPa), E (GPa), nu (dimensionless), A (dimensionless), zeta (dimensionless), lambda (GPa), mu (GPa), B (GPa), vl (m/s), vt (m/s), vm (m/s), theta_D (K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_properties.csv`
- `/app/outputs/elastic_properties_ZB.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_properties.csv
- path: `/app/outputs/equilibrium_properties.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Equilibrium lattice constants, bulk moduli, pressure derivatives, total energies, and energetic ordering for the four PdN phases (ZB, RS, CsCl, WZ). The energy_above_ground column is relative to the phase with the lowest total energy (the predicted ground state), not hardcoded to any particular structure. The wurtzite row includes c0, u, and c_a.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `a0`, `B`, `Bprime`, `E0`, `energy_above_ground`
  - `optional_columns`: `c0`, `u`, `c_a`
  - `units`:
    - `a0`: angstrom
    - `B`: GPa
    - `Bprime`: dimensionless
    - `E0`: eV/atom
    - `energy_above_ground`: eV/atom
    - `c0`: angstrom
    - `u`: dimensionless
    - `c_a`: dimensionless

### elastic_properties_ZB.csv
- path: `/app/outputs/elastic_properties_ZB.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Elastic constants and derived mechanical/thermal properties for the most stable phase (the ground-state phase identified by the solver). The checker recomputes derived quantities (G, E, nu, A, zeta, lambda, mu, sound velocities, Debye temperature) from the supplied elastic constants and bulk modulus to verify internal consistency, and compares the values to paper-reported data.
- schema:
  - `type`: table
  - `required_columns`: `C11`, `C12`, `C44`, `G`, `E`, `nu`, `A`, `zeta`, `lambda`, `mu`, `B`, `vl`, `vt`, `vm`, `theta_D`
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C44`: GPa
    - `G`: GPa
    - `E`: GPa
    - `nu`: dimensionless
    - `A`: dimensionless
    - `zeta`: dimensionless
    - `lambda`: GPa
    - `mu`: GPa
    - `B`: GPa
    - `vl`: m/s
    - `vt`: m/s
    - `vm`: m/s
    - `theta_D`: K

Notes: The task covers the paper's complete pipeline for ground-state structure determination and elastic property computation of PdN. The agent must run the DFT calculations; no pre-made pseudopotentials or energy data are provided. The pseudopotential generation, DFT scans, and elastic constant computation steps are required process stages whose outputs are consumed by the scored stages. The elastic properties step is load-bearing. Output file names reflect conventional naming; the descriptions are neutralised to avoid leaking the ground-state identity ahead of the solver's own determination.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "a0",
          "B",
          "Bprime",
          "E0",
          "energy_above_ground"
        ],
        "optional_columns": [
          "c0",
          "u",
          "c_a"
        ],
        "units": {
          "a0": "angstrom",
          "B": "GPa",
          "Bprime": "dimensionless",
          "E0": "eV/atom",
          "energy_above_ground": "eV/atom",
          "c0": "angstrom",
          "u": "dimensionless",
          "c_a": "dimensionless"
        }
      },
      "description": "Equilibrium lattice constants, bulk moduli, pressure derivatives, total energies, and energetic ordering for the four PdN phases (ZB, RS, CsCl, WZ). The energy_above_ground column is relative to the phase with the lowest total energy (the predicted ground state), not hardcoded to any particular structure. The wurtzite row includes c0, u, and c_a."
    },
    {
      "file": "elastic_properties_ZB.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "C11",
          "C12",
          "C44",
          "G",
          "E",
          "nu",
          "A",
          "zeta",
          "lambda",
          "mu",
          "B",
          "vl",
          "vt",
          "vm",
          "theta_D"
        ],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C44": "GPa",
          "G": "GPa",
          "E": "GPa",
          "nu": "dimensionless",
          "A": "dimensionless",
          "zeta": "dimensionless",
          "lambda": "GPa",
          "mu": "GPa",
          "B": "GPa",
          "vl": "m/s",
          "vt": "m/s",
          "vm": "m/s",
          "theta_D": "K"
        }
      },
      "description": "Elastic constants and derived mechanical/thermal properties for the most stable phase (the ground-state phase identified by the solver). The checker recomputes derived quantities (G, E, nu, A, zeta, lambda, mu, sound velocities, Debye temperature) from the supplied elastic constants and bulk modulus to verify internal consistency, and compares the values to paper-reported data."
    }
  ],
  "notes": "The task covers the paper's complete pipeline for ground-state structure determination and elastic property computation of PdN. The agent must run the DFT calculations; no pre-made pseudopotentials or energy data are provided. The pseudopotential generation, DFT scans, and elastic constant computation steps are required process stages whose outputs are consumed by the scored stages. The elastic properties step is load-bearing. Output file names reflect conventional naming; the descriptions are neutralised to avoid leaking the ground-state identity ahead of the solver's own determination."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact. For `equilibrium_properties.csv`, it checks that the reported structural parameters and energetic ordering are plausible for a correct DFT calculation by comparing against reference benchmarks. For `elastic_properties_ZB.csv`, the verifier recomputes all derived quantities (G, E, nu, A, zeta, lambda, mu, sound velocities, Debye temperature) from the supplied C11, C12, C44, and B using the same formulas described in this task, verifying internal consistency. It then compares the raw elastic constants and the derived property values against independent reference data. Both artifacts contribute to a final combined reward; you must execute the full workflow to produce them. Simply reporting numbers without running the calculations will not yield a passing score.
