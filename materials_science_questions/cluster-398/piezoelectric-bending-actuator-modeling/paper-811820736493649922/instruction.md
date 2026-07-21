# Traveling-Wave Piezoelectric Device Parameter Calculation

## Problem background
A converter-display device for opto-electronic imaging can be realized using a one-dimensional array of micromechanical strip waveguides. Each strip is attached to a piezoelectric transducer; applying an AC voltage excites traveling flexural waves in the strip, producing a periodic surface relief that acts as a tunable diffraction grating. The key design parameters—piezoelectric element thickness, excitation voltage, wave amplitude, flexural wavelength, diffraction angle, and diffraction efficiency—can be determined analytically from the material properties of the piezoceramic and strip, together with the excitation frequency, electric field, and light wavelength.

## Approach
The approach models the piezoelectric element as a thickness-mode resonator that deforms under an applied electric field, with the strain amplitude determined by the piezoelectric modulus and voltage. This deformation drives one end of a free-standing strip waveguide, launching a traveling flexural wave whose wavelength follows from thin-plate elasticity theory. The resulting sinusoidal surface relief forms a phase diffraction grating; diffraction theory then relates the relief amplitude to the diffraction angle and efficiency under monochromatic illumination. The computation proceeds from the given constants without requiring external data or iterative simulation; all needed expressions are evaluated directly.

## Reproduction target
Given the material constants (piezoceramic PCB-590: c_p = 2.8e3 m/s, d33 = 500e-12 C/N; rhenium strip: E = 2e11 Pa, ρ = 21e3 kg/m³, σ ≈ 0.3, thickness h = 0.2e-6 m), excitation frequency f0 = 5e6 Hz, electric field E0 = 3e5 V/m, and light wavelength λ = 0.5e-6 m, compute the six device parameters (piezoelectric element thickness, AC voltage amplitude, wave amplitude, flexural wavelength, diffraction angle, and diffraction efficiency) and write them to a single JSON file as specified in the workflow steps. All constants are provided in the instruction; no fetching of external datasets is required.

## Assets

- Python 3 standard library: python3

## Workflow steps

### Step 1: Prepare material constants and operating conditions
- Role: process
- Action: Record the given material constants and operating conditions from the problem statement: piezoceramic PCB-590 (c_p = 2.8e3 m/s, d33 = 500e-12 C/N), rhenium strip (E = 2e11 Pa, ρ = 21e3 kg/m³, σ ≈ 0.3, thickness h = 0.2e-6 m), excitation frequency f0 = 5e6 Hz, electric field E0 = 3e5 V/m, light wavelength λ = 0.5e-6 m.
- Evidence: none

### Step 2: Compute device performance parameters
- Role: scored (load-bearing)
- Action: Using the recorded constants, compute the six parameters: piezoelectric element thickness ℓ (in micrometers), AC voltage amplitude U0 (in volts), wave amplitude Δℓ (in micrometers), flexural wavelength Λ (in meters), diffraction angle θ (in radians), and diffraction efficiency (dimensionless). Use the formulas: ℓ = c_p/(4*f0); U0 = E0 * ℓ; Δℓ = d33 * U0; Λ = sqrt((2πh/f0) * sqrt(E/(12ρ(1-σ^2)))); θ = λ/Λ; diffraction efficiency = (2π*Δℓ/λ * cos(θ))^2. Write the results as a JSON object with the keys: piezo_thickness_um, wave_amplitude_um, excitation_voltage_V, flexural_wavelength_m, diffraction_angle_rad, diffraction_efficiency.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: { piezo_thickness_um: number (micrometers), wave_amplitude_um: number (micrometers), excitation_voltage_V: number (volts), flexural_wavelength_m: number (meters), diffraction_angle_rad: number (radians), diffraction_efficiency: number (dimensionless) }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.json
- path: `/app/outputs/computed_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed device parameters from material properties and operating conditions.
- schema:
  - `type`: object
  - `required`: `piezo_thickness_um`, `wave_amplitude_um`, `excitation_voltage_V`, `flexural_wavelength_m`, `diffraction_angle_rad`, `diffraction_efficiency`
  - `properties`:
    - `piezo_thickness_um`:
      - `type`: number
      - `description`: Piezoelectric element thickness in micrometers
    - `wave_amplitude_um`:
      - `type`: number
      - `description`: Wave amplitude in micrometers
    - `excitation_voltage_V`:
      - `type`: number
      - `description`: AC voltage amplitude in volts
    - `flexural_wavelength_m`:
      - `type`: number
      - `description`: Flexural wavelength in meters
    - `diffraction_angle_rad`:
      - `type`: number
      - `description`: Diffraction angle in radians
    - `diffraction_efficiency`:
      - `type`: number
      - `description`: Diffraction efficiency (dimensionless)

Notes: All six values must be computed and reported; the checker compares to the paper's reported values within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "piezo_thickness_um",
          "wave_amplitude_um",
          "excitation_voltage_V",
          "flexural_wavelength_m",
          "diffraction_angle_rad",
          "diffraction_efficiency"
        ],
        "properties": {
          "piezo_thickness_um": {
            "type": "number",
            "description": "Piezoelectric element thickness in micrometers"
          },
          "wave_amplitude_um": {
            "type": "number",
            "description": "Wave amplitude in micrometers"
          },
          "excitation_voltage_V": {
            "type": "number",
            "description": "AC voltage amplitude in volts"
          },
          "flexural_wavelength_m": {
            "type": "number",
            "description": "Flexural wavelength in meters"
          },
          "diffraction_angle_rad": {
            "type": "number",
            "description": "Diffraction angle in radians"
          },
          "diffraction_efficiency": {
            "type": "number",
            "description": "Diffraction efficiency (dimensionless)"
          }
        }
      },
      "description": "Computed device parameters from material properties and operating conditions."
    }
  ],
  "notes": "All six values must be computed and reported; the checker compares to the paper's reported values within a tolerance."
}
```

## How you are scored
A hidden verifier will read the JSON file you produce and compare each of the six fields against independently established reference values. Each field carries equal weight. The verifier checks that your computed numbers fall within a reasonable tolerance of the reference; you do not need to know the tolerance values, but you should aim for accurate computation using the provided constants and formulas. The final reward is the fraction of fields that pass the comparison.
