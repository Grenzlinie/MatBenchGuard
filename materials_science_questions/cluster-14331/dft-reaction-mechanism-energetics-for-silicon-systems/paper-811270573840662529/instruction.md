# SiH5- Pseudorotation Barrier

## Problem background
Pentacoordinated silicon species such as SiH5- can undergo Berry pseudorotation, a process that interconverts equivalent molecular geometries through a low-lying transition state. Predicting the energy barrier for this fluxional motion is important for understanding the dynamics of hypervalent silicon compounds. This task asks you to compute the pseudorotation barrier for SiH5- using ab initio quantum chemistry methods.

## Approach
Use the MP2 electron correlation method with the 6-31G(d,p) basis set to perform full geometry optimizations on both the minimum-energy structure and the transition state of SiH5-. Confirm the transition state has exactly one imaginary vibrational frequency. The barrier is the energy difference between the transition state and the minimum, expressed in kcal/mol.

## Reproduction target
Calculate the activation barrier for Berry pseudorotation of SiH5- at the MP2/6-31G(d,p) level of theory. Write the barrier value as a single floating-point number (in kcal/mol) to the file `/app/outputs/barrier_kcal_mol.txt`.

## Assets

- Psi4: https://psicode.org/

## Workflow steps

### Step 1: Optimize SiH5- minimum at MP2/6-31G(d,p)
- Role: process
- Action: Build the SiH5- molecular system and perform a geometry optimization at the MP2/6-31G(d,p) level to locate a minimum-energy structure.
- Evidence: none

### Step 2: Transition state search and frequency verification for SiH5-
- Role: process
- Action: Locate the transition state (TS) for Berry pseudorotation of SiH5- at the MP2/6-31G(d,p) level. Confirm the TS character by a vibrational frequency calculation showing exactly one imaginary frequency. Record the TS energy.
- Evidence: none

### Step 3: Compute pseudorotation barrier
- Role: scored (load-bearing)
- Action: Calculate the activation barrier as ΔE = E(TS) – E(min) using the energies from the previous steps, convert to kcal/mol, and write the result to /app/outputs/barrier_kcal_mol.txt.
- Output file: `/app/outputs/barrier_kcal_mol.txt`
- Format: txt
- Contract: A single ASCII floating-point number, e.g., '2.0'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/barrier_kcal_mol.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### barrier_kcal_mol.txt
- path: `/app/outputs/barrier_kcal_mol.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Computed pseudorotation barrier for SiH5- at MP2/6-31G(d,p) level, written as a single float in kcal/mol.
- schema:
  - `type`: text
  - `units`:
    - `value`: kcal/mol

Notes: The checker reads the barrier value from /app/outputs/barrier_kcal_mol.txt and compares it against a target value using an exact_match policy with a tolerance (not disclosed). The barrier must be computed by the workflow described in the process steps; a hard-coded value may be detected only by the tolerance window.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "barrier_kcal_mol.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": {
          "value": "kcal/mol"
        }
      },
      "description": "Computed pseudorotation barrier for SiH5- at MP2/6-31G(d,p) level, written as a single float in kcal/mol."
    }
  ],
  "notes": "The checker reads the barrier value from /app/outputs/barrier_kcal_mol.txt and compares it against a target value using an exact_match policy with a tolerance (not disclosed). The barrier must be computed by the workflow described in the process steps; a hard-coded value may be detected only by the tolerance window."
}
```

## How you are scored
A hidden verifier reads the barrier value you write to `/app/outputs/barrier_kcal_mol.txt` and compares it against a reference value derived from the original publication. Your work will be scored based on how close your computed barrier is to that hidden reference; the verdict is determined solely by that comparison. The process steps (geometry optimization, transition state search, frequency verification) are required but not directly scored—only the final barrier value matters.
