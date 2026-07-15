# Reproduce proton transfer geometries and activation energies with hybrid DFT

## Problem background
Proton transfer between methane (CH₄) and methyl radical (CH₃·) is a fundamental organic reaction whose activation barrier has been measured experimentally (14.1 kcal/mol). Accurate computational prediction of the barrier is challenging, with Hartree–Fock and MP2 methods overestimating it. This study applies hybrid density functional theory (DFT) methods—including Becke3LYP and Becke3P86—with basis sets such as 6‑31G(d) to model the reaction, and compares the results to ROHF and MP2 ab initio calculations. The key deliverables are optimized equilibrium geometries (C–H bond lengths) and activation energies computed as the energy difference between the transition state and the separated reactants.

## Approach
Hybrid DFT methods combine Hartree–Fock exchange with DFT exchange‑correlation functionals to improve predictions of thermochemistry and geometries. In this task, you will perform unrestricted/open‑shell geometry optimizations on three molecular structures: CH₃ (methyl radical), CH₄ (methane), and the transition state (TS) for proton transfer between them. Two levels of theory are used: Becke3LYP/6‑31G(d) and MP2/6‑31G(d). The optimizations are performed without any symmetry constraints or structural constraints. From the converged geometries you will extract the equilibrium C–H bond lengths in CH₃ and CH₄. The total energies of CH₃, CH₄, and the TS provide the activation energy for each method, calculated as E(TS) – (E(CH₃) + E(CH₄)). The computed bond lengths and activation energies are the reproduction targets.

## Reproduction target
Compute optimized geometries and total energies for CH₃, CH₄, and the proton‑transfer transition state using PySCF at the Becke3LYP/6‑31G(d) and MP2/6‑31G(d) levels. Extract the C–H bond length from each optimized CH₃ and CH₄ structure. Compute the activation energy for each method as E(TS) – (E(CH₃) + E(CH₄)), converted from Hartree to kcal/mol (1 Hartree = 627.5095 kcal/mol). Write a single JSON file, results.json, containing these six numbers:
- CH3_bond_length_Becke3LYP (Å)
- CH3_bond_length_MP2 (Å)
- CH4_bond_length_Becke3LYP (Å)
- CH4_bond_length_MP2 (Å)
- activation_energy_Becke3LYP (kcal/mol)
- activation_energy_MP2 (kcal/mol)
The verifier will compare your numbers against hidden reference values that correspond to the same computational protocol. You must also save the optimisation log as optim_log.txt.

## Assets

- PySCF: https://pypi.org/project/pyscf/

## Workflow steps

### Step 1: Geometry optimizations and energy calculations
- Role: process
- Action: Using PySCF, construct initial structures for CH3 (methyl radical, C–H ≈ 1.08 Å), CH4 (tetrahedral, C–H ≈ 1.09 Å), and the transition state (approximately linear H3C–H–CH3 with r1 ≈ 1.08 Å, r2 ≈ 1.33 Å). Perform unrestricted/open-shell geometry optimizations without symmetry or structural constraints at the Becke3LYP/6-31G(d) and MP2/6-31G(d) levels, saving the final coordinates and total energies.
- Evidence: `/app/outputs/optim_log.txt`

### Step 2: Extract bond lengths and compute activation energies
- Role: scored (load-bearing)
- Action: From the optimized geometries produced in the previous step, extract the C–H bond lengths for CH3 and CH4 (for both Becke3LYP and MP2 methods). Retrieve the total energies of CH3, CH4, and TS from the optimization outputs. Compute the activation energy for each method as E(TS) – (E(CH3) + E(CH4)) and convert the result from Hartree to kcal/mol (1 Hartree = 627.5095 kcal/mol). Write a single JSON file containing the six fields specified in the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"CH3_bond_length_Becke3LYP": <number (Å)>, "CH3_bond_length_MP2": <number (Å)>, "CH4_bond_length_Becke3LYP": <number (Å)>, "CH4_bond_length_MP2": <number (Å)>, "activation_energy_Becke3LYP": <number (kcal/mol)>, "activation_energy_MP2": <number (kcal/mol)>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized C–H bond lengths in CH3 and CH4 for Becke3LYP and MP2 methods (Å) and activation energies (kcal/mol) computed as E(TS) – E(CH3) – E(CH4). All six numeric fields must be present.
- schema:
  - `type`: object
  - `required`: `CH3_bond_length_Becke3LYP`, `CH3_bond_length_MP2`, `CH4_bond_length_Becke3LYP`, `CH4_bond_length_MP2`, `activation_energy_Becke3LYP`, `activation_energy_MP2`
  - `properties`:
    - `CH3_bond_length_Becke3LYP`:
      - `type`: number
      - `unit`: Å
    - `CH3_bond_length_MP2`:
      - `type`: number
      - `unit`: Å
    - `CH4_bond_length_Becke3LYP`:
      - `type`: number
      - `unit`: Å
    - `CH4_bond_length_MP2`:
      - `type`: number
      - `unit`: Å
    - `activation_energy_Becke3LYP`:
      - `type`: number
      - `unit`: kcal/mol
    - `activation_energy_MP2`:
      - `type`: number
      - `unit`: kcal/mol

Notes: The hidden checker compares each field to the paper's reported values with predetermined tolerances. All fields must fall within tolerance for full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "CH3_bond_length_Becke3LYP",
          "CH3_bond_length_MP2",
          "CH4_bond_length_Becke3LYP",
          "CH4_bond_length_MP2",
          "activation_energy_Becke3LYP",
          "activation_energy_MP2"
        ],
        "properties": {
          "CH3_bond_length_Becke3LYP": {
            "type": "number",
            "unit": "Å"
          },
          "CH3_bond_length_MP2": {
            "type": "number",
            "unit": "Å"
          },
          "CH4_bond_length_Becke3LYP": {
            "type": "number",
            "unit": "Å"
          },
          "CH4_bond_length_MP2": {
            "type": "number",
            "unit": "Å"
          },
          "activation_energy_Becke3LYP": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "activation_energy_MP2": {
            "type": "number",
            "unit": "kcal/mol"
          }
        }
      },
      "description": "Optimized C–H bond lengths in CH3 and CH4 for Becke3LYP and MP2 methods (Å) and activation energies (kcal/mol) computed as E(TS) – E(CH3) – E(CH4). All six numeric fields must be present."
    }
  ],
  "notes": "The hidden checker compares each field to the paper's reported values with predetermined tolerances. All fields must fall within tolerance for full credit."
}
```

## How you are scored
A hidden verifier reads your results.json and compares each of the six numeric fields to hidden reference values that were obtained with the same methodology (Becke3LYP/6‑31G(d) and MP2/6‑31G(d)). The comparison uses predetermined tolerances that account for typical implementation‑dependent differences (different optimizer, numerical settings, etc.). Full credit (reward = 1.0) is awarded only if **all six fields** fall within the specified tolerance. There is no partial credit; a single field outside tolerance yields a reward of zero. The verifier does not inspect your optimisation log (optim_log.txt) numerically, but you must still produce it as process evidence.
