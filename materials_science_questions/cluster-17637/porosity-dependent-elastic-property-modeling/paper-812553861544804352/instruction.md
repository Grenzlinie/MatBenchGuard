# Seismic Behaviour of Aged Concrete Gravity Dams Under Near and Far Source Ground Motions

## Problem background
Concrete gravity dams deteriorate over decades due to alkali-aggregate reaction, micro-cracking, and simultaneous strength gain. At the same time, sediment accumulates on the reservoir bottom, gradually altering the reflection of pressure waves and the hydrodynamic forces on the dam. Understanding how these aging effects change the seismic response under different types of earthquake ground motions—near-source records that contain strong long-period pulses versus far-source records that lack such pulses—is important for safety assessment. This task involves computing the degraded concrete properties at several ages and the peak seismic response of the Koyna dam-reservoir system to a set of recorded ground motions.

## Approach
The concrete degradation is estimated using an empirical model that combines the rate of alkali-aggregate reaction expansion, a mechanical damage function, the gain in compressive strength with age, and a total-porosity-based reduction of the elastic modulus. The tensile strength of the degraded concrete is scaled from the unaged value according to the change in elastic modulus.

A 2D finite-element model of the Koyna dam and reservoir is built: the dam is represented by displacement-based solid elements, the reservoir by pressure-based fluid elements, and the two are directly coupled. The far end of the reservoir is truncated and equipped with a frequency-dependent non-reflecting boundary condition. Energy absorption at the reservoir bottom is modelled by an equivalent wave reflection coefficient that decreases as sediment thickness grows (sedimentation rate 0.3 m/year).

Linear time-history analysis is performed using Newmark’s average acceleration method. The system is excited by four horizontal ground-motion records—two from the Northridge earthquake (a near-source and a far-source record) and two from the Imperial Valley earthquake (again near-source and far-source)—all scaled to a peak ground acceleration of 0.24 g.

For each simulation case, time histories of relative horizontal crest displacement, major principal stress at the heel, minor principal stress at the neck, and hydrodynamic pressure are saved, and the peak (maximum absolute) values are extracted.

## Reproduction target
Produce two CSV files:

1. **degraded_properties.csv** – the degraded elastic modulus E_m (MPa) and tensile strength f_t (MPa) of the dam concrete at ages 1, 25, 50, 75, and 100 years, computed using the degradation model.

2. **response_summary.csv** – the peak seismic response quantities (maximum absolute relative horizontal crest displacement (m), maximum major principal stress at the heel (MPa, tensile), maximum minor principal stress at the neck (MPa, compressive), and maximum hydrodynamic pressure (MPa)) for all eight simulation cases (combination of earthquake, motion type, and age).

## Assets

- PEER NGA-West2 ground motion records: Northridge (RSN 1044 Newhall-LA County Fire Station, RSN 1000 Lake Hughes) and Imperial Valley (RSN 179 El Centro Array #4, RSN 186 Superstition Mountain): https://ngawest2.berkeley.edu/

## Workflow steps

### Step 1: Compute age-dependent degraded concrete properties
- Role: scored
- Action: Implement the empirical degradation model using the AAR strain time-fit relation, AAR damage factor, mechanical porosity via damage function, total porosity, un-degraded modulus from compressive strength, degraded modulus polynomial, and tensile strength scaling. Use a 28-day compressive strength of 36.3 MPa and initial modulus constant 32660 MPa. Compute the degraded elastic modulus E_m and tensile strength f_t at ages 1, 25, 50, 75, and 100 years.
- Output file: `/app/outputs/degraded_properties.csv`
- Format: csv
- Contract: Columns: age (years), E_m (MPa), f_t (MPa). One row per age: 1, 25, 50, 75, 100.
- Scoring: scored by hidden verifier

### Step 2: Run seismic finite-element simulations for Koyna dam-reservoir system
- Role: process
- Action: Build a 2D plane-strain finite-element model of the Koyna gravity dam and reservoir using Lagrangian displacement formulation for the dam and Eulerian pressure formulation for the reservoir. Implement a non-reflecting boundary condition at the reservoir far end (truncation length 0.5 times water depth) and sediment absorption via an equivalent reflection coefficient that varies with age (sedimentation rate 0.3 m/year). For each of the two ages (1 and 75 years), assemble the coupled dam-reservoir system matrices using the corresponding degraded concrete properties from Step 1 (E, Poisson's ratio 0.235, density 2415.82 kg/m³) and the reflection coefficient. Perform linear time-history analysis with Newmark's average acceleration method under the four scaled ground motions (NF1, FF1, NF2, FF2) with PGA 0.24g. Save the time histories of relative horizontal crest displacement, major principal stress at the heel, minor principal stress at the neck, and hydrodynamic pressure for each case.
- Evidence: none

### Step 3: Extract peak seismic response quantities
- Role: scored (load-bearing)
- Action: From the time-history outputs of Step 2, determine the maximum absolute relative horizontal crest displacement, maximum major principal stress at the heel (tensile), maximum minor principal stress at the neck (compressive), and maximum hydrodynamic pressure for each ground motion and age (1 year, 75 years). Compile the results into the output file.
- Output file: `/app/outputs/response_summary.csv`
- Format: csv
- Contract: Columns: earthquake (Northridge or Imperial Valley), motion_type (NF or FF), age (years), max_crest_displacement (m), max_major_principal_stress_heel (MPa), max_minor_principal_stress_neck (MPa), max_hydrodynamic_pressure (MPa). One row per case (8 rows): NF1 age1, NF1 age75, FF1 age1, FF1 age75, NF2 age1, NF2 age75, FF2 age1, FF2 age75.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/degraded_properties.csv`
- `/app/outputs/response_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### degraded_properties.csv
- path: `/app/outputs/degraded_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Degraded concrete elastic modulus and tensile strength at specified ages.
- schema:
  - `type`: table
  - `required_columns`: `age`, `E_m`, `f_t`
  - `units`:
    - `age`: years
    - `E_m`: MPa
    - `f_t`: MPa

### response_summary.csv
- path: `/app/outputs/response_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Peak seismic response quantities for all simulation cases.
- schema:
  - `type`: table
  - `required_columns`: `earthquake`, `motion_type`, `age`, `max_crest_displacement`, `max_major_principal_stress_heel`, `max_minor_principal_stress_neck`, `max_hydrodynamic_pressure`
  - `units`:
    - `age`: years
    - `max_crest_displacement`: m
    - `max_major_principal_stress_heel`: MPa
    - `max_minor_principal_stress_neck`: MPa
    - `max_hydrodynamic_pressure`: MPa

Notes: The seismic simulation step (Step 2) must be executed; its outputs feed the load-bearing scored step. Verification compares the reported values to hidden reference values with tolerances and also checks monotonic trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "degraded_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "age",
          "E_m",
          "f_t"
        ],
        "units": {
          "age": "years",
          "E_m": "MPa",
          "f_t": "MPa"
        }
      },
      "description": "Degraded concrete elastic modulus and tensile strength at specified ages."
    },
    {
      "file": "response_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "earthquake",
          "motion_type",
          "age",
          "max_crest_displacement",
          "max_major_principal_stress_heel",
          "max_minor_principal_stress_neck",
          "max_hydrodynamic_pressure"
        ],
        "units": {
          "age": "years",
          "max_crest_displacement": "m",
          "max_major_principal_stress_heel": "MPa",
          "max_minor_principal_stress_neck": "MPa",
          "max_hydrodynamic_pressure": "MPa"
        }
      },
      "description": "Peak seismic response quantities for all simulation cases."
    }
  ],
  "notes": "The seismic simulation step (Step 2) must be executed; its outputs feed the load-bearing scored step. Verification compares the reported values to hidden reference values with tolerances and also checks monotonic trends."
}
```

## How you are scored
A hidden verifier will compare the numeric entries in your two CSV files against reference values using appropriate tolerances. In addition, the verifier will check that your results obey the physical trends expected from the underlying theory—for example, systematic relationships between ages and motion types. The final score is the weighted sum of the scores for degraded_properties.csv and response_summary.csv.
