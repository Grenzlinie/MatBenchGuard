# Hot-Electron Transverse Runaway: Analytic Galvanomagnetic Characteristics

## Problem background
In semiconductors under crossed electric (E) and non-quantizing magnetic (H) fields, hot-electron transport can exhibit carrier runaway when the energy dependences of the momentum and energy mean free paths satisfy certain conditions. One such condition — transverse runaway — occurs for scattering mechanisms where the momentum free-path exponent t is positive and the sum t + t_0 = 2 (t_0 being the energy free-path exponent). Under transverse runaway, the nondissipative (Hall) current diverges while the dissipative current simultaneously vanishes, leading to characteristic behaviour of the galvanomagnetic coefficients as the applied electric field approaches a critical value. The theory provides analytic expressions for the Hall angle, magnetoresistance, and current-voltage characteristic at constant carrier density, as well as for the breakdown field when carrier-density changes from impact ionization are included. This task reproduces the predicted transport properties for a representative scattering combination, testing the numerical evaluation of the derived closed-form expressions.

## Approach
The analysis starts from a kinetic description of hot electrons, where the distribution function in crossed fields can be expressed through a warming function that depends on the energy and the applied magnetic field. Under strong-heating conditions and with the transverse-runaway exponent relation, the effective warming electric field E is linked to the applied field E_x by an analytic relation involving the gamma function. From this, closed-form expressions for the Hall angle (tan θ), normalized magnetoresistance (ρ/ρ_0), and normalized current density (j_x/j_0) are obtained as functions of the reduced applied field E_x/E_0 and the magnetic field ratio H/H_i^0. The critical field E_0 itself is given by a material-dependent approximate formula that depends on the ion density. When impact ionization and trapping are included, the carrier density becomes field-dependent, and a critical breakdown field E_x_cr emerges from the balance of ionization and trapping rates; this ratio E_x_cr/E_0 can be computed from the compensation degree, cross-section exponents, and the same gamma-function combinations. The reproduction task requires implementing these analytic formulas numerically for the scattering combination t = 3, t_0 = -1 (momentum scattered by ionized impurities, energy scattered by deformation acoustic phonons), using standard mathematical libraries (gamma function) and fixed values for the ion density, magnetic field ratio, compensation, and cross-section parameters.

## Reproduction target
Compute the following quantities for a semiconductor system with momentum scattering by ionized impurities (t = 3) and energy scattering by deformation acoustic phonons (t_0 = -1):

1. **Critical electric field E_0** — evaluate E_0 from the approximate formula E_0 ≈ 2×10^{-7} z n_i^{1/2} V/cm using ionization multiplicity z = 1 and ion density n_i = 6.2×10^{14} cm^{-3}. Save the result as a single decimal number.

2. **Transport coefficients vs applied field** — using the analytic expressions for Hall angle, magnetoresistance, and current density with the computed E_0 and a magnetic field ratio H/H_i^0 = 1, compute tan θ, ρ/ρ_0, and j_x/j_0 for reduced applied fields E_x/E_0 ranging from 0.1 to 0.99 in steps of 0.01. Output a CSV table.

3. **Breakdown field with impact ionization** — from the impact-ionization model, with degree of compensation c_0 = 0.5, trapping cross-section exponent r = 1, and cross-section ratio σ_r^0/σ_I^0 = 1, compute the normalized critical breakdown field E_x_cr/E_0. Output the dimensionless ratio.

All outputs must be placed under `/app/outputs` with the exact filenames and formats specified in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute critical electric field E0
- Role: scored
- Action: Using the approximate formula (E0 ≈ 2×10^{-7} z n_i^{1/2} V/cm, with z=1 and ion density n_i=6.2×10^{14} cm^{-3}) for n-type Ge, compute the critical field E0 in V/cm.
- Output file: `/app/outputs/step_01_critical_field.txt`
- Format: txt
- Contract: A single decimal number representing E0 in V/cm.
- Scoring: scored by hidden verifier

### Step 2: Compute galvanomagnetic characteristics as functions of applied field
- Role: scored
- Action: For the scattering combination t=3, t0=-1, using the analytic expressions for Hall angle, magnetoresistance, and current density with E0 from step_01 and a magnetic field ratio H/H_i^0 = 1, compute tan θ, ρ/ρ0, and j_x/j0 for reduced applied fields Ex/E0 from 0.1 to 0.99 in steps of 0.01. Save as CSV.

The required analytic formulas are:
- Hall angle: `\tan\theta = (E_x/E_0) / \sqrt{1 - (E_x/E_0)^2}`
- Normalized magnetoresistance: `\rho/\rho_0 = D(t) \cdot (H/H_i^0) \cdot (E_x/E_0) / \sqrt{1 - (E_x/E_0)^2}`
  where `D(t) = \frac{\Gamma(3/(2t)) \; \Gamma((t+5)/2)}{\Gamma(3/2) \; \Gamma((3+2t)/(2t)) \; t}`
- Normalized current density: `j_x/j_0 = \frac{1}{D(t)} \cdot \frac{\Gamma((3+t)/(2t))}{\Gamma((3+2t)/(2t))} \cdot t^{-1/2} \cdot \frac{H_i^0}{H} \cdot \frac{1}{\sqrt{1 - (E_x/E_0)^2}}`
Use `H/H_i^0 = 1` (so `H_i^0/H = 1`). Compute the gamma functions using a standard library (e.g., `scipy.special.gamma`).
- Output file: `/app/outputs/step_02_transport_coefficients.csv`
- Format: csv
- Contract: CSV with header: Ex_ratio,tan_theta,rho_ratio,j_ratio. Ex_ratio values range from 0.1 to 0.99.
- Scoring: scored by hidden verifier

### Step 3: Compute breakdown field Ex_cr/E0 with impact ionization
- Role: scored
- Action: Compute the normalized breakdown field using the impact-ionization model. First compute

`\Phi_2(c_0, t) = \left[ \frac{\sigma_r^0}{\sigma_I^0} \cdot \frac{\Gamma((2-r)/t)}{\Gamma(3/(2t))} \cdot \frac{c_0}{1-c_0} \right]^{1/(2r)} \cdot \frac{\Gamma((2t+3)/(2t))}{\Gamma((t+3)/(2t))}`

Then the normalized breakdown field is

`\frac{E_x^{cr}}{E_0} = \frac{\Phi_2 \cdot (H/H_i^0)}{\sqrt{1 + (\Phi_2 \cdot (H/H_i^0))^2}}` with `H/H_i^0 = 1`.

Use the given parameter values: t=3, degree of compensation c0=0.5, trapping cross-section exponent r=1, cross-section ratio σ_r^0/σ_I^0=1.
- Output file: `/app/outputs/step_03_breakdown_field.txt`
- Format: txt
- Contract: A single decimal number representing Ex_cr/E0, dimensionless.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_critical_field.txt`
- `/app/outputs/step_02_transport_coefficients.csv`
- `/app/outputs/step_03_breakdown_field.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_critical_field.txt
- path: `/app/outputs/step_01_critical_field.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Critical electric field for onset of transverse runaway.
- schema:
  - `type`: text
  - `description`: A single float giving E0 in V/cm.

### step_02_transport_coefficients.csv
- path: `/app/outputs/step_02_transport_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Hall angle, magnetoresistance, and current density vs reduced electric field.
- schema:
  - `type`: table
  - `required_columns`: `Ex_ratio`, `tan_theta`, `rho_ratio`, `j_ratio`

### step_03_breakdown_field.txt
- path: `/app/outputs/step_03_breakdown_field.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Normalized breakdown field from impact-ionization model.
- schema:
  - `type`: text
  - `description`: A single float giving Ex_cr/E0, dimensionless.

Notes: All outputs are deterministic evaluations of analytic formulas. Scoring recomputes the same expressions and compares each value to the paper-reported gold with relative tolerance (1%).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_critical_field.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single float giving E0 in V/cm."
      },
      "description": "Critical electric field for onset of transverse runaway."
    },
    {
      "file": "step_02_transport_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Ex_ratio",
          "tan_theta",
          "rho_ratio",
          "j_ratio"
        ]
      },
      "description": "Hall angle, magnetoresistance, and current density vs reduced electric field."
    },
    {
      "file": "step_03_breakdown_field.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single float giving Ex_cr/E0, dimensionless."
      },
      "description": "Normalized breakdown field from impact-ionization model."
    }
  ],
  "notes": "All outputs are deterministic evaluations of analytic formulas. Scoring recomputes the same expressions and compares each value to the paper-reported gold with relative tolerance (1%)."
}
```

## How you are scored
A hidden verifier will independently implement the same analytic formulas with the given parameters and compare your output artifacts to reference values. For the critical field and breakdown field, the numeric value is compared within a tolerance. For the CSV, each row is compared column-wise. The verifier assigns a weighted score per stage, and the final reward is the combined weighted score. Reporting a number without producing the required artifacts as specified will not earn credit.
