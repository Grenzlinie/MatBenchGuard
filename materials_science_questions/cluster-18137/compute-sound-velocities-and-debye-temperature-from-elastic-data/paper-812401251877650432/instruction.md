# Compute Elastic Moduli and Debye Temperature from Ultrasonic Velocity Data

## Problem background
Amorphous selenium‑tellurium (Se₁₋ₓTeₓ) alloys are chalcogenide glasses whose mechanical and thermal properties are of fundamental interest. Ultrasonic velocity measurements — both longitudinal (vₗ) and transverse (vₜ) — together with mass density (ρ) and mean atomic density (ρ₀) can be used to determine the elastic moduli (Young's modulus E, shear modulus G, bulk modulus K) and the Debye temperature (θₘ) within the isotropic continuum approximation. In this task you will compute these quantities from provided experimental velocity and density data for four amorphous Se₁₋ₓTeₓ compositions at 20 °C.

## Approach
The computation is based on standard continuum elasticity relations for isotropic solids. Given vₗ, vₜ and ρ, the shear modulus is directly G = ρ vₜ². The bulk modulus K and Young's modulus E follow from combinations of vₗ, vₜ and ρ. The mean sound velocity vₘ is obtained from vₗ and vₜ, and the Debye temperature is θₘ = (h/k) vₘ (3ρ₀/(4π))^{1/3}, where h and k are the Planck and Boltzmann constants. You will read the input file, apply these formulas row‑by‑row, and write the resulting (x, E, G, K, θₘ) values to a CSV file. No further experimental data or modelling is required.

## Reproduction target
Produce a CSV file `elastic_constants.csv` containing one row for each Te atomic fraction `x` provided in the input. Columns: `x` (dimensionless), `E` (Young's modulus, 10⁹ dyn cm⁻²), `G` (shear modulus, 10⁹ dyn cm⁻²), `K` (bulk modulus, 10⁹ dyn cm⁻²), and `theta_m` (Debye temperature, K). The computation must use the isotropic continuum formulas described in the approach and the constants h and k.

## Assets

- input_measured_values.csv

## Workflow steps

### Step 1: Compute elastic constants and Debye temperature
- Role: scored (load-bearing)
- Action: Read the bundled input_measured_values.csv. For each row (composition x), compute shear modulus G = ρ * v_t^2, then compute bulk modulus K and Young's modulus E using the isotropic continuum relations that combine v_l, v_t and ρ. Compute mean sound velocity v_m from v_l and v_t, then compute Debye temperature θ_m = (h/k) * v_m * (3ρ0/(4π))^{1/3}. Output a CSV file elastic_constants.csv with columns x, E, G, K, theta_m (one row per composition), preserving units (E, G, K in 10^9 dyn/cm^2, θ_m in K).
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: CSV with columns: x (float, dimensionless), E (float, units 10^9 dyn/cm^2), G (float, units 10^9 dyn/cm^2), K (float, units 10^9 dyn/cm^2), theta_m (float, units K). Four rows for the given compositions.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed elastic moduli and Debye temperature for each composition. The checker compares these values against the paper's reported gold values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `x`, `E`, `G`, `K`, `theta_m`
  - `units`:
    - `x`: dimensionless
    - `E`: 10^9 dyn/cm^2
    - `G`: 10^9 dyn/cm^2
    - `K`: 10^9 dyn/cm^2
    - `theta_m`: K
  - `rows`: 4

Notes: The task is restricted to the stationary elastic moduli and Debye temperature at T=20°C. All other stages of the paper (temperature-dependent derivatives, overvolume, optical Kramers-Kronig analysis, Fulcher viscosity fitting) are excluded because they rely on non-public or non-computable inputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "E",
          "G",
          "K",
          "theta_m"
        ],
        "units": {
          "x": "dimensionless",
          "E": "10^9 dyn/cm^2",
          "G": "10^9 dyn/cm^2",
          "K": "10^9 dyn/cm^2",
          "theta_m": "K"
        },
        "rows": 4
      },
      "description": "Computed elastic moduli and Debye temperature for each composition. The checker compares these values against the paper's reported gold values within tolerance."
    }
  ],
  "notes": "The task is restricted to the stationary elastic moduli and Debye temperature at T=20°C. All other stages of the paper (temperature-dependent derivatives, overvolume, optical Kramers-Kronig analysis, Fulcher viscosity fitting) are excluded because they rely on non-public or non-computable inputs."
}
```

## How you are scored
A hidden verifier will load your `elastic_constants.csv`, read the four computed values for each composition, and compare them against reference values that represent the ground truth for these alloys. Your reward is determined by how closely your numbers match the references; exact agreement is not required, but substantial deviations reduce the score. All steps must be completed honestly — reporting numbers you found elsewhere will not pass the verifier's cross‑checks. The final score is a weighted combination of the individual quality checks.
