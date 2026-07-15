# Electronic Structure and Vibrational Properties of Substituted Si Clathrates

## Problem background
The electronic structure and vibrational properties of type-I silicon clathrates Ba8Si46 and its silver- and gold-substituted counterparts are important for understanding superconductivity in these materials. Substituting framework silicon with noble metals is known to change the superconducting critical temperature, but the roles of the electronic density of states near the Fermi level, phonon mode contributions, and electron-phonon coupling remain subjects of ongoing investigation. First-principles calculations can disentangle these contributions by computing the electronic DOS, zone-center phonon frequencies, and the electron-phonon coupling parameter λ for the pure and substituted clathrates, providing a microscopic picture of the interplay between guest barium atoms, framework substitution, and superconducting behaviour.

## Approach
Use first-principles density-functional theory as implemented in Quantum ESPRESSO with PBE-GGA pseudopotentials. Construct the initial crystal structures of Ba8Si46, Ba8Ag6Si40, and Ba8Au6Si40 from known experimental lattice constants and Wyckoff positions. Perform geometry optimizations to obtain minimum-energy structures. From the optimized structures compute the electronic density of states (DOS) and extract the total DOS at the Fermi level for each compound. Compute phonon frequencies at the Brillouin-zone center (Γ point) using density-functional perturbation theory (DFPT) or the finite-displacement method with Phonopy, and identify characteristic vibrational modes: the highest-frequency optical mode (dominated by Si framework stretching) and the barium-dominated vibrations in the large and small cages. Finally, compute the electron-phonon coupling constant λ for Ba8Si46 at the zone center using DFPT. The workflow produces a set of numerical outputs that characterise the electronic and vibrational properties of the three compounds.

## Reproduction target
Produce the following computational results for Ba8Si46, Ba8Ag6Si40, and Ba8Au6Si40:
- The total electronic density of states at the Fermi level, N(EF), in states/eV per unit cell, for each compound.
- The highest optical phonon frequency at Γ (in cm⁻¹) for each compound.
- The characteristic vibrational frequencies of Ba atoms in the large cages and in the small cages (in cm⁻¹) for each compound, extracted from zone-center phonon eigenvectors.
- The zone-center electron-phonon coupling constant λ for Ba8Si46.
All results must be written to the specified output files under `/app/outputs` following the output contracts defined below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP Efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/package/efficiency
- Crystal structure of Ba8Si46 (COD #1009002): http://www.crystallography.net/cod/1009002.html

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Perform DFT geometry optimization for Ba8Si46, Ba8Ag6Si40, and Ba8Au6Si40 using Quantum ESPRESSO with PBE-GGA pseudopotentials. Save optimized lattice vectors and atomic coordinates.
- Evidence: `/app/outputs/optimized_structures.json`

### Step 2: Electronic DOS at Fermi level
- Role: scored
- Action: Using the optimized structures, run self-consistent DFT calculations and compute the electronic density of states (DOS). Extract the total DOS at the Fermi level N(EF) in states/eV per unit cell for Ba8Si46, Ba8Ag6Si40, and Ba8Au6Si40.
- Output file: `/app/outputs/dos_fermi_levels.csv`
- Format: csv
- Contract: compound (string), N_EF (float, states/eV/unit cell), description (string)
- Scoring: scored by hidden verifier

### Step 3: Zone-center phonon calculation
- Role: process
- Action: Using the optimized structures, compute the phonon frequencies at the Gamma point for Ba8Si46, Ba8Ag6Si40, and Ba8Au6Si40 via DFPT (Quantum ESPRESSO ph.x) or finite displacements (Phonopy). Save the full list of frequencies and mode characters.
- Evidence: `/app/outputs/phonon_frequencies.json`

### Step 4: Highest optical phonon frequency
- Role: scored
- Action: From the phonon frequencies computed in step_03, identify the highest frequency mode for each compound. Report the value in cm⁻¹.
- Output file: `/app/outputs/highest_phonon_frequencies.csv`
- Format: csv
- Contract: compound (string), frequency (float, cm⁻¹)
- Scoring: scored by hidden verifier

### Step 5: Ba cage vibrations
- Role: scored
- Action: Using the phonon eigenvectors from step_03, identify the vibrational modes dominated by Ba atoms in the large cages and in the small cages for each compound. For each compound report the characteristic frequency (peak position) for each cage type.
- Output file: `/app/outputs/ba_vibration_frequencies.csv`
- Format: csv
- Contract: compound (string), cage_type (string: 'large' or 'small'), frequency (float, cm⁻¹)
- Scoring: scored by hidden verifier

### Step 6: Electron-phonon coupling constant for Ba8Si46
- Role: scored (load-bearing)
- Action: For the optimized Ba8Si46 structure, compute the electron-phonon coupling parameter λ at the zone center using Quantum ESPRESSO's DFPT electron-phonon module. Output the total λ.
- Output file: `/app/outputs/electron_phonon_lambda.json`
- Format: json
- Contract: {"compound": "Ba8Si46", "lambda": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_fermi_levels.csv`
- `/app/outputs/highest_phonon_frequencies.csv`
- `/app/outputs/ba_vibration_frequencies.csv`
- `/app/outputs/electron_phonon_lambda.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_fermi_levels.csv
- path: `/app/outputs/dos_fermi_levels.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Electronic DOS at Fermi level for Ba8Si46, Ba8Ag6Si40, and Ba8Au6Si40.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `N_EF`, `description`
  - `units`:
    - `N_EF`: states/eV/unit cell

### highest_phonon_frequencies.csv
- path: `/app/outputs/highest_phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Highest optical phonon frequency for each compound.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `frequency`
  - `units`:
    - `frequency`: cm⁻¹

### ba_vibration_frequencies.csv
- path: `/app/outputs/ba_vibration_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Characteristic Ba vibrational frequencies in large and small cages for each compound.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `cage_type`, `frequency`
  - `units`:
    - `frequency`: cm⁻¹

### electron_phonon_lambda.json
- path: `/app/outputs/electron_phonon_lambda.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electron-phonon coupling constant λ for Ba8Si46.
- schema:
  - `type`: object
  - `required`:
    - `compound`: string
    - `lambda`: number

Notes: All scored quantities are compared against hidden gold values from the paper with appropriate tolerances; the ordering of N_EF and shifts in frequencies are also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_fermi_levels.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "N_EF",
          "description"
        ],
        "units": {
          "N_EF": "states/eV/unit cell"
        }
      },
      "description": "Electronic DOS at Fermi level for Ba8Si46, Ba8Ag6Si40, and Ba8Au6Si40."
    },
    {
      "file": "highest_phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "frequency"
        ],
        "units": {
          "frequency": "cm⁻¹"
        }
      },
      "description": "Highest optical phonon frequency for each compound."
    },
    {
      "file": "ba_vibration_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "cage_type",
          "frequency"
        ],
        "units": {
          "frequency": "cm⁻¹"
        }
      },
      "description": "Characteristic Ba vibrational frequencies in large and small cages for each compound."
    },
    {
      "file": "electron_phonon_lambda.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "compound": "string",
          "lambda": "number"
        }
      },
      "description": "Electron-phonon coupling constant λ for Ba8Si46."
    }
  ],
  "notes": "All scored quantities are compared against hidden gold values from the paper with appropriate tolerances; the ordering of N_EF and shifts in frequencies are also verified."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that checks each scored output file independently. For each scored artifact the verifier compares your computed values against reference expectations (e.g., correct ordering of N(EF) among compounds, approximate high-frequency phonon values, and a reasonable λ for Ba8Si46) with appropriate tolerances that account for genuine differences between DFT implementations and pseudopotential choices. The per-stage scores are then combined with assigned weights to produce a final overall reward between 0 and 1. Simply reporting the published numbers is not sufficient; the verifier expects results obtained by genuinely executing the computational pipeline described in the workflow steps.
