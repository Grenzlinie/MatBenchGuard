# Reproduction of B5O Radical Energetics and Isomerization Barrier

## Problem background
The B5O radical is a hexa-atomic boron-oxide cluster. Previous computational studies have disagreed on the number and nature of low-lying isomers. Determining the ground-state structure, the energetic ordering of candidate isomers, and their kinetic stability is essential for understanding the doping and oxidation processes of pure boron clusters. This task focuses on two key doublet isomers (referred to as ^201 and ^202) and a transition state connecting them (^2Ts02/03).

## Approach
The approach uses a two-level electronic structure strategy. First, the geometrical structures of isomers ^201 and ^202 and the transition state ^2Ts02/03 are optimized at the density functional theory level (B3LYP) with the 6-311+G(d) basis set, and harmonic vibrational frequencies are computed to obtain zero-point vibrational energy (ZPVE) corrections. Second, single-point energy calculations are performed on the optimized geometries at the coupled-cluster level (CCSD(T)) with a larger basis set (6-311+G(2df)). The final quantities are the CCSD(T) electronic energies combined with the B3LYP ZPVE corrections, which are used to derive relative energies and isomerization barriers.

## Reproduction target
Compute the ZPVE-corrected total energies (in Hartrees) for isomers ^201, ^202, and the transition state ^2Ts02/03. From these, derive (1) the relative energy of ^202 with respect to ^201, and (2) the isomerization barrier height of ^2Ts02/03 relative to ^201, both expressed in kcal/mol (1 Hartree = 627.509 kcal/mol). The raw electronic energies and ZPVE corrections must be compiled into a JSON file (`energies.json`); the derived relative energies and barrier are not required in the file but will be recomputed by the verifier.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Basis sets (6-311+G(d), 6-311+G(2df)): https://www.basissetexchange.org/

## Workflow steps

### Step 1: Optimize geometry and compute frequencies for isomer ^201
- Role: process
- Action: Construct initial geometry for the belt-like B5O doublet isomer (labeled ^201 in the paper). Perform geometry optimization and harmonic vibrational frequency calculation at the B3LYP/6-311+G(d) level. Verify the resulting stationary point is a minimum (no imaginary frequencies). Save the final electronic energy and zero-point vibrational energy (ZPVE) correction.
- Evidence: `/app/outputs/201_opt_freq.out`

### Step 2: Optimize geometry and compute frequencies for isomer ^202
- Role: process
- Action: Construct initial geometry for the B5O doublet isomer bearing an exocyclic BO moiety (labeled ^202). Perform geometry optimization and harmonic vibrational frequency calculation at B3LYP/6-311+G(d). Confirm the structure is a minimum (all real frequencies). Record the final electronic energy and ZPVE.
- Evidence: `/app/outputs/202_opt_freq.out`

### Step 3: Optimize geometry and compute frequencies for transition state ^2Ts02/03
- Role: process
- Action: Use the optimized geometries of ^201 and ^202 from Steps 1 and 2 to perform a Quadratic Synchronous Transit (QST2) calculation at the B3LYP/6-311+G(d) level to obtain an initial guess for the transition state connecting them. Then, perform a transition-state optimization and harmonic vibrational frequency calculation at the same level. Verify that the converged stationary point has exactly one imaginary frequency. Optionally, confirm the connectivity between the two minima via an intrinsic reaction coordinate (IRC) calculation. Record the final electronic energy and ZPVE.
- Evidence: `/app/outputs/Ts02_03_opt_freq.out`

### Step 4: High-level single-point energy calculations
- Role: process
- Action: Using the optimized geometries from steps 1-3, perform single-point energy calculations at the CCSD(T)/6-311+G(2df) level for isomers ^201, ^202, and the transition state ^2Ts02/03. Record the total electronic energies.
- Evidence: `/app/outputs/ccsdt_sp.out`

### Step 5: Compile energies and ZPVE into JSON
- Role: scored (load-bearing)
- Action: Extract the CCSD(T) total electronic energies (in Hartrees) and the B3LYP ZPVE corrections (in Hartrees, unscaled) for ^201, ^202, and ^2Ts02/03 from the output files of steps 1-4. Write a JSON file containing, for each species, the electronic energy and ZPVE. Use the keys '201', '202', and 'Ts02_03'.
- Output file: `/app/outputs/energies.json`
- Format: json
- Contract: Object with top-level keys '201', '202', 'Ts02_03'. Each value is an object with entries: 'electronic_energy' (float, units Hartrees) and 'zpe' (float, units Hartrees).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.json
- path: `/app/outputs/energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: JSON file with electronic energies and ZPVE corrections for the key stationary points. The checker will compute ZPVE-corrected total energies and then derive relative energy of ^202 vs ^201 and the barrier height of ^2Ts02/03 relative to ^201, both in kcal/mol (1 Hartree = 627.509 kcal/mol).
- schema:
  - `type`: object
  - `required`:
    - `201`:
      - `electronic_energy`: number
      - `zpe`: number
    - `202`:
      - `electronic_energy`: number
      - `zpe`: number
    - `Ts02_03`:
      - `electronic_energy`: number
      - `zpe`: number
  - `units`:
    - `electronic_energy`: Hartrees
    - `zpe`: Hartrees

Notes: The checker recomputes relative energies and isomerization barrier from the submitted raw energies; no absolute target values are provided in the task. The reproduction relies on re-running the electronic structure workflow with an open-source code (ORCA) and standard basis sets. The IRC connectivity verification for the transition state is optional but recommended.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "201": {
            "electronic_energy": "number",
            "zpe": "number"
          },
          "202": {
            "electronic_energy": "number",
            "zpe": "number"
          },
          "Ts02_03": {
            "electronic_energy": "number",
            "zpe": "number"
          }
        },
        "units": {
          "electronic_energy": "Hartrees",
          "zpe": "Hartrees"
        }
      },
      "description": "JSON file with electronic energies and ZPVE corrections for the key stationary points. The checker will compute ZPVE-corrected total energies and then derive relative energy of ^202 vs ^201 and the barrier height of ^2Ts02/03 relative to ^201, both in kcal/mol (1 Hartree = 627.509 kcal/mol)."
    }
  ],
  "notes": "The checker recomputes relative energies and isomerization barrier from the submitted raw energies; no absolute target values are provided in the task. The reproduction relies on re-running the electronic structure workflow with an open-source code (ORCA) and standard basis sets. The IRC connectivity verification for the transition state is optional but recommended."
}
```

## How you are scored
A hidden verifier reads your `energies.json`, extracts the electronic energies and ZPVE corrections, computes ZPVE-corrected total energies, and then calculates the relative isomer energy and the isomerization barrier. These computed values are compared against independently established reference values, allowing for implementation tolerances. Full credit is awarded if both quantities fall within the respective allowed ranges; greater deviation results in proportionally lower scores. Simply reporting the paper's numbers is not sufficient — the verifier checks that the raw energies are genuine and lead to the correct derived values.
