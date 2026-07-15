# Lattice Energy Calculation for Two Polymorphs Using Dreiding Force Field

## Problem background
Conformational polymorphism — the ability of a molecule to crystallize in more than one three‑dimensional arrangement — is important for understanding solid‑state properties. This task deals with two polymorphic forms, (I) and (II), of an organic compound with formula C13H10N2O. Both crystal structures belong to space group P21/c but differ in their asymmetric unit contents: polymorph (I) has one molecule per asymmetric unit (Z' = 1) while polymorph (II) has two (Z' = 2). The central question of the original study was which of the two forms is more stable, as measured by the total lattice energy, and how the energy difference can be attributed to intermolecular interactions, particularly hydrogen bonding.

## Approach
The stability ranking is investigated by force‑field calculations. Periodic unit cells are constructed from publicly available crystallographic data (CIF files) for both polymorphs. The Dreiding 2.21 force field is used to describe the intra‑ and intermolecular interactions, and partial atomic charges are determined by the charge equilibration (QEq) method. Total lattice energies (potential energy per unit cell) are computed for each polymorph in two ways: (1) directly from the experimental crystal structures without geometry changes, and (2) after performing a cell‑only optimisation that allows the lengths a, b, c and the monoclinic angle β to relax while keeping α = γ = 90° and treating entire molecules as rigid. Comparing the resulting energies reveals the relative thermodynamic stability and the magnitude of any shift caused by lattice relaxation.

## Reproduction target
Your goal is to compute the total lattice energies (in kcal/mol) of polymorphs (I) and (II) for both the crystallographic (as‑deposited) structures and the optimised structures. From these you will calculate two energy differences: δ_cryst = E(II) — E(I) for the crystallographic structures and δ_opt = E(II) — E(I) for the optimised structures. All values must be written to a JSON file, `/app/outputs/energies.json`, with exactly the following keys (all float, unit kcal/mol): `energy_I_cryst`, `energy_II_cryst`, `energy_I_opt`, `energy_II_opt`, `delta_cryst`, `delta_opt`. The sign and magnitude of the delta values indicate which polymorph is more stable; your task is to determine this through computation, not to match any pre‑supplied number.

## Assets

- CIF files for polymorphs (I) and (II) (IUCr electronic archive, reference BM1452): 10.1107/s010827010100909x
- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/

## Workflow steps

### Step 1: Crystal structure optimization
- Role: process
- Action: Build periodic unit cells from the CIF files of polymorphs (I) and (II). Assign Dreiding 2.21 force field atom types and charges using the charge equilibration (QEq) method. Perform cell-only minimization allowing the lattice parameters a, b, c, and beta to vary while constraining alpha=gamma=90 degrees and treating molecules as rigid. Record the optimized unit cell parameters for both polymorphs.
- Evidence: none

### Step 2: Calculate lattice energies and energy differences
- Role: scored (load-bearing)
- Action: For the original crystallographic structures (from CIF) and the optimized structures from the previous step, compute the total lattice energy (potential energy per unit cell) using the Dreiding 2.21 force field with QEq charges under periodic boundary conditions. Compute delta_cryst = E(II)_cryst - E(I)_cryst and delta_opt = E(II)_opt - E(I)_opt. Write all values to energies.json.
- Output file: `/app/outputs/energies.json`
- Format: json
- Contract: Keys: energy_I_cryst (float), energy_II_cryst (float), energy_I_opt (float), energy_II_opt (float), delta_cryst (float), delta_opt (float). All in kcal/mol.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.json
- path: `/app/outputs/energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: File containing the computed total lattice energies (kcal/mol) for the two polymorphs in both crystallographic and optimized structures, and the two energy differences. The values of delta_cryst and delta_opt will be compared to hidden reference values with a tolerance; their sign indicates relative stability without revealing the expected direction.
- schema:
  - `type`: object
  - `required`:
    - `energy_I_cryst`: number (float)
    - `energy_II_cryst`: number (float)
    - `energy_I_opt`: number (float)
    - `energy_II_opt`: number (float)
    - `delta_cryst`: number (float)
    - `delta_opt`: number (float)
  - `items`:
    - `energy_I_cryst`:
      - `type`: number
      - `unit`: kcal/mol
    - `energy_II_cryst`:
      - `type`: number
      - `unit`: kcal/mol
    - `energy_I_opt`:
      - `type`: number
      - `unit`: kcal/mol
    - `energy_II_opt`:
      - `type`: number
      - `unit`: kcal/mol
    - `delta_cryst`:
      - `type`: number
      - `unit`: kcal/mol
    - `delta_opt`:
      - `type`: number
      - `unit`: kcal/mol

Notes: The agent must use the Dreiding 2.21 force field with QEq charges. The CIF files should be obtained from the IUCr electronic archives. LAMMPS is the recommended tool. Only energies.json is scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "energy_I_cryst": "number (float)",
          "energy_II_cryst": "number (float)",
          "energy_I_opt": "number (float)",
          "energy_II_opt": "number (float)",
          "delta_cryst": "number (float)",
          "delta_opt": "number (float)"
        },
        "items": {
          "energy_I_cryst": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "energy_II_cryst": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "energy_I_opt": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "energy_II_opt": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "delta_cryst": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "delta_opt": {
            "type": "number",
            "unit": "kcal/mol"
          }
        }
      },
      "description": "File containing the computed total lattice energies (kcal/mol) for the two polymorphs in both crystallographic and optimized structures, and the two energy differences. The values of delta_cryst and delta_opt will be compared to hidden reference values with a tolerance; their sign indicates relative stability without revealing the expected direction."
    }
  ],
  "notes": "The agent must use the Dreiding 2.21 force field with QEq charges. The CIF files should be obtained from the IUCr electronic archives. LAMMPS is the recommended tool. Only energies.json is scored."
}
```

## How you are scored
A hidden verifier inspects your `/app/outputs/energies.json`. It performs the following checks: (i) the file exists and is valid JSON with all required keys; (ii) the verifier checks that the sign of each delta value matches the expected relative stability ordering (derived from the original published study) and that the magnitudes fall within an allowed tolerance that accounts for differences between simulation packages; (iii) internal consistency between the individual energies and the deltas is verified. The final reward is a weighted combination of these checks, with the comparison of the delta values carrying most of the weight. Simply writing reference numbers without performing the actual workflow will not pass all verification; your task is to faithfully reproduce the computational experiment.
