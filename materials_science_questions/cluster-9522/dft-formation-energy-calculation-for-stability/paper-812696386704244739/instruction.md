# DFT Cohesive Energy and Formation Enthalpy of Ti-Substituted NiAl

## Problem background
NiAl intermetallic compounds are attractive as matrix materials for high-temperature composites due to their high melting point, low density, and good oxidation resistance. During fabrication of NiAl-based composites containing BaO and TiO₂, Ti can dissolve into the NiAl matrix, leading to lattice distortion. Understanding the effect of Ti dissolution on the stability of the NiAl phase is important. Density functional theory (DFT) can be used to quantify the stability by calculating the cohesive energy and formation enthalpy of NiAl with varying Ti solution content.

## Approach
In this task, we use plane-wave DFT (as implemented in Quantum ESPRESSO) to compute total energies for the B2-structured NiAl phase and three Ti-substituted derivatives, NiAlTi₁, NiAlTi₂, and NiAlTi₃, obtained by substituting Al atoms with Ti in a supercell. Additionally, we compute total energies for isolated Ni, Al, and Ti atoms. From these total energies, we derive the cohesive energy (the energy gained by forming the bulk phase from the isolated atoms) and the formation enthalpy (the difference between the cohesive energy of the compound and the cohesive energies of the pure elements). The calculations will reveal how the stability of the NiAl phase changes with increasing Ti substitution, as reflected by the computed cohesive energy and formation enthalpy trends.

## Reproduction target
Perform DFT total energy calculations for NiAl, NiAlTi₁, NiAlTi₂, NiAlTi₃ and for isolated Ni, Al, Ti atoms. Compute the cohesive energy and formation enthalpy for each NiAlTiₓ phase according to the standard definitions provided in the workflow steps. Write the results to the output file dft_energies.json with the specified format. The verifier will assess the computed energies and the trend with Ti content.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- NiAl B2 crystal structure
- SSSP pseudopotentials for Ni, Al, Ti: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Structure model preparation for DFT
- Role: process
- Action: Build atomic models and DFT input files for bulk NiAl (B2), NiAlTi1, NiAlTi2, NiAlTi3 (obtained by substituting Al with Ti in a supercell), and isolated Ni, Al, Ti atoms. Use the standard B2 lattice and public pseudopotentials.
- Evidence: none

### Step 2: DFT total energy calculations
- Role: process
- Action: For each system (NiAl, NiAlTi1, NiAlTi2, NiAlTi3 and isolated Ni, Al, Ti atoms) perform geometry relaxation followed by a final self-consistent field (scf) calculation using Quantum ESPRESSO (pw.x). Collect the converged total energies.
- Evidence: `/app/outputs/total_energies.json`

### Step 3: Compute cohesive energy and formation enthalpy
- Role: scored (load-bearing)
- Action: From the total energies obtained in step 2, compute the cohesive energy and formation enthalpy for each phase (NiAl, NiAlTi1, NiAlTi2, NiAlTi3). Cohesive energy is defined as the difference between the bulk phase total energy and the sum of isolated atom energies. Formation enthalpy is the difference between the cohesive energy of the ternary phase and the cohesive energies of the respective pure elements. Write the results to dft_energies.json.
- Output file: `/app/outputs/dft_energies.json`
- Format: json
- Contract: JSON object with keys 'NiAl', 'NiAlTi1', 'NiAlTi2', 'NiAlTi3'; each value is an object with keys 'cohesive_energy' (float in eV) and 'formation_enthalpy' (float in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_energies.json
- path: `/app/outputs/dft_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Derived cohesive energies and formation enthalpies of NiAlTi_x phases. Checker will compare each value to the paper's reported numbers with tolerance and verify that both quantities become less negative (increase) with Ti content.
- schema:
  - `type`: object
  - `required`:
    - `NiAl`:
      - `cohesive_energy`: float (eV)
      - `formation_enthalpy`: float (eV)
    - `NiAlTi1`:
      - `cohesive_energy`: float (eV)
      - `formation_enthalpy`: float (eV)
    - `NiAlTi2`:
      - `cohesive_energy`: float (eV)
      - `formation_enthalpy`: float (eV)
    - `NiAlTi3`:
      - `cohesive_energy`: float (eV)
      - `formation_enthalpy`: float (eV)
  - `units`:
    - `cohesive_energy`: eV
    - `formation_enthalpy`: eV

Notes: The target_policy exact_match applies with a hidden tolerance; the checker additionally enforces the monotonic trend. This output encapsulates the headline computational result of the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "NiAl": {
            "cohesive_energy": "float (eV)",
            "formation_enthalpy": "float (eV)"
          },
          "NiAlTi1": {
            "cohesive_energy": "float (eV)",
            "formation_enthalpy": "float (eV)"
          },
          "NiAlTi2": {
            "cohesive_energy": "float (eV)",
            "formation_enthalpy": "float (eV)"
          },
          "NiAlTi3": {
            "cohesive_energy": "float (eV)",
            "formation_enthalpy": "float (eV)"
          }
        },
        "units": {
          "cohesive_energy": "eV",
          "formation_enthalpy": "eV"
        }
      },
      "description": "Derived cohesive energies and formation enthalpies of NiAlTi_x phases. Checker will compare each value to the paper's reported numbers with tolerance and verify that both quantities become less negative (increase) with Ti content."
    }
  ],
  "notes": "The target_policy exact_match applies with a hidden tolerance; the checker additionally enforces the monotonic trend. This output encapsulates the headline computational result of the paper."
}
```

## How you are scored
The hidden verifier will independently score your dft_energies.json artifact. It will compare the cohesive energy and formation enthalpy of each phase to expected reference values, and it will also evaluate whether both quantities exhibit the correct monotonic trend with increasing Ti substitution. The final reward is a weighted combination of these checks. Reporting numbers is not sufficient; the verifier expects values that are physically consistent with the DFT workflow you execute.
