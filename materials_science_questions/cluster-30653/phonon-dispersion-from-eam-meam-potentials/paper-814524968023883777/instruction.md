# Gold Melting Curve Simulation

## Problem background
Gold is widely used as a pressure calibrator in high-pressure experiments, yet its high-pressure melting curve—the temperature at which it melts as a function of pressure—remains uncertain. Two molecular dynamics methods exist for determining melting: the well-established two-phase (TP) coexistence method and the recently proposed shock melting (SM) method. The SM method claims to achieve similar accuracy with substantially fewer atoms, offering potential efficiency gains. This work re-runs both methods to compute the melting curve of gold and compares the resulting pressure–temperature data, testing whether the SM method can reproduce the TP curve with a much smaller simulation system.

## Approach
All simulations use the Adams‑EAM interatomic potential for gold within the LAMMPS package. In the two-phase method, a solid–liquid slab is built and NPT simulations are run at a range of pressures. The melting temperature is identified by monitoring the motion of the solid–liquid interface. In the shock melting method, a smaller simulation box is shocked using the multi-scale shock technique (MSST). For each initial state, shocking produces a P‑T curve with a characteristic ‘Z’ shape; the lower corner point is taken as the melting temperature at that pressure. Data points are collected over a pressure range of 0–150 GPa. Finally, the Simon melting equation, Tm = Tm0 (P/a + 1)^b, is fitted to each set of data points using nonlinear least squares, yielding parameters Tm0, a, and b for both methods. The two melting curves are then compared.

## Reproduction target
Compute the melting temperature of gold at pressures spanning 0 to 150 GPa using both the two-phase and shock melting methods, with the Adams‑EAM potential. Provide at least 10 pressure–temperature data points for each method in CSV format. Fit the Simon equation to the data from each method, obtaining the parameters Tm0 (K), a (GPa), and b (dimensionless). The shock‑melting curve should be compared against the two‑phase curve to assess agreement.

## Assets

- LAMMPS: https://lammps.sandia.gov/
- Adams-EAM interatomic potential for gold: https://www.ctcms.nist.gov/potentials/entry/1990--Adams-J-B-Foiles-S-M-Wolfer-W-G--Au/

## Workflow steps

### Step 1: Two-phase (TP) melting curve simulation
- Role: scored (load-bearing)
- Action: Run LAMMPS MD simulations with the Adams-EAM potential to compute the high-pressure melting curve of gold using the two-phase coexistence method. Build a solid-liquid coexistence configuration, run NPT simulations at a range of pressures (at least 10 points from 0 to 150 GPa), and determine the melting temperature by monitoring interface motion. Output a CSV file containing pressure (GPa) and the corresponding melting temperature (K).
- Output file: `/app/outputs/tp_melting_curve.csv`
- Format: csv
- Contract: Two columns: pressure_GPa (float, units: GPa) and melting_temperature_K (float, units: K). At least 10 rows spanning 0 to 150 GPa.
- Scoring: scored by hidden verifier

### Step 2: Shock melting (SM) curve simulation
- Role: scored (load-bearing)
- Action: Run LAMMPS MD simulations with the Adams-EAM potential and the MSST module to compute the high-pressure melting curve of gold using the shock melting method. Use a small simulation box (e.g., 640 atoms), shock the sample at various velocities, and extract melting temperatures from the lower corner of the 'Z'-shaped P-T curves over a range of initial states covering at least 10 pressures from 0 to 150 GPa. Output a CSV file with pressure (GPa) and melting temperature (K).
- Output file: `/app/outputs/sm_melting_curve.csv`
- Format: csv
- Contract: Two columns: pressure_GPa (float, units: GPa) and melting_temperature_K (float, units: K). At least 10 rows spanning 0 to 150 GPa.
- Scoring: scored by hidden verifier

### Step 3: Simon equation fitting
- Role: scored
- Action: Fit the Simon melting equation Tm = Tm0 * (P/a + 1)^b to the TP and SM melting data points separately using non-linear least squares. Output a JSON file containing the fitted parameters for both methods.
- Output file: `/app/outputs/simon_fit.json`
- Format: json
- Contract: JSON object with keys 'method_tp' and 'method_sm'. Each key maps to an object with keys 'Tm0' (float, units: K), 'a' (float, units: GPa), and 'b' (float, dimensionless). Example: {"method_tp": {"Tm0": 1000.0, "a": 30.0, "b": 0.5}, "method_sm": {"Tm0": 1000.0, "a": 25.0, "b": 0.5}}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tp_melting_curve.csv`
- `/app/outputs/sm_melting_curve.csv`
- `/app/outputs/simon_fit.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tp_melting_curve.csv
- path: `/app/outputs/tp_melting_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Melting data from the two-phase method. The checker recomputes the Simon equation parameters from these points and compares to hidden gold values.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `melting_temperature_K`
  - `units`:
    - `pressure_GPa`: GPa
    - `melting_temperature_K`: K

### sm_melting_curve.csv
- path: `/app/outputs/sm_melting_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Melting data from the shock melting method. The checker recomputes the Simon equation parameters from these points and compares to hidden gold values.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `melting_temperature_K`
  - `units`:
    - `pressure_GPa`: GPa
    - `melting_temperature_K`: K

### simon_fit.json
- path: `/app/outputs/simon_fit.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Agent-reported Simon fit parameters for both methods. The checker recomputes the fit from the CSV data and checks this file for consistency.
- schema:
  - `type`: object
  - `required`:
    - `method_tp`:
      - `type`: object
      - `required`: `Tm0`, `a`, `b`
      - `units`:
        - `Tm0`: K
        - `a`: GPa
        - `b`: dimensionless
    - `method_sm`:
      - `type`: object
      - `required`: `Tm0`, `a`, `b`
      - `units`:
        - `Tm0`: K
        - `a`: GPa
        - `b`: dimensionless

Notes: All three scored artifacts are required. The checker refits the Simon equation from the raw CSV data, compares the resulting parameters with hidden paper gold, and also verifies that the simon_fit.json parameters are consistent with the recomputed fit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tp_melting_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "melting_temperature_K"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "melting_temperature_K": "K"
        }
      },
      "description": "Melting data from the two-phase method. The checker recomputes the Simon equation parameters from these points and compares to hidden gold values."
    },
    {
      "file": "sm_melting_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "melting_temperature_K"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "melting_temperature_K": "K"
        }
      },
      "description": "Melting data from the shock melting method. The checker recomputes the Simon equation parameters from these points and compares to hidden gold values."
    },
    {
      "file": "simon_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "method_tp": {
            "type": "object",
            "required": [
              "Tm0",
              "a",
              "b"
            ],
            "units": {
              "Tm0": "K",
              "a": "GPa",
              "b": "dimensionless"
            }
          },
          "method_sm": {
            "type": "object",
            "required": [
              "Tm0",
              "a",
              "b"
            ],
            "units": {
              "Tm0": "K",
              "a": "GPa",
              "b": "dimensionless"
            }
          }
        }
      },
      "description": "Agent-reported Simon fit parameters for both methods. The checker recomputes the fit from the CSV data and checks this file for consistency."
    }
  ],
  "notes": "All three scored artifacts are required. The checker refits the Simon equation from the raw CSV data, compares the resulting parameters with hidden paper gold, and also verifies that the simon_fit.json parameters are consistent with the recomputed fit."
}
```

## How you are scored
Your outputs will be evaluated by an automated verifier. For each method, the verifier refits the Simon equation to your submitted CSV data and compares the fitted parameters to hidden reference values. The simon_fit.json file is also checked for consistency with the refitted parameters. Additionally, the two melting curves are compared to ensure they overlap within a tolerance. Each artifact is scored independently, and the final reward is the weighted sum of the stage scores. Simply quoting known results is insufficient; your numbers must be produced by running the described simulations.
