# Atomistic simulation of dislocation-precipitate interactions in bcc Fe: CRSS for various precipitate morphologies

## Problem background
Precipitation hardening in α-iron (bcc Fe) greatly influences the mechanical properties of steels. When an edge dislocation in the Fe matrix encounters a coherent precipitate, the dislocation must overcome the obstacle, and the stress required for detachment—the critical resolved shear stress (CRSS)—quantifies the strengthening effect. The CRSS depends on the precipitate's size, shape, chemical composition, and ordering, but the interplay among these factors is not fully understood. Computing the CRSS for a range of precipitate morphologies via atomistic simulation provides insight into how chemical inhomogeneities and geometry alter the pinning behaviour, aiding alloy design.

## Approach
Classical molecular dynamics (MD) simulations will be performed using the embedded-atom method (EAM) to model interatomic interactions in the Fe–Cu–Ni system. An edge dislocation with Burgers vector a₀/2⟨111⟩ is introduced into a bcc Fe simulation cell containing a coherent precipitate on bcc lattice sites. Six precipitate morphologies are considered: spherical Cu, spherical Ni, ordered B2 CuNi, random Fe₂₅Cu₇₅, a Cu-core/Ni-shell particle, and an ellipsoidal Cu precipitate. For each configuration, quasi‑static loading at 300 K is applied: the shear stress is increased stepwise, with equilibration at each stress level until the dislocation detaches. The CRSS is recorded as the applied shear stress at detachment. The method follows established protocols for dislocation‑precipitate interaction and uses publicly available EAM potential files.

## Reproduction target
Produce the CRSS (in MPa) for each of the six specified precipitate conditions using the described MD workflow. The conditions are: (1) spherical Cu precipitate of radius 1.25 nm, (2) spherical Ni precipitate of radius 1.25 nm, (3) ordered B2 CuNi precipitate of radius 1.25 nm, (4) random Fe₂₅Cu₇₅ precipitate of radius 1.25 nm, (5) Cu-core/Ni-shell precipitate with core radius 0.6 nm and total radius 1.25 nm, and (6) ellipsoidal Cu precipitate with circular cross‑section radius 1.25 nm and perpendicular half‑axis 0.5 nm. Report all six CRSS values in a single CSV file with columns ‘condition’ and ‘crss_MPa’. The condition column must contain exactly one of the following identifier strings: 'Cu_spherical_1.25nm', 'Ni_spherical_1.25nm', 'CuNi_ordered_1.25nm', 'Fe25Cu75_spherical_1.25nm', 'CuNi_core_shell_core0.6nm', 'Cu_ellipsoidal_0.5nm_halfaxis'.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org
- EAM potential for Fe (Simonelli et al. 1993): https://www.ctcms.nist.gov/potentials/entry/1993--Simonelli-G-Pasianot-R-Savino-E-J--Fe/
- EAM potential for Cu (Voter 1993): https://www.ctcms.nist.gov/potentials/entry/1993--Voter-A-F--Cu/
- EAM potential for Ni (Voter 1993): https://www.ctcms.nist.gov/potentials/entry/1993--Voter-A-F--Ni/
- Cross-interaction EAM potentials for Fe-Cu, Fe-Ni, Cu-Ni

## Workflow steps

### Step 1: Generate initial atomic configurations for all precipitate conditions
- Role: process
- Action: Create LAMMPS-compatible initial atomic configurations for six precipitate conditions: spherical Cu (radius 1.25 nm), spherical Ni (1.25 nm), ordered B2 CuNi (1.25 nm), random Fe25Cu75 (1.25 nm), Cu-core/Ni-shell (core radius 0.6 nm), and an ellipsoidal Cu precipitate (circular cross-section radius 1.25 nm, perpendicular half-axis 0.5 nm). Each configuration consists of a bcc Fe block of 19.7×9.73×19.7 nm³ with periodic boundaries in x and z, fixed boundary layers in y, a coherent precipitate (atoms on bcc lattice sites), and an edge dislocation inserted by removing three (111) half-planes and closing the crystal.
- Evidence: `/app/outputs/configs_built.log`

### Step 2: Run quasi‑static MD and extract CRSS
- Role: scored (load-bearing)
- Action: For each configuration from the previous step, run LAMMPS with the assembled EAM alloy potential. Use a Nosé–Hoover thermostat at 300 K, timestep 0.5 fs. Apply a stepwise increasing shear stress: start at a low stress, equilibrate 20 ps at each level, and reduce increments as detachment is approached (final increment 8 MPa). Monitor the dislocation position and record the shear stress at the instant the dislocation detaches from the precipitate. Report the CRSS (in MPa) for all six conditions in the output CSV file.
- Output file: `/app/outputs/crss_results.csv`
- Format: csv
- Contract: Columns: condition (string), crss_MPa (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/crss_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### crss_results.csv
- path: `/app/outputs/crss_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Critical resolved shear stress (MPa) for each of the six precipitate conditions. The condition column identifies the precipitate type, and crss_MPa is the detachment stress.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `crss_MPa`
  - `columns`:
    - `name`: condition
    - `type`: string
    - `enum`: `Cu_spherical_1.25nm`, `Ni_spherical_1.25nm`, `CuNi_ordered_1.25nm`, `Fe25Cu75_spherical_1.25nm`, `CuNi_core_shell_core0.6nm`, `Cu_ellipsoidal_0.5nm_halfaxis`
    - `name`: crss_MPa
    - `type`: number
    - `units`: MPa

Notes: The CSV must include exactly one row per condition with the correct condition identifier and the computed CRSS. The hidden checker will compare crss_MPa values against paper-derived gold using a generous tolerance window; a value equal to or better than the threshold (within tolerance) earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "crss_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "crss_MPa"
        ],
        "columns": [
          {
            "name": "condition",
            "type": "string",
            "enum": [
              "Cu_spherical_1.25nm",
              "Ni_spherical_1.25nm",
              "CuNi_ordered_1.25nm",
              "Fe25Cu75_spherical_1.25nm",
              "CuNi_core_shell_core0.6nm",
              "Cu_ellipsoidal_0.5nm_halfaxis"
            ]
          },
          {
            "name": "crss_MPa",
            "type": "number",
            "units": "MPa"
          }
        ]
      },
      "description": "Critical resolved shear stress (MPa) for each of the six precipitate conditions. The condition column identifies the precipitate type, and crss_MPa is the detachment stress."
    }
  ],
  "notes": "The CSV must include exactly one row per condition with the correct condition identifier and the computed CRSS. The hidden checker will compare crss_MPa values against paper-derived gold using a generous tolerance window; a value equal to or better than the threshold (within tolerance) earns full credit."
}
```

## How you are scored
A hidden verifier independently evaluates your submitted artifacts for each workflow stage. The verifier checks the shape and content of the output files, compares your computed CRSS values against reference data using a predefined tolerance, and assigns a weighted partial reward per stage. The final score is a weighted combination of stage rewards. Simply reporting numbers is not enough; your submitted files must satisfy the output contract and demonstrate that the required simulations were carried out. The exact tolerances and reference values are not disclosed.
