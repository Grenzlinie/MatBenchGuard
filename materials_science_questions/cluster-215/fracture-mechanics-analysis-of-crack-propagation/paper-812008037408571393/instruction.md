# Stress-Modified Ductile Fracture Strain Criteria and Burst Pressure Prediction for Pipeline Steel

## Problem background
Ductile failure of pipeline steels such as API X65 is strongly influenced by stress triaxiality – the ratio of hydrostatic stress to equivalent stress. A stress-modified fracture strain model relates the equivalent strain to fracture to the average stress triaxiality, providing a local failure criterion. Such criteria can be applied to predict burst pressures of pipes containing defects like gouges, offering a more physically based alternative to global net-section approaches. This task aims to reproduce the stress-modified fracture strain relationship for API X65 steel and to validate it against full-scale pipe burst experiments.

## Approach
The approach combines experimental data from tensile tests on smooth and notched round bars with detailed elastic–plastic finite element (FE) analyses. Axisymmetric FE models of the specimens are built using the provided true stress–plastic strain curve and loaded up to the experimentally observed failure initiation points. From the FE results, the histories of stress triaxiality and equivalent strain are extracted at the specimen centre (critical location) and as section‑average values over the minimum cross‑section. An average stress triaxiality is computed via a history integral up to the fracture strain, yielding paired data points. Exponential functions are then fitted to these pairs, giving explicit fracture strain criteria of the form ε_f = a·exp(b·(σ_m/σ_e)) + c. Two variants are calibrated: one based on the point of most severe damage (critical location) and one based on ligament‑averaged quantities (section average). In the second part, 3D FE models of a full‑scale pipe with a machined 45° V‑gouge are built for two gouge lengths (100 mm and 200 mm). The pipe is pressurised with a closed‑end boundary condition, and again stress triaxiality and equivalent strain are monitored as functions of internal pressure. By applying the previously fitted fracture strain criteria locally at each pressure step, the burst pressure – the pressure at which the local equivalent strain first meets the critical fracture strain – is predicted.

## Reproduction target
Your goal is to produce three artifacts:

1. The fitted parameters (a, b, c) for the critical‑location fracture strain criterion, relating equivalent strain to fracture to average stress triaxiality.
2. The fitted parameters (a, b, c) for the section‑average fracture strain criterion.
3. Predicted burst pressures for the two pipe gouge configurations: MNA (ℓ = 100 mm) and MNB (ℓ = 200 mm).

The criteria must be derived from the tensile‑bar FE simulations and the provided experimental fracture strains. The burst pressure predictions must be derived from the pipe FE simulations using the fitted criteria.

## Assets

- True stress–plastic strain curve of API X65 steel (digitized from paper Fig. 4): bundled as true_stress_plastic_strain.csv
- Experimental fracture strains for each notch radius (digitized from paper Fig. 12): bundled as fracture_strains.csv
- Open‑source finite‑element software (e.g. CalculiX, Elmer, or custom axisymmetric code) capable of large‑strain elastic‑plastic analysis with reduced‑integration CAX8R‑equivalent elements: public; agent may choose any open‑source FE solver
- Python environment with numpy, scipy, csv, json: installable via pip (numpy, scipy)

## Workflow steps

### Step 1: FE simulation of smooth and notched tensile bars
- Role: process
- Action: Set up axisymmetric elastic–plastic finite‑element models of the smooth and four notched tensile specimens (notch radii R0.2, R1.5, R3, R6) using the provided true stress–plastic strain curve. Apply axial displacement and run large‑strain simulations up to the experimentally reported failure initiation points. Extract engineering load–displacement curves and full field outputs of principal stresses, equivalent stress, equivalent strain, and stress triaxiality throughout loading.
- Evidence: `/app/outputs/tensile_bar_simulations.log`

### Step 2: Extraction of stress triaxiality and fracture strain pairs
- Role: process
- Action: From the FE results at the failure initiation points (identified using the provided experimental fracture strains), compute the average stress triaxiality (using the history integral definition in the paper) and the corresponding equivalent strain to fracture at the specimen centre (critical location) and averaged over the minimum section (section average). Exclude the R0.2 notch from the centre‑based criterion if the critical location is at the notch tip (as determined by a damage indicator analysis). Produce the (stress triaxiality, equivalent strain to fracture) data pairs.
- Evidence: `/app/outputs/fracture_data_pairs.csv`

### Step 3: Fit stress‑modified fracture strain criterion (critical location)
- Role: scored (load-bearing)
- Action: Perform exponential regression on the (average stress triaxiality, equivalent strain to fracture) data pairs to obtain the parameters a, b, c for the critical‑location criterion. Write the fitted parameters to the output JSON file.
- Output file: `/app/outputs/critical_location_criterion.json`
- Format: json
- Contract: JSON object with float keys a, b, c.
- Scoring: scored by hidden verifier

### Step 4: Fit stress‑modified fracture strain criterion (section average)
- Role: scored (load-bearing)
- Action: Same as Step 3 but for the section‑average approach. Write to the output JSON file.
- Output file: `/app/outputs/section_average_criterion.json`
- Format: json
- Contract: JSON object with float keys a, b, c.
- Scoring: scored by hidden verifier

### Step 5: FE simulation of pipe with gouge
- Role: process
- Action: Create 3D elastic–plastic finite‑element models of the API X65 pipe (Do=762 mm, t=17.5 mm) with a 45° V‑shaped gouge (depth d=8.75 mm, notch radius 2 mm) for the two gouge lengths ℓ=100 mm (MNA) and ℓ=200 mm (MNB). Use the same true stress–plastic strain curve and apply internal pressure with a closed‑end boundary condition. Run simulations and monitor stress triaxiality and equivalent strain at the gouge tip (critical location) and averaged over the remaining ligament as functions of internal pressure.
- Evidence: `/app/outputs/pipe_simulations.log`

### Step 6: Predict burst pressure using the failure criteria
- Role: scored
- Action: For each pipe case (MNA, MNB), apply the fitted fracture strain criteria (from Steps 3 and 4) to the FE‑computed stress triaxiality and equivalent strain histories. Determine the internal pressure at which the local equivalent strain first reaches the critical fracture strain. Report the predicted burst pressure for each configuration.
- Output file: `/app/outputs/burst_pressure_predictions.csv`
- Format: csv
- Contract: CSV with columns: pipe_no (string), predicted_burst_pressure_MPa (float). Two rows for MNA and MNB.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_location_criterion.json`
- `/app/outputs/section_average_criterion.json`
- `/app/outputs/burst_pressure_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_location_criterion.json
- path: `/app/outputs/critical_location_criterion.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted parameters for the critical‑location fracture strain criterion.
- schema:
  - `type`: object
  - `required`:
    - `a`: float
    - `b`: float
    - `c`: float
  - `items`: object
  - `units`:
    - `a`: dimensionless
    - `b`: dimensionless
    - `c`: dimensionless

### section_average_criterion.json
- path: `/app/outputs/section_average_criterion.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted parameters for the section‑average fracture strain criterion.
- schema:
  - `type`: object
  - `required`:
    - `a`: float
    - `b`: float
    - `c`: float
  - `items`: object
  - `units`:
    - `a`: dimensionless
    - `b`: dimensionless
    - `c`: dimensionless

### burst_pressure_predictions.csv
- path: `/app/outputs/burst_pressure_predictions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Predicted burst pressures for the MNA and MNB pipe configurations.
- schema:
  - `type`: table
  - `required_columns`: `pipe_no`, `predicted_burst_pressure_MPa`
  - `items`: object
  - `units`:
    - `pipe_no`: string
    - `predicted_burst_pressure_MPa`: MPa

Notes: The hidden checker compares the fitted parameters and predicted burst pressures to the paper‑reported values within predetermined tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_location_criterion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "a": "float",
          "b": "float",
          "c": "float"
        },
        "items": {},
        "units": {
          "a": "dimensionless",
          "b": "dimensionless",
          "c": "dimensionless"
        }
      },
      "description": "Fitted parameters for the critical‑location fracture strain criterion."
    },
    {
      "file": "section_average_criterion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "a": "float",
          "b": "float",
          "c": "float"
        },
        "items": {},
        "units": {
          "a": "dimensionless",
          "b": "dimensionless",
          "c": "dimensionless"
        }
      },
      "description": "Fitted parameters for the section‑average fracture strain criterion."
    },
    {
      "file": "burst_pressure_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pipe_no",
          "predicted_burst_pressure_MPa"
        ],
        "items": {},
        "units": {
          "pipe_no": "string",
          "predicted_burst_pressure_MPa": "MPa"
        }
      },
      "description": "Predicted burst pressures for the MNA and MNB pipe configurations."
    }
  ],
  "notes": "The hidden checker compares the fitted parameters and predicted burst pressures to the paper‑reported values within predetermined tolerances."
}
```

## How you are scored
A hidden verifier will independently examine each of your three output files. It will check that the files follow the required schemas and then compare the numerical values you report against reference results derived from the source work. Each output file carries equal weight in the final reward. To receive full credit you must produce correct numbers through genuine execution of the workflow; simply reporting an expected value without performing the required simulations and analyses will not suffice.
