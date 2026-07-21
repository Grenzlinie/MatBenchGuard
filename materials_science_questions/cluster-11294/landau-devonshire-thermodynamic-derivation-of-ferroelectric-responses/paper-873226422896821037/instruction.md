# Voltage-Tunable Lumped Element Model of a Square Tensioned Membrane

## Problem background
Adaptive acoustic liners can tune their absorption frequency, but conventional designs often rely on moving parts or bias flow adding weight and complexity. Certain compliant, voltage-tunable membranes offer an alternative that can be integrated into an acoustic liner as a tunable element. This task reproduces a lumped element model of a square membrane under biaxial prestretch and uniform pressure loading, with a voltage-dependent in‑plane stress. The model predicts the static displacement, the resonance frequency, and the shift of resonance frequency with applied DC voltage. All material constants, geometry, and prestretch values are given explicitly below; your job is to implement the computational pipeline and produce the key predictions for two prestretch conditions.

## Physical parameters (all values provided)

### Membrane geometry and density
- Side length: b = 0.0254 m (square membrane)
- Initial thickness: h₀ = 100 µm = 100 × 10⁻⁶ m
- Membrane density: ρ = 1000 kg/m³
- Air density (for radiation mass): ρ_air = 1.204 kg/m³
- Vacuum permittivity: ε₀ = 8.854 × 10⁻¹² F/m

### Electrode parameters
- Electrode density: ρ_E = 1010 kg/m³
- Total electrode thickness: t_elec = 25 µm = 25 × 10⁻⁶ m
- Effective relative permittivity (linear fit): ε_r(λ) = −0.28 λ + 2.76

### Yeoh hyperelastic material constants (Elastosil Film 2030)
- C₁₀ = 180.7 kPa
- C₂₀ = −16.7 kPa
- C₃₀ = 6.6 kPa

## Approach
The membrane is modeled as a thin, tensioned square diaphragm with pinned edges. The initial in‑plane prestress is computed from the biaxial prestretch using the Yeoh hyperelastic material model with the constants above. A modal series solution for the static deflection under uniform pressure is used to derive lumped acoustic parameters: acoustic compliance from volume displacement, acoustic mass from kinetic energy equivalence, and radiation mass including a recess correction. When electrodes are present, an additional electrode acoustic mass is added based on the electrode density and thickness. The fundamental resonance frequency follows from these lumped elements. The application of a DC voltage across the thickness reduces the in‑plane stress via the electrostrictive pressure, which depends on the relative permittivity. The reduced stress updates the acoustic compliance, leading to a voltage‑dependent shift of the resonance frequency. The resulting predictions are computed for prestretch values of 1.15 and 1.38 and, when applicable, for voltages from 0 to 5 kV.

## Static deflection series
The dimensionless static deflection of a pinned square membrane under uniform pressure \(q_0\) is given by the double series (only odd indices \(m,n=1,3,5,\ldots\)):

\[
\hat{\delta}(\hat{x},\hat{y}) = \frac{16}{\pi^{4}} \sum_{m=1,3,5,\ldots}^{\infty} \sum_{n=1,3,5,\ldots}^{\infty}
\frac{\sin(m\pi \hat{x})\,\sin(n\pi \hat{y})}{m\,n\,(m^{2}+n^{2})},
\]

where the normalised coordinates are \(\hat{x}=x/b\) and \(\hat{y}=y/b\) (the membrane occupies \(x\in[0,b]\), \(y\in[0,b]\), therefore the centre is at \(\hat{x}=0.5,\;\hat{y}=0.5\)).  
The physical (dimensional) displacement is recovered by

\[
\delta(\hat{x},\hat{y}) = \frac{q_{0}\,b^{2}}{\sigma\,h}\; \hat{\delta}(\hat{x},\hat{y}),
\]

where \(\sigma\) is the in‑plane stress (Pa), \(h = h_{0}/\lambda^{2}\) is the current thickness after prestretch, and \(b\) is the side length.  
When computing the static centre displacement, the series must be truncated at a sufficiently large number of odd terms (e.g. up to \(m,n\le 51\)) to reach convergence.

## Reproduction target
Compute and output the following quantities:
1. Static centre displacement (in nanometers) for an incident sound pressure level of 80 dB (re 20 µPa, RMS pressure 0.2 Pa) at 100 Hz, for each prestretch.
2. Normalized static displacement profile along the centreline (\(\hat{y}=0.5\)) for \(\lambda = 1.38\); report the displacement normalized by its maximum value.
3. Fundamental resonance frequencies (in Hz) for both prestretches, each with and without electrodes.
4. Normalized resonance frequency \(f(V)/f(0)\) as a function of applied voltage from 0 to 5 kV in steps of 0.5 kV, for both prestretches. All frequency calculations must include the total acoustic mass (membrane, radiation, and electrode when present).

## Workflow steps

### Step 1: Compute initial prestress
- Role: process
- Action: For each given biaxial prestretch λ (1.15 and 1.38), compute the first strain invariant I₁ = 2λ² + 1/λ⁴, then the initial in‑plane stress σ₀ = 2(λ² − 1/λ⁴)[C₁₀ + 2C₂₀(I₁−3) + 3C₃₀(I₁−3)²] using the Yeoh constants provided above. Use SI units (Pa).
- Evidence: none

### Step 2: Static centre displacement at 80 dB
- Role: scored
- Action: Using the computed prestress \(\sigma=\sigma_0\) and membrane geometry, calculate the static centre deflection for each prestretch at a uniform pressure \(q_0 = 20\times10^{-6}\times10^{80/20} = 0.2\;\text{Pa}\).  
  Use the modal series formula from the **Static deflection series** section. The centre is at \(\hat{x}=0.5,\;\hat{y}=0.5\). Write the centre displacement in nanometers.  
  Note: The thickness after prestretch is \(h = h_0 / \lambda^2\).
- Output file: `/app/outputs/step_01_center_displacement.csv`
- Format: csv
- Contract: prestretch (float), displacement_nm (float)
- Scoring: scored by hidden verifier

### Step 3: Normalized mode shape along centreline
- Role: scored
- Action: For the prestretch \(\lambda = 1.38\), compute the static displacement profile along the centreline \(\hat{y}=0.5\) for normalised \(x\)-coordinate from 0 to 1. Evaluate the same modal series, normalise by the maximum displacement, and write the normalised \((\hat{x},\ \delta/\delta_{\max})\) pairs.
- Output file: `/app/outputs/step_02_mode_shape.csv`
- Format: csv
- Contract: x_norm (float, 0..1), displacement_norm (float)
- Scoring: scored by hidden verifier

### Step 4: Fundamental resonance frequencies
- Role: scored
- Action: For each prestretch, compute the lumped acoustic parameters:
  - Membrane mass: \(M_{aM} = 1.3785\,\rho\,h / b^{2}\) (with \(h = h_0 / \lambda^{2}\))
  - Compliance: \(C_{aM} = 0.0351\,b^{4} / (\sigma\,h)\)
  - Radiation mass: \(M_{aRad} = 1.486\,b\,\rho_{\!air} / (2\,b^{2}) = 1.486\,\rho_{\!air} / (2\,b)\)
  - Electrode mass (when “with electrodes”): \(M_{aE} = 1.3785\,\rho_{E}\,t_{elec} / b^{2}\)
  Then compute the fundamental resonance frequency \(f = 1 / (2\pi \sqrt{M_{total}\,C_{aM}})\) where \(M_{total} = M_{aM} + M_{aRad} (+ M_{aE}\) if electrodes present).
  Write a row with prestretch, a boolean for electrodes, and the frequency in Hz.  
  **The boolean `with_electrode` must be written as the lowercase string `true` or `false`.**
- Output file: `/app/outputs/step_03_resonance_frequencies.csv`
- Format: csv
- Contract: prestretch (float), with_electrode (bool), frequency_Hz (float)
- Scoring: scored by hidden verifier

### Step 5: Normalized resonance frequency vs voltage
- Role: scored (load‑bearing)
- Action: For each prestretch, compute the effective permittivity \(\varepsilon_r = -0.28\lambda + 2.76\). For voltages from 0 to 5 kV in steps of 0.5 kV, compute the reduced stress \(\sigma(V) = \sigma_0 - \varepsilon_0\,\varepsilon_r\,(\lambda^{2} V / h_0)^{2}\), the corresponding compliance \(C_{aM}(V) = 0.0351\,b^{4} / (\sigma(V)\,h)\) with \(h = h_0 / \lambda^{2}\), and then the resonance frequency \(f(V)\) using the total mass \((M_{aM}+M_{aRad}+M_{aE})\) with electrodes included. Normalize by \(f(0)\) and write the normalized frequency.  
  If \(\sigma(V) \le 0\), set the normalized frequency to 0.
- Output file: `/app/outputs/step_04_voltage_dependence.csv`
- Format: csv
- Contract: prestretch (float), voltage_kV (float), normalized_frequency (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_center_displacement.csv`
- `/app/outputs/step_02_mode_shape.csv`
- `/app/outputs/step_03_resonance_frequencies.csv`
- `/app/outputs/step_04_voltage_dependence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_center_displacement.csv
- path: `/app/outputs/step_01_center_displacement.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Static centre displacement for the two prestretch values at 80 dB.
- schema:
  - `type`: table
  - `required_columns`: `prestretch`, `displacement_nm`
  - `units`:
    - `displacement_nm`: nanometers

### step_02_mode_shape.csv
- path: `/app/outputs/step_02_mode_shape.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Normalized displacement profile along the centreline for λ = 1.38; RMSE against digitized gold curve is computed by the verifier.
- schema:
  - `type`: table
  - `required_columns`: `x_norm`, `displacement_norm`
  - `units`:
    - `x_norm`: dimensionless
    - `displacement_norm`: dimensionless

### step_03_resonance_frequencies.csv
- path: `/app/outputs/step_03_resonance_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Fundamental resonance frequencies with and without electrodes. The column `with_electrode` must contain the lowercase strings `true` or `false`.
- schema:
  - `type`: table
  - `required_columns`: `prestretch`, `with_electrode`, `frequency_Hz`
  - `units`:
    - `frequency_Hz`: Hz

### step_04_voltage_dependence.csv
- path: `/app/outputs/step_04_voltage_dependence.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Normalized resonance frequency versus voltage for both prestretches.
- schema:
  - `type`: table
  - `required_columns`: `prestretch`, `voltage_kV`, `normalized_frequency`
  - `units`:
    - `normalized_frequency`: dimensionless

Notes: All targets are computed from the exact parameters given in this instruction. Tolerances are defined in the hidden grading specification and are not disclosed to the solver. The load-bearing step (voltage_dependence) ensures that the core process steps (prestress, compliance calculation) must have been executed correctly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_center_displacement.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "prestretch",
          "displacement_nm"
        ],
        "units": {
          "displacement_nm": "nanometers"
        }
      },
      "description": "Static centre displacement for the two prestretch values at 80 dB, compared to experimental data with a relative tolerance."
    },
    {
      "file": "step_02_mode_shape.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_norm",
          "displacement_norm"
        ],
        "units": {
          "x_norm": "dimensionless",
          "displacement_norm": "dimensionless"
        }
      },
      "description": "Normalized displacement profile along the centreline for λ=1.38; RMSE against digitized gold curve is computed by the verifier."
    },
    {
      "file": "step_03_resonance_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "prestretch",
          "with_electrode",
          "frequency_Hz"
        ],
        "units": {
          "frequency_Hz": "Hz"
        }
      },
      "description": "Fundamental resonance frequencies with and without electrodes, scored against measured values via relative tolerance. The column 'with_electrode' must contain the lowercase strings 'true' or 'false'."
    },
    {
      "file": "step_04_voltage_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "prestretch",
          "voltage_kV",
          "normalized_frequency"
        ],
        "units": {
          "normalized_frequency": "dimensionless"
        }
      },
      "description": "Normalized resonance frequency versus voltage for both prestretches; absolute tolerance per voltage point is applied against experimental data."
    }
  ],
  "notes": "All targets are compared to experimental measurements from the source paper. Tolerances are defined in the hidden grading specification and are not disclosed to the solver. The load-bearing step (voltage_dependence) ensures that the core process steps (prestress, compliance calculation) must have been executed correctly."
}
```

## How you are scored
A hidden verifier will check each of your four output files independently. For the tabular outputs (centre displacement, resonance frequencies, voltage dependence), the verifier compares your submitted numbers to reference values using appropriate divergence measures. For the mode shape profile, the verifier will compare your normalized curve against an expected shape using a curve similarity metric. Each scored file contributes a specified weight to the overall reward, with the voltage-dependence file (the main actuator prediction) carrying the largest share. The final reward is the weighted sum of the per-file scores. To receive full credit you must genuinely execute the computational workflow and write all required artifacts.