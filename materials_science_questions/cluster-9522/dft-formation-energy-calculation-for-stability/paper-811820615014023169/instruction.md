# DFT Formation Energy Calculation for Stability of Fe-Cr Ordered Intermetallics

## Problem background
Fe–Cr alloys at low Cr concentrations exhibit complex ordering tendencies, with several candidate intermetallic phases proposed around 6–7 at.% Cr. The relative stability of these ordered compounds is an open question. This task investigates three candidate structures – a body‑centered tetragonal Fe14Cr compound and two variants of Fe15Cr – by computing their formation enthalpies from first‑principles total energies. The goal is to determine which structure is thermodynamically most stable under the chosen computational protocol.

## Approach
First, reference total energies are computed for the pure bcc phases of Fe and Cr using the PBE exchange‑correlation functional and GBRV pseudopotentials in Quantum ESPRESSO. Then, three periodic supercells are constructed according to the structural descriptions in the literature:
- Fe14Cr: a 30‑atom body‑centered tetragonal cell (a = b = 6.4 Å, c = 8.6 Å) with Cr atoms placed at sites corresponding to the 7th and 8th neighbour shells of the underlying bcc lattice.
- Fe15Cr‑6nn: Cr atoms occupy a simple cubic sublattice with Cr–Cr distances in the 6th neighbour shell.
- Fe15Cr‑6/8nn: a modified Fe15Cr arrangement where Cr–Cr distances fall in the 6th and 8th neighbour shells.

For each compound, a static DFT calculation is run with the same functional and pseudopotentials used for the references. The formation enthalpy per atom is then obtained as
  ΔH = (E_total – N_Fe·E_Fe_bcc – N_Cr·E_Cr_bcc) / (N_Fe + N_Cr),
where E_total is the cell’s total energy and E_Fe_bcc, E_Cr_bcc are the per‑atom reference energies of the pure elements. The computed enthalpies allow a direct energetic comparison among the three candidate ordered phases.

## Reproduction target
Produce two scored artifacts:
1. `enthalpies.json` – a JSON file containing
   - the reference energies per atom for bcc Fe and bcc Cr (in eV) and the calculator used,
   - for each of the three structures, its name, composition, number of atoms, total energy (eV), and formation enthalpy per atom (meV/atom).
2. `results_summary.txt` – a plain‑text file that states which structure has the lowest formation enthalpy and briefly confirms its relative stability.

The formation enthalpies must be computed with Quantum ESPRESSO using the PBE functional and GBRV pseudopotentials, following the workflow described in the steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GBRV pseudopotentials (PBE): http://www.physics.rutgers.edu/gbrv/
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/
- Python 3: python3

## Workflow steps

### Step 1: Build and compute reference energies for bcc Fe and bcc Cr
- Role: process
- Action: Construct conventional bcc unit cells of pure Fe and pure Cr and perform DFT static total energy calculations with Quantum ESPRESSO using the PBE functional and GBRV pseudopotentials. Converge total energies with respect to k-point mesh and plane-wave cutoff.
- Evidence: `/app/outputs/reference_energies.json`

### Step 2: Build Fe14Cr and Fe15Cr supercells
- Role: process
- Action: Build the crystal structures of: (i) Fe14Cr body-centered tetragonal cell with a=b=6.4 Å, c=8.6 Å, containing 30 atoms, where Cr atoms occupy sites corresponding to the 7th and 8th neighbour shells of the underlying bcc lattice; (ii) Fe15Cr-6nn (Cr in 6th neighbour shell, simple cubic sublattice); (iii) Fe15Cr-6/8nn (Cr at 6th and 8th neighbour shells). Use the literature descriptions from the paper to determine atomic positions.
- Evidence: `/app/outputs/structures.log`

### Step 3: Run DFT total energy calculations for compounds
- Role: process
- Action: For each of the three structures, run a static DFT calculation using Quantum ESPRESSO with the same functional and pseudopotentials as in step 1, converging total energies.
- Evidence: `/app/outputs/dft_energies.json`

### Step 4: Compute and report formation enthalpies
- Role: scored (load-bearing)
- Action: Using the total energies from step 3 and the per-atom reference energies from step 1, compute the formation enthalpy per atom for each compound in meV/atom. Write the results to enthalpies.json with fields: reference_energies (Fe_bcc and Cr_bcc per atom in eV), and a compounds list where each entry contains name, composition, number_of_atoms, total_energy_eV, and formation_enthalpy_meV_per_atom.
- Output file: `/app/outputs/enthalpies.json`
- Format: json
- Contract: Object with keys: "reference_energies" (object with Fe_bcc_eV_per_atom (number), Cr_bcc_eV_per_atom (number), calculator (string)), "compounds" (array of objects with name (string), composition (string), number_of_atoms (int), total_energy_eV (float), formation_enthalpy_meV_per_atom (float)).
- Scoring: scored by hidden verifier

### Step 5: Write stability conclusion
- Role: scored
- Action: Based on the enthalpies computed in step 4, write a plain text file results_summary.txt stating which structure has the lowest formation enthalpy and confirming its relative stability.
- Output file: `/app/outputs/results_summary.txt`
- Format: txt
- Contract: Plain text containing the name of the most stable structure and a statement about its relative stability.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/enthalpies.json`
- `/app/outputs/results_summary.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### enthalpies.json
- path: `/app/outputs/enthalpies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Formation enthalpies of Fe14Cr and Fe15Cr candidate structures computed from DFT total energies relative to bcc Fe and bcc Cr references. The checker verifies that Fe14Cr has the lowest enthalpy (threshold_or_better).
- schema:
  - `type`: object
  - `required`:
    - `reference_energies`:
      - `type`: object
      - `required`:
        - `Fe_bcc_eV_per_atom`: number
        - `Cr_bcc_eV_per_atom`: number
        - `calculator`: string
    - `compounds`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`:
          - `name`: string
          - `composition`: string
          - `number_of_atoms`: integer
          - `total_energy_eV`: number
          - `formation_enthalpy_meV_per_atom`: number

### results_summary.txt
- path: `/app/outputs/results_summary.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Plain text file stating which structure is the most stable based on formation enthalpies. The checker performs a structural audit to ensure the correct compound is identified as most stable.
- schema:
  - `type`: text

Notes: Only the DFT formation enthalpy validation is scoped; AKMC simulations and SRO analyses are excluded. The agent must reproduce all structures and DFT calculations from scratch using open-source tools.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "enthalpies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "reference_energies": {
            "type": "object",
            "required": {
              "Fe_bcc_eV_per_atom": "number",
              "Cr_bcc_eV_per_atom": "number",
              "calculator": "string"
            }
          },
          "compounds": {
            "type": "array",
            "items": {
              "type": "object",
              "required": {
                "name": "string",
                "composition": "string",
                "number_of_atoms": "integer",
                "total_energy_eV": "number",
                "formation_enthalpy_meV_per_atom": "number"
              }
            }
          }
        }
      },
      "description": "Formation enthalpies of Fe14Cr and Fe15Cr candidate structures computed from DFT total energies relative to bcc Fe and bcc Cr references. The checker verifies that Fe14Cr has the lowest enthalpy (threshold_or_better)."
    },
    {
      "file": "results_summary.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "Plain text file stating which structure is the most stable based on formation enthalpies. The checker performs a structural audit to ensure the correct compound is identified as most stable."
    }
  ],
  "notes": "Only the DFT formation enthalpy validation is scoped; AKMC simulations and SRO analyses are excluded. The agent must reproduce all structures and DFT calculations from scratch using open-source tools."
}
```

## How you are scored
A hidden automated verifier scores each stage independently.
- The formation enthalpies you report in `enthalpies.json` are compared, within a tolerance that accounts for legitimate code‑to‑code differences, to the correct reference values derived from the paper’s DFT results. The ordering among the three structures is also checked: the most stable compound must be correctly identified.
- Your `results_summary.txt` is audited to confirm that it correctly names the lowest‑enthalpy structure and gives a consistent stability statement.
- Each scored stage contributes a weight; the final reward is a weighted sum. Simply writing a known number without executing the required DFT calculations will not satisfy the checker.
