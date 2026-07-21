# D-Shaped PCF SPR Sensor Temperature Effects Simulation

## Problem background
Surface plasmon resonance (SPR) sensors based on side-polished D-shaped photonic crystal fibers (PCF) offer a practical route for chemical and biological sensing by enabling direct coating of the metal film on the exposed core. However, ambient temperature fluctuations can affect sensor performance through thermal changes in the silica refractive index, the metal's dielectric function, and the film thickness. A comprehensive temperature-dependent theoretical model that couples these effects is needed to understand and predict how temperature influences the resonance wavelength and peak loss of such sensors. This task reproduces the core computational investigation: implementing the temperature-dependent material models and running full-vectorial FEM simulations to compute the resonance wavelength and confinement loss of the y-polarized core mode under a range of temperatures, analyte refractive indices, and key structural variations.

## Sensor geometry (derived from the commercial PCF ESM-12)
The PCF cladding consists of **six layers of air holes arranged in a hexagonal lattice**. The fiber is side-polished to a depth \(h\), defined as the distance from the fiber core to the polished surface. A thin gold film is coated onto the polished flat surface to enable SPR excitation. The baseline geometric parameters are:

- Lattice pitch (center-to-center hole distance): \(\Lambda = 7.9\,\mu\text{m}\)
- Air hole diameter: \(d = 3.9\,\mu\text{m}\) (duty ratio \(d/\Lambda = 0.5\))
- Polishing depth: \(h = 0.5\,\Lambda = 3.95\,\mu\text{m}\)
- Gold film thickness at room temperature: \(d_0 = 35\,\text{nm}\)

## Material models (exact equations and parameters from the paper)

### 1. Fused silica refractive index – Sellmeier equation with temperature dependence

The temperature-dependent refractive index of fused silica follows:

\[
\begin{aligned}
n_{\text{silica}}^{2} &=1.31552+0.690754 \times 10^{-5} T \\
+& \frac{\left(0.788404+0.235835 \times 10^{-4} T\right) \lambda^{2}}{\lambda^{2}-\left(0.0110199+0.584758 \times 10^{-6} T\right)} \\
+& \frac{\left(0.91316+0.548368 \times 10^{-6} T\right) \lambda^{2}}{\lambda^{2}-100}
\end{aligned}
\]

- \(\lambda\): wavelength in **micrometers** (μm)
- \(T\): temperature in degrees Celsius (°C)

### 2. Gold dielectric function – Drude model with temperature corrections

The complex permittivity of gold is given by the Drude model:

\[
\varepsilon(\omega)=\varepsilon_{1}+i\varepsilon_{2}=\varepsilon_{\infty}-\frac{\omega_{p}^{2}}{\omega(\omega+i\omega_{c})}
\]

- \(\omega\): angular frequency (rad/s)
- \(\varepsilon_{\infty}\): high-frequency dielectric constant
- \(\omega_p\): plasma frequency (rad/s)
- \(\omega_c\): collision frequency (rad/s)

**Temperature-dependent plasma frequency:**

\[
\omega_{p}=\omega_{p0}\exp\!\left(-\frac{T-T_{0}}{2}\times 3\gamma\right)
\]

- \(T\): temperature in Kelvin (K)
- \(T_0\): reference temperature (298 K)
- \(\gamma\): volumetric thermal expansion coefficient of gold (K⁻¹)

**Temperature-dependent collision frequency:**

\[
\omega_{c}=\omega_{ce}+\omega_{cp}
\]

**Electron-electron scattering:**

\[
\omega_{ce}(T)=\frac{1}{6}\pi^{4}\frac{\Gamma\Delta}{\hbar E_{F}}\left[(k_{B}T)^{2}+\left(\frac{\hbar\omega}{4\pi^{2}}\right)^{2}\right]
\]

- \(\hbar = h/(2\pi)\): reduced Planck constant
- \(E_F\): Fermi energy of gold (eV)
- \(k_B\): Boltzmann constant
- \(\Gamma\Delta\) is the product of two constants from Lawrence’s electron scattering model. In the paper’s Table 1 this product is taken as exactly **1.0** (dimensionless) for gold. Use \(\Gamma\Delta = 1.0\) in all calculations.

**Phonon-electron scattering:**

\[
\omega_{cp}(T)=\omega_{p}(T_{0})\left[\frac{2}{5}+4\left(\frac{T}{T_{D}}\right)^{5}\int_{0}^{T_{D}/T}\frac{z^{4}}{e^{z}-1}\,dz\right]
\]

- \(T_D\): Debye temperature of gold (K)

### 3. Gold film thickness – thermal expansion correction

\[
d_{Au}=d_{0}\left[1+\gamma\,\frac{1+\mu}{1-\mu}\,(T-T_{0})\right]
\]

- \(d_0\): film thickness at room temperature (298 K) → **35 nm** for the baseline sensor
- \(\mu\): Poisson’s ratio of gold
- The factor \(\gamma\frac{1+\mu}{1-\mu}\) is the corrected thermal expansion coefficient for a thin film.

### Table 1 parameters (for gold)

Use the following values in all calculations:

| Parameter | Symbol | Value | Units |
|-----------|--------|-------|-------|
| High-frequency dielectric constant | \(\varepsilon_{\infty}\) | 1.0 | dimensionless |
| Plasma frequency at \(T_0\) | \(\omega_{p0}\) | \(1.3673 \times 10^{16}\) | rad/s |
| Volumetric thermal expansion coefficient | \(\gamma\) | \(42.6 \times 10^{-6}\) | K⁻¹ |
| Reference temperature | \(T_0\) | 298 | K |
| Debye temperature | \(T_D\) | 170 | K |
| Fermi energy | \(E_F\) | 5.53 | eV |
| Poisson’s ratio | \(\mu\) | 0.44 | dimensionless |
| Film thickness at \(T_0\) | \(d_0\) | 35 | nm |
| \(\Gamma\Delta\) product (electron‑electron scattering) | \(\Gamma\Delta\) | 1.0 | dimensionless |

**Physical constants** (standard values):
- Planck constant \(h = 6.62607015 \times 10^{-34}\) J·s
- Reduced Planck constant \(\hbar = 1.0545718 \times 10^{-34}\) J·s
- Boltzmann constant \(k_B = 1.380649 \times 10^{-23}\) J/K
- 1 eV = \(1.602176634 \times 10^{-19}\) J

## Approach
Implement the three temperature-dependent material models described above. Set up the baseline side-polished D-shaped PCF geometry according to the “Sensor geometry” section (six-layer hexagonal air-hole cladding, lattice pitch Λ=7.9 μm, air hole diameter d=3.9 μm, polishing depth h=0.5Λ, gold thickness 35 nm, analyte RI=1.35). Using a full-vectorial FEM solver capable of complex-valued eigenmode analysis and cylindrical PML, sweep over wavelength to extract the complex effective index of the y-polarized fundamental core mode and compute the confinement loss (dB/cm) via

\[
\text{Loss (dB/cm)} = 8.686 \times \frac{2\pi}{\lambda}\;\text{Im}(n_{\text{eff}})
\]

where \(\lambda\) is in centimeters. From the loss spectrum, identify the resonance wavelength (wavelength of peak loss) and the peak loss value. This baseline analysis is performed at three temperatures (270, 320, 370 K). Then, keeping the baseline geometry, investigate the dependence of the peak loss on the analyte RI (1.33–1.36) at those three temperatures, as well as the peak loss dependence on temperature (270–370 K) at a fixed RI=1.35. Finally, assess the influence of duty ratio (d/Λ=0.4, 0.6) and lattice pitch (Λ=5 μm, 10 μm) by computing the resonance wavelength and peak loss for each configuration at the three temperatures.

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
- Action: Implement the temperature-dependent material models for fused silica and gold as described in the “Material models” section above. Code the Sellmeier equation, the Drude model with temperature-corrected plasma and collision frequencies, and the thermal expansion correction for film thickness. Use exactly the parameter values listed in the Table 1 above.
- Evidence: none

### Step 2: Baseline FEM simulation
- Role: scored (load-bearing)
- Action: Set up the side-polished D-shaped PCF geometry as described in “Sensor geometry”: six-layer hexagonal air-hole cladding, lattice pitch Λ = 7.9 μm, air hole diameter d = 3.9 μm (d/Λ = 0.5), polishing depth h = 0.5Λ = 3.95 μm, gold film thickness 35 nm, analyte refractive index n_a = 1.35. Using the implemented temperature-dependent models and a full-vectorial FEM solver, compute the complex effective indices of the y-polarized fundamental core mode and SPP mode over a wavelength range (e.g., 500–800 nm) at three temperatures: T = 270 K, 320 K, 370 K. For each temperature, calculate the confinement loss (dB/cm) from the imaginary part of the effective index, identify the resonance wavelength (wavelength of peak loss), and record the peak loss value. **Important checks**: The resonance wavelength should fall within 500–800 nm and must increase monotonically with temperature (red-shift). Ensure your output respects these properties.
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
- Action: For the same geometry and analyte RI=1.35, vary the temperature from 270 K to 370 K in steps of 10 K. At each temperature, run the FEM simulation and record the peak loss (dB/cm). **Expected behavior**: The peak loss should decrease approximately linearly with temperature. Your results should exhibit a high coefficient of determination (R² > 0.95) and the absolute value of the slope should be within 0.05–0.25 dB/(cm·K) (i.e., the peak loss decreases with increasing temperature).
- Output file: `/app/outputs/temp_dependence.csv`
- Format: csv
- Contract: temperature_K: float, peak_loss_dB_per_cm: float (rows for temperatures from 270 K to 370 K in 10 K steps)
- Scoring: scored by hidden verifier

### Step 5: Structural parameter variation
- Role: scored
- Action: Investigate the effect of duty ratio and lattice pitch on the resonance wavelength and peak loss. For duty ratio variation, set Λ=7.9 μm, vary d/Λ to 0.4 and 0.6 (i.e., d=3.16 μm and 4.74 μm), keeping other parameters as baseline. For lattice pitch variation, set Λ=5 μm and 10 μm with d/Λ=0.5, keeping other parameters as baseline. For each configuration (duty ratio and lattice pitch), compute the resonance wavelength and peak loss at temperatures T=270, 320, 370 K. **Expected qualitative trends from the paper**: (i) The resonance wavelength is nearly unaffected by these structural changes – its variation across all configurations at a given temperature should be less than 5 nm. (ii) The peak loss ordering must satisfy: for duty ratio, the peak loss at 0.6 is larger than at 0.4; for lattice pitch, the peak loss at 5 μm is larger than at 10 μm. Verify that your results conform to these expectations.
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

Notes: The agent must implement the full temperature-dependent material models (Sellmeier for fused silica, Drude for gold with temperature-corrected plasma and collision frequencies, and film thickness correction) using the exact parameters provided above. An open-source or proprietary full-vectorial FEM solver with cylindrical PML must be used to compute complex effective indices and confinement losses. The output values are compared to hidden reference values derived from the paper’s reported simulation results.

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