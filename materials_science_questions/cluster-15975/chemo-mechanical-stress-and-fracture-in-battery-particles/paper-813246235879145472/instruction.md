# Electromigration Damage Exponent Derivation for Solder Joints under Pulsed DC

## Problem background
Electromigration (EM) is a critical reliability concern for lead-free solder joints in advanced microelectronic packaging, where high current densities and elevated temperatures drive mass transport and eventual open-circuit failure. Under time-varying (pulsed) direct current, the interplay between electron wind force, thermal gradients, chemical potential, and stress gradients becomes complex. This task addresses a fully coupled thermal–electrical–mechanical–chemical damage model for SAC405 solder joints subjected to pulsed DC loading. The model predicts the evolution of vacancy concentration, stress, and damage using an entropy-based degradation metric. The goal is to derive the exponents that relate the dominant damage growth rate to duty factor, frequency, and current density—key parameters for a mean-time-to-failure (MTTF) equation.

## Approach
Implement a multiphysics finite element model in an open-source solver (e.g., FEniCS) that solves the coupled governing equations: vacancy conservation (mass diffusion driven by electric field, stress gradient, thermal gradient, and concentration gradient), static force equilibrium, transient heat transfer with Joule heating, electrical conduction, and an entropy-based damage evolution law. The material response includes viscoplasticity for the SAC405 solder. The simulation campaign consists of three parameter sweeps: (1) duty factor sweep at fixed low frequency and nominal current density; (2) frequency sweep at fixed duty factor and nominal current density; (3) current density sweep at fixed duty factor and frequency. For each condition, the damage parameter at the cathode current-crowding corner is recorded over time up to at least 6.7 hours. From these damage curves, an exponential growth rate is extracted for each condition. Finally, power-law regressions are performed to relate the growth rates to the swept parameters, yielding the three MTTF exponents.

## Reproduction target
Using the open-source FE implementation and the 2D plane-strain geometry described in the workflow steps, simulate damage evolution for the following 11 loading conditions:
- Duty factor sweep: r = 0.38, 0.50, 0.72, 1.00, with frequency f = 0.05 Hz and maximum current density j = 2.0×10⁶ A/cm².
- Frequency sweep: f = 0.05, 0.50, 5.00, 20.00 Hz, with duty factor r = 0.50 and j = 2.0×10⁶ A/cm².
- Current density sweep: j = 8.1×10⁵, 2.0×10⁶, 4.8×10⁶ A/cm², with r = 0.50 and f = 0.05 Hz.
Produce a CSV file (`step_01_damage_vs_time.csv`) containing the damage at the cathode corner (corner B) versus time for all conditions. Then fit an exponential growth model to the late-time (t > 6 h) damage data of each condition to extract the dominant growth rate b. Perform power-law regressions: b ∝ r^m, b ∝ f^p, b ∝ j^n, and output the derived exponents m, p, n in `step_02_exponents.json`. The target is to correctly compute these three exponents, which characterize the duty factor, frequency, and current density dependence of electromigration damage.

## Assets

- FEniCS (or equivalent open-source finite element solver): https://fenicsproject.org/
- NumPy, SciPy: numpy scipy

## Workflow steps

### Step 1: Implement coupled damage model in open-source FE
- Role: process
- Action: Implement the fully coupled thermal-electrical-mechanical-chemical damage model (vacancy conservation with electron wind force, chemical potential, stress gradient, and thermal gradient; force equilibrium; heat transfer with Joule heating; electrical conduction; entropy-based damage; and viscoplastic constitutive law) in an open-source finite element solver such as FEniCS. The implementation must support parametric control of duty factor, frequency, and maximum current density.
- Evidence: `/app/outputs/model_implementation.zip`

### Step 2: Set up FE geometry, mesh, and loading
- Role: process
- Action: Construct a 2D plane-strain finite element mesh of the solder joint geometry: solder bump diameter 116 µm, stand-off height 100 µm, Al trace thickness 2 µm, Cu trace thickness 10 µm. Apply boundary conditions: electrical current enters from top-left Al trace and exits from bottom-right Cu trace. Define pulse current loading profiles for the parameter sweeps: (1) duty factor sweep r = 0.38, 0.50, 0.72, 1.00 at frequency 0.05 Hz, current density 2.0×10⁶ A/cm²; (2) frequency sweep f = 0.05, 0.50, 5.00, 20.00 Hz at duty factor 0.50, current density 2.0×10⁶ A/cm²; (3) current density sweep j = 8.1×10⁵, 2.0×10⁶, 4.8×10⁶ A/cm² at duty factor 0.50, frequency 0.05 Hz. Set ambient temperature to 330.2 K. Assign SAC405 material parameters: vacancy relaxation time 1.8e-3 s, effective charge number 10, grain boundary diffusivity 2.72e6 µm²/s, thermal conductivity 57.3 W/(m·K), initial vacancy concentration 1.1e6 µm⁻³, vacancy relaxation ratio 0.2, and viscoplastic constants (kinematic hardening constants, isotropic hardening constant).
- Evidence: `/app/outputs/mesh_and_input.zip`

### Step 3: Run parameter sweeps and collect damage data
- Role: scored (load-bearing)
- Action: Execute the finite element model for all 11 parameter sets defined in step 2. For each simulation, record the damage parameter D at the cathode current-corner (corner B) as a function of time from t=0 to at least 6.7 hours of loading. Output the damage vs. time data in a single CSV file.
- Output file: `/app/outputs/step_01_damage_vs_time.csv`
- Format: csv
- Contract: columns: condition_id (string, e.g. 'r=0.38_f=0.05_j=2.0e6'), time_h (float, hours), damage (float, dimensionless damage parameter D).
- Scoring: scored by hidden verifier

### Step 4: Fit exponents and produce MTTF exponents
- Role: scored
- Action: From the damage data in step_01_damage_vs_time.csv, for times > 6 hours, fit an exponential model D = a·exp(b·t) for each condition to extract dominant growth rate b. Perform power-law regressions: b ∝ r^m using the four duty factor conditions, b ∝ f^p using the four frequency conditions, b ∝ j^n using the three current density conditions. Output the derived exponents m, p, n.
- Output file: `/app/outputs/step_02_exponents.json`
- Format: json
- Contract: JSON object with keys: m (float, duty factor exponent), p (float, frequency exponent), n (float, current density exponent).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_damage_vs_time.csv`
- `/app/outputs/step_02_exponents.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_damage_vs_time.csv
- path: `/app/outputs/step_01_damage_vs_time.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw damage vs time data for all 11 simulation conditions. The checker verifies existence, rule‑based data quality (e.g., data for all required conditions, monotonic damage increase), and uses it internally to recompute growth rates and exponents.
- schema:
  - `type`: table
  - `required_columns`: `condition_id`, `time_h`, `damage`
  - `units`:
    - `time_h`: hours
    - `damage`: dimensionless

### step_02_exponents.json
- path: `/app/outputs/step_02_exponents.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The derived MTTF equation exponents m (duty factor), p (frequency), n (current density). Compared to a hidden reference with tolerances; the checker also recomputes exponents from the CSV for cross‑validation.
- schema:
  - `type`: object
  - `required`:
    - `m`: float
    - `p`: float
    - `n`: float

Notes: The scoring primarily weights the accuracy of the derived exponents (from both the CSV and the reported JSON) against hidden paper‑reported values. Data quality checks on the CSV (presence of all 11 conditions, monotonicity) contribute a smaller fraction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_damage_vs_time.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition_id",
          "time_h",
          "damage"
        ],
        "units": {
          "time_h": "hours",
          "damage": "dimensionless"
        }
      },
      "description": "Raw damage vs time data for all 11 simulation conditions. The checker verifies existence, rule‑based data quality (e.g., data for all required conditions, monotonic damage increase), and uses it internally to recompute growth rates and exponents."
    },
    {
      "file": "step_02_exponents.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "m": "float",
          "p": "float",
          "n": "float"
        }
      },
      "description": "The derived MTTF equation exponents m (duty factor), p (frequency), n (current density). Compared to a hidden reference with tolerances; the checker also recomputes exponents from the CSV for cross‑validation."
    }
  ],
  "notes": "The scoring primarily weights the accuracy of the derived exponents (from both the CSV and the reported JSON) against hidden paper‑reported values. Data quality checks on the CSV (presence of all 11 conditions, monotonicity) contribute a smaller fraction."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently examines each required output artifact. For `step_01_damage_vs_time.csv`, the verifier checks that all 11 expected condition identifiers are present, that the damage increases monotonically with time within each condition, and then recomputes the exponential growth rates b for t > 6 h. For `step_02_exponents.json`, the verifier compares the reported exponents m, p, n to its own power-law fits derived from your CSV data, and also to a hidden reference (derived from the underlying paper). Data quality (completeness, monotonicity) contributes a small fraction of the reward, while the accuracy of the recomputed exponents (how closely they match the expected values) carries the most weight. The final reward is a weighted combination; reporting numbers without the supporting raw data is insufficient.
