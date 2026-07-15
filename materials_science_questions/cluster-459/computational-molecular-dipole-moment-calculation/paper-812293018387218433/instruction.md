# Quantum Chemical Calculation of Bicyclo[1.1.1]pentanone Structure and Dipole Moment

## Problem background
Bicyclo[1.1.1]pentanone is a strained cyclic ketone whose heavy-atom framework and dipole moment are sensitive probes of the performance of different theoretical methods. The molecule has been studied by microwave spectroscopy, which provided a substitution‑structure (r_s) for the heavy atoms and a precisely measured dipole moment. This task computes the equilibrium geometry (selected bond lengths and angles) and the dipole moment using four widely used computational approaches: molecular mechanics (MM2), semi‑empirical (MNDO), and ab initio Hartree–Fock theory with STO‑3G and 3‑21G basis sets. The computed quantities are compared with the experimentally determined values to see how well each theoretical model reproduces the structure and polarity of this small, strained system.

## Approach
Starting from the publicly known chemical structure of bicyclo[1.1.1]pentanone (SMILES `O=C1C2CC1C2`), an initial 3D conformer is generated and relaxed with a fast force field (MMFF94 via RDKit) to obtain a reasonable starting geometry. This common starting structure is then optimized independently with four methods: MM2 (Tinker), MNDO (MOPAC), RHF/STO‑3G (PySCF), and RHF/3‑21G (PySCF). After each optimization the dipole moment is computed at the optimized geometry. From each optimized structure the following heavy‑atom parameters are extracted: bond lengths C=O, C1−C2, C1−C4, and the non‑bonded bridgehead distance C1···C3; bond angles C1C2C3, C1C4C3, and C2MC4 (where M is the midpoint of C1 and C3); and the dipole moment. All results are collected into a single JSON file for comparison with the experimental microwave spectroscopy results.

## Reproduction target
Using the four computational methods listed (MM2, MNDO, RHF/STO‑3G, RHF/3‑21G), compute the equilibrium heavy‑atom bond lengths (C=O, C1−C2, C1−C4, and the bridgehead distance C1···C3 in Ångströms), the bond angles (C1C2C3, C1C4C3, and C2MC4 in degrees), and the dipole moment (in Debye) for bicyclo[1.1.1]pentanone. Report all values in a structured JSON file (`theoretical_results.json`) with one top‑level key for each method, each containing the required bond lengths, bond angles, and dipole moment.

## Assets

- Tinker (MM2 force field implementation): https://github.com/TinkerTools/tinker
- OpenMOPAC (MOPAC) for semi-empirical MNDO: https://github.com/OpenMOPAC/mopac
- PySCF (Python package for quantum chemistry): pyscf
- RDKit cheminformatics toolkit: rdkit
- numpy: numpy

## Workflow steps

### Step 1: Prepare initial 3D geometry
- Role: process
- Action: Build a 3D conformer of bicyclo[1.1.1]pentanone from its SMILES (O=C1C2CC1C2) using RDKit, perform a rapid MMFF94 geometry optimization, and save the resulting coordinates as an XYZ file for use by all four computational methods.
- Evidence: `/app/outputs/initial_geometry.xyz`

### Step 2: Compute geometries and dipole moments with four methods
- Role: scored (load-bearing)
- Action: Starting from the initial geometry, perform separate geometry optimizations and dipole moment calculations for bicyclo[1.1.1]pentanone with each of the four methods: (1) MM2 using Tinker, (2) MNDO using MOPAC, (3) RHF/STO-3G using PySCF, (4) RHF/3-21G using PySCF. For each optimized structure extract the bond lengths C=O, C1-C2, C1-C4, C1...C3 (non-bonded distance), the bond angles C1C2C3, C1C4C3, C2MC4 (M is the midpoint of C1 and C3), and the dipole moment. Assemble all results into theoretical_results.json.
- Output file: `/app/outputs/theoretical_results.json`
- Format: json
- Contract: { 'MM2': { 'bond_lengths': {'C=O': number, 'C1-C2': number, 'C1-C4': number, 'C1...C3': number}, 'bond_angles': {'C1C2C3': number, 'C1C4C3': number, 'C2MC4': number}, 'dipole_moment': number }, 'MNDO': {...}, 'STO-3G': {...}, '3-21G': {...} }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/theoretical_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### theoretical_results.json
- path: `/app/outputs/theoretical_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The single scored artifact: heavy‑atom bond lengths (Å), bond angles (°), and dipole moment (D) from MM2, MNDO, RHF/STO-3G, and RHF/3-21G optimizations. The hidden checker compares each parameter to the experimental reference from the paper, awarding full credit when the deviation is within a method‑specific tolerance (absolute error ≤ tolerance) and partial credit degrading as the error increases.
- schema:
  - `type`: object
  - `description`: Computed structural parameters and dipole moment for the four theoretical methods.
  - `required`: `MM2`, `MNDO`, `STO-3G`, `3-21G`
  - `method_object`:
    - `type`: object
    - `required`: `bond_lengths`, `bond_angles`, `dipole_moment`
    - `bond_lengths`:
      - `type`: object
      - `required`: `C=O`, `C1-C2`, `C1-C4`, `C1...C3`
      - `additionalProperties`: False
      - `value_type`: number (float, Ångström)
    - `bond_angles`:
      - `type`: object
      - `required`: `C1C2C3`, `C1C4C3`, `C2MC4`
      - `additionalProperties`: False
      - `value_type`: number (float, degrees)
    - `dipole_moment`:
      - `type`: number
      - `unit`: Debye

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "theoretical_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "description": "Computed structural parameters and dipole moment for the four theoretical methods.",
        "required": [
          "MM2",
          "MNDO",
          "STO-3G",
          "3-21G"
        ],
        "method_object": {
          "type": "object",
          "required": [
            "bond_lengths",
            "bond_angles",
            "dipole_moment"
          ],
          "bond_lengths": {
            "type": "object",
            "required": [
              "C=O",
              "C1-C2",
              "C1-C4",
              "C1...C3"
            ],
            "additionalProperties": false,
            "value_type": "number (float, Ångström)"
          },
          "bond_angles": {
            "type": "object",
            "required": [
              "C1C2C3",
              "C1C4C3",
              "C2MC4"
            ],
            "additionalProperties": false,
            "value_type": "number (float, degrees)"
          },
          "dipole_moment": {
            "type": "number",
            "unit": "Debye"
          }
        }
      },
      "description": "The single scored artifact: heavy‑atom bond lengths (Å), bond angles (°), and dipole moment (D) from MM2, MNDO, RHF/STO-3G, and RHF/3-21G optimizations. The hidden checker compares each parameter to the experimental reference from the paper, awarding full credit when the deviation is within a method‑specific tolerance (absolute error ≤ tolerance) and partial credit degrading as the error increases."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `theoretical_results.json`. For each method it compares every reported structural parameter and the dipole moment to the experimental reference (the microwave r_s structure and Stark‑effect dipole moment). Comparisons use method‑dependent tolerances that account for the systematic differences among the theoretical models. Your score is the fraction of all parameters across the four methods that fall within their respective tolerance windows. The verifier also verifies that the optimizations were carried out correctly (e.g., no imaginary frequencies for the HF methods, proper convergence). Simply reporting the paper’s numbers is not sufficient; the verifier assesses whether the quantities you computed from the actual calculations are sufficiently close to the experimental values.
