# Zero-field Splitting Analysis of Fe(II) S4 Complexes

## Problem background
Four-coordinate {FeIIS4} complexes are promising candidates for spin-based qubits and qudits because their zero-field splitting (ZFS) parameters, the axial D and the rhombicity E/D, determine the energy separation between the ground-state spin sublevels that serve as quantum bits. A remarkable experimental observation is that in a series of [Fe(C3S5)2]2– complexes with different counterions, the D parameter remains nearly constant despite the interligand dihedral angle (θd) varying from about 72° to 90°, while E/D is reported to change little. This invariance to structural distortions is highly desirable for surface-adsorbed qubits, yet the electronic origin of this behaviour is not fully understood. The present task uses multi-reference ab initio electronic structure calculations to compute D and E/D for the three experimentally characterised complexes and for a set of model structures in which θd is systematically varied, with the aim of uncovering the factors that govern the stability of D and the variation of E/D.

## Approach
The zero-field splitting parameters are computed using the effective Hamiltonian approach applied to state-averaged complete-active-space self-consistent field (SA-CASSCF) wave functions, followed by N-electron valence second-order perturbation theory (NEVPT2) to recover dynamic correlation. An active space of six electrons in five d-based orbitals (CASSCF(6,5)) is employed, and the calculation is performed on the bare [Fe(C3S5)2]2– anion because the counterions do not influence the ZFS. The axial splitting D and rhombicity E/D are extracted, together with optional quantities such as the g-tensor, the dominant spin-flip contribution to D, and the d_xz–d_yz orbital energy splitting that drives the rhombicity.

Two sets of structures are studied. First, the publicly available X‑ray crystal structures of complexes 1–3 are used directly. Second, starting from the experimentally determined geometry of complex 1, a series of models is generated in which the dihedral angle θd between the two C3S5 ligand planes is varied from approximately 30° to 90° in steps of 10° (and at approximately 64.7° if possible), while all other bond lengths and angles are kept fixed to the values in complex 1. The same CASSCF/NEVPT2 protocol is then applied to every model, yielding D and E/D as a function of θd. The resulting data will allow identification of the dihedral‑angle windows where D stays constant, where it reverses sign, and how E/D evolves.

## Reproduction target
Produce two CSV files under /app/outputs:

1. `d_values_complexes.csv` — the axial zero-field splitting D (cm⁻¹) and rhombicity E/D (dimensionless) for the three experimental complexes 1–3. Optionally, include the g-tensor components, the spin-flip contribution to D, and the d_xz–d_yz orbital energy splitting.

2. `dihedral_scan.csv` — D (cm⁻¹) and E/D (dimensionless) for each dihedral-angle model, identified by the dihedral angle θd (degrees). Optionally, include the spin-flip contribution to D.

The target is to produce these tables through the computational workflow described in the steps below; no external datasets beyond the crystal structures are required.

## Assets

- ORCA quantum chemistry package (version supporting SA-CASSCF/NEVPT2 and effective Hamiltonian ZFS): https://orcaforum.kofo.mpg.de/
- X-ray crystal structures of complexes 1–3: 10.1039/C8DT02145G
- Computational resources (CPU cluster or cloud instance)

## Workflow steps

### Step 1: Retrieve and prepare molecular structures from X-ray data
- Role: process
- Action: Retrieve the CIF files of complexes 1–3 from the CSD or the paper's ESI. Extract the atomic coordinates of the [Fe(C3S5)2]2– anion. Verify the dihedral angle between the two ligand planes for each complex. Store the geometry for complex 1 for later model generation.
- Evidence: none

### Step 2: Compute zero-field splitting parameters for complexes 1–3
- Role: scored
- Action: Perform SA-CASSCF(6,5)/NEVPT2 calculations on each complex (anion without counterion, as counterions do not affect D). Use the effective Hamiltonian approach to extract the axial zero-field splitting D, rhombicity E/D, and (optionally) g-tensor components, the dominant spin-flip contribution to D, and the d_xz–d_yz orbital energy splitting ΔE. Write the results to d_values_complexes.csv.
- Output file: `/app/outputs/d_values_complexes.csv`
- Format: csv
- Contract: CSV with columns: Complex, D_cm⁻¹, E_over_D, and optionally g_x, g_y, g_z, spin_flip_contribution_D_cm⁻¹, Delta_E_dxz_dyz_cm⁻¹.
- Scoring: scored by hidden verifier

### Step 3: Generate model geometries with varied dihedral angle
- Role: process
- Action: Starting from the geometry of complex 1, systematically vary the interligand dihedral angle θd from 30° to 90° in steps of 10°. Also include a model at θd ≈ 64.7° if possible. Keep all bond lengths and angles (other than the dihedral) fixed to the values in complex 1. Produce coordinate files for each dihedral model.
- Evidence: `/app/outputs/model_geometries_list.csv`

### Step 4: Compute zero-field splitting parameters for the dihedral angle scan
- Role: scored (load-bearing)
- Action: For each dihedral model constructed in step 3, perform the same SA-CASSCF(6,5)/NEVPT2 protocol and effective Hamiltonian analysis as used for the experimental complexes. Extract the axial zero-field splitting D and rhombicity E/D, and (optionally) the spin-flip contribution to D. Write the results to dihedral_scan.csv.
- Output file: `/app/outputs/dihedral_scan.csv`
- Format: csv
- Contract: CSV with columns: theta_d_deg, D_cm⁻¹, E_over_D, and optionally spin_flip_contribution_D_cm⁻¹.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/d_values_complexes.csv`
- `/app/outputs/dihedral_scan.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### d_values_complexes.csv
- path: `/app/outputs/d_values_complexes.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Zero-field splitting D and rhombicity E/D for complexes 1-3. The checker compares reported D and E/D to hidden reference values from the paper.
- schema:
  - `type`: table
  - `required_columns`: `Complex`, `D_cm⁻¹`, `E_over_D`
  - `optional_columns`: `g_x`, `g_y`, `g_z`, `spin_flip_contribution_D_cm⁻¹`, `Delta_E_dxz_dyz_cm⁻¹`
  - `units`:
    - `Complex`: integer (1,2,3)
    - `D_cm⁻¹`: cm^-1
    - `E_over_D`: dimensionless
    - `g_x`: dimensionless
    - `g_y`: dimensionless
    - `g_z`: dimensionless
    - `spin_flip_contribution_D_cm⁻¹`: cm^-1
    - `Delta_E_dxz_dyz_cm⁻¹`: cm^-1

### dihedral_scan.csv
- path: `/app/outputs/dihedral_scan.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: ZFS parameters for the dihedral angle scan (θd from ~30° to 90°). The checker verifies D values within a hidden window for the experimental range, detects D sign change, and checks E/D behavior.
- schema:
  - `type`: table
  - `required_columns`: `theta_d_deg`, `D_cm⁻¹`, `E_over_D`
  - `optional_columns`: `spin_flip_contribution_D_cm⁻¹`
  - `units`:
    - `theta_d_deg`: degrees
    - `D_cm⁻¹`: cm^-1
    - `E_over_D`: dimensionless
    - `spin_flip_contribution_D_cm⁻¹`: cm^-1

Notes: The primary scored quantities are D and E/D. The optional columns provide supporting evidence but do not affect scoring. Tolerances are set to absorb legitimate method/implementation spread while requiring a genuine CASSCF/NEVPT2 run.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "d_values_complexes.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Complex",
          "D_cm⁻¹",
          "E_over_D"
        ],
        "optional_columns": [
          "g_x",
          "g_y",
          "g_z",
          "spin_flip_contribution_D_cm⁻¹",
          "Delta_E_dxz_dyz_cm⁻¹"
        ],
        "units": {
          "Complex": "integer (1,2,3)",
          "D_cm⁻¹": "cm^-1",
          "E_over_D": "dimensionless",
          "g_x": "dimensionless",
          "g_y": "dimensionless",
          "g_z": "dimensionless",
          "spin_flip_contribution_D_cm⁻¹": "cm^-1",
          "Delta_E_dxz_dyz_cm⁻¹": "cm^-1"
        }
      },
      "description": "Zero-field splitting D and rhombicity E/D for complexes 1-3. The checker compares reported D and E/D to hidden reference values from the paper."
    },
    {
      "file": "dihedral_scan.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta_d_deg",
          "D_cm⁻¹",
          "E_over_D"
        ],
        "optional_columns": [
          "spin_flip_contribution_D_cm⁻¹"
        ],
        "units": {
          "theta_d_deg": "degrees",
          "D_cm⁻¹": "cm^-1",
          "E_over_D": "dimensionless",
          "spin_flip_contribution_D_cm⁻¹": "cm^-1"
        }
      },
      "description": "ZFS parameters for the dihedral angle scan (θd from ~30° to 90°). The checker verifies D values within a hidden window for the experimental range, detects D sign change, and checks E/D behavior."
    }
  ],
  "notes": "The primary scored quantities are D and E/D. The optional columns provide supporting evidence but do not affect scoring. Tolerances are set to absorb legitimate method/implementation spread while requiring a genuine CASSCF/NEVPT2 run."
}
```

## How you are scored
A hidden verifier independently evaluates each scored output file and combines the scores into a final reward between 0 and 1. The verifier compares your reported D and E/D values (and, if provided, supporting quantities) against hidden reference targets extracted from the published computational work. For the complex series, the scoring checks quantitative agreement within a tolerance; for the dihedral scan, it also verifies correct qualitative trends—specifically, that D remains nearly constant over the experimental dihedral range, that E/D increases as θd decreases from 90° to 72°, and that D changes sign at lower dihedral angles. Simply reporting numbers (including the paper's published values) without performing the required CASSCF/NEVPT2 calculations will not yield a high reward; the verifier expects values that can only result from genuinely executing the workflow.
