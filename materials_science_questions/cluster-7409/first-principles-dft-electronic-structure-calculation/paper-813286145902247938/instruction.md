# First-principles DFT+U analysis of Bi substitutional defect in anatase TiO2

## Problem background
Anatase titanium dioxide (TiO2) is a promising photocatalyst, but its activity is limited to ultraviolet light. Doping with bismuth (Bi) has been proposed to extend absorption into the visible range, yet experimental reports disagree on whether Bi actually substitutes for titanium in the anatase lattice and whether the doped material exhibits visible-light absorption. First-principles electronic structure calculations can help resolve these questions by directly computing the defect formation energy and the position of any impurity band inside the gap. In this task you will perform such calculations to determine whether Bi substitution is thermodynamically favourable and what electronic states it introduces.

## Approach
You will use plane-wave density functional theory (DFT) with the generalized-gradient approximation of Perdew–Burke–Ernzerhof (GGA-PBE) and Dudarev's rotationally invariant Hubbard U correction applied to the Ti 3d states (GGA+U). The calculation employs an open-source DFT code such as Quantum ESPRESSO. Starting from the known anatase crystal structure, you construct a 2×2×2 supercell and replace one Ti atom with Bi. For both the pure and Bi-doped supercells you relax the geometry and compute the total density of electronic states (DOS) at two different U−J values (3.2 eV and 7.2 eV). From the DOS of the doped system you extract the energy of the in-gap defect band peak relative to the valence band maximum. To compute the neutral Bi³⁺ substitutional defect formation energy you also need the total energies of the reference phases: metallic Ti, metallic Bi, the O₂ molecule, anatase TiO₂, and Bi₂O₃. Using these energies you set up the thermodynamic equilibrium between the anatase host, the Bi₂O₃ phase, and the oxygen reservoir. Chemical potentials of Ti, Bi, and O are derived through a formation-energy cycle, and the defect formation energy is obtained as the difference between the total energies of the supercell containing the defect and the pure supercell, plus the chemical potentials of the exchanged atoms. The complete thermodynamic formalism is described in the literature; you must implement it yourself from the standard defect-formation energy expression.

## Reproduction target
Produce two scored deliverables: (1) the in-gap defect band energies (eV) above the valence band maximum for the Bi-doped anatase supercell at U−J = 3.2 eV and U−J = 7.2 eV, and (2) the neutral Bi³⁺ substitutional defect formation energy (eV). Output them as JSON files with the exact fields specified in the output contract.

## Assets

- Anatase TiO2 crystal structure: ICSD #9852 or Materials Project mp-390
- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/download
- PBE pseudopotentials for Ti, O, Bi: https://www.materialscloud.org/discover/sssp/table
- Crystal structures of reference phases (Ti, Bi, O2, anatase TiO2, Bi2O3): https://materialsproject.org/

## Workflow steps

### Step 1: Supercell construction
- Role: process
- Action: Construct a 2×2×2 supercell of anatase from the primitive Ti2O4 cell. Then create a Bi-doped supercell by replacing one Ti atom with Bi.
- Evidence: none

### Step 2: DFT reference calculation for pure anatase
- Role: process
- Action: Perform DFT+U calculation on the pure anatase supercell using GGA-PBE functional with Dudarev's DFT+U on Ti 3d (U-J = 3.2 eV and 7.2 eV). Relax atomic positions and cell volume until convergence. Compute the total density of states (DOS) and identify the valence band maximum (VBM) for each U-J value. Record the VBM energies for use as reference.
- Evidence: none

### Step 3: DFT for Bi-doped anatase and extraction of in-gap band positions
- Role: scored
- Action: Perform DFT+U calculation on the Bi-doped supercell using the same settings (U-J = 3.2 eV and 7.2 eV). After relaxation, compute the total DOS. For each U-J value, read the energy of the in-gap defect band peak relative to the VBM obtained in step 2. Write a JSON file 'band_positions.json' containing two keys: 'U-J_3.2' and 'U-J_7.2' with the band energies in eV.
- Output file: `/app/outputs/band_positions.json`
- Format: json
- Contract: {'U-J_3.2': float, 'U-J_7.2': float}
- Scoring: scored by hidden verifier

### Step 4: DFT total energies of reference phases
- Role: process
- Action: Construct unit cells for Ti metal, Bi metal, the O2 molecule, anatase TiO2, and Bi2O3. Perform DFT+U calculations under the same PBE functional and plane-wave cutoff to obtain the ground-state total energy of each phase. Relax structures appropriately (no U correction on the O2 molecule). Record the total energies.
- Evidence: none

### Step 5: Compute defect formation energy
- Role: scored (load-bearing)
- Action: Using the total energies from steps 2, 3 and 4, derive the chemical potentials of Ti, Bi, and O via the thermodynamic formation-energy formalism. Then calculate the neutral Bi³⁺ substitutional defect formation energy using the paper's equation for formation energy. Write a JSON file 'formation_energy.json' with key 'Bi_plus3_defect_formation_energy_eV' and the energy in eV.
- Output file: `/app/outputs/formation_energy.json`
- Format: json
- Contract: {'Bi_plus3_defect_formation_energy_eV': float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_positions.json`
- `/app/outputs/formation_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_positions.json
- path: `/app/outputs/band_positions.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: In-gap defect band energies above the valence-band maximum for Bi-doped anatase at U-J=3.2 eV and 7.2 eV.
- schema:
  - `type`: object
  - `required`:
    - `U-J_3.2`: float (energy in eV)
    - `U-J_7.2`: float (energy in eV)

### formation_energy.json
- path: `/app/outputs/formation_energy.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Neutral Bi³⁺ substitutional defect formation energy in anatase.
- schema:
  - `type`: object
  - `required`:
    - `Bi_plus3_defect_formation_energy_eV`: float (energy in eV)

Notes: The two scored quantities are the in-gap band positions at two U-J values and the defect formation energy. The hidden checker will compare the reported values to the paper's computed values with appropriate tolerances that account for toolchain differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_positions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "U-J_3.2": "float (energy in eV)",
          "U-J_7.2": "float (energy in eV)"
        }
      },
      "description": "In-gap defect band energies above the valence-band maximum for Bi-doped anatase at U-J=3.2 eV and 7.2 eV."
    },
    {
      "file": "formation_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Bi_plus3_defect_formation_energy_eV": "float (energy in eV)"
        }
      },
      "description": "Neutral Bi³⁺ substitutional defect formation energy in anatase."
    }
  ],
  "notes": "The two scored quantities are the in-gap band positions at two U-J values and the defect formation energy. The hidden checker will compare the reported values to the paper's computed values with appropriate tolerances that account for toolchain differences."
}
```

## How you are scored
Your outputs will be checked by a hidden verifier that compares the numeric values you report in `band_positions.json` and `formation_energy.json` to reference values. Credit is awarded based on how close your computed results are to the expected quantities; the reward is monotonic (the closer you are, the higher the score). The verifier does not re-run the DFT simulation; it trusts that you have carried out the calculations honestly. Reporting the correct numbers is not enough if they cannot be obtained from a genuine DFT run — the verifier's tolerances account for toolchain differences, so you should focus on executing the procedure accurately rather than trying to guess the target.
