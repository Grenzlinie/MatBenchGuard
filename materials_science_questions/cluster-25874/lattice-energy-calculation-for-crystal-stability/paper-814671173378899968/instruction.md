# TD-DFT excitation energies and colour of organic molecular crystals

## Problem background
Certain substituted fulgide derivatives exhibit a striking colour change upon crushing: yellow crystals turn into a deep red powder. This phenomenon, termed tribochromism, is thought to arise from differences in molecular conformation, but the precise electronic origin of the colour difference is unknown. Understanding how molecular geometry affects electronic excitation energies is key to explaining the observed colour polymorphism.

## Approach
Use density functional theory to compute ground-state electronic structures and time-dependent DFT to obtain vertical excitation energies. Starting from the experimental crystal structures (CIF files) of five related compounds, extract a single molecule of each, optimize its geometry at the BLYP-D/TZVPP level both in vacuum and in a continuum solvent environment (COSMO, with refractive index 75 and dielectric constant 3.0, modelling an organic crystal). Then perform TD-DFT single-point calculations with the B2PLYP double-hybrid functional and TZVP basis to determine the HOMO-LUMO gap and the energy of the first singlet excited state. For a subset of molecules, attempt to optimize the excited-state geometry at the BLYP/TZVP level (no dispersion) to estimate an adiabatic correction. The results for all molecules will be compared to see whether a clear relationship exists between the molecular conformation (as found in the crystals) and the computed excitation energies.

## Reproduction target
Produce a CSV file containing, for each of the five compounds I, II, IIIa, IIIb, IV, the HOMO-LUMO gap (eV), the first singlet vertical excitation energy in the gas phase (eV), the same energy with the COSMO solvation model (eV), and the adiabatic correction (eV) or the string 'failed' if the optimization could not be completed. All values must be derived from the specified ORCA workflow; no pre-computed data may be used. The relative ordering of these energies across the molecules, in relation to their conformations, is part of the verification.

## Assets

- CIF files for compounds I, II, IIIa, IIIb, IV: https://doi.org/10.1186/s13065-014-0070-3
- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Extract molecular geometries from crystal structures
- Role: process
- Action: For each of the five compounds (I, II, IIIa, IIIb, IV), extract the geometry of a single molecule from the corresponding CIF file to generate initial Cartesian coordinates compatible with ORCA input.
- Evidence: `/app/outputs/extracted_geometries.txt`

### Step 2: Optimize ground-state geometries
- Role: process
- Action: For each molecule, perform geometry optimisations using ORCA with the BLYP functional, a dispersion correction (BLYP-D), and the TZVPP basis set. Run optimisations both in the gas phase and with the COSMO solvation model (refractive index 75, dielectric constant 3.0).
- Evidence: `/app/outputs/optimization_outputs.zip`

### Step 3: Run TD-DFT and compile electronic excitation results
- Role: scored (load-bearing)
- Action: At each optimised geometry, perform TD-DFT calculations with the B2PLYP double-hybrid functional and the TZVP basis set to compute the HOMO-LUMO gap and the first singlet vertical excitation energy (gas phase and COSMO). For molecules I, IIIa, and IV attempt excited-state geometry optimisation at the BLYP/TZVP level (no dispersion) to estimate adiabatic corrections; for II and IIIb note that the optimisation fails. Assemble all results into a CSV file.
- Output file: `/app/outputs/molecular_calculations_results.csv`
- Format: csv
- Contract: Columns: molecule (string), HOMO_LUMO_gap_eV (float), gas_phase_excitation_eV (float), COSMO_excitation_eV (float), adiabatic_correction_eV (float or string 'failed')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/molecular_calculations_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### molecular_calculations_results.csv
- path: `/app/outputs/molecular_calculations_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored electronic-structure results: for the five molecules (I, II, IIIa, IIIb, IV) report the HOMO-LUMO gap, the first singlet vertical excitation energy in the gas phase and with the COSMO continuum model, and the adiabatic correction or 'failed' if the excited-state optimisation did not converge.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `HOMO_LUMO_gap_eV`, `gas_phase_excitation_eV`, `COSMO_excitation_eV`, `adiabatic_correction_eV`
  - `units`:
    - `HOMO_LUMO_gap_eV`: eV
    - `gas_phase_excitation_eV`: eV
    - `COSMO_excitation_eV`: eV
    - `adiabatic_correction_eV`: eV (or the string 'failed')

Notes: All values must originate from the described ORCA workflow (no pre-computed data from the paper). The scorer will compare each numeric entry to a hidden reference (the paper's Table 4) with domain-appropriate tolerances and will also verify the trend that twisted conformers exhibit lower gaps and excitation energies than folded conformers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "molecular_calculations_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "HOMO_LUMO_gap_eV",
          "gas_phase_excitation_eV",
          "COSMO_excitation_eV",
          "adiabatic_correction_eV"
        ],
        "units": {
          "HOMO_LUMO_gap_eV": "eV",
          "gas_phase_excitation_eV": "eV",
          "COSMO_excitation_eV": "eV",
          "adiabatic_correction_eV": "eV (or the string 'failed')"
        }
      },
      "description": "Scored electronic-structure results: for the five molecules (I, II, IIIa, IIIb, IV) report the HOMO-LUMO gap, the first singlet vertical excitation energy in the gas phase and with the COSMO continuum model, and the adiabatic correction or 'failed' if the excited-state optimisation did not converge."
    }
  ],
  "notes": "All values must originate from the described ORCA workflow (no pre-computed data from the paper). The scorer will compare each numeric entry to a hidden reference (the paper's Table 4) with domain-appropriate tolerances and will also verify the trend that twisted conformers exhibit lower gaps and excitation energies than folded conformers."
}
```

## How you are scored
A hidden verifier will read your CSV and compare each numeric entry to reference values with a predefined tolerance. It will also examine the relative magnitudes of the HOMO-LUMO gaps and excitation energies across the five molecules to confirm that they follow the physically expected trend consistent with the conformations present. Each correctly matched entry and a correct overall trend contribute to the final reward; the reward is proportional to the number of successfully verified entries.
