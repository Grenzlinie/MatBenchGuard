# First-principles electron-phonon coupling and superconducting Tc for MgB2 and NbB2

## Problem background
Understanding electron‑phonon coupling in superconducting materials is essential for explaining their transition temperatures. MgB₂ and NbB₂ are both AlB₂‑type diborides, but they exhibit very different superconducting properties. The average electron‑phonon coupling constant λ and the shape of the Eliashberg function α²F(ω) are key quantities that determine the superconducting transition temperature Tc within isotropic Eliashberg theory. This task requires you to compute these quantities from first‑principles and to estimate Tc for both materials, thereby illuminating the origin of their different superconducting behaviour.

## Approach
Perform density‑functional theory (DFT) and density‑functional perturbation theory (DFPT) calculations using an open‑source plane‑wave code (Quantum ESPRESSO). From the self‑consistent electronic structure, compute phonons and the electron‑phonon matrix elements on a grid of phonon wave‑vectors. Post‑process these to obtain the isotropic Eliashberg function α²F(ω) and the average electron‑phonon coupling constant λ. Use the resulting α²F(ω) to solve numerically the imaginary‑axis isotropic Eliashberg gap equation for a range of Coulomb pseudopotential μ* values. Extract the superconducting transition temperature Tc as the temperature where the gap vanishes. Compare the results for MgB₂ and NbB₂ to assess which material is more strongly coupled and has a higher Tc.

## Reproduction target
Produce two JSON artifacts:

- `lambda_values.json`: the average electron‑phonon coupling constant λ for MgB₂ and NbB₂.
- `tc_values.json`: the superconducting transition temperature Tc for both materials at least at μ* = 0.1; optionally report Tc at additional μ* values.

The computed λ and Tc must be internally consistent: the relative ordering of λ between the two materials and the relative ordering of Tc (including its trend as μ* increases) must follow from the physics of the system and from the computed Eliashberg functions.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- SSSP efficiency pseudopotential library: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: DFT and DFPT calculations
- Role: process
- Action: Run Quantum ESPRESSO scf, phonon (ph.x) and electron-phonon coupling (lambda.x or equivalent) for MgB2 and NbB2 using the reported lattice constants (a=5.76 au, c=6.59 au for MgB2; a=5.81 au, c=6.10 au for NbB2). Produce dynamical matrices and electron-phonon matrix elements needed for post-processing.
- Evidence: none

### Step 2: Average electron-phonon coupling λ
- Role: scored (load-bearing)
- Action: From the DFPT output compute the isotropic Eliashberg function α²F(ω) and the average electron-phonon coupling constant λ for MgB2 and NbB2. Write the results to lambda_values.json.
- Output file: `/app/outputs/lambda_values.json`
- Format: json
- Contract: {"type": "array", "items": {"type": "object", "required": ["material", "lambda"], "properties": {"material": {"type": "string", "enum": ["MgB2", "NbB2"]}, "lambda": {"type": "number"}}}}
- Scoring: scored by hidden verifier

### Step 3: Solve isotropic Eliashberg equation
- Role: process
- Action: Using the computed α²F(ω) for each material, solve the isotropic Eliashberg gap equation numerically for a range of μ* values (e.g., 0.10–0.20) to obtain Tc. This step produces the Tc vs μ* curves.
- Evidence: none

### Step 4: Superconducting transition temperatures Tc
- Role: scored (load-bearing)
- Action: Extract the Tc values at μ*=0.10 (and optionally other μ*) for MgB2 and NbB2. Write the results to tc_values.json.
- Output file: `/app/outputs/tc_values.json`
- Format: json
- Contract: {"type": "array", "items": {"type": "object", "required": ["material", "mu_star", "Tc"], "properties": {"material": {"type": "string", "enum": ["MgB2", "NbB2"]}, "mu_star": {"type": "number"}, "Tc": {"type": "number", "units": "K"}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lambda_values.json`
- `/app/outputs/tc_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lambda_values.json
- path: `/app/outputs/lambda_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Average electron-phonon coupling constant λ for MgB2 and NbB2. Each entry must have material and the λ value.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `material`, `lambda`
    - `properties`:
      - `material`:
        - `type`: string
        - `enum`: `MgB2`, `NbB2`
      - `lambda`:
        - `type`: number

### tc_values.json
- path: `/app/outputs/tc_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Superconducting transition temperature Tc for MgB2 and NbB2 at one or more μ* values. Each entry must have material, μ*, and Tc in Kelvin.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `material`, `mu_star`, `Tc`
    - `properties`:
      - `material`:
        - `type`: string
        - `enum`: `MgB2`, `NbB2`
      - `mu_star`:
        - `type`: number
      - `Tc`:
        - `type`: number
        - `units`: K

Notes: The checker compares λ and Tc to paper-reported values with appropriate tolerances and also verifies ordering (MgB2 λ > NbB2 λ, MgB2 Tc > NbB2 Tc).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lambda_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "material",
            "lambda"
          ],
          "properties": {
            "material": {
              "type": "string",
              "enum": [
                "MgB2",
                "NbB2"
              ]
            },
            "lambda": {
              "type": "number"
            }
          }
        }
      },
      "description": "Average electron-phonon coupling constant λ for MgB2 and NbB2. Each entry must have material and the λ value."
    },
    {
      "file": "tc_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "material",
            "mu_star",
            "Tc"
          ],
          "properties": {
            "material": {
              "type": "string",
              "enum": [
                "MgB2",
                "NbB2"
              ]
            },
            "mu_star": {
              "type": "number"
            },
            "Tc": {
              "type": "number",
              "units": "K"
            }
          }
        }
      },
      "description": "Superconducting transition temperature Tc for MgB2 and NbB2 at one or more μ* values. Each entry must have material, μ*, and Tc in Kelvin."
    }
  ],
  "notes": "The checker compares λ and Tc to paper-reported values with appropriate tolerances and also verifies ordering (MgB2 λ > NbB2 λ, MgB2 Tc > NbB2 Tc)."
}
```

## How you are scored
A hidden automated verifier reads your `lambda_values.json` and `tc_values.json`. It compares your computed λ and Tc values to reference data derived from the original research, using appropriate numerical tolerances to allow for legitimate differences in computational setup (pseudopotentials, exchange‑correlation functional, k‑point grids). The verifier also checks that the relative trends between the two materials and across μ* values are physically consistent. The final score is a weighted combination of the checks on λ and Tc, with the main headline quantities carrying the largest weight.
