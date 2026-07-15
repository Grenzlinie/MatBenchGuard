# Critical Strain and Glass Transition in a Bulk Metallic Glass System

## Problem background
Bulk metallic glasses require extremely low critical cooling rates to avoid crystallization, but molecular dynamics simulations operate at much higher rates. An atomistic theory proposes that local topological instability, driven by atomic size disparities, can facilitate glass formation. The stability of a local atomic configuration depends on the ratio of atomic radii; when a critical uniform volume expansion is exceeded, the local coordination number changes discontinuously. This critical strain establishes a condition for the glass transition. For a binary alloy, the glass transition temperature and the activation energy for diffusion can be expressed in terms of this critical strain and the material's elastic properties. The goal is to compute the critical uniform volume strain as a function of atomic size ratio and then apply it to predict the glass transition characteristics of a well-known bulk metallic glass former.

## Approach
The theoretical approach starts from the local coordination number of an atom A embedded in a matrix of atom B, expressed as a function of the size ratio x = r_A/r_B. The precise formula uses geometric packing arguments to give N_C(x). The partial derivative of N_C with respect to x determines the change Δx_C needed to change the coordination number by one. From Δx_C, the critical uniform volume expansion for local topological instability is obtained as ε_V^crit = 3 Δx_C / (2 x).

The glass transition temperature T_g is then related to ε_V^crit through the atomic volume Ω and bulk modulus K of the alloy: T_g = (2 Ω K / k_B) (ε_V^crit)², where k_B is Boltzmann's constant. For a specific composition, the activation energy for diffusion at the glass transition is E_a = 0.039 * (1+7) * Ω * K, which incorporates the critical shear strain and the fact that all atoms are frozen at T_g (fraction frozen f = 1). All quantities are evaluated in SI units and converted to the required output units (K and eV).

The workflow consists of implementing these analytic expressions for a set of atomic size ratios to generate the critical strain curve, then computing T_g and E_a for the alloy Fe80B20 using literature values for its atomic volume and bulk modulus.

## Reproduction target
Reproduce the critical uniform volume strain ε_V^crit and the intermediate quantity Δx_C for the atomic size ratios x = 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0. Then, using the critical strain at x=1 (corresponding to equal-sized atoms) and standard material constants for the alloy Fe80B20 (atomic volume Ω and bulk modulus K available in the literature), compute the predicted glass transition temperature T_g (in Kelvin) and the activation energy for diffusion E_a at T_g (in eV). Output all results as a single JSON file.

## Assets

- Python with standard library: python

## Workflow steps

### Step 1: Compute critical strain, glass transition temperature and activation energy
- Role: scored
- Action: Evaluate the analytic expressions for the critical uniform volume strain as a function of atomic size ratio x. Using the critical strain at x=1 and known material constants (atomic volume and bulk modulus) for Fe80B20, compute the glass transition temperature T_g and the activation energy E_a at T_g. Write the results to JSON.
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: { "critical_strain_data": [{"x": float, "delta_x_C": float, "epsilon_V_crit": float}], "glass_transition": {"T_g_K": float, "E_a_eV": float} }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed critical strain curve and glass transition values for Fe80B20.
- schema:
  - `type`: object
  - `required`: `critical_strain_data`, `glass_transition`
  - `properties`:
    - `critical_strain_data`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `x`:
            - `type`: number
          - `delta_x_C`:
            - `type`: number
          - `epsilon_V_crit`:
            - `type`: number
        - `required`: `x`, `delta_x_C`, `epsilon_V_crit`
    - `glass_transition`:
      - `type`: object
      - `properties`:
        - `T_g_K`:
          - `type`: number
        - `E_a_eV`:
          - `type`: number
      - `required`: `T_g_K`, `E_a_eV`

Notes: The checker independently recomputes the critical strain values and compares the agent's glass transition temperature and activation energy against the paper-reported values within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "critical_strain_data",
          "glass_transition"
        ],
        "properties": {
          "critical_strain_data": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "x": {
                  "type": "number"
                },
                "delta_x_C": {
                  "type": "number"
                },
                "epsilon_V_crit": {
                  "type": "number"
                }
              },
              "required": [
                "x",
                "delta_x_C",
                "epsilon_V_crit"
              ]
            }
          },
          "glass_transition": {
            "type": "object",
            "properties": {
              "T_g_K": {
                "type": "number"
              },
              "E_a_eV": {
                "type": "number"
              }
            },
            "required": [
              "T_g_K",
              "E_a_eV"
            ]
          }
        }
      },
      "description": "Computed critical strain curve and glass transition values for Fe80B20."
    }
  ],
  "notes": "The checker independently recomputes the critical strain values and compares the agent's glass transition temperature and activation energy against the paper-reported values within tolerance."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently recomputes Δx_C and ε_V^crit from the same analytic formulas for each specified x value and compares them to your reported values. For T_g and E_a, the verifier compares your computed values to the expected results derived from the paper's expressions using the accepted material constants for Fe80B20. The verifier first validates that your submitted JSON file adheres to the required schema. Then it assigns a reward in [0,1] by combining the agreements across the critical strain data and the glass transition quantities. The precise tolerances and weighting are fixed by the verifier; your code must produce results that match the target within the allowed margins.
