# CaIrO3 Thermal Expansion and Grüneisen Parameter Fitting

## Problem background
The post-perovskite polymorph of MgSiO₃ is thought to dominate the D″ region at the base of the Earth's lower mantle. CaIrO₃ is the archetype ambient-pressure structural analogue of this phase, and accurate knowledge of its thermal expansion and elastic anisotropy is important for interpreting seismic observations. High-precision unit‑cell parameters (a, b, c) of CaIrO₃ have been measured by X‑ray powder diffraction over a wide temperature range (113–1173 K). Your task is to extract from these data the thermal expansion coefficients, Debye temperature, zero‑temperature cell dimensions, incompressibility‑related parameters, and axial elastic anisotropy ratios by fitting appropriate physical models.

## Approach
Two physical models are to be fitted:

1. **Linear thermal expansion model:** For temperatures between 298 K and 1173 K, the temperature dependence of a quantity X (volume or each axis length) is modelled as X(T) = X_{Tr} exp[ ∫_{Tr}^{T} (a0 + a1 T') dT' ] with reference temperature Tr = 300 K. Fit this model to the volume and to each axis length individually to obtain the reference value at Tr and the coefficients a0 and a1.

2. **Second‑order Grüneisen approximation:** Over the full temperature range (113–1173 K) the volume V(T) is described by V(T) = V0 U / (Q − b U) + V0 where U is the Debye internal energy computed from the Debye model: U(T) = 9 N kB T (T/θ_D)³ ∫₀^{θ_D/T} x³/(eˣ−1) dx (N is the number of atoms per unit cell). The fitted parameters are θ_D (Debye temperature), Q = V0 K0/γ′, V0 (volume at T=0 K), and b = (K0′−1)/2. Similarly, for each unit‑cell axis a(T) a separate model of the form a(T) = a0 U / (Q_A − b_A U) + a0 is fitted, where the fit yields θ_D, Q_A = κ_a0 V0 γ/γ′, the zero‑temperature axis length, and b_A.

3. **Axial incompressibilities:** Using the Q_A values from the axis fits, the V0 from the volume fit, and an assumed constant thermodynamic Grüneisen parameter γ = 1.17 (taken to equal γ′), compute the axial incompressibility for each axis as κ_a = (Q_A γ′) / (V0 γ), and similarly for b and c. Normalize these to the c‑axis incompressibility to obtain the ratios κ_a:κ_c, κ_b:κ_c, κ_c:κ_c (with κ_c:κ_c ≡ 1).

## Reproduction target
Produce three comma‑separated files:
- `thermal_expansion_coefficients.csv`: contains for each target (volume, a_axis, b_axis, c_axis) the fitted value at Tr=300 K, the linear coefficient a0 (K⁻¹), and the quadratic coefficient a1 (K⁻²).
- `fitted_gruneisen_parameters.csv`: contains for each fit target (volume, a_axis, b_axis, c_axis) the fitted parameter name (theta_D, Q, V0, b, or the corresponding axis‑specific names), the fitted value, and its estimated standard uncertainty (from the fit).
- `axial_incompressibility_ratios.csv`: contains the axis label (a, b, c) and the ratio of that axis's incompressibility to the c‑axis incompressibility (dimensionless, with κ_c:κ_c exactly 1.0).
The reference temperature for the linear expansion fits is 300 K; the Grüneisen fits use the whole temperature range; the Debye energy integral uses N = number of atoms in the CaIrO₃ unit cell. The assumed Grüneisen parameter is γ = 1.17.

## Assets

- CaIrO3_unit_cell_parameters.csv
- scipy numpy: scipy numpy

## Workflow steps

### Step 1: Prepare volume data
- Role: process
- Action: Read the provided CaIrO3_unit_cell_parameters.csv and compute the unit-cell volume V = a * b * c for each temperature. Write an intermediate CSV file 'volume_data.csv' with columns T (K) and V (Å³) for use in downstream steps.
- Evidence: `/app/outputs/volume_data.csv`

### Step 2: Fit linear thermal expansion coefficients
- Role: scored (load-bearing)
- Action: Fit a linear thermal expansion model to the unit-cell volume data from 298–1173 K and to each axis length a(T), b(T), c(T) over the same temperature range to obtain reference values at Tr=300 K and coefficients a0 and a1. Write the results to thermal_expansion_coefficients.csv.
- Output file: `/app/outputs/thermal_expansion_coefficients.csv`
- Format: csv
- Contract: CSV with columns: target (string: volume, a_axis, b_axis, c_axis), value_at_Tr (float, unit: Å³ for volume, Å for axes), a0 (float, unit: K⁻¹), a1 (float, unit: K⁻²).
- Scoring: scored by hidden verifier

### Step 3: Fit second-order Grüneisen approximation
- Role: scored (load-bearing)
- Action: Implement the second-order Grüneisen approximation with Debye internal energy and fit it to the full-range (113–1173 K) volume data by nonlinear least-squares to obtain Debye temperature θ_D, Q, V0, and b. Similarly, fit the axial Grüneisen approximation to a(T), b(T), c(T) over the full range to obtain per-axis θ_D, Q_A, axis_length_at_0, and b_A. Report all fitted values and their estimated standard uncertainties in fitted_gruneisen_parameters.csv.
- Output file: `/app/outputs/fitted_gruneisen_parameters.csv`
- Format: csv
- Contract: CSV with columns: parameter (string: theta_D, Q, V0, b for volume; theta_D, Q_A, a0, b_A for a-axis, etc.), fit_target (string: volume, a_axis, b_axis, c_axis), fitted_value (float), fitted_esd (float). Units: theta_D in K, Q in J, V0 in Å³, axis lengths in Å, b dimensionless.
- Scoring: scored by hidden verifier

### Step 4: Derive axial incompressibilities and ratios
- Role: scored (load-bearing)
- Action: Using the Q_A values from the axis fits, V0 from the volume fit, and an assumed thermodynamic Grüneisen parameter γ = 1.17 (with γ′ = γ), compute axial incompressibilities κ_a, κ_b, κ_c. Normalize these to the c-axis incompressibility to obtain the ratios κ_a:κ_c, κ_b:κ_c, κ_c:κ_c. Write the ratios to axial_incompressibility_ratios.csv.
- Output file: `/app/outputs/axial_incompressibility_ratios.csv`
- Format: csv
- Contract: CSV with columns: axis (string: a, b, c), ratio (float). Ratios dimensionless, normalized such that κ_c:κ_c = 1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_expansion_coefficients.csv`
- `/app/outputs/fitted_gruneisen_parameters.csv`
- `/app/outputs/axial_incompressibility_ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_expansion_coefficients.csv
- path: `/app/outputs/thermal_expansion_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Volumetric and linear thermal expansion coefficients for CaIrO3.
- schema:
  - `type`: table
  - `required_columns`: `target`, `value_at_Tr`, `a0`, `a1`

### fitted_gruneisen_parameters.csv
- path: `/app/outputs/fitted_gruneisen_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fitted second-order Grüneisen parameters for volume and unit-cell axes.
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `fit_target`, `fitted_value`, `fitted_esd`

### axial_incompressibility_ratios.csv
- path: `/app/outputs/axial_incompressibility_ratios.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Axial incompressibility ratios normalized to c-axis.
- schema:
  - `type`: table
  - `required_columns`: `axis`, `ratio`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_expansion_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "target",
          "value_at_Tr",
          "a0",
          "a1"
        ]
      },
      "description": "Volumetric and linear thermal expansion coefficients for CaIrO3."
    },
    {
      "file": "fitted_gruneisen_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "fit_target",
          "fitted_value",
          "fitted_esd"
        ]
      },
      "description": "Fitted second-order Grüneisen parameters for volume and unit-cell axes."
    },
    {
      "file": "axial_incompressibility_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "axis",
          "ratio"
        ]
      },
      "description": "Axial incompressibility ratios normalized to c-axis."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submitted CSV files are evaluated by a hidden verifier. Each file carries a weight, and the verifier compares every numerical value in those files against independently determined correct values. For parameters that have a directional meaning (e.g., errors, coefficients), meeting or exceeding the correct result earns full credit; for fixed derived quantities, agreement within a small tolerance is required. The reward is the weighted average of the fraction of parameters that satisfy the respective criteria. Simply reporting numbers without running the required fitting will not yield the correct values, as only a proper implementation of the described models can produce the reference values.
