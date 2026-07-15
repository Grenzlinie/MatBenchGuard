# Compute the Entropy of Liquid Cyclohexane from Heat Capacity and Phase Transition Data

## Problem background
Cyclohexane is a fundamental organic compound whose thermodynamic properties are essential for understanding phase behavior and reaction energetics. This task computes the molal entropy of liquid cyclohexane at 298.16 K in its standard state using experimental calorimetric data. The entropy is determined by integrating the heat capacity over temperature and adding the entropy contributions from solid–solid transitions and fusion. The computed entropy demonstrates how careful calorimetry can yield precise thermodynamic state functions.

## Approach
The entropy is computed by summing contributions over the entire temperature range from 0 K to 298.16 K. For temperatures below 18 K, where direct heat capacity measurements are unavailable, the Debye model is employed with a characteristic temperature and degrees of freedom derived from the low‑temperature behavior. From 18 K to the melting point, the entropy increment is obtained by numerical integration of Cp/T using the experimental heat capacity data for three distinct phases: Crystal I, Crystal II, and liquid. Phase‑change entropies at the transition temperature (186.10 K) and melting point (279.82 K) are added as ΔH/T using the measured enthalpies of transition and fusion. The final total entropy at 298.16 K is the sum of all these contributions. All necessary input data—the heat capacity table and the transition/fusion parameters—are provided as a CSV file. The workflow is a straightforward integration and arithmetic calculation using standard numerical libraries.

## Reproduction target
Compute the molal entropy of liquid cyclohexane at 298.16 K in cal/(deg·mol) by summing: (1) the Debye‑model entropy at 18 K; (2) the integral of Cp/T from 18 K to 186.10 K for Crystal I; (3) the transition entropy ΔH/T at 186.10 K; (4) the integral of Cp/T from 186.10 K to 279.82 K for Crystal II; (5) the fusion entropy ΔH/T at 279.82 K; and (6) the integral of Cp/T from 279.82 K to 298.16 K for the liquid. The result must be written to `entropy_cyclohexane.json` with a single field `entropy_298_16`. The tolerance and exact paper‑reported value are hidden.

## Assets

- Cyclohexane heat capacity data: https://raw.githubusercontent.com/Paper2ARM/cyclohexane-entropy-reproduction/main/heat_capacity_data.csv
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Load heat capacity data
- Role: process
- Action: Load the provided CSV file containing experimental heat capacity data for cyclohexane (columns: T (K), Cp (cal/mol/K), phase). The file also contains transition and fusion parameters in a separate block.
- Evidence: none

### Step 2: Compute Debye entropy (0 to 18 K)
- Role: process
- Action: Using the Debye model with a Debye temperature of 150 K and 6 degrees of freedom, compute the entropy S_18 at 18 K.
- Evidence: none

### Step 3: Integrate Cp/T for Crystals I (18-186.1 K)
- Role: process
- Action: Integrate Cp/T over the temperature range 18.0 K to 186.1 K using the heat capacity data for the Crystal I phase to obtain the entropy increment ΔS_Crystal_I.
- Evidence: none

### Step 4: Compute transition entropy at 186.10 K
- Role: process
- Action: Compute the entropy of the solid-solid transition at 186.10 K using ΔS_trans = ΔH_trans / T_trans, where ΔH_trans = 1610.8 cal/mol.
- Evidence: none

### Step 5: Integrate Cp/T for Crystals II (186.1-279.82 K)
- Role: process
- Action: Integrate Cp/T over the temperature range 186.1 K to 279.82 K using the heat capacity data for the Crystal II phase to obtain ΔS_Crystal_II.
- Evidence: none

### Step 6: Compute fusion entropy at 279.82 K
- Role: process
- Action: Compute the entropy of fusion at 279.82 K using ΔS_fusion = ΔH_fusion / T_fusion, where ΔH_fusion = 639.8 cal/mol.
- Evidence: none

### Step 7: Integrate Cp/T for liquid (279.82-298.16 K)
- Role: process
- Action: Integrate Cp/T over the temperature range 279.82 K to 298.16 K using the heat capacity data for the liquid phase to obtain ΔS_liquid.
- Evidence: none

### Step 8: Compute total entropy and output
- Role: scored
- Action: Sum all entropy contributions (S_18, ΔS_Crystal_I, ΔS_trans, ΔS_Crystal_II, ΔS_fusion, ΔS_liquid) to obtain the total molal entropy of liquid cyclohexane at 298.16 K. Write the result to entropy_cyclohexane.json.
- Output file: `/app/outputs/entropy_cyclohexane.json`
- Format: json
- Contract: {"entropy_298_16": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/entropy_cyclohexane.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### entropy_cyclohexane.json
- path: `/app/outputs/entropy_cyclohexane.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The computed molal entropy of liquid cyclohexane at 298.16 K, in cal/deg/mole.
- schema:
  - `type`: object
  - `properties`:
    - `entropy_298_16`:
      - `type`: number
      - `units`: cal/(deg mol)
  - `required`: `entropy_298_16`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "entropy_cyclohexane.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "entropy_298_16": {
            "type": "number",
            "units": "cal/(deg mol)"
          }
        },
        "required": [
          "entropy_298_16"
        ]
      },
      "description": "The computed molal entropy of liquid cyclohexane at 298.16 K, in cal/deg/mole."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `entropy_cyclohexane.json`, extracts the value of `entropy_298_16`, and compares it to a hidden reference value derived from the original paper. The reward is 1.0 if your computed entropy falls within an allowed tolerance; otherwise it is 0.0. The tolerance is set to allow for differences in numerical integration methods. The verifier does not see your intermediate steps but relies solely on the final scored artifact. You are expected to implement the full integration chain as described; fabricating the answer without actually doing the computation will likely produce a result outside the tolerance.
