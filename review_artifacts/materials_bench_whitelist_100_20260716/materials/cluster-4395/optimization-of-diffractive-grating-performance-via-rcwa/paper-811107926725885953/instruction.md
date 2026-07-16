# Analytical optimization of grating coupler period and fill-factor for TE and TM polarizations on SOI platform

## Problem background
Efficient coupling between silicon-on-insulator (SOI) submicron waveguides and single-mode optical fibers remains a critical challenge in silicon photonics. Grating couplers, which are periodic structures that diffract light between the waveguide and free space, offer a compact solution, but their performance depends critically on the grating period and fill‑factor. Traditionally, finding the optimal values of these parameters to maximize coupling efficiency requires time‑consuming numerical simulations. This task implements an analytical method that directly computes the optimal period and fill‑factor for a uniform grating coupler on an SOI platform, for both TE and TM polarizations at operational wavelengths of 1.55 μm and 1.31 μm. The analytical design is then verified by a 2D electromagnetic simulation to assess the resulting coupling efficiency.

## Approach
The core idea is that the optimal effective refractive index of the grating region, which determines the period through the Bragg condition, is not the average of the etched and unetched waveguide indices at the operational wavelength, but rather the average evaluated at a slightly shorter wavelength. For TE polarization the required wavelength shift is 36 nm; for TM polarization it is twice that, 72 nm. By first computing the effective refractive indices of the etched (70 nm Si) and unetched (220 nm Si) slab waveguide with a SiO₂ cladding at the shifted wavelength, one obtains a corrected grating effective index, which leads directly to the optimal period. The fill‑factor is then derived from those effective indices using a linear relation. Once the period and fill‑factor are determined, the grating coupler is simulated with a 2D electromagnetic solver (e.g., RCWA) to obtain the coupling efficiency as a function of wavelength. The workflow thus consists of four stages: (1) solving the slab waveguide modes at the shifted wavelengths, (2) applying the analytical formulas to obtain the four optimal parameter sets, (3) performing RCWA simulations to generate coupling efficiency spectra, and (4) extracting the peak efficiency and the wavelength at which it occurs for each design.

## Reproduction target
For both TE and TM polarizations at the two operational wavelengths (1.55 μm and 1.31 μm), compute the optimal grating period and fill‑factor using the analytical method described above. Then, for each of the four resulting grating designs, run a 2D electromagnetic simulation (RCWA) sweeping the input wavelength over the relevant range to obtain the coupling efficiency spectrum. From these spectra, extract the peak coupling efficiency and the center wavelength (wavelength of maximum efficiency). The objective is to demonstrate that the analytically designed gratings achieve high coupling efficiency, with the peak occurring close to the intended operational wavelength.

## Assets

- numpy: pip install numpy
- scipy: pip install scipy
- rcwa (or alternative grating simulation tool): pip install rcwa

## Workflow steps

### Step 1: Slab waveguide mode solving
- Role: process
- Action: Compute effective refractive indices for the etched (70 nm Si) and unetched (220 nm Si) slab waveguide with SiO2 cladding for TE and TM polarizations at the shifted wavelengths (λ_op – 36 nm for TE, λ_op – 72 nm for TM) for λ_op = 1.55 μm and 1.31 μm. Use appropriate material refractive indices at those wavelengths.
- Evidence: none

### Step 2: Analytical grating design
- Role: scored
- Action: For each polarization (TE, TM) and operational wavelength (1.55 μm, 1.31 μm), compute the optimal grating period using the Bragg condition and the optimal fill-factor using the effective index relationships. Write the four design points to a CSV file.
- Output file: `/app/outputs/step_01_design_parameters.csv`
- Format: csv
- Contract: Columns: polarization (string, 'TE' or 'TM'), wavelength_um (float), period_nm (float), fill_factor (float). Four rows: TE 1.55, TE 1.31, TM 1.55, TM 1.31.
- Scoring: scored by hidden verifier

### Step 3: Grating coupler simulation
- Role: scored (load-bearing)
- Action: For each of the four grating designs (using the period and fill-factor from step 2, etch depth 70 nm, SiO2 cladding, incidence angle 10°), run a 2D electromagnetic simulation (e.g., RCWA) sweeping the input wavelength over a range around the operational wavelength (e.g., 1.4–1.7 μm for 1.55 μm, 1.2–1.4 μm for 1.31 μm) and record the coupling efficiency into the fundamental waveguide mode. Concatenate the wavelength-dependent spectra into one CSV.
- Output file: `/app/outputs/step_02_efficiency_spectra.csv`
- Format: csv
- Contract: Columns: polarization (string), wavelength_nm (float), coupling_efficiency (float). Contains spectra for the four designs concatenated.
- Scoring: scored by hidden verifier

### Step 4: Result summary
- Role: scored
- Action: From the efficiency spectra, extract the peak coupling efficiency and the center wavelength (wavelength at the peak) for each design. Output a JSON file with these metrics for all four configurations.
- Output file: `/app/outputs/step_03_results.json`
- Format: json
- Contract: JSON object with keys 'TE_1550', 'TE_1310', 'TM_1550', 'TM_1310'. Each value is an object with float fields 'peak_efficiency' and 'center_wavelength_nm'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_design_parameters.csv`
- `/app/outputs/step_02_efficiency_spectra.csv`
- `/app/outputs/step_03_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_design_parameters.csv
- path: `/app/outputs/step_01_design_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Analytically computed optimal grating period and fill-factor for TE and TM polarizations at 1.55 and 1.31 μm. The checker compares these to hidden paper gold values with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `polarization`, `wavelength_um`, `period_nm`, `fill_factor`

### step_02_efficiency_spectra.csv
- path: `/app/outputs/step_02_efficiency_spectra.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: RCWA-simulated coupling efficiency as a function of wavelength for the four designs. The checker recomputes peak efficiency and center wavelength from these spectra and compares them to paper simulation values (threshold_or_better for efficiency, ±20 nm for center wavelength).
- schema:
  - `type`: table
  - `required_columns`: `polarization`, `wavelength_nm`, `coupling_efficiency`

### step_03_results.json
- path: `/app/outputs/step_03_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: The agent's extracted peak efficiency and center wavelength for each design. The checker cross-checks consistency with step_02 and verifies structural correctness.
- schema:
  - `type`: object
  - `required_keys`: `TE_1550`, `TE_1310`, `TM_1550`, `TM_1310`
  - `value_schema`:
    - `type`: object
    - `required_fields`: `peak_efficiency`, `center_wavelength_nm`
    - `field_types`:
      - `peak_efficiency`: float
      - `center_wavelength_nm`: float

Notes: The analytical design uses the pre-existing wavelength shift factors Δλ̅_TE = 36 nm and Δλ̅_TM = 72 nm; the agent does not need to re-derive these. The RCWA simulation is a faithful substitute for the BPM used in the paper. The experimental fabrication and characterization are out of scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_design_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "polarization",
          "wavelength_um",
          "period_nm",
          "fill_factor"
        ]
      },
      "description": "Analytically computed optimal grating period and fill-factor for TE and TM polarizations at 1.55 and 1.31 μm. The checker compares these to hidden paper gold values with tolerances."
    },
    {
      "file": "step_02_efficiency_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "polarization",
          "wavelength_nm",
          "coupling_efficiency"
        ]
      },
      "description": "RCWA-simulated coupling efficiency as a function of wavelength for the four designs. The checker recomputes peak efficiency and center wavelength from these spectra and compares them to paper simulation values (threshold_or_better for efficiency, ±20 nm for center wavelength)."
    },
    {
      "file": "step_03_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required_keys": [
          "TE_1550",
          "TE_1310",
          "TM_1550",
          "TM_1310"
        ],
        "value_schema": {
          "type": "object",
          "required_fields": [
            "peak_efficiency",
            "center_wavelength_nm"
          ],
          "field_types": {
            "peak_efficiency": "float",
            "center_wavelength_nm": "float"
          }
        }
      },
      "description": "The agent's extracted peak efficiency and center wavelength for each design. The checker cross-checks consistency with step_02 and verifies structural correctness."
    }
  ],
  "notes": "The analytical design uses the pre-existing wavelength shift factors Δλ̅_TE = 36 nm and Δλ̅_TM = 72 nm; the agent does not need to re-derive these. The RCWA simulation is a faithful substitute for the BPM used in the paper. The experimental fabrication and characterization are out of scope."
}
```

## How you are scored
A hidden verifier independently evaluates each of the three scored output files: (i) the design parameters (period and fill‑factor) are compared against a reference with suitable tolerances; (ii) the coupling efficiency spectra are used to recompute the peak efficiency and center wavelength for each configuration, and those values are assessed against performance criteria (meeting a threshold and alignment with the target wavelength); (iii) the summary JSON file is checked for internal consistency with the spectra. The overall reward is a weighted combination of these three components, giving substantial weight to both the accuracy of the analytically derived parameters and the simulated coupling performance. Reporting numbers without genuine computation will not pass the verification.
