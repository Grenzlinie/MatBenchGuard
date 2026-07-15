# Dielectric function from DFT for perovskite KTaO3 with oxygen vacancy defects

## Problem background
Perovskite KTaO3 is a promising photocatalyst, but its relatively large band gap limits its use of the solar spectrum. Replacing some Ta atoms with Sb3+ dopants and introducing compensating oxygen vacancies is a proposed strategy to tune the electronic structure and move the optical response toward the visible region. The location of the oxygen vacancy may play a critical role: it can sit between the dopant and a Ta atom (defect‑1) or between two Ta atoms (defect‑2). This task uses density functional theory (DFT) calculations to investigate how these two defect configurations affect the structural parameters, the electronic band gap, and the dielectric function of the Sb‑doped KTaO3 system, compared with the undoped parent compound.

## Approach
The approach is to perform plane‑wave (or full‑potential) DFT calculations using the PBE GGA functional, followed by a band‑gap correction via a TB‑mBJ or hybrid functional. Three systems are studied: undoped cubic KTaO3, and 2×2×2 supercells of Sb‑doped KTa0.875Sb0.125O2.875 with the oxygen vacancy in defect‑1 and defect‑2 configurations.

For each system, the equilibrium lattice parameter is obtained by calculating total energies at several volumes around the expected value and fitting the resulting E(V) data to the Murnaghan equation of state. The optimized structure then serves as input for a self‑consistent DFT calculation that yields the Kohn–Sham eigenvalues and the momentum matrix elements needed for optical properties. The electronic band gap is determined from the total density of states (the energy difference between the valence band maximum and conduction band minimum). Finally, the imaginary part ε2(ω) of the dielectric function is computed from the direct optical transition matrix elements over the photon energy range 0–10 eV. The three artifacts (structural parameters, band gap, ε2 spectrum) provide a self‑contained picture of how the vacancy location changes the electronic and optical character of the material.

## Reproduction target
Using an open‑source DFT code capable of total‑energy, density‑of‑states, and optical matrix‑element calculations, produce the following quantities for undoped cubic KTaO3 and for the two Sb‑doped defective supercells (defect‑1 and defect‑2):

1. Equilibrium lattice parameter and Ta–O bond length (half the lattice parameter in the cubic supercell) obtained from a Murnaghan equation‑of‑state fit to total energies computed at several volumes. Write these fitted structural parameters, together with the bulk modulus and ground‑state energy, to `structural_properties.csv`.
2. Electronic band gap extracted from the total density of states at the optimized volume. Write the band gap (in eV; negative or zero for systems that show no band gap) to `band_gap.csv`.
3. The imaginary part of the dielectric function ε2(ω) for photon energies from 0 to 10 eV with a step size ≤ 0.1 eV, computed from the Kohn–Sham eigenvalues and momentum matrix elements. Write the spectrum to `dielectric_function.csv`.

The output files must follow the column schemas and unit conventions described in the workflow steps and the output contract.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, ABINIT): https://www.quantum-espresso.org
- Pseudopotential library (e.g., SSSP precision or GBRV): https://pseudopotentials.quantum-espresso.org
- Crystal structure of cubic KTaO3 (space group Pm-3m): https://next-gen.materialsproject.org/materials/mp-3614

## Workflow steps

### Step 1: Generate input structures
- Role: process
- Action: Create crystal structure input files for cubic KTaO3 (primitive cell) and for 2×2×2 supercells of KTa0.875Sb0.125O2.875 with defect-1 (oxygen vacancy between Sb and Ta) and defect-2 (oxygen vacancy between two Ta atoms).
- Evidence: none

### Step 2: DFT total energy versus volume calculations
- Role: process
- Action: For each system, perform self-consistent DFT calculations at several volumes around the expected equilibrium, using PBE-GGA functional and a plane-wave/pseudopotential approach with suitable convergence parameters. Record the total energy for each volume.
- Evidence: none

### Step 3: Murnaghan EOS fit and structural properties
- Role: scored
- Action: Fit the E(V) data for each system to the Murnaghan equation of state. Extract equilibrium lattice parameter, Ta-O bond length (half the lattice constant for the supercell), bulk modulus, pressure derivative, and ground-state energy. Write results to structural_properties.csv.
- Output file: `/app/outputs/structural_properties.csv`
- Format: csv
- Contract: Columns: system (values: undoped, Sb_defect1, Sb_defect2), lattice_parameter_A (float, Angstrom), bond_length_A (float, Angstrom), bulk_modulus_GPa (float), ground_state_energy_Ry (float).
- Scoring: scored by hidden verifier

### Step 4: DFT SCF calculation at equilibrium volumes
- Role: process
- Action: Using the optimized lattice constants from step 3, run DFT SCF calculations with a suitable k-point mesh to obtain Kohn-Sham eigenvalues and momentum matrix elements. Use a functional that improves the band gap (e.g., TB-mBJ or a hybrid functional).
- Evidence: none

### Step 5: Band gap from total density of states
- Role: scored
- Action: Compute the total density of states from the SCF results; determine the band gap as the energy difference between the valence band maximum and conduction band minimum. Output the gap for each system to band_gap.csv.
- Output file: `/app/outputs/band_gap.csv`
- Format: csv
- Contract: Columns: system (same coding as above), band_gap_eV (float; negative or zero for metallic systems).
- Scoring: scored by hidden verifier

### Step 6: Imaginary part of dielectric function
- Role: scored (load-bearing)
- Action: From the momentum matrix elements and eigenvalues, compute the imaginary part of the dielectric function ε2(ω) over photon energies 0–10 eV with a step ≤ 0.1 eV for each system. Write the spectra to dielectric_function.csv.
- Output file: `/app/outputs/dielectric_function.csv`
- Format: csv
- Contract: Columns: system (string), energy_eV (float from 0 to 10 eV), epsilon2 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_properties.csv`
- `/app/outputs/band_gap.csv`
- `/app/outputs/dielectric_function.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_properties.csv
- path: `/app/outputs/structural_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Fitted structural parameters from Murnaghan equation of state for undoped KTaO3, Sb-defect1, and Sb-defect2.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `system`, `lattice_parameter_A`, `bond_length_A`, `bulk_modulus_GPa`, `ground_state_energy_Ry`
  - `units`:
    - `lattice_parameter_A`: Angstrom
    - `bond_length_A`: Angstrom
    - `bulk_modulus_GPa`: GPa
    - `ground_state_energy_Ry`: Rydberg

### band_gap.csv
- path: `/app/outputs/band_gap.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Electronic band gaps extracted from total density of states.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `system`, `band_gap_eV`
  - `units`:
    - `band_gap_eV`: eV

### dielectric_function.csv
- path: `/app/outputs/dielectric_function.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Imaginary part of dielectric function ε2(ω) over 0–10 eV. The verifier will recompute static dielectric constant via Kramers-Kronig and compare the value and first peak position against hidden references.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `system`, `energy_eV`, `epsilon2`
  - `units`:
    - `energy_eV`: eV
    - `epsilon2`: dimensionless

Notes: Tolerances are set to accommodate systematic differences between DFT codes and pseudopotentials.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "system",
          "lattice_parameter_A",
          "bond_length_A",
          "bulk_modulus_GPa",
          "ground_state_energy_Ry"
        ],
        "units": {
          "lattice_parameter_A": "Angstrom",
          "bond_length_A": "Angstrom",
          "bulk_modulus_GPa": "GPa",
          "ground_state_energy_Ry": "Rydberg"
        }
      },
      "description": "Fitted structural parameters from Murnaghan equation of state for undoped KTaO3, Sb-defect1, and Sb-defect2."
    },
    {
      "file": "band_gap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "system",
          "band_gap_eV"
        ],
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "Electronic band gaps extracted from total density of states."
    },
    {
      "file": "dielectric_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "system",
          "energy_eV",
          "epsilon2"
        ],
        "units": {
          "energy_eV": "eV",
          "epsilon2": "dimensionless"
        }
      },
      "description": "Imaginary part of dielectric function ε2(ω) over 0–10 eV. The verifier will recompute static dielectric constant via Kramers-Kronig and compare the value and first peak position against hidden references."
    }
  ],
  "notes": "Tolerances are set to accommodate systematic differences between DFT codes and pseudopotentials."
}
```

## How you are scored
Your outputs are checked by a hidden verifier that scores each artifact independently and combines the subscores into a final reward between 0 and 1. The verifier:

- Reads `structural_properties.csv` and compares the lattice parameter and bond length for each system to hidden reference values (with appropriate tolerances to account for code‑to‑code differences).
- Reads `band_gap.csv` and compares the reported band gap to reference values; for any system that is metallic, the expected gap is zero or negative.
- Reads `dielectric_function.csv`, performs a Kramers‑Kronig integration to obtain the static dielectric constant, and locates the first dominant peak of ε2. These derived quantities are compared to hidden reference values.

The overall reward is a weighted combination of the structural, band‑gap, and dielectric‑function scores. Simply reporting numbers that match the paper is not sufficient—the verifier evaluates the correctness of the computed results against its private references. The tolerances are set to accommodate legitimate implementation differences between DFT codes and pseudopotentials.
