# First-principles elastic properties and Vickers hardness of vanadium carbides

## Problem background
Vanadium carbides (VCs) serve as reinforcing phases in steels and coatings, significantly improving wear resistance and mechanical properties. However, the mechanical properties of sub-stoichiometric vanadium carbides, such as V2C, V4C3, V6C5, and V8C7, are not well characterized. First-principles density functional theory (DFT) calculations can provide the single-crystal elastic constants and derived polycrystalline elastic moduli and hardness, revealing the effect of carbon content on the mechanical behavior of the V–C system. This task aims to compute those properties for a series of vanadium carbide phases, allowing a systematic comparison.

## Approach
The computational workflow uses plane-wave DFT with the GGA-PBE exchange-correlation functional to perform geometry optimization and then compute the single-crystal elastic constants C_ij for each phase via the stress-strain method. From the C_ij, polycrystalline bulk modulus B and shear modulus G are obtained using Voigt-Reuss-Hill (VRH) averaging. Young's modulus E is then computed as E = 9BG/(3B+G), Poisson's ratio ν = (3B−2G)/(2(3B+G)), and Vickers hardness H_v is estimated via Chen's model: H_v = 2·( (G/B)^2 · G )^{0.583} − 3. The calculations are performed on the following vanadium carbide phases, using their reported experimental space groups and lattice constants: pure V (Im‑3m, a=3.04 Å), V2C (Pbcn, a=4.577 Å, b=5.743 Å, c=5.037 Å), V4C3 (R‑3m, a=2.917 Å, c=27.83 Å), P31‑V6C5 (P31, a=5.09 Å, c=14.40 Å), V8C7 (P4_332, a=8.3334 Å), and cubic VC (Fm‑3m, a=4.158 Å).

## Reproduction target
Produce a JSON file properties.json containing the computed independent elastic constants (C_ij in Voigt notation), polycrystalline bulk modulus B, shear modulus G, Young’s modulus E, Poisson’s ratio ν, and Vickers hardness H_v for all six phases: V, V2C, V4C3, P31-V6C5, V8C7, and c-VC. The file must be structured as described in the output contract. The computed shear modulus G and Young’s modulus E should exhibit a monotonic increase with carbon content across the series V → V2C → V4C3 → V6C5 → V8C7 → VC.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE precision): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Construct input structures for DFT calculations of all vanadium carbide phases using literature space groups and lattice constants: pure V (Im-3m, a=3.04 Å); V2C (Pbcn, a=4.577 Å, b=5.743 Å, c=5.037 Å); V4C3 (R-3m, a=2.917 Å, c=27.83 Å); P31-V6C5 (P31, a=5.09 Å, c=14.40 Å); V8C7 (P4_332, a=8.3334 Å); cubic VC (Fm-3m, a=4.158 Å). Generate atomic positions accordingly. These structures serve as starting points for DFT relaxation.
- Evidence: none

### Step 2: DFT elastic constants calculation
- Role: process
- Action: For each phase (V, V2C, V4C3, P31-V6C5, V8C7, c-VC), perform DFT geometry optimization using Quantum ESPRESSO with the GGA-PBE functional and SSSP pseudopotentials. Then compute the single-crystal elastic constants Cij via the stress-strain method. Store the resulting independent Cij (Voigt notation) for each phase in a structured file elastic_constants.json.
- Evidence: `/app/outputs/elastic_constants.json`

### Step 3: Derive polycrystalline elastic moduli and Vickers hardness
- Role: scored (load-bearing)
- Action: Read the elastic constants from elastic_constants.json. For each phase, apply Voigt-Reuss-Hill averaging to compute polycrystalline bulk modulus B and shear modulus G. Then compute Young's modulus E = 9BG/(3B+G), Poisson's ratio ν = (3B-2G)/(2(3B+G)), and Vickers hardness Hv = 2((G/B)^2 * G)^{0.583} − 3 (Chen's model). Write all results (Cij, B, G, E, ν, Hv) for all phases into properties.json.
- Output file: `/app/outputs/properties.json`
- Format: json
- Contract: A JSON object with a top-level key 'phases' that is an array. Each element is an object with keys: 'phase_name' (string), 'space_group' (string), 'Cij' (list of floats, all independent elastic constants in Voigt order according to crystal symmetry), 'B' (float, GPa), 'G' (float, GPa), 'E' (float, GPa), 'v' (float), 'Hv' (float, GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### properties.json
- path: `/app/outputs/properties.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Aggregated elastic properties and Vickers hardness for all vanadium carbide phases, computed from DFT elastic constants via Voigt-Reuss-Hill averaging and Chen's hardness model.
- schema:
  - `type`: object
  - `properties`:
    - `phases`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `phase_name`:
            - `type`: string
          - `space_group`:
            - `type`: string
          - `Cij`:
            - `type`: array
            - `items`:
              - `type`: number
          - `B`:
            - `type`: number
            - `unit`: GPa
          - `G`:
            - `type`: number
            - `unit`: GPa
          - `E`:
            - `type`: number
            - `unit`: GPa
          - `v`:
            - `type`: number
          - `Hv`:
            - `type`: number
            - `unit`: GPa
        - `required`: `phase_name`, `space_group`, `Cij`, `B`, `G`, `E`, `v`, `Hv`
  - `required`: `phases`

Notes: The checker recomputes B and G from the submitted Cij using Voigt-Reuss-Hill averaging, then derives E, ν, Hv and compares these to reference values with tolerances. A structural trend check verifies that E and G increase monotonically with carbon content across the phases.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "properties": {
          "phases": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "phase_name": {
                  "type": "string"
                },
                "space_group": {
                  "type": "string"
                },
                "Cij": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                },
                "B": {
                  "type": "number",
                  "unit": "GPa"
                },
                "G": {
                  "type": "number",
                  "unit": "GPa"
                },
                "E": {
                  "type": "number",
                  "unit": "GPa"
                },
                "v": {
                  "type": "number"
                },
                "Hv": {
                  "type": "number",
                  "unit": "GPa"
                }
              },
              "required": [
                "phase_name",
                "space_group",
                "Cij",
                "B",
                "G",
                "E",
                "v",
                "Hv"
              ]
            }
          }
        },
        "required": [
          "phases"
        ]
      },
      "description": "Aggregated elastic properties and Vickers hardness for all vanadium carbide phases, computed from DFT elastic constants via Voigt-Reuss-Hill averaging and Chen's hardness model."
    }
  ],
  "notes": "The checker recomputes B and G from the submitted Cij using Voigt-Reuss-Hill averaging, then derives E, ν, Hv and compares these to reference values with tolerances. A structural trend check verifies that E and G increase monotonically with carbon content across the phases."
}
```

## How you are scored
The submitted properties.json is evaluated by a hidden verifier that parses the file and, for each phase, recomputes the polycrystalline moduli B and G from the reported C_ij using Voigt-Reuss-Hill averaging. It then derives E, ν, and H_v using the same formulas, and compares these values to reference results with appropriate tolerances. Additionally, the verifier checks that the shear modulus G and Young’s modulus E increase monotonically with carbon content across the listed order of phases. The final reward is a weighted combination of the accuracy of the derived quantities and the monotonicity check. Reporting the final numbers alone without a valid elastic-constants path will not satisfy the scoring.
