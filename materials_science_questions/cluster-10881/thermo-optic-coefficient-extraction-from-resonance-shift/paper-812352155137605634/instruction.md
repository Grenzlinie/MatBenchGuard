# Nonlinear Optical Coefficient Extraction from Second-Harmonic Generation

## Problem background
High-power lasers require efficient frequency doubling to access visible and ultraviolet wavelengths. Crystals of cesium dihydrogen arsenate (CDA) and deuterated CDA (CD*A) are promising nonlinear optical materials that allow 90‑degree phase‑matched second‑harmonic generation (SHG) of 1064 nm Nd‑laser radiation. To evaluate their performance, two key properties must be determined: the nonlinear optical coefficient d₃₆ and the temperature dependence of the birefringence. This task asks you to compute these quantities from the measured peak SHG conversion efficiency and temperature bandwidth, using the physical models described below.

## Approach
The reproduction follows a two‑part analytical approach. **All calculations are performed in the electrostatic unit system (ESU / Gaussian units)**, which is the unit system used in the source paper. In this system electric field amplitudes are expressed in statvolt cm⁻¹, lengths in centimetres, time in seconds, and power in erg s⁻¹.

- **d₃₆ extraction**: The plane‑wave lossless SHG model (P₂/P₁ = tanh²(l/l_s)) relates the peak conversion efficiency to the nonlinear coefficient under a known pump electric field amplitude E₀. E₀ is derived from the effective pump power density using the relation **I = (c nᵒ₁ / 8π) E₀²**, which is the standard connection between intensity and field amplitude in Gaussian units (c is the speed of light in vacuum, nᵒ₁ the ordinary refractive index at the fundamental wavelength). The effective pump power density is obtained by taking the nominal laser power (50 MW), accounting for a 10 % polarisation loss and the crystal‑dependent transmission / Fresnel reflection loss (12 % for CDA, 7.5 % for CD*A), and dividing by the beam area (beam diameter 5 mm). Once E₀ is known, the relation l_s⁻¹ = (8π²/(nᵒ₁ λ)) d₃₆ E₀ together with the measured conversion efficiency yields an initial value of d₃₆. A multimode intensity‑fluctuation correction factor **1/√((2n‑1)/n)** with a representative number of axial modes n = 3 is then applied to obtain the corrected d₃₆ that would be measured with an ideal single‑mode pump.

- **Birefringence temperature variation**: The temperature bandwidth ΔT (FWHM) of 90° phase matching is related to the temperature derivative of the birefringence by **d(n₂⁰ − n₁⁰)/dT = λ/(2.25 l ΔT)**. The derivative is computed using the central measured ΔT values (3.4 °C for CDA, 4.5 °C for CD*A) and the crystal lengths (all expressed in centimetres).

A third quantity, the ratio of d₃₆ to the known value for KDP, is obtained by dividing the corrected d₃₆ by d₃₆(KDP) = 1.04 × 10⁻⁹ ESU.

All required numerical constants are listed in the workflow steps.

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
- Action:
  1. Adopt the **ESU (Gaussian) unit system**. Use the following physical constants and conversion factors:
     - Speed of light: **c = 2.99792458 × 10¹⁰ cm s⁻¹**
     - 1 W = 10⁷ erg s⁻¹, therefore 50 MW = 5 × 10¹⁴ erg s⁻¹
     - Fundamental wavelength: λ = 1.0642 μm = **1.0642 × 10⁻⁴ cm**
     - Beam diameter = 5 mm, so beam radius = 0.25 cm, beam area **A = π × (0.25 cm)²**
  2. Compute the **effective pump power density** I_eff for each crystal by correcting the nominal laser power for losses:
     - Polarisation loss: 10 % (factor 0.90)
     - Crystal transmission and Fresnel reflection loss: **12 % for CDA** (factor 0.88), **7.5 % for CD*A** (factor 0.925)
     - Therefore **P_eff = 50 MW × 0.90 × (1 − L)** with L = 0.12 (CDA) or L = 0.075 (CD*A)
     - Convert P_eff to erg s⁻¹ (multiply by 10⁷ erg J⁻¹) and divide by A to obtain I_eff in erg s⁻¹ cm⁻².
  3. Determine the pump electric field amplitude from the intensity relation in Gaussian units:
     - **I_eff = (c nᵒ₁ / 8π) E₀²**   →   **E₀ = √(8π I_eff / (c nᵒ₁))**
     - Use the ordinary refractive indices at 10642 Å: nᵒ₁(CDA) = 1.5516, nᵒ₁(CD*A) = 1.5503.
  4. Use the **loss‑corrected peak power‑conversion efficiencies** from the paper: 57 % for CDA (P₂/P₁ = 0.57) and 45 % for CD*A (P₂/P₁ = 0.45).
     - Crystal lengths: l = 17.5 mm = 1.75 cm (CDA), l = 13.5 mm = 1.35 cm (CD*A).
  5. Solve the plane‑wave lossless SHG equation for the nonlinear interaction length l_s:
     - **P₂/P₁ = tanh²(l / l_s)**
     - l_s⁻¹ = (8π² / (nᵒ₁ λ)) d₃₆ E₀
     - From the measured efficiency, obtain l_s, then extract the **initial (uncorrected) d₃₆**.
  6. Apply the multimode intensity‑fluctuation correction. For n ≈ 3 axial modes the enhancement factor is √((2n‑1)/n) = √(5/3). The intrinsic (corrected) d₃₆ is obtained by dividing the initial value by this factor:
     - **d₃₆(corrected) = d₃₆(initial) / √((2n‑1)/n)** with n = 3.
  7. Write the corrected d₃₆ values (in ESU) for both crystals.
- Output file: `/app/outputs/d36_values.json`
- Format: json
- Contract: {"cda": <float>, "cd_a": <float>}
- Scoring: scored by hidden verifier

### Step 2: Compute birefringence temperature variation
- Role: scored
- Action: Using the measured temperature bandwidths ΔT (FWHM) = 3.4 °C for CDA and 4.5 °C for CD*A, crystal lengths l (1.75 cm for CDA, 1.35 cm for CD*A), and fundamental wavelength λ = 1.0642 × 10⁻⁴ cm, compute the temperature derivative of the birefringence:
  - **d(n₂⁰ − n₁⁰)/dT = λ / (2.25 l ΔT)**
  - Use the central ΔT values (3.4 °C and 4.5 °C).
  - The result is in K⁻¹ (°C⁻¹ is equivalent).
  - Write the results.
- Output file: `/app/outputs/birefringence_temp_variation.json`
- Format: json
- Contract: {"cda": <float>, "cd_a": <float>}
- Scoring: scored by hidden verifier

### Step 3: Compute d36/d36(KDP) ratio
- Role: scored
- Action: Divide the corrected d₃₆ value (identical for both crystals, obtained in Step 1) by the reference value d₃₆(KDP) = 1.04 × 10⁻⁹ ESU to obtain the dimensionless ratio.
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