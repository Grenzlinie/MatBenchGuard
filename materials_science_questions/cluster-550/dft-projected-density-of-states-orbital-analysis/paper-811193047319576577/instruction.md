# DFT IR Frequencies, HOMO-LUMO Gaps, and Binding Energies of Cr(III) Complexes

## Problem background
Transition-metal complexes of semi- and thiosemicarbazides exhibit diverse coordination geometries that influence their chemical and biological properties. Infrared (IR) spectroscopy is a primary tool for inferring the ligand binding mode, but assignments often rely on comparison with theoretical spectra. Density functional theory (DFT) can predict vibrational frequencies, frontier molecular orbital energies, and thermodynamic stabilities independently. This task addresses the computational characterization of three ligands—H₂PAPS, H₂PAPT, H₂PABT—and their Cr(III) complexes. The goal is to compute the DFT harmonic vibrational frequencies that act as fingerprints of the proposed coordination modes, the HOMO–LUMO energy gaps and derived reactivity descriptors, and the binding energies of the complexes. These quantities provide a theoretical basis for interpreting the experimental IR bands and evaluating relative stability.

## Approach
The approach follows the standard computational workflow of applying unrestricted DFT to geometry optimization, followed by frequency and property calculations. You will construct molecular models for each ligand in its relevant tautomeric forms (keto/enol for H₂PAPS, thione/thiol for H₂PAPT and H₂PABT) and for the three Cr(III) complexes, respecting the reported coordination modes—neutral tridentate for H₂PAPS, monoanionic bidentate for H₂PAPT, and monoanionic tridentate for H₂PABT. After optimizing all geometries, you will compute harmonic vibrational frequencies to identify the diagnostic IR bands (carbonyls C=O¹, C=O², C=O³; azomethine C=N; N–N; and C=S/SH for the sulfur-containing ligands). You will extract the highest occupied (HOMO) and lowest unoccupied (LUMO) molecular orbital energies and derive global reactivity indices (electronegativity χ, hardness η, softness σ, electrophilicity ω) using the standard formulas. Finally, from the total energies of the optimized complexes and their constituent fragments, you will compute the binding energy and extract the dipole moment. The entire workflow may be performed with any open‑source DFT package such as ORCA. Optionally, a cheminformatics library (e.g., RDKit) may assist in generating initial 3D coordinates.

## Reproduction target
The concrete deliverables are three CSV files placed under `/app/outputs`:

- `computed_ir_frequencies.csv`: For each compound (three ligands and three complexes), report for each band label (`ν(C=O)¹`, `ν(C=O)²`, `ν(C=O)³`, `ν(C=N)`, `ν(N–N)`, and for H₂PAPT/H₂PABT `ν(C=S)`/`ν(SH)`) the computed harmonic frequency in cm⁻¹ (or null if absent), and a boolean `present` flag indicating whether the band appears in the calculated spectrum.
- `computed_homo_lumo_gaps.csv`: For each compound, provide the HOMO energy (eV), LUMO energy (eV), gap (eV), and the descriptors electronegativity, hardness, softness, and electrophilicity.
- `computed_binding_energies.csv`: For the three complexes, report the binding energy in kcal/mol and the dipole moment in Debye.

The values must be computed according to the procedure described; the verifier will check them against hidden references that account for the expected accuracy of the DFT method.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- RDKit: rdkit

## Workflow steps

### Step 1: DFT geometry optimization of ligands
- Role: process
- Action: Build molecular models of H₂PAPS, H₂PAPT, and H₂PABT in all relevant tautomeric forms (keto/enol for H₂PAPS, thione/thiol for H₂PAPT and H₂PABT). Perform unrestricted DFT geometry optimization to obtain stable ground-state geometries.
- Evidence: `/app/outputs/optimized_ligand_geometries.xyz`

### Step 2: DFT geometry optimization of Cr(III) complexes
- Role: process
- Action: Construct initial coordinates for the three complexes [Cr(H₂PAPS)Cl₃], [Cr(HPAPT)Cl₂(H₂O)₂], and [Cr(HPABT)Cl₂(H₂O)] according to the proposed coordination modes (neutral tridentate, monoanionic bidentate, monoanionic tridentate). Perform unrestricted DFT geometry optimization.
- Evidence: `/app/outputs/optimized_complex_geometries.xyz`

### Step 3: DFT vibrational frequencies and IR band assignment
- Role: scored (load-bearing)
- Action: Run DFT frequency calculations on the optimized geometries of all ligands (relevant tautomers) and all complexes. Extract key vibrational modes: ν(C=O)¹, ν(C=O)², ν(C=O)³, ν(C=N) (azomethine), ν(N-N), and for H₂PAPT/H₂PABT ν(C=S)/ν(SH) as applicable. For each compound and each band label, record the computed harmonic frequency (cm⁻¹) and whether the band is present (True) or absent (False).
- Output file: `/app/outputs/computed_ir_frequencies.csv`
- Format: csv
- Contract: compound (str), band_label (str), frequency_cm1 (float, nullable if absent), present (bool)
- Scoring: scored by hidden verifier

### Step 4: HOMO‑LUMO energies and global reactivity descriptors
- Role: scored (load-bearing)
- Action: Extract the HOMO and LUMO energies (eV) from the DFT output of all optimized ligands and complexes. Compute the energy gap ΔE = E_LUMO – E_HOMO. Additionally calculate global reactivity descriptors: electronegativity χ, chemical hardness η, softness σ, and electrophilicity index ω using standard formulas.
- Output file: `/app/outputs/computed_homo_lumo_gaps.csv`
- Format: csv
- Contract: compound (str), homo_eV (float), lumo_eV (float), gap_eV (float), electronegativity_eV (float), hardness_eV (float), softness_eV_recip (float), electrophilicity_eV (float)
- Scoring: scored by hidden verifier

### Step 5: Binding energies and dipole moments
- Role: scored
- Action: From the total energies of the optimized complexes and the appropriate fragments (free ligands in their optimal tautomeric form, Cr³⁺ ion, chloride ions, and water molecules as needed), compute the binding energy of each complex. Report the dipole moment (Debye) extracted from the DFT output.
- Output file: `/app/outputs/computed_binding_energies.csv`
- Format: csv
- Contract: compound (str), binding_energy_kcal_per_mol (float), dipole_moment_debye (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_ir_frequencies.csv`
- `/app/outputs/computed_homo_lumo_gaps.csv`
- `/app/outputs/computed_binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_ir_frequencies.csv
- path: `/app/outputs/computed_ir_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: DFT-computed harmonic frequencies and presence flags for IR bands of ligands and complexes.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `band_label`, `frequency_cm1`, `present`
  - `units`:
    - `frequency_cm1`: cm⁻¹
    - `present`: boolean

### computed_homo_lumo_gaps.csv
- path: `/app/outputs/computed_homo_lumo_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: HOMO and LUMO energies and derived global reactivity descriptors.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `homo_eV`, `lumo_eV`, `gap_eV`, `electronegativity_eV`, `hardness_eV`, `softness_eV_recip`, `electrophilicity_eV`
  - `units`:
    - `homo_eV`: eV
    - `lumo_eV`: eV
    - `gap_eV`: eV
    - `electronegativity_eV`: eV
    - `hardness_eV`: eV
    - `softness_eV_recip`: eV⁻¹
    - `electrophilicity_eV`: eV

### computed_binding_energies.csv
- path: `/app/outputs/computed_binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Binding energies and dipole moments for Cr(III) complexes.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `binding_energy_kcal_per_mol`, `dipole_moment_debye`
  - `units`:
    - `binding_energy_kcal_per_mol`: kcal/mol
    - `dipole_moment_debye`: Debye

Notes: The hidden checker compares the agent's computed values to paper-reported references using appropriate tolerances (e.g., ±30 cm⁻¹ for frequencies, ±0.2 eV for orbital energies, ±5 kcal/mol for binding energies, ±0.5 D for dipole moments). Presence flags must match expected disappearance patterns for certain bands.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_ir_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "band_label",
          "frequency_cm1",
          "present"
        ],
        "units": {
          "frequency_cm1": "cm⁻¹",
          "present": "boolean"
        }
      },
      "description": "DFT-computed harmonic frequencies and presence flags for IR bands of ligands and complexes."
    },
    {
      "file": "computed_homo_lumo_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "homo_eV",
          "lumo_eV",
          "gap_eV",
          "electronegativity_eV",
          "hardness_eV",
          "softness_eV_recip",
          "electrophilicity_eV"
        ],
        "units": {
          "homo_eV": "eV",
          "lumo_eV": "eV",
          "gap_eV": "eV",
          "electronegativity_eV": "eV",
          "hardness_eV": "eV",
          "softness_eV_recip": "eV⁻¹",
          "electrophilicity_eV": "eV"
        }
      },
      "description": "HOMO and LUMO energies and derived global reactivity descriptors."
    },
    {
      "file": "computed_binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "binding_energy_kcal_per_mol",
          "dipole_moment_debye"
        ],
        "units": {
          "binding_energy_kcal_per_mol": "kcal/mol",
          "dipole_moment_debye": "Debye"
        }
      },
      "description": "Binding energies and dipole moments for Cr(III) complexes."
    }
  ],
  "notes": "The hidden checker compares the agent's computed values to paper-reported references using appropriate tolerances (e.g., ±30 cm⁻¹ for frequencies, ±0.2 eV for orbital energies, ±5 kcal/mol for binding energies, ±0.5 D for dipole moments). Presence flags must match expected disappearance patterns for certain bands."
}
```

## How you are scored
A hidden verifier evaluates your three output files independently. For the IR frequencies, it compares each computed frequency to a hidden reference value (within a tolerance that accounts for the expected shift from the chosen DFT functional and basis set) and verifies the presence/absence flag matches the expected coordination pattern. For the HOMO–LUMO descriptors, it checks that your computed values lie within an acceptable range of hidden reference values. For the binding energies and dipole moments, it similarly compares to hidden reference numbers. Each file is assigned a score based on the fraction of correct entries, and the final reward is a weighted sum of these file-level scores. Simply reproducing the paper’s numbers without performing actual DFT calculations will not pass: the verification tolerances are set so that a genuine re‑computation with a comparable methodology must be carried out. No paper identity or gold values are disclosed.
