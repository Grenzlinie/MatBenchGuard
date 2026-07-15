# Sodium Binding Enthalpies of MALDI Matrix Molecules via Ab Initio Calculations

## Problem background
In matrix-assisted laser desorption ionization (MALDI) mass spectrometry, the gas-phase interaction of sodium cations (Na⁺) with organic matrix molecules influences the formation of sodiated analyte ions and the observed mass spectra. Understanding the sodium ion binding affinities of common MALDI matrix molecules helps evaluate secondary ion‑molecule reactions in the MALDI plume. This task addresses the computational determination of accurate gas‑phase sodium ion binding enthalpies and free energies for six widely used MALDI matrix acids using ab initio quantum chemistry methods.

## Approach
The computational approach uses a two‑level ab initio strategy. For each molecule (and for the various plausible binding isomers of the sodium complex), an initial three‑dimensional molecular structure is generated. Geometry optimizations and vibrational frequency calculations are performed at the Hartree–Fock level with a double‑zeta polarized basis set (HF/6‑31G*). These provide the optimized geometries, zero‑point vibrational energies, and thermal corrections at 298 K. Single‑point energy calculations are then carried out at the second‑order Møller–Plesset level (MP2) with a larger, doubly polarized triple‑zeta basis set augmented with diffuse functions (6‑311+G(2d,2p)) to obtain accurate electronic energies. Sodium binding enthalpies and free energies are obtained as the energy difference between the sodiated complex and the separated neutral molecule plus Na⁺ ion, including zero‑point and thermal corrections. For each molecule, the lowest‑energy isomer of the sodium complex and the most stable conformer of the neutral molecule are used. The workflow uses the open‑source quantum chemistry package ORCA as the computational engine, replacing the proprietary Gaussian code used in the original work.

## Reproduction target
Compute and report the following quantities at the MP2/6‑311+G(2d,2p)//HF/6‑31G* level of theory, including zero‑point and thermal corrections at 298 K:
- Sodium binding enthalpy (ΔH₂₉₈) and free energy (ΔG₂₉₈) for each of the six MALDI matrix molecules: 2,5‑dihydroxybenzoic acid (DHB), sinapinic acid (SA), 4‑hydroxy‑α‑cyanocinnamic acid (4‑HCCA), picolinic acid (PA), nicotinic acid (NA), and anthranilic acid (AA).
- Relative enthalpies (ΔH₂₉₈) of the eight DHB–Na⁺ isomers (labeled 1–8) with respect to isomer 1.
Write the results into two CSV files: `binding_enthalpies.csv` and `dhb_isomer_energies.csv`, following the output contract specifications.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- NumPy: numpy
- Pandas: pandas
- RDKit: rdkit
- OpenBabel: https://openbabel.org

## Workflow steps

### Step 1: Prepare initial molecular geometries
- Role: process
- Action: Generate initial 3D structures for all neutral acids, sodiated complexes (all isomers considered in the paper for DHB, SA, 4-HCCA, PA, NA, AA), and the Na+ ion. Use SMILES notation and chemical knowledge; produce XYZ files for each species.
- Evidence: none

### Step 2: HF/6-31G* geometry optimization and frequency calculation
- Role: process
- Action: For each species, run a Hartree–Fock/6-31G* geometry optimization and vibrational frequency calculation using ORCA. Save optimized geometries and thermodynamic data (zero-point energies, thermal corrections at 298 K).
- Evidence: none

### Step 3: MP2/6-311+G(2d,2p) single-point energies
- Role: process
- Action: For each HF-optimized geometry, run an MP2 single-point energy calculation with the 6-311+G(2d,2p) basis set (no frozen core) using ORCA. Extract the total electronic energy.
- Evidence: none

### Step 4: Compute binding enthalpies and free energies
- Role: scored (load-bearing)
- Action: Combine the MP2 total energies with HF zero-point and thermal corrections (no scaling) to compute the Na+ binding enthalpy ΔH298 and free energy ΔG298 for each of the six molecules (DHB, SA, 4-HCCA, PA, NA, AA) at the MP2/6-311+G(2d,2p)//HF/6-31G* level. Report results in binding_enthalpies.csv.
- Output file: `/app/outputs/binding_enthalpies.csv`
- Format: csv
- Contract: Columns: molecule (string), delta_H298_kcalmol (float), delta_G298_kcalmol (float). One row per molecule: DHB, SA, 4-HCCA, PA, NA, AA.
- Scoring: scored by hidden verifier

### Step 5: Compute relative energies of DHB-Na+ isomers
- Role: scored (load-bearing)
- Action: Using MP2 and HF data, compute the relative energy (ΔH298) of each DHB-Na+ isomer 2–8 with respect to isomer 1 (set to 0). Write dhb_isomer_energies.csv.
- Output file: `/app/outputs/dhb_isomer_energies.csv`
- Format: csv
- Contract: Columns: isomer_label (integer 1-8), relative_delta_H_kcalmol (float). If an isomer could not be located, use 'not found'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_enthalpies.csv`
- `/app/outputs/dhb_isomer_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_enthalpies.csv
- path: `/app/outputs/binding_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sodium binding enthalpies and free energies at 298 K for the six MALDI matrix molecules DHB, SA, 4-HCCA, PA, NA, AA, computed at the MP2/6-311+G(2d,2p)//HF/6-31G* level including ZPVE and thermal corrections.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `delta_H298_kcalmol`, `delta_G298_kcalmol`
  - `units`:
    - `delta_H298_kcalmol`: kcal/mol
    - `delta_G298_kcalmol`: kcal/mol

### dhb_isomer_energies.csv
- path: `/app/outputs/dhb_isomer_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relative enthalpies (ΔH298) of DHB-Na+ isomers 1-8 at the MP2/6-311+G(2d,2p)//HF/6-31G* level, with isomer 1 as reference (0.0 kcal/mol).
- schema:
  - `type`: table
  - `required_columns`: `isomer_label`, `relative_delta_H_kcalmol`
  - `units`:
    - `relative_delta_H_kcalmol`: kcal/mol

Notes: The hidden checker compares the reported binding enthalpies and free energies to paper-reported values with appropriate tolerances, and verifies relative ordering and key energy differences for DHB isomers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "delta_H298_kcalmol",
          "delta_G298_kcalmol"
        ],
        "units": {
          "delta_H298_kcalmol": "kcal/mol",
          "delta_G298_kcalmol": "kcal/mol"
        }
      },
      "description": "Sodium binding enthalpies and free energies at 298 K for the six MALDI matrix molecules DHB, SA, 4-HCCA, PA, NA, AA, computed at the MP2/6-311+G(2d,2p)//HF/6-31G* level including ZPVE and thermal corrections."
    },
    {
      "file": "dhb_isomer_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "isomer_label",
          "relative_delta_H_kcalmol"
        ],
        "units": {
          "relative_delta_H_kcalmol": "kcal/mol"
        }
      },
      "description": "Relative enthalpies (ΔH298) of DHB-Na+ isomers 1-8 at the MP2/6-311+G(2d,2p)//HF/6-31G* level, with isomer 1 as reference (0.0 kcal/mol)."
    }
  ],
  "notes": "The hidden checker compares the reported binding enthalpies and free energies to paper-reported values with appropriate tolerances, and verifies relative ordering and key energy differences for DHB isomers."
}
```

## How you are scored
A hidden verifier reads your two output CSV files and scores them independently. For `binding_enthalpies.csv`, the verifier compares your reported ΔH₂₉₈ and ΔG₂₉₈ values to reference values (with tolerances that account for legitimate computational variability due to different software and settings) and checks that the relative ordering of binding enthalpies among the six molecules follows the physically expected trend. For `dhb_isomer_energies.csv`, the verifier compares the relative energies to reference values and checks key structural relationships (e.g., the energy ranking of isomers). Both scored outputs contribute to a final weighted reward; you must produce both files with the correct structure to be scored. The exact tolerances and reference values are not provided to you; your job is to perform the calculations faithfully and report the results.
