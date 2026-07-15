# Formation energies of tetramer clusters on fcc (110) surfaces

## Problem background
The stability of small atomic clusters on metal surfaces governs thin‑film growth and epitaxy. For tetramer islands (clusters of four adatoms) on fcc (110) surfaces, several metastable shapes compete—square, N‑, T‑, L‑, and linear—and knowing which geometry is most stable at low temperature is essential for understanding cluster diffusion, coalescence, and the formation of extended structures. This task investigates two hetero‑epitaxial systems, Pt₄ on Cu(110) and Au₄ on Ag(110), by computing the formation energies of the five tetramer shapes at 0 K using embedded‑atom method (EAM) potentials.

## Approach
The approach is molecular statics within the embedded‑atom method (EAM). An fcc (110) slab of 6 layers (5400 atoms) is built for each substrate (Cu and Ag). After relaxing the slab at 0 K under microcanonical conditions, the five tetramer configurations—compact square (4S), two parallel dimers (4N), T‑shape (4T), L‑shape (4L), and linear chain along [110] (4l)—are placed on the relaxed surface according to their geometric descriptions. Static energy minimizations are then performed for each slab+cluster configuration, as well as for the clean slab and for a single adatom on the same slab. From these total energies the formation energy of each tetramer is obtained. All calculations use standard publicly available EAM potentials and an open‑source molecular‑dynamics code (such as LAMMPS) capable of EAM energy evaluation and minimisation.

## Reproduction target
Produce a single CSV file, `formation_energies.csv`, containing the formation energy (in eV) for all ten combinations: five shapes (4S, 4N, 4T, 4L, 4l) on each of two systems (Pt₄/Cu and Au₄/Ag). The formation energy of a tetramer shape is defined as the total energy of the slab with that cluster minus the total energy of the clean relaxed slab minus four times the total energy of a single adatom on the same surface. The CSV must have exactly 10 data rows and the columns `system` (string, either `Pt4/Cu` or `Au4/Ag`), `shape` (string from the set `4S`,`4N`,`4T`,`4L`,`4l`), and `formation_energy` (float, units eV).

## Assets

- EAM interatomic potential for Cu: https://www.ctcms.nist.gov/potentials/
- EAM interatomic potential for Pt: https://www.ctcms.nist.gov/potentials/
- EAM interatomic potential for Ag: https://www.ctcms.nist.gov/potentials/
- EAM interatomic potential for Au: https://www.ctcms.nist.gov/potentials/
- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/

## Workflow steps

### Step 1: Prepare and relax (110) substrate slabs
- Role: process
- Action: Generate fcc (110) slabs of Cu and Ag with 6 layers, 5400 atoms each. Fix the bottom layers, apply the respective EAM potential (Cu for Pt4/Cu, Ag for Au4/Ag), and relax the slabs at 0 K for 40 ps under microcanonical conditions to obtain equilibrated surface geometries. Use an open-source MD code supporting EAM (e.g., LAMMPS).
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Construct tetramer configurations and compute total energies
- Role: process
- Action: For each heterosystem (Pt4/Cu and Au4/Ag), place the five tetramer shapes (4S: compact square, 4N: two parallel dimers, 4T: T-shape, 4L: L-shape, 4l: linear chain along [110]) on the relaxed (110) substrate according to the geometric descriptions in the paper. Perform static energy minimization at 0 K with the corresponding EAM potentials to obtain the total energy of each slab+cluster configuration, and also compute the total energy of the clean relaxed slab and the energy of a single adatom on the same slab.
- Evidence: none

### Step 3: Calculate formation energies of tetramer shapes
- Role: scored (load-bearing)
- Action: For each system and shape, compute the formation energy as E_formation = E_total(slab+cluster) - E_total(clean_slab) - 4 * E_single_adatom, where E_single_adatom is the total energy of the same slab with one adatom in its relaxed on-surface position. Output all ten formation energies in a CSV file.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: Columns: system (string: 'Pt4/Cu' or 'Au4/Ag'), shape (string: '4S','4N','4T','4L','4l'), formation_energy (float, eV). Exactly 10 data rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Formation energies of tetramer clusters on Pt4/Cu(110) and Au4/Ag(110) surfaces at 0 K, used to verify the stability ranking (linear > square > others).
- schema:
  - `type`: table
  - `required_columns`: `system`, `shape`, `formation_energy`
  - `units`:
    - `formation_energy`: eV

Notes: Scoring compares the reported formation energies to the paper's reference values with tolerance and additionally checks that for each system the ordering is 4l > 4S > energies of 4N,4T,4L.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "shape",
          "formation_energy"
        ],
        "units": {
          "formation_energy": "eV"
        }
      },
      "description": "Formation energies of tetramer clusters on Pt4/Cu(110) and Au4/Ag(110) surfaces at 0 K, used to verify the stability ranking (linear > square > others)."
    }
  ],
  "notes": "Scoring compares the reported formation energies to the paper's reference values with tolerance and additionally checks that for each system the ordering is 4l > 4S > energies of 4N,4T,4L."
}
```

## How you are scored
A hidden verifier reads your `formation_energies.csv`. It compares each reported formation energy to a reference (derived from the same procedure with the same potentials) with an appropriate tolerance, and it also checks structural relations between the energies for each system. The final reward is a weighted combination of these checks—correct values and correct relative trends both contribute. The tolerance and the exact weight distribution are not disclosed; your job is to produce physically accurate formation energies by faithfully executing the described workflow, not to replicate a particular published table.
