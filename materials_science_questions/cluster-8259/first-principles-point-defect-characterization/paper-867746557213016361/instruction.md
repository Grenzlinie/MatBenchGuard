# First-principles point defect characterization using QM/MM embedded-cluster method

## Problem background
Wide-band-gap semiconductor GaN is essential for blue light-emitting diodes and power electronics. Despite its technological importance, achieving stable p-type conductivity has proved difficult, especially when doping with divalent metals such as Mg. The material is natively n-type, and point defects – particularly nitrogen vacancies (V_N) and substitutional Mg on a Ga site (Mg_Ga) – are believed to play a central role in compensating free holes and in the characteristic photoluminescence (PL) spectra observed at low doping levels. An accurate understanding of their formation and ionisation energetics is therefore critical to explain the observed electronic and optical behaviour of lightly doped GaN.

## Approach
This task uses an embedded-cluster quantum‑mechanical/molecular‑mechanical (QM/MM) method to compute defect total energies. A QM region of approximately 100 atoms is described by hybrid density functional theory (DFT) with the BB1K functional (42 % exact exchange) and a triple‑zeta‑plus‑polarisation Gaussian basis set. The QM cluster is surrounded by a much larger MM region that employs polarisable‑shell interatomic potentials for GaN, accurately reproducing the dielectric, elastic, and structural response of the host. This approach avoids supercell image‑charge artefacts and yields well‑defined reference levels for ionisation energies. Three systems are treated: bulk GaN (to determine the valence‑band maximum and total energy reference), Mg_Ga defects with the hole localised either on an axial or a basal nitrogen, and nitrogen vacancies V_N in charge states +3, +1, 0, and –1. From the computed total energies, formation energies are derived as a function of Fermi energy under N‑rich chemical potentials, and vertical ionisation energies are obtained as energy differences between different charge states at fixed geometry. The resulting numbers are directly comparable with experimental PL transitions and defect‑characterisation data.

## Reproduction target
The goal is to compute four quantities that characterise the Mg_Ga and V_N defects in GaN:

1. **Mg_Ga^0 formation energy:** the formation energy of neutral Mg_Ga with the hole localised on an axial N, under N‑rich conditions, reported in eV.
2. **V_N charge‑state crossing:** the Fermi energy (above the valence‑band maximum) at which the formation energies of V_N^+ and V_N^3+ are equal, in eV.
3. **V_N shallow donor vertical ionisation energy:** the vertical ionisation energy (ΔE between V_N^0 and V_N^+ at fixed geometry) relative to the conduction‑band minimum, in meV.
4. **Mg_Ga photoluminescence (PL) transitions:** vertical ionisation energies for the basal‑plane and axial hole configurations, each for a singlet final state (and optionally for a triplet final state), reported in a CSV file with columns configuration, final_state, energy_eV.

These values must be obtained from the QM/MM DFT workflow described below and written to the specified output files under `/app/outputs`. They represent the main experimentally accessible quantities associated with compensation and luminescence in lightly Mg‑doped GaN.

## Assets

- QM/MM electronic structure code (e.g., CP2K, ChemShell): https://www.cp2k.org
- BB1K hybrid exchange-correlation functional: 10.1021/jp049590d
- Triple-zeta-plus-polarisation Gaussian basis for Ga, N, Mg: https://www.basissetexchange.org
- Polarisable-shell interatomic potentials for GaN: 10.1098/rsta.2010.0115
- GaN crystallographic structure parameters

## Workflow steps

### Step 1: Construct QM/MM embedded-cluster models
- Role: process
- Action: Construct the QM/MM embedded cluster for bulk GaN and for each defect (Mg_Ga with axial and basal hole, V_N in charge states +3, +1, 0, -1) using the polarisable-shell MM environment and a QM region of ~100 atoms. Save the resulting input structures for DFT calculations.
- Evidence: `/app/outputs/cluster_models.xyz`

### Step 2: DFT calculation of bulk GaN reference
- Role: process
- Action: Perform QM/MM hybrid DFT total energy calculation on the bulk GaN embedded cluster using BB1K functional and TZP basis set. Extract the total energy and the valence band maximum energy relative to the quasi-vacuum level. Save these reference values.
- Evidence: `/app/outputs/bulk_energies.json`

### Step 3: DFT calculations for Mg_Ga defect
- Role: process
- Action: Run QM/MM DFT total energy calculations for neutral and positively charged Mg_Ga defects with the hole localised on an axial N and on a basal N (four configurations: neutral/charged × axial/basal). Save the total energies.
- Evidence: `/app/outputs/MgGa_energies.json`

### Step 4: DFT calculations for V_N defect
- Role: process
- Action: Run QM/MM DFT total energy calculations for the nitrogen vacancy in charge states +3, +1, 0, and -1 (including geometry relaxation for relevant states). Save the total energies.
- Evidence: `/app/outputs/VN_energies.json`

### Step 5: Compute Mg_Ga^0 formation energy
- Role: scored (load-bearing)
- Action: From the bulk and Mg_Ga energies, with N-rich chemical potentials, calculate the formation energy of neutral Mg_Ga (axial hole configuration) using the standard defect formation energy formula with Fermi energy set appropriately. Write the value in eV.
- Output file: `/app/outputs/step_01_MgGa_formation_energy.txt`
- Format: txt
- Contract: Single number: formation energy in eV. Format: '<value> eV'.
- Scoring: scored by hidden verifier

### Step 6: Compute V_N charge-state crossing
- Role: scored (load-bearing)
- Action: Using the V_N energies for +3 and +1 states and the bulk reference, determine the Fermi energy (above VBM) at which the formation energies of V_N^+ and V_N^3+ intersect. Write the value in eV.
- Output file: `/app/outputs/step_02_VN_crossing.txt`
- Format: txt
- Contract: Single number: Fermi energy in eV above VBM. Format: '<value> eV'.
- Scoring: scored by hidden verifier

### Step 7: Compute V_N shallow donor vertical IE
- Role: scored (load-bearing)
- Action: From V_N total energies for neutral and +1 states (fixed geometry), calculate the vertical ionisation energy of V_N^0 and express it relative to the CBM. Write the value in meV.
- Output file: `/app/outputs/step_03_VN_vertical_IE.txt`
- Format: txt
- Contract: Single number: vertical IE in meV. Format: '<value> meV'.
- Scoring: scored by hidden verifier

### Step 8: Compute Mg_Ga PL transitions
- Role: scored (load-bearing)
- Action: From the Mg_Ga energies, calculate the vertical ionisation energies (ΔE between charge states q and q+1) for the basal-plane and axial hole configurations, with singlet final state (and optionally triplet). Write a CSV with columns: configuration, final_state, energy_eV.
- Output file: `/app/outputs/step_04_MgGa_PL_transitions.csv`
- Format: csv
- Contract: CSV with columns 'configuration' (basal-plane or axial), 'final_state' (singlet or triplet), 'energy_eV' (vertical IE in eV). At minimum, rows for basal-plane/singlet and axial/singlet are required; all four rows may be present.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_MgGa_formation_energy.txt`
- `/app/outputs/step_02_VN_crossing.txt`
- `/app/outputs/step_03_VN_vertical_IE.txt`
- `/app/outputs/step_04_MgGa_PL_transitions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_MgGa_formation_energy.txt
- path: `/app/outputs/step_01_MgGa_formation_energy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Formation energy of neutral Mg_Ga (axial hole configuration) under N-rich conditions, compared against a hidden reference value within tolerance.
- schema:
  - `type`: text
  - `description`: A single line containing the formation energy in eV, formatted as '<value> eV'.

### step_02_VN_crossing.txt
- path: `/app/outputs/step_02_VN_crossing.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Fermi energy at which V_N^+ and V_N^3+ formation energies cross, compared against a hidden reference value within tolerance.
- schema:
  - `type`: text
  - `description`: A single line containing the Fermi energy crossing point in eV above VBM, formatted as '<value> eV'.

### step_03_VN_vertical_IE.txt
- path: `/app/outputs/step_03_VN_vertical_IE.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Vertical ionisation energy of V_N^0 relative to CBM, compared against a hidden reference value within tolerance.
- schema:
  - `type`: text
  - `description`: A single line containing the vertical ionisation energy in meV, formatted as '<value> meV'.

### step_04_MgGa_PL_transitions.csv
- path: `/app/outputs/step_04_MgGa_PL_transitions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing vertical ionisation energies for at least the two key PL transitions (basal-plane/singlet and axial/singlet). Each row is compared against a hidden reference value within tolerance.
- schema:
  - `type`: table
  - `format`: csv
  - `required_columns`: `configuration`, `final_state`, `energy_eV`
  - `column_types`:
    - `configuration`: string (basal-plane or axial)
    - `final_state`: string (singlet or triplet)
    - `energy_eV`: float (vertical IE in eV)
  - `minimum_rows`: 2

Notes: All scored outputs are evaluated by result-level compare (T0) against paper-reported values with tolerances: formation energies ±0.1 eV, ionisation energies ±0.05 eV. The reward is monotonic in closeness; meeting or exceeding precision earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_MgGa_formation_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single line containing the formation energy in eV, formatted as '<value> eV'."
      },
      "description": "Formation energy of neutral Mg_Ga (axial hole configuration) under N-rich conditions, compared against a hidden reference value within tolerance."
    },
    {
      "file": "step_02_VN_crossing.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single line containing the Fermi energy crossing point in eV above VBM, formatted as '<value> eV'."
      },
      "description": "Fermi energy at which V_N^+ and V_N^3+ formation energies cross, compared against a hidden reference value within tolerance."
    },
    {
      "file": "step_03_VN_vertical_IE.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single line containing the vertical ionisation energy in meV, formatted as '<value> meV'."
      },
      "description": "Vertical ionisation energy of V_N^0 relative to CBM, compared against a hidden reference value within tolerance."
    },
    {
      "file": "step_04_MgGa_PL_transitions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "format": "csv",
        "required_columns": [
          "configuration",
          "final_state",
          "energy_eV"
        ],
        "column_types": {
          "configuration": "string (basal-plane or axial)",
          "final_state": "string (singlet or triplet)",
          "energy_eV": "float (vertical IE in eV)"
        },
        "minimum_rows": 2
      },
      "description": "CSV containing vertical ionisation energies for at least the two key PL transitions (basal-plane/singlet and axial/singlet). Each row is compared against a hidden reference value within tolerance."
    }
  ],
  "notes": "All scored outputs are evaluated by result-level compare (T0) against paper-reported values with tolerances: formation energies ±0.1 eV, ionisation energies ±0.05 eV. The reward is monotonic in closeness; meeting or exceeding precision earns full credit."
}
```

## How you are scored
A hidden verifier reads the four scored output files you produce (step_01_MgGa_formation_energy.txt, step_02_VN_crossing.txt, step_03_VN_vertical_IE.txt, step_04_MgGa_PL_transitions.csv). It compares the numerical values and, for the CSV, the per‑row energies against reference values (obtained from the original study) using appropriate tolerances. Each scored output contributes to a combined reward in the range [0, 1]; the reward is monotonic in accuracy – results that are closer to the reference earn higher credit, and matching or exceeding the reference precision yields full credit. The verifier does not recompute the QM/MM simulations; it carries out a result‑level comparison. Consequently, fabricating numbers or guessing will not give a high score; only a faithful execution of the described workflow can produce the correct answers.
