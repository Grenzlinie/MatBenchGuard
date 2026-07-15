# Spectral Moments and Anharmonic Heat Capacity of LiGaO₂ from Experimental Data

## Problem background
LiGaO₂ is an orthorhombic ternary compound considered for piezoelectric transducers, substrate applications, and as a host for transition-metal ions. Its elastic, dielectric, and optical properties have been investigated, but the influence of lattice anharmonicity on its vibrational thermal properties has not been quantified in detail. Experimental heat-capacity and thermal-expansion data show temperature dependences that can only be explained by anharmonic contributions. This task aims to determine the first three even spectral moments of the phonon density of states, the high-temperature effective Debye temperature, the anharmonic part of the heat capacity, and the principal and volume Grüneisen functions of LiGaO₂, using only published experimental thermodynamic and elastic data.

## Approach
The analysis rests on the method of spectral moments within the Debye model. Starting from published molar heat capacity at constant pressure (Cₚ), the heat capacity at constant volume (C_V) is obtained by subtracting the (α_V² V_m T)/κ term, where α_V is the volume thermal expansion coefficient, V_m the molar volume, and κ the isothermal compressibility. For each temperature, the effective Debye temperature Θ_D is extracted by inverting the Debye function C_V = 12R·F(Θ_D/T). At sufficiently low temperatures where anharmonicity is negligible, Θ_D² is expanded as a function of 1/T² in the form Θ_D² = Θ∞²[1 − A(Θ∞/T)² + B(Θ∞/T)⁴]. A least‑squares fit to the data below 250 K yields the high‑temperature Debye limit Θ∞ and the coefficients A and B. From these, the even spectral moments μ₂, μ₄, and μ₆ are computed via the algebraic relations μ₂ = (3/5)(kΘ∞/h)², A = (3/100)(μ₄/μ₂² − 25/21), and B = (1/1400)(μ₆/μ₂³ − 125/81 − 100A). The harmonic heat capacity C_Vh(T) is then extrapolated to all temperatures using the fitted Θ_D(T). The anharmonic contribution ΔC_V = C_V − C_Vh is isolated, and its relative part ΔC_V/C_Vh is modelled as b₁T + b₂T², with b₁ and b₂ determined by weighted least squares. Finally, the principal Grüneisen functions γ_i (i = a,b,c) are calculated from the elastic stiffness constants, thermal expansion coefficients, molar volume, and experimental C_V, and the volume Grüneisen function is obtained as the linear‑compressibility‑weighted average of the γ_i. All analyses use only publicly available input data and standard numerical methods.

## Reproduction target
Given the published experimental data for LiGaO₂ (molar heat capacity Cₚ(T) from 180 K to 700 K, linear thermal expansion coefficients α_a(T), α_b(T), α_c(T) from 300 K to 1100 K, molar volume, isothermal compressibility, and elastic stiffness constants c_ij), reproduce the thermodynamic analysis by: converting Cₚ to C_V using C_V = Cₚ − (α_V² V_m T)/κ; inverting the Debye function to obtain the effective Debye temperature Θ_D(T); fitting Θ_D² vs 1/T² to the expansion Θ_D² = Θ∞² [1 − A (Θ∞/T)² + B (Θ∞/T)⁴] for T < 250 K to extract Θ∞, A, and B; computing the spectral moments μ₂ from Θ∞ and μ₄, μ₆ from A and B with the given algebraic relations; computing the harmonic heat capacity C_Vh(T) from the Debye model using Θ∞; determining the anharmonic contribution ΔC_V(T) = C_V(T) − C_Vh(T) and fitting ΔC_V/C_Vh = b₁T + b₂T² to obtain the coefficients b₁ and b₂; and computing the principal Grüneisen functions γ_i = (c_{i1}α_a + c_{i2}α_b + c_{i3}α_c) V_m / C_V for i = a,b,c, as well as the volume Grüneisen function γ as the weighted average of the γ_i with the linear compressibilities. The required outputs are the three scored artifacts described in the workflow steps: the spectral moments and Θ∞, the anharmonic coefficients, and the temperature-dependent Grüneisen functions at specified temperatures.

## Assets

- Molar heat capacity at constant pressure C_p(T) for LiGaO₂ (180-700 K)
- Linear thermal expansion coefficients α_a(T), α_b(T), α_c(T) for LiGaO₂ (300-1100 K)
- Molar volume V_m of LiGaO₂
- Elastic stiffness constants c_ij of LiGaO₂

## Workflow steps

### Step 1: Prepare input data and compute auxiliary quantities
- Role: process
- Action: Compile the experimental heat capacity C_p(T) (180‑700 K), the three linear thermal expansion coefficients α_a(T), α_b(T), α_c(T) (300‑1100 K), the molar volume V_m, and the elastic stiffness constants c_ij from the published references. Compute the isothermal compressibility κ from the elastic compliance constants s_ij. Estimate the low‑temperature Debye temperature Θ₀ using Anderson’s approximation with the elastic constants.
- Evidence: `/app/outputs/data_parameters.json`

### Step 2: Convert heat capacity to constant volume and compute effective Debye temperature
- Role: process
- Action: Convert C_p(T) to C_V(T) using C_V = C_p − (α_V² V_m T)/κ, where α_V = α_a + α_b + α_c. For each temperature, invert the Debye function C_V = 12R F(Θ_D/T) to obtain the effective Debye temperature Θ_D(T).
- Evidence: `/app/outputs/debye_temperature.csv`

### Step 3: Fit high‑temperature expansion to obtain spectral moments and Θ∞
- Role: scored (load-bearing)
- Action: Restrict the Θ_D data to temperatures below 250 K where anharmonicity is negligible. Fit Θ_D² vs 1/T² to the expansion Θ_D² = Θ∞² [1 − A (Θ∞/T)² + B (Θ∞/T)⁴] to extract Θ∞, A, B. Compute μ₂ from Θ∞ using the relation μ₂ = (3/5)(k Θ∞ / h)². Derive μ₄ and μ₆ from A and B using the algebraic relations A = (3/100)(μ₄/μ₂² − 25/21) and B = (1/1400)(μ₆/μ₂³ − 125/81 − 100A). Save μ₂, μ₄, μ₆, and Θ∞ in a JSON file.
- Output file: `/app/outputs/step_04_moments_theta_inf.json`
- Format: json
- Contract: JSON object with keys: "mu2" (s⁻²), "mu4" (s⁻⁴), "mu6" (s⁻⁶), "theta_inf" (K).
- Scoring: scored by hidden verifier

### Step 4: Extrapolate harmonic heat capacity C_Vh(T)
- Role: process
- Action: Using Θ∞, A, B, compute Θ_D(T) for all temperatures via the expansion, then evaluate the harmonic heat capacity C_Vh(T) = 12R F(Θ_D/T).
- Evidence: `/app/outputs/harmonic_cv.csv`

### Step 5: Determine anharmonic heat‑capacity coefficients
- Role: scored
- Action: Compute ΔC_V(T) = C_V(T) − C_Vh(T) and the relative anharmonic contribution ΔC_V/C_Vh. Fit the relative contribution to a model ΔC_V/C_Vh = b₁ T + b₂ T² using least squares. Save b₁ and b₂ in a JSON file.
- Output file: `/app/outputs/step_06_anharmonic_coefficients.json`
- Format: json
- Contract: JSON object with keys: "b1" (K⁻¹), "b2" (K⁻²).
- Scoring: scored by hidden verifier

### Step 6: Calculate macroscopic Grüneisen functions
- Role: scored
- Action: Using the elastic stiffness constants c_ij, the thermal expansion coefficients α_a,α_b,α_c, the molar volume V_m, and the experimental C_V(T), compute the principal Grüneisen functions γ_i = (c_{i1}α_a + c_{i2}α_b + c_{i3}α_c) V_m / C_V for i=a,b,c, and the volume Grüneisen function γ as the weighted average of γ_i with the linear compressibilities. Output a CSV file for temperatures T = 300, 350, 400, 450, 500, 550, 600, 650, 700 K, with columns T, gamma_a, gamma_b, gamma_c, gamma_volume.
- Output file: `/app/outputs/step_07_gruneisen_functions.csv`
- Format: csv
- Contract: CSV file with header: T,gamma_a,gamma_b,gamma_c,gamma_volume. Each row contains a temperature (K) and four float values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_04_moments_theta_inf.json`
- `/app/outputs/step_06_anharmonic_coefficients.json`
- `/app/outputs/step_07_gruneisen_functions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_04_moments_theta_inf.json
- path: `/app/outputs/step_04_moments_theta_inf.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Spectral moments and high-temperature Debye temperature; checker compares these values to the paper-reported reference within tolerances.
- schema:
  - `type`: object
  - `required`: `mu2`, `mu4`, `mu6`, `theta_inf`
  - `properties`:
    - `mu2`:
      - `type`: number
      - `unit`: s^-2
    - `mu4`:
      - `type`: number
      - `unit`: s^-4
    - `mu6`:
      - `type`: number
      - `unit`: s^-6
    - `theta_inf`:
      - `type`: number
      - `unit`: K

### step_06_anharmonic_coefficients.json
- path: `/app/outputs/step_06_anharmonic_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Anharmonic coefficients; checker compares to reference values with tolerances.
- schema:
  - `type`: object
  - `required`: `b1`, `b2`
  - `properties`:
    - `b1`:
      - `type`: number
      - `unit`: K^-1
    - `b2`:
      - `type`: number
      - `unit`: K^-2

### step_07_gruneisen_functions.csv
- path: `/app/outputs/step_07_gruneisen_functions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Grüneisen functions at the specified temperatures; checker compares each row to reference values within relative or absolute tolerances.
- schema:
  - `type`: table
  - `required_columns`: `T`, `gamma_a`, `gamma_b`, `gamma_c`, `gamma_volume`
  - `units`:
    - `T`: K
    - `gamma_a`: dimensionless
    - `gamma_b`: dimensionless
    - `gamma_c`: dimensionless
    - `gamma_volume`: dimensionless

Notes: The workflow is compute‑driven; all inputs are published numeric data. The agent fetches the datasets from the references listed in instruction.md (no direct URL required). The checker performs a result‑level compare with the paper‑reported values using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_04_moments_theta_inf.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "mu2",
          "mu4",
          "mu6",
          "theta_inf"
        ],
        "properties": {
          "mu2": {
            "type": "number",
            "unit": "s^-2"
          },
          "mu4": {
            "type": "number",
            "unit": "s^-4"
          },
          "mu6": {
            "type": "number",
            "unit": "s^-6"
          },
          "theta_inf": {
            "type": "number",
            "unit": "K"
          }
        }
      },
      "description": "Spectral moments and high-temperature Debye temperature; checker compares these values to the paper-reported reference within tolerances."
    },
    {
      "file": "step_06_anharmonic_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "b1",
          "b2"
        ],
        "properties": {
          "b1": {
            "type": "number",
            "unit": "K^-1"
          },
          "b2": {
            "type": "number",
            "unit": "K^-2"
          }
        }
      },
      "description": "Anharmonic coefficients; checker compares to reference values with tolerances."
    },
    {
      "file": "step_07_gruneisen_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "gamma_a",
          "gamma_b",
          "gamma_c",
          "gamma_volume"
        ],
        "units": {
          "T": "K",
          "gamma_a": "dimensionless",
          "gamma_b": "dimensionless",
          "gamma_c": "dimensionless",
          "gamma_volume": "dimensionless"
        }
      },
      "description": "Grüneisen functions at the specified temperatures; checker compares each row to reference values within relative or absolute tolerances."
    }
  ],
  "notes": "The workflow is compute‑driven; all inputs are published numeric data. The agent fetches the datasets from the references listed in instruction.md (no direct URL required). The checker performs a result‑level compare with the paper‑reported values using appropriate tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently scores each of the three final output artifacts (spectral moments and Θ∞, anharmonic coefficients, and Grüneisen functions). For each artifact, the checker compares your reported values to reference values obtained from the same input data using the prescribed procedure, applying appropriate tolerances. The individual scores are weighted and combined to produce a total reward in [0,1]. Simply copying a published number is not enough; you must faithfully run the computational workflow and produce artifacts that agree with the reference within the required accuracy.
