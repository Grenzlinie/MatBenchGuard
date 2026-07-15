# D-Shaped PCF SPR Sensor Temperature Effects Simulation

## Problem background
Surface plasmon resonance (SPR) sensors based on side-polished D-shaped photonic crystal fibers (PCF) offer a practical route for chemical and biological sensing by enabling direct coating of the metal film on the exposed core. However, ambient temperature fluctuations can affect sensor performance through thermal changes in the silica refractive index, the metal's dielectric function, and the film thickness. A comprehensive temperature-dependent theoretical model that couples these effects is needed to understand and predict how temperature influences the resonance wavelength and peak loss of such sensors. This task reproduces the core computational investigation: implementing the temperature-dependent material models and re-running full-vectorial FEM simulations to compute the resonance wavelength and confinement loss of the y-polarized core mode under a range of temperatures, analyte refractive indices, and key structural variations.

## Approach
Implement the three temperature-dependent material models from the work: a Sellmeier equation for fused silica that includes temperature-dependent coefficients, a Drude model for the gold film with temperature-corrected plasma and collision frequencies (incorporating electron-electron and phonon-electron scattering), and a thermal expansion correction for the gold film thickness. Set up the baseline side-polished D-shaped PCF geometry (lattice pitch Λ=7.9 μm, air hole diameter d=3.9 μm, polishing depth h=0.5Λ, gold thickness 35 nm, analyte RI=1.35). Using a full-vectorial FEM solver capable of complex-valued eigenmode analysis and cylindrical PML, sweep over wavelength to extract the complex effective index of the y-polarized fundamental core mode and compute the confinement loss. From the loss spectrum, identify the resonance wavelength (wavelength of peak loss) and the peak loss value. This baseline analysis is performed at three temperatures (270, 320, 370 K). Then, keeping the baseline geometry, investigate the dependence of the peak loss on the analyte RI (1.33–1.36) at those three temperatures, as well as the peak loss dependence on temperature (270–370 K) at a fixed RI=1.35. Finally, assess the influence of duty ratio (d/Λ=0.4, 0.6) and lattice pitch (Λ=5 μm, 10 μm) by computing the resonance wavelength and peak loss for each configuration at the three temperatures.

## Reproduction target
Produce four CSV files:
- `baseline_results.csv`: resonance wavelength and peak loss for the baseline sensor at temperatures 270, 320, and 370 K.
- `ri_dependence.csv`: peak loss as a function of analyte RI (1.33, 1.34, 1.35, 1.36) for each of the three temperatures.
- `temp_dependence.csv`: peak loss as a function of temperature (270 K to 370 K in 10 K steps) at fixed RI=1.35.
- `structural_variation.csv`: resonance wavelength and peak loss for duty ratios 0.4 and 0.6, and for lattice pitches 5 μm and 10 μm, each at temperatures 270, 320, and 370 K.
All files must follow the column schemas specified in the contract below.

## Assets

- Full-vectorial FEM solver: fenics or elmer or similar open-source FEM package; COMSOL Multiphysics (proprietary) is also acceptable

## Workflow steps

### Step 1: Implement temperature-dependent material models
- Role: process
- Action: Implement the temperature-dependent material models for fused silica and gold as described in the paper: (1) Sellmeier equation for fused silica refractive index as a function of wavelength and temperature (Equation 1). (2) Drude model for gold permittivity with temperature-dependent plasma frequency (Equation 3) and collision frequency (Equations 4-6, including electron-electron and phonon-electron scattering). (3) Thermal expansion correction for gold film thickness (Equation 7). Use the parameter values from Table 1 of the paper.
- Evidence: none

### Step 2: Baseline FEM simulation
- Role: scored (load-bearing)
- Action: Set up the side-polished D-shaped PCF geometry with the following parameters: lattice pitch Λ = 7.9 μm, air hole diameter d = 3.9 μm (d/Λ = 0.5), polishing depth h = 0.5Λ = 3.95 μm, gold film thickness 35 nm, analyte refractive index n_a = 1.35. Using the implemented temperature-dependent models and a full-vectorial FEM solver, compute the complex effective indices of the y-polarized fundamental core mode and SPP mode over a wavelength range (e.g., 500–800 nm) at three temperatures: T = 270 K, 320 K, 370 K. For each temperature, calculate the confinement loss (dB/cm) from the imaginary part of the effective index, identify the resonance wavelength (wavelength of peak loss), and record the peak loss value.
- Output file: `/app/outputs/baseline_results.csv`
- Format: csv
- Contract: temperature_K: float, resonance_wavelength_nm: float, peak_loss_dB_per_cm: float (three rows corresponding to T=270, 320, 370 K)
- Scoring: scored by hidden verifier

### Step 3: RI dependence of peak loss
- Role: scored
- Action: Using the same reference geometry (Λ=7.9 μm, d=3.9 μm, h=0.5Λ, dAu=35 nm), vary the analyte RI from 1.33 to 1.36 in steps of 0.01. At each RI and for each temperature T=270, 320, 370 K, run the FEM simulation and record the peak loss (dB/cm) of the y-polarized core mode.
- Output file: `/app/outputs/ri_dependence.csv`
- Format: csv
- Contract: temperature_K: float, ri: float, peak_loss_dB_per_cm: float (12 rows: for T=270,320,370 and ri=1.33,1.34,1.35,1.36)
- Scoring: scored by hidden verifier

### Step 4: Temperature dependence of peak loss
- Role: scored
- Action: For the same geometry and analyte RI=1.35, vary the temperature from 270 K to 370 K in steps of 10 K. At each temperature, run the FEM simulation and record the peak loss (dB/cm).
- Output file: `/app/outputs/temp_dependence.csv`
- Format: csv
- Contract: temperature_K: float, peak_loss_dB_per_cm: float (rows for temperatures from 270 K to 370 K in 10 K steps)
- Scoring: scored by hidden verifier

### Step 5: Structural parameter variation
- Role: scored
- Action: Investigate the effect of duty ratio and lattice pitch on the resonance wavelength and peak loss. For duty ratio variation, set Λ=7.9 μm, vary d/Λ to 0.4 and 0.6 (i.e., d=3.16 μm and 4.74 μm), keeping other parameters as baseline. For lattice pitch variation, set Λ=5 μm and 10 μm with d/Λ=0.5, keeping other parameters as baseline. For each configuration (duty ratio and lattice pitch), compute the resonance wavelength and peak loss at temperatures T=270, 320, 370 K.
- Output file: `/app/outputs/structural_variation.csv`
- Format: csv
- Contract: temperature_K: float, parameter: string (one of 'duty_ratio' or 'lattice_pitch'), parameter_value: float, resonance_wavelength_nm: float, peak_loss_dB_per_cm: float (rows for each combination)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/baseline_results.csv`
- `/app/outputs/ri_dependence.csv`
- `/app/outputs/temp_dependence.csv`
- `/app/outputs/structural_variation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### baseline_results.csv
- path: `/app/outputs/baseline_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Resonance wavelength and peak loss of the y-polarized core mode for the baseline D-shaped PCF SPR sensor at temperatures 270, 320, and 370 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `resonance_wavelength_nm`, `peak_loss_dB_per_cm`
  - `units`:
    - `temperature_K`: K
    - `resonance_wavelength_nm`: nm
    - `peak_loss_dB_per_cm`: dB/cm

### ri_dependence.csv
- path: `/app/outputs/ri_dependence.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Peak loss as a function of analyte RI at temperatures 270, 320, and 370 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `ri`, `peak_loss_dB_per_cm`
  - `units`:
    - `temperature_K`: K
    - `ri`: RIU
    - `peak_loss_dB_per_cm`: dB/cm

### temp_dependence.csv
- path: `/app/outputs/temp_dependence.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Peak loss as a function of temperature for fixed analyte RI=1.35.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `peak_loss_dB_per_cm`
  - `units`:
    - `temperature_K`: K
    - `peak_loss_dB_per_cm`: dB/cm

### structural_variation.csv
- path: `/app/outputs/structural_variation.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Resonance wavelength and peak loss for duty ratio 0.4, 0.6 and lattice pitch 5 µm, 10 µm at temperatures 270, 320, and 370 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `parameter`, `parameter_value`, `resonance_wavelength_nm`, `peak_loss_dB_per_cm`
  - `units`:
    - `temperature_K`: K
    - `parameter`: string
    - `parameter_value`: µm or ratio
    - `resonance_wavelength_nm`: nm
    - `peak_loss_dB_per_cm`: dB/cm

Notes: The agent must implement the full temperature-dependent material models (Sellmeier for fused silica, Drude for gold with temperature-corrected plasma and collision frequencies, and film thickness correction) using the parameters from the paper. An open-source or proprietary full-vectorial FEM solver with cylindrical PML must be used to compute complex effective indices and confinement losses. The output values are compared to hidden reference values derived from the paper’s reported simulation results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "baseline_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "resonance_wavelength_nm",
          "peak_loss_dB_per_cm"
        ],
        "units": {
          "temperature_K": "K",
          "resonance_wavelength_nm": "nm",
          "peak_loss_dB_per_cm": "dB/cm"
        }
      },
      "description": "Resonance wavelength and peak loss of the y-polarized core mode for the baseline D-shaped PCF SPR sensor at temperatures 270, 320, and 370 K."
    },
    {
      "file": "ri_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "ri",
          "peak_loss_dB_per_cm"
        ],
        "units": {
          "temperature_K": "K",
          "ri": "RIU",
          "peak_loss_dB_per_cm": "dB/cm"
        }
      },
      "description": "Peak loss as a function of analyte RI at temperatures 270, 320, and 370 K."
    },
    {
      "file": "temp_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "peak_loss_dB_per_cm"
        ],
        "units": {
          "temperature_K": "K",
          "peak_loss_dB_per_cm": "dB/cm"
        }
      },
      "description": "Peak loss as a function of temperature for fixed analyte RI=1.35."
    },
    {
      "file": "structural_variation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "parameter",
          "parameter_value",
          "resonance_wavelength_nm",
          "peak_loss_dB_per_cm"
        ],
        "units": {
          "temperature_K": "K",
          "parameter": "string",
          "parameter_value": "µm or ratio",
          "resonance_wavelength_nm": "nm",
          "peak_loss_dB_per_cm": "dB/cm"
        }
      },
      "description": "Resonance wavelength and peak loss for duty ratio 0.4, 0.6 and lattice pitch 5 µm, 10 µm at temperatures 270, 320, and 370 K."
    }
  ],
  "notes": "The agent must implement the full temperature-dependent material models (Sellmeier for fused silica, Drude for gold with temperature-corrected plasma and collision frequencies, and film thickness correction) using the parameters from the paper. An open-source or proprietary full-vectorial FEM solver with cylindrical PML must be used to compute complex effective indices and confinement losses. The output values are compared to hidden reference values derived from the paper’s reported simulation results."
}
```

## How you are scored
Each CSV is scored independently by a hidden verifier that compares your submitted values to reference values derived from the original paper. The comparison uses tolerances for resonance wavelength, peak loss, and the linear slopes of the peak loss versus RI and versus temperature. The verifier assigns a score to each stage, and the final reward is a weighted combination of these stage scores. Simply reporting the paper's numbers is not sufficient; the scores reward results that fall within the expected range of a correct re-implementation.
