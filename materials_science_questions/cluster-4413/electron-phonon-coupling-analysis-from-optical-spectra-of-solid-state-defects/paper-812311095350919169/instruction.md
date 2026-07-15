# Crystal-field parameter and phonon energy determination from lanthanide fluorescence spectra

## Problem background
Trivalent lanthanide ions in cubic elpasolite host lattices exhibit well‑resolved fluorescence spectra with sharp magnetic‑dipole transitions and vibronic sidebands. Analyzing these spectra with group theory and the first‑order crystal‑field Hamiltonian allows extraction of crystal‑field energy levels, the fourth‑order crystal‑field parameter B4^0, and the energies of odd‑parity vibrational modes (t1u, t2u). These quantities characterize the local electronic structure and electron‑phonon coupling, and their determination is the scientific objective of this task.

## Approach
Using the crystal‑field constants and the transition wavenumbers provided, the agent identifies the crystal‑field levels responsible for each observed magnetic‑dipole transition. The energy differences within the 7F2 multiplet are then combined with the operator‑equivalent factor to calculate the first‑order crystal‑field parameter B4^0 via the standard Oh Hamiltonian formula. Independently, the vibronic sideband offsets associated with the 5D0→7F2 transitions are analyzed: symmetric sideband pairs are matched, and the phonon mode assignments are derived by cross‑referencing with known odd‑parity vibrational frequencies of the analogous lattice Cs2KGdF6. The same group‑theoretical assignment procedure is applied to the Tb3+ transitions.

## Reproduction target
Given the transition wavenumbers and crystal‑field constants provided in the input files, produce:
- a table of assigned Eu3+ magnetic‑dipole transitions with wavenumber and assignment string,
- a numeric value for the first‑order crystal‑field parameter B4^0 (in cm⁻¹),
- a table of odd‑parity phonon mode energies for S6(t1u), S7(t1u), S8(t1u), and S10(t2u), and
- a table of assigned Tb3+ magnetic‑dipole transitions for the 5D4→7F5 and 5D4→7F3 regions.

## Assets

- Amberger_1980_spectral_data.json
- Crystal_field_constants.json

## Workflow steps

### Step 1: Assign Eu3+ magnetic dipole transitions
- Role: scored
- Action: Load the Eu3+ zero-phonon line wavenumbers and crystal‑field constants from the provided spectral data and constants files. Using group theoretical selection rules for Oh symmetry and the assignment pattern of the homologous chloro‑elpasolite, assign each observed magnetic dipole transition to a pair of crystal-field levels. Produce a CSV file containing each transition's label, wavenumber, and assignment.
- Output file: `/app/outputs/eu_assignment.csv`
- Format: csv
- Contract: {"required_columns": ["label", "wavenumber", "assignment"], "units": {"wavenumber": "cm^{-1}"}}
- Scoring: scored by hidden verifier

### Step 2: Compute B4^0 from 7F2 splitting
- Role: scored
- Action: From the energy differences of the 7F2 crystal‑field levels determined in the previous step and the provided operator‑equivalent factor, compute the first‑order crystal-field parameter B4^0 using the standard Oh Hamiltonian formula. Write the numeric value to a text file.
- Output file: `/app/outputs/b4_value.txt`
- Format: txt
- Contract: {"type": "text", "description": "Single line containing the numeric value of B4^0 in cm⁻¹"}
- Scoring: scored by hidden verifier

### Step 3: Extract odd-parity phonon energies from Eu3+ vibronic sidebands
- Role: scored (load-bearing)
- Action: Load the Eu3+ vibronic sideband offset data (displacements relative to the zero-phonon lines of the 5D0→7F2 transitions). Identify patterns of symmetric sidebands and isolate the contributions of the odd-parity vibrational modes. By comparison with literature data on Cs2KGdF6 and symmetry arguments, assign the sideband offsets to the t1u and t2u modes S6, S7, S8, S10. Produce a CSV file of mode labels and their energies.
- Output file: `/app/outputs/phonon_energies.csv`
- Format: csv
- Contract: {"required_columns": ["mode", "energy_cm1"], "units": {"energy_cm1": "cm^{-1}"}}
- Scoring: scored by hidden verifier

### Step 4: Assign Tb3+ magnetic dipole transitions
- Role: scored
- Action: Load the Tb3+ transition wavenumbers for the 5D4→7F5 and 5D4→7F3 regions. Using Oh selection rules and the prior detailed assignment for the homologous chloro‑elpasolite, assign each observed band to a crystal-field transition. Produce a CSV file containing all bands listed in the paper’s table, with band number/label, wavenumber, and assignment.
- Output file: `/app/outputs/tb_assignment.csv`
- Format: csv
- Contract: {"required_columns": ["label", "wavenumber", "assignment"], "units": {"wavenumber": "cm^{-1}"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eu_assignment.csv`
- `/app/outputs/b4_value.txt`
- `/app/outputs/phonon_energies.csv`
- `/app/outputs/tb_assignment.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eu_assignment.csv
- path: `/app/outputs/eu_assignment.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Assigned Eu3+ zero-phonon magnetic dipole transitions with label, wavenumber, and assignment string.
- schema:
  - `type`: table
  - `required_columns`: `label`, `wavenumber`, `assignment`
  - `units`:
    - `wavenumber`: cm^{-1}

### b4_value.txt
- path: `/app/outputs/b4_value.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: First‑order crystal-field parameter B4^0 computed from the 7F2 splitting.
- schema:
  - `type`: text
  - `description`: Single line containing the numeric value of B4^0 in cm⁻¹.

### phonon_energies.csv
- path: `/app/outputs/phonon_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Energies of odd‑parity vibrational modes S6(t1u), S7(t1u), S8(t1u), S10(t2u) derived from vibronic sidebands.
- schema:
  - `type`: table
  - `required_columns`: `mode`, `energy_cm1`
  - `units`:
    - `energy_cm1`: cm^{-1}

### tb_assignment.csv
- path: `/app/outputs/tb_assignment.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Assigned Tb3+ magnetic dipole transitions (5D4→7F5 and 5D4→7F3) with band label, wavenumber, and assignment string.
- schema:
  - `type`: table
  - `required_columns`: `label`, `wavenumber`, `assignment`
  - `units`:
    - `wavenumber`: cm^{-1}

Notes: All outputs are compared against hidden paper‑reported values with appropriate tolerances (±2 cm⁻¹ for transition wavenumbers, ±3 cm⁻¹ for B4^0 and phonon energies). Assignments are matched case‑insensitively.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eu_assignment.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "label",
          "wavenumber",
          "assignment"
        ],
        "units": {
          "wavenumber": "cm^{-1}"
        }
      },
      "description": "Assigned Eu3+ zero-phonon magnetic dipole transitions with label, wavenumber, and assignment string."
    },
    {
      "file": "b4_value.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single line containing the numeric value of B4^0 in cm⁻¹."
      },
      "description": "First‑order crystal-field parameter B4^0 computed from the 7F2 splitting."
    },
    {
      "file": "phonon_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "energy_cm1"
        ],
        "units": {
          "energy_cm1": "cm^{-1}"
        }
      },
      "description": "Energies of odd‑parity vibrational modes S6(t1u), S7(t1u), S8(t1u), S10(t2u) derived from vibronic sidebands."
    },
    {
      "file": "tb_assignment.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "label",
          "wavenumber",
          "assignment"
        ],
        "units": {
          "wavenumber": "cm^{-1}"
        }
      },
      "description": "Assigned Tb3+ magnetic dipole transitions (5D4→7F5 and 5D4→7F3) with band label, wavenumber, and assignment string."
    }
  ],
  "notes": "All outputs are compared against hidden paper‑reported values with appropriate tolerances (±2 cm⁻¹ for transition wavenumbers, ±3 cm⁻¹ for B4^0 and phonon energies). Assignments are matched case‑insensitively."
}
```

## How you are scored
Each output file listed in the workflow steps is independently scored by a hidden verifier. The verifier compares your submitted wavenumbers, assignments, parameter value, and phonon energies against reference values using appropriate tolerances, and assigns a partial score to every stage. The final reward is the weighted sum of the stage scores. Submitting correct, physically consistent values derived from genuine analysis is required; reporting paper‑level numbers without proper derivation will not achieve the required stage‑by‑stage accuracy.
