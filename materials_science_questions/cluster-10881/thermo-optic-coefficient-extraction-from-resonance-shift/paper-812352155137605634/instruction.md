# Nonlinear Optical Coefficient Extraction from Second-Harmonic Generation

## Problem background
High-power lasers require efficient frequency doubling to access visible and ultraviolet wavelengths. Crystals of cesium dihydrogen arsenate (CDA) and deuterated CDA (CD*A) are promising nonlinear optical materials that allow 90‑degree phase‑matched second‑harmonic generation (SHG) of 1064 nm Nd‑laser radiation. To evaluate their performance, two key properties must be determined: the nonlinear optical coefficient d₃₆ and the temperature dependence of the birefringence. This task asks you to compute these quantities from the measured peak SHG conversion efficiency and temperature bandwidth, using the physical models described below.

## Approach
The reproduction follows a two‑part analytical approach:

- **d₃₆ extraction**: The plane‑wave lossless SHG model (P₂/P₁ = tanh²(l/l_s)) relates the peak conversion efficiency to the nonlinear coefficient under a known pump electric field E₀. E₀ is derived from the fundamental power density (50 MW pump power, 5 mm beam diameter) and the ordinary refractive index. After obtaining the preliminary d₃₆ for each crystal, a multimode intensity‑fluctuation correction factor 1/√((2n‑1)/n) with a representative number of axial modes n = 3 is applied to yield the corrected d₃₆.

- **Birefringence temperature variation**: The temperature bandwidth ΔT (FWHM) of 90° phase matching is related to the temperature derivative of the birefringence by d(n₂⁰ − n₁⁰)/dT = λ/(2.25 l ΔT). The derivative is computed using the central measured ΔT values and the crystal lengths.

A third quantity, the ratio of d₃₆ to the known value for KDP, is obtained by dividing the corrected d₃₆ by d₃₆(KDP) = 1.04 × 10⁻⁹ ESU. All required numerical inputs (refractive indices, crystal lengths, conversion efficiencies, temperature bandwidths) are listed in the workflow steps.

## Reproduction target
Compute and write the following three results to the designated JSON files:

1. The corrected nonlinear optical constant d₃₆ (in ESU) for both CDA and CD*A.
2. The temperature variation of the birefringence d(n₂⁰ − n₁⁰)/dT (in K⁻¹) for both crystals.
3. The dimensionless ratio d₃₆/d₃₆(KDP).

The exact output file schemas and paths are specified in the Workflow Steps and Output Contract. Your solution must produce each artifact using the provided constants and the physical models outlined in the Approach.

## Assets

- d36(KDP) reference value

## Workflow steps

### Step 1: Compute corrected d36 for CDA and CD*A
- Role: scored (load-bearing)
- Action: Using the provided fundamental ordinary refractive indices (n1_o for CDA=1.5516, CD*A=1.5503), crystal lengths (17.5 mm for CDA, 13.5 mm for CD*A), fundamental wavelength 1.0642 μm, pump power 50 MW, beam diameter 5 mm, and loss‑corrected peak conversion efficiencies (57% for CDA, 45% for CD*A), compute the electric field amplitude E0 from power density, then solve the plane-wave lossless relation P2/P1 = tanh²(l/l_s) with l_s⁻¹ = (8π²/(n1_o λ)) d36 E0 to obtain the initial d36 for each crystal. Apply the multimode intensity fluctuation correction factor by dividing the initial value by √((2n−1)/n) using a representative number of axial modes n = 3. Write the corrected d36 values (in ESU) for both crystals.
- Output file: `/app/outputs/d36_values.json`
- Format: json
- Contract: {"cda": <float>, "cd_a": <float>}
- Scoring: scored by hidden verifier

### Step 2: Compute birefringence temperature variation
- Role: scored
- Action: Using the measured temperature bandwidths ΔT (FWHM) = 3.4±0.1 °C for CDA and 4.5±0.1 °C for CD*A, crystal lengths as above, and fundamental wavelength 1.0642 μm, compute the temperature derivative of the birefringence d(n2⁰ − n1⁰)/dT using the relation d(n2⁰ − n1⁰)/dT = λ/(2.25 l ΔT). Use the central ΔT values (3.4 °C and 4.5 °C). Write the results (in K⁻¹).
- Output file: `/app/outputs/birefringence_temp_variation.json`
- Format: json
- Contract: {"cda": <float>, "cd_a": <float>}
- Scoring: scored by hidden verifier

### Step 3: Compute d36/d36(KDP) ratio
- Role: scored
- Action: Divide the corrected d36 value (identical for both crystals, obtained in the previous step) by the reference value d36(KDP) = 1.04 × 10⁻⁹ ESU to obtain the dimensionless ratio.
- Output file: `/app/outputs/d36_ratio.json`
- Format: json
- Contract: {"ratio": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/d36_values.json`
- `/app/outputs/birefringence_temp_variation.json`
- `/app/outputs/d36_ratio.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### d36_values.json
- path: `/app/outputs/d36_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Corrected nonlinear optical constant d36 (in ESU) for CDA and CD*A.
- schema:
  - `type`: object
  - `required`:
    - `cda`: float
    - `cd_a`: float

### birefringence_temp_variation.json
- path: `/app/outputs/birefringence_temp_variation.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Temperature derivative of birefringence d(n2⁰ − n1⁰)/dT (in K⁻¹) for CDA and CD*A.
- schema:
  - `type`: object
  - `required`:
    - `cda`: float
    - `cd_a`: float

### d36_ratio.json
- path: `/app/outputs/d36_ratio.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Dimensionless ratio d36(CDA)/d36(KDP) = d36(CD*A)/d36(KDP).
- schema:
  - `type`: object
  - `required`:
    - `ratio`: float

Notes: All necessary constants (refractive indices, crystal lengths, laser parameters, conversion efficiencies, temperature bandwidths, number of axial modes) are provided in the instruction or are standard physical constants. The agent performs the computations using the described formulas; the checker will compare the submitted values to hidden reference values derived from the same public inputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "d36_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "cda": "float",
          "cd_a": "float"
        }
      },
      "description": "Corrected nonlinear optical constant d36 (in ESU) for CDA and CD*A."
    },
    {
      "file": "birefringence_temp_variation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "cda": "float",
          "cd_a": "float"
        }
      },
      "description": "Temperature derivative of birefringence d(n2⁰ − n1⁰)/dT (in K⁻¹) for CDA and CD*A."
    },
    {
      "file": "d36_ratio.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "ratio": "float"
        }
      },
      "description": "Dimensionless ratio d36(CDA)/d36(KDP) = d36(CD*A)/d36(KDP)."
    }
  ],
  "notes": "All necessary constants (refractive indices, crystal lengths, laser parameters, conversion efficiencies, temperature bandwidths, number of axial modes) are provided in the instruction or are standard physical constants. The agent performs the computations using the described formulas; the checker will compare the submitted values to hidden reference values derived from the same public inputs."
}
```

## How you are scored
A hidden verifier checks your submitted artifact files against independently derived reference values. The verifier assesses each scored output (d₃₆, birefringence derivative, and ratio) individually, then combines the scores with predefined weights to produce a single reward between 0 and 1. Reporting a number without following the required computation will not earn full credit. The reward reflects how accurately your computed results match the expected target quantities; partial credit is possible.
