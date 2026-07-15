# Magnetic Anisotropy Energy Computation for TM-doped Hexagonal Boron Nitride Monolayers

## Problem background
Magnetic anisotropy energy (MAE) is a critical property for spintronic devices because it determines the preferred orientation of magnetization and its thermal stability. Two-dimensional materials can exhibit large magnetic anisotropy due to reduced symmetry and dimensionality. Hexagonal boron nitride (h‑BN) is a wide‑band‑gap semiconductor isostructural to graphene, and substituting boron atoms with magnetic 3d transition metal atoms may induce magnetism and appreciable MAE. This task computationally investigates the magnetic moment, MAE, and easy‑axis direction of h‑BN monolayers where a single boron site is replaced by Fe, Mn, Sc, or Co, using density functional theory with spin–orbit coupling.

## Approach
The computational approach is based on plane‑wave density functional theory (DFT) within the generalized gradient approximation (GGA‑PBE). A 7×7×1 supercell of h‑BN (with vacuum) is constructed, and one boron atom is replaced by each transition metal (Fe, Mn, Sc, Co). Atomic positions are relaxed until forces are small. A self‑consistent field calculation then provides the charge density, wavefunctions, and total magnetic moment.  To extract the magnetic anisotropy, two non‑self‑consistent total‑energy calculations are performed with spin–orbit coupling included, with the magnetization aligned along the out‑of‑plane (z) and an in‑plane (x) direction. The magnetic anisotropy energy is defined as MAE = E_z − E_x, where a positive MAE indicates an in‑plane easy axis, a negative MAE an out‑of‑plane easy axis, and a zero magnetic moment renders the system nonmagnetic (easy axis ‘none’). The workflow is implemented with an open‑source DFT code (e.g., Quantum ESPRESSO) and suitable projector‑augmented‑wave pseudopotentials, reproducing the computational protocol originally reported in the literature.

## Reproduction target
Produce a JSON file, `mae_results.json`, containing the consolidated results for the four transition‑metal‑substituted systems Fe@B, Mn@B, Sc@B, and Co@B. For each system, report the computed total magnetic moment (in μ_B, or null if nonmagnetic), the MAE in meV (null if nonmagnetic), and the easy axis derived from the MAE sign: ‘in‑plane’ for MAE > 0, ‘out‑of‑plane’ for MAE < 0, ‘none’ if the magnetic moment is zero. The file must be an array of exactly four objects with keys `system`, `magnetic_moment_muB`, `MAE_meV`, and `easy_axis` as detailed in the output contract.

## Assets

- Quantum ESPRESSO (open-source plane-wave DFT code): https://www.quantum-espresso.org/
- SSSP Efficiency pseudopotentials (or GBRV) for Fe, Mn, Sc, Co, B, N: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Build supercell structures for TM@B
- Role: process
- Action: Construct 7×7×1 supercells of h-BN (lattice constant 2.504 Å, vacuum 15 Å) and substitute one B atom with each of Fe, Mn, Sc, Co. Save input coordinates for DFT.
- Evidence: `/app/outputs/initial_structures.txt`

### Step 2: Geometry relaxation
- Role: process
- Action: For each TM@B system, relax atomic positions using DFT with GGA-PBE functional, plane-wave cutoff 400 eV, k-mesh 3×3×1, force convergence 0.01 eV/Å. Save optimized coordinates and final total energy.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: Self-consistent electronic structure calculation
- Role: process
- Action: Perform a self-consistent DFT calculation on the relaxed structures using a 5×5×1 k-mesh and energy convergence 1×10⁻⁶ eV. Obtain the charge density, total magnetic moment, and wavefunctions.
- Evidence: `/app/outputs/scf.log`

### Step 4: MAE calculation and result compilation
- Role: scored (load-bearing)
- Action: For each system, run non-self-consistent SOC calculations with magnetization along z and x directions (5×5×1 k-mesh, energy convergence 1×10⁻⁷ eV). Compute MAE = E_z − E_x and determine easy axis (in-plane for MAE>0, out-of-plane for MAE<0, none if nonmagnetic). Compile the total magnetic moment from s03 and the computed MAE+axis into a JSON array. Write result to mae_results.json.
- Output file: `/app/outputs/mae_results.json`
- Format: json
- Contract: JSON array of exactly 4 objects, each with keys: 'system' (string: one of 'Fe@B','Mn@B','Sc@B','Co@B'), 'magnetic_moment_muB' (number or null if nonmagnetic), 'MAE_meV' (number or null if nonmagnetic/zero), 'easy_axis' (string: 'in-plane','out-of-plane','none').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mae_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mae_results.json
- path: `/app/outputs/mae_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Consolidated results of magnetic moment, MAE, and easy axis for Fe@B, Mn@B, Sc@B, Co@B.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `magnetic_moment_muB`, `MAE_meV`, `easy_axis`
    - `properties`:
      - `system`:
        - `type`: string
      - `magnetic_moment_muB`:
        - `type`: `number`, `null`
      - `MAE_meV`:
        - `type`: `number`, `null`
      - `easy_axis`:
        - `type`: string

Notes: The hidden checker compares the reported values against paper-reported references with appropriate tolerances. For nonmagnetic systems (Sc@B, Co@B) the expectation is magnetic_moment_muB=0, MAE_meV=null, easy_axis='none'.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mae_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system",
            "magnetic_moment_muB",
            "MAE_meV",
            "easy_axis"
          ],
          "properties": {
            "system": {
              "type": "string"
            },
            "magnetic_moment_muB": {
              "type": [
                "number",
                "null"
              ]
            },
            "MAE_meV": {
              "type": [
                "number",
                "null"
              ]
            },
            "easy_axis": {
              "type": "string"
            }
          }
        }
      },
      "description": "Consolidated results of magnetic moment, MAE, and easy axis for Fe@B, Mn@B, Sc@B, Co@B."
    }
  ],
  "notes": "The hidden checker compares the reported values against paper-reported references with appropriate tolerances. For nonmagnetic systems (Sc@B, Co@B) the expectation is magnetic_moment_muB=0, MAE_meV=null, easy_axis='none'."
}
```

## How you are scored
A hidden verifier will compare your `mae_results.json` against a reference derived from the original computational study. The magnetic moment is checked for exact integer agreement; the MAE is compared within a tolerance that accounts for differences between DFT implementations (different codes, pseudopotentials, or numerical details); and the easy axis must be consistent with the sign of the MAE according to the convention used. Each correctly reported system contributes to the final score, which is proportional to the number of systems out of four that match the reference within tolerance. Intermediate log files are not directly scored but their presence documents the workflow execution.
