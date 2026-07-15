# Coupled FEM quenching simulation for 1045 steel cylinder

## Problem background
Quenching of low-alloy steels involves coupled thermal, mechanical, and phase transformation phenomena that determine the final microstructure, hardness, and residual stresses. Predicting these outcomes accurately can help optimize heat treatment to avoid cracking and distortion. This task reproduces a finite element simulation of quenching a 1045 steel cylinder from 840°C into water, which couples temperature, stress, and microstructural evolution to predict phase distributions, hardness profiles, stress fields, and dimensional changes.

## Approach
A 2D axisymmetric finite element model is implemented that solves the transient temperature field with latent heat release, the evolution of diffusional transformation fractions (ferrite, pearlite, bainite) using the Johnson–Mehl–Avrami–Kolmogorov (JMAK) equation with the additivity rule and virtual time to handle continuous cooling, and the martensite fraction via stress‑dependent Magee’s rule. The equilibrium ferrite fraction is derived from the extended Fe–Fe₃C phase boundary. Thermo‑physical properties are obtained by mixture rule from phase‑specific temperature‑dependent data (thermal conductivity, specific heat) taken from Woodard et al. (1999). A convection boundary condition uses heat transfer coefficients from Kakhki et al. (2009). The mechanical response follows a thermo‑elastic‑plastic constitutive law that includes transformation‑induced plasticity. The coupled equations are solved iteratively by a Newton–Raphson method. The resulting transient fields of temperature, phase fractions, stress, and displacement are post‑processed to extract the scored outputs.

## Reproduction target
Run the simulation for a 50 mm diameter, 100 mm long cylinder of AISI 1045 steel initially at 840 °C quenched into water at 25 °C. From the FEM results, produce the following CSV files (exact column specifications are given in the output contract):
- cooling_curves.csv: temperature at surface and center over time
- phase_fractions.csv: phase volume fractions along the central radius at 5, 20, 60, and 200 s
- von_mises_stress.csv: final von Mises stress profile along the radius
- volume_change.csv: total cylinder volume history
- dimensional_change.csv: reduction in diameter and length
- hardness_profile.csv: Vickers hardness profile based on Maynier’s empirical formulas.
The aim is to achieve quantitative agreement with the experimentally measured values for this setup, within tolerances that accommodate genuine re‑implementation variance.

## Assets

- Fe–Fe3C phase diagram
- TTT diagram of AISI 1045 steel
- Thermo-physical properties of 1045 steel phases: 10.1007/s11661-999-0159-4
- Heat transfer coefficients for water quenching: 10.1088/0965-0393/17/4/045007
- Magee constants for stress-dependent martensite
- Maynier hardness formulas

## Workflow steps

### Step 1: Derive temperature-dependent equilibrium ferrite fraction
- Role: process
- Action: From the Fe–Fe3C phase diagram, extend the Acm line below Ae1 to obtain the equilibrium volume fraction of pro-eutectoid ferrite as a function of temperature for 1045 steel (0.45 wt% C). Write the curve to ferrite_fraction_curve.txt.
- Evidence: `/app/outputs/ferrite_fraction_curve.txt`

### Step 2: Extract JMAK kinetic parameters from TTT diagram
- Role: process
- Action: From a public TTT diagram of 1045 steel, read transformation start and finish times (t_s, t_f) for ferrite, pearlite, and bainite at several temperatures. Compute JMAK parameters b(T) and n(T) using F_s=0.1, F_f=0.99. Save the parameters to jmak_parameters.csv.
- Evidence: `/app/outputs/jmak_parameters.csv`

### Step 3: Run FEM simulation of cylinder quenching
- Role: process
- Action: Implement a 2D axisymmetric thermo-mechanical-metallurgical finite element simulation of a 1045 steel cylinder (50 mm diameter, 100 mm length) quenched from 840°C into water at 25°C. Couple heat equation with latent heat, JMAK diffusional kinetics with additivity rule and virtual time, stress-dependent martensite via Magee's rule, temperature-dependent ferrite fraction from step_01, and thermo-elastic-plastic constitutive law including TRIP. Use thermo-physical properties from Woodard1999, convection boundary condition from Kakhki2009, and Magee constants from Onodera1976. Solve transient fields of temperature, phase fractions, stress, and displacement. Save a simulation summary log as evidence.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 4: Extract cooling curves
- Role: scored (load-bearing)
- Action: From the FEM results, extract temperature histories at the surface (r=25 mm) and center (r=0) over time from 0 to ≥200 s. Write to cooling_curves.csv.
- Output file: `/app/outputs/cooling_curves.csv`
- Format: csv
- Contract: time (s), temperature_surface (K), temperature_center (K)
- Scoring: scored by hidden verifier

### Step 5: Extract phase volume fraction profiles
- Role: scored
- Action: From FEM, extract phase volume fractions (ferrite, pearlite, bainite, martensite) along the central radius (0–25 mm) at quenching times t=5, 20, 60, 200 s. Ensure fractions sum to ≤1.0. Write to phase_fractions.csv.
- Output file: `/app/outputs/phase_fractions.csv`
- Format: csv
- Contract: radius (mm), time (s), ferrite, pearlite, bainite, martensite
- Scoring: scored by hidden verifier

### Step 6: Extract von Mises stress distribution
- Role: scored
- Action: From FEM at final time (≥200 s), extract von Mises stress along radius (0–25 mm). Write to von_mises_stress.csv.
- Output file: `/app/outputs/von_mises_stress.csv`
- Format: csv
- Contract: radius (mm), von_Mises_stress (MPa)
- Scoring: scored by hidden verifier

### Step 7: Compute volume change history
- Role: scored
- Action: From FEM displacement field, compute total volume of the cylinder at each simulation time step and write to volume_change.csv.
- Output file: `/app/outputs/volume_change.csv`
- Format: csv
- Contract: time (s), volume (mm³)
- Scoring: scored by hidden verifier

### Step 8: Compute dimensional change
- Role: scored
- Action: From final deformed shape, compute reduction in diameter and length (initial vs. final) and write to dimensional_change.csv.
- Output file: `/app/outputs/dimensional_change.csv`
- Format: csv
- Contract: dimension, initial_mm, final_mm, change_mm
- Scoring: scored by hidden verifier

### Step 9: Calculate hardness profile
- Role: scored
- Action: Using phase volume fractions at final time and Maynier's empirical formulas, compute Vickers macrohardness via mixture rule: HV = Σ F_i * HV_i. Write to hardness_profile.csv.
- Output file: `/app/outputs/hardness_profile.csv`
- Format: csv
- Contract: radius (mm), Vickers hardness (HV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cooling_curves.csv`
- `/app/outputs/phase_fractions.csv`
- `/app/outputs/von_mises_stress.csv`
- `/app/outputs/volume_change.csv`
- `/app/outputs/dimensional_change.csv`
- `/app/outputs/hardness_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cooling_curves.csv
- path: `/app/outputs/cooling_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time series of surface and center temperatures during quenching from 0 to ≥200 s.
- schema:
  - `type`: table
  - `required_columns`: `time`, `temperature_surface`, `temperature_center`
  - `units`:
    - `time`: s
    - `temperature_surface`: K
    - `temperature_center`: K

### phase_fractions.csv
- path: `/app/outputs/phase_fractions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase volume fractions along the central radius at t=5,20,60,200 s; fractions sum to ≤1.0.
- schema:
  - `type`: table
  - `required_columns`: `radius`, `time`, `ferrite`, `pearlite`, `bainite`, `martensite`
  - `units`:
    - `radius`: mm
    - `time`: s
    - `ferrite`: volume fraction
    - `pearlite`: volume fraction
    - `bainite`: volume fraction
    - `martensite`: volume fraction

### von_mises_stress.csv
- path: `/app/outputs/von_mises_stress.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Final von Mises stress distribution along radius at ≥200 s.
- schema:
  - `type`: table
  - `required_columns`: `radius`, `von_Mises_stress`
  - `units`:
    - `radius`: mm
    - `von_Mises_stress`: MPa

### volume_change.csv
- path: `/app/outputs/volume_change.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total cylinder volume versus time from 0 to ≥200 s.
- schema:
  - `type`: table
  - `required_columns`: `time`, `volume`
  - `units`:
    - `time`: s
    - `volume`: mm³

### dimensional_change.csv
- path: `/app/outputs/dimensional_change.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Diameter and length reduction after quenching; exactly two rows.
- schema:
  - `type`: table
  - `required_columns`: `dimension`, `initial_mm`, `final_mm`, `change_mm`
  - `units`:
    - `dimension`: string
    - `initial_mm`: mm
    - `final_mm`: mm
    - `change_mm`: mm

### hardness_profile.csv
- path: `/app/outputs/hardness_profile.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Final Vickers hardness profile along radius.
- schema:
  - `type`: table
  - `required_columns`: `radius`, `Vickers hardness`
  - `units`:
    - `radius`: mm
    - `Vickers hardness`: HV

Notes: All scored artifacts are compared to hidden reference data digitized from the paper’s figures. Tolerances are generous to accommodate re-implementation variance; the checker computes point-wise error and awards credit based on fraction of points within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cooling_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "temperature_surface",
          "temperature_center"
        ],
        "units": {
          "time": "s",
          "temperature_surface": "K",
          "temperature_center": "K"
        }
      },
      "description": "Time series of surface and center temperatures during quenching from 0 to ≥200 s."
    },
    {
      "file": "phase_fractions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "radius",
          "time",
          "ferrite",
          "pearlite",
          "bainite",
          "martensite"
        ],
        "units": {
          "radius": "mm",
          "time": "s",
          "ferrite": "volume fraction",
          "pearlite": "volume fraction",
          "bainite": "volume fraction",
          "martensite": "volume fraction"
        }
      },
      "description": "Phase volume fractions along the central radius at t=5,20,60,200 s; fractions sum to ≤1.0."
    },
    {
      "file": "von_mises_stress.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "radius",
          "von_Mises_stress"
        ],
        "units": {
          "radius": "mm",
          "von_Mises_stress": "MPa"
        }
      },
      "description": "Final von Mises stress distribution along radius at ≥200 s."
    },
    {
      "file": "volume_change.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "volume"
        ],
        "units": {
          "time": "s",
          "volume": "mm³"
        }
      },
      "description": "Total cylinder volume versus time from 0 to ≥200 s."
    },
    {
      "file": "dimensional_change.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "dimension",
          "initial_mm",
          "final_mm",
          "change_mm"
        ],
        "units": {
          "dimension": "string",
          "initial_mm": "mm",
          "final_mm": "mm",
          "change_mm": "mm"
        }
      },
      "description": "Diameter and length reduction after quenching; exactly two rows."
    },
    {
      "file": "hardness_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "radius",
          "Vickers hardness"
        ],
        "units": {
          "radius": "mm",
          "Vickers hardness": "HV"
        }
      },
      "description": "Final Vickers hardness profile along radius."
    }
  ],
  "notes": "All scored artifacts are compared to hidden reference data digitized from the paper’s figures. Tolerances are generous to accommodate re-implementation variance; the checker computes point-wise error and awards credit based on fraction of points within tolerance."
}
```

## How you are scored
A hidden verifier independently scores each scored artifact by comparing your submitted data to reference data derived from the paper’s figures. For each output, it computes pointwise differences between your values and the reference. The final score is a weighted combination of per‑artifact scores. Good agreement (small deviations) yields high credit; large systematic errors reduce the score. Phase fractions must sum to ≤ 1.0. No specific numeric thresholds are revealed to you, but a correct implementation that follows the physical models described above should produce results that pass the evaluation.
