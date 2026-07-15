# First-Principles DFT Band Gap and Orbital Character Analysis for Cs3Bi2Br9

## Problem background
Cs3Bi2Br9 is a layered vacancy-ordered triple perovskite with unusual optoelectronic properties, including a sharp exciton peak and strong luminescence at room temperature. Understanding its electronic structure — specifically the band gap values and the atomic orbital makeup of the band edges — is central to explaining these properties and designing related materials. Density functional theory (DFT) with hybrid functionals and spin-orbit coupling can provide reliable predictions of these electronic features, but the concrete numbers depend on the chosen exchange-correlation functional, pseudopotentials, and computational parameters. In this task, you will compute the electronic band structure of the room-temperature trigonal phase of Cs3Bi2Br9 and extract the band gaps and band-edge orbital characters.

## Approach
Use a first-principles DFT code that supports the HSE06 hybrid functional and spin-orbit coupling (e.g., Quantum ESPRESSO). Starting from the published crystal structure (space group P-3m1), set up a self-consistent field calculation to obtain the ground-state charge density. Then perform a non-self-consistent band structure calculation along a high-symmetry path that includes the Γ and A k-points. Analyze the resulting band energies to determine the energies of the valence band maximum and conduction band minimum, and compute the indirect band gap (Γ → A) and the direct band gap (Γ → Γ). Separately, project the Kohn-Sham wavefunctions onto atomic orbitals to obtain orbital-resolved contributions. Identify which atomic species and orbital types dominate at the valence band top and conduction band bottom.

## Reproduction target
Produce two output files:

1. `band_gaps.json` containing the indirect band gap (in eV) and direct band gap (in eV) computed from your HSE06+SOC band structure.
2. `band_edge_character.json` containing string descriptions of the dominant orbital character of the valence band maximum and the conduction band minimum (e.g., using notations like "Bi 6s + Br 4p" or "Bi p").

## Assets

- Cs3Bi2Br9 crystal structure (room-temperature trigonal P-3m1)
- Quantum ESPRESSO (or other DFT code supporting HSE06 and SOC): quantum-espresso
- PBE pseudopotentials for Cs, Bi, Br (with SOC support): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare crystal structure input
- Role: process
- Action: Obtain the room-temperature trigonal P-3m1 crystal structure of Cs3Bi2Br9 from a public database and prepare a DFT input file (lattice parameters, atomic positions).
- Evidence: `/app/outputs/structure_input.txt`

### Step 2: HSE06+SOC self-consistent field calculation
- Role: process
- Action: Perform a self-consistent field DFT calculation using the HSE06 hybrid functional with spin-orbit coupling included, using appropriate k-point mesh and plane-wave energy cutoffs.
- Evidence: `/app/outputs/scf_output.log`

### Step 3: Band structure calculation
- Role: process
- Action: Perform a non-self-consistent band structure calculation along a high-symmetry k-path that includes the Gamma and A points, using the charge density from the SCF step.
- Evidence: `/app/outputs/bands.dat`

### Step 4: Orbital projection analysis
- Role: process
- Action: Project the Kohn-Sham wavefunctions onto atomic orbitals to obtain orbital-resolved band weights or projected density of states.
- Evidence: `/app/outputs/projwfc_output.dat`

### Step 5: Extract band gaps
- Role: scored (load-bearing)
- Action: Analyze the band structure to locate the valence band maximum and conduction band minimum at the Gamma point and A point, compute the indirect gap (Gamma to A) and direct gap (Gamma to Gamma), and write the values in eV.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: { "indirect_gap_eV": number, "direct_gap_eV": number }
- Scoring: scored by hidden verifier

### Step 6: Extract band edge orbital character
- Role: scored (load-bearing)
- Action: From the orbital projection data, determine the dominant atomic orbitals contributing to the valence band maximum and conduction band minimum, and write descriptive strings.
- Output file: `/app/outputs/band_edge_character.json`
- Format: json
- Contract: { "vbm_character": string, "cbm_character": string }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`
- `/app/outputs/band_edge_character.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Indirect band gap (Gamma to A) and direct band gap (Gamma to Gamma) computed from HSE06+SOC DFT band structure.
- schema:
  - `type`: object
  - `required`:
    - `indirect_gap_eV`: number (eV)
    - `direct_gap_eV`: number (eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `indirect_gap_eV`: eV
    - `direct_gap_eV`: eV

### band_edge_character.json
- path: `/app/outputs/band_edge_character.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Dominant orbital character of the valence band maximum and conduction band minimum, e.g., Bi 6s and Br 4p for VBM, Bi p for CBM.
- schema:
  - `type`: object
  - `required`:
    - `vbm_character`: string
    - `cbm_character`: string
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The paper also reports optical absorption spectrum and phonon dispersion; these are not required for the core electronic structure reproduction. The agent must use HSE06 functional with spin-orbit coupling.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "indirect_gap_eV": "number (eV)",
          "direct_gap_eV": "number (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "indirect_gap_eV": "eV",
          "direct_gap_eV": "eV"
        }
      },
      "description": "Indirect band gap (Gamma to A) and direct band gap (Gamma to Gamma) computed from HSE06+SOC DFT band structure."
    },
    {
      "file": "band_edge_character.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "vbm_character": "string",
          "cbm_character": "string"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Dominant orbital character of the valence band maximum and conduction band minimum, e.g., Bi 6s and Br 4p for VBM, Bi p for CBM."
    }
  ],
  "notes": "The paper also reports optical absorption spectrum and phonon dispersion; these are not required for the core electronic structure reproduction. The agent must use HSE06 functional with spin-orbit coupling."
}
```

## How you are scored
A hidden verifier will read your `band_gaps.json` and `band_edge_character.json`. The band gap values will be compared against reference values that correspond to the paper's reported DFT results; tolerance is applied to accommodate differences in pseudopotentials and computational settings. The orbital character strings are checked for the correct atomic elements and orbital types (case-insensitive, so "Bi p" and "BI P" are both acceptable). Each output file carries a fraction of the total reward; you must produce both correctly to earn full credit. The verifier does not award credit for merely reproducing the numbers stated in this instruction — you must execute the DFT workflow and extract the results from the calculations.
