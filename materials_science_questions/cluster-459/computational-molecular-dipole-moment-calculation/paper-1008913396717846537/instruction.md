# DFT Calculation of Dipole Moments and HOMO-LUMO Gaps for Methacrylate Side-Chain Units

## Problem background
Dielectric polymer capacitors require a combination of high energy density, low loss, and good processability. Fluorination of glassy polymers has been proposed as a way to enhance energy storage by modifying the dipole moments and electronic structure of the polymer side chains. Computational characterization of these side-chain units can help explain the experimentally observed trade-offs. This task computes the dipole moments (in Debye) of three methacrylate side-chain units — methyl methacrylate (MMA), ethyl methacrylate (EMA), and trifluoroethyl methacrylate (3FEMA) — and the HOMO‑LUMO gaps (in eV) of the EMA and 3FEMA units via density functional theory. The computed properties quantify the effect of chain lengthening and fluorine substitution on molecular polarity and electronic gaps.

## Approach
Use density functional theory at the B3LYP/3-21G level to perform gas-phase calculations on the isolated side-chain molecules. For each of MMA, EMA, and 3FEMA, carry out a full geometry optimization to obtain the ground-state molecular structure. Then run a single‑point calculation on each optimized geometry to extract the total dipole moment vector and the frontier molecular orbital energies. Compute the magnitude of the dipole moment for each molecule and the HOMO‑LUMO energy gap for EMA and 3FEMA. All calculations may be performed with any open‑source quantum chemistry package that supports the B3LYP functional and the 3‑21G basis set, such as Psi4, ORCA, or NWChem.

## Reproduction target
Write the optimized Cartesian coordinates for MMA, EMA, and 3FEMA to 'optimized_geometries.xyz' in standard multi‑molecule XYZ format. Produce a JSON file, 'computed_properties.json', containing the following numeric entries: dipole_MMA (Debye), dipole_EMA (Debye), dipole_3FEMA (Debye), HOMO_LUMO_EMA (eV), and HOMO_LUMO_3FEMA (eV). All values must be obtained from DFT calculations at the B3LYP/3-21G level.

## Assets

- Open-source quantum chemistry package (e.g. Psi4, ORCA, NWChem): https://psicode.org/

## Workflow steps

### Step 1: DFT geometry optimization
- Role: scored
- Action: Perform DFT geometry optimization for the side-chain units MMA (methyl methacrylate), EMA (ethyl methacrylate), and 3FEMA (trifluoroethyl methacrylate) at the B3LYP/3-21G level of theory. Write the optimized Cartesian coordinates to 'optimized_geometries.xyz' in standard XYZ format (one block per molecule). Each block begins with the number of atoms on the first line, a comment line (e.g., molecule name), and then one line per atom with element symbol and x, y, z coordinates in Ångströms.
- Output file: `/app/outputs/optimized_geometries.xyz`
- Format: txt
- Contract: XYZ text file containing three structure blocks in sequence. Each block: first line = integer atom count (15 for MMA, 18 for EMA, 18 for 3FEMA), second line = comment, subsequent lines = element symbol and three floating-point coordinates (Å).
- Scoring: scored by hidden verifier

### Step 2: Compute dipole moments and HOMO-LUMO gaps
- Role: scored (load-bearing)
- Action: Using the optimized geometries from step 1, run a single-point DFT calculation at the same B3LYP/3-21G level of theory to obtain the total dipole moment vectors (Debye) for MMA, EMA, and 3FEMA, and the HOMO-LUMO gaps (eV) for EMA and 3FEMA. Compute the magnitude of the dipole moment for each. Write a JSON file 'computed_properties.json' containing the keys: dipole_MMA (float, Debye), dipole_EMA (float, Debye), dipole_3FEMA (float, Debye), HOMO_LUMO_EMA (float, eV), HOMO_LUMO_3FEMA (float, eV).
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: JSON object with numeric fields: dipole_MMA, dipole_EMA, dipole_3FEMA (in Debye); HOMO_LUMO_EMA, HOMO_LUMO_3FEMA (in eV). All required.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_geometries.xyz`
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_geometries.xyz
- path: `/app/outputs/optimized_geometries.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optimized molecular geometries for MMA, EMA, and 3FEMA. The checker validates file format, non-empty content, and approximate atom counts for each molecule.
- schema:
  - `type`: other
  - `description`: XYZ text file with three molecule blocks in sequence; each block: first line integer atom count (MMA 15, EMA 18, 3FEMA 18), second line comment, then atom lines with element symbol and three Cartesian coordinates in Å.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT computed dipole moments and HOMO-LUMO gaps for the three methacrylate derivatives. Each number is compared to the hidden reference (the paper-reported value) within an allowed relative tolerance.
- schema:
  - `type`: object
  - `required`:
    - `dipole_MMA`: number
    - `dipole_EMA`: number
    - `dipole_3FEMA`: number
    - `HOMO_LUMO_EMA`: number
    - `HOMO_LUMO_3FEMA`: number
  - `units`:
    - `dipole_MMA`: Debye
    - `dipole_EMA`: Debye
    - `dipole_3FEMA`: Debye
    - `HOMO_LUMO_EMA`: eV
    - `HOMO_LUMO_3FEMA`: eV

Notes: The XYZ output is sanity-checked for correct format and approximate atom counts. The JSON properties are compared to reference values computed using the same level of theory.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_geometries.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "other",
        "description": "XYZ text file with three molecule blocks in sequence; each block: first line integer atom count (MMA 15, EMA 18, 3FEMA 18), second line comment, then atom lines with element symbol and three Cartesian coordinates in Å."
      },
      "description": "Optimized molecular geometries for MMA, EMA, and 3FEMA. The checker validates file format, non-empty content, and approximate atom counts for each molecule."
    },
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "dipole_MMA": "number",
          "dipole_EMA": "number",
          "dipole_3FEMA": "number",
          "HOMO_LUMO_EMA": "number",
          "HOMO_LUMO_3FEMA": "number"
        },
        "units": {
          "dipole_MMA": "Debye",
          "dipole_EMA": "Debye",
          "dipole_3FEMA": "Debye",
          "HOMO_LUMO_EMA": "eV",
          "HOMO_LUMO_3FEMA": "eV"
        }
      },
      "description": "DFT computed dipole moments and HOMO-LUMO gaps for the three methacrylate derivatives. Each number is compared to the hidden reference (the paper-reported value) within an allowed relative tolerance."
    }
  ],
  "notes": "The XYZ output is sanity-checked for correct format and approximate atom counts. The JSON properties are compared to reference values computed using the same level of theory."
}
```

## How you are scored
A hidden verifier inspects each required output file separately. The 'optimized_geometries.xyz' file is checked for valid XYZ structure and approximate atom counts. The entries in 'computed_properties.json' are compared against hidden reference values obtained from the same level of theory using an appropriate tolerance. Each scored stage contributes a weighted portion to the final reward; reporting a number without performing the underlying DFT calculations is not sufficient.
