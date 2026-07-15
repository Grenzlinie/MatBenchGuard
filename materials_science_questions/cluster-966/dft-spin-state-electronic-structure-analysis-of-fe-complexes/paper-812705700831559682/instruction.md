# DFT geometry optimization and electronic structure analysis of a high-coordinate Sn(II)-iodide cation with Fe(CO)4 caps

## Problem background
The compound [SnI8{Fe(CO)4}4]2+ contains an unprecedented eight-coordinate Sn(II) iodide unit in a doubly capped trigonal prismatic geometry, stabilized by Fe(CO)4 clamps. A key computational question is whether this geometry is a genuine energetic minimum compared with alternative SnI8 arrangements, and how the bonding situation leads to short I⋯I contacts. Density functional theory (DFT) calculations are employed to determine the relative stability of prismatic versus alternative isomers, to compute the HOMO–LUMO gap, and to extract optimized structural parameters that can be compared with the experimental crystal structure.

## Approach
Build initial atomic coordinates from the experimental crystallographic data of the [SnI8{Fe(CO)4}4]2+ cation. Construct an idealized square-antiprismatic (D4 symmetry) SnI8 core with the same Fe(CO)4 caps. Perform full geometry optimizations for both the capped prismatic isomer and the D4 antiprism isomer using a standard DFT functional and basis set (e.g., PBE0/def2-TZVP with effective core potentials for Sn and I). From the converged structures, compute the relative energy difference, the HOMO–LUMO gap of the lowest-energy structure, and selected interatomic distances and angles.

## Reproduction target
Perform DFT calculations on the [SnI8{Fe(CO)4}4]2+ cation to compute: (1) the energy difference (in kJ/mol) between the prismatic and the D4 antiprismatic isomers, (2) the HOMO–LUMO gap (in eV) of the lowest-energy isomer, (3) the Sn–I, Fe–I, two representative I⋯I distances (in pm), and the I–Fe–I angle (in degrees) from the optimized prismatic structure. Report all results in a single JSON file (`reproduced_results.json`) with the specified schema.

## Assets

- Crystallographic data (CIF) for [SnI8{Fe(CO)4}4][Al2Cl7]2
- DFT software package (e.g., ORCA, Gaussian, CP2K): https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Obtain initial geometry from CIF
- Role: process
- Action: Download the CIF file for the title compound from the CCDC (https://www.ccdc.cam.ac.uk/) using deposition number CCDC 1955936, extract the atomic coordinates of the [SnI8{Fe(CO)4}4]2+ cation, and prepare a Cartesian coordinate file (.xyz) suitable for DFT input.
- Evidence: `/app/outputs/initial_structure.xyz`

### Step 2: Build D4 antiprism isomer structure
- Role: process
- Action: Construct an idealized square-antiprismatic (D4 symmetry) SnI8 core geometry with the same Fe(CO)4 caps as the experimental structure, and generate a Cartesian coordinate file (.xyz) for this isomer.
- Evidence: `/app/outputs/d4_structure.xyz`

### Step 3: DFT geometry optimization and energy evaluation
- Role: process
- Action: Perform full geometry optimizations using a suitable DFT functional and basis set (e.g., PBE0/def2-TZVP with effective core potentials for Sn and I) for both the capped prismatic isomer (from step1) and the D4 antiprismatic isomer (from step2). After convergence, record the final total energies of both structures.
- Evidence: `/app/outputs/dft_energies.txt`

### Step 4: Extract and report key DFT results
- Role: scored
- Action: From the optimized structures: (a) compute the energy difference ΔE = E(prism) - E(D4) in kJ/mol; (b) from the optimized prismatic (S4 minimum) structure, compute the HOMO-LUMO gap in eV; (c) extract the Sn–I distance, Fe–I distance, two representative I⋯I distances (the shortest pair and one other), and the I–Fe–I angle (all distances in pm, angle in degrees). Write all quantities into a JSON file.
- Output file: `/app/outputs/reproduced_results.json`
- Format: json
- Contract: JSON object with keys: E_diff_kJ_per_mol (float), HOMO_LUMO_gap_eV (float), Sn_I_dist_pm (float), Fe_I_dist_pm (float), I_I_sep1_pm (float), I_I_sep2_pm (float), I_Fe_I_angle_deg (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_results.json
- path: `/app/outputs/reproduced_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed DFT energy difference, HOMO-LUMO gap, and selected geometric parameters for the [SnI8{Fe(CO)4}4]2+ cation.
- schema:
  - `type`: object
  - `required`: `E_diff_kJ_per_mol`, `HOMO_LUMO_gap_eV`, `Sn_I_dist_pm`, `Fe_I_dist_pm`, `I_I_sep1_pm`, `I_I_sep2_pm`, `I_Fe_I_angle_deg`
  - `units`:
    - `E_diff_kJ_per_mol`: kJ/mol
    - `HOMO_LUMO_gap_eV`: eV
    - `Sn_I_dist_pm`: pm
    - `Fe_I_dist_pm`: pm
    - `I_I_sep1_pm`: pm
    - `I_I_sep2_pm`: pm
    - `I_Fe_I_angle_deg`: deg

Notes: The hidden checker compares each numeric field to the paper's reported reference values with predefined tolerances. The agent must use a reasonable DFT setup; the tolerances accommodate expected method-dependent spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "E_diff_kJ_per_mol",
          "HOMO_LUMO_gap_eV",
          "Sn_I_dist_pm",
          "Fe_I_dist_pm",
          "I_I_sep1_pm",
          "I_I_sep2_pm",
          "I_Fe_I_angle_deg"
        ],
        "units": {
          "E_diff_kJ_per_mol": "kJ/mol",
          "HOMO_LUMO_gap_eV": "eV",
          "Sn_I_dist_pm": "pm",
          "Fe_I_dist_pm": "pm",
          "I_I_sep1_pm": "pm",
          "I_I_sep2_pm": "pm",
          "I_Fe_I_angle_deg": "deg"
        }
      },
      "description": "Computed DFT energy difference, HOMO-LUMO gap, and selected geometric parameters for the [SnI8{Fe(CO)4}4]2+ cation."
    }
  ],
  "notes": "The hidden checker compares each numeric field to the paper's reported reference values with predefined tolerances. The agent must use a reasonable DFT setup; the tolerances accommodate expected method-dependent spread."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s artifact and combines the scores by weight into a final reward between 0 and 1. For the scored artifact `reproduced_results.json`, the verifier reads the numeric fields and compares them to hidden reference values using tolerances; every field contributes to the score. You must produce a valid JSON file containing all required keys. Merely reporting any number is not sufficient – the values must be physically reasonable and derived from properly converged DFT calculations. The verifier also requires that you have produced the intermediate evidence files documented in the workflow steps.
