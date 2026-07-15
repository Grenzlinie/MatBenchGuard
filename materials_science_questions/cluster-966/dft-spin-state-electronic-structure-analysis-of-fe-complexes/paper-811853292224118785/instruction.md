# DFT Conformational Energy Ordering of Bridled Chiroporphyrin Metal Complexes

## Problem background
Transition metal complexes of bridled chiroporphyrins (BCP8) can adopt different atropisomer conformations (αααα and αβαβ) depending on the central metal and its spin state. Understanding these conformational preferences is critical for designing molecular switches and nanotweezers. The cationic species FeCl(BCP8) (d5) and MnCl(BCP8) (d4) are axially ligated and can exist in high‑spin and, for Fe, low‑spin states. Density‑functional theory (DFT) calculations provide gas‑phase relative electronic energies of the αααα‑in, αααα‑out, and αβαβ conformers, revealing the interplay between d‑orbital occupancy, axial ligation, and strap constraints. The task is to determine the energetic ordering of these conformers.

## Approach
Perform spin‑polarized DFT geometry optimizations using the RPBE (revised Perdew–Burke–Ernzerhof) exchange‑correlation functional. Constrain the overall symmetry to C₂ to be consistent with the known molecular topology. Study all nine combinations: for [FeCl(BCP8)] the three conformers in both high‑spin (HS, sextet) and low‑spin (LS, doublet) states, and for [MnCl(BCP8)] the three conformers in the high‑spin (quintet) state only. After converging each structure, collect the final total electronic energy. For each complex and spin state, convert energies to cm⁻¹ and set the lowest energy (expected to be HS αααα‑in) as the zero reference. Report the resulting relative energies.

## Reproduction target
Produce a JSON file at /app/outputs/relative_energies.json containing the gas‑phase relative electronic energies (cm⁻¹) for all nine conformer/spin combinations. The file must be a JSON array of objects, each with the keys: complex (string, e.g. "FeCl(BCP8)"), conformer (one of "αααα‑in", "αααα‑out", "αβαβ"), spin ("HS" or "LS"), and relative_energy_cm‑1 (float). The high‑spin αααα‑in conformer shall serve as the energy reference and have a relative energy of 0.0 cm⁻¹.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de

## Workflow steps

### Step 1: Build initial geometries and input files
- Role: process
- Action: Construct Cartesian coordinates for the nine conformer/spin-state combinations of [FeCl(BCP8)] and [MnCl(BCP8)] listed in the paper (αααα‑in, αααα‑out, αβαβ; HS and LS for Fe, HS for Mn) using the known BCP8 molecular topology. Create ORCA input files with the RPBE functional, appropriate spin multiplicities, and C₂ symmetry constraint.
- Evidence: none

### Step 2: Perform DFT geometry optimizations
- Role: process
- Action: Run spin‑polarized DFT geometry optimizations with ORCA for all nine structures, using the RPBE functional and a suite of basis sets of triple‑ξ quality on metals and double‑ξ on other atoms (e.g., def2‑TZVP and def2‑SVP). Collect the final total electronic energy of each converged structure.
- Evidence: none

### Step 3: Compute relative electronic energies
- Role: scored (load-bearing)
- Action: For each complex and spin state, identify the lowest total energy conformer and set its energy to zero as the reference. Convert all total energies to cm⁻¹, compute the relative energy for every conformer, and write a JSON array of objects to /app/outputs/relative_energies.json.
- Output file: `/app/outputs/relative_energies.json`
- Format: json
- Contract: Array of objects, each containing: complex (string, e.g. "FeCl(BCP8)"), conformer (string, one of "αααα‑in", "αααα‑out", "αβαβ"), spin (string, "HS" or "LS"), relative_energy_cm‑1 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energies.json
- path: `/app/outputs/relative_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Gas‑phase relative electronic energies (cm⁻¹) for each BCP8 complex/conformer/spin combination, with the HS αααα‑in conformer serving as the zero reference. Compared against the paper‑reported values with a per‑entry tolerance window.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `complex`:
        - `type`: string
      - `conformer`:
        - `type`: string
      - `spin`:
        - `type`: string
      - `relative_energy_cm-1`:
        - `type`: number
    - `required`: `complex`, `conformer`, `spin`, `relative_energy_cm-1`

Notes: The hidden checker compares every entry’s relative_energy_cm‑1 to the corresponding paper‑reported value; tolerance absorbs expected differences from basis‑set/implementation changes (RPBE with Gaussian‑type orbitals vs original ADF Slater‑type basis).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "complex": {
              "type": "string"
            },
            "conformer": {
              "type": "string"
            },
            "spin": {
              "type": "string"
            },
            "relative_energy_cm-1": {
              "type": "number"
            }
          },
          "required": [
            "complex",
            "conformer",
            "spin",
            "relative_energy_cm-1"
          ]
        }
      },
      "description": "Gas‑phase relative electronic energies (cm⁻¹) for each BCP8 complex/conformer/spin combination, with the HS αααα‑in conformer serving as the zero reference. Compared against the paper‑reported values with a per‑entry tolerance window."
    }
  ],
  "notes": "The hidden checker compares every entry’s relative_energy_cm‑1 to the corresponding paper‑reported value; tolerance absorbs expected differences from basis‑set/implementation changes (RPBE with Gaussian‑type orbitals vs original ADF Slater‑type basis)."
}
```

## How you are scored
A hidden verifier will compare each entry in your relative_energies.json to a reference set of values obtained from the original study. For each entry, a normalized reward (0 to 1) is awarded based on how close your reported energy is to the reference, with generous tolerances that absorb differences arising from the use of open‑source quantum chemistry tools (ORCA with Gaussian basis sets) versus the original proprietary code (ADF with Slater‑type basis sets) while maintaining meaningful discrimination. The final reward is the average over all entries. Do not rely on fabricating numbers; only a genuine computational workflow will produce values that consistently fall within the tolerance windows.
