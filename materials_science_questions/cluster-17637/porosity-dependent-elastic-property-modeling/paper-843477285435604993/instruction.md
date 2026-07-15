# Free Vibration and Active Control of Piezoelectric FG Metal Foam Plates with GPLs using Polygonal Finite Element Method

## Problem background
Functionally graded metal foam plates reinforced by graphene platelets (GPLs) combine low density with enhanced stiffness. Integrating piezoelectric layers enables active vibration control, but numerical modeling of such smart structures is challenging due to through-thickness variations of porosity and GPL dispersion and the electromechanical coupling. This problem addresses the design and analysis of GPL-reinforced metal foam plates with piezoelectric sensor/actuator layers for vibration suppression. The computational target is the prediction of free vibration frequencies and the demonstration of active vibration damping via velocity feedback control.

## Approach
The approach employs a polygonal finite element method (PFEM) based on a generalized C0-type higher-order shear deformation theory (C0-HSDT) with quadratic serendipity shape functions and assumed shear strain fields to model the mechanical displacement. The core layer’s effective properties are computed using the Halpin-Tsai micromechanical model and the rule of mixtures for GPLs, while the piezoelectric layers are modeled with linear electric potential through the thickness. Active vibration control is implemented via a constant velocity feedback scheme: the sensor layer generates a voltage proportional to the plate's deformation velocity, which is fed back to the actuator layer to produce a damping effect. The dynamic response is integrated with the Newmark method and a modal damping ratio.

## Reproduction target
Implement the PFEM solver and compute: (1) the first natural frequency (mode 1) of a simply supported (SSSS) piezoelectric FG metal foam plate having porosity distribution PD-S, GPL dispersion GPL-S, porosity coefficient e0=0.3, GPL weight fraction Λ_GPL=1.0 wt%, core thickness h_c=10 mm, each PZT-G1195N layer thickness h_p=0.1 mm, under closed-circuit electrical boundary condition; (2) the central deflection time history under a step load of amplitude q0=0.1 MPa with a sinusoidal spatial distribution, applied for a duration t1=0.02 s and then released, for two velocity feedback gains: Gv=0 (uncontrolled) and Gv=0.01 (controlled). Demonstrate that the controlled response decays faster than the uncontrolled one.

## Assets

- Material properties of copper, GPLs, PZT-G1195N
- Python 3 with NumPy and SciPy: numpy, scipy

## Workflow steps

### Step 1: PFEM solver implementation and mesh generation
- Role: process
- Action: Implement the polygonal finite element method (PFEM) solver with C0-HSDT, quadratic serendipity shape functions, assumed shear strain fields, and active velocity feedback control as described in the methodology. Generate a polygonal mesh (approximately 462 nodes) for a square plate of size a=b=0.2 m.
- Evidence: `/app/outputs/mesh_info.txt`

### Step 2: Material property calculation for FG metal foam plate with GPLs
- Role: process
- Action: Calculate through-thickness effective material properties for the foam core using the Halpin-Tsai micromechanical model and rule of mixtures, and compute the integrated constitutive and mass matrices for the given configuration: porosity distribution PD-S, GPL dispersion GPL-S, e0=0.3, Λ_GPL=1.0 wt%, core thickness h_c=10 mm, piezoelectric layer thickness h_p=0.1 mm, PZT-G1195N layers.
- Evidence: `/app/outputs/property_log.txt`

### Step 3: Free vibration analysis
- Role: scored
- Action: Compute the first natural frequency (mode 1) of the simply supported (SSSS) piezoelectric FG metal foam plate with closed-circuit electrical boundary condition using the implemented solver. Write the result to step_01_natural_frequencies.json.
- Output file: `/app/outputs/step_01_natural_frequencies.json`
- Format: json
- Contract: {"type":"object","required":{"mode1_freq_hz":"number"},"units":{"mode1_freq_hz":"Hz"}}
- Scoring: scored by hidden verifier

### Step 4: Dynamic response and active vibration control
- Role: scored
- Action: Using the solver and Newmark integration with a modal damping ratio of 0.8%, compute the central deflection time history under a uniformly distributed sinusoidal spatial load with step time function (q0=0.1 MPa, t1=0.02 s, then released) for two velocity feedback gains: Gv=0 (uncontrolled) and Gv=0.01 (controlled). Output a CSV with columns time_s, deflection_mm, gain (string 'Gv0' or 'Gv0.01'). Write to step_02_deflection_time_series.csv.
- Output file: `/app/outputs/step_02_deflection_time_series.csv`
- Format: csv
- Contract: required_columns: time_s (float), deflection_mm (float), gain (str: Gv0 or Gv0.01)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_natural_frequencies.json`
- `/app/outputs/step_02_deflection_time_series.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_natural_frequencies.json
- path: `/app/outputs/step_01_natural_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: First natural frequency of the simply supported piezoelectric FG metal foam plate for the specified configuration.
- schema:
  - `type`: object
  - `required`:
    - `mode1_freq_hz`: number
  - `units`:
    - `mode1_freq_hz`: Hz

### step_02_deflection_time_series.csv
- path: `/app/outputs/step_02_deflection_time_series.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series of central deflection for uncontrolled (Gv0) and controlled (Gv0.01) cases under a step load. The checker recomputes peak deflection magnitude for each gain and verifies that the controlled response decays faster than the uncontrolled one.
- schema:
  - `type`: table
  - `required_columns`: `time_s`, `deflection_mm`, `gain`
  - `units`:
    - `time_s`: seconds
    - `deflection_mm`: millimeters
  - `column_types`:
    - `time_s`: float
    - `deflection_mm`: float
    - `gain`: string

Notes: The hidden gold for the natural frequency is the paper-reported value for the same configuration, compared with relative tolerance 1%. For the dynamic response, the checker extracts the peak deflection magnitude for each gain and compares to the paper's reference within 5% tolerance, and also checks the trend of faster decay with control.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_natural_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "mode1_freq_hz": "number"
        },
        "units": {
          "mode1_freq_hz": "Hz"
        }
      },
      "description": "First natural frequency of the simply supported piezoelectric FG metal foam plate for the specified configuration."
    },
    {
      "file": "step_02_deflection_time_series.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_s",
          "deflection_mm",
          "gain"
        ],
        "units": {
          "time_s": "seconds",
          "deflection_mm": "millimeters"
        },
        "column_types": {
          "time_s": "float",
          "deflection_mm": "float",
          "gain": "string"
        }
      },
      "description": "Time series of central deflection for uncontrolled (Gv0) and controlled (Gv0.01) cases under a step load. The checker recomputes peak deflection magnitude for each gain and verifies that the controlled response decays faster than the uncontrolled one."
    }
  ],
  "notes": "The hidden gold for the natural frequency is the paper-reported value for the same configuration, compared with relative tolerance 1%. For the dynamic response, the checker extracts the peak deflection magnitude for each gain and compares to the paper's reference within 5% tolerance, and also checks the trend of faster decay with control."
}
```

## How you are scored
A hidden verifier independently evaluates your outputs for each scored workflow stage. It reads step_01_natural_frequencies.json and compares the reported first natural frequency to a hidden reference value. It reads step_02_deflection_time_series.csv and compares peak deflection magnitudes and decay trends against hidden references. The final reward is a weighted combination of the stage scores. Reporting a number is not sufficient; the underlying solver must correctly model the physics to produce consistent results.
