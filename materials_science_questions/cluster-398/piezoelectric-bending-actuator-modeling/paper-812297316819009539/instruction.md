# Rayleigh-Ritz Model for Interdigitated Piezoelectric Actuator

## Problem background
Conventional piezoelectric wafer actuators use a through-thickness electric field and the transverse (d31) piezoelectric effect, producing isotropic in‑plane strains. By patterning interdigitated surface electrodes, a large in‑plane electric field component is created that instead engages the larger longitudinal (d33) effect, potentially yielding stronger and more anisotropic planar actuation. The effective homogeneous properties of a representative volume element (RVE) of such a wafer depend on the electrode geometry, especially the ratio of electrode spacing to wafer thickness (p/h). An approximate Rayleigh‑Ritz variational model has been proposed to predict these effective properties analytically. This task reproduces that model for a specific piezoceramic (PSI‑5A‑S2) and computes the field‑normalized relative free strains and clamped stress as functions of p/h, for a fixed electrode‑width‑to‑thickness ratio w/h = 1. The produced parametric curves are the target of this reproduction.

## Approach
The analytical method uses a Rayleigh‑Ritz approach based on the electromechanical Generalized Hamilton’s Principle. Assumed piecewise‑linear displacement fields (in the X, Y and Z directions) and a piecewise‑linear electric potential are defined over the RVE, with additional degrees of freedom to capture strain variations under the electrodes. The material is treated as a uniform piezoelectric poled in the X direction, with full electromechanical coupling. The assumed fields are substituted into the energy expressions, yielding a system of equations that relates average stresses, average strains, and the effective electric field. After static condensation of the strain under the electrodes, a compact effective constitutive law is obtained that expresses average stresses in terms of average strains and the applied field, with modified coupling coefficients that include a geometric factor (p‑w)/p. From this law, the field‑normalized relative X strain, Y strain, and X stress are calculated as the ratio of the interdigitated actuator’s performance to that of a conventional through‑thickness actuator at the same effective field level. The required material constants (stiffness, piezoelectric coupling, dielectric) are provided in the asset table below. Your job is to implement this model and evaluate it for a sweep of p/h values with w/h fixed at 1.

## Reproduction target
Implement the Rayleigh‑Ritz variational model described above, using the PSI‑5A‑S2 material constants (stiffness cE, coupling e, dielectric εS) supplied in the assets. Set the electrode‑width‑to‑thickness ratio w/h = 1. For integer values of p/h in the range 2 to 20 inclusive, solve the effective constitutive equations and compute the field‑normalized relative quantities: field‑normalized X strain, field‑normalized Y strain, and field‑normalized X stress. Write the results as a CSV file with columns p_over_h, field_norm_X_strain, field_norm_Y_strain, field_norm_X_stress — one row for each p/h value, with no missing rows. The CSV must be placed at /app/outputs/rayleigh_ritz_results.csv. The correctness of your implementation will be assessed by comparing these computed values to undisclosed reference predictions derived from the published model.

## Assets

- PSI-5A-S2 piezoelectric material constants

## Workflow steps

### Step 1: Rayleigh-Ritz model and parametric study
- Role: scored (load-bearing)
- Action: Implement the Rayleigh-Ritz variational model for the interdigitated electrode actuator. Using the provided PSI-5A-S2 material constants, set w/h = 1. For p/h ranging from 2 to 20 inclusive, compute the effective constitutive law and derive the field-normalized relative X strain, Y strain, and X stress. Output a CSV file with one row per p/h value.
- Output file: `/app/outputs/rayleigh_ritz_results.csv`
- Format: csv
- Contract: Columns: p_over_h (float), field_norm_X_strain (float), field_norm_Y_strain (float), field_norm_X_stress (float). At least 19 rows covering integer p/h from 2 to 20.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rayleigh_ritz_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rayleigh_ritz_results.csv
- path: `/app/outputs/rayleigh_ritz_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Parametric sweep of the Rayleigh-Ritz model: p/h from 2 to 20, w/h=1, reporting field-normalized relative X strain, Y strain, and X stress.
- schema:
  - `type`: table
  - `required_columns`: `p_over_h`, `field_norm_X_strain`, `field_norm_Y_strain`, `field_norm_X_stress`
  - `units`:
    - `p_over_h`: dimensionless
    - `field_norm_X_strain`: dimensionless
    - `field_norm_Y_strain`: dimensionless
    - `field_norm_X_stress`: dimensionless

Notes: At p/h=6 the values will be compared to a hidden gold with a relative tolerance; structural consistency (sign, monotonic trends) may also be audited.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rayleigh_ritz_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "p_over_h",
          "field_norm_X_strain",
          "field_norm_Y_strain",
          "field_norm_X_stress"
        ],
        "units": {
          "p_over_h": "dimensionless",
          "field_norm_X_strain": "dimensionless",
          "field_norm_Y_strain": "dimensionless",
          "field_norm_X_stress": "dimensionless"
        }
      },
      "description": "Parametric sweep of the Rayleigh-Ritz model: p/h from 2 to 20, w/h=1, reporting field-normalized relative X strain, Y strain, and X stress."
    }
  ],
  "notes": "At p/h=6 the values will be compared to a hidden gold with a relative tolerance; structural consistency (sign, monotonic trends) may also be audited."
}
```

## How you are scored
A hidden verifier will evaluate your submitted CSV. It compares the three field‑normalized quantities at each p/h to reference values that originate from the published model calculations, using tolerances that account for the expected numerical spread between different implementations. In addition, the verifier may check that the results satisfy basic physical consistency (for example, that the strain components have the expected signs and that their magnitudes vary monotonically with p/h). The final reward is a weighted combination of these checks, with the numerical accuracy carrying the largest weight. Meeting or exceeding the expected accuracy earns full credit; reward decreases as the computed results deviate further from the reference. Simply reporting the paper’s numbers without a correct computational implementation will not pass the verifier.
