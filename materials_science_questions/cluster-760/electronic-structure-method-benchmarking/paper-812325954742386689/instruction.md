# Electronic structure and thermochemistry of chlorinated and fluorinated peroxyl radicals

## Problem background
Chlorinated and fluorinated methyl peroxyl radicals participate in key atmospheric and combustion processes. Reliable computational prediction of their equilibrium structures, bond strengths, and electron affinities is essential both for understanding their chemical reactivity and for benchmarking electronic structure methods. This task systematically examines how chlorine and fluorine substitution influences these properties and assesses the agreement between MP2 and B3LYP functionals for these quantities.

## Approach
The workflow uses a combination of ab initio and density functional theory calculations. Initial molecular geometries are built for all relevant species—six peroxyl radicals, parent halomethanes, corresponding alkyl radicals and anions, and the small fragments H and O₂. Full geometry optimizations and vibrational frequency analyses are performed at MP2(full)/6‑31G(d,p) and B3LYP/6‑31G(d,p). These optimizations supply equilibrium structures, zero‑point energies, and thermal corrections. Mulliken population analysis on the resulting wavefunctions yields atomic charges, spin densities, and dipole moments. To improve energetics, single‑point energies are recomputed at MP4(SDTQ)/6‑311+G(d,p) and B3LYP/6‑311+G(2df,2p). C–H bond dissociation energies are then derived via isodesmic reactions anchoring to the experimental C–H bond energy of methane. C–O bond dissociation energies for the peroxyl radicals are obtained analogously, anchored to the experimental C–O bond energy of the methyl peroxyl radical. Adiabatic electron affinities are calculated from total electronic energies obtained with a diffuse basis set (6‑31+G(d,p)) at 0 K, again comparing the MP2 and B3LYP levels. The whole pipeline is to be executed to produce the required output files; the scoring evaluates how well the computed numbers agree with reference values without requiring any pre‑existing data from the paper.

## Reproduction target
For the six peroxyl radicals CH₂ClO₂•, CHCl₂O₂•, CCl₃O₂•, CFCl₂O₂•, CF₂ClO₂•, and CHFClO₂•, compute:
- Equilibrium bond lengths (C–O and O–O), the C–O–O angle, and the X–C–O–O torsion angles at MP2/6‑31G(d,p) and B3LYP/6‑31G(d,p), saved to `/app/outputs/geometries.csv`.
- Mulliken charges, spin densities on the C1, O2, and O3 atoms, and dipole moments at the same levels, saved to `/app/outputs/charge_spin_dipole.json`.
- C–H bond dissociation energies (kcal/mol) for the parent methanes CH₄, CH₃Cl, CH₂Cl₂, CHCl₃, CHFCl₂, CHF₂Cl, and CH₂FCl, at MP2 and B3LYP, using the experimental BDE(CH₄)=104.9 kcal/mol, saved to `/app/outputs/CH_BDEs.csv`.
- C–O bond dissociation energies (kcal/mol) for the peroxyl radicals R–O₂• where R = CH₃, CH₂Cl, CHCl₂, CCl₃, CFCl₂, CF₂Cl, CHFCl, at MP2 and B3LYP, anchored to the experimental BDE(CH₃–O₂)=32.7 kcal/mol, saved to `/app/outputs/CO_BDEs.csv`.
- Adiabatic electron affinities (kcal/mol) at 0 K for the same seven peroxyl radicals, calculated at MP2/6‑31+G(d,p) and B3LYP/6‑31+G(d,p), saved to `/app/outputs/EAs.csv`.
All values must be obtained by executing the computational steps described in the workflow, not by looking up the paper's numbers.

## Assets

- ORCA quantum chemistry package: https://www.orcasoftware.de

## Workflow steps

### Step 1: Build initial molecular structures
- Role: process
- Action: Generate initial Cartesian or Z‑matrix coordinates for all peroxyl radicals (CH₂ClO₂•, CHCl₂O₂•, CCl₃O₂•, CFCl₂O₂•, CF₂ClO₂•, CHFClO₂•), parent halomethanes, alkyl radicals, anions, and small fragments (H, O₂).
- Evidence: none

### Step 2: Geometry optimization and frequency calculations
- Role: process
- Action: Perform full geometry optimizations and vibrational frequency calculations at MP2(full)/6‑31G(d,p) and B3LYP/6‑31G(d,p) for all species required for later thermochemistry and property analysis. Save optimized geometries and wavefunction data.
- Evidence: none

### Step 3: Extract structural parameters
- Role: scored
- Action: From the optimized geometries, extract the C‑O and O‑O bond lengths, the C‑O‑O bond angle, and the X‑C‑O‑O torsion angles for each peroxyl radical at both MP2 and B3LYP levels and write the results to geometries.csv.
- Output file: `/app/outputs/geometries.csv`
- Format: csv
- Contract: Columns: Radical (string), Method (string), R_C1O2 (float, Å), R_O2O3 (float, Å), Angle_C1O2O3 (float, degrees), Torsion_X4 (float, degrees), Torsion_X5 (float, degrees), Torsion_X6 (float, degrees). One row per radical‑method combination.
- Scoring: scored by hidden verifier

### Step 4: Compute charge, spin density, and dipole moment
- Role: scored
- Action: Perform Mulliken population analysis on the MP2 and B3LYP wavefunctions to obtain atomic charges and spin densities for C1, O2, O3, and compute dipole moments. Write the data to charge_spin_dipole.json.
- Output file: `/app/outputs/charge_spin_dipole.json`
- Format: json
- Contract: Array of objects; each object has properties: radical (string), method (string, 'MP2' or 'B3LYP'), dipole_moment (float, Debye), atoms (array of objects with symbol (string), charge (float), spin_density (float)). Atom order: C1, O2, O3.
- Scoring: scored by hidden verifier

### Step 5: Higher‑level single‑point energy calculations
- Role: process
- Action: Compute single‑point energies at MP4(SDTQ)/6‑311+G(d,p) and B3LYP/6‑311+G(2df,2p) using the optimized geometries from step 2 for all species involved in thermochemistry.
- Evidence: none

### Step 6: Compute C‑H bond dissociation energies
- Role: scored
- Action: Calculate C‑H BDEs for parent halomethanes using isodesmic reactions and the experimental BDE(CH₄)=104.9 kcal/mol; combine with ZPE and thermal corrections from step 2. Write results to CH_BDEs.csv.
- Output file: `/app/outputs/CH_BDEs.csv`
- Format: csv
- Contract: Columns: Level (string, e.g., B3LYP/6‑31G(d,p)), CH4 (float, kcal/mol), CH3Cl (float), CH2Cl2 (float), CHCl3 (float), CHFCl2 (float), CHF2Cl (float), CH2FCl (float).
- Scoring: scored by hidden verifier

### Step 7: Compute C‑O bond dissociation energies
- Role: scored (load-bearing)
- Action: Calculate C‑O BDEs for the peroxyl radicals via isodesmic reactions, using the experimental BDE(CH₃‑O₂)=32.7 kcal/mol and energies/ZPE from steps 2 and 5. Write results to CO_BDEs.csv.
- Output file: `/app/outputs/CO_BDEs.csv`
- Format: csv
- Contract: Columns: Level (string), CH3‑O2 (float, kcal/mol), CH2Cl‑O2 (float), CHCl2‑O2 (float), CCl3‑O2 (float), CFCl2‑O2 (float), CF2Cl‑O2 (float), CHFCl‑O2 (float).
- Scoring: scored by hidden verifier

### Step 8: Single‑point calculations with diffuse basis for electron affinity
- Role: process
- Action: Run single‑point energy calculations at MP2/6‑31+G(d,p) and B3LYP/6‑31+G(d,p) for the peroxyl radicals and their corresponding anions using the optimized geometries from step 2.
- Evidence: none

### Step 9: Compute electron affinities
- Role: scored
- Action: Calculate adiabatic electron affinities as the difference between the total electronic energies of the radical and the anion species obtained in step 8. Write results to EAs.csv.
- Output file: `/app/outputs/EAs.csv`
- Format: csv
- Contract: Columns: Level (string), CH3‑O2 (float, kcal/mol), CH2Cl‑O2 (float), CHCl2‑O2 (float), CCl3‑O2 (float), CFCl2‑O2 (float), CF2Cl‑O2 (float), CHFCl‑O2 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometries.csv`
- `/app/outputs/charge_spin_dipole.json`
- `/app/outputs/CH_BDEs.csv`
- `/app/outputs/CO_BDEs.csv`
- `/app/outputs/EAs.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometries.csv
- path: `/app/outputs/geometries.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium bond lengths (Å), angles (°), and torsion angles (°) for six peroxyl radicals at MP2 and B3LYP levels.
- schema:
  - `type`: table
  - `required_columns`: `Radical`, `Method`, `R_C1O2`, `R_O2O3`, `Angle_C1O2O3`, `Torsion_X4`, `Torsion_X5`, `Torsion_X6`
  - `units`:
    - `R_C1O2`: Å
    - `R_O2O3`: Å
    - `Angle_C1O2O3`: degrees
    - `Torsion_X4`: degrees
    - `Torsion_X5`: degrees
    - `Torsion_X6`: degrees

### charge_spin_dipole.json
- path: `/app/outputs/charge_spin_dipole.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Mulliken charges, spin densities and dipole moments for each radical at MP2 and B3LYP.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `radical`, `method`, `dipole_moment`, `atoms`
    - `properties`:
      - `radical`: string
      - `method`: string
      - `dipole_moment`: float (Debye)
      - `atoms`: array of objects with symbol (string), charge (float), spin_density (float), ordered C1, O2, O3

### CH_BDEs.csv
- path: `/app/outputs/CH_BDEs.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: C‑H bond dissociation energies (kcal/mol) of parent methanes.
- schema:
  - `type`: table
  - `required_columns`: `Level`, `CH4`, `CH3Cl`, `CH2Cl2`, `CHCl3`, `CHFCl2`, `CHF2Cl`, `CH2FCl`
  - `units`:
    - `CH4`: kcal/mol
    - `CH3Cl`: kcal/mol
    - `CH2Cl2`: kcal/mol
    - `CHCl3`: kcal/mol
    - `CHFCl2`: kcal/mol
    - `CHF2Cl`: kcal/mol
    - `CH2FCl`: kcal/mol

### CO_BDEs.csv
- path: `/app/outputs/CO_BDEs.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: C‑O bond dissociation energies (kcal/mol) of peroxyl radicals.
- schema:
  - `type`: table
  - `required_columns`: `Level`, `CH3-O2`, `CH2Cl-O2`, `CHCl2-O2`, `CCl3-O2`, `CFCl2-O2`, `CF2Cl-O2`, `CHFCl-O2`
  - `units`:
    - `CH3-O2`: kcal/mol
    - `CH2Cl-O2`: kcal/mol
    - `CHCl2-O2`: kcal/mol
    - `CCl3-O2`: kcal/mol
    - `CFCl2-O2`: kcal/mol
    - `CF2Cl-O2`: kcal/mol
    - `CHFCl-O2`: kcal/mol

### EAs.csv
- path: `/app/outputs/EAs.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Adiabatic electron affinities (kcal/mol) of peroxyl radicals.
- schema:
  - `type`: table
  - `required_columns`: `Level`, `CH3-O2`, `CH2Cl-O2`, `CHCl2-O2`, `CCl3-O2`, `CFCl2-O2`, `CF2Cl-O2`, `CHFCl-O2`
  - `units`:
    - `CH3-O2`: kcal/mol
    - `CH2Cl-O2`: kcal/mol
    - `CHCl2-O2`: kcal/mol
    - `CCl3-O2`: kcal/mol
    - `CFCl2-O2`: kcal/mol
    - `CF2Cl-O2`: kcal/mol
    - `CHFCl-O2`: kcal/mol

Notes: The agent must use ORCA or another standard quantum chemistry package. Tolerances for geometric parameters and energies are set on the hidden grading side. All values must be computed from first principles; pre‑computed numbers from the paper are not accepted.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Radical",
          "Method",
          "R_C1O2",
          "R_O2O3",
          "Angle_C1O2O3",
          "Torsion_X4",
          "Torsion_X5",
          "Torsion_X6"
        ],
        "units": {
          "R_C1O2": "Å",
          "R_O2O3": "Å",
          "Angle_C1O2O3": "degrees",
          "Torsion_X4": "degrees",
          "Torsion_X5": "degrees",
          "Torsion_X6": "degrees"
        }
      },
      "description": "Equilibrium bond lengths (Å), angles (°), and torsion angles (°) for six peroxyl radicals at MP2 and B3LYP levels."
    },
    {
      "file": "charge_spin_dipole.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "radical",
            "method",
            "dipole_moment",
            "atoms"
          ],
          "properties": {
            "radical": "string",
            "method": "string",
            "dipole_moment": "float (Debye)",
            "atoms": "array of objects with symbol (string), charge (float), spin_density (float), ordered C1, O2, O3"
          }
        }
      },
      "description": "Mulliken charges, spin densities and dipole moments for each radical at MP2 and B3LYP."
    },
    {
      "file": "CH_BDEs.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Level",
          "CH4",
          "CH3Cl",
          "CH2Cl2",
          "CHCl3",
          "CHFCl2",
          "CHF2Cl",
          "CH2FCl"
        ],
        "units": {
          "CH4": "kcal/mol",
          "CH3Cl": "kcal/mol",
          "CH2Cl2": "kcal/mol",
          "CHCl3": "kcal/mol",
          "CHFCl2": "kcal/mol",
          "CHF2Cl": "kcal/mol",
          "CH2FCl": "kcal/mol"
        }
      },
      "description": "C‑H bond dissociation energies (kcal/mol) of parent methanes."
    },
    {
      "file": "CO_BDEs.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Level",
          "CH3-O2",
          "CH2Cl-O2",
          "CHCl2-O2",
          "CCl3-O2",
          "CFCl2-O2",
          "CF2Cl-O2",
          "CHFCl-O2"
        ],
        "units": {
          "CH3-O2": "kcal/mol",
          "CH2Cl-O2": "kcal/mol",
          "CHCl2-O2": "kcal/mol",
          "CCl3-O2": "kcal/mol",
          "CFCl2-O2": "kcal/mol",
          "CF2Cl-O2": "kcal/mol",
          "CHFCl-O2": "kcal/mol"
        }
      },
      "description": "C‑O bond dissociation energies (kcal/mol) of peroxyl radicals."
    },
    {
      "file": "EAs.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Level",
          "CH3-O2",
          "CH2Cl-O2",
          "CHCl2-O2",
          "CCl3-O2",
          "CFCl2-O2",
          "CF2Cl-O2",
          "CHFCl-O2"
        ],
        "units": {
          "CH3-O2": "kcal/mol",
          "CH2Cl-O2": "kcal/mol",
          "CHCl2-O2": "kcal/mol",
          "CCl3-O2": "kcal/mol",
          "CFCl2-O2": "kcal/mol",
          "CF2Cl-O2": "kcal/mol",
          "CHFCl-O2": "kcal/mol"
        }
      },
      "description": "Adiabatic electron affinities (kcal/mol) of peroxyl radicals."
    }
  ],
  "notes": "The agent must use ORCA or another standard quantum chemistry package. Tolerances for geometric parameters and energies are set on the hidden grading side. All values must be computed from first principles; pre‑computed numbers from the paper are not accepted."
}
```

## How you are scored
A hidden verifier independently reads each of the five required output files. The overall reward is a weighted combination of the per‑artifact scores. For each artifact the verifier checks the reported numeric entries against reference values within appropriate tolerances (structural parameters, energies, dipole moments) and assesses whether the expected trends across radicals are reproduced. The reward reflects how well the computed numbers agree with a correct re‑run of the computational protocol; reporting numbers from the paper without actually executing the calculations cannot earn a high score.
