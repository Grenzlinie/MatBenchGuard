# Vibrational Analysis of Small Silicon-Containing Molecules

## Problem background
Infrared (IR) spectroscopy is a primary tool for studying silicate structures, but interpreting the spectra is difficult because of the complex bonding and coupling among vibrational modes. Quantum-chemical calculations can assist by predicting vibrational frequencies, normal modes, and IR intensities. The semi-empirical MNDO method is computationally efficient and has been applied to silicates. This task evaluates the MNDO method on five small silicon-containing benchmark molecules: SiH₄ (silane), SiF₄ (silicon tetrafluoride), Si(OH)₄ (orthosilicic acid), SiO₄⁴⁻ (orthosilicate), and Si₂O₇⁶⁻ (pyrosilicate). The open questions are whether MNDO geometry optimization reproduces the expected bond lengths and whether the calculated IR-active vibrational modes obey the correct symmetry patterns — two IR-active modes for tetrahedral (Td) species and degenerate modes for Si₂O₇⁶⁻ consistent with D3d symmetry. Answering these questions establishes the reliability of MNDO for interpreting silicate IR spectra.

## Approach
The approach uses semi-empirical quantum chemistry via the open-source MOPAC program implementing the MNDO method. For each of the five molecules, an initial geometry is built from standard experimental bond lengths and the expected molecular symmetry (Td for SiH₄, SiF₄, and SiO₄⁴⁻; S4 for Si(OH)₄; and D3d for Si₂O₇⁶⁻). Each structure is then fully optimized with MNDO. After optimization, force constants are computed numerically and the vibrational frequencies and normal modes are obtained through the GF matrix method. IR-active modes are identified using computed transition dipoles. The resulting optimized bond lengths are collected for comparison with reference values, and the IR-active frequencies with relative intensities are listed to allow verification of symmetry patterns (two IR-active modes for the Td molecules, degenerate patterns for Si₂O₇⁶⁻ consistent with D3d).

## Reproduction target
The task is to produce the optimized bond lengths (and angles where applicable) for SiH₄, SiF₄, Si(OH)₄, SiO₄⁴⁻, and Si₂O₇⁶⁻, together with the list of IR-active vibrational frequencies and their relative intensities. Bond lengths will be compared to reference values. The IR-active modes will be checked for correct symmetry: exactly two modes for SiH₄, SiF₄, and SiO₄⁴⁻ (Td); and degenerate modes for Si₂O₇⁶⁻ consistent with D3d. Absolute frequency values are not evaluated — only the symmetry pattern (number of IR-active modes and degeneracy) is scored. The outputs are `optimized_geometries.csv` and `ir_active_frequencies.json`, as specified in the workflow steps and output contract.

## Assets

- MOPAC (Molecular Orbital PACkage): https://github.com/openmopac/mopac

## Workflow steps

### Step 1: Prepare initial molecular geometries
- Role: process
- Action: Generate initial Cartesian coordinates for SiH4, SiF4, Si(OH)4, SiO4^4-, and Si2O7^6- using standard experimental bond lengths and symmetries (Td for SiH4, SiF4, SiO4^4-; S4 for Si(OH)4; D3d for Si2O7^6-).
- Evidence: none

### Step 2: Run MNDO geometry optimization and vibrational analysis
- Role: process
- Action: For each of the five molecules, execute MOPAC with the MNDO method to perform geometry optimization and vibrational analysis (computation of force constants, vibrational frequencies, and IR transition dipoles).
- Evidence: `/app/outputs/mopac_run_summary.log`

### Step 3: Extract optimized bond lengths and angles
- Role: scored (load-bearing)
- Action: Parse the MOPAC output files to obtain the optimized bond lengths and angles for each molecule. Write the results to optimized_geometries.csv.
- Output file: `/app/outputs/optimized_geometries.csv`
- Format: csv
- Contract: molecule:string, bond_type:string, length_Angstrom:float, angle_deg:float (optional; one row per unique bond/angle)
- Scoring: scored by hidden verifier

### Step 4: Extract IR-active frequencies and relative intensities
- Role: scored (load-bearing)
- Action: Parse the MOPAC frequency output to list all vibrational modes with non-zero IR intensity. For each molecule, report the IR-active frequencies and their relative intensities in ir_active_frequencies.json.
- Output file: `/app/outputs/ir_active_frequencies.json`
- Format: json
- Contract: array of objects with molecule:string, frequency_cm-1:float, relative_intensity:float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_geometries.csv`
- `/app/outputs/ir_active_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_geometries.csv
- path: `/app/outputs/optimized_geometries.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with one row per unique bond or angle per molecule. The checker will compare the bond lengths to hidden gold values from the paper's Table 1 within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `bond_type`, `length_Angstrom`
  - `optional_columns`: `angle_deg`
  - `units`:
    - `length_Angstrom`: Angstrom
    - `angle_deg`: degree

### ir_active_frequencies.json
- path: `/app/outputs/ir_active_frequencies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: JSON array of objects, each representing an IR-active mode. The checker will verify the number of IR-active modes per molecule and degeneracy pattern (two modes for Td species, degenerate modes for Si2O7^6- consistent with D3d symmetry). Exact frequency values are not validated; the symmetry pattern is scored.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `molecule`, `frequency_cm-1`, `relative_intensity`
    - `properties`:
      - `molecule`:
        - `type`: string
      - `frequency_cm-1`:
        - `type`: number
      - `relative_intensity`:
        - `type`: number

Notes: The task reproduces the core validation on small molecules only; larger silicate clusters are excluded per taskability scope. The solver may use a modern MOPAC version. The checker tolerates systematic absolute frequency shifts from MNDO and only checks symmetry patterns for IR spectra.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_geometries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "bond_type",
          "length_Angstrom"
        ],
        "optional_columns": [
          "angle_deg"
        ],
        "units": {
          "length_Angstrom": "Angstrom",
          "angle_deg": "degree"
        }
      },
      "description": "CSV file with one row per unique bond or angle per molecule. The checker will compare the bond lengths to hidden gold values from the paper's Table 1 within a tolerance."
    },
    {
      "file": "ir_active_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "molecule",
            "frequency_cm-1",
            "relative_intensity"
          ],
          "properties": {
            "molecule": {
              "type": "string"
            },
            "frequency_cm-1": {
              "type": "number"
            },
            "relative_intensity": {
              "type": "number"
            }
          }
        }
      },
      "description": "JSON array of objects, each representing an IR-active mode. The checker will verify the number of IR-active modes per molecule and degeneracy pattern (two modes for Td species, degenerate modes for Si2O7^6- consistent with D3d symmetry). Exact frequency values are not validated; the symmetry pattern is scored."
    }
  ],
  "notes": "The task reproduces the core validation on small molecules only; larger silicate clusters are excluded per taskability scope. The solver may use a modern MOPAC version. The checker tolerates systematic absolute frequency shifts from MNDO and only checks symmetry patterns for IR spectra."
}
```

## How you are scored
A hidden verifier scores each of the two required output files independently and combines them into a final reward between 0 and 1.

- **optimized_geometries.csv**: The verifier checks the reported bond lengths against reference values with a tolerance. Only bond-length accuracy is scored; angles are optional and not evaluated.
- **ir_active_frequencies.json**: The verifier checks the correct number of IR-active modes per molecule and the degeneracy pattern: exactly two modes for SiH₄, SiF₄, and SiO₄⁴⁻; degenerate modes for Si₂O₇⁶⁻ consistent with D3d. The exact frequency values are not evaluated. Si(OH)₄ is not assessed for its IR pattern.

Both stages carry substantial weight, with the headline symmetry check and bond-length accuracy comprising the majority of the reward. Reporting paper-like numbers without correctly produced artifacts will not earn credit.
