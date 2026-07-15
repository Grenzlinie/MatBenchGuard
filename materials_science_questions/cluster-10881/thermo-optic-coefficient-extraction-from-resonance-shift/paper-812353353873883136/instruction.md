# Computation of FFPI Theoretical Finesse, Effective Reflectance, and Temperature Sensitivity

## Problem background
The fiber‑optic Fabry‑Perot interferometer (FFPI) is a single monomode fiber with high‑reflectance dielectric end faces. Its performance is characterized by an effective finesse, which depends on the end reflectance and the fiber length. When the fiber ends are slightly tilted, the effective reflectance decreases, reducing the observed finesse. Additionally, temperature changes induce a relative phase shift in the fiber, governed by the thermo‑mechanical properties of the composite fiber structure (core/cladding, cushion layer, jacket). Your task is to compute the theoretical finesse for several FFPI configurations, infer the effective reflectance from measured finesse values, and predict the temperature‑induced phase shift sensitivity for jacketed and unjacketed fibers.

## Approach
The theoretical effective finesse ℱ_e is computed from the end reflectance R via the standard Fabry‑Perot relations. First compute the coefficient F = 4R/(1−R)², then the effective finesse is ℱ_e = (π/2) / sin⁻¹(1/√(F+2)).

The five fiber configurations (length L, nominal reflectance R) are:
- L = 0.01 m, R = 0.90
- L = 0.24 m, R = 0.80
- L = 1.00 m, R = 0.80
- L = 10.0 m, R = 0.80
- L = 100 m, R = 0.70

The measured effective finesse values reported for these same physical interferometers (used to extract the effective reflectance) are, respectively: 20, 10, 13, 6, and 3. For each configuration, numerically invert the finesse formula ℱ_e(R) to find the effective end reflectance R_e that matches the measured finesse.

Temperature sensitivity is modeled by treating the fiber as a composite cylinder. The optical phase shift per degree Celsius, S(phase), is given by
S(phase) = (1/n)(∂n/∂T) + (n²/2)[(p₁₁+p₁₂)ν − p₁₂](β − α₁) + β,
where β = Σ(α_i E_i S_i) / Σ(E_i S_i) is the weighted thermal expansion of the fiber. The indices i = 1,2,3 refer to the silica core/cladding, the silicone cushion, and the nylon jacket, respectively. Evaluate S(phase) for the fully jacketed case (all three layers) and for an unjacketed fiber (silica only).

The material constants are:
- Silica: E = 730×10⁸ N/m², S = 0.012 mm², α = 0.004×10⁻⁴/°C
- Silicone: E = 0.01×10⁸ N/m², S = 0.11 mm², α = 2.5×10⁻⁴/°C
- Nylon: E = 5.5×10⁸ N/m², S = 0.52 mm², α = 1×10⁻⁴/°C
- Refractive index n = 1.46, ∂n/∂T = 1.1×10⁻⁵/°C
- Photo‑elastic constants p₁₁ = 0.121, p₁₂ = 0.270
- Poisson’s ratio ν = 0.17

Use these values to compute β and then S(phase) for both jacketed and unjacketed fibers.

## Reproduction target
Produce three output files: (1) a CSV file with the computed theoretical effective finesse for the five configurations; (2) a CSV file with the effective end reflectance obtained by matching the measured finesse to the theoretical curve; (3) a JSON file with the temperature‑induced phase shift sensitivities S(phase) for jacketed and unjacketed fibers. All required constants, configurations, and measured finesse values are given in this instruction. Your computations must follow the described models and produce numeric results that reflect the underlying physics, as evaluated by a hidden checker.

## Assets
No external assets. All necessary constant values, fiber dimensions, expansion coefficients, elastic moduli, refractive index, thermo‑optic and photo‑elastic constants, the list of FFPI configurations, and the measured finesse values are provided directly in the instruction above. No downloads or external data retrieval are required.

## Workflow steps

### Step 1: Compute theoretical effective finesse
- Role: scored
- Action: For each (L,R) pair specified (length L and nominal end reflectance R from Table I), compute F = 4R/(1-R)² and then the theoretical effective finesse ℱ_e = (π/2) / sin⁻¹(1/√(F+2)). Write the results as a CSV.
- Output file: `/app/outputs/finesse.csv`
- Format: csv
- Contract: A CSV table with columns: L (float, meters), R (float, 0-1), theoretical_finesse (float, dimensionless). Five rows.
- Scoring: scored by hidden verifier

### Step 2: Extract effective end reflectance from measured finesse
- Role: scored
- Action: For the same five configurations, given the paper's measured effective finesse values, numerically invert the relation ℱ_e(R) from step_01 to find the effective reflectance R_e that produces the measured finesse. Write the results as a CSV.
- Output file: `/app/outputs/effective_reflectance.csv`
- Format: csv
- Contract: A CSV table with columns: L (float, meters), R_nominal (float), effective_reflectance (float). Five rows.
- Scoring: scored by hidden verifier

### Step 3: Compute temperature-induced phase shift sensitivity
- Role: scored
- Action: Using the composite-cylinder model and the material parameters provided (Young's moduli, cross-sections, expansion coefficients, refractive index, ∂n/∂T, photoelastic constants, Poisson's ratio), compute the temperature-induced relative phase shift sensitivity S(phase) for both jacketed and unjacketed fibers. Evaluate the expression S(phase) = (1/n)(∂n/∂T) + (n²/2)[(p₁₁+p₁₂)ν - p₁₂](β - α₁) + β, with β computed from the weighted expansion of the fiber layers. Output a JSON file.
- Output file: `/app/outputs/temp_sensitivities.json`
- Format: json
- Contract: A JSON object with two keys: jacketed_S_phase (float, unit: 1/°C) and unjacketed_S_phase (float, unit: 1/°C).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/finesse.csv`
- `/app/outputs/effective_reflectance.csv`
- `/app/outputs/temp_sensitivities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### finesse.csv
- path: `/app/outputs/finesse.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Theoretical effective finesse for five FFPI configurations.
- schema:
  - `type`: table
  - `required_columns`: `L`, `R`, `theoretical_finesse`
  - `units`:
    - `L`: meters
    - `R`: dimensionless
    - `theoretical_finesse`: dimensionless

### effective_reflectance.csv
- path: `/app/outputs/effective_reflectance.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Effective end reflectance derived by matching measured finesse to the theoretical curve.
- schema:
  - `type`: table
  - `required_columns`: `L`, `R_nominal`, `effective_reflectance`
  - `units`:
    - `L`: meters
    - `R_nominal`: dimensionless
    - `effective_reflectance`: dimensionless

### temp_sensitivities.json
- path: `/app/outputs/temp_sensitivities.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Temperature-induced phase shift sensitivity for jacketed and unjacketed fibers.
- schema:
  - `type`: object
  - `required`:
    - `jacketed_S_phase`: float (1/°C)
    - `unjacketed_S_phase`: float (1/°C)

Notes: All constants needed for the computations are provided in the instruction. The measured finesse values for the reflectance extraction step are also listed in the instruction. No external data fetching is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "finesse.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "R",
          "theoretical_finesse"
        ],
        "units": {
          "L": "meters",
          "R": "dimensionless",
          "theoretical_finesse": "dimensionless"
        }
      },
      "description": "Theoretical effective finesse for five FFPI configurations."
    },
    {
      "file": "effective_reflectance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "R_nominal",
          "effective_reflectance"
        ],
        "units": {
          "L": "meters",
          "R_nominal": "dimensionless",
          "effective_reflectance": "dimensionless"
        }
      },
      "description": "Effective end reflectance derived by matching measured finesse to the theoretical curve."
    },
    {
      "file": "temp_sensitivities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "jacketed_S_phase": "float (1/°C)",
          "unjacketed_S_phase": "float (1/°C)"
        }
      },
      "description": "Temperature-induced phase shift sensitivity for jacketed and unjacketed fibers."
    }
  ],
  "notes": "All constants needed for the computations are provided in the instruction. The measured finesse values for the reflectance extraction step are also listed in the instruction. No external data fetching is required."
}
```

## How you are scored
Your submitted output files are verified independently by a hidden grading script. For each scored artifact, the checker compares your computed values against reference values derived from the paper’s theoretical analysis. The final reward is a weighted sum of the per‑artifact scores. Accuracy counts—produce results that faithfully reflect the models and inputs described in this instruction. The checker uses hidden tolerances; you should implement the calculations correctly, not just report approximately correct numbers.
