# DFT-based force-field parameter derivation for iron-sulfur clusters

## Problem background
Molecular mechanics simulations of hydrogenase enzymes require force-field parameters for the metalloclusters. This task addresses the absence of a complete, internally consistent set of parameters for the H-cluster and auxiliary iron-sulfur clusters by deriving them solely from quantum chemical calculations. You will compute bond, angle, dihedral, and improper torsion force constants, as well as atomic partial charges, using a density functional theory protocol at the BLYP/6-31+G* level and Natural Population Analysis.

## Approach
The derivation uses gas-phase DFT calculations on isolated cluster models capped with methylthiolate ligands. For each of the eight cluster/redox systems, you will perform geometry optimization and harmonic vibrational analysis to obtain the Hessian matrix in internal coordinates. Diagonal Hessian elements are converted to CHARMM force constants using a linear scaling factor and unit conversion factors. Partial charges are obtained from Natural Population Analysis of the converged wavefunction, and methylthiolate sulfur-capping hydrogen charges are redistributed to cysteine methylene hydrogens. The final parameter set is compiled into a CSV table.

## Reproduction target
Produce a single CSV file (`ff_parameters.csv`) containing the derived force constants and atomic charges for all eight cluster/redox states: oxidized and reduced [2Fe]H, [4Fe4S]Cys4, [4Fe4S]Cys3His, [2Fe2S]Cys4. Each row must specify the cluster identifier, coordinate type, atom labels, parameter type (bond force constant, angle force constant, dihedral amplitude, improper torsion constant, or charge), the numeric value, and its units. The CSV must follow the prescribed schema: columns `cluster`, `coordinate_type`, `atom1`, `atom2`, `atom3`, `atom4`, `parameter_type`, `value`, `units`.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de
- Multiwfn wavefunction analysis: http://sobereva.com/multiwfn/

## Workflow steps

### Step 1: Build initial molecular models of the metalloclusters
- Role: process
- Action: Construct initial Cartesian coordinate files for all eight cluster/redox systems (oxidized and reduced [2Fe]H, [4Fe4S]Cys4, [4Fe4S]Cys3His, [2Fe2S]Cys4) with methylthiolate capping groups replacing cysteinate, using the atom types, residue names, and connectivity from the original work.
- Evidence: `/app/outputs/models_summary.txt`

### Step 2: Run DFT geometry optimization, frequency, and charge calculations
- Role: process
- Action: For each cluster model, perform a gas-phase geometry optimization followed by an analytical frequency calculation using the BLYP functional and 6-31+G* basis set in ORCA. Use settings that output the Hessian in internal coordinates. Compute Natural Population Analysis (NPA) charges from the converged wavefunction using Multiwfn. Store the DFT output and wavefunction files.
- Evidence: `/app/outputs/dft_calculations.log`

### Step 3: Derive force-field parameters and compile CSV table
- Role: scored (load-bearing)
- Action: Extract the diagonal Hessian elements corresponding to the manually defined internal coordinates (bonds, angles, dihedrals, impropers). Apply the scaling factor (0.9945)^2 and convert to CHARMM units (multiply bond constants by 2242.3, angle/torsion constants by 627.49). Map harmonic torsional constants to CHARMM dihedral amplitudes. Redistribute methylthiolate hydrogen charges to cysteinate methylene hydrogens while preserving integer cluster charge. Compile all bond force constants, angle force constants, dihedral amplitudes, improper torsion constants, and NPA partial charges into a single CSV file with the prescribed schema for the eight cluster/redox systems.
- Output file: `/app/outputs/ff_parameters.csv`
- Format: csv
- Contract: CSV with columns: cluster (string), coordinate_type (string), atom1 (string), atom2 (string), atom3 (string), atom4 (string), parameter_type (string), value (float), units (string). One row per parameter. The value column holds the numeric parameter as computed by the agent.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ff_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ff_parameters.csv
- path: `/app/outputs/ff_parameters.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CSV containing all derived force constants and partial charges for the eight metallocluster models. Each row reports one parameter with its cluster label, coordinate type, atom labels, parameter type, numeric value, and units. The checker compares each value to the paper's reported gold within a tolerance that awards full credit if the deviation is below threshold and partial credit for larger deviations.
- schema:
  - `type`: table
  - `required_columns`: `cluster`, `coordinate_type`, `atom1`, `atom2`, `atom3`, `atom4`, `parameter_type`, `value`, `units`
  - `units`:
    - `value`: per row, as given in the units column (kcal/(mol·Å²), kcal/(mol·rad²), kcal/mol, or e)

Notes: The verification compares each parameter individually against the reference values using per-parameter tolerances. The final score is the fraction of parameters that meet the tolerance threshold, with monotonic partial credit for deviations up to twice the tolerance. This ensures that consistently accurate parameter sets score higher, while a lazy guess fails.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ff_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster",
          "coordinate_type",
          "atom1",
          "atom2",
          "atom3",
          "atom4",
          "parameter_type",
          "value",
          "units"
        ],
        "units": {
          "value": "per row, as given in the units column (kcal/(mol·Å²), kcal/(mol·rad²), kcal/mol, or e)"
        }
      },
      "description": "CSV containing all derived force constants and partial charges for the eight metallocluster models. Each row reports one parameter with its cluster label, coordinate type, atom labels, parameter type, numeric value, and units. The checker compares each value to the paper's reported gold within a tolerance that awards full credit if the deviation is below threshold and partial credit for larger deviations."
    }
  ],
  "notes": "The verification compares each parameter individually against the reference values using per-parameter tolerances. The final score is the fraction of parameters that meet the tolerance threshold, with monotonic partial credit for deviations up to twice the tolerance. This ensures that consistently accurate parameter sets score higher, while a lazy guess fails."
}
```

## How you are scored
A hidden verifier will independently score your `ff_parameters.csv`. For each parameter, the verifier compares your computed value to a reference value and awards full credit if the deviation is within a per-parameter tolerance band, with linear partial credit for larger deviations up to a cutoff. The final score is the fraction of parameters that pass. This rewards accurate reproduction of the DFT-based derivation pipeline. No credit is given for merely reporting numbers without running the required calculations.
