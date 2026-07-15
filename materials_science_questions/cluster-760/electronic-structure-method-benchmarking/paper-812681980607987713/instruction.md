# CCSD(T) continued-fraction extrapolation accuracy evaluation on benchmark molecules

## Problem background
Coupled-cluster methods such as CCSD(T) are among the most accurate single‑reference quantum chemistry approaches, but their residual error relative to the full configuration‑interaction (FCI) limit can still be appreciable for many systems.  Extrapolation schemes that post‑process the CCSD(T) energy have been proposed to bring it closer to FCI without increasing the computational cost.  One such scheme uses a continued‑fraction approximant, denoted CCSD(T)‑cf, that combines the SCF, CCSD, and CCSD(T) energies into a new estimate.  This task requires you to compute CCSD(T)‑cf energies for a set of benchmark atoms and molecules and to evaluate how they compare with conventional CCSD(T) results relative to known FCI energies.  The central question is whether the continued‑fraction extrapolation consistently reduces the absolute error toward FCI across a representative set of systems.

## Approach
The workflow has two stages.  First, you will run frozen‑core restricted Hartree–Fock (SCF), CCSD, and CCSD(T) calculations on seven benchmark systems using the open‑source package PySCF with the specified basis sets.  These calculations produce the three total energies E_SCF, E_CCSD and E_CCSD(T) for each system.  Second, you will apply the continued‑fraction extrapolation to obtain the CCSD(T)‑cf energy.  Let δ1 = E_SCF, δ2 = E_CCSD − E_SCF, and δ3 = E_CCSD(T) − E_CCSD.  The extrapolated energy is then given by

  E_CCSD(T)‑cf = δ1 / (1 − (δ2/δ1) / (1 − δ3/δ2))

The comparison of interest is between the errors of conventional CCSD(T) and those of CCSD(T)‑cf, both measured against FCI reference values (which are not provided to you).  You will output for each system all four energies (E_SCF, E_CCSD, E_CCSD(T), E_CCSD(T)‑cf) in a single JSON file.  The hidden verifier will compare these computed energies to the FCI benchmarks and will grade the improvement and consistency with published data.

## Reproduction target
Produce a JSON file `/app/outputs/step_01_energies.json` containing the total energies (in Hartree) for the following seven systems:
  BH/cc‑pVDZ, CH₂(³B₁)/DZP, NH₂(²B₁)/DZP, Ne/cc‑pVDZ, F⁻/cc‑pVDZ, H₂O/cc‑pVDZ, N₂/cc‑pVDZ.
For each entry, report the four energies: E_SCF, E_CCSD, E_CCSD(T), and E_CCSD(T)‑cf.  The goal is to demonstrate that the CCSD(T)‑cf energies yield smaller absolute errors relative to FCI than the corresponding CCSD(T) energies, and that the errors are consistent with known reference values.

## Assets

- Benchmark molecular geometries: https://raw.githubusercontent.com/Goodson2002/benchmark-geometries/main/geometries.xyz
- PySCF quantum chemistry package: python3 -m pip install pyscf
- Basis set definitions (cc-pVDZ, aug-cc-pVDZ, DZP, etc.): Basis Set Exchange https://www.basissetexchange.org/

## Workflow steps

### Step 1: Run SCF, CCSD, and CCSD(T) calculations
- Role: process
- Action: For each system (BH/cc-pVDZ, CH₂(³B₁)/DZP, NH₂(²B₁)/DZP, Ne/cc-pVDZ, F⁻/cc-pVDZ, H₂O/cc-pVDZ, N₂/cc-pVDZ) obtain the molecular geometry from the provided public geometry file. Using PySCF, perform frozen-core restricted Hartree-Fock (SCF), CCSD, and CCSD(T) calculations with the specified basis sets, saving the total energies (E_SCF, E_CCSD, E_CCSD(T)) for each system.
- Evidence: `/app/outputs/raw_energies.json`

### Step 2: Compute CCSD(T)-cf energies and write final artifact
- Role: scored (load-bearing)
- Action: For each system, compute δ1 = E_SCF, δ2 = E_CCSD − E_SCF, δ3 = E_CCSD(T) − E_CCSD. Apply the continued-fraction formula to obtain CCSD(T)-cf energy. Write an array of objects containing system, basis, E_SCF, E_CCSD, E_CCSD(T), and E_CCSD(T)-cf for all systems to /app/outputs/step_01_energies.json.
- Output file: `/app/outputs/step_01_energies.json`
- Format: json
- Contract: Array of objects: each with string fields 'system' and 'basis', and numeric fields 'E_SCF', 'E_CCSD', 'E_CCSD(T)', 'E_CCSD(T)-cf' (energies in Hartree, float).
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
- target_policy: metric_recompute
- description: JSON array containing the computed SCF, CCSD, CCSD(T), and CCSD(T)-cf total energies for the seven benchmark systems. The hidden checker recomputes errors relative to FCI reference values and verifies improvement and consistency with published data.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `basis`, `E_SCF`, `E_CCSD`, `E_CCSD(T)`, `E_CCSD(T)-cf`
    - `properties`:
      - `system`:
        - `type`: string
      - `basis`:
        - `type`: string
      - `E_SCF`:
        - `type`: number
        - `unit`: Hartree
      - `E_CCSD`:
        - `type`: number
        - `unit`: Hartree
      - `E_CCSD(T)`:
        - `type`: number
        - `unit`: Hartree
      - `E_CCSD(T)-cf`:
        - `type`: number
        - `unit`: Hartree

Notes: Only the CCSD(T)-cf extrapolation improvement claim is evaluated. The MP4-qλ and z_d singularity analysis are out of scope. The agent must run the quantum chemistry calculations from scratch; no pre-computed energies are provided.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system",
            "basis",
            "E_SCF",
            "E_CCSD",
            "E_CCSD(T)",
            "E_CCSD(T)-cf"
          ],
          "properties": {
            "system": {
              "type": "string"
            },
            "basis": {
              "type": "string"
            },
            "E_SCF": {
              "type": "number",
              "unit": "Hartree"
            },
            "E_CCSD": {
              "type": "number",
              "unit": "Hartree"
            },
            "E_CCSD(T)": {
              "type": "number",
              "unit": "Hartree"
            },
            "E_CCSD(T)-cf": {
              "type": "number",
              "unit": "Hartree"
            }
          }
        }
      },
      "description": "JSON array containing the computed SCF, CCSD, CCSD(T), and CCSD(T)-cf total energies for the seven benchmark systems. The hidden checker recomputes errors relative to FCI reference values and verifies improvement and consistency with published data."
    }
  ],
  "notes": "Only the CCSD(T)-cf extrapolation improvement claim is evaluated. The MP4-qλ and z_d singularity analysis are out of scope. The agent must run the quantum chemistry calculations from scratch; no pre-computed energies are provided."
}
```

## How you are scored
A hidden verifier will read your submitted `step_01_energies.json`.  For each system it compares your computed energies to hidden FCI reference values and checks two main properties:
  (1) Whether the absolute error of CCSD(T)‑cf is smaller than the absolute error of CCSD(T) (i.e., improvement).
  (2) Whether the computed absolute errors for CCSD(T) and CCSD(T)‑cf fall within a tolerance of the corresponding values reported in the literature.
The final reward is a weighted sum of the number of systems that satisfy both criteria; full credit is awarded if at least six of the seven systems meet the requirements.  The verifier never penalizes a result that outperforms the reference; it only checks that the errors are not larger than allowed and that improvement is achieved.
