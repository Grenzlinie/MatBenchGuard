# DFT Total Energy Comparison of Adamantane and Fluorite NiSi₂ Structures

## Problem background
NiSi2 can crystallize in two distinct structures: adamantane and fluorite. Understanding their relative stability is important for interpreting experimental observations of thick surface-stabilized films on Si(100). This task computes the relative stability of the two structures using first-principles density functional theory (DFT) total energy calculations. The result will be the difference in total energy per unit cell, which will indicate which structure is energetically favored.

## Approach
The relative stability is assessed by computing the total energy per unit cell for each structure in Rydbergs and then calculating the energy difference (adamantane − fluorite) in electronvolts. The unit cells are constructed from the reported lattice constants and atomic positions. DFT calculations are performed with an open-source plane-wave code (e.g., Quantum ESPRESSO) using standard pseudopotentials for Ni and Si. The total energies must be converged with respect to plane-wave cutoff energy and k-point sampling so that the energy difference is numerically reliable.

## Reproduction target
Compute the unit-cell total energy (in Ry) for both adamantane NiSi2 and fluorite NiSi2, then compute the energy difference (adamantane − fluorite) in eV. Report the results in a JSON file at `/app/outputs/step_01_energies.json` with the following structure: `{"adamantane_energy_Ry": <float>, "fluorite_energy_Ry": <float>, "energy_difference_eV": <float>}`.

## Assets

- NiSi2 adamantane and fluorite crystal structures
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials for Ni and Si: PSLibrary or SSSP

## Workflow steps

### Step 1: DFT total energy calculations for adamantane and fluorite NiSi2
- Role: scored (load-bearing)
- Action: Construct unit cells for adamantane NiSi2 (a=5.429 Å, Si at (0,0,0) and (1/4,1/4,1/4), Ni at (1/2,0,0)) and fluorite NiSi2 (a=5.395 Å, standard CaF2 positions). Using an open-source DFT code (e.g., Quantum ESPRESSO) with appropriate pseudopotentials, perform self-consistent total-energy calculations. Converge the total energies with respect to plane-wave cutoff and k-point sampling to a high precision. Compute the unit-cell total energy for each structure in Ry and the energy difference (adamantane − fluorite) in eV. Write the results to a JSON file.
- Output file: `/app/outputs/step_01_energies.json`
- Format: json
- Contract: {"adamantane_energy_Ry": <float>, "fluorite_energy_Ry": <float>, "energy_difference_eV": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energies.json
- path: `/app/outputs/step_01_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Unit-cell total energies for adamantane and fluorite NiSi2 in Rydbergs, and the energy difference in eV, used to assess the relative stability predicted by DFT.
- schema:
  - `type`: object
  - `required`:
    - `adamantane_energy_Ry`: number (Ry)
    - `fluorite_energy_Ry`: number (Ry)
    - `energy_difference_eV`: number (eV)

Notes: The checker compares the agent-computed energy_difference_eV to the paper's reported value within a tolerance, and also verifies that the difference is positive.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "adamantane_energy_Ry": "number (Ry)",
          "fluorite_energy_Ry": "number (Ry)",
          "energy_difference_eV": "number (eV)"
        }
      },
      "description": "Unit-cell total energies for adamantane and fluorite NiSi2 in Rydbergs, and the energy difference in eV, used to assess the relative stability predicted by DFT."
    }
  ],
  "notes": "The checker compares the agent-computed energy_difference_eV to the paper's reported value within a tolerance, and also verifies that the difference is positive."
}
```

## How you are scored
A hidden verifier reads your `step_01_energies.json` and compares the `energy_difference_eV` to a reference value. Full credit is awarded if the computed difference is within a tolerance that accounts for systematic differences between DFT implementations. The verifier also checks that the individual total energies are physically plausible. No partial credit is given for incomplete or incorrect data; the score is binary (1.0 if the result is within tolerance, 0.0 otherwise).
