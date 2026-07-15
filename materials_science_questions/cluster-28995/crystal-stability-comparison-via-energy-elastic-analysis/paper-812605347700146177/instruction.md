# Crystal Stability Comparison via Energy/Elastic Analysis

## Problem background
The stability of a crystal structure in sp-bonded metals is determined by the shape of the interatomic pair potential Φ(R). Using a simple Ashcroft empty-core pseudopotential and the Ichimaru-Utsumi dielectric function, one can compute Φ(R) and examine how the force constants at the close-packed nearest-neighbour distance depend on the pseudopotential core radius relative to the electron-density parameter. For elements with valence Z=3, varying the ratio Rc/Rs changes the radial and tangential force constants, which in turn determine the elastic shear moduli of a hypothetical FCC lattice. The task here is to compute these force constants and the resulting elastic moduli for four specific values of Rc/Rs at fixed Rs and Z, and to see under which conditions the FCC structure would be stable or unstable against shear distortions.

## Approach
Implement the Ashcroft empty-core pseudopotential and the Ichimaru-Utsumi dielectric function to compute the pair potential Φ(R). For each prescribed set of parameters (Rs=2.20 au, Z=3, Rc/Rs values), numerically evaluate Φ(R) and its first and second derivatives at the close-packed nearest-neighbour distance Dcp = 1.809 Rs Z^{1/3}. From these derivatives, form the tangential force constant 𝒥 = Φ'(Dcp)/Dcp and the radial force constant ℛ = Φ''(Dcp). Then compute the atomic volume Ω_a and derive the FCC elastic shear moduli C (rhombohedral) and C' (tetragonal) using the nearest-neighbour expressions C = (4Ω_a)^{-1/3}(3𝒥 + ℛ) and C' = (4Ω_a)^{-1/3}(7𝒥/2 + ℛ/2). Execute this pipeline for each of the four target Rc/Rs ratios and write the raw force constants and the moduli to separate JSON files.

## Reproduction target
For the four parameter combinations (Rc/Rs = 0.48, 0.42, 0.36, 0.33) with Rs=2.20 au and Z=3, produce two JSON artifacts: (1) force_constants.json containing the tangential constant J and radial constant R at Dcp for each ratio, and (2) elastic_moduli_groupIII.json containing the corresponding FCC shear moduli C_FCC and C_prime_FCC. All values must be in atomic units (Hartree). The task is complete when both files are written to /app/outputs with the exact keys and fields specified in the output contract.

## Assets

- Ashcroft empty‑core pseudopotential (1966): 10.1016/0031-9163(66)90224-9
- Ichimaru‑Utsumi dielectric function (1981): 10.1103/PhysRevB.24.7385

## Workflow steps

### Step 1: Compute force constants
- Role: scored (load-bearing)
- Action: Implement the Ashcroft empty‑core pseudopotential and the Ichimaru‑Utsumi dielectric function to compute the pair potential Φ(R). For the four parameter sets (Rs=2.20 au, Z=3, Rc/Rs=0.48, 0.42, 0.36, 0.33) compute the first and second derivatives of Φ(R) at R = Dcp = 1.809 * Rs * Z^{1/3} au. Determine the tangential force constant 𝒥 = Φ'(Dcp)/Dcp and radial force constant ℛ = Φ''(Dcp). Write the results to a JSON file.
- Output file: `/app/outputs/force_constants.json`
- Format: json
- Contract: JSON object with keys '0.48', '0.42', '0.36', '0.33'. Each value is an object with fields 'J' (tangential force constant, float, Ha) and 'R' (radial force constant, float, Ha).
- Scoring: scored by hidden verifier

### Step 2: Compute elastic shear moduli
- Role: scored
- Action: From the force constants obtained in step_01, compute the atomic volume Ω_a = (4π/3)*(Rs * Z^{1/3})^3. Evaluate the FCC elastic shear moduli C = (4Ω_a)^{-1/3} * (3𝒥 + ℛ) and C' = (4Ω_a)^{-1/3} * (7𝒥/2 + ℛ/2). Write the results for each Rc/Rs to a JSON file.
- Output file: `/app/outputs/elastic_moduli_groupIII.json`
- Format: json
- Contract: JSON object with keys '0.48', '0.42', '0.36', '0.33'. Each value is an object with fields 'C_FCC' (float, Ha) and 'C_prime_FCC' (float, Ha).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/force_constants.json`
- `/app/outputs/elastic_moduli_groupIII.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### force_constants.json
- path: `/app/outputs/force_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed force constants at the FCC close-packed distance for four Rc/Rs ratios.
- schema:
  - `type`: object
  - `required`: `0.48`, `0.42`, `0.36`, `0.33`
  - `additionalProperties`:
    - `type`: object
    - `required`: `J`, `R`
    - `properties`:
      - `J`:
        - `type`: number
        - `description`: Tangential force constant (Ha)
      - `R`:
        - `type`: number
        - `description`: Radial force constant (Ha)

### elastic_moduli_groupIII.json
- path: `/app/outputs/elastic_moduli_groupIII.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: FCC elastic shear moduli derived from force constants.
- schema:
  - `type`: object
  - `required`: `0.48`, `0.42`, `0.36`, `0.33`
  - `additionalProperties`:
    - `type`: object
    - `required`: `C_FCC`, `C_prime_FCC`
    - `properties`:
      - `C_FCC`:
        - `type`: number
        - `description`: Rhombohedral shear modulus (Ha)
      - `C_prime_FCC`:
        - `type`: number
        - `description`: Tetragonal shear modulus (Ha)

Notes: Values are in atomic units (Hartree). The checker will verify self-consistency between the two artifacts, compare absolute values against a hidden reference, and check the sign pattern of the moduli as described by the structural stability argument.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "force_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "0.48",
          "0.42",
          "0.36",
          "0.33"
        ],
        "additionalProperties": {
          "type": "object",
          "required": [
            "J",
            "R"
          ],
          "properties": {
            "J": {
              "type": "number",
              "description": "Tangential force constant (Ha)"
            },
            "R": {
              "type": "number",
              "description": "Radial force constant (Ha)"
            }
          }
        }
      },
      "description": "Computed force constants at the FCC close-packed distance for four Rc/Rs ratios."
    },
    {
      "file": "elastic_moduli_groupIII.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "0.48",
          "0.42",
          "0.36",
          "0.33"
        ],
        "additionalProperties": {
          "type": "object",
          "required": [
            "C_FCC",
            "C_prime_FCC"
          ],
          "properties": {
            "C_FCC": {
              "type": "number",
              "description": "Rhombohedral shear modulus (Ha)"
            },
            "C_prime_FCC": {
              "type": "number",
              "description": "Tetragonal shear modulus (Ha)"
            }
          }
        }
      },
      "description": "FCC elastic shear moduli derived from force constants."
    }
  ],
  "notes": "Values are in atomic units (Hartree). The checker will verify self-consistency between the two artifacts, compare absolute values against a hidden reference, and check the sign pattern of the moduli as described by the structural stability argument."
}
```

## How you are scored
A hidden verifier loads your force_constants.json and elastic_moduli_groupIII.json. It checks that all required keys and fields are present, recomputes the elastic moduli from your submitted force constants to verify self-consistency, and then compares your computed force constants and moduli against hidden reference values (obtained from a trustworthy re‑implementation of the same pair‑potential model) within a generous tolerance. The verifier further examines whether the sequence of moduli values behaves as predicted by the physical model, without penalising minor numerical differences. The final reward is a weighted combination of the force‑constant agreement and the moduli evaluation; each stage carries a substantial share. Simply reporting approximate numbers is not sufficient – the pipeline must be executed correctly to earn the majority of the points.
