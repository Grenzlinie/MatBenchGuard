# Dipole Moment Calculation of Si-O Bond Using Slater Orbitals and Electron Localization Assessment

## Problem background
Oxidized silicon surfaces are explored for nanoscale memory cells that store charge via localized electron states. A critical requirement for a bound electron is that the dipole moment of a surface bond exceeds a threshold known as the Lakhno critical dipole moment. This task focuses on the Si–O bond: compute its dipole moment from first‑principles Slater‑type atomic orbitals and compare it against the critical value to determine whether the Si–O configuration can support a localized bound electron state.

## Approach
Use the Slater‑type atomic orbital forms for silicon 3p and oxygen 2p as defined in the literature. Compute the overlap integral between these orbitals by integrating the product of the two wavefunctions over the relevant spatial coordinates (radial and angular parts). From the overlap integral, derive the Si–O bond dipole moment at a bond length of 1.6 Å (corresponding to r/a0 = 3). The computation involves evaluating analytically tractable radial and angular integrals; the Lakhno critical dipole moment (0.318 D) serves as the benchmark for electron localization.

## Reproduction target
Compute the Si–O bond dipole moment at a bond length of 1.6 Å (r/a0 = 3) using the Slater orbital overlap integral as described. Report the resulting dipole moment in Debye. Then determine whether this dipole moment exceeds the Lakhno critical dipole moment of 0.318 D, and record both the computed dipole moment and the Boolean exceed flag. All outputs must be saved in a JSON file with keys 'mu_Si_O' (float, Debye) and 'exceeds_critical' (boolean).

## Assets

- Python scientific computing stack: numpy scipy

## Workflow steps

### Step 1: Define Slater orbitals and compute overlap integrals
- Role: process
- Action: Define the Slater-type atomic orbitals for Si(3p) and O(2p) as described in the paper. Compute the overlap integrals for the 3pSi-2pO pair as a function of interatomic distance, and save the computed overlap values for a set of representative distances as verification that the orbital implementation is correct.
- Evidence: `/app/outputs/overlap_integrals.json`

### Step 2: Compute Si-O dipole moment and localization assessment
- Role: scored (load-bearing)
- Action: Using the Slater orbital overlap integral as derived in the paper, compute the dipole moment of the Si-O bond at a bond length of 1.6 Å (r/a0 = 3). Perform the integration over radial and angular coordinates and obtain the dipole moment value in Debye. Determine whether this dipole moment exceeds the critical value for electron localization (Lakhno criterion). Record both the computed dipole moment and the Boolean exceed flag.
- Output file: `/app/outputs/step_01_dipole_result.json`
- Format: json
- Contract: Object with keys 'mu_Si_O' (float, Debye) and 'exceeds_critical' (boolean).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_dipole_result.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_dipole_result.json
- path: `/app/outputs/step_01_dipole_result.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Si-O bond dipole moment and electron localization assessment.
- schema:
  - `type`: object
  - `required`: `mu_Si_O`, `exceeds_critical`
  - `properties`:
    - `mu_Si_O`:
      - `type`: number
      - `units`: Debye
    - `exceeds_critical`:
      - `type`: boolean

Notes: The Lakhno critical dipole moment is 0.318 D. The bond length used is 1.6 Å.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_dipole_result.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "mu_Si_O",
          "exceeds_critical"
        ],
        "properties": {
          "mu_Si_O": {
            "type": "number",
            "units": "Debye"
          },
          "exceeds_critical": {
            "type": "boolean"
          }
        }
      },
      "description": "Si-O bond dipole moment and electron localization assessment."
    }
  ],
  "notes": "The Lakhno critical dipole moment is 0.318 D. The bond length used is 1.6 Å."
}
```

## How you are scored
A hidden verifier independently reads your output files. It compares the computed dipole moment to a reference value using a tolerance and checks the Boolean exceed flag. The reward is a weighted combination of these checks; the exact reference and tolerance are not disclosed. No portion of the reward is based on reproducing a particular format or on replicating any other artifact from the original publication.
