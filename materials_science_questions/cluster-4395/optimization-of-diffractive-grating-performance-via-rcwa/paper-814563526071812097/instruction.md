# Non-periodic HCG Reflector Beam-Forming Design and Simulation

## Problem background
High-index contrast gratings (HCGs) are subwavelength structures made of high-index bars surrounded by low-index media, capable of high reflectivity and phase control. By varying grating parameters (period and bar width) in a non-periodic arrangement, one can shape the reflected wavefront to steer a beam. This task investigates a non-periodic HCG reflector on a silicon-on-insulator (SOI) substrate, designed to deflect a reflected beam by a target angle while maintaining high reflectivity under TM-polarized light at 1550 nm. The problem is to computationally design the grating geometry and simulate its electromagnetic response to predict the deflection angle and total reflectivity.

## Approach
The design proceeds in three stages. First, the reflection properties (reflectivity and phase shift) of a periodic HCG (500 nm Si on 500 nm buried SiO₂) are mapped as functions of grating period and bar width using rigorous coupled-wave analysis (RCWA) for TM polarization at 1550 nm. This map covers a range of periods (0.3–1.2 μm) and bar widths (0.2–0.7 μm). Second, a non-periodic grating with 14 bars is designed by selecting periods and bar widths from this map such that the reflected phase approximates a linear profile yielding a specific target deflection angle; the total structure width should be ∼9.66 μm and the total phase shift ∼13.4 rad. Third, the designed non-periodic structure is simulated with a full-wave electromagnetic solver (e.g., Meep) using a TM-polarized Gaussian beam at 1550 nm, perfectly matched layers (PML) and scattering boundary conditions. From the simulation, the reflected beam deflection angle (via peak shift between different distances) and the total reflectivity are computed and reported.

## Reproduction target
The goal is to produce two scored outputs: (1) a CSV file (designed_hcg_parameters.csv) containing the 14-bar design (bar number, period, bar width) and the total width; (2) a JSON file (simulation_results.json) reporting the simulated deflection angle (in degrees) and total reflectivity (in percent). These quantities are then compared by a hidden verifier against expected reference values.

## Assets

- S4 (Stanford Stratified Structure Solver): https://github.com/victorliu/S4
- Meep: https://github.com/NanoComp/meep
- numpy, matplotlib, scipy: numpy matplotlib scipy

## Workflow steps

### Step 1: RCWA lookup table generation
- Role: process
- Action: Using an open-source RCWA solver (e.g., S4), compute reflectivity and phase shift of a periodic HCG (500 nm Si thickness, 500 nm buried SiO2, refractive indices 3.47 and 1.47) for TM polarization at 1550 nm. Scan grating periods from 0.3 to 1.2 μm and bar widths from 0.2 to 0.7 μm. Save the resulting lookup table (reflectivity and phase shift as functions of period and bar width) for the next step.
- Evidence: `/app/outputs/rcwa_lookup.csv`

### Step 2: Design of non-periodic HCG grating parameters
- Role: scored
- Action: From the RCWA lookup table generated in step_0, select a set of 14 grating periods and bar widths that discretely approximate a linear reflected phase profile targeting a deflection angle. The total structure width should be approximately 9.66 μm with a total phase shift of approximately 13.4 rad. Output the parameters to a CSV file with columns: bar_number (integer 1-14 or string 'total_width_um'), period_um (float), bar_width_um (float). Include a row with bar_number='total_width_um' and period_um = total width.
- Output file: `/app/outputs/designed_hcg_parameters.csv`
- Format: csv
- Contract: Columns: bar_number (integer 1-14, or string 'total_width_um'), period_um (float), bar_width_um (float). 15 rows: 14 bars + summary row.
- Scoring: scored by hidden verifier

### Step 3: FEM simulation and extraction of deflection angle and reflectivity
- Role: scored (load-bearing)
- Action: Using an open-source FEM solver (e.g., Meep), simulate the designed non-periodic HCG structure from step_1. The incident light is a TM-polarized Gaussian beam at 1550 nm. Use perfectly matched layers (PML) and scattering boundary conditions. Extract the reflected E-field intensity profiles at distances 18, 20, 22, and 24 μm from the reflection plane. Compute the deflection angle from the peak shift between 18 and 24 μm, and compute the total reflectivity. Write the results to a JSON file with keys 'deflection_angle_deg' (float) and 'reflectivity_pct' (float).
- Output file: `/app/outputs/simulation_results.json`
- Format: json
- Contract: JSON object with keys: deflection_angle_deg (float, degrees), reflectivity_pct (float, percent).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/designed_hcg_parameters.csv`
- `/app/outputs/simulation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### designed_hcg_parameters.csv
- path: `/app/outputs/designed_hcg_parameters.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Non-periodic HCG grating parameters (14 bars and total width) designed from RCWA lookup table.
- schema:
  - `type`: table
  - `required_columns`: `bar_number`, `period_um`, `bar_width_um`
  - `units`:
    - `period_um`: μm
    - `bar_width_um`: μm

### simulation_results.json
- path: `/app/outputs/simulation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Simulated deflection angle and total reflectivity of the non-periodic HCG reflector from FEM.
- schema:
  - `type`: object
  - `required`:
    - `deflection_angle_deg`: float
    - `reflectivity_pct`: float
  - `units`:
    - `deflection_angle_deg`: degrees
    - `reflectivity_pct`: percent

Notes: The design CSV is checked for structural validity (14 bars, parameter ranges, total width). The simulation JSON is compared to paper-reported reference values with tolerances; reflectivity is scored threshold-or-better, deflection angle within absolute tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "designed_hcg_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "bar_number",
          "period_um",
          "bar_width_um"
        ],
        "units": {
          "period_um": "μm",
          "bar_width_um": "μm"
        }
      },
      "description": "Non-periodic HCG grating parameters (14 bars and total width) designed from RCWA lookup table."
    },
    {
      "file": "simulation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "deflection_angle_deg": "float",
          "reflectivity_pct": "float"
        },
        "units": {
          "deflection_angle_deg": "degrees",
          "reflectivity_pct": "percent"
        }
      },
      "description": "Simulated deflection angle and total reflectivity of the non-periodic HCG reflector from FEM."
    }
  ],
  "notes": "The design CSV is checked for structural validity (14 bars, parameter ranges, total width). The simulation JSON is compared to paper-reported reference values with tolerances; reflectivity is scored threshold-or-better, deflection angle within absolute tolerance."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects the output artifacts. The verifier performs a structural audit on designed_hcg_parameters.csv to confirm the design satisfies required constraints (number of bars, parameter ranges, total width). For simulation_results.json, the verifier compares the reported deflection angle and reflectivity against reference values with appropriate tolerances. The reflectivity is scored on a threshold-or-better basis (meeting the reference qualifies for full credit), while the deflection angle is scored within an absolute tolerance. The final reward is a weighted combination of these checks. Simply reporting values is not enough; you must actually run the pipeline to generate the outputs.
