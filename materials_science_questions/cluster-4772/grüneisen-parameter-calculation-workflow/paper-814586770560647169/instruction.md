# DFT calculation of mode Grüneisen parameters and thermal expansion of trigonal H3[Co(CN)6]

## Problem background
Flexible framework structures such as cyanide-bridged coordination polymers display unusual thermal expansion behaviour driven by soft phonon modes. H3[Co(CN)6] crystallises in a trigonal structure (space group P-31m) containing linear Co–C–N–H–N–C–Co linkages. Anisotropic lattice vibrations produce both positive and negative contributions to the overall thermal expansion. First-principles phonon calculations can identify which modes are soft, quantify their Grüneisen parameters, and predict the resulting volumetric thermal expansion coefficient under the quasiharmonic approximation.

## Approach
Use an open‑source DFT code (Quantum ESPRESSO) with the PBE functional and PAW pseudopotentials to relax the trigonal H3[Co(CN)6] structure. Compute the elastic constants and zone‑centre phonon frequencies, then obtain the complete phonon eigenvectors. To derive mode Grüneisen parameters, perform phonon calculations at several volumes around equilibrium (e.g. ±10%) and use finite‑volume differences. Fit the total‑energy vs. volume data to a Birch–Murnaghan equation of state to obtain the bulk modulus. Finally, calculate the volumetric thermal expansion coefficient at 300 K using the mode Grüneisen parameters, bulk modulus, and molar volume within the Einstein specific‑heat model of the quasiharmonic approximation. The open‑source package Phonopy is used to construct supercells, post‑process DFPT forces, and compute Grüneisen parameters.

## Reproduction target
Produce two scored artifacts: (1) a CSV file listing every zone‑centre optical phonon mode with its frequency, symmetry label, Grüneisen parameter, and degeneracy; (2) a JSON file containing the relaxed lattice parameters, the bulk modulus, and the volumetric thermal expansion coefficient computed at 300 K. At least two optical modes must exhibit negative Grüneisen parameters, reflecting the presence of soft phonon branches.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE, PAW) for H, Co, C, N: https://www.materialscloud.org/discover/sssp/table
- Phonopy: https://phonopy.github.io/phonopy/
- Crystal structure of H3[Co(CN)6] (trigonal, space group P-31m): 10.1088/0953-8984/22/40/404202

## Workflow steps

### Step 1: DFT structure relaxation
- Role: process
- Action: Set up the trigonal H3[Co(CN)6] structure (space group P-31m) from the public CIF and perform DFT relaxation of lattice parameters and atomic positions using Quantum ESPRESSO with the PBE functional.
- Evidence: `/app/outputs/relax.log`

### Step 2: Phonon and Grüneisen parameter calculations
- Role: process
- Action: Using Phonopy and Quantum ESPRESSO DFPT: compute (1) elastic constants at the relaxed volume; (2) zone-center phonon frequencies and eigenvectors; (3) DFPT forces at volumes varied by ±10% around equilibrium; (4) fit volume-energy data to the Birch-Murnaghan equation of state to obtain bulk modulus B0; (5) compute mode Grüneisen parameters for all optical modes via finite-volume differences.
- Evidence: `/app/outputs/gruneisen_calc.log`

### Step 3: Output mode Grüneisen parameters table
- Role: scored (load-bearing)
- Action: Assemble the computed zone-center optical phonon frequencies and their mode Grüneisen parameters into a CSV file.
- Output file: `/app/outputs/mode_gruneisen.csv`
- Format: csv
- Contract: Columns: mode_index (int), frequency_cm1 (float), symmetry (str), gamma (float), degeneracy (int). One row per optical branch.
- Scoring: scored by hidden verifier

### Step 4: Output thermal expansion coefficient
- Role: scored
- Action: Compute the volumetric thermal expansion coefficient at 300 K using the mode Grüneisen parameters, bulk modulus, and molar volume under the Einstein model within the quasiharmonic approximation. Write the results to a JSON file.
- Output file: `/app/outputs/thermal_expansion.json`
- Format: json
- Contract: {'relaxed_lattice_parameters': {'a': float (Å), 'c': float (Å)}, 'bulk_modulus_B0': float (GPa), 'thermal_expansion_coefficient_300K': float (K⁻¹)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mode_gruneisen.csv`
- `/app/outputs/thermal_expansion.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mode_gruneisen.csv
- path: `/app/outputs/mode_gruneisen.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Table of all zone-center optical phonon modes with frequencies, Grüneisen parameters, symmetry labels, and degeneracies. The checker verifies structural properties: correct number of modes (at least 30), presence of at least two negative gamma values, and physically plausible values.
- schema:
  - `type`: table
  - `required_columns`: `mode_index`, `frequency_cm1`, `gamma`, `degeneracy`
  - `units`:
    - `frequency_cm1`: cm⁻¹
    - `gamma`: dimensionless

### thermal_expansion.json
- path: `/app/outputs/thermal_expansion.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Contains the relaxed lattice parameters, bulk modulus, and computed volumetric thermal expansion coefficient at 300 K. The checker recomputes the thermal expansion coefficient from the submitted mode_gruneisen.csv and compares the result to the hidden paper-reported value using a tolerance that absorbs toolchain differences.
- schema:
  - `type`: object
  - `required`: `relaxed_lattice_parameters`, `bulk_modulus_B0`, `thermal_expansion_coefficient_300K`
  - `items`:
    - `relaxed_lattice_parameters`:
      - `a`: float (Å)
      - `c`: float (Å)
    - `bulk_modulus_B0`: float (GPa)
    - `thermal_expansion_coefficient_300K`: float (K⁻¹)

Notes: All DFT calculations use the PBE functional. The thermal expansion coefficient is re-derived from the agent-provided mode Grüneisen parameters and lattice parameters within the verifier sandbox, ensuring that the mode table cannot be fabricated without running the actual phonon calculations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mode_gruneisen.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode_index",
          "frequency_cm1",
          "gamma",
          "degeneracy"
        ],
        "units": {
          "frequency_cm1": "cm⁻¹",
          "gamma": "dimensionless"
        }
      },
      "description": "Table of all zone-center optical phonon modes with frequencies, Grüneisen parameters, symmetry labels, and degeneracies. The checker verifies structural properties: correct number of modes (at least 30), presence of at least two negative gamma values, and physically plausible values."
    },
    {
      "file": "thermal_expansion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "relaxed_lattice_parameters",
          "bulk_modulus_B0",
          "thermal_expansion_coefficient_300K"
        ],
        "items": {
          "relaxed_lattice_parameters": {
            "a": "float (Å)",
            "c": "float (Å)"
          },
          "bulk_modulus_B0": "float (GPa)",
          "thermal_expansion_coefficient_300K": "float (K⁻¹)"
        }
      },
      "description": "Contains the relaxed lattice parameters, bulk modulus, and computed volumetric thermal expansion coefficient at 300 K. The checker recomputes the thermal expansion coefficient from the submitted mode_gruneisen.csv and compares the result to the hidden paper-reported value using a tolerance that absorbs toolchain differences."
    }
  ],
  "notes": "All DFT calculations use the PBE functional. The thermal expansion coefficient is re-derived from the agent-provided mode Grüneisen parameters and lattice parameters within the verifier sandbox, ensuring that the mode table cannot be fabricated without running the actual phonon calculations."
}
```

## How you are scored
A hidden verifier grades each artifact independently. For `mode_gruneisen.csv` it checks that the file contains the required number of optical modes, that the required columns are present, and that at least two modes have negative Grüneisen parameters. For `thermal_expansion.json` the verifier recomputes the thermal expansion coefficient at 300 K from your submitted mode Grüneisen parameters, relaxed lattice constants, and bulk modulus, then compares the result against an expected reference value using a tolerance that absorbs legitimate toolchain differences. Both artifacts contribute to the overall reward; reporting a number without running the DFT pipeline is not sufficient.
