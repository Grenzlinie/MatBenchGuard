# Reproduce Diffraction Efficiency of a 2D Slanted Grating via RCWA

## Problem background
Diffraction gratings are key components in many planar optical systems, especially in near-eye displays for virtual reality (VR) and augmented reality (AR). Achieving efficient two-dimensional exit pupil expansion requires a grating that can split incident light into two high-efficiency diffraction orders with low polarization dependence. This reproduction task focuses on a 1×2 two-dimensional slanted grating with a double-layer cylindrical nano-structure, designed to deliver high and balanced diffraction efficiency into the (−1,0) and (0,−1) orders while maintaining wide fabrication tolerances. The goal is to compute the diffraction behavior of the optimized grating structure using rigorous coupled-wave analysis (RCWA).

## Approach
The core method is rigorous coupled-wave analysis (RCWA), a numerical technique that solves Maxwell's equations for periodic structures by expanding the electromagnetic fields and permittivity in Fourier series. The grating consists of a double-layer cylindrical array on a substrate: a bottom layer of MgF₂ and a top layer of SiO₂, with air above. The structure is slanted at a prescribed angle and the periods are equal in the x- and y-directions, with the cylinders oriented at a fixed azimuthal angle to ensure polarization insensitivity. Using the exact geometric parameters supplied in the workflow, RCWA simulations will be performed for normal incidence under both TE and TM polarizations. The efficiencies of the (−1,0) and (0,−1) transmitted diffraction orders will be computed. This baseline computation is then extended to wavelength and incident-angle sweeps, as well as systematic tolerance analyses where key geometric parameters (layer thicknesses, grating period, slanted angle, and duty cycle) are varied over specified ranges. All results are recorded as raw diffraction efficiencies in CSV files; no post-processing or optimization is required beyond executing the RCWA sweeps.

## Reproduction target
Produce six CSV files containing the raw RCWA-computed diffraction efficiencies for the grating structure. Each file corresponds to one of the following tasks: (1) single-point efficiencies of the (−1,0) and (0,−1) orders at 450 nm under normal incidence for TE and TM polarizations, including the total efficiency per polarization; (2) efficiencies of the two target orders for wavelengths from 400 to 500 nm (step ≤2 nm) under normal incidence, separately for TE and TM; (3) efficiencies of the target orders for incident polar angles from −5° to 5° (step ≤0.5°) at 450 nm, for both polarizations; (4) a grid sweep of MgF₂ thickness h₁ (280–380 nm) and SiO₂ thickness h₂ (500–570 nm) at 450 nm normal incidence, recording all target-order efficiencies and the total effective efficiency; (5) a grid sweep of grating period d (550–650 nm) and slanted angle α (10°–25°), with other parameters fixed, at 450 nm normal incidence; (6) a sweep of duty cycle f from 0.4 to 0.6 (step ≤0.02) at 450 nm normal incidence. The exact column schemas are specified in the workflow steps. These raw CSVs enable the verifier to extract the wavelength band, angular tolerance, and fabrication windows that satisfy given efficiency thresholds.

## Assets

- RCWA solver (e.g., S4): https://github.com/PhilipVHawk/S4
- Python with numpy, scipy: numpy scipy

## Workflow steps

### Step 1: Efficiency at 450 nm
- Role: scored (load-bearing)
- Action: Run RCWA for the given grating (d=603 nm, h1=330 nm, h2=528 nm, f=0.47, α=20.6°, β=45°) at 450 nm under normal incidence for TE and TM polarizations. Extract diffraction efficiencies of orders (-1,0) and (0,-1), and compute total efficiency per polarization. Write CSV.
- Output file: `/app/outputs/efficiency_at_450nm.csv`
- Format: csv
- Contract: polarization (TE/TM), order ((-1,0)/(0,-1)), efficiency (%), total_efficiency (%). One row per combination, plus optional total-efficiency rows.
- Scoring: scored by hidden verifier

### Step 2: Wavelength sweep
- Role: scored
- Action: Run RCWA for wavelengths from 400 to 500 nm (step ≤2 nm) under normal incidence for TE and TM. Record efficiencies of orders (-1,0) and (0,-1). Write CSV.
- Output file: `/app/outputs/wavelength_sweep.csv`
- Format: csv
- Contract: wavelength_nm, DE_(-1,0)_TE, DE_(0,-1)_TE, DE_(-1,0)_TM, DE_(0,-1)_TM
- Scoring: scored by hidden verifier

### Step 3: Incident angle sweep
- Role: scored
- Action: Run RCWA for incident polar angles from -5° to 5° (step ≤0.5°) at 450 nm for TE and TM. Record efficiencies of orders (-1,0) and (0,-1). Write CSV.
- Output file: `/app/outputs/angle_sweep.csv`
- Format: csv
- Contract: incident_angle_deg, DE_(-1,0)_TE, DE_(0,-1)_TE, DE_(-1,0)_TM, DE_(0,-1)_TM
- Scoring: scored by hidden verifier

### Step 4: Tolerance analysis: layer thicknesses
- Role: scored
- Action: Run RCWA for a grid of MgF2 thickness h1 (280–380 nm, ≤5 nm step) and SiO2 thickness h2 (500–570 nm, ≤5 nm step) at 450 nm normal incidence. Record total effective efficiency and individual order efficiencies. Write CSV.
- Output file: `/app/outputs/tolerance_thickness.csv`
- Format: csv
- Contract: h1_nm, h2_nm, total_eff_TE, total_eff_TM, DE_(-1,0)_TE, DE_(0,-1)_TE, DE_(-1,0)_TM, DE_(0,-1)_TM
- Scoring: scored by hidden verifier

### Step 5: Tolerance analysis: period and slanted angle
- Role: scored
- Action: Run RCWA for a grid of period d (550–650 nm, ≤5 nm step) and slanted angle α (10°–25°, ≤1° step) with other parameters fixed at optimum. Record efficiencies. Write CSV.
- Output file: `/app/outputs/tolerance_period_angle.csv`
- Format: csv
- Contract: period_nm, slanted_angle_deg, DE_(-1,0)_TE, DE_(0,-1)_TE, DE_(-1,0)_TM, DE_(0,-1)_TM
- Scoring: scored by hidden verifier

### Step 6: Tolerance analysis: duty cycle
- Role: scored
- Action: Run RCWA for duty cycle f from 0.4 to 0.6 (step ≤0.02) at 450 nm normal incidence. Record efficiencies. Write CSV.
- Output file: `/app/outputs/tolerance_duty.csv`
- Format: csv
- Contract: duty_cycle, DE_(-1,0)_TE, DE_(0,-1)_TE, DE_(-1,0)_TM, DE_(0,-1)_TM
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/efficiency_at_450nm.csv`
- `/app/outputs/wavelength_sweep.csv`
- `/app/outputs/angle_sweep.csv`
- `/app/outputs/tolerance_thickness.csv`
- `/app/outputs/tolerance_period_angle.csv`
- `/app/outputs/tolerance_duty.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### efficiency_at_450nm.csv
- path: `/app/outputs/efficiency_at_450nm.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Diffraction efficiencies of target orders at 450 nm for TE and TM polarizations.
- schema:
  - `type`: table
  - `required_columns`: `polarization`, `order`, `efficiency`
  - `units`:
    - `efficiency`: %

### wavelength_sweep.csv
- path: `/app/outputs/wavelength_sweep.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Efficiency vs. wavelength sweep (400–500 nm).
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `DE_(-1,0)_TE`, `DE_(0,-1)_TE`, `DE_(-1,0)_TM`, `DE_(0,-1)_TM`
  - `units`:
    - `wavelength_nm`: nm
    - `efficiencies`: %

### angle_sweep.csv
- path: `/app/outputs/angle_sweep.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Efficiency vs. incident polar angle sweep (-5° to 5°).
- schema:
  - `type`: table
  - `required_columns`: `incident_angle_deg`, `DE_(-1,0)_TE`, `DE_(0,-1)_TE`, `DE_(-1,0)_TM`, `DE_(0,-1)_TM`
  - `units`:
    - `incident_angle_deg`: degree
    - `efficiencies`: %

### tolerance_thickness.csv
- path: `/app/outputs/tolerance_thickness.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Tolerance sweep of layer thicknesses (h1 and h2).
- schema:
  - `type`: table
  - `required_columns`: `h1_nm`, `h2_nm`, `total_eff_TE`, `total_eff_TM`, `DE_(-1,0)_TE`, `DE_(0,-1)_TE`, `DE_(-1,0)_TM`, `DE_(0,-1)_TM`
  - `units`:
    - `h1_nm`: nm
    - `h2_nm`: nm
    - `efficiencies`: %

### tolerance_period_angle.csv
- path: `/app/outputs/tolerance_period_angle.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Tolerance sweep of grating period and slanted angle.
- schema:
  - `type`: table
  - `required_columns`: `period_nm`, `slanted_angle_deg`, `DE_(-1,0)_TE`, `DE_(0,-1)_TE`, `DE_(-1,0)_TM`, `DE_(0,-1)_TM`
  - `units`:
    - `period_nm`: nm
    - `slanted_angle_deg`: degree
    - `efficiencies`: %

### tolerance_duty.csv
- path: `/app/outputs/tolerance_duty.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Tolerance sweep of duty cycle.
- schema:
  - `type`: table
  - `required_columns`: `duty_cycle`, `DE_(-1,0)_TE`, `DE_(0,-1)_TE`, `DE_(-1,0)_TM`, `DE_(0,-1)_TM`
  - `units`:
    - `duty_cycle`: dimensionless
    - `efficiencies`: %

Notes: The checker derives tolerance ranges and efficiency thresholds from the raw CSV data and compares them to hidden reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "efficiency_at_450nm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "polarization",
          "order",
          "efficiency"
        ],
        "units": {
          "efficiency": "%"
        }
      },
      "description": "Diffraction efficiencies of target orders at 450 nm for TE and TM polarizations."
    },
    {
      "file": "wavelength_sweep.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "DE_(-1,0)_TE",
          "DE_(0,-1)_TE",
          "DE_(-1,0)_TM",
          "DE_(0,-1)_TM"
        ],
        "units": {
          "wavelength_nm": "nm",
          "efficiencies": "%"
        }
      },
      "description": "Efficiency vs. wavelength sweep (400–500 nm)."
    },
    {
      "file": "angle_sweep.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "incident_angle_deg",
          "DE_(-1,0)_TE",
          "DE_(0,-1)_TE",
          "DE_(-1,0)_TM",
          "DE_(0,-1)_TM"
        ],
        "units": {
          "incident_angle_deg": "degree",
          "efficiencies": "%"
        }
      },
      "description": "Efficiency vs. incident polar angle sweep (-5° to 5°)."
    },
    {
      "file": "tolerance_thickness.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "h1_nm",
          "h2_nm",
          "total_eff_TE",
          "total_eff_TM",
          "DE_(-1,0)_TE",
          "DE_(0,-1)_TE",
          "DE_(-1,0)_TM",
          "DE_(0,-1)_TM"
        ],
        "units": {
          "h1_nm": "nm",
          "h2_nm": "nm",
          "efficiencies": "%"
        }
      },
      "description": "Tolerance sweep of layer thicknesses (h1 and h2)."
    },
    {
      "file": "tolerance_period_angle.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "period_nm",
          "slanted_angle_deg",
          "DE_(-1,0)_TE",
          "DE_(0,-1)_TE",
          "DE_(-1,0)_TM",
          "DE_(0,-1)_TM"
        ],
        "units": {
          "period_nm": "nm",
          "slanted_angle_deg": "degree",
          "efficiencies": "%"
        }
      },
      "description": "Tolerance sweep of grating period and slanted angle."
    },
    {
      "file": "tolerance_duty.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "duty_cycle",
          "DE_(-1,0)_TE",
          "DE_(0,-1)_TE",
          "DE_(-1,0)_TM",
          "DE_(0,-1)_TM"
        ],
        "units": {
          "duty_cycle": "dimensionless",
          "efficiencies": "%"
        }
      },
      "description": "Tolerance sweep of duty cycle."
    }
  ],
  "notes": "The checker derives tolerance ranges and efficiency thresholds from the raw CSV data and compares them to hidden reference values."
}
```

## How you are scored
A hidden verifier processes your six CSV files independently. For each file, the verifier computes one or more summary metrics directly from the raw data: for example, the wavelength range where both (−1,0) and (0,−1) orders exceed a certain efficiency threshold, the incident-angle range meeting another threshold, the combined parameter regions for high total effective efficiency, and the tolerance windows for period, slanted angle, and duty cycle. Each derived metric is compared against a hidden reference value using predefined absolute tolerances. If your computed metric falls within the tolerance, you earn full credit for that stage; otherwise the stage scores zero. The six stages are weighted equally, so the final reward is the average of the six stage scores (a float between 0 and 1). Because the verifier re-derives the summary quantities from your raw simulation outputs, merely reporting the paper’s published numbers without running the RCWA simulations will not pass the checks.
