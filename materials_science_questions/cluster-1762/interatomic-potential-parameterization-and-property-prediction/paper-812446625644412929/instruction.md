# Point-Charge Model Calculation of Anisotropic Lattice Expansion in Li4SiO4

## Problem background
The work investigates the origin of enhanced Li+ ionic conductivity in B3+-substituted Li4SiO4 solid solutions. The paper proposes that the anisotropic expansion of the monoclinic Li4SiO4 unit cell upon B3+ doping is caused by repulsive Coulomb forces from the additional interstitial Li+ ions. A simple point-charge model calculation sums these forces over all ion pairs and derives relative expansion rates along the a, b, c crystallographic axes. Reproducing this model calculation is the goal of this task — compute the anisotropic expansion ratios from the crystal structure under the assumption of point charges.

## Approach
We use the crystal structure of Li4SiO4 reported by Tranqui et al. (1979), which is monoclinic, space group P2_1/m, Z=14, and contains 42 Li sites — 19 ordered and 23 available interstitial sites. For the point-charge calculation (model A), all 23 interstitial sites are occupied by Li+ ions. Assign point charges: Li +1, O -2, Si +4. Compute the total Coulomb force contributions F = Σ q_i q_j / r^2 for all ion pairs (Li+–Li+, Li+–O2–, Li+–Si4+). Project the net force vector onto the a, b, c crystallographic axes to obtain the components F_a, F_b, F_c. The relative expansion rates are taken as proportional to the absolute values of these force components, i.e., Δa ∝ |F_a|, Δb ∝ |F_b|, Δc ∝ |F_c|. Finally, normalize the three numbers so that Δb = 1.0 exactly. The result is written to expansion_ratios.json.

## Reproduction target
Using the Li4SiO4 crystal structure (monoclinic, with all 42 Li sites, interstitial sites occupied per model A) and a point-charge model as described, compute the relative lattice expansion rates Δa, Δb, Δc. Normalize the ratios so that Δb = 1.0. Output the result in the file expansion_ratios.json with fields delta_a, delta_b, delta_c, and an ordered ratio_vector [delta_a, 1.0, delta_c].

## Assets

- Li4SiO4 crystal structure (Tranqui et al., 1979): 10.1107/S0567740879009057

## Workflow steps

### Step 1: Compute Coulomb forces from the Li4SiO4 crystal structure with interstitial occupancy
- Role: process
- Action: Obtain the crystal structure of Li4SiO4 (monoclinic, all 42 Li sites with the 23 interstitial sites occupied as in model A). Assign point charges: Li +1, O -2, Si +4. Compute the total Coulomb force contributions F = Σ q_i q_j / r^2 over all ion pairs (Li+–Li+, Li+–O2−, Li+–Si4+), then project the net force onto the a, b, c crystallographic axes to obtain the force components F_a, F_b, F_c.
- Evidence: `/app/outputs/forces.json`

### Step 2: Derive relative expansion ratios
- Role: scored (load-bearing)
- Action: Using the computed force components, determine the relative lattice expansion rates Δa ∝ |F_a|, Δb ∝ |F_b|, Δc ∝ |F_c|. Normalize the ratios so that Δb = 1.0 exactly. Write the result to expansion_ratios.json.
- Output file: `/app/outputs/expansion_ratios.json`
- Format: json
- Contract: {"delta_a": float,"delta_b": 1.0,"delta_c": float,"ratio_vector": [float, 1.0, float]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/expansion_ratios.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### expansion_ratios.json
- path: `/app/outputs/expansion_ratios.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Point-charge Coulomb model anisotropic expansion ratios; delta_b is exactly 1.0 by normalization, and the checker recomputes the ratios from the same crystal structure for comparison with a tolerance.
- schema:
  - `type`: object
  - `required`: `delta_a`, `delta_b`, `delta_c`, `ratio_vector`
  - `properties`:
    - `delta_a`:
      - `type`: number
      - `description`: Relative expansion along a-axis
    - `delta_b`:
      - `type`: number
      - `description`: Relative expansion along b-axis, normalized to 1.0
    - `delta_c`:
      - `type`: number
      - `description`: Relative expansion along c-axis
    - `ratio_vector`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
      - `description`: Ordered vector [delta_a, delta_b, delta_c]
  - `description`: Relative lattice expansion ratios derived from point-charge model forces.

Notes: The task reproduces only the separable point-charge model subresult. The remaining experimental conductivity analyses and structural interpretations are omitted because the necessary raw data and sample-specific details are not publicly available.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "expansion_ratios.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "delta_a",
          "delta_b",
          "delta_c",
          "ratio_vector"
        ],
        "properties": {
          "delta_a": {
            "type": "number",
            "description": "Relative expansion along a-axis"
          },
          "delta_b": {
            "type": "number",
            "description": "Relative expansion along b-axis, normalized to 1.0"
          },
          "delta_c": {
            "type": "number",
            "description": "Relative expansion along c-axis"
          },
          "ratio_vector": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3,
            "description": "Ordered vector [delta_a, delta_b, delta_c]"
          }
        },
        "description": "Relative lattice expansion ratios derived from point-charge model forces."
      },
      "description": "Point-charge Coulomb model anisotropic expansion ratios; delta_b is exactly 1.0 by normalization, and the checker recomputes the ratios from the same crystal structure for comparison with a tolerance."
    }
  ],
  "notes": "The task reproduces only the separable point-charge model subresult. The remaining experimental conductivity analyses and structural interpretations are omitted because the necessary raw data and sample-specific details are not publicly available."
}
```

## How you are scored
Your submitted artifact expansion_ratios.json is scored by a hidden verifier. The verifier independently recomputes the same point-charge model from the same crystal structure (the CIF is bundled in the test environment). It compares your submitted ratios (delta_a, delta_c) to its own recomputed values and checks that delta_b is exactly 1.0. The match is judged within a tolerance; the exact tolerance is hidden but is large enough to absorb small implementation differences while still requiring a correct recomputation. The verifier produces a reward in [0, 1] based on the agreement. Note that merely reproducing the paper’s reported numbers will not work if they are not consistent with the verifier’s own independent calculation, so you must genuinely implement the point-charge model.
