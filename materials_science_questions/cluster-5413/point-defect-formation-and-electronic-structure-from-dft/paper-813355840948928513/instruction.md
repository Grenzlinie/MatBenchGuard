# Band gap calculations for hydrous forsterite with free-proton defect using DFT

## Problem background
Hydrous forsterite (Mg2SiO4 with water incorporated as hydrogen point defects) is studied to understand how hydrogen affects electrical conductivity in olivine, the most abundant mineral in the upper mantle. A proposed mechanism is that when one hydrogen occupies an Mg vacancy and a second hydrogen is placed as a free proton along certain crystallographic directions, new electronic states appear that could narrow the band gap, potentially transforming forsterite from an insulator into a semiconductor. This work aims to compute the electronic band gaps of the free-proton defect model to determine whether such a transition occurs.

## Approach
The approach uses first-principles density functional theory (DFT) with the generalized gradient approximation (GGA) PBE exchange-correlation functional and a plane-wave basis set, as implemented in an open-source plane-wave DFT code. The primitive cell of anhydrous forsterite is obtained from a public crystal structure database. For the hydrous defect configurations: a magnesium atom at the M1 site is removed to create a vacancy; one hydrogen atom is placed at the vacancy center; and a second hydrogen (the free proton) is placed at one of three fractional-coordinate positions corresponding to the [100], [010], and [001] orientations. Structure relaxations are performed for each configuration, followed by an electronic structure calculation to obtain the Kohn-Sham eigenvalues. The band gap is extracted as the energy difference between the highest occupied and lowest unoccupied states. The anhydrous primitive cell is also calculated to provide a reference baseline.

## Reproduction target
Compute and report the electronic band gaps (in eV) for the anhydrous forsterite primitive cell and for the three free-proton hydrous configurations with orientations [100], [010], and [001], all at 0 GPa. The results must be written to the file `/app/outputs/band_gaps.json` with the following structure: an object containing `anhydrous_band_gap` (a number) and `free_proton_band_gaps` (an object with keys `"[100]"`, `"[010]"`, `"[001]"` each mapping to a number).

## Assets

- Forsterite (Mg2SiO4) crystal structure: COD 1011195
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials for Mg, Si, O, H (GGA-PBE norm-conserving): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Build initial atomic models
- Role: process
- Action: Construct the primitive cell of anhydrous Mg2SiO4 from the public crystal structure. For the hydrous defect configurations: (1) remove one Mg atom at the M1 site to create a vacancy; (2) place one hydrogen atom at the vacancy (fractional coordinate (0.5,0.5,0.5)); (3) add a second hydrogen (free proton) at one of three positions: (0.75,0.5,0.5) for [100] orientation, (0.5,0.63,0.5) for [010], and (0.5,0.5,0.68) for [001]. Save the initial structures as Quantum ESPRESSO input files.
- Evidence: none

### Step 2: DFT band gap calculation
- Role: scored (load-bearing)
- Action: Perform structure relaxation and electronic structure calculation at 0 GPa for (a) the anhydrous forsterite primitive cell and (b) the three hydrous free-proton configurations. Use a plane-wave DFT code with GGA-PBE exchange-correlation. Extract the Kohn-Sham band gap (difference between the highest occupied and lowest unoccupied eigenvalues) for each system. Write all results to band_gaps.json.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"anhydrous_band_gap": number (eV), "free_proton_band_gaps": {"[100]": number (eV), "[010]": number (eV), "[001]": number (eV)}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Band gaps of anhydrous forsterite and the free-proton hydrous configurations along three crystallographic orientations, all computed at 0 GPa with GGA-PBE.
- schema:
  - `type`: object
  - `required`:
    - `anhydrous_band_gap`: number (eV)
    - `free_proton_band_gaps`: object
  - `items`:
    - `[100]`: number (eV)
    - `[010]`: number (eV)
    - `[001]`: number (eV)

Notes: Only the band gaps are scored; density-of-states data for the [010] orientation is an optional supporting output not required by this contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "anhydrous_band_gap": "number (eV)",
          "free_proton_band_gaps": "object"
        },
        "items": {
          "[100]": "number (eV)",
          "[010]": "number (eV)",
          "[001]": "number (eV)"
        }
      },
      "description": "Band gaps of anhydrous forsterite and the free-proton hydrous configurations along three crystallographic orientations, all computed at 0 GPa with GGA-PBE."
    }
  ],
  "notes": "Only the band gaps are scored; density-of-states data for the [010] orientation is an optional supporting output not required by this contract."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact. For `band_gaps.json`, the verifier compares your computed band gap values against predetermined reference values with an allowed tolerance that absorbs legitimate toolchain differences (different DFT code, pseudopotentials, convergence settings). The verifier also checks that the relative magnitudes among the three free-proton orientations are physically consistent. Reward is assigned based on the accuracy and internal consistency of your results, with the band gap data carrying the primary weight.
