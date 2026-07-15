# Vacancy migration energy barrier in Fe-Cr alloys

## Problem background
The migration of vacancies in Fe-Cr alloys controls key microstructural evolution processes such as precipitation and hardening under thermal ageing and irradiation. The energy barrier for a vacancy-atom exchange is known to depend on the local chemical environment around the migrating atom and the vacancy. This task investigates how the vacancy migration barrier changes when the neighbourhood of the migrating atom is progressively filled with Cr atoms, for both Fe-vacancy and Cr-vacancy exchanges. A systematic DFT study of this dependence provides a basis for improved kinetic models.

## Approach
We use spin-polarised density functional theory (DFT) with the generalised gradient approximation (PW91) and PAW pseudopotentials to model a 250-atom bcc Fe supercell (5×5×5) containing a vacancy. Chromium atoms are introduced at a sequence of specific sites in the first and second nearest-neighbour shells of the migrating atom and vacancy, following the site nomenclature (A, B1–B3, C1–C3, D1–D3, E1–E3, F, G1–G3, H1–H3) described in the literature. For each configuration, the minimum energy path for the vacancy-atom jump is computed with the Nudged Elastic Band method using the climbing image (NEB-CI) with 5 images. The migration barrier is obtained as the difference between the saddle-point energy and the initial-state energy. Both cases where the migrating atom is Fe and where it is Cr are considered, yielding a series of barriers as a function of the Cr count in the surroundings.

## Reproduction target
Compute the migration barriers for Fe-vacancy and Cr-vacancy exchanges for the progressive filling of the first and second nearest-neighbour shells of the migrating atom with Cr atoms, from 0 to 21 Cr atoms. For each configuration, record the initial, saddle, and final energies and the migration barrier (saddle minus initial). Output the results in a CSV file with columns: Cr_count (integer), migrating_atom ('Fe' or 'Cr'), initial_energy (eV), saddle_energy (eV), final_energy (eV), migration_barrier (eV). The file must contain one row per configuration (22 rows for Fe-vacancy, 21 rows for Cr-vacancy). The computed barriers should reproduce the qualitative trends expected from atomic interactions and magnetism in the Fe-Cr system.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW pseudopotentials for Fe and Cr (e.g., PSLibrary): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Generate Fe-Cr supercell configurations
- Role: process
- Action: Generate all Fe-Cr supercell configurations: a 250-atom bcc supercell (5×5×5) with lattice parameter 2.831 Å, containing a vacancy and a migrating atom (Fe or Cr). Place Cr atoms at the sequence of sites A, B1, B2, B3, C1, C2, C3, D1, D2, D3, E1, E2, E3, F, G1, G2, G3, H1, H2, H3 according to the site nomenclature described in the paper (Figure 1). Create 22 configurations (Cr count 0 to 21) for Fe migrating, and 21 configurations (1 to 21) for Cr migrating.
- Evidence: `/app/outputs/configurations_summary.txt`

### Step 2: Compute migration barriers via DFT NEB-CI
- Role: scored (load-bearing)
- Action: For each configuration and both migrating atom types, perform spin-polarized DFT calculations using Quantum ESPRESSO with PAW pseudopotentials and GGA-PW91 exchange-correlation functional, with plane-wave cutoff 300 eV and 2×2×2 Monkhorst-Pack k-point mesh. First relax the initial and final structures, then run the NEB method with climbing image (5 images) to obtain the minimum energy path. Record the total energies (initial, saddle, final) and the migration barrier (saddle_energy - initial_energy) in the CSV file.
- Output file: `/app/outputs/migration_barriers.csv`
- Format: csv
- Contract: CSV with columns: Cr_count (integer, number of Cr atoms in first+second shells of migrating atom), migrating_atom (string, 'Fe' or 'Cr'), initial_energy (float, eV), saddle_energy (float, eV), final_energy (float, eV), migration_barrier (float, eV). One row per configuration (22 rows for Fe, 21 rows for Cr).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/migration_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### migration_barriers.csv
- path: `/app/outputs/migration_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed migration barriers for Fe and Cr vacancy exchanges; compared against paper-reported reference values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Cr_count`, `migrating_atom`, `initial_energy`, `saddle_energy`, `final_energy`, `migration_barrier`
  - `units`:
    - `initial_energy`: eV
    - `saddle_energy`: eV
    - `final_energy`: eV
    - `migration_barrier`: eV

Notes: Cr_count is the number of Cr atoms in the first and second nearest-neighbor shells of the migrating atom as defined by the site filling sequence. The checker compares migration_barrier for each (Cr_count, migrating_atom) entry to a hidden paper-reported reference within a tolerance, and also verifies internal consistency (saddle_energy > initial_energy and final_energy).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "migration_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Cr_count",
          "migrating_atom",
          "initial_energy",
          "saddle_energy",
          "final_energy",
          "migration_barrier"
        ],
        "units": {
          "initial_energy": "eV",
          "saddle_energy": "eV",
          "final_energy": "eV",
          "migration_barrier": "eV"
        }
      },
      "description": "Computed migration barriers for Fe and Cr vacancy exchanges; compared against paper-reported reference values with tolerance."
    }
  ],
  "notes": "Cr_count is the number of Cr atoms in the first and second nearest-neighbor shells of the migrating atom as defined by the site filling sequence. The checker compares migration_barrier for each (Cr_count, migrating_atom) entry to a hidden paper-reported reference within a tolerance, and also verifies internal consistency (saddle_energy > initial_energy and final_energy)."
}
```

## How you are scored
A hidden verifier will compare your submitted migration_barriers.csv against a set of reference values and physical consistency checks. It will verify that for each (Cr_count, migrating_atom) pair the reported migration barrier is numerically reasonable and that the overall trend across Cr concentrations exhibits the correct qualitative behaviour (e.g. directions of change). The verifier also checks internal consistency: the saddle energy must be higher than the initial and final energies. The final reward is based on the fraction of entries that pass these numeric and structural checks, with credit weighted toward the main Fe-vacancy trend. Missing rows or invalid signs will reduce the score. The verifier does not require exact reproduction of any particular implementation's numbers, but does require barriers that are physically plausible and follow the expected pattern.
