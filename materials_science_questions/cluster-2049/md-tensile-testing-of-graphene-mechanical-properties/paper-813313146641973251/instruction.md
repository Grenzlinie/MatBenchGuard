# Characterizing Effective Length in Double-Walled Carbon Nanotubes via Multiscale Simulation

## Problem background
Double-walled carbon nanotubes (DWCNTs) are explored as reinforcement in polymer nanocomposites. When the composite is loaded, stress transfers from the matrix to the CNT outer layer, but the inner layer contributes only if load can cross the interlayer interface. The interlayer adhesion may rely solely on van der Waals (vdW) forces or be enhanced by artificial covalent cross-links. The load transfer efficiency can be quantified by an effective length Leff — the length that carries an equivalent amount of saturated axial load. This task computes Leff for a set of DWCNT configurations (with and without covalent bonds) and compares them against a single-walled CNT baseline.

## Approach
The work follows a multiscale simulation strategy. First, molecular dynamics (MD) pull-out simulations are run on (3,3)/(8,8) DWCNTs of different lengths. The outer layer is incrementally extended while the inner layer is held at one end, producing extension versus reaction force curves. Two interlayer interaction scenarios are tested: pure vdW (Lennard‑Jones) and four artificial covalent cross‑links per tube. Second, the atomistic behaviour is mapped onto an equivalent continuum solid — a two‑layer hollow cylinder with radii converted from the carbon‑shell diameters. The interlayer adhesion is represented by axial spring elements whose stiffness (nonlinear for vdW, linear for covalent) is calibrated by matching the FEM pull‑out force‑extension curves to the MD curves. Third, the calibrated continuum solid is embedded in a cylindrical representative volume element (RVE) of a matrix (elastic modulus 3 GPa, CNT volume fraction 1 %). An axial load is applied to the matrix, and 3‑D finite element analysis yields the axial stress distributions in the outer and inner layers. From these stresses the effective length Leff is computed using the definition that equates the area under the stress profile to the saturated stress of a single‑wall CNT. The same RVE procedure is applied to an (8,8) SWCNT using its equivalent solid fibre.

## Reproduction target
Compute the effective length Leff for the following six configurations:
- DWCNT with vdW‑only interlayer interaction: lengths 160, 324, 590, 984 Å.
- DWCNT with four covalent cross‑links between layers: same four lengths.
- Single‑walled (8,8) CNT as a baseline.
The results must be saved in a CSV file at `/app/outputs/effective_lengths.csv` with columns `configuration`, `length_Angstrom`, and `effective_length_Angstrom`. The `configuration` column takes the value `DWCNT_vdW`, `DWCNT_covalent`, or `SWCNT`; `length_Angstrom` is the integer nanotube length; `effective_length_Angstrom` is a positive float.

## Assets

- MD simulation package (e.g., LAMMPS or OpenMM): https://lammps.sandia.gov
- FEM package (e.g., CalculiX or FEniCS): https://www.calculix.de
- AMBER force field parameters for sp2 carbon
- Lennard-Jones parameters (u=0.0556 kcal/mol, r0=3.40 Å)

## Workflow steps

### Step 1: MD pull-out simulation of DWCNTs
- Role: process
- Action: Run molecular dynamics simulations for (3,3)/(8,8) DWCNTs of lengths 160, 324, 590, 984 Å under two interlayer interaction conditions: van der Waals only and with four covalent cross-links. Use AMBER force field for intralayer bonded interactions and Lennard-Jones potential for non-bonded interactions. Pull outer layer incrementally (0.02 Å steps) in NVT ensemble and compute reaction force on inner layer fixed end. Produce extension versus reaction force curves for each configuration.
- Evidence: `/app/outputs/extension_reaction_curves.json`

### Step 2: Build equivalent continuum solid and calibrate spring constants
- Role: process
- Action: Construct a two-layer hollow cylindrical continuum solid with radii R1o=7.125 Å, R1i=3.735 Å, R2i=0.335 Å using material properties from the given table (E_outer=788.5 GPa, ν_outer=0.2732; E_inner=739.3 GPa, ν_inner=0.2822). Model interlayer interaction with axial spring elements and contact surfaces. Perform FEM pull-out matching the MD protocol to calibrate spring constants (nonlinear for vdW, linear for covalent) so that the continuum reaction force vs. extension curves match the MD curves.
- Evidence: `/app/outputs/calibrated_springs.json`

### Step 3: RVE FEM analysis and effective length calculation
- Role: scored (load-bearing)
- Action: Embed the calibrated continuum solid into a cylindrical representative volume element (RVE) of matrix material (elastic modulus 3 GPa, CNT volume fraction 1%, RVE matrix radius 71.25 Å). Apply axial loading of 100 MPa on the matrix. Perform 3-D finite element analysis to obtain axial stress distributions in outer and inner layers for each DWCNT case, and also for an (8,8) SWCNT (using an equivalent solid fiber with the same matrix). Compute effective length for each configuration using the definition of effective length as the length that carries an equivalent amount of saturated load. Output a CSV with effective lengths for all six configurations.
- Output file: `/app/outputs/effective_lengths.csv`
- Format: csv
- Contract: CSV with columns: configuration (string: 'DWCNT_vdW', 'DWCNT_covalent', 'SWCNT'), length_Angstrom (int), effective_length_Angstrom (float). Six rows total.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_lengths.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_lengths.csv
- path: `/app/outputs/effective_lengths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective lengths for DWCNTs (vdW and covalent) at four lengths and for a (8,8) SWCNT, quantifying load transfer efficiency.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `length_Angstrom`, `effective_length_Angstrom`
  - `units`:
    - `length_Angstrom`: Å
    - `effective_length_Angstrom`: Å

Notes: The effective lengths are compared against hidden reference values digitized from the paper with a tolerance of ±10%, and an additional structural ordering condition (monotonic increase with length, covalent > vdW) is enforced by the checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_lengths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "length_Angstrom",
          "effective_length_Angstrom"
        ],
        "units": {
          "length_Angstrom": "Å",
          "effective_length_Angstrom": "Å"
        }
      },
      "description": "Effective lengths for DWCNTs (vdW and covalent) at four lengths and for a (8,8) SWCNT, quantifying load transfer efficiency."
    }
  ],
  "notes": "The effective lengths are compared against hidden reference values digitized from the paper with a tolerance of ±10%, and an additional structural ordering condition (monotonic increase with length, covalent > vdW) is enforced by the checker."
}
```

## How you are scored
A hidden verifier will check your submitted `/app/outputs/effective_lengths.csv`. It compares each effective-length value against expected reference values derived from the original study, with tolerance for legitimate variations due to implementation differences. In addition, the verifier checks that the numbers satisfy required structural relationships (e.g., monotonic trends with tube length, relative ordering between van der Waals and covalent cases). The final reward is a weighted combination of these checks. Simply reporting the paper’s numbers without executing the multiscale pipeline will not satisfy the scoring criteria.
