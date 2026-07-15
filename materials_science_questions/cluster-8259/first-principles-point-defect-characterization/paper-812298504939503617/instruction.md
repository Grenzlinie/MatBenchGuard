# DFT study of forsterite lattice parameters and band gaps under pressure and hydrogen doping

## Problem background
Forsterite (Mg2SiO4) is the magnesium end-member of olivine, the most abundant mineral in the Earth's upper mantle. Hydrogen can be incorporated into its crystal lattice as point defects, most commonly associated with magnesium vacancies. It is believed that these defects can alter the electrical conductivity of forsterite, but the underlying electronic-structure mechanism is not fully resolved. This work investigates, using first-principles calculations, how hydrostatic pressure influences the electronic band gap of anhydrous forsterite and, separately, whether a free-proton defect model can produce electronic states that modify the gap of hydrous forsterite.

## Approach
Density functional theory (DFT) calculations are carried out with the generalized gradient approximation (GGA) and norm-conserving pseudopotentials. For anhydrous forsterite, variable-cell geometry optimizations are performed at hydrostatic pressures ranging from 0 to 16 GPa to obtain equilibrium lattice constants and cell volumes. Kohn-Sham band-structure calculations at selected pressures then yield the electronic band gap, defined as the energy difference between the conduction-band minimum and the valence-band maximum. For hydrous forsterite, a supercell is constructed from the optimized ambient-pressure anhydrous structure. One magnesium atom is removed from an M1 site to create a vacancy. Two hydrogen-defect scenarios are explored. In the free-proton model, one hydrogen occupies the Mg vacancy while a second hydrogen is placed at distinct crystallographic positions corresponding to the [100], [010], and [001] orientations; the structures are relaxed, and band gaps are computed for each orientation. Throughout the workflow, the open-source DFT code used reproduces the same computational protocol employed in the original study, allowing the key quantities to be recomputed independently.

## Reproduction target
Your objective is to produce three scored artifacts:
- For anhydrous forsterite, optimize the geometry at pressures 0, 2, 4, 6, 8, 10, 12 GPa and extract the lattice parameters a, b, c (Å) and cell volume V (Å³).
- From the optimized structures at 0 GPa and 16 GPa, compute the Kohn-Sham band gap (eV).
- For the hydrous free-proton model, construct the three configurations with the second proton along [100], [010], and [001], relax each, and compute their band gaps (eV).
Write these results to the specified CSV files; each file must contain the required columns and units as listed in the workflow steps.

## Assets

- Forsterite crystal structure (Mg2SiO4, Pbnm): https://materialsproject.org/
- Quantum ESPRESSO or equivalent open-source DFT code: https://www.quantum-espresso.org/
- Norm-conserving pseudopotentials for Mg, Si, O, H: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Anhydrous forsterite geometry optimization
- Role: process
- Action: Using a DFT code with GGA exchange-correlation and norm-conserving pseudopotentials, perform variable-cell geometry optimizations of the forsterite crystal structure at hydrostatic pressures 0, 2, 4, 6, 8, 10, 12, 14, 16 GPa. Relax cell shape and atomic positions until forces and stress are converged. Save the optimized structures for each pressure.
- Evidence: `/app/outputs/anhydrous_optimization_log.txt`

### Step 2: Anhydrous lattice parameters
- Role: scored (load-bearing)
- Action: From the optimized structures at pressures 0,2,4,6,8,10,12 GPa (obtained in step01), extract the lattice constants a, b, c (in Å) and cell volume V (in Å³). Write the values to anhydrous_lattice_parameters.csv.
- Output file: `/app/outputs/anhydrous_lattice_parameters.csv`
- Format: csv
- Contract: pressure_GPa, a_Ang, b_Ang, c_Ang, V_Ang3
- Scoring: scored by hidden verifier

### Step 3: Anhydrous electronic structure (band gap)
- Role: process
- Action: Using the optimized structures at 0 GPa and 16 GPa from step01, perform self-consistent field (SCF) calculations followed by a band-structure calculation to obtain the Kohn-Sham band gap (energy difference between conduction band minimum and valence band maximum).
- Evidence: `/app/outputs/anhydrous_scf_log.txt`

### Step 4: Anhydrous band gaps
- Role: scored (load-bearing)
- Action: From the band-structure calculations in step03, extract the band gap energies for anhydrous forsterite at 0 GPa and 16 GPa. Write the values to anhydrous_band_gaps.csv.
- Output file: `/app/outputs/anhydrous_band_gaps.csv`
- Format: csv
- Contract: pressure_GPa, Eg_eV
- Scoring: scored by hidden verifier

### Step 5: Hydrous forsterite defect model construction
- Role: process
- Action: Create a supercell of the anhydrous forsterite optimized at 0 GPa (from step01). Remove one Mg atom from an M1 site (0.5,0.5,0.5). For the free-proton (Type 2) configurations, place one H atom at the M1 vacancy and the second H atom at the fractional coordinates (0.75,0.5,0.5) – [100] orientation, (0.5,0.63,0.5) – [010] orientation, and (0.5,0.5,0.68) – [001] orientation. Perform geometry optimizations for each of these three configurations at 0 GPa.
- Evidence: `/app/outputs/hydrous_optimization_log.txt`

### Step 6: Hydrous electronic structure (band gap)
- Role: process
- Action: For each optimized hydrous configuration from step05, perform SCF and band-structure calculations to obtain the Kohn-Sham band gap.
- Evidence: `/app/outputs/hydrous_scf_log.txt`

### Step 7: Hydrous band gaps
- Role: scored (load-bearing)
- Action: From the band-structure results in step06, extract the band gap energies for the three hydrous configurations (free proton along [100], [010], [001]). Write the values to hydrous_band_gaps.csv.
- Output file: `/app/outputs/hydrous_band_gaps.csv`
- Format: csv
- Contract: orientation, Eg_eV
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/anhydrous_lattice_parameters.csv`
- `/app/outputs/anhydrous_band_gaps.csv`
- `/app/outputs/hydrous_band_gaps.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### anhydrous_lattice_parameters.csv
- path: `/app/outputs/anhydrous_lattice_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice constants and cell volume of anhydrous forsterite at pressures 0–12 GPa. Correspondence to paper Table 1.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `a_Ang`, `b_Ang`, `c_Ang`, `V_Ang3`
  - `units`:
    - `pressure_GPa`: GPa
    - `a_Ang`: Angstrom
    - `b_Ang`: Angstrom
    - `c_Ang`: Angstrom
    - `V_Ang3`: Angstrom^3

### anhydrous_band_gaps.csv
- path: `/app/outputs/anhydrous_band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band gap energy of anhydrous forsterite at 0 and 16 GPa. Correspondence to paper Fig. 1 trend endpoints.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `Eg_eV`
  - `units`:
    - `pressure_GPa`: GPa
    - `Eg_eV`: eV

### hydrous_band_gaps.csv
- path: `/app/outputs/hydrous_band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band gap energy of hydrous forsterite (free proton model) along three orientations. Correspondence to paper-reported values.
- schema:
  - `type`: table
  - `required_columns`: `orientation`, `Eg_eV`
  - `units`:
    - `orientation`: crystallographic direction
    - `Eg_eV`: eV

Notes: All scored artifacts are compared to the original paper's published values with domain-appropriate tolerances. The workflow uses open-source DFT tools; the exact pseudopotential choice may shift values, which is accommodated by the tolerances. The scoring policy is reference_match: numeric values must fall within absolute tolerances around the hidden gold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "anhydrous_lattice_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "a_Ang",
          "b_Ang",
          "c_Ang",
          "V_Ang3"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "a_Ang": "Angstrom",
          "b_Ang": "Angstrom",
          "c_Ang": "Angstrom",
          "V_Ang3": "Angstrom^3"
        }
      },
      "description": "Optimized lattice constants and cell volume of anhydrous forsterite at pressures 0–12 GPa. Correspondence to paper Table 1."
    },
    {
      "file": "anhydrous_band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "Eg_eV"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "Eg_eV": "eV"
        }
      },
      "description": "Band gap energy of anhydrous forsterite at 0 and 16 GPa. Correspondence to paper Fig. 1 trend endpoints."
    },
    {
      "file": "hydrous_band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "orientation",
          "Eg_eV"
        ],
        "units": {
          "orientation": "crystallographic direction",
          "Eg_eV": "eV"
        }
      },
      "description": "Band gap energy of hydrous forsterite (free proton model) along three orientations. Correspondence to paper-reported values."
    }
  ],
  "notes": "All scored artifacts are compared to the original paper's published values with domain-appropriate tolerances. The workflow uses open-source DFT tools; the exact pseudopotential choice may shift values, which is accommodated by the tolerances. The scoring policy is reference_match: numeric values must fall within absolute tolerances around the hidden gold."
}
```

## How you are scored
A hidden verifier reads each scored CSV file you produce and compares the numeric values to reference data that is not visible to you. Each scored artifact is assigned a weight, and the final reward (a float between 0 and 1) is a weighted sum of individual stage scores. The verifier does not inspect intermediate logs or evidence files; it only evaluates the structure and content of the scored outputs. You must follow the exact output format and column schemas described in the workflow steps.
