# Interfacial Tension of Hard Spheres with Short-Ranged Attraction via Cell Theory

## Problem background
In the low-temperature limit, a system of hard spheres interacting via a short-range square-well attraction (range δ ≪ 1) separates into a near-close-packed solid coexisting with an extremely dilute gas. Understanding the interfacial tension between these phases is important for nucleation theory and may explain why globular proteins crystallize only in a narrow range of conditions. Using a simple cell theory, analytic expressions can be derived for the free energy per particle in the bulk solid and in the outermost solid layer, yielding predictions for the interfacial tensions of the (111), (110), and (100) surfaces of an fcc lattice. A key claim is that the ratio of the interfacial tension to a characteristic temperature (T_coll) becomes very large as δ → 0. This task will recompute those interfacial tensions and examine how this ratio behaves as the attraction range is varied.

## Approach
The calculation is based on a cell theory, where the free energy per particle in the bulk solid, a_s, is estimated from the logarithm of the available volume. With σ=1 and ε=1, and a short attraction range δ, the formulas simplify. For a given δ, the bulk solid free energy per particle (in units of T) is a_s/T = -3 ln δ - 6ε/T. A particle in the outermost layer loses z_m nearest neighbours (z_m=3 for (111), 5 for (110), 4 for (100)), so its free energy per particle relative to the bulk is a_i - a_s = z_m ε / 2. The interfacial tension γ is obtained by dividing this excess free energy by the area per sphere for that surface: A(111)=(√3/2)σ², A(110)=√2 σ², A(100)=σ². The characteristic temperature T_coll is defined as T_coll/ε = 2 / ln(1/δ). Using these formulas, you will compute γ for the three surfaces and, for the (111) surface, the dimensionless ratio γ_111 / T_coll for a sequence of decreasing δ (0.1, 0.01, 0.001).

## Reproduction target
Produce two JSON artifacts:
- intermediate.json: store the computed free energies (bulk and surface) for the given δ values.
- surface_tensions.json: the final scored output, containing the interfacial tensions γ for the (111), (110), and (100) planes (in units of εσ⁻²), and an array gamma_over_T_coll with entries giving the ratio γ_111/T_coll for each δ in the set [0.1, 0.01, 0.001]. The output must follow the schema specified in the output contract.

## Assets

- Python (numpy): https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Derive free energy difference per outermost particle
- Role: process
- Action: Implement the cell-theory formulas to compute the bulk solid free energy per particle a_s/T = -3 ln δ - 6ε/T, the surface free energy per particle for the (111), (110) and (100) planes using the number of missing neighbors z_m=3,5,4 respectively, and the area per sphere for each plane: (√3/2)σ², √2 σ², σ². Use σ=1, ε=1, and input δ values (0.1, 0.01, 0.001) for later use. Output the intermediate quantities (free energies) to intermediate.json.
- Evidence: `/app/outputs/intermediate.json`

### Step 2: Compute interfacial tensions and divergence ratio
- Role: scored (load-bearing)
- Action: From the free energy differences, compute interfacial tension γ = (a_i - a_s) / (Area per sphere) for each plane: γ_111, γ_110, γ_100. Compute T_coll = 2ε / ln(1/δ). Compute the ratio γ_111 / T_coll for δ = 0.1, 0.01, 0.001. Write all results to surface_tensions.json.
- Output file: `/app/outputs/surface_tensions.json`
- Format: json
- Contract: Object with keys '111', '110', '100' (floating-point tensions) and 'gamma_over_T_coll' (array of objects, each with 'delta' and 'ratio').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_tensions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_tensions.json
- path: `/app/outputs/surface_tensions.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed interfacial tensions for the three low-index FCC surfaces and the ratio of (111) tension to T_coll for a sequence of δ values, verifying the divergence trend.
- schema:
  - `type`: object
  - `required`: `111`, `110`, `100`, `gamma_over_T_coll`
  - `properties`:
    - `111`:
      - `type`: number
      - `description`: Interfacial tension for (111) plane in units of εσ⁻²
    - `110`:
      - `type`: number
      - `description`: Interfacial tension for (110) plane in units of εσ⁻²
    - `100`:
      - `type`: number
      - `description`: Interfacial tension for (100) plane in units of εσ⁻²
    - `gamma_over_T_coll`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `delta`, `ratio`
        - `properties`:
          - `delta`:
            - `type`: number
            - `description`: Range parameter δ
          - `ratio`:
            - `type`: number
            - `description`: γ₁₁₁ / T_coll, dimensionless

Notes: Agent must implement the analytic formulas as described in the approach. The checker will recompute expected values with a tolerance and verify that the ratio strictly increases as δ decreases.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_tensions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "111",
          "110",
          "100",
          "gamma_over_T_coll"
        ],
        "properties": {
          "111": {
            "type": "number",
            "description": "Interfacial tension for (111) plane in units of εσ⁻²"
          },
          "110": {
            "type": "number",
            "description": "Interfacial tension for (110) plane in units of εσ⁻²"
          },
          "100": {
            "type": "number",
            "description": "Interfacial tension for (100) plane in units of εσ⁻²"
          },
          "gamma_over_T_coll": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "delta",
                "ratio"
              ],
              "properties": {
                "delta": {
                  "type": "number",
                  "description": "Range parameter δ"
                },
                "ratio": {
                  "type": "number",
                  "description": "γ₁₁₁ / T_coll, dimensionless"
                }
              }
            }
          }
        }
      },
      "description": "Computed interfacial tensions for the three low-index FCC surfaces and the ratio of (111) tension to T_coll for a sequence of δ values, verifying the divergence trend."
    }
  ],
  "notes": "Agent must implement the analytic formulas as described in the approach. The checker will recompute expected values with a tolerance and verify that the ratio strictly increases as δ decreases."
}
```

## How you are scored
A hidden verifier will independently recompute the expected interfacial tensions and the ratio values from the same cell-theory formulas. It will compare your submitted surface_tensions.json values using relative tolerances. It will also examine the trend of the ratio across the three δ values. Your total reward is a combination of scoring on the three tension values and the ratio array. Simply reporting numbers without genuine computation will not succeed because the verifier checks consistency and correctness.
