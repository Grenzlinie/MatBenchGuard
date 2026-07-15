# Computational Molecular Dipole Moment Calculation for Liquid Crystal Homologs

## Problem background
This task concerns two rod-like liquid crystal homologs, referred to as 3F and 4F. The molecules differ only by one methylene unit in their terminal alkyl chain, yet they exhibit strikingly different polar ordering: one displays ferroelectric smectic phases while the other shows paraelectric phases. Understanding the microscopic origin of this behavior requires characterizing the molecular electric dipole moments and overall molecular shape.

The molecular structures are:
- **3F**: 3,4,5-trifluorophenyl 2-fluoro-4-[(4-propylbenzoyl)oxy]benzoate  
  SMILES: `CCCc1ccc(cc1)C(=O)Oc2ccc(c(F)c2)C(=O)Oc3cc(F)c(F)c(F)c3`
- **4F**: 3,4,5-trifluorophenyl 2-fluoro-4-[(4-butylbenzoyl)oxy]benzoate  
  SMILES: `CCCCc1ccc(cc1)C(=O)Oc2ccc(c(F)c2)C(=O)Oc3cc(F)c(F)c(F)c3`

You will compute the Cartesian dipole moment components (μₓ, μ_y, μ_z), total dipole moment (μ_total), molecular length (L), width (D), and the aspect ratio L/D for both molecules using quantum‑chemical methods. These quantities provide insight into the electrostatic and steric factors that may govern the phase behavior.

## Approach
The approach relies on density functional theory (DFT) calculations. For each molecule you must:
1. Generate a reasonable initial three‑dimensional geometry from the supplied SMILES string using a cheminformatics library.
2. Perform a gas‑phase geometry optimization followed by a vibrational frequency analysis to ensure the structure is a true minimum. Use the B3LYP hybrid functional and the 6‑311G+(d,p) basis set.
3. From the optimized geometry, extract the dipole moment vector components and the total magnitude (in Debye). Determine the molecular length (L, maximum atom pair distance along the principal molecular axis) and the molecular width (D, average of the two perpendicular dimensions) in Å, and compute the length‑to‑width ratio L/D.

The calculations should be performed with an open‑source quantum chemistry package (ORCA or an equivalent DFT code). RDKit is recommended for structure generation. You will compare the results for the two homologs to reveal how the addition of a single methylene group alters the computed molecular properties.

## Reproduction target
Produce a CSV file, `dft_values.csv`, containing the following values for both molecules (3F and 4F):
- `mu_x`, `mu_y`, `mu_z` – Cartesian components of the dipole moment in Debye
- `mu_total` – magnitude of the total dipole moment in Debye
- `L` – molecular length in Å
- `D` – molecular width in Å
- `L_D` – length‑to‑width ratio (dimensionless)

The file must have columns `molecule, mu_x, mu_y, mu_z, mu_total, L, D, L_D` with exactly one row for 3F and one row for 4F. All numeric fields should be recorded to a reasonable precision (typically two decimal places for energy/geometry quantities).

## Assets

- ORCA quantum chemistry package (version 5.x or later): https://orcaforum.kofo.mpg.de/
- RDKit cheminformatics library: rdkit

## Workflow steps

### Step 1: DFT calculations and parameter extraction
- Role: scored (load-bearing)
- Action: Generate initial 3D molecular structures for compounds 3F and 4F from their SMILES strings using RDKit. Perform gas-phase geometry optimization and frequency analysis for each molecule using the ORCA quantum chemistry package at the B3LYP/6-311G+(d,p) level of theory. From the optimized geometries, extract the Cartesian components of the dipole moment (mu_x, mu_y, mu_z) in Debye, the total dipole moment (mu_total), the molecular length L and width D in Å, and the length-to-width ratio L/D. Write all values to dft_values.csv.
- Output file: `/app/outputs/dft_values.csv`
- Format: csv
- Contract: Columns: molecule (string, '3F' or '4F'), mu_x (float, Debye), mu_y (float, Debye), mu_z (float, Debye), mu_total (float, Debye), L (float, Angstrom), D (float, Angstrom), L_D (float, dimensionless). Two rows: one for each molecule.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_values.csv
- path: `/app/outputs/dft_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: DFT-computed dipole moments and molecular geometry parameters for the two homologs 3F and 4F.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `mu_x`, `mu_y`, `mu_z`, `mu_total`, `L`, `D`, `L_D`
  - `units`:
    - `mu_x`: Debye
    - `mu_y`: Debye
    - `mu_z`: Debye
    - `mu_total`: Debye
    - `L`: Angstrom
    - `D`: Angstrom
    - `L_D`: dimensionless
  - `row_count`: 2

Notes: Only the numerical values from Table 2 of the source paper are scored. ESP maps, charge density analysis, and experimental characterization are out of scope. The agent must use an open-source DFT code (ORCA or equivalent).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "mu_x",
          "mu_y",
          "mu_z",
          "mu_total",
          "L",
          "D",
          "L_D"
        ],
        "units": {
          "mu_x": "Debye",
          "mu_y": "Debye",
          "mu_z": "Debye",
          "mu_total": "Debye",
          "L": "Angstrom",
          "D": "Angstrom",
          "L_D": "dimensionless"
        },
        "row_count": 2
      },
      "description": "DFT-computed dipole moments and molecular geometry parameters for the two homologs 3F and 4F."
    }
  ],
  "notes": "Only the numerical values from Table 2 of the source paper are scored. ESP maps, charge density analysis, and experimental characterization are out of scope. The agent must use an open-source DFT code (ORCA or equivalent)."
}
```

## How you are scored
After you submit your output, a hidden verifier will automatically evaluate `dft_values.csv`. The verifier checks that the file is well‑formed, contains the required columns and two rows, and that the numeric values are physically plausible and consistent with a correct execution of the DFT workflow. The verifier compares your computed values against an independently established reference; reporting numbers without genuinely performing the calculations will not pass. The final reward is a number between 0 and 1 that reflects how well your results agree with the expected physical quantities.
