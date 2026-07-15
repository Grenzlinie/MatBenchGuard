# Single-Parabolic-Band Modeling of Thermoelectric Transport Properties

## Problem background
Heavily electron-doped SrTiO3-based oxides are promising n-type thermoelectric materials for harvesting waste heat. Substituting the Sr site with Ca or Ba has been suggested to reduce the lattice thermal conductivity, but it is not yet clear how these substitutions affect the electronic transport properties. This task investigates the compositional dependence of the density-of-states effective mass (m_d*), the carrier relaxation time (τ), and the thermoelectric power factor (PF = S²σ) in 20%-Nb-doped (Ca,Sr,Ba)(Ti0.8Nb0.2)O3 epitaxial films at room temperature. By computing these parameters from experimentally measured carrier concentration, Hall mobility, and Seebeck coefficient for a set of A-site compositions, we can map the electron transport landscape across the phase diagram.

## Approach
The electronic transport parameters are derived using a single-parabolic-band (SPB) model. For each composition, the Seebeck coefficient S is related to the reduced chemical potential ξ (the ratio of the chemical potential to kBT) through the Fermi integrals. These integrals are evaluated numerically at a temperature of 300 K and are taken with a scattering parameter r = 0.5, appropriate for acoustic-phonon scattering. Solving the Seebeck equation gives ξ. Once ξ is known, the density-of-states effective mass m_d* is obtained from the carrier concentration n_e via the Fermi-Dirac integral of order 1/2. The carrier relaxation time τ is then calculated from the Hall mobility μ_Hall and the effective mass using τ = (μ_Hall × m_d*) / e, where e is the elementary charge. The electrical conductivity is computed as σ = n_e × e × μ_Hall, and the thermoelectric power factor follows as PF = S² × σ.

## Reproduction target
You are provided with an input CSV file containing the measured transport data for 15 (Ca,Sr,Ba)(Ti0.8Nb0.2)O3 compositions. The columns are the A-site composition label, carrier concentration n_e (in units of 10²¹ cm⁻³), Hall mobility μ_Hall (cm²/V/s), and Seebeck coefficient S (μV/K). Implement the SPB model as described above, numerically solve for the reduced chemical potential from the Seebeck coefficient for every composition, and compute the resulting m_d*, τ, and PF. Write your results to /app/outputs/computed_properties.csv. The CSV must have exactly the following columns: composition (string), n_e (float, 10²¹ cm⁻³), mu_Hall (float, cm²/V/s), S (float, μV/K), m_d_star (float, in units of the free electron mass m₀), tau (float, femtoseconds), PF (float, W/m/K²). The file must contain one data row per composition (15 rows in total).

## Assets

- Table I experimental transport data
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute SPB-derived transport properties
- Role: scored (load-bearing)
- Action: Implement the single-parabolic-band model with scattering parameter r=0.5 at T=300 K. For each composition in the provided input CSV (Table I), numerically solve for the reduced chemical potential from the Seebeck coefficient using Fermi integrals, then compute density-of-states effective mass, carrier relaxation time, and thermoelectric power factor. Write the results to computed_properties.csv.
- Output file: `/app/outputs/computed_properties.csv`
- Format: csv
- Contract: Columns: composition (str), n_e (float, units 10²¹ cm⁻³), mu_Hall (float, units cm²/V/s), S (float, units μV/K), m_d_star (float, units m₀), tau (float, units fs), PF (float, units W/m/K²). Exactly 15 data rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.csv
- path: `/app/outputs/computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Input transport data (composition, n_e, mu_Hall, S) and the computed density-of-states effective mass (m_d_star), carrier relaxation time (tau), and thermoelectric power factor (PF) for 15 compositions.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `n_e`, `mu_Hall`, `S`, `m_d_star`, `tau`, `PF`
  - `units`:
    - `n_e`: 10²¹ cm⁻³
    - `mu_Hall`: cm²/V/s
    - `S`: μV/K
    - `m_d_star`: m₀
    - `tau`: fs
    - `PF`: W/m/K²

Notes: The checker will recompute the derived quantities (m_d_star, tau, PF) from the provided input columns; tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "n_e",
          "mu_Hall",
          "S",
          "m_d_star",
          "tau",
          "PF"
        ],
        "units": {
          "n_e": "10²¹ cm⁻³",
          "mu_Hall": "cm²/V/s",
          "S": "μV/K",
          "m_d_star": "m₀",
          "tau": "fs",
          "PF": "W/m/K²"
        }
      },
      "description": "Input transport data (composition, n_e, mu_Hall, S) and the computed density-of-states effective mass (m_d_star), carrier relaxation time (tau), and thermoelectric power factor (PF) for 15 compositions."
    }
  ],
  "notes": "The checker will recompute the derived quantities (m_d_star, tau, PF) from the provided input columns; tolerances are hidden."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier. The verifier first checks that the output CSV file is present, correctly formatted, and contains the required columns and row count. It then reads the n_e, mu_Hall, and S columns from your file, re-runs the same SPB calculation independently, and compares your computed m_d_star, tau, and PF values to its own recomputed results. The final reward is based on how closely your output matches the verifier's reference; simply reporting the expected final numbers without correctly solving the Fermi integral equations will not receive credit. The verifier does not reveal the reference values or tolerances, so you must produce a genuine numerical solution of the SPB model to succeed.
