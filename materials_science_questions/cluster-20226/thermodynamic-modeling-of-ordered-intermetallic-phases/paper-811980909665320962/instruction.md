# Compute zero-wavenumber structure factor S_CC(0) under frozen-in and chemical equilibrium conditions for a strongly associating mixture

## Problem background
Binary liquid mixtures with a strong tendency to form chemical associates (e.g., A2B complexes) exhibit concentration-concentration structure factors at zero wavenumber, S_CC(0), that depend on the state of the chemical reaction. In a frozen-in (non-equilibrium) situation, such as rapidly quenched melts, the number of complexes is fixed; under full chemical equilibrium, it is determined by the mass action law. This task explores that difference quantitatively: we compute S_CC(0) at two representative concentrations for a model strongly associating A–B mixture, comparing the equilibrium and frozen-in cases to quantify how the structural order differs.

## Approach
We treat the binary A–B mixture as a ternary system of free A atoms, free B atoms, and A2B complexes (μ=2, ν=1). In the substitutional alloy approximation, the S_CC(0) of the binary system is expressed directly in terms of the numbers of atoms and complexes and the overall composition. For a given total atom count N, the complex number n3 is determined in two ways: (a) frozen-in: n3 is set to N c / μ (satisfying the compound’s stoichiometry at concentration c ≤ c_c = μ/(μ+ν)); (b) equilibrium: n3 is solved from the mass action law n3 / (n1^μ n2^ν) = K, where K is derived from a specified mixing free energy, together with atom conservation n1 = Nc − μ n3, n2 = N(1−c) − ν n3, with all n_i ≥ 0. Using these n_i values, S_CC(0) is computed from the substitutional alloy formula that depends only on N, the composition c, the stoichiometric coefficients, and n3. The compressibility term cancels out, leaving a closed-form expression.

## Reproduction target
Compute S_CC(0) at two concentrations c = 0.1 and c = 2/3 (the compound stoichiometry) using the model described above. For each concentration, evaluate S_CC(0) under the frozen-in assumption and under full chemical equilibrium with G_M(c_c)/RT = −3. Save the four dimensionless values as a JSON object with keys "frozen_in_c0p1", "equilibrium_c0p1", "frozen_in_c2p3", "equilibrium_c2p3" into the file /app/outputs/scc_results.json.

## Assets
There are no external datasets, models, or proprietary tools required. The workflow only needs standard numerical computing libraries (e.g., numpy, scipy) that the agent can install from the Python package index. No paper-specific code or data files are provided.

## Workflow steps

### Step 1: Compute S_CC(0) for frozen-in and equilibrium cases
- Role: scored
- Action: Implement the substitutional alloy model for a binary A–B mixture with A2B associates (μ=2, ν=1). Use total atom count N=1000. For each concentration c in {0.1, 2/3}: (1) Frozen-in case: set n3 = N * c / μ. (2) Equilibrium case: solve n3 from the mass action law n3 / (n1^μ * n2^ν) = K, where K = exp((μ+ν) * G_M(c_c)/RT) with G_M(c_c)/RT = -3, and n1, n2 satisfy atom conservation n1 = N*c - μ*n3, n2 = N*(1-c) - ν*n3, while ensuring n1, n2, n3 ≥ 0. Compute S_CC(0) from the substitutional alloy expression S_CC(0) = c(1-c) - (n3/N)[μ(1-c)^2 + ν c^2 - (μ+ν)^2 (c_c - c)^2] where c_c = μ/(μ+ν). Save the four values as a JSON object with keys frozen_in_c0p1, equilibrium_c0p1, frozen_in_c2p3, equilibrium_c2p3 in /app/outputs/scc_results.json.
- Output file: `/app/outputs/scc_results.json`
- Format: json
- Contract: {"frozen_in_c0p1": float, "equilibrium_c0p1": float, "frozen_in_c2p3": float, "equilibrium_c2p3": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/scc_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### scc_results.json
- path: `/app/outputs/scc_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: S_CC(0) values for two concentrations under frozen-in and equilibrium states computed from the substitutional alloy model.
- schema:
  - `type`: object
  - `required`: `frozen_in_c0p1`, `equilibrium_c0p1`, `frozen_in_c2p3`, `equilibrium_c2p3`
  - `properties`:
    - `frozen_in_c0p1`:
      - `type`: number
      - `unit`: dimensionless
    - `equilibrium_c0p1`:
      - `type`: number
      - `unit`: dimensionless
    - `frozen_in_c2p3`:
      - `type`: number
      - `unit`: dimensionless
    - `equilibrium_c2p3`:
      - `type`: number
      - `unit`: dimensionless

Notes: The values are deterministic given the stated parameters. The checker recomputes them independently and compares with a tight relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "scc_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "frozen_in_c0p1",
          "equilibrium_c0p1",
          "frozen_in_c2p3",
          "equilibrium_c2p3"
        ],
        "properties": {
          "frozen_in_c0p1": {
            "type": "number",
            "unit": "dimensionless"
          },
          "equilibrium_c0p1": {
            "type": "number",
            "unit": "dimensionless"
          },
          "frozen_in_c2p3": {
            "type": "number",
            "unit": "dimensionless"
          },
          "equilibrium_c2p3": {
            "type": "number",
            "unit": "dimensionless"
          }
        }
      },
      "description": "S_CC(0) values for two concentrations under frozen-in and equilibrium states computed from the substitutional alloy model."
    }
  ],
  "notes": "The values are deterministic given the stated parameters. The checker recomputes them independently and compares with a tight relative tolerance."
}
```

## How you are scored
A hidden verifier independently recomputes the four expected S_CC(0) values from the same model and parameter set. It compares each of your submitted numbers to the expected value within a tight relative tolerance. Your reward is the fraction of the four values that fall within the tolerance, so providing accurate calculations for all four conditions yields the highest score. The verifier does not require any external resources; scoring is deterministic.
