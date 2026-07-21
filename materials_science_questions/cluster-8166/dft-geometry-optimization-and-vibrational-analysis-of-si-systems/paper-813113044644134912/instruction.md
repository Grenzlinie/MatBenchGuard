# DFT Study of Binding Energies and Electronic Properties of Fullerene-Ligand Complexes

## Problem background
This computational chemistry study investigates the interaction of 1-acetylpiperazine (1-ap) with undoped C20, boron-doped C20 (BC19), and silicon-doped C20 (SiC19) fullerenes. The goal is to determine the binding stability and electronic properties of the resulting complexes by computing binding energies and frontier molecular orbital characteristics. Understanding these properties helps assess the potential of doped fullerenes as carriers or sensors for the ligand. The problem is posed as a reproducible DFT task: compute the relevant energies and properties for all six complexes in both gas phase and water solvent.

## Approach
The investigation uses density functional theory (DFT) with the M06‑2X exchange‑correlation functional and the 6‑31G(d) basis set. First, the isolated fragments (C20, BC19, SiC19, and 1-acetylpiperazine) are optimized in the gas phase and in water using the polarizable continuum model (PCM) for solvation. Then, six complexes are formed: C20+1-ap interacting via the carbonyl oxygen (C=O), C20+1-ap via the amine nitrogen (NH), and analogous pairs for BC19 and SiC19, with the dopant atom as the primary interaction site. Geometry optimizations are performed for all complexes in both media. Binding energies are corrected for basis set superposition error (BSSE) using the counterpoise method. Finally, from the optimized complex wavefunctions, HOMO–LUMO energies are extracted and used to compute the energy gap, chemical hardness, and electrophilicity index. All calculations are carried out with open‑source quantum chemistry software that supports the required functional, basis set, solvation model, and counterpoise correction.

## Reproduction target
Produce two scored CSV files under `/app/outputs`:

1. `binding_energies.csv` with columns: complex (string), medium (gas/water), Eb_kcal_per_mol (float). Must contain one row for each of the six complexes (C20+1-ap C=O, C20+1-ap NH, BC19+1-ap C=O, BC19+1-ap NH, SiC19+1-ap C=O, SiC19+1-ap NH) in gas phase and another row for each in water, for a total of 12 rows. Eb_kcal_per_mol is the BSSE-corrected binding energy in kcal/mol.

2. `electronic_properties.csv` with columns: complex (string), medium (gas/water), EHOMO_eV (float), ELUMO_eV (float), Egap_eV (float), eta_eV (float), omega_eV (float). Must contain 12 rows covering the same six complexes in both media. Units are eV for all columns.

All values must be derived from M06‑2X/6‑31G(d) DFT calculations with PCM water solvation (where applicable) and counterpoise BSSE correction, using the workflow described in the steps.

## Assets

- Open-source DFT software (e.g., Psi4, ORCA): https://psicode.org/

## Workflow steps

### Step 1: Optimize isolated fragments
- Role: process
- Action: Perform geometry optimization of isolated fragments: C20, BC19, SiC19, and 1-acetylpiperazine at the M06-2X/6-31G(d) level of theory in gas phase and in water using the PCM solvation model. Verify no imaginary vibrational frequencies. Record optimized geometries and total electronic energies.
- Evidence: `/app/outputs/fragment_geometries.json`

### Step 2: Optimize complexes
- Role: process
- Action: Build starting geometries for the six complexes: C20+1-ap (C=O), C20+1-ap (NH), BC19+1-ap (C=O), BC19+1-ap (NH), SiC19+1-ap (C=O), SiC19+1-ap (NH). For doped fullerenes the primary interaction site is the dopant atom. Perform geometry optimization at M06-2X/6-31G(d) in gas and water, verifying no imaginary frequencies. Record optimized geometries.
- Evidence: `/app/outputs/complex_geometries.json`

### Step 3: Calculate BSSE-corrected binding energies
- Role: scored (load-bearing)
- Action: Using the optimized fragment and complex geometries, perform counterpoise (Boys-Bernardi) BSSE-corrected single-point energy calculations at M06-2X/6-31G(d) level for each complex in gas and water. Compute the binding energy Eb = E_complex - (E_fragment1_in_complex_basis + E_fragment2_in_complex_basis). Report results in kcal/mol.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: CSV with columns: complex (string), medium (gas/water), Eb_kcal_per_mol (float). 12 rows.
- Scoring: scored by hidden verifier

### Step 4: Extract electronic properties
- Role: scored
- Action: From the optimized complex wavefunctions, extract HOMO and LUMO energies in eV. Compute energy gap Egap = ELUMO - EHOMO, chemical hardness eta = Egap/2, and electrophilicity index omega = mu^2/(2*eta) where mu = (EHOMO+ELUMO)/2. Report results for each complex in gas and water.
- Output file: `/app/outputs/electronic_properties.csv`
- Format: csv
- Contract: CSV with columns: complex (string), medium (gas/water), EHOMO_eV (float), ELUMO_eV (float), Egap_eV (float), eta_eV (float), omega_eV (float). 12 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`
- `/app/outputs/electronic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: BSSE-corrected binding energies and key interatomic distances (Si...O, Si...N, B...O, B...N) for the six complexes in gas phase and water.
- schema:
  - `type`: table
  - `required_columns`: `complex`, `medium`, `Eb_kcal_per_mol`
  - `optional_columns`: `Si_O_angstrom`, `Si_N_angstrom`, `B_O_angstrom`, `B_N_angstrom`
  - `units`:
    - `Eb_kcal_per_mol`: kcal/mol
    - `Si_O_angstrom`: angstrom
    - `Si_N_angstrom`: angstrom
    - `B_O_angstrom`: angstrom
    - `B_N_angstrom`: angstrom

### electronic_properties.csv
- path: `/app/outputs/electronic_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: HOMO/LUMO energies, gap, hardness, and electrophilicity for each complex.
- schema:
  - `type`: table
  - `required_columns`: `complex`, `medium`, `EHOMO_eV`, `ELUMO_eV`, `Egap_eV`, `eta_eV`, `omega_eV`
  - `units`:
    - `EHOMO_eV`: eV
    - `ELUMO_eV`: eV
    - `Egap_eV`: eV
    - `eta_eV`: eV
    - `omega_eV`: eV

Notes: Binding energies and electronic properties are compared to reference values. Interatomic distances extracted from optimized geometries are included in the binding energies file for doped complexes.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "complex",
          "medium",
          "Eb_kcal_per_mol"
        ],
        "optional_columns": [
          "Si_O_angstrom",
          "Si_N_angstrom",
          "B_O_angstrom",
          "B_N_angstrom"
        ],
        "units": {
          "Eb_kcal_per_mol": "kcal/mol",
          "Si_O_angstrom": "angstrom",
          "Si_N_angstrom": "angstrom",
          "B_O_angstrom": "angstrom",
          "B_N_angstrom": "angstrom"
        }
      },
      "description": "BSSE-corrected binding energies and key interatomic distances (Si...O, Si...N, B...O, B...N) for the six complexes in gas phase and water."
    },
    {
      "file": "electronic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "complex",
          "medium",
          "EHOMO_eV",
          "ELUMO_eV",
          "Egap_eV",
          "eta_eV",
          "omega_eV"
        ],
        "units": {
          "EHOMO_eV": "eV",
          "ELUMO_eV": "eV",
          "Egap_eV": "eV",
          "eta_eV": "eV",
          "omega_eV": "eV"
        }
      },
      "description": "HOMO/LUMO energies, gap, hardness, and electrophilicity for each complex."
    }
  ],
  "notes": "Binding energies and electronic properties are compared to reference values. Interatomic distances extracted from optimized geometries are included in the binding energies file for doped complexes."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored artifact (`binding_energies.csv` and `electronic_properties.csv`). For each numeric field, the verifier compares your computed value to an expected reference value using appropriate tolerances. The final reward is a weighted sum of the scores from the two artifacts. Producing values that are consistent with the required computational method and that capture the correct relative trends is essential; simply reporting reference numbers without proper computation will not receive full credit.
