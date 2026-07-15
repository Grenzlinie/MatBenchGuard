# Third-order elastic constants and thermal properties of hcp cobalt from central-force model

## Problem background
Cobalt in its hexagonal close‑packed (hcp) form is a technologically important transition metal with a near‑ideal c/a ratio. Knowledge of its third‑order elastic (TOE) constants and derived thermal properties – the volume Grüneisen gamma, Anderson‑Grüneisen parameter, second Grüneisen constant, and temperature‑dependent bulk modulus – is central to understanding anharmonic lattice effects and thermal expansion. This task requires computing these quantities from a nearest‑neighbour central‑force model that uses experimentally measured second‑order elastic constants as input, providing a self‑contained theoretical evaluation of the material's anharmonic behaviour.

## Approach
The work employs a central‑force model for an ideal hcp lattice where the interatomic potential is a two‑term inverse‑power form, φ(r) = −a/rᵐ + b/rⁿ. The model expresses the ten independent TOE constants in terms of two auxiliary parameters k₂, k₃ and the nearest‑neighbour distance D. The procedure first determines the exponent sum n+m from the published high‑temperature Grüneisen gamma of cobalt, then evaluates the auxiliary constant η from the experimental second‑order elastic constants C₁₁ and C₃₃ at 4 K and 298 K. From η, M (atomic mass) and D one calculates k₂ and k₃. Using the model's analytic expressions for an hcp lattice, the ten TOE constants at both temperatures are evaluated. Subsequently, a lattice dynamics calculation is performed: a dynamical matrix based on the central‑force potential is diagonalised at a grid of wave vectors in the irreducible part of the Brillouin zone, yielding phonon frequencies and mode Grüneisen parameters. By averaging over the obtained frequency distribution with Einstein specific‑heat weights, the temperature dependence of the volume Grüneisen gamma is obtained, and its low‑ and high‑temperature limits are extracted. The Anderson‑Grüneisen parameter δ is derived from the pressure derivative of the bulk modulus expressed through the TOE constants. The second Grüneisen constant q follows from the relation q = γ (1 + δ α T) at T = 298 K. Finally, the adiabatic bulk modulus at 298 K is computed using Anderson's theory, Bₛ = B₀₀ − (δ γ / V₀) ∫₀ᵀ Cᵥ dT, with the Debye model for the specific heat contribution.

## Reproduction target
Produce the following three output artifacts:
1. A JSON file containing the ten independent third‑order elastic constants Cᵢⱼₖ of hcp cobalt at 4 K and at 298 K, in units of 10¹¹ dyn/cm², ordered as [C₁₁₁, C₂₂₂, C₃₃₃, C₁₁₂, C₁₁₃, C₁₂₃, C₁₃₃, C₁₄₄, C₁₅₅, C₃₄₄].
2. A JSON file with the four derived thermodynamic quantities: the low‑temperature limit γ_L of the volume Grüneisen gamma, the Anderson‑Grüneisen parameter δ, the second Grüneisen constant q, and the high‑temperature limit γ_H of the volume Grüneisen gamma.
3. A JSON file containing the adiabatic bulk modulus B_s at 298 K, in units of 10¹¹ dyn/cm².

## Assets

- Second-order elastic constants of hcp cobalt
- Experimental high-temperature Grüneisen gamma of cobalt
- Cobalt atomic mass and nearest-neighbor distance
- Ramji Rao–Srinivasan model expressions for TOE constants
- Reference thermodynamic data for cobalt
- Python numerical packages

## Workflow steps

### Step 1: Determine model parameters
- Role: process
- Action: Obtain the second-order elastic constants C11 and C33 of hcp cobalt at 4 K and 298 K from the published work of Fisher and Dever (1967). Use the experimental high-temperature Grüneisen gamma γ_H = 2.07 to fix the exponent sum (n+m) = 6*γ_H. With the nearest-neighbor distance D = 2.514 a.u. and the atomic mass M = 58.933 u, compute the auxiliary constant η from the measured SOE constants, then calculate k2 and k3 from the model definitions.
- Evidence: `/app/outputs/model_parameters.json`

### Step 2: Compute TOE constants
- Role: scored (load-bearing)
- Action: Using the parameters k2, k3, D, and the model expressions for an ideal hcp lattice, evaluate the ten independent third-order elastic constants C_ijk at both 4 K and 298 K. Write the results to toe_constants.json.
- Output file: `/app/outputs/toe_constants.json`
- Format: json
- Contract: JSON object with keys '4K' and '298K'; each value is a list of 10 floats in units of 10^11 dynes/cm^2, ordered [C111, C222, C333, C112, C113, C123, C133, C144, C155, C344].
- Scoring: scored by hidden verifier

### Step 3: Compute thermodynamic quantities
- Role: scored (load-bearing)
- Action: From the TOE constants and SOE constants, compute: (a) the low-temperature limit γ_L of the volume Grüneisen gamma via an elastic-wave velocity averaging procedure; (b) the Anderson-Grüneisen parameter δ from the pressure derivative of the bulk modulus; (c) the second Grüneisen constant q using q = γ (1 + δ α T) with the given thermal expansion coefficient α and T = 298 K; (d) the high-temperature limit γ_H of the volume Grüneisen gamma by performing a lattice dynamics calculation (using the central-force model to obtain mode frequencies, mode Grüneisen parameters, and the frequency distribution, then integrating with the specific heat) and recording its high-temperature asymptote. Write all four scalars to thermodynamic_constants.json.
- Output file: `/app/outputs/thermodynamic_constants.json`
- Format: json
- Contract: JSON object with keys: 'gamma_L' (float), 'delta' (float), 'q' (float), 'gamma_H' (float).
- Scoring: scored by hidden verifier

### Step 4: Compute bulk modulus at 298 K
- Role: scored (load-bearing)
- Action: Using the Anderson theory formula B_s = B_00 - (δ γ / V_0) ∫_0^T C_v dT with T = 298 K, δ from step 03, an appropriate average Grüneisen constant (e.g., the experimental value 2.07), the Debye model for the specific heat integral with θ_D = 446 K, and the parameters B_00 = 19.49×10^11 dynes/cm^2 and V_0 = 6.668, compute the adiabatic bulk modulus B_s at 298 K. Write the result to bulk_modulus_298K.json.
- Output file: `/app/outputs/bulk_modulus_298K.json`
- Format: json
- Contract: JSON object with key 'B_s_298K' (float) in units of 10^11 dynes/cm^2.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/toe_constants.json`
- `/app/outputs/thermodynamic_constants.json`
- `/app/outputs/bulk_modulus_298K.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### toe_constants.json
- path: `/app/outputs/toe_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Ten third-order elastic constants of hcp cobalt at 4 K and 298 K in units of 10^11 dynes/cm^2.
- schema:
  - `type`: object
  - `properties`:
    - `4K`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 10
      - `maxItems`: 10
    - `298K`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 10
      - `maxItems`: 10
  - `required`: `4K`, `298K`

### thermodynamic_constants.json
- path: `/app/outputs/thermodynamic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Low-temperature limit of volume Grüneisen gamma, Anderson-Grüneisen parameter, second Grüneisen constant, and high-temperature limit of volume Grüneisen gamma for hcp cobalt.
- schema:
  - `type`: object
  - `properties`:
    - `gamma_L`:
      - `type`: number
    - `delta`:
      - `type`: number
    - `q`:
      - `type`: number
    - `gamma_H`:
      - `type`: number
  - `required`: `gamma_L`, `delta`, `q`, `gamma_H`

### bulk_modulus_298K.json
- path: `/app/outputs/bulk_modulus_298K.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Adiabatic bulk modulus of hcp cobalt at 298 K in units of 10^11 dynes/cm^2.
- schema:
  - `type`: object
  - `properties`:
    - `B_s_298K`:
      - `type`: number
  - `required`: `B_s_298K`

Notes: All scored artifacts are compared against hidden reference values derived from the paper's reported results. Tolerances are set to absorb numerical differences from independent re-implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "toe_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "4K": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 10,
            "maxItems": 10
          },
          "298K": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 10,
            "maxItems": 10
          }
        },
        "required": [
          "4K",
          "298K"
        ]
      },
      "description": "Ten third-order elastic constants of hcp cobalt at 4 K and 298 K in units of 10^11 dynes/cm^2."
    },
    {
      "file": "thermodynamic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "gamma_L": {
            "type": "number"
          },
          "delta": {
            "type": "number"
          },
          "q": {
            "type": "number"
          },
          "gamma_H": {
            "type": "number"
          }
        },
        "required": [
          "gamma_L",
          "delta",
          "q",
          "gamma_H"
        ]
      },
      "description": "Low-temperature limit of volume Grüneisen gamma, Anderson-Grüneisen parameter, second Grüneisen constant, and high-temperature limit of volume Grüneisen gamma for hcp cobalt."
    },
    {
      "file": "bulk_modulus_298K.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "B_s_298K": {
            "type": "number"
          }
        },
        "required": [
          "B_s_298K"
        ]
      },
      "description": "Adiabatic bulk modulus of hcp cobalt at 298 K in units of 10^11 dynes/cm^2."
    }
  ],
  "notes": "All scored artifacts are compared against hidden reference values derived from the paper's reported results. Tolerances are set to absorb numerical differences from independent re-implementations."
}
```

## How you are scored
A hidden verifier independently scores each of the three output artifacts. The verifier compares your submitted arrays and scalar values against reference data using a set of tolerances that account for legitimate variations in numerical implementation (e.g., integration grid density, root‑finding tolerance). The reward is a weighted sum of the individual artifact scores; your task is to faithfully implement the described model and procedures, not to guess the exact numbers. The scoring rules and tolerances are not public.
