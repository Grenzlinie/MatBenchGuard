# Kinetic Hydrogen Supersaturation from Dislocation Transport

## Problem background
Hydrogen embrittlement in steels is sometimes attributed to the idea that moving dislocations can transport hydrogen and deposit it at internal voids, creating high local pressures for purely kinetic reasons. This task investigates whether dislocation transport can produce a significant kinetic hydrogen supersaturation. A continuum upper‑bound model is used that balances the rate of hydrogen arrival via dislocations with diffusive departure, yielding a steady‑state supersaturation S.

## Approach
Implement the steady‑state diffusion‑resistance model that equates the dislocation‑mediated hydrogen arrival rate to the diffusive loss rate. For a smooth surface, the relevant geometry factor is ln(2L/r₀); for a crack tip it is ln(4L/r₀); and for a homogeneous internal distribution it is ln(L/r₀). The supersaturation S = (λ ε̇ η) / (2π a b D c₀) × ln(factor). Use the following material and geometric parameters reported in the literature (do not alter them – they define the target). Ferritic iron: η = 2, a·b = 5.81×10⁻²⁰ m², D = 1×10⁻⁹ m²/s, c₀ = 3.4×10²¹ atoms/m³, L = λ = 1×10⁻⁷ m, r₀ = 1×10⁻⁹ m, ε̇ = 1×10⁻⁵ s⁻¹. Ferritic iron crack tip: same parameters plus crack velocity v = 1×10⁻⁵ m/s and plastic zone size R = 5×10⁻⁵ m; compute the local crack‑tip strain rate as ε̇ = v / (2R). Austenitic stainless steel smooth surface: a·b = 5.77×10⁻²⁰ m²; the permeability product D·c₀ = 2×10¹⁰ atoms/(m·s); choose any D and c₀ consistent with this product (e.g., D = 1×10⁻⁹ m²/s, c₀ = 2×10¹⁹ atoms/m³) and report the values you used; all other parameters as for ferritic iron. Internal hydrogen case (ferritic iron): same parameters as the ferritic smooth‑surface case. Evaluate S for all four cases and write the results to the output file.

## Reproduction target
Compute the kinetic supersaturation S for the four cases – (1) external hydrogen smooth surface in ferritic iron, (2) external hydrogen smooth surface in austenitic stainless steel, (3) external hydrogen crack tip in ferritic iron, and (4) internal hydrogen homogeneous distribution in ferritic iron. Produce a single JSON file, supersaturation_results.json, containing an entry for each case with the computed S value and the full set of parameter values used. The correctness of your computed S values will be verified by recomputing S from your supplied parameters and comparing against reference values.

## Assets

- Python 3: python3

## Workflow steps

### Step 1: Compute kinetic supersaturation S for all four cases
- Role: scored (load-bearing)
- Action: Implement the three geometry‑specific supersaturation formulas: smooth surface (ln(2L/r0)), crack tip (ln(4L/r0)), and internal hydrogen (ln(L/r0)). Using the publicly reported material and geometric parameters for ferritic iron and austenitic stainless steel, evaluate the supersaturation S = (λ ε̇ η)/(2π a b D c0) × ln(factor) for each case: (1) external hydrogen smooth surface ferritic iron, (2) same for austenitic stainless steel, (3) external hydrogen crack tip in ferritic iron with crack‑tip strain rate estimated from crack velocity and plastic zone size, (4) internal hydrogen homogeneous initial distribution in ferritic iron. Write the four S values and the complete parameter sets used for each case into the output file.
- Output file: `/app/outputs/supersaturation_results.json`
- Format: json
- Contract: Top-level JSON object with keys 'smooth_iron', 'smooth_austenitic', 'crack_iron', 'internal_iron'. Each value is an object with required fields: 'S' (float) and 'parameters' (object containing numeric fields: lambda, epsilon_dot, eta, a_times_b, D, c0, L, r0; for 'crack_iron' additionally crack_velocity and plastic_zone_size).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/supersaturation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### supersaturation_results.json
- path: `/app/outputs/supersaturation_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed supersaturation S and parameter sets for the four model cases. The checker extracts the parameters, recomputes S using the appropriate geometry factor, and compares the result against hidden gold values.
- schema:
  - `type`: object
  - `required`: `smooth_iron`, `smooth_austenitic`, `crack_iron`, `internal_iron`
  - `properties`:
    - `smooth_iron`:
      - `type`: object
      - `required`: `S`, `parameters`
      - `properties`:
        - `S`:
          - `type`: number
        - `parameters`:
          - `type`: object
          - `required`: `lambda`, `epsilon_dot`, `eta`, `a_times_b`, `D`, `c0`, `L`, `r0`
    - `smooth_austenitic`:
      - `type`: object
      - `required`: `S`, `parameters`
      - `properties`:
        - `S`:
          - `type`: number
        - `parameters`:
          - `type`: object
          - `required`: `lambda`, `epsilon_dot`, `eta`, `a_times_b`, `D`, `c0`, `L`, `r0`
    - `crack_iron`:
      - `type`: object
      - `required`: `S`, `parameters`
      - `properties`:
        - `S`:
          - `type`: number
        - `parameters`:
          - `type`: object
          - `required`: `lambda`, `epsilon_dot`, `eta`, `a_times_b`, `D`, `c0`, `L`, `r0`, `crack_velocity`, `plastic_zone_size`
    - `internal_iron`:
      - `type`: object
      - `required`: `S`, `parameters`
      - `properties`:
        - `S`:
          - `type`: number
        - `parameters`:
          - `type`: object
          - `required`: `lambda`, `epsilon_dot`, `eta`, `a_times_b`, `D`, `c0`, `L`, `r0`

Notes: No gold values or tolerances are disclosed. The agent must use the publicly known parameters from the paper's numerical examples (ferritic iron: η=2, a·b=5.81e-20 m², D=1e-9 m²/s, c0=3.4e21 atoms/m³, L=λ=1e-7 m, r0=1e-9 m, ε̇=1e-5 s⁻¹; crack adds v=1e-5 m/s, R=5e-5 m; austenitic: a·b=5.77e-20 m², D·c0=2e10 atoms/(m·s)).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "supersaturation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "smooth_iron",
          "smooth_austenitic",
          "crack_iron",
          "internal_iron"
        ],
        "properties": {
          "smooth_iron": {
            "type": "object",
            "required": [
              "S",
              "parameters"
            ],
            "properties": {
              "S": {
                "type": "number"
              },
              "parameters": {
                "type": "object",
                "required": [
                  "lambda",
                  "epsilon_dot",
                  "eta",
                  "a_times_b",
                  "D",
                  "c0",
                  "L",
                  "r0"
                ]
              }
            }
          },
          "smooth_austenitic": {
            "type": "object",
            "required": [
              "S",
              "parameters"
            ],
            "properties": {
              "S": {
                "type": "number"
              },
              "parameters": {
                "type": "object",
                "required": [
                  "lambda",
                  "epsilon_dot",
                  "eta",
                  "a_times_b",
                  "D",
                  "c0",
                  "L",
                  "r0"
                ]
              }
            }
          },
          "crack_iron": {
            "type": "object",
            "required": [
              "S",
              "parameters"
            ],
            "properties": {
              "S": {
                "type": "number"
              },
              "parameters": {
                "type": "object",
                "required": [
                  "lambda",
                  "epsilon_dot",
                  "eta",
                  "a_times_b",
                  "D",
                  "c0",
                  "L",
                  "r0",
                  "crack_velocity",
                  "plastic_zone_size"
                ]
              }
            }
          },
          "internal_iron": {
            "type": "object",
            "required": [
              "S",
              "parameters"
            ],
            "properties": {
              "S": {
                "type": "number"
              },
              "parameters": {
                "type": "object",
                "required": [
                  "lambda",
                  "epsilon_dot",
                  "eta",
                  "a_times_b",
                  "D",
                  "c0",
                  "L",
                  "r0"
                ]
              }
            }
          }
        }
      },
      "description": "Computed supersaturation S and parameter sets for the four model cases. The checker extracts the parameters, recomputes S using the appropriate geometry factor, and compares the result against hidden gold values."
    }
  ],
  "notes": "No gold values or tolerances are disclosed. The agent must use the publicly known parameters from the paper's numerical examples (ferritic iron: η=2, a·b=5.81e-20 m², D=1e-9 m²/s, c0=3.4e21 atoms/m³, L=λ=1e-7 m, r0=1e-9 m, ε̇=1e-5 s⁻¹; crack adds v=1e-5 m/s, R=5e-5 m; austenitic: a·b=5.77e-20 m², D·c0=2e10 atoms/(m·s))."
}
```

## How you are scored
A hidden verifier reads your supersaturation_results.json and, for each of the four cases, recomputes S from the parameter values you submitted using the appropriate geometric factor (ln(2L/r₀), ln(4L/r₀), or ln(L/r₀)). Each case’s recomputed S is compared to a hidden gold value. Your reward is the fraction of cases that agree within the verifier’s hidden tolerance; all four correct gives full credit. Simply reporting a number without consistent parameters will be detected and scored zero.
