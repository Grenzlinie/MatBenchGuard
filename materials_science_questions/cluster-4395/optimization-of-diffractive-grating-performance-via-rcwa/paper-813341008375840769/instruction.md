# Conical Grazing-Incidence Diffraction Grating Beamsplitter Simulation

## Problem background
High-efficiency beamsplitters for extreme ultraviolet (EUV) radiation are critical for interferometric plasma diagnostics. Conventional grazing-incidence laminar gratings suffer from strong sensitivity of the 0th‑order suppression to small fabrication variations and from shadowing losses. The present work introduces a beamsplitter based on conical grazing‑incidence diffraction: the incident beam is oriented perpendicular to the grating vector (off‑plane incidence). This mounting symmetrizes the ±1st diffraction orders, and by choosing a sufficiently grazing angle only the −1, 0, and +1 orders can propagate while higher orders become evanescent. A binary grating profile is used, and destructive interference between the field reflected from the substrate and from the grating bars can suppress the 0th order, yielding a nearly perfect 50:50 beamsplitter with two high‑efficiency ±1st‑order output beams and negligible background. The goal is to compute the diffraction efficiencies of such a grating through rigorous coupled‑wave analysis (RCWA) under the conditions reported in the literature.

## Approach
We implement rigorous coupled‑wave analysis (RCWA) for conical diffraction from a binary reflection grating. The grating consists of SiO₂ bars on a silicon substrate, with a 1 nm native SiO₂ layer at the bottom of the grooves. The grating period is 400 nm, and the incident wave is a plane wave at a design wavelength of 25 nm. The complex refractive indices of Si and SiO₂ are obtained from the publicly available Henke optical constants database.

The grating is operated in conical (off‑plane) mounting: the azimuthal angle is zero, meaning the incident wave vector lies perpendicular to the grating vector, while the grazing incidence angle φ₀ is around 85°. This arrangement, combined with an appropriate choice of φ₀, restricts propagating orders to −1, 0, and +1.

The procedure first performs a parameter sweep over the groove depth (roughly 70–140 nm) and the grating duty cycle (fraction of the period occupied by the SiO₂ bars, roughly 0.4–0.7) to find the combination that maximises the ±1st‑order efficiencies while minimising the 0th‑order efficiency. Using the resulting optimal parameters, the diffraction efficiencies are then computed for the −1, 0, and +1 orders under several relevant conditions: a series of experimentally realised duty cycles with their associated groove thicknesses and optimal incidence angles, the dependence on the linear polarisation angle of the incident field, the sensitivity to misalignment of the grazing incidence angle and the conical tilt, the wavelength dependence over 21–29 nm, and the fine tilt dependence of the optimal sample.

## Reproduction target
Use an open‑source RCWA implementation to produce the following six CSV files under `/app/outputs`:

1. `step_01_efficiency_table.csv` — For each of the five duty cycles (48.9%, 52.1%, 54.7%, 56.3%, 59.3%) with the corresponding groove thickness (93.9 nm, 96.6 nm, 100.6 nm, 102.8 nm, 110.5 nm) and the incidence angle that minimises the 0th order for that duty cycle (84.92°, 84.83°, 84.77°, 84.71°, 84.64°), compute the −1, 0, +1 order diffraction efficiencies at λ = 25 nm with s‑polarised light. Also include the optimal global design (duty cycle 54.7%, groove depth 100.6 nm, incidence angle 84.77°). Columns: duty_cycle, groove_depth_nm, incidence_angle_deg, efficiency_m1, efficiency_0, efficiency_p1.

2. `step_02_polarization_dependence.csv` — At the optimal parameters (duty cycle 0.547, groove depth 100.6 nm, φ₀ = 84.77°, λ = 25 nm), compute efficiencies for linear polarisation angles ϑ from 0° to 180° in steps of 10°. Columns: polarization_angle_deg, efficiency_m1, efficiency_0, efficiency_p1.

3. `step_03_angular_error_phi.csv` — Efficiencies versus grazing incidence angle φ₀ from 83.5° to 86.5° in steps of 0.05°, keeping other parameters optimal. Columns: incidence_angle_deg, efficiency_m1, efficiency_0, efficiency_p1.

4. `step_04_angular_error_dpsi.csv` — Efficiencies versus conical tilt angle δψ from −0.5° to +0.5° in steps of 0.025°, with other parameters optimal. Columns: tilt_angle_deg, efficiency_m1, efficiency_0, efficiency_p1.

5. `step_05_wavelength_dependence.csv` — Efficiencies for wavelengths from 21 nm to 29 nm in steps of 0.5 nm, using the Henke optical constants for each wavelength. Columns: wavelength_nm, efficiency_m1, efficiency_0, efficiency_p1.

6. `step_06_tilt_dependence_sample.csv` — Fine tilt dependence for the optimal sample: δψ from −0.2° to +0.2° in steps of 0.01°. Columns: tilt_angle_deg, efficiency_m1, efficiency_0, efficiency_p1.

All efficiencies are fractions in [0,1]. The columns must follow the schemas exactly. The checker will compare your computed efficiencies against the expected RCWA results and verify structural properties such as symmetry, peak locations, and monotonicity.

## Assets

- Henke optical constants for Si and SiO₂: http://henke.lbl.gov/optical_constants/
- RCWA Python package: pip install rcwa

## Workflow steps

### Step 1: Obtain Si and SiO₂ optical constants
- Role: process
- Action: Retrieve or download the complex refractive index (δ, β) for Si and SiO₂ across the EUV range (including λ = 25 nm) from the Henke database (http://henke.lbl.gov/optical_constants/).
- Evidence: `/app/outputs/optical_constants.json`

### Step 2: Set up RCWA solver and grating model
- Role: process
- Action: Implement or configure an open-source RCWA solver for conical diffraction from a binary reflection grating. Define the grating model: period d = 400 nm, SiO₂ bars on a silicon substrate with a 1 nm native SiO₂ layer on the groove bottoms. Use the optical constants obtained in the previous step. The incident medium is vacuum and the exit medium is silicon with the native SiO₂ overlay. The solver must handle s‑polarised and arbitrary linear polarisations and return complex‑amplitude diffraction efficiencies.
- Evidence: `/app/outputs/rcwa_solver_setup.log`

### Step 3: RCWA optimisation of groove depth and duty cycle
- Role: process
- Action: Using the RCWA solver, perform a parameter sweep over groove depth Δt (≈ 70–140 nm) and duty cycle f (≈ 0.4–0.7) for the grating at λ = 25 nm, incidence angle φ₀ = 84.77° and s‑polarised light. Determine the combination that maximises the ±1st‑order efficiencies while minimising the 0th‑order efficiency. Record the efficiency landscape as a CSV.
- Evidence: `/app/outputs/optimization_landscape.csv`

### Step 4: Diffraction efficiencies for the duty‑cycle series and optimal configuration
- Role: scored (load-bearing)
- Action: For each of the five duty cycles (48.9%, 52.1%, 54.7%, 56.3%, 59.3%) use the corresponding groove thickness (93.9 nm, 96.6 nm, 100.6 nm, 102.8 nm, 110.5 nm) and the incidence angle that minimises the 0th order for that duty cycle (84.92°, 84.83°, 84.77°, 84.71°, 84.64°) to compute the -1, 0, +1 order diffraction efficiencies at λ = 25 nm, s‑polarised incidence. Additionally compute the efficiencies for the optimal global design: duty cycle 54.7%, groove depth 100.6 nm, φ₀ = 84.77°. Output a CSV file.
- Output file: `/app/outputs/step_01_efficiency_table.csv`
- Format: csv
- Contract: CSV with columns: duty_cycle (float between 0 and 1), groove_depth_nm (float), incidence_angle_deg (float), efficiency_m1 (float), efficiency_0 (float), efficiency_p1 (float). All efficiencies are fractions in [0,1].
- Scoring: scored by hidden verifier

### Step 5: Polarisation dependence of diffraction efficiencies
- Role: scored
- Action: At the optimal grating parameters (duty cycle 0.547, groove depth 100.6 nm, φ₀ = 84.77°, λ = 25 nm), compute the -1, 0, +1 order efficiencies for linear polarisation angles ϑ from 0° to 180° in steps of 10°. Output a CSV file.
- Output file: `/app/outputs/step_02_polarization_dependence.csv`
- Format: csv
- Contract: CSV with columns: polarization_angle_deg (float), efficiency_m1 (float), efficiency_0 (float), efficiency_p1 (float).
- Scoring: scored by hidden verifier

### Step 6: Angular error budget – incidence angle φ₀
- Role: scored
- Action: For the optimal grating configuration (duty cycle 0.547, groove depth 100.6 nm, λ = 25 nm, s‑polarised, δψ = 0°), compute the -1, 0, +1 order efficiencies while varying φ₀ from 83.5° to 86.5° in steps of 0.05°. Output a CSV file.
- Output file: `/app/outputs/step_03_angular_error_phi.csv`
- Format: csv
- Contract: CSV with columns: incidence_angle_deg (float), efficiency_m1 (float), efficiency_0 (float), efficiency_p1 (float).
- Scoring: scored by hidden verifier

### Step 7: Angular error budget – conical tilt δψ
- Role: scored
- Action: For the optimal grating configuration (duty cycle 0.547, groove depth 100.6 nm, λ = 25 nm, s‑polarised, φ₀ = 84.77°), compute the -1, 0, +1 order efficiencies while varying the conical tilt δψ from -0.5° to +0.5° in steps of 0.025°. Output a CSV file.
- Output file: `/app/outputs/step_04_angular_error_dpsi.csv`
- Format: csv
- Contract: CSV with columns: tilt_angle_deg (float), efficiency_m1 (float), efficiency_0 (float), efficiency_p1 (float).
- Scoring: scored by hidden verifier

### Step 8: Wavelength‑dependent diffraction efficiencies
- Role: scored
- Action: For the optimal grating configuration (duty cycle 0.547, groove depth 100.6 nm, φ₀ = 84.77°, s‑polarised), compute the -1, 0, +1 order efficiencies over the wavelength range 21–29 nm in steps of 0.5 nm. For each wavelength, retrieve the corresponding optical constants for Si and SiO₂ from the Henke database. Output a CSV file.
- Output file: `/app/outputs/step_05_wavelength_dependence.csv`
- Format: csv
- Contract: CSV with columns: wavelength_nm (float), efficiency_m1 (float), efficiency_0 (float), efficiency_p1 (float).
- Scoring: scored by hidden verifier

### Step 9: Tilt‑angle dependence for the specific optimal sample
- Role: scored
- Action: Using the grating parameters for the optimal fabricated sample (duty cycle 0.547, groove depth 100.6 nm, φ₀ = 84.77°, s‑polarised), compute the -1, 0, +1 order efficiencies as a function of conical tilt δψ from -0.2° to +0.2° in steps of 0.01°. Output a CSV file.
- Output file: `/app/outputs/step_06_tilt_dependence_sample.csv`
- Format: csv
- Contract: CSV with columns: tilt_angle_deg (float), efficiency_m1 (float), efficiency_0 (float), efficiency_p1 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_efficiency_table.csv`
- `/app/outputs/step_02_polarization_dependence.csv`
- `/app/outputs/step_03_angular_error_phi.csv`
- `/app/outputs/step_04_angular_error_dpsi.csv`
- `/app/outputs/step_05_wavelength_dependence.csv`
- `/app/outputs/step_06_tilt_dependence_sample.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_efficiency_table.csv
- path: `/app/outputs/step_01_efficiency_table.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed -1, 0, +1 order diffraction efficiencies for the duty-cycle series and the optimal configuration.
- schema:
  - `type`: table
  - `required_columns`: `duty_cycle`, `groove_depth_nm`, `incidence_angle_deg`, `efficiency_m1`, `efficiency_0`, `efficiency_p1`
  - `units`:
    - `duty_cycle`: fraction
    - `groove_depth_nm`: nm
    - `incidence_angle_deg`: degrees
    - `efficiency_m1`: fraction [0,1]
    - `efficiency_0`: fraction [0,1]
    - `efficiency_p1`: fraction [0,1]

### step_02_polarization_dependence.csv
- path: `/app/outputs/step_02_polarization_dependence.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Diffraction efficiencies as a function of incident linear polarisation angle.
- schema:
  - `type`: table
  - `required_columns`: `polarization_angle_deg`, `efficiency_m1`, `efficiency_0`, `efficiency_p1`
  - `units`:
    - `polarization_angle_deg`: degrees
    - `efficiency_m1`: fraction [0,1]
    - `efficiency_0`: fraction [0,1]
    - `efficiency_p1`: fraction [0,1]

### step_03_angular_error_phi.csv
- path: `/app/outputs/step_03_angular_error_phi.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Sensitivity of efficiencies to the grazing incidence angle φ₀.
- schema:
  - `type`: table
  - `required_columns`: `incidence_angle_deg`, `efficiency_m1`, `efficiency_0`, `efficiency_p1`
  - `units`:
    - `incidence_angle_deg`: degrees
    - `efficiency_m1`: fraction [0,1]
    - `efficiency_0`: fraction [0,1]
    - `efficiency_p1`: fraction [0,1]

### step_04_angular_error_dpsi.csv
- path: `/app/outputs/step_04_angular_error_dpsi.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Sensitivity of efficiencies to conical tilt δψ.
- schema:
  - `type`: table
  - `required_columns`: `tilt_angle_deg`, `efficiency_m1`, `efficiency_0`, `efficiency_p1`
  - `units`:
    - `tilt_angle_deg`: degrees
    - `efficiency_m1`: fraction [0,1]
    - `efficiency_0`: fraction [0,1]
    - `efficiency_p1`: fraction [0,1]

### step_05_wavelength_dependence.csv
- path: `/app/outputs/step_05_wavelength_dependence.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Wavelength-dependent diffraction efficiencies in the 21–29 nm range.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `efficiency_m1`, `efficiency_0`, `efficiency_p1`
  - `units`:
    - `wavelength_nm`: nm
    - `efficiency_m1`: fraction [0,1]
    - `efficiency_0`: fraction [0,1]
    - `efficiency_p1`: fraction [0,1]

### step_06_tilt_dependence_sample.csv
- path: `/app/outputs/step_06_tilt_dependence_sample.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: RCWA‑predicted diffraction efficiencies versus conical tilt for the optimal sample.
- schema:
  - `type`: table
  - `required_columns`: `tilt_angle_deg`, `efficiency_m1`, `efficiency_0`, `efficiency_p1`
  - `units`:
    - `tilt_angle_deg`: degrees
    - `efficiency_m1`: fraction [0,1]
    - `efficiency_0`: fraction [0,1]
    - `efficiency_p1`: fraction [0,1]

Notes: All scored artifacts are produced from RCWA simulations using public optical constants and the explicitly stated grating parameters. No experimental data or fabrication steps are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_efficiency_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "duty_cycle",
          "groove_depth_nm",
          "incidence_angle_deg",
          "efficiency_m1",
          "efficiency_0",
          "efficiency_p1"
        ],
        "units": {
          "duty_cycle": "fraction",
          "groove_depth_nm": "nm",
          "incidence_angle_deg": "degrees",
          "efficiency_m1": "fraction [0,1]",
          "efficiency_0": "fraction [0,1]",
          "efficiency_p1": "fraction [0,1]"
        }
      },
      "description": "Computed -1, 0, +1 order diffraction efficiencies for the duty-cycle series and the optimal configuration."
    },
    {
      "file": "step_02_polarization_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "polarization_angle_deg",
          "efficiency_m1",
          "efficiency_0",
          "efficiency_p1"
        ],
        "units": {
          "polarization_angle_deg": "degrees",
          "efficiency_m1": "fraction [0,1]",
          "efficiency_0": "fraction [0,1]",
          "efficiency_p1": "fraction [0,1]"
        }
      },
      "description": "Diffraction efficiencies as a function of incident linear polarisation angle."
    },
    {
      "file": "step_03_angular_error_phi.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "incidence_angle_deg",
          "efficiency_m1",
          "efficiency_0",
          "efficiency_p1"
        ],
        "units": {
          "incidence_angle_deg": "degrees",
          "efficiency_m1": "fraction [0,1]",
          "efficiency_0": "fraction [0,1]",
          "efficiency_p1": "fraction [0,1]"
        }
      },
      "description": "Sensitivity of efficiencies to the grazing incidence angle φ₀."
    },
    {
      "file": "step_04_angular_error_dpsi.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "tilt_angle_deg",
          "efficiency_m1",
          "efficiency_0",
          "efficiency_p1"
        ],
        "units": {
          "tilt_angle_deg": "degrees",
          "efficiency_m1": "fraction [0,1]",
          "efficiency_0": "fraction [0,1]",
          "efficiency_p1": "fraction [0,1]"
        }
      },
      "description": "Sensitivity of efficiencies to conical tilt δψ."
    },
    {
      "file": "step_05_wavelength_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "efficiency_m1",
          "efficiency_0",
          "efficiency_p1"
        ],
        "units": {
          "wavelength_nm": "nm",
          "efficiency_m1": "fraction [0,1]",
          "efficiency_0": "fraction [0,1]",
          "efficiency_p1": "fraction [0,1]"
        }
      },
      "description": "Wavelength-dependent diffraction efficiencies in the 21–29 nm range."
    },
    {
      "file": "step_06_tilt_dependence_sample.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "tilt_angle_deg",
          "efficiency_m1",
          "efficiency_0",
          "efficiency_p1"
        ],
        "units": {
          "tilt_angle_deg": "degrees",
          "efficiency_m1": "fraction [0,1]",
          "efficiency_0": "fraction [0,1]",
          "efficiency_p1": "fraction [0,1]"
        }
      },
      "description": "RCWA‑predicted diffraction efficiencies versus conical tilt for the optimal sample."
    }
  ],
  "notes": "All scored artifacts are produced from RCWA simulations using public optical constants and the explicitly stated grating parameters. No experimental data or fabrication steps are required."
}
```

## How you are scored
A hidden automated verifier will independently score each of the six scored artifacts and combine them into a final reward using predefined weights. The verifier compares your computed diffraction efficiencies against a hidden set of reference values and also checks qualitative behaviours (e.g., symmetry between the ±1 orders, the shape of the polarisation dependence, the position of the 0th‑order minimum when varying φ₀). You must genuinely run the RCWA simulations as described; simply reporting the expected numbers without the corresponding computation will not meet the requirements. The verifier does not run RCWA itself, so your raw computed values must be present in the CSV files. No gold values or tolerances are disclosed publicly; the checker contains all necessary thresholds.
