# Oxygen vacancy migration pathways in cation-ordered double perovskites from atomistic simulations

## Problem background
Perovskite oxides (ABO₃) are important for solid oxide fuel cells, supercapacitors, and chemical sensors due to their high oxygen ionic conductivity. Double perovskites (AA′BB′O₆) offer even more flexibility for tailoring properties through cation ordering. This task investigates how different cation orderings on the A-site (Sr/La) and B-site (Ti/Al) sublattices — columnar, layered, or rocksalt — affect oxygen vacancy migration in the model double perovskite SrLaTiAlO₆, using classical Buckingham potentials with nudged elastic band (NEB) calculations. The goal is to compute migration energies and diffusion pathway dimensionalities for all nine distinct ordered structures, thereby revealing how ordering controls ionic transport.

## Approach
The interactions between ions are described by Buckingham pair potentials (parameters provided) supplemented with long‑range Coulomb interactions summed via the Ewald method. Nine supercells (≈960 atoms each) are constructed, one for each A‑site × B‑site ordering combination (columnar, layered, rocksalt). Each structure is relaxed to equilibrium. The lowest‑energy oxygen vacancy site is then identified by scanning inequivalent oxygen positions: a single oxygen is removed, the structure re‑relaxed, and the vacancy formation energy computed. Starting from that lowest‑energy vacancy site, temperature‑accelerated dynamics (TAD) is used to discover candidate hop events, which are then refined using the nudged elastic band (NEB) method to find the minimum‑energy path. The saddle energy of that path gives the migration barrier (eV), and the geometry of the net center‑of‑mass translation determines the diffusion pathway dimensionality (1D, 2D, or 3D).

## Reproduction target
Produce a CSV file `migration_results.csv` with exactly one row for each of the nine distinct cation orderings of SrLaTiAlO₆: AC/BC, AC/BL, AC/BR, AL/BC, AL/BL, AL/BR, AR/BC, AR/BL, AR/BR. Each row must contain the lowest single‑hop oxygen vacancy migration energy (in eV) and the dimensionality of the net migration pathway (a string: '1D', '2D', or '3D'). The migration energy is the saddle energy of the lowest‑barrier NEB path that connects equivalent lowest‑energy vacancy sites, and the dimensionality describes the spatial extent of the net translation (e.g., confined to a plane → 2D).

## Assets

- Buckingham pair potential parameters for SrLaTiAlO6
- Molecular dynamics code (LAMMPS or equivalent): https://www.lammps.org
- Structure generation tools (ASE / Python): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Build nine ordered double perovskite supercells
- Role: process
- Action: Construct nine supercells (approximately 960 atoms each) of SrLaTiAlO₆ with all combinations of A-site ordering (columnar, layered, rocksalt for Sr/La) and B-site ordering (columnar, layered, rocksalt for Ti/Al). Assign the ordering label to each structure using the notation A-ordering/B-ordering (e.g., AC/BC, AR/BL).
- Evidence: none

### Step 2: Relax structures with Buckingham potentials
- Role: process
- Action: For each of the nine ordered structures, relax atomic positions and lattice constants using the Buckingham pair potentials (Table 1 parameters) with Ewald summation for long-range Coulomb interactions. Minimize total energy until forces and stress are converged.
- Evidence: none

### Step 3: Identify lowest-energy oxygen vacancy site per ordering
- Role: process
- Action: For each relaxed structure, create a single oxygen vacancy (remove one O atom), re-relax the atomic positions, and compute the vacancy formation energy. Scan symmetry-inequivalent oxygen sites to find the lowest-energy vacancy position. Record the coordinates of this site.
- Evidence: none

### Step 4: Run TAD and NEB saddle characterization for vacancy hops
- Role: process
- Action: For each ordered structure, run temperature-accelerated dynamics (TAD) simulations to discover candidate hop events that move the vacancy to an equivalent lowest-energy site. For each discovered event, use the nudged elastic band (NEB) method to locate the minimum energy path and extract the single‑hop migration energy barrier. From the resulting path, determine the dimensionality of the net migration pathway (1D, 2D, or 3D).
- Evidence: `/app/outputs/saddle_results.txt`

### Step 5: Compile migration energies and dimensionality into scored CSV
- Role: scored (load-bearing)
- Action: From the NEB results for each cation ordering, extract the lowest single-hop oxygen vacancy migration energy in eV and the dimensionality of the net diffusion pathway (1D, 2D, or 3D). Write one row per ordering into a CSV file named migration_results.csv.
- Output file: `/app/outputs/migration_results.csv`
- Format: csv
- Contract: CSV file with header row. Columns: ordering (string, one of: AC/BC, AC/BL, AC/BR, AL/BC, AL/BL, AL/BR, AR/BC, AR/BL, AR/BR), migration_energy_eV (float, non-negative), dimensionality (string, one of: '1D', '2D', '3D'). Exactly nine data rows, one per ordering, in any order.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/migration_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### migration_results.csv
- path: `/app/outputs/migration_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: One row per cation ordering, containing the computed migration energy (float, eV) and dimensionality string ('1D','2D','3D'). Exact string match for ordering label and dimensionality; migration energy compared within a hidden tolerance of ±0.1 eV.
- schema:
  - `type`: table
  - `required_columns`: `ordering`, `migration_energy_eV`, `dimensionality`
  - `units`:
    - `migration_energy_eV`: eV

Notes: The checker validates that exactly nine rows are present and that each row matches the expected values within the defined tolerances. Rows may appear in any order.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "migration_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ordering",
          "migration_energy_eV",
          "dimensionality"
        ],
        "units": {
          "migration_energy_eV": "eV"
        }
      },
      "description": "One row per cation ordering, containing the computed migration energy (float, eV) and dimensionality string ('1D','2D','3D'). Exact string match for ordering label and dimensionality; migration energy compared within a hidden tolerance of ±0.1 eV."
    }
  ],
  "notes": "The checker validates that exactly nine rows are present and that each row matches the expected values within the defined tolerances. Rows may appear in any order."
}
```

## How you are scored
Your submitted `migration_results.csv` is evaluated by a hidden verifier. For each ordering, the verifier compares your reported migration energy to a hidden reference value (using a tolerance) and checks whether your dimensionality string exactly matches the hidden reference. A row is fully correct only when both the energy (within tolerance) and the dimensionality (exact match) meet the hidden criteria. Your reward is the fraction of the nine rows that are fully correct, linearly scaled to the range [0, 1]. Reporting numbers without performing the required structure building, relaxation, vacancy site scanning, and NEB calculations is unlikely to satisfy the hidden checks.
