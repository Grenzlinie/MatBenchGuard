# DFT Electronic Properties of Organosilicon(IV) Complexes

## Problem background
Organosilicon(IV) complexes with Schiff base ligands are of interest for their structural, electronic, and biological properties. Density functional theory (DFT) calculations provide insight into frontier orbital energies, energy gaps, and dipole moments, which are relevant for understanding reactivity and potential bioactivity. Reproducing the computed electronic properties of a representative free ligand and its organosilicon complexes helps validate the computational methodology employed. This task focuses on the DFT characterization of three molecules: the Schiff base L³H and its complexes Me₃SiL³ and PhSiL³OEt. The goal is to compute their optimized geometries and electronic parameters using a widely used quantum chemical approach.

## Approach
Use density functional theory with the B3LYP hybrid exchange–correlation functional and the 6-31++G(d,p) basis set. The workflow involves:
1. Building initial 3D structures from the SMILES strings provided below.
2. Performing a geometry optimization for each molecule to a local minimum.
3. Extracting from the final optimized wavefunction the SCF energy, the energies of the highest occupied (HOMO) and lowest unoccupied (LUMO) molecular orbitals, the HOMO–LUMO gap, and the total dipole moment.

Any open‑source quantum chemistry package that supports B3LYP/6‑31++G(d,p) geometry optimization may be used (e.g., ORCA, NWChem, Psi4, PySCF). The three molecules are:
- **L³H** (free Schiff base): `Oc1ccccc1C(N2CCCC2)=NNC(=O)N`
- **Me₃SiL³** (trimethylsilicon complex): `C[Si]1(C)(C)Oc2ccccc2C(N3CCCC3)=[N]1N=C(N)O`
- **PhSiL³OEt** (phenyl silicon ethoxy complex): `CCO[Si]1(c2ccccc2)Oc3ccccc3C(N4CCCC4)=[N]1N=C(N)O`

The SMILES for the complexes are approximate; the geometry optimization will relax to the correct coordination environment.

## Reproduction target
Perform a DFT geometry optimization for each of the three molecules (L³H, Me₃SiL³, PhSiL³OEt) at the B3LYP/6‑31++G(d,p) level of theory. From the final SCF step of each optimization, extract:
- SCF energy (in atomic units, Hartree)
- HOMO energy (in eV)
- LUMO energy (in eV)
- HOMO–LUMO gap (in eV)
- Dipole moment (in Debye)
Write these values into a JSON file `dft_results.json` with one entry per molecule, each containing the fields `scf_energy`, `homo`, `lumo`, `gap`, and `dipole`. The exact schema is described in the Output Contract.

## Assets

- Open-source quantum chemistry package supporting B3LYP/6-31++G(d,p) (ORCA, NWChem, Psi4, PySCF, etc.): https://orcaforum.kofo.mpg.de/
- SMILES strings for L3H, Me3SiL3, and PhSiL3OEt

## Workflow steps

### Step 1: Build molecular structures
- Role: process
- Action: From the provided SMILES strings for the three molecules (L3H, Me3SiL3, PhSiL3OEt), generate initial three-dimensional atomic coordinates using a molecular builder (e.g., Open Babel or RDKit). Save the initial structures in XYZ format.
- Evidence: `/app/outputs/initial_structures.zip`

### Step 2: DFT geometry optimization
- Role: process
- Action: For each of the three molecules (L3H, Me3SiL3, PhSiL3OEt), perform a DFT geometry optimization using the B3LYP functional and the 6-31++G(d,p) basis set with an open-source quantum chemistry package. Save the optimization output logs and the final optimized coordinates.
- Evidence: `/app/outputs/opt_outputs.zip`

### Step 3: Extract electronic properties
- Role: scored (load-bearing)
- Action: From the final SCF step of each optimization, extract the SCF energy (in atomic units), the HOMO and LUMO energies (in eV), the HOMO-LUMO energy gap (in eV), and the dipole moment (in Debye). Write these values into a JSON file `dft_results.json` with one entry per molecule, each containing the fields scf_energy, homo, lumo, gap, and dipole.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: object with keys 'L3H', 'Me3SiL3', 'PhSiL3OEt'; each value is an object with numeric fields: scf_energy (Hartree), homo (eV), lumo (eV), gap (eV), dipole (Debye)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: DFT-derived electronic properties for the three molecules. The checker reads these values and compares them to hidden gold values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `L3H`:
      - `type`: object
      - `required`: `scf_energy`, `homo`, `lumo`, `gap`, `dipole`
      - `properties`:
        - `scf_energy`:
          - `type`: number
          - `unit`: Hartree
        - `homo`:
          - `type`: number
          - `unit`: eV
        - `lumo`:
          - `type`: number
          - `unit`: eV
        - `gap`:
          - `type`: number
          - `unit`: eV
        - `dipole`:
          - `type`: number
          - `unit`: Debye
    - `Me3SiL3`:
      - `type`: object
      - `required`: `scf_energy`, `homo`, `lumo`, `gap`, `dipole`
      - `properties`:
        - `scf_energy`:
          - `type`: number
          - `unit`: Hartree
        - `homo`:
          - `type`: number
          - `unit`: eV
        - `lumo`:
          - `type`: number
          - `unit`: eV
        - `gap`:
          - `type`: number
          - `unit`: eV
        - `dipole`:
          - `type`: number
          - `unit`: Debye
    - `PhSiL3OEt`:
      - `type`: object
      - `required`: `scf_energy`, `homo`, `lumo`, `gap`, `dipole`
      - `properties`:
        - `scf_energy`:
          - `type`: number
          - `unit`: Hartree
        - `homo`:
          - `type`: number
          - `unit`: eV
        - `lumo`:
          - `type`: number
          - `unit`: eV
        - `gap`:
          - `type`: number
          - `unit`: eV
        - `dipole`:
          - `type`: number
          - `unit`: Debye

Notes: The hidden gold values are taken from Table 3 of the source paper. Tolerances are set to account for differences between DFT implementations and basis set variations. The output contract defines the exact structure expected; any deviation in keys, units, or missing fields results in a score of zero for that entry.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "L3H": {
            "type": "object",
            "required": [
              "scf_energy",
              "homo",
              "lumo",
              "gap",
              "dipole"
            ],
            "properties": {
              "scf_energy": {
                "type": "number",
                "unit": "Hartree"
              },
              "homo": {
                "type": "number",
                "unit": "eV"
              },
              "lumo": {
                "type": "number",
                "unit": "eV"
              },
              "gap": {
                "type": "number",
                "unit": "eV"
              },
              "dipole": {
                "type": "number",
                "unit": "Debye"
              }
            }
          },
          "Me3SiL3": {
            "type": "object",
            "required": [
              "scf_energy",
              "homo",
              "lumo",
              "gap",
              "dipole"
            ],
            "properties": {
              "scf_energy": {
                "type": "number",
                "unit": "Hartree"
              },
              "homo": {
                "type": "number",
                "unit": "eV"
              },
              "lumo": {
                "type": "number",
                "unit": "eV"
              },
              "gap": {
                "type": "number",
                "unit": "eV"
              },
              "dipole": {
                "type": "number",
                "unit": "Debye"
              }
            }
          },
          "PhSiL3OEt": {
            "type": "object",
            "required": [
              "scf_energy",
              "homo",
              "lumo",
              "gap",
              "dipole"
            ],
            "properties": {
              "scf_energy": {
                "type": "number",
                "unit": "Hartree"
              },
              "homo": {
                "type": "number",
                "unit": "eV"
              },
              "lumo": {
                "type": "number",
                "unit": "eV"
              },
              "gap": {
                "type": "number",
                "unit": "eV"
              },
              "dipole": {
                "type": "number",
                "unit": "Debye"
              }
            }
          }
        }
      },
      "description": "DFT-derived electronic properties for the three molecules. The checker reads these values and compares them to hidden gold values with tolerances."
    }
  ],
  "notes": "The hidden gold values are taken from Table 3 of the source paper. Tolerances are set to account for differences between DFT implementations and basis set variations. The output contract defines the exact structure expected; any deviation in keys, units, or missing fields results in a score of zero for that entry."
}
```

## How you are scored
A hidden verifier reads your `dft_results.json`. For each molecule it compares each of the five reported properties (SCF energy, HOMO, LUMO, gap, dipole) to independently obtained reference values. Agreement within a tolerance earns full credit for that value; results outside the tolerance earn partial or no credit, scaled linearly with the deviation. The overall score is the weighted average over all values across the three molecules. The verifier also checks that the JSON file strictly follows the schema (required keys, numeric fields, correct units). Missing or misnamed fields result in zero credit for that entry.
