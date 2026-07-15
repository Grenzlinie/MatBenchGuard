# Low-velocity impact modeling of CNT-reinforced composite plates

## Problem background
Low-velocity impact response of advanced composite plates is crucial for aerospace and automotive structural design. This task addresses the impact behaviour of functionally graded carbon nanotube-reinforced composite (FG-CNTRC) plates with circular geometry. The plates consist of a polymer matrix reinforced by single-walled carbon nanotubes (SWCNTs) that can be distributed uniformly or graded across the thickness. The objective is to develop a computational model that predicts the contact force history, indentation depth, lateral deflection at the impact point, and total contact duration when a spherical impactor strikes the center of a clamped plate. The model must incorporate the non‑linear Hertzian contact law, the plate's kinematics based on a high‑order shear deformation theory, and the temperature‑dependent effective material properties of the composite. The computed peak metrics and force time series characterise the plate's ability to absorb energy and resist damage under impact, and they allow a direct comparison between different CNT distribution profiles and volume fractions.

## Approach
The reproduction follows a semi‑analytical Ritz‑based procedure. Effective material properties of the CNTRC plate are obtained by the extended rule of mixtures, which blends the temperature‑dependent orthotropic SWCNT properties with the isotropic PMMA matrix using CNT/matrix efficiency parameters. The plate kinematics are described by Reddy’s third‑order shear deformation theory, providing a realistic through‑thickness shear strain distribution without requiring a shear correction factor. The spatial displacement field is approximated by a Ritz expansion using polynomial shape functions that inherently satisfy the clamped boundary conditions on the circular edge. All domain integrals required for the mass and stiffness matrices are evaluated by two‑dimensional Simpson quadrature over the circular domain. The impactor‑plate interaction is modelled by the nonlinear Hertzian contact law, which relates the contact force to the local indentation. The equations of motion for the plate’s generalised coordinates and the impactor’s vertical displacement are coupled ordinary differential equations. They are integrated forward in time using a fourth‑order Runge–Kutta scheme. The workflow computes the full impact event for two circular plate configurations: a validation case (an isotropic clamped aluminium plate struck by a steel sphere) and the target case (a clamped X‑CNTRC plate with a CNT volume fraction of 0.28 at room temperature). From the simulated time histories, force curves are extracted and peak metrics are computed.

## Reproduction target
Implement the complete simulation pipeline and produce the following scored artifacts for the two cases:

Case 1 – Isotropic validation plate: a circular aluminium alloy plate (radius 38 mm, thickness 6 mm) with clamped edges, impacted at the center by a steel sphere of radius 19 mm and initial velocity 2.54 m/s. The plate material is isotropic with E = 68.95 GPa, ν = 0.33, and ρ = 2768 kg/m³.

Case 2 – X‑CNTRC plate: a circular CNT‑reinforced composite plate (radius 200 mm, thickness 10 mm) with clamped edges, impacted at the center by a steel sphere of radius 15 mm and initial velocity 3 m/s. The plate uses the X‑profile CNT distribution (both top and bottom surfaces are CNT‑rich) with effective volume fraction V*_CNT = 0.28. All temperature‑dependent material properties are evaluated at T = 300 K, using the supplied SWCNT and PMMA data and the CNT/matrix efficiency parameters η₁ = 0.141, η₂ = 1.585, η₃ = 1.109.

For each case, write a CSV file with header 'time,contact_force' containing the contact force time history (time in seconds, force in Newtons). Then, from the simulation data, compute four peak metrics: maximum contact force (MCF, in kN), maximum indentation depth (α_max, in mm), maximum lateral deflection of the plate at the impact point (w_max, in mm), and total contact duration (T₀, in µs). Store these metrics in a JSON file with two top‑level keys 'validation' and 'fg_cntrc', each holding an object with the fields 'MCF', 'alpha_max', 'w_max', 'T0'.

## Assets

- SWCNT (10,10) material properties at T=300K
- PMMA matrix properties at T=300K
- CNT/matrix efficiency parameters for V*_CNT=0.28
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute effective material properties
- Role: process
- Action: Using the extended rule of mixtures, compute through-thickness effective material properties E11, E22, G12, ν12, ρ, α11, α22 for the X-CNTRC distribution with V*_CNT=0.28 at T=300K, using the provided temperature-dependent SWCNT and PMMA matrix properties and CNT efficiency parameters. For the isotropic validation case, set E=68.95 GPa, ν=0.33, ρ=2768 kg/m³.
- Evidence: none

### Step 2: Assemble Ritz structural model and run validation simulation
- Role: process
- Action: Define Reddy's HSDT displacement field, build clamped-boundary Ritz shape functions using boundary-enforcing polynomials for a circular plate (radius 38 mm, thickness 6 mm). Implement 2D Simpson quadrature and assemble global mass M and stiffness K matrices (Appendix A). Couple the impactor with Hertzian contact law (steel sphere radius 19 mm, E=199.95 GPa, ν=0.33, ρ=7971.8 kg/m³, V0=2.54 m/s). Integrate the coupled ODE with fourth-order Runge-Kutta, recording time histories of contact force, impactor displacement, and plate lateral deflection.
- Evidence: `/app/outputs/validation_simulation.log`

### Step 3: Write contact force CSV for validation
- Role: scored (load-bearing)
- Action: Extract time (seconds) and contact force (Newtons) from the validation simulation and save as a CSV with header 'time,contact_force'.
- Output file: `/app/outputs/contact_force_validation.csv`
- Format: csv
- Contract: Two columns: 'time' (float, seconds), 'contact_force' (float, Newtons).
- Scoring: scored by hidden verifier

### Step 4: Assemble Ritz structural model and run FG-CNTRC simulation
- Role: process
- Action: Define Reddy's HSDT displacement field, build clamped-boundary Ritz shape functions using boundary-enforcing polynomials for a circular plate (radius 200 mm, thickness 10 mm) with X-CNTRC distribution and V*_CNT=0.28 at T=300K. Implement 2D Simpson quadrature and assemble global mass M and stiffness K matrices (Appendix A). Couple the impactor with Hertzian contact law (steel sphere radius 15 mm, density 7960 kg/m³, V0=3 m/s, E1 from impactor properties). Integrate the coupled ODE with fourth-order Runge-Kutta, recording contact force, indentation, lateral deflection, and impactor velocity.
- Evidence: `/app/outputs/fg_cntrc_simulation.log`

### Step 5: Write contact force CSV for FG-CNTRC
- Role: scored (load-bearing)
- Action: Extract time (seconds) and contact force (Newtons) from the FG-CNTRC simulation and save as a CSV with header 'time,contact_force'.
- Output file: `/app/outputs/contact_force_fg_cntrc.csv`
- Format: csv
- Contract: Two columns: 'time' (float, seconds), 'contact_force' (float, Newtons).
- Scoring: scored by hidden verifier

### Step 6: Compute peak metrics and write summary JSON
- Role: scored
- Action: From both simulations, compute maximum contact force (MCF) in kN, maximum indentation (alpha_max) in mm, maximum lateral deflection (w_max) in mm, and contact duration (T0) in microseconds. Save as a JSON object with keys 'validation' and 'fg_cntrc', each containing those four numeric fields.
- Output file: `/app/outputs/summary_metrics.json`
- Format: json
- Contract: JSON object with keys 'validation' and 'fg_cntrc'; each value is an object with fields 'MCF' (float, kN), 'alpha_max' (float, mm), 'w_max' (float, mm), 'T0' (float, µs).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/contact_force_validation.csv`
- `/app/outputs/contact_force_fg_cntrc.csv`
- `/app/outputs/summary_metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### contact_force_validation.csv
- path: `/app/outputs/contact_force_validation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series of contact force for the isotropic clamped plate impact.
- schema:
  - `type`: table
  - `required_columns`: `time`, `contact_force`
  - `units`:
    - `time`: seconds
    - `contact_force`: Newtons

### contact_force_fg_cntrc.csv
- path: `/app/outputs/contact_force_fg_cntrc.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series of contact force for the clamped X-CNTRC plate impact.
- schema:
  - `type`: table
  - `required_columns`: `time`, `contact_force`
  - `units`:
    - `time`: seconds
    - `contact_force`: Newtons

### summary_metrics.json
- path: `/app/outputs/summary_metrics.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Peak impact metrics for validation and FG-CNTRC cases.
- schema:
  - `type`: object
  - `required`: `validation`, `fg_cntrc`
  - `properties`:
    - `validation`:
      - `type`: object
      - `properties`:
        - `MCF`:
          - `type`: number
          - `unit`: kN
        - `alpha_max`:
          - `type`: number
          - `unit`: mm
        - `w_max`:
          - `type`: number
          - `unit`: mm
        - `T0`:
          - `type`: number
          - `unit`: µs
    - `fg_cntrc`:
      - `type`: object
      - `properties`:
        - `MCF`:
          - `type`: number
          - `unit`: kN
        - `alpha_max`:
          - `type`: number
          - `unit`: mm
        - `w_max`:
          - `type`: number
          - `unit`: mm
        - `T0`:
          - `type`: number
          - `unit`: µs

Notes: The output contract covers the three artifacts used by the checker: two contact force time series (CSV) and a summary JSON of peak metrics. The checker recomputes peak force from the CSV files and verifies consistency with the summary. All required columns and fields are declared; no hidden gold values or tolerances are disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "contact_force_validation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "contact_force"
        ],
        "units": {
          "time": "seconds",
          "contact_force": "Newtons"
        }
      },
      "description": "Time series of contact force for the isotropic clamped plate impact."
    },
    {
      "file": "contact_force_fg_cntrc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "contact_force"
        ],
        "units": {
          "time": "seconds",
          "contact_force": "Newtons"
        }
      },
      "description": "Time series of contact force for the clamped X-CNTRC plate impact."
    },
    {
      "file": "summary_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "validation",
          "fg_cntrc"
        ],
        "properties": {
          "validation": {
            "type": "object",
            "properties": {
              "MCF": {
                "type": "number",
                "unit": "kN"
              },
              "alpha_max": {
                "type": "number",
                "unit": "mm"
              },
              "w_max": {
                "type": "number",
                "unit": "mm"
              },
              "T0": {
                "type": "number",
                "unit": "µs"
              }
            }
          },
          "fg_cntrc": {
            "type": "object",
            "properties": {
              "MCF": {
                "type": "number",
                "unit": "kN"
              },
              "alpha_max": {
                "type": "number",
                "unit": "mm"
              },
              "w_max": {
                "type": "number",
                "unit": "mm"
              },
              "T0": {
                "type": "number",
                "unit": "µs"
              }
            }
          }
        }
      },
      "description": "Peak impact metrics for validation and FG-CNTRC cases."
    }
  ],
  "notes": "The output contract covers the three artifacts used by the checker: two contact force time series (CSV) and a summary JSON of peak metrics. The checker recomputes peak force from the CSV files and verifies consistency with the summary. All required columns and fields are declared; no hidden gold values or tolerances are disclosed."
}
```

## How you are scored
Your submission is evaluated by an automatic verifier that inspects the three required output files. The verifier first checks that each CSV file contains a valid two‑column time series with the correct headers, no missing or non‑numeric entries, and a physically plausible single‑peak shape. It then recomputes the maximum contact force from each CSV and verifies that this value is consistent (within a tight tolerance) with the MCF reported in summary_metrics.json. A large discrepancy between the CSV peak and the summary MCF reduces the weight of that case’s metrics.

The main scoring compares the computed peak metrics (MCF, α_max, w_max, T₀) for the two cases against hidden reference values that are derived from independent simulations and published benchmarks. Each of the four FG‑CNTRC metrics is assigned equal weight (20 % of the total score, summing to 80 %), and the validation case contributes the remaining 20 %. The verifier uses a directional reward that increases as your result approaches the reference; legitimate differences caused by discretisation or solver settings are accommodated by the scoring function. Simply reporting plausible numbers without executing the full simulation pipeline is detectable through the combination of shape checks, cross‑artifact consistency, and comparison against the hidden references.
