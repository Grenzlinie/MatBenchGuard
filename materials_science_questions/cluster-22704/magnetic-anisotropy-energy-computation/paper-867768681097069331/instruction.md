# First-principles magnetocrystalline anisotropy energy of Fe2Ta and Fe2W

## Problem background
Permanent magnet materials with large magnetocrystalline anisotropy energy (MAE) and saturation magnetization are sought for energy applications. The hexagonal C14 Laves phase compounds Fe2Ta and Fe2W combine 3d and 5d elements, creating strong spin-orbit coupling that can yield uniaxial MAE. This reproduction targets the structural, magnetic, and anisotropy properties of these compounds from first-principles density functional theory (DFT).

## Approach
The approach uses spin-polarized DFT in the generalized gradient approximation. Starting from experimental crystal structures, scalar-relativistic calculations test ferromagnetic vs ferrimagnetic Fe spin alignment to determine the ground-state magnetic ordering. The lowest-energy configuration's lattice parameters (a, c) and internal coordinates (xFe2, z5d) are relaxed until forces converge. Using the relaxed geometry, spin-orbit coupling (SOC) is included to compute total energies with magnetization constrained along the [100] and [001] crystallographic directions. The magnetocrystalline anisotropy energy (MAE) is the energy difference E[100] − E[001] in meV per unit cell, converted to MJ/m³ using the unit cell volume from the relaxation step. The total spin magnetic moment per unit cell from the scalar-relativistic calculation is reported alongside the MAE.

## Reproduction target
Compute and output two data artifacts. First, for each compound a relaxed structure (relaxed_structures.json) containing optimized lattice parameters a and c (Å), internal coordinates xFe2 and z5d, unit cell volume (Å³), and total energy (Ry). Second, for each compound (mae_moments.json) the total spin magnetic moment per unit cell (μB), the MAE in meV per unit cell and in MJ/m³, and the easy magnetization axis ('c' if MAE > 0). Both artifacts must be produced in the exact JSON format specified in the output contract.

## Assets

- Quantum ESPRESSO (QE): https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials for Fe, Ta, W: https://www.materialscloud.org/discover/sssp/table/efficiency
- C14 Laves phase experimental crystal structures for Fe2Ta and Fe2W

## Workflow steps

### Step 1: Structural relaxation and magnetic ground state
- Role: scored
- Action: Perform scalar-relativistic spin-polarized DFT calculations for Fe2Ta and Fe2W in the C14 Laves phase using experimental lattice parameters as initial guesses. For each compound, test both ferromagnetic (parallel Fe spins) and ferrimagnetic (antiparallel Fe spins) alignments to identify the ground-state magnetic ordering. Relax the lattice parameters (a, c) and internal coordinates (xFe2, z5d) for the lower-energy magnetic configuration until forces converge. From the final relaxed structure, extract optimized lattice parameters, unit cell volume, and total energy, and write them to relaxed_structures.json. Also save the site-projected spin magnetic moments and total spin moment per unit cell to spin_moments.json (used in the next step).
- Output file: `/app/outputs/relaxed_structures.json`
- Format: json
- Contract: {"Fe2Ta": {"a_angstrom": float, "c_angstrom": float, "xFe2": float, "z5d": float, "volume_angstrom3": float, "total_energy_Ry": float}, "Fe2W": {"a_angstrom": float, "c_angstrom": float, "xFe2": float, "z5d": float, "volume_angstrom3": float, "total_energy_Ry": float}}
- Scoring: scored by hidden verifier

### Step 2: MAE calculation and final assembly
- Role: scored (load-bearing)
- Action: Using the relaxed structures and ground-state magnetic ordering from step 1, perform spin–orbit coupling (SOC) DFT calculations with the magnetization constrained along the crystallographic [100] and [001] directions. Compute the total energies E[100] and E[001]; calculate MAE = E[100] − E[001] in meV per unit cell, and convert to MJ/m³ using the unit cell volume from step 1. Read the total spin magnetic moment per unit cell from spin_moments.json and include it in the output. Identify the easy axis as 'c' if MAE > 0. Write the final results to mae_moments.json.
- Output file: `/app/outputs/mae_moments.json`
- Format: json
- Contract: {"Fe2Ta": {"total_spin_moment_muB_per_unit_cell": float, "mae_meV_per_unit_cell": float, "mae_MJ_per_m3": float, "easy_axis": "c"}, "Fe2W": {"total_spin_moment_muB_per_unit_cell": float, "mae_meV_per_unit_cell": float, "mae_MJ_per_m3": float, "easy_axis": "c"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_structures.json`
- `/app/outputs/mae_moments.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_structures.json
- path: `/app/outputs/relaxed_structures.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized lattice parameters, internal coordinates, unit cell volume, and total energy for Fe2Ta and Fe2W obtained from scalar-relativistic spin-polarized DFT relaxation.
- schema:
  - `type`: object
  - `required`:
    - `Fe2Ta`:
      - `a_angstrom`: number
      - `c_angstrom`: number
      - `xFe2`: number
      - `z5d`: number
      - `volume_angstrom3`: number
      - `total_energy_Ry`: number
    - `Fe2W`:
      - `a_angstrom`: number
      - `c_angstrom`: number
      - `xFe2`: number
      - `z5d`: number
      - `volume_angstrom3`: number
      - `total_energy_Ry`: number

### mae_moments.json
- path: `/app/outputs/mae_moments.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Magnetocrystalline anisotropy energy (meV/u.c. and MJ/m³), total spin magnetic moment per unit cell, and easy axis direction for Fe2Ta and Fe2W, computed with spin-orbit coupling.
- schema:
  - `type`: object
  - `required`:
    - `Fe2Ta`:
      - `total_spin_moment_muB_per_unit_cell`: number
      - `mae_meV_per_unit_cell`: number
      - `mae_MJ_per_m3`: number
      - `easy_axis`: c
    - `Fe2W`:
      - `total_spin_moment_muB_per_unit_cell`: number
      - `mae_meV_per_unit_cell`: number
      - `mae_MJ_per_m3`: number
      - `easy_axis`: c

Notes: The total spin moment in mae_moments.json should match the value in spin_moments.json. The easy axis string must be exactly 'c' (lower-case) for both compounds. Scoring uses a symmetric tolerance window around the paper-reported values; values must fall within the tolerance to earn credit. The alloy series Fe2Ta1-xWx and the ferro‑to‑ferrimagnetic transition composition are omitted because the VCA is an approximate method with known over‑estimation, the paper's primary quantitative claims are the end‑compound properties, and the alloy results are qualitative and heavily post‑processed, making a verifiable scored artifact impractical under the paper2arm reproducibility model.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_structures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Fe2Ta": {
            "a_angstrom": "number",
            "c_angstrom": "number",
            "xFe2": "number",
            "z5d": "number",
            "volume_angstrom3": "number",
            "total_energy_Ry": "number"
          },
          "Fe2W": {
            "a_angstrom": "number",
            "c_angstrom": "number",
            "xFe2": "number",
            "z5d": "number",
            "volume_angstrom3": "number",
            "total_energy_Ry": "number"
          }
        }
      },
      "description": "Optimized lattice parameters, internal coordinates, unit cell volume, and total energy for Fe2Ta and Fe2W obtained from scalar-relativistic spin-polarized DFT relaxation."
    },
    {
      "file": "mae_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Fe2Ta": {
            "total_spin_moment_muB_per_unit_cell": "number",
            "mae_meV_per_unit_cell": "number",
            "mae_MJ_per_m3": "number",
            "easy_axis": "c"
          },
          "Fe2W": {
            "total_spin_moment_muB_per_unit_cell": "number",
            "mae_meV_per_unit_cell": "number",
            "mae_MJ_per_m3": "number",
            "easy_axis": "c"
          }
        }
      },
      "description": "Magnetocrystalline anisotropy energy (meV/u.c. and MJ/m³), total spin magnetic moment per unit cell, and easy axis direction for Fe2Ta and Fe2W, computed with spin-orbit coupling."
    }
  ],
  "notes": "The total spin moment in mae_moments.json should match the value in spin_moments.json. The easy axis string must be exactly 'c' (lower-case) for both compounds. Scoring uses a symmetric tolerance window around the paper-reported values; values must fall within the tolerance to earn credit. The alloy series Fe2Ta1-xWx and the ferro‑to‑ferrimagnetic transition composition are omitted because the VCA is an approximate method with known over‑estimation, the paper's primary quantitative claims are the end‑compound properties, and the alloy results are qualitative and heavily post‑processed, making a verifiable scored artifact impractical under the paper2arm reproducibility model."
}
```

## How you are scored
A hidden verifier independently checks each output file. It compares your submitted values to reference values using appropriate tolerances and a threshold-or-better policy: if your result meets or exceeds the reference target, you earn full credit for that quantity; otherwise credit is assigned proportionally. The total reward is a weighted combination of the scores from all required quantities. Submitting the correct paper numbers is not sufficient; the verifier expects a consistent set of computed results from a genuine DFT workflow.
