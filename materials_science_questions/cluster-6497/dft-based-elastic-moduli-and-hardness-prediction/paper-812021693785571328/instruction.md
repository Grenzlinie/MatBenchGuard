# Maximum-entropy statistical model for internal stress distributions in polycrystalline ceramics

## Problem background
Boron nitride polycrystals containing high-pressure phases (wurtzite BN_W and sphalerite BN_S) together with small amounts of graphite-like BN_g exhibit complex internal stress distributions. These stresses arise from phase transformations, differences in thermal expansion and elastic properties, and the anisotropy of the grains. Understanding the internal stress state is important for optimising mechanical properties such as cracking resistance. An information-theoretic maximum-entropy statistical model provides a way to compute the distributions of inherent stresses and strains and to extract the mean axial stress σ₀ and the rms deviation Δσ in each phase. The target of this task is to compute σ₀ and Δσ for a set of specified phase compositions, texture angles, and stress sources.

## Approach
The model treats the polycrystal as a heterogeneous elastic solid with isotropic spherical grains. Using the maximum-entropy principle together with the effective Hooke tensor and thermal strains, one obtains a distribution function for the local strains. The parameters of the distribution (μ, μ_σ, μ_ε) are determined by ensemble averages over the probability density of elastic moduli and transformation/thermal strains. The inputs to the model are the isotropic elastic constants (Young’s modulus E and Poisson’s ratio ν) and linear thermal expansion coefficients α of the phases, the transformation strains associated with phase changes, the temperature change ΔT, and the external pressure σ_a. The computation is split into four analysis cases: (1) high‑temperature transformation, where stresses develop during cooling from synthesis conditions due solely to thermal expansion mismatch and elastic unloading; (2) low‑temperature transformation, which additionally includes an isotropic transformation strain from the BN_W→BN_S volume change; (3) a single‑phase textured BN_W polycrystal, where intrinsic thermal expansion anisotropy is the only stress source; and (4) a three‑phase system with a small fraction of BN_g, which introduces an additional large isotropic transformation strain. For each case the model yields a mean axial stress σ₀ and an rms fluctuation Δσ for the relevant phases.

## Reproduction target
Implement the maximum-entropy statistical model using the elastic constants, thermal expansion coefficients, and transformation strains specified below. For each of the four cases, compute the mean axial stress σ₀ (GPa) and the rms deviation Δσ (GPa) and write the results to stress_results.json in the required schema.

Cases and conditions:
- Cases 1 and 2 (two‑phase BN_W + BN_S): compute σ₀ and Δσ for both BN_W and BN_S at BN_S volume fractions V_BNS = 0.0, 0.2, 0.4, 0.6, 0.8, 1.0.
- Case 3 (single‑phase textured BN_W): compute σ₀ and Δσ for texture angles of 0°, 15°, 30°, 45°, 60°, 75°, 90° (measured from [0001] direction).
- Case 4 (three‑phase BN_W + BN_S + BN_g): compute σ₀ and Δσ for the BN_g phase at the three volume fraction triples given in the supporting table (V_BNS, V_BNW, V_BNG) = (0.20, 0.79, 0.01), (0.50, 0.49, 0.01), (0.49, 0.49, 0.02).

Inputs common to all cases:
- Temperature change: ΔT = –1700 K.
- External pressure during unloading: σ_a = –5 GPa.
- The isotropic elastic constants and thermal expansion coefficients are: BN_S (E = 900 GPa, ν = 0.1, α = 2.8 × 10⁻⁶ K⁻¹); BN_W (isotropic approximation: E = 800 GPa, ν = 0.1, α = 3.03 × 10⁻⁶ K⁻¹); BN_g (E = 80 GPa, ν = 0.2, thermal expansion coefficient not needed). For case 3 the anisotropic thermal expansion of BN_W is α₁₁ = α₂₂ = 2.7 × 10⁻⁶ K⁻¹, α₃₃ = 3.7 × 10⁻⁶ K⁻¹.
- Transformation strains: for case 2, an isotropic transformation strain ε_tr = 3.2 × 10⁻³ associated with the BN_W→BN_S volume change; for case 4, an additional isotropic transformation strain ε_tr = 170 × 10⁻³ associated with BN_W→BN_g.
- Grains are assumed isotropic and spherical; use the expression ε* = (γ_σ + γ_ε)/2 for the effective strain-independent term.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute internal stress distributions
- Role: scored (load-bearing)
- Action: Implement the statistical model described in the paper (maximum-entropy approach with isotropic spherical grains, effective tensor E, parameters μ, μ_σ, μ_ε defined via ensemble averages of Hooke tensor and thermal strains). Use the elastic constants (Young's modulus, Poisson's ratio) and linear thermal expansion coefficients given in the paper's Table of Elastic Properties. For each scenario (cases 1–4), compute the mean axial stress σ₀ (GPa) and rms deviation Δσ (GPa) for the relevant phases using the specified volume fractions, temperature change, and external pressure. Write all results to stress_results.json according to the output schema.
- Output file: `/app/outputs/stress_results.json`
- Format: json
- Contract: A JSON object containing four keys: "case1", "case2", "case3", "case4". "case1" and "case2" are each an array of objects with fields: "V_BNS" (number, volume fraction), "phase" (string, either "BN_W" or "BN_S"), "sigma0" (number, GPa), "delta_sigma" (number, GPa). "case3" is an array of objects with fields: "angle_deg" (number, texture angle in degrees), "sigma0" (number, GPa), "delta_sigma" (number, GPa). "case4" is an object with key "table2" containing an array of objects with fields: "V_BNS" (number), "V_BNW" (number), "V_BNG" (number), "sigma0" (number, GPa), "delta_sigma" (number, GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_results.json
- path: `/app/outputs/stress_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed mean axial stress σ₀ and rms deviation Δσ for all analysis cases. The checker will compare each σ₀ and Δσ to the paper's published values within tolerance.
- schema:
  - `type`: object
  - `properties`:
    - `case1`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `V_BNS`:
            - `type`: number
          - `phase`:
            - `type`: string
          - `sigma0`:
            - `type`: number
            - `unit`: GPa
          - `delta_sigma`:
            - `type`: number
            - `unit`: GPa
        - `required`: `V_BNS`, `phase`, `sigma0`, `delta_sigma`
    - `case2`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `V_BNS`:
            - `type`: number
          - `phase`:
            - `type`: string
          - `sigma0`:
            - `type`: number
            - `unit`: GPa
          - `delta_sigma`:
            - `type`: number
            - `unit`: GPa
        - `required`: `V_BNS`, `phase`, `sigma0`, `delta_sigma`
    - `case3`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `angle_deg`:
            - `type`: number
          - `sigma0`:
            - `type`: number
            - `unit`: GPa
          - `delta_sigma`:
            - `type`: number
            - `unit`: GPa
        - `required`: `angle_deg`, `sigma0`, `delta_sigma`
    - `case4`:
      - `type`: object
      - `properties`:
        - `table2`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `V_BNS`:
                - `type`: number
              - `V_BNW`:
                - `type`: number
              - `V_BNG`:
                - `type`: number
              - `sigma0`:
                - `type`: number
                - `unit`: GPa
              - `delta_sigma`:
                - `type`: number
                - `unit`: GPa
            - `required`: `V_BNS`, `V_BNW`, `V_BNG`, `sigma0`, `delta_sigma`
  - `required`: `case1`, `case2`, `case3`, `case4`

Notes: The task covers the paper's entire computational stage (model solution). The comparison with experimental x-ray measurements is not required as an agent step; it serves as the basis for the hidden grading reference.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "case1": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "V_BNS": {
                  "type": "number"
                },
                "phase": {
                  "type": "string"
                },
                "sigma0": {
                  "type": "number",
                  "unit": "GPa"
                },
                "delta_sigma": {
                  "type": "number",
                  "unit": "GPa"
                }
              },
              "required": [
                "V_BNS",
                "phase",
                "sigma0",
                "delta_sigma"
              ]
            }
          },
          "case2": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "V_BNS": {
                  "type": "number"
                },
                "phase": {
                  "type": "string"
                },
                "sigma0": {
                  "type": "number",
                  "unit": "GPa"
                },
                "delta_sigma": {
                  "type": "number",
                  "unit": "GPa"
                }
              },
              "required": [
                "V_BNS",
                "phase",
                "sigma0",
                "delta_sigma"
              ]
            }
          },
          "case3": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "angle_deg": {
                  "type": "number"
                },
                "sigma0": {
                  "type": "number",
                  "unit": "GPa"
                },
                "delta_sigma": {
                  "type": "number",
                  "unit": "GPa"
                }
              },
              "required": [
                "angle_deg",
                "sigma0",
                "delta_sigma"
              ]
            }
          },
          "case4": {
            "type": "object",
            "properties": {
              "table2": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "V_BNS": {
                      "type": "number"
                    },
                    "V_BNW": {
                      "type": "number"
                    },
                    "V_BNG": {
                      "type": "number"
                    },
                    "sigma0": {
                      "type": "number",
                      "unit": "GPa"
                    },
                    "delta_sigma": {
                      "type": "number",
                      "unit": "GPa"
                    }
                  },
                  "required": [
                    "V_BNS",
                    "V_BNW",
                    "V_BNG",
                    "sigma0",
                    "delta_sigma"
                  ]
                }
              }
            }
          }
        },
        "required": [
          "case1",
          "case2",
          "case3",
          "case4"
        ]
      },
      "description": "Computed mean axial stress σ₀ and rms deviation Δσ for all analysis cases. The checker will compare each σ₀ and Δσ to the paper's published values within tolerance."
    }
  ],
  "notes": "The task covers the paper's entire computational stage (model solution). The comparison with experimental x-ray measurements is not required as an agent step; it serves as the basis for the hidden grading reference."
}
```

## How you are scored
A hidden verifier reads the output file stress_results.json. It compares each computed σ₀ and Δσ value against a set of hidden reference values derived from the original study, within a tolerance (the tolerance is chosen to allow for differences in implementation, numerical integration quality, and floating‑point precision). The verifier computes the fraction of values that fall within the tolerance for each case separately. The final reward is a weighted sum of these case scores; all four cases carry a similar weight, with the main emphasis on the numerical accuracy of σ₀ and Δσ across the requested volume fractions, angles, and compositions. Reporting the paper’s numbers without actually implementing the model will not satisfy the checker because the tolerance is tight enough that generic guesses will miss the mark, while a correct implementation of the described physical model is expected to pass. The reward is a float between 0 and 1, where 1 indicates that all checked values met the tolerance criteria.
