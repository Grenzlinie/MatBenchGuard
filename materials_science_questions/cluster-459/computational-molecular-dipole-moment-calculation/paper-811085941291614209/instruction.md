# Ab initio MP2/6-311G(3df,2p) calculation of formamide: optimized geometry, dipole moment, rotational constants and harmonic vibrational IR spectrum

## Problem background
Formamide is the smallest amide containing a peptide linkage, making it a fundamental model for understanding amide structures and their vibrational spectra. The planarity of the amino group and the position of the low-frequency NH2 torsional mode have been controversial; experimental and theoretical studies have reached differing conclusions. High-level ab initio calculations can resolve these questions by accurately predicting the equilibrium geometry, dipole moment, rotational constants, and infrared-active normal modes. This task reproduces such a computation at the MP2/6-311G(3df,2p) level to provide the optimized geometry, dipole moment, rotational constants, and harmonic vibrational spectrum of formamide.

## Approach
The approach uses second-order Møller-Plesset perturbation theory (MP2) with the triple-zeta 6-311G(3df,2p) basis set, which includes multiple polarization functions on all atoms. The geometry of formamide is optimized starting from a nonplanar initial guess, allowing the structure to naturally adopt its lowest-energy conformation. At the optimized geometry, the harmonic vibrational frequencies and absolute IR intensities are obtained by diagonalizing the mass-weighted Hessian; the dipole moment and rotational constants are computed from the same MP2 wavefunction. The resulting molecular parameters and vibrational data constitute a high-level theoretical reference for formamide.

## Reproduction target
Compute the optimized molecular geometry, dipole moment, rotational constants, and the complete set of unscaled harmonic vibrational wavenumbers and absolute IR intensities of formamide at the MP2/6-311G(3df,2p) level. The geometry must be evaluated for planarity via the relevant dihedral angles. All results must be written to three output files: an XYZ file with the Cartesian coordinates, a TSV file containing the dipole moment and the rotational constants A, B, C, and a TSV file listing the harmonic data (mode index, wavenumber, intensity) for all 12 normal modes.

## Assets

- Psi4 quantum chemistry package: https://psicode.org/

## Workflow steps

### Step 1: Geometry optimization and vibrational frequency calculation
- Role: process
- Action: Run MP2/6-311G(3df,2p) geometry optimization of formamide followed by a harmonic vibrational frequency and IR intensity calculation using an open-source quantum chemistry package (e.g., Psi4). Save the complete calculation output to a log file.
- Evidence: `/app/outputs/calculation.log`

### Step 2: Output optimized geometry
- Role: scored
- Action: Extract the final optimized Cartesian coordinates from the calculation output and write them to an XYZ file.
- Output file: `/app/outputs/optimal_geometry.xyz`
- Format: txt
- Contract: Standard XYZ: first line number of atoms (6), second line comment, subsequent lines each with element symbol and x, y, z coordinates in Angstroms.
- Scoring: scored by hidden verifier

### Step 3: Molecular parameters (dipole, rotational constants)
- Role: scored
- Action: Extract the dipole moment (in Debye) and the rotational constants A, B, C (in MHz) from the calculation output, and write them to a TSV file.
- Output file: `/app/outputs/molecular_parameters.tsv`
- Format: tsv
- Contract: TSV with header 'property	value'. Rows: dipole_moment_D, A_MHz, B_MHz, C_MHz. Values are floats.
- Scoring: scored by hidden verifier

### Step 4: Harmonic vibrational data (unscaled wavenumbers and intensities)
- Role: scored (load-bearing)
- Action: Extract the unscaled harmonic vibrational wavenumbers (cm⁻¹) and absolute IR intensities (km mol⁻¹) for all 12 normal modes from the calculation output, and write them to a TSV file.
- Output file: `/app/outputs/harmonic_vibrational_data.tsv`
- Format: tsv
- Contract: TSV with header 'mode_index	wavenumber_cm1	intensity_km_mol'. mode_index is an integer from 1 to 12; wavenumber_cm1 and intensity_km_mol are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimal_geometry.xyz`
- `/app/outputs/molecular_parameters.tsv`
- `/app/outputs/harmonic_vibrational_data.tsv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimal_geometry.xyz
- path: `/app/outputs/optimal_geometry.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: XYZ coordinates of the optimized formamide geometry.
- schema:
  - `type`: text
  - `description`: Standard XYZ file with 6 atoms, coordinates in Angstroms.

### molecular_parameters.tsv
- path: `/app/outputs/molecular_parameters.tsv`
- format: tsv
- purpose: scored
- target_policy: exact_match
- description: Dipole moment and rotational constants (A, B, C) computed from the MP2 wavefunction; compared to reference values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `property`, `value`
  - `items`:
    - `property`: string
    - `value`: float

### harmonic_vibrational_data.tsv
- path: `/app/outputs/harmonic_vibrational_data.tsv`
- format: tsv
- purpose: scored
- target_policy: exact_match
- description: Unscaled harmonic wavenumbers and absolute IR intensities for all 12 normal modes; compared to reference values with mode-dependent tolerances.
- schema:
  - `type`: table
  - `required_columns`: `mode_index`, `wavenumber_cm1`, `intensity_km_mol`
  - `items`:
    - `mode_index`: integer
    - `wavenumber_cm1`: float
    - `intensity_km_mol`: float

Notes: The geometry is evaluated silently; the other parameters are scored with tolerances hidden in the checker. All reference values are the paper's reported MP2/6-311G(3df,2p) results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimal_geometry.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Standard XYZ file with 6 atoms, coordinates in Angstroms."
      },
      "description": "XYZ coordinates of the optimized formamide geometry."
    },
    {
      "file": "molecular_parameters.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "value"
        ],
        "items": {
          "property": "string",
          "value": "float"
        }
      },
      "description": "Dipole moment and rotational constants (A, B, C) computed from the MP2 wavefunction; compared to reference values within tolerances."
    },
    {
      "file": "harmonic_vibrational_data.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode_index",
          "wavenumber_cm1",
          "intensity_km_mol"
        ],
        "items": {
          "mode_index": "integer",
          "wavenumber_cm1": "float",
          "intensity_km_mol": "float"
        }
      },
      "description": "Unscaled harmonic wavenumbers and absolute IR intensities for all 12 normal modes; compared to reference values with mode-dependent tolerances."
    }
  ],
  "notes": "The geometry is evaluated silently; the other parameters are scored with tolerances hidden in the checker. All reference values are the paper's reported MP2/6-311G(3df,2p) results."
}
```

## How you are scored
A hidden checker evaluates your output files independently. It compares the dipole moment and rotational constants to reference values with appropriate margins. The harmonic wavenumbers and intensities are compared mode-by-mode against expected results. The final score is a weighted combination of the three scored stages. The checker does not reward simply transcribing known numbers; it expects values that are fully consistent with a genuine MP2/6-311G(3df,2p) calculation.
