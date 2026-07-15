# Diffractive Grating Outcoupling Efficiency via RCWA

## Problem background
Uniform LCD backlighting from point-like LED sources is challenging, especially for thin light guides. Conventional scattering or refractive extractors often produce non-uniform illumination with visible hot spots and may require additional redirecting optics. This work investigates a diffractive light extractor: a binary surface-relief grating placed on a light guide that diffracts guided light into directions that can escape. By modulating the fill factor of the grating along the guide, the outcoupling efficiency can be controlled to achieve uniform brightness. The optical performance is determined by rigorous electromagnetic simulations: the diffraction efficiencies and propagation angles of all reflected and transmitted orders, and the total outcoupled power—the sum of reflected orders that emerge below the critical angle for total internal reflection. The simulations rely on the rigorous coupled-wave analysis (RCWA) for TE polarization, with grating parameters, refractive indices, and incidence angles specified from the design space.

## Approach
The calculations use the rigorous coupled-wave analysis (RCWA), also known as the Fourier expansion method, for one-dimensional binary gratings. An open-source RCWA implementation (such as the S4 package or the 'rcwa' Python package) is employed to solve Maxwell's equations for a periodic permittivity profile. For a given grating period, relief height, fill factor, wavelength, incident angle, TE polarization, and refractive indices of the incident and output media, the solver returns the fraction of incident power diffracted into each reflected and transmitted order (efficiency) and the corresponding propagation angle with respect to the surface normal. Only propagating transmitted orders are considered—evanescent orders are omitted. The total outcoupled power for a given incidence angle and fill factor is obtained by summing the efficiencies of all reflected orders whose propagation angle is less than the critical angle for total internal reflection at the interface between the incident medium (index 1.5) and the output medium (index 1.0), i.e., arcsin(1/1.5) ≈ 41.8°. The workflow proceeds in two stages: first, computing the diffraction efficiencies for a reference grating at a single incidence angle to validate the solver; second, sweeping over fill factors and three incidence angles to map the outcoupled power as a function of fill factor.

## Reproduction target
This task has two concrete output targets, each saved as a CSV file under `/app/outputs`.

1. **Reference grating diffraction efficiencies**: For the grating with period = 2.5 µm, height = 0.5 µm, fill factor = 0.5, wavelength λ = 0.57 µm, refractive indices n₁ = 1.5 (incident medium), n₃ = 1.0 (output medium), TE polarization, and incidence angle 65°, compute the reflected and transmitted efficiencies (ηr, ηt) and the corresponding propagation angles (θr, θt) for diffraction orders m = −5, −4, …, 0. For each transmitted order, report ηt and θt only if the order propagates in the output medium; otherwise leave those entries blank.

2. **Outcoupled power vs fill factor**: For the same grating geometry (period 2.5 µm, height 0.55 µm, refractive indices 1.5/1.0, TE polarization), compute the total outcoupled power for each incidence angle in {60°, 70°, 80°} and each fill factor in {0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50}. The total outcoupled power is the sum of reflected-order efficiencies for those reflected orders whose propagation angle (with respect to the surface normal) is less than the critical angle arcsin(1/1.5) ≈ 41.8°. Report the results with one row per fill factor and columns for the power at each incidence angle.

All values should be reported as percentages.

## Assets

- Open-source RCWA solver (S4 or rcwa Python package): https://github.com/stefanuv/S4 or PyPI package 'rcwa'

## Workflow steps

### Step 1: Compute diffraction efficiencies for the reference grating
- Role: scored
- Action: Using a rigorous coupled-wave analysis (RCWA) solver, compute the reflected and transmitted diffraction efficiencies (ηr, ηt) and corresponding propagation angles (θr, θt) for a 1D binary grating with period 2.5 µm, height 0.5 µm, fill factor 0.5, wavelength 0.57 µm, incident medium index 1.5, output medium index 1.0, incidence angle 65°, and TE polarization. Include orders m = -5 to 0. For transmitted orders, include only propagating orders (those with real propagation angles in the output medium); leave ηt and θt empty for evanescent orders.
- Output file: `/app/outputs/step_01_diffraction_efficiencies.csv`
- Format: csv
- Contract: CSV with columns: m (integer, order number), eta_r (float, reflected efficiency in percent), theta_r (float, reflected angle in degrees), eta_t (float, transmitted efficiency in percent, empty for evanescent), theta_t (float, transmitted angle in degrees, empty for evanescent).
- Scoring: scored by hidden verifier

### Step 2: Compute total outcoupled power vs fill factor for three incidence angles
- Role: scored
- Action: For the same grating geometry (period 2.5 µm, height 0.55 µm, refractive indices 1.5 and 1.0, TE polarization), and for each incidence angle in {60°, 70°, 80°} and each fill factor in {0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50}, compute all reflected-order efficiencies. For each (angle, fill factor) pair, sum the efficiencies of those reflected orders whose propagation angle (measured from the surface normal) is less than the critical angle for total internal reflection at the 1.5/1.0 interface (arcsin(1/1.5) ≈ 41.8°). Report each total as a percentage.
- Output file: `/app/outputs/step_02_outcoupled_power.csv`
- Format: csv
- Contract: CSV with columns: f (float, fill factor), power_60 (float, total outcoupled power at 60° incidence in percent), power_70 (float, at 70°), power_80 (float, at 80°). Rows for f = 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_diffraction_efficiencies.csv`
- `/app/outputs/step_02_outcoupled_power.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_diffraction_efficiencies.csv
- path: `/app/outputs/step_01_diffraction_efficiencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Diffraction efficiencies and angles for a binary grating with period 2.5 µm, height 0.5 µm, fill factor 0.5, wavelength 0.57 µm, incident index 1.5, output index 1.0, 65° incidence, TE polarization.
- schema:
  - `type`: table
  - `required_columns`: `m`, `eta_r`, `theta_r`, `eta_t`, `theta_t`
  - `units`:
    - `m`: integer
    - `eta_r`: percent
    - `theta_r`: degrees
    - `eta_t`: percent
    - `theta_t`: degrees

### step_02_outcoupled_power.csv
- path: `/app/outputs/step_02_outcoupled_power.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total outcoupled power (reflected orders below critical angle) vs fill factor for 60°, 70°, 80° incidence, grating period 2.5 µm, height 0.55 µm, indices 1.5/1.0, TE polarization.
- schema:
  - `type`: table
  - `required_columns`: `f`, `power_60`, `power_70`, `power_80`
  - `units`:
    - `f`: dimensionless
    - `power_60`: percent
    - `power_70`: percent
    - `power_80`: percent

Notes: Values will be compared to hidden reference numbers from the source paper, with tolerance margins appropriate for different RCWA implementations. The solving agent must obtain its own RCWA implementation (open-source or self-written) and run it with the specified parameters; no pre-computed data is provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_diffraction_efficiencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "eta_r",
          "theta_r",
          "eta_t",
          "theta_t"
        ],
        "units": {
          "m": "integer",
          "eta_r": "percent",
          "theta_r": "degrees",
          "eta_t": "percent",
          "theta_t": "degrees"
        }
      },
      "description": "Diffraction efficiencies and angles for a binary grating with period 2.5 µm, height 0.5 µm, fill factor 0.5, wavelength 0.57 µm, incident index 1.5, output index 1.0, 65° incidence, TE polarization."
    },
    {
      "file": "step_02_outcoupled_power.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "f",
          "power_60",
          "power_70",
          "power_80"
        ],
        "units": {
          "f": "dimensionless",
          "power_60": "percent",
          "power_70": "percent",
          "power_80": "percent"
        }
      },
      "description": "Total outcoupled power (reflected orders below critical angle) vs fill factor for 60°, 70°, 80° incidence, grating period 2.5 µm, height 0.55 µm, indices 1.5/1.0, TE polarization."
    }
  ],
  "notes": "Values will be compared to hidden reference numbers from the source paper, with tolerance margins appropriate for different RCWA implementations. The solving agent must obtain its own RCWA implementation (open-source or self-written) and run it with the specified parameters; no pre-computed data is provided."
}
```

## How you are scored
Your submission is evaluated by a hidden automated verifier. Each output file is assessed independently: the verifier reads your CSV files and compares the reported values to reference results. A score is computed for each stage based on how closely your values match the expected results, with full credit when all values lie within acceptable tolerances and partial credit for partial accuracy. The final reward is a weighted combination of the stage scores, with the reference grating stage and the outcoupled power stage each carrying a substantial share. There is no need to match any particular published table or figure—your implementation must correctly execute the RCWA procedure described above.
