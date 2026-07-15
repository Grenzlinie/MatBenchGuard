# Computational Phonon Analysis of Ti3C2O2 MXene

## Problem background
Plasmonic MXenes are 2D transition metal carbides with unique electronic and vibrational properties. Understanding how photoexcited electrons transfer energy to the crystal lattice (phonons) is critical for designing materials with efficient energy transport and conversion. In particular, the question of whether nonthermal electrons can directly couple to specific coherent phonon modes without undergoing electron-electron scattering remains open. This task investigates, through first-principles calculations, the orbital-resolved electronic band structure and phonon dispersion of a representative MXene monolayer (Ti3C2O2) to understand the structural and symmetry factors that determine electron-phonon coupling selectivity.

## Approach
The computational approach uses hybrid-functional density functional theory (DFT) to obtain the electronic band structure and orbital-projected density of states (fatbands) of a Ti3C2O2 monolayer, a common model for the experimentally studied Ti3C2Tx. The calculation identifies the energies and principal orbital characters of several band features near the Fermi level that are involved in electronic transitions at different pump wavelengths. In parallel, phonon dispersion and phonon density of states are computed using a finite-displacement supercell method coupled with a phonon post-processing tool (PHONOPY). The computed phonon frequencies and the relative phonon DOS of the out-of-plane (A1g) and in-plane (Eg) modes provide a microscopic basis for understanding the observed coupling strengths. The combined electronic and phonon results allow one to correlate orbital symmetry and phonon density of states with the selectivity of electron-phonon coupling.

## Reproduction target
Perform the following computational study on a Ti3C2O2 monolayer:
- Relax the crystal structure using DFT (geometry optimization).
- Compute the electronic band structure with a hybrid functional and extract the energies (eV, relative to the Fermi level) of four bands labelled a, b, c, and d, as well as the dominant Ti d-orbital characters for bands c and d.
- Compute the phonon dispersion and phonon density of states (DOS) using a finite-displacement method and PHONOPY. Extract the frequencies (cm⁻¹) of the A1g and Eg vibrational modes and provide a qualitative comparison of their phonon DOS (e.g., which mode has higher DOS).
The results must be written to the JSON files `/app/outputs/electronic_structure.json` and `/app/outputs/phonon_analysis.json` as specified in the workflow steps.

## Assets

- Quantum ESPRESSO DFT package: https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Ti3C2O2 monolayer crystal structure

## Workflow steps

### Step 1: Obtain and relax Ti3C2O2 monolayer structure
- Role: process
- Action: Construct the Ti3C2O2 monolayer structure and perform a DFT geometry optimization until atomic forces are converged. Save the relaxed structure for downstream calculations.
- Evidence: `/app/outputs/relaxed_structure.cif`

### Step 2: Compute orbital-resolved electronic band structure
- Role: scored (load-bearing)
- Action: Perform a hybrid-functional DFT calculation on the relaxed Ti3C2O2 structure to obtain the band structure and orbital-projected density of states (fatbands). Extract the energies (eV relative to the Fermi level) of bands labelled a, b, c, d and the dominant Ti d-orbital characters for bands c and d. Write the results to electronic_structure.json.
- Output file: `/app/outputs/electronic_structure.json`
- Format: json
- Contract: JSON object with schema: bands (object with keys a,b,c,d each holding energy in eV), orbital_characters (object with keys c and d, each a list of dominant orbital strings, e.g., ["d_xy","d_xz","d_z2"])
- Scoring: scored by hidden verifier

### Step 3: Compute phonon dispersion and DOS
- Role: scored
- Action: Using the relaxed Ti3C2O2 structure, compute force constants via a finite-displacement method in a supercell, then calculate the phonon dispersion and phonon density of states with PHONOPY. Extract the frequencies (cm⁻¹) of the A1g and Eg modes and provide a comparison of their phonon DOS (A1g higher than Eg). Write the results to phonon_analysis.json.
- Output file: `/app/outputs/phonon_analysis.json`
- Format: json
- Contract: JSON object with schema: phonon_modes (object with keys A1g and Eg each holding frequency in cm⁻¹), phonon_DOS_comparison (string, e.g., "A1g higher than Eg")
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_structure.json`
- `/app/outputs/phonon_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_structure.json
- path: `/app/outputs/electronic_structure.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Orbital-resolved electronic band energies and dominant Ti d-orbital contributions for Ti3C2O2.
- schema:
  - `type`: object
  - `required`:
    - `bands`: object with keys a,b,c,d each a number (energy in eV)
    - `orbital_characters`: object with keys c and d each a list of strings

### phonon_analysis.json
- path: `/app/outputs/phonon_analysis.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Phonon frequencies of A1g and Eg modes and the qualitative phonon DOS comparison.
- schema:
  - `type`: object
  - `required`:
    - `phonon_modes`: object with keys A1g and Eg each a number (frequency in cm⁻¹)
    - `phonon_DOS_comparison`: string

Notes: The hidden checker compares the agent's reported band energies (relative to Fermi level) and dominant orbital characters against the paper's HSE06-computed values with reasonable tolerances. Phonon frequencies and the DOS comparison are similarly checked against the paper's reported results. Tolerances accommodate differences due to pseudopotential/functional choices.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "bands": "object with keys a,b,c,d each a number (energy in eV)",
          "orbital_characters": "object with keys c and d each a list of strings"
        }
      },
      "description": "Orbital-resolved electronic band energies and dominant Ti d-orbital contributions for Ti3C2O2."
    },
    {
      "file": "phonon_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "phonon_modes": "object with keys A1g and Eg each a number (frequency in cm⁻¹)",
          "phonon_DOS_comparison": "string"
        }
      },
      "description": "Phonon frequencies of A1g and Eg modes and the qualitative phonon DOS comparison."
    }
  ],
  "notes": "The hidden checker compares the agent's reported band energies (relative to Fermi level) and dominant orbital characters against the paper's HSE06-computed values with reasonable tolerances. Phonon frequencies and the DOS comparison are similarly checked against the paper's reported results. Tolerances accommodate differences due to pseudopotential/functional choices."
}
```

## How you are scored
After you finish, a hidden verifier independently evaluates your submitted artifacts. It checks each scored output file against reference criteria derived from the scientific requirements of the task. The total reward is a weighted combination of the scores for the individual stages (see 'Workflow steps'). You must produce the required files by actually executing the calculations; merely reporting expected values without running the full pipeline will not satisfy the scoring. Artifacts that are missing, malformed, or contain incorrect quantities will lose credit.
