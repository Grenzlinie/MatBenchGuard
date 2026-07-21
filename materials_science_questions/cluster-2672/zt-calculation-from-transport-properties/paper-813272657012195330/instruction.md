# Impact of Impurity Bands on Thermoelectric Power Factor

## Problem background
The thermoelectric figure of merit ZT is proportional to the power factor α²σ (Seebeck coefficient squared times electrical conductivity). Modifying the electronic density of states, for example by introducing narrow impurity bands, can alter the Seebeck coefficient and conductivity and thus change the power factor. This task investigates how a narrow impurity band, located at various depths inside a parabolic main band, affects the power factor as a function of the Seebeck coefficient. The model assumes acoustic-mode lattice scattering so that all carriers (main band and impurity band) have equal mobility. The key question is how the power factor varies with Seebeck coefficient for different impurity band depths, compared to the case with no impurity band.

## Approach
Implement an impurity band model where a narrow impurity band lies at a depth E_I from the edge of a parabolic main band with density of states proportional to √E. All carriers obey Fermi-Dirac statistics and have the same mobility (acoustic scattering). For a range of reduced Fermi energies η = E_F/(kT), compute:
- Main band carrier concentration n_M from the Fermi-Dirac integral.
- Impurity band carrier concentration n_I from n_M and the Fermi distribution ratio f(η − ε_I) / (1 − f(η − ε_I)), where ε_I = E_I/(kT).
- Seebeck coefficient of the main band carriers α_M using the generalized formula with Fermi-Dirac integrals.
- Seebeck coefficient of impurity band carriers α_I = (k/e)(η − ε_I).
- Total Seebeck coefficient α as the conductivity-weighted average (α_I n_I + α_M n_M)/(n_I + n_M).
- Electrical conductivity σ in arbitrary units proportional to (n_I + n_M).
- Power factor PF = α²σ.
Perform this calculation for four cases: no impurity band (n_I = 0), and impurity band depths E_I = 0, kT, 4kT. Sample enough η points to cover a Seebeck coefficient range of roughly 0 to 400 μV/K. Output the resulting curves as a CSV file.

## Reproduction target
Produce a CSV file with columns impurity_band_depth (string: 'none', '0', 'kT', '4kT'), seebeck_muV_per_K (float), and power_factor_arb_units (float). Rows must cover Seebeck coefficients from approximately 0 to 400 μV/K for each impurity band depth. The verifier will read this file, interpolate to find the power factor at a Seebeck coefficient of exactly 200 μV/K for each depth, and compare the relative power factor between different band depths to evaluate the effect of the impurity band location.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute impurity-band power factor curves
- Role: scored (load-bearing)
- Action: Implement the impurity band model assuming a narrow impurity band inside a parabolic main band with density of states proportional to sqrt(E), equal carrier mobility (acoustic-mode lattice scattering), and carriers obeying Fermi-Dirac statistics. For a range of reduced Fermi energies η, compute: (i) impurity band carrier concentration n_I and main band carrier concentration n_M using the Fermi distribution relation n_I = n_M * f(η - ε_I) / (1 - f(η - ε_I)) with ε_I = E_I/(kT); (ii) Seebeck coefficient for main-band carriers α_M from the generalised formula involving Fermi-Dirac integrals, and for impurity-band carriers α_I = (k/e)*(η - ε_I); (iii) conductivity-weighted total Seebeck coefficient α = (α_I n_I + α_M n_M)/(n_I+n_M); (iv) electrical conductivity in arbitrary units proportional to (n_I+n_M); and (v) power factor PF = α²σ. Repeat for impurity band depths E_I = 0, kT, 4kT and for the no-impurity-band case (n_I ≡ 0). Sample enough η points to cover a Seebeck coefficient range of roughly 0 to 400 μV/K. Save all results in a CSV file with columns: impurity_band_depth (string: 'none', '0', 'kT', '4kT'), seebeck_muV_per_K (float), power_factor_arb_units (float).
- Output file: `/app/outputs/power_factor_vs_seebeck.csv`
- Format: csv
- Contract: Columns: impurity_band_depth (string), seebeck_muV_per_K (float), power_factor_arb_units (float). Rows covering Seebeck coefficients from ~0 to 400 μV/K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/power_factor_vs_seebeck.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### power_factor_vs_seebeck.csv
- path: `/app/outputs/power_factor_vs_seebeck.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file containing the power factor versus Seebeck coefficient for each impurity band depth (none, 0, kT, 4kT).
- schema:
  - `type`: table
  - `required_columns`: `impurity_band_depth`, `seebeck_muV_per_K`, `power_factor_arb_units`
  - `units`:
    - `seebeck_muV_per_K`: μV/K
    - `power_factor_arb_units`: arbitrary units

Notes: Power factor is in arbitrary units, so only relative reductions and ordering are meaningful. The checker will interpolate at a specific Seebeck coefficient to verify the paper's numerical claim.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "power_factor_vs_seebeck.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "impurity_band_depth",
          "seebeck_muV_per_K",
          "power_factor_arb_units"
        ],
        "units": {
          "seebeck_muV_per_K": "μV/K",
          "power_factor_arb_units": "arbitrary units"
        }
      },
      "description": "CSV file containing the power factor versus Seebeck coefficient for each impurity band depth (none, 0, kT, 4kT)."
    }
  ],
  "notes": "Power factor is in arbitrary units, so only relative reductions and ordering are meaningful. The checker will interpolate at a specific Seebeck coefficient to verify the paper's numerical claim."
}
```

## How you are scored
A hidden verifier reads your output CSV, interpolates the power factor at a Seebeck coefficient of 200 μV/K for each impurity band depth, and computes the ratio of the power factor with E_I=0 to the power factor without impurity band. It also checks the ordering of the power factors at 200 μV/K across the four depths. Your total reward is a weighted combination of these checks. The verifier uses its own hidden tolerances and does not rely on any numbers you may have reported outside the CSV.
