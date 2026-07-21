# GaN/AlGaN Nanowire Heterostructure Transition Energies

## Problem background
GaN nanodiscs (NDs) embedded in AlGaN nanowire heterostructures exhibit pronounced three-dimensional carrier confinement, with the photoluminescence emission energy strongly influenced by the aluminum concentration in the AlGaN barriers and by the presence of a lateral AlGaN shell that forms during growth. Determining the ground-state optical transition energies as a function of barrier composition is essential for understanding the interplay among strain, polarization, and carrier confinement in these nanostructures.

## Approach
The approach employs self-consistent three-dimensional Schrödinger-Poisson simulations of the nanowire heterostructure for several aluminum concentrations in the barriers, using a continuum effective-mass model. The geometry consists of a hexagonal GaN core, a stack of nine GaN nanodiscs separated by Al_xGa_{1-x}N barriers, and a laterally graded Al_xGa_{1-x}N shell whose thickness is parameterized based on the Al content. Two scenarios are compared for each Al concentration: one that includes the lateral shell and one that omits it (only the axial barriers). Material parameters for Al_xGa_{1-x}N are taken as linear or quadratic interpolations from publicly known endpoint values. For each structure, the strain distribution is first computed by minimizing the elastic energy with zero-stress boundary conditions at the nanowire surface; then the resulting band-edge profiles are calculated including spontaneous and piezoelectric polarization. The single-particle electron and hole ground-state energies are obtained for selected nanodiscs, and optical transition energies are derived with corrections for excitonic binding when the lateral electric field inside the ND is below a threshold for exciton ionization.

## Reproduction target
Compute the ground-state optical transition energies (in eV) for GaN nanodiscs embedded in GaN/Al_xGa_{1-x}N nanowire heterostructures with barrier aluminum concentrations x = 0.08, 0.11, 0.14, 0.20, 0.26, 0.34, 0.41, and 1.0. For each concentration, perform simulations with and without the lateral Al_xGa_{1-x}N shell, and extract the transition energies for nanodiscs 2, 5, 7, and 9 (include all NDs 2–9 for the AlN barrier case). Write the results to `/app/outputs/transition_energies.csv` following the specified output schema.

## Assets

- 3D Schrödinger-Poisson solver: https://www.nextnano.de/nextnanoplus/
- Material parameters of AlxGa1-xN
- Nanowire heterostructure geometry

## Workflow steps

### Step 1: Compute corrected ND transition energies
- Role: scored (load-bearing)
- Action: Construct the full 3D nanowire heterostructure geometry with and without a lateral AlGaN shell for each required Al barrier composition (x = 0.08, 0.11, 0.14, 0.20, 0.26, 0.34, 0.41, 1.0). Run self-consistent Schrödinger-Poisson simulations using the publicly known material parameters for AlxGa1-xN. Extract the one-particle ground-state energies for electrons and holes in nanodiscs 2, 5, 7, and 9 (for AlN barriers include all NDs 2–9). Apply excitonic corrections when the lateral electric field inside the ND is below 80 kV/cm; otherwise report the corrected transition energies. Write the resulting transition energies to transition_energies.csv.
- Output file: `/app/outputs/transition_energies.csv`
- Format: csv
- Contract: Columns: Al_concentration (float), shell_included_ND2 (float), shell_included_ND5 (float), shell_included_ND7 (float), shell_included_ND9 (float), no_shell_ND2 (float), no_shell_ND5 (float), no_shell_ND7 (float), no_shell_ND9 (float). All energies in eV. Row order arbitrary.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_energies.csv
- path: `/app/outputs/transition_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: The scored artifact that captures the reproduction target: the dependence of ND transition energies on barrier Al composition for both shell-included and no-shell models, enabling verification of the nonmonotonic trend with the lateral shell and the monotonic trend without it.
- schema:
  - `type`: table
  - `required_columns`: `Al_concentration`, `shell_included_ND2`, `shell_included_ND5`, `shell_included_ND7`, `shell_included_ND9`, `no_shell_ND2`, `no_shell_ND5`, `no_shell_ND7`, `no_shell_ND9`
  - `units`:
    - `Al_concentration`: dimensionless (mole fraction)
    - `shell_included_ND2`: eV
    - `shell_included_ND5`: eV
    - `shell_included_ND7`: eV
    - `shell_included_ND9`: eV
    - `no_shell_ND2`: eV
    - `no_shell_ND5`: eV
    - `no_shell_ND7`: eV
    - `no_shell_ND9`: eV
  - `description`: All energy columns are the ground-state optical transition energies of the specified nanodisc, corrected for excitonic effects when the lateral electric field in that ND is below 80 kV/cm (as described in the paper).

Notes: The checker will evaluate structural trends (nonmonotonic peak, monotonic decrease, shell vs no-shell ordering) rather than exact numerical agreement, due to expected solver-to-solver variability. No hidden tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Al_concentration",
          "shell_included_ND2",
          "shell_included_ND5",
          "shell_included_ND7",
          "shell_included_ND9",
          "no_shell_ND2",
          "no_shell_ND5",
          "no_shell_ND7",
          "no_shell_ND9"
        ],
        "units": {
          "Al_concentration": "dimensionless (mole fraction)",
          "shell_included_ND2": "eV",
          "shell_included_ND5": "eV",
          "shell_included_ND7": "eV",
          "shell_included_ND9": "eV",
          "no_shell_ND2": "eV",
          "no_shell_ND5": "eV",
          "no_shell_ND7": "eV",
          "no_shell_ND9": "eV"
        },
        "description": "All energy columns are the ground-state optical transition energies of the specified nanodisc, corrected for excitonic effects when the lateral electric field in that ND is below 80 kV/cm (as described in the paper)."
      },
      "description": "The scored artifact that captures the reproduction target: the dependence of ND transition energies on barrier Al composition for both shell-included and no-shell models, enabling verification of the nonmonotonic trend with the lateral shell and the monotonic trend without it."
    }
  ],
  "notes": "The checker will evaluate structural trends (nonmonotonic peak, monotonic decrease, shell vs no-shell ordering) rather than exact numerical agreement, due to expected solver-to-solver variability. No hidden tolerances are disclosed here."
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier. For each workflow stage, the verifier reads the corresponding output artifact and checks that it satisfies the required format and that the computed transition energies exhibit the physically expected dependence on aluminum concentration. No single gold value is disclosed; the verifier assesses whether your simulated energies are internally consistent and reproduce the systematic trends that follow from the underlying electrostatics and strain physics. The final reward is a weighted combination of the stage scores, with the scored artifact carrying the largest weight.
