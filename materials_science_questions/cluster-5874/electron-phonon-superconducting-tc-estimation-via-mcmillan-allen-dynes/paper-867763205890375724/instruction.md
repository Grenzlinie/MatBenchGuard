# Compute Superconducting and Antiferromagnetic Transition Temperatures

## Problem background
In a metallic antiferromagnet composed of stacked conductive layers that are ferromagnetically polarized with alternating magnetization direction, interlayer antiferromagnetic exchange interactions can induce interlayer spin‑singlet Cooper pairing. The paper derives analytical expressions for the antiferromagnetic transition temperature T_AF and the superconducting transition temperature T_c as functions of the on‑site Coulomb repulsion U, the interlayer exchange coupling J, the density of states ρ0, the electron density n, and an effective bandwidth cutoff W_c. This task investigates the relationship between T_AF and T_c by computing both temperatures for a set of prescribed dimensionless parameters and recording when T_AF exceeds T_c.

## Approach
The model treats each layer as a two‑dimensional electron system with an on‑site Coulomb repulsion U and a nearest‑neighbor antiferromagnetic interlayer exchange J (ferromagnetic within a layer). In a mean‑field / random‑phase approximation the antiferromagnetic order with wave‑vector (0,0,π/c) occurs when (U+J)χ₀ = 1, yielding an explicit expression for T_AF. Superconductivity is introduced through interlayer spin‑singlet pairing of electrons on adjacent layers with opposite spins, with the same exchange J providing the pairing attraction. The BCS gap equation leads to a formula for T_c that depends on the dimensionless coupling Jρ0 and the cutoff W_c. The task is to evaluate these analytical formulas for several parameter combinations and record the results.

## Reproduction target
Compute T_c and T_AF for at least five different values of the dimensionless coupling Jρ0 (e.g., 0.05 to 0.5) while keeping Uρ0 = 1.0, n = 2, and W_c = 1. For each parameter set evaluate whether T_AF > T_c and T_AF > 0, and record a boolean indicating if the antiferromagnetic ordering temperature exceeds the superconducting one. Write the results as a CSV file with columns: Jρ0, Uρ0, n, W_c, T_c, T_AF, T_AF_gt_T_c.

## Assets
No external datasets or pretrained models are required. All necessary formulas and parameter values are given in the instruction. A standard Python 3 environment with the built‑in math module is sufficient to implement the computations.

## Workflow steps

### Step 1: Compute Tc and T_AF for parameter sets
- Role: scored (load-bearing)
- Action: Implement the given formulas for the superconducting transition temperature T_c = 1.13 * W_c * exp(-2/(Jρ0)) and the antiferromagnetic transition temperature T_AF = n/(2ρ0 * ln((U+J)ρ0 / ((U+J)ρ0 - 1))) with ρ0=1. For at least five different values of Jρ0 (e.g., 0.05 to 0.5) while fixing Uρ0=1.0, n=2, W_c=1, compute T_c and T_AF. For each row, evaluate whether T_AF > T_c and T_AF > 0; record as boolean T_AF_gt_T_c. Write the results to results.csv.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: Jρ0 (float), Uρ0 (float), n (int), W_c (float), T_c (float), T_AF (float), T_AF_gt_T_c (bool)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of computed transition temperatures Tc and T_AF for given coupling constants, along with a boolean indicating whether T_AF > T_c when T_AF>0.
- schema:
  - `type`: table
  - `required_columns`: `Jρ0`, `Uρ0`, `n`, `W_c`, `T_c`, `T_AF`, `T_AF_gt_T_c`
  - `units`: object

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Jρ0",
          "Uρ0",
          "n",
          "W_c",
          "T_c",
          "T_AF",
          "T_AF_gt_T_c"
        ],
        "units": {}
      },
      "description": "Table of computed transition temperatures Tc and T_AF for given coupling constants, along with a boolean indicating whether T_AF > T_c when T_AF>0."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your submitted results.csv and extracts the parameter columns (Jρ0, Uρ0, n, W_c). It recomputes T_c and T_AF using the same analytical formulas and checks that your reported temperatures match the recomputed values within a hidden tolerance. It also verifies that the boolean T_AF_gt_T_c is correct according to the definition (true when T_AF > T_c and T_AF > 0). The final reward is the fraction of rows for which all checks pass. Providing a correct implementation that yields accurate floating‑point numbers is essential; simply reporting expected values without correct computation will not pass.
