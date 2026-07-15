# Collision-Induced Transition Moments in O₂ + H₂ / C₂H₄ Complexes via Semiempirical MINDO/3 with Configuration Interaction and Spin‑Orbit Coupling

## Problem background
The radiative transitions b¹Σ⁺ → a¹Δ and a¹Δ → X³Σ⁻ in molecular oxygen are forbidden in isolation but can be collision‑induced by surrounding molecules. When a mixture of collision partners is present, their combined influence on the transition moments is not simply additive—cooperative effects can enhance or weaken the moments depending on the geometry. Understanding this cooperative interplay is important for modelling collision‑induced emission in oxygen‑containing gas mixtures. The present task investigates how the simultaneous presence of H₂ and ethylene (C₂H₄) affects the electric‑dipole transition moments of O₂ in a ternary collision complex, and whether the cooperative effect is stronger or weaker than the influence of each partner alone.

## Approach
We use the semiempirical MINDO/3 method with configuration interaction including single and double excitations (CI(SD)) and spin‑orbit coupling treated by first‑order perturbation theory. Collision complex geometries are built by fixing the O₂–C₂H₄ distance at 3.8 Å and varying the H₂ approach distance R over the set {5.0, 4.8, 4.4, 4.0, 3.8, 3.6, 3.4, 3.2, 3.0, 2.8, 2.6} Å. Two ternary arrangements are studied: model I places H₂ symmetrically above the O₂–C₂H₄ bond centre; model II places H₂ above O₂, orthogonal to the C₂H₄ orientation. For each geometry a MINDO/3 single‑point calculation yields the ground‑state wavefunction including CI and spin‑orbit mixing. The resulting electric‑dipole transition moments M_{b‑a} and M_{a‑X} are extracted. For ternary complexes the b‑a moment is decomposed into an SCF (orbital‑dipole) contribution and a CI contribution, following M_{b‑a}^{tot} = M_{b‑a}^{SCF} + M_{b‑a}^{CI}. The corresponding binary complexes O₂ + H₂ and O₂ + C₂H₄ are computed at the same R values to provide references against which the cooperative effect can be compared.

## Reproduction target
Produce a JSON file `computed_transition_moments.json` containing the electric‑dipole transition moments for the b–a and a–X transitions of O₂ in the four collision systems: O₂ + H₂, O₂ + C₂H₄, and the two ternary models O₂ + C₂H₄ + H₂ (model I and model II). For each system and each R distance in the set listed above, report the total moments M_{b‑a} and M_{a‑X} (for binary systems) or the decomposed b‑a moment with its SCF and CI components along with the total M_{b‑a}^{tot} and M_{a‑X} (for ternary systems). All values must be expressed in units of 10⁻⁴ eÅ and must follow the JSON schema specified in the output contract. The submitted artifact will be checked for internal self‑consistency of the decomposition and for the structural trends that indicate cooperative enhancement or suppression.

## Assets

- MOPAC: https://github.com/openmopac/mopac

## Workflow steps

### Step 1: Generate collision complex geometries
- Role: process
- Action: Construct Cartesian coordinates for the binary complexes O₂+H₂ and O₂+C₂H₄, and for the ternary complex O₂+C₂H₄+H₂ in model I and model II. Fix the O₂–C₂H₄ distance at 3.8 Å. Vary the H₂ approach distance R (distance between H₂ and the O₂+C₂H₄ subsystem) over the set {5.0, 4.8, 4.4, 4.0, 3.8, 3.6, 3.4, 3.2, 3.0, 2.8, 2.6} Å. Use MINDO/3‑optimised isolated molecule geometries as building blocks. Model I places H₂ above the centre of the O₂–C₂H₄ bond with equal distances to O₂ and C₂H₄; model II places H₂ above the O₂ molecule, interacting primarily with the π_g,z orbital while C₂H₄ interacts with π_g,x.
- Evidence: `/app/outputs/geometries.json`

### Step 2: Compute transition moments and output table
- Role: scored (load-bearing)
- Action: For every geometry generated in the previous step, run a MINDO/3 single‑point calculation with configuration interaction including single and double excitations (CI(SD)) and spin‑orbit coupling treated by perturbation theory. From the resulting wavefunctions, extract the electric‑dipole transition moments M_{b‑a} and M_{a‑X} for the binary complexes, and for the ternary complexes additionally decompose M_{b‑a} into its SCF (orbital‑dipole) contribution M_{b‑a}^{SCF}, its CI contribution M_{b‑a}^{CI}, and the total M_{b‑a}^{tot}. Assemble all results into a single JSON file following the specified schema. All moments are reported in units of 10⁻⁴ eÅ.
- Output file: `/app/outputs/computed_transition_moments.json`
- Format: json
- Contract: A JSON object with key 'systems', whose value is an array of system objects. Each system object has 'name' (string) and 'R_values' (array). Each element of R_values is an object with 'R' (number, Å) and the following fields: for binary systems 'O2+H2' and 'O2+C2H4' include 'M_ba' (number), 'M_aX' (number); for ternary systems 'O2+C2H4+H2_model_I' and 'O2+C2H4+H2_model_II' include 'M_ba_SCF' (number), 'M_ba_CI' (number), 'M_ba_tot' (number), and 'M_aX' (number). All moment values are in 10⁻⁴ eÅ.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_transition_moments.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_transition_moments.json
- path: `/app/outputs/computed_transition_moments.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: This artifact contains the collision‑induced electric‑dipole transition moments for the b–a and a–X transitions of O₂ in binary (O₂+H₂, O₂+C₂H₄) and ternary (O₂+C₂H₄+H₂ model I and II) complexes. For ternary systems it also provides the SCF and CI components of the b–a moment. The checker recomputes self‑consistency (M_ba_tot vs M_ba_SCF+M_ba_CI) and verifies structural trends (enhancement for model I, suppression for model II) without requiring absolute‑value agreement with the reference literature.
- schema:
  - `type`: object
  - `required`: `systems`
  - `properties`:
    - `systems`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `name`, `R_values`
        - `properties`:
          - `name`:
            - `type`: string
            - `enum`: `O2+H2`, `O2+C2H4`, `O2+C2H4+H2_model_I`, `O2+C2H4+H2_model_II`
          - `R_values`:
            - `type`: array
            - `items`:
              - `type`: object
              - `required`: `R`
              - `properties`:
                - `R`:
                  - `type`: number
                  - `unit`: angstrom
                - `M_ba`:
                  - `type`: number
                  - `unit`: 10^-4 eÅ
                - `M_aX`:
                  - `type`: number
                  - `unit`: 10^-4 eÅ
                - `M_ba_SCF`:
                  - `type`: number
                  - `unit`: 10^-4 eÅ
                - `M_ba_CI`:
                  - `type`: number
                  - `unit`: 10^-4 eÅ
                - `M_ba_tot`:
                  - `type`: number
                  - `unit`: 10^-4 eÅ

Notes: Only transition moments (Table 2 equivalents) are scored; molecular‑orbital coefficient analysis (Table 1) is not required. The agent must use a MINDO/3 implementation with CI(SD) and spin‑orbit coupling, e.g. MOPAC.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_transition_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "systems"
        ],
        "properties": {
          "systems": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "name",
                "R_values"
              ],
              "properties": {
                "name": {
                  "type": "string",
                  "enum": [
                    "O2+H2",
                    "O2+C2H4",
                    "O2+C2H4+H2_model_I",
                    "O2+C2H4+H2_model_II"
                  ]
                },
                "R_values": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": [
                      "R"
                    ],
                    "properties": {
                      "R": {
                        "type": "number",
                        "unit": "angstrom"
                      },
                      "M_ba": {
                        "type": "number",
                        "unit": "10^-4 eÅ"
                      },
                      "M_aX": {
                        "type": "number",
                        "unit": "10^-4 eÅ"
                      },
                      "M_ba_SCF": {
                        "type": "number",
                        "unit": "10^-4 eÅ"
                      },
                      "M_ba_CI": {
                        "type": "number",
                        "unit": "10^-4 eÅ"
                      },
                      "M_ba_tot": {
                        "type": "number",
                        "unit": "10^-4 eÅ"
                      }
                    }
                  }
                }
              }
            }
          }
        }
      },
      "description": "This artifact contains the collision‑induced electric‑dipole transition moments for the b–a and a–X transitions of O₂ in binary (O₂+H₂, O₂+C₂H₄) and ternary (O₂+C₂H₄+H₂ model I and II) complexes. For ternary systems it also provides the SCF and CI components of the b–a moment. The checker recomputes self‑consistency (M_ba_tot vs M_ba_SCF+M_ba_CI) and verifies structural trends (enhancement for model I, suppression for model II) without requiring absolute‑value agreement with the reference literature."
    }
  ],
  "notes": "Only transition moments (Table 2 equivalents) are scored; molecular‑orbital coefficient analysis (Table 1) is not required. The agent must use a MINDO/3 implementation with CI(SD) and spin‑orbit coupling, e.g. MOPAC."
}
```

## How you are scored
The hidden verifier evaluates your `computed_transition_moments.json` against two criteria:

1. **Self‑consistency of the decomposed b‑a moment:** For every ternary data point, the verifier recomputes the relative difference between M_{b‑a}^{tot} and (M_{b‑a}^{SCF} + M_{b‑a}^{CI}) and rewards values that satisfy a tight consistency tolerance (at most 1% deviation).

2. **Structural trends of the cooperative influence:** The verifier checks that one ternary model exhibits **enhancement** (its b‑a moment is larger than the corresponding binary moments) and the other ternary model exhibits **suppression** (its b‑a moment is substantially lower) at selected distances. The specific distances, which model acts as enhancer/suppressor, and the numerical margins are hidden and derived from the paper’s published results and are not disclosed.

The final reward (a float between 0 and 1) combines the self‑consistency score and the trend‑compliance score, with the largest weight on correctly replicating the structural trends. Merely providing a syntactically valid JSON is not sufficient; the computed moments must be physically reasonable and consistent with the MINDO/3 method and the specified collision geometries.
