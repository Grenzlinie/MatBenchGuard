# Oxygen vacancy migration energy barriers in double perovskite SrLaTiAlO6 with varying cation ordering

## Problem background
Perovskite oxides are promising solid electrolytes for fuel cells, sensors, and other devices because they can exhibit high oxygen ionic conductivity. Double perovskites with formula AA'BB'O6 offer additional chemical flexibility: when the A and B cation sublattices are occupied by two different cation species, the cations can arrange in distinct ordered patterns. These cation orderings can dramatically change the energy landscape for oxygen vacancies, thus affecting their mobility.

This task examines the double perovskite SrLaTiAlO6, constructed from the end members SrTiO3 and LaAlO3. There are three common types of ordering on each sublattice — columnar (C), layered (L), and rocksalt (R) — giving nine possible ordered structures. The goal is to compute, for each ordering, the minimum migration barrier an oxygen vacancy must overcome to hop, and the dimensionality (1D, 2D, or 3D) of the resulting diffusion pathway. By comparing the nine results, one can infer how cation ordering influences ionic transport in this class of materials.

## Approach
The interactions between ions are described using Buckingham pair potentials of the form
V_ij = A_ij exp(-r_ij/ρ_ij) - C_ij / r_ij⁶,
combined with long-range Coulomb interactions summed via the Ewald method. The parameters and formal charges used are:

  Interaction    A (eV)       ρ (Å)     C (eV·Å⁶)
  Sr-O           682.172      0.39450    0
  Ti-O           2179.122     0.30384    8.986
  La-O           2088.79      0.3460    23.25
  Al-O           1725.20      0.28971    0.0
  O-O            9547.96      0.21916   32.0

Formal charges: Sr +2, Ti +4, La +3, Al +3, O -2.

The workflow begins by building 960‑atom supercells for the nine orderings (AC/BC, AC/BL, AC/BR, AL/BC, AL/BL, AL/BR, AR/BC, AR/BL, AR/BR, where the first letter indicates A‑site ordering and the second B‑site ordering). Each supercell is then relaxed to its minimum energy using the potentials above.

Next, for each relaxed structure, oxygen vacancy formation energies are evaluated at all symmetry‑inequivalent oxygen sites. The site with the lowest formation energy is selected as the starting point for migration studies because the vacancy will most likely reside there.

Finally, temperature‑accelerated dynamics (TAD) is used to explore the energy landscape around the vacancy, and the nudged elastic band (NEB) method is employed to characterize the saddle points of discovered events. From these calculations, the single‑hop migration barrier (the lowest‑energy barrier that leads to net diffusion) is extracted in eV, and the dimensionality of the overall lowest‑energy pathway is determined. The results for all nine orderings are collected into a single CSV file.

## Reproduction target
Using the given Buckingham pair potentials and formal charges, construct the nine ordered SrLaTiAlO6 supercells. Relax each structure to obtain equilibrium lattice constants and relaxed atomic positions. Then, for each ordering, compute oxygen vacancy formation energies for all distinct oxygen sites, identify the most stable vacancy site, run temperature‑accelerated dynamics (TAD) simulations and nudged elastic band (NEB) calculations, and determine the minimum single‑hop migration barrier (in eV) and the dimensionality (1D, 2D, or 3D) of the lowest‑energy diffusion pathway. Report the results in `/app/outputs/step_01_migration_results.csv` with columns: A_order (C/L/R), B_order (C/L/R), migration_energy_eV (float), dimensionality (string). There must be exactly nine rows, one for each ordering.

## Assets

- Buckingham potential parameters for Sr-O, Ti-O, La-O, Al-O, O-O
- Cation ordering patterns for nine double perovskites
- Open-source NEB and molecular dynamics capability

## Workflow steps

### Step 1: Generate ordered supercells
- Role: process
- Action: Build nine SrLaTiAlO6 supercells (960 atoms each) corresponding to all combinations of columnar (C), layered (L), and rocksalt (R) orderings on the A (Sr/La) and B (Ti/Al) sublattices: AC/BC, AC/BL, AC/BR, AL/BC, AL/BL, AL/BR, AR/BC, AR/BL, AR/BR.
- Evidence: `/app/outputs/generated_structures.log`

### Step 2: Relax structures
- Role: process
- Action: Energy-minimize each supercell using the Buckingham pair potentials (Table 1) and Ewald summation to obtain equilibrium lattice constants and relaxed atomic positions. Record the relaxed configurations.
- Evidence: `/app/outputs/relaxed_structures.log`

### Step 3: Identify lowest-energy vacancy site
- Role: process
- Action: For each relaxed structure, compute oxygen vacancy formation energies for all symmetry-distinct oxygen sites and select the most stable site (lowest formation energy).
- Evidence: `/app/outputs/vacancy_site_selection.log`

### Step 4: TAD+NEB migration barriers
- Role: scored (load-bearing)
- Action: For each ordering, run temperature-accelerated dynamics (TAD) simulations starting from the lowest-energy vacancy site, characterize discovered saddle points with the nudged elastic band (NEB) method to obtain single-hop migration barriers (eV), and determine the dimensionality of the lowest-energy migration pathway (1D, 2D, or 3D). Compile the results into a CSV file.
- Output file: `/app/outputs/step_01_migration_results.csv`
- Format: csv
- Contract: CSV with columns: A_order (string, one of C/L/R), B_order (string, one of C/L/R), migration_energy_eV (float), dimensionality (string, one of '1D','2D','3D'). Exactly 9 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_migration_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_migration_results.csv
- path: `/app/outputs/step_01_migration_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Migration energy (eV) and dimensionality (1D/2D/3D) for each of the nine cation orderings.
- schema:
  - `type`: table
  - `required_columns`: `A_order`, `B_order`, `migration_energy_eV`, `dimensionality`
  - `units`:
    - `migration_energy_eV`: eV

Notes: Migration energies are compared to the expected reference values with tolerance; dimensionality must match exactly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_migration_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "A_order",
          "B_order",
          "migration_energy_eV",
          "dimensionality"
        ],
        "units": {
          "migration_energy_eV": "eV"
        }
      },
      "description": "Migration energy (eV) and dimensionality (1D/2D/3D) for each of the nine cation orderings."
    }
  ],
  "notes": "Migration energies are compared to the expected reference values with tolerance; dimensionality must match exactly."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier. The verifier reads your output CSV and, for each ordering, compares the reported migration energy and dimensionality against a hidden gold reference derived from the original study. Migration energies are checked within an appropriate tolerance, and dimensionalities must match the reference exactly. The final reward is based on how many of the nine orderings are reproduced correctly, with higher weight for the migration barriers and the dimensionalities combined. Intermediate process logs (generated_structures.log, relaxed_structures.log, vacancy_site_selection.log) help document your workflow, but the primary scoring depends on the migration_results.csv file. Accurate reproduction requires a faithful execution of the described workflow; simply guessing or reporting out‑of‑context numbers will not yield a high score.
