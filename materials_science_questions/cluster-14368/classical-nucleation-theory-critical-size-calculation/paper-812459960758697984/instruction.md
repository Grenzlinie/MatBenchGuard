# Droplet Evaporation Lifetime and Psychrometric Temperature Calculation

## Problem background
Evaporation of a spherical liquid droplet in a gaseous environment is a fundamental problem in aerosol science, atmospheric physics, and power engineering. The evaporation rate is controlled by coupled diffusion of vapor, conductive heat transfer leading to droplet cooling, the finite condensation coefficient of vapor molecules, and the curvature‑dependent vapor pressure (Kelvin effect). A diffusion–heat coupled model that balances molecular and heat fluxes yields analytical predictions for the droplet lifetime as a function of initial radius and for the steady‑state psychrometric temperature. This task implements that model for water droplets under specified ambient conditions, computing the characteristic model parameters, the psychrometric temperature difference, and a table of complete evaporation times.

## Approach
Implement the diffusion–heat coupled evaporation model for a spherical droplet. The model couples diffusive vapor transport with conductive heat flow to obtain a closed‑form relationship linking droplet radius, relative humidity, surface temperature, and evaporation rate. Using the water physical properties listed in the workflow steps, compute (1) the characteristic dimensionless/dimensional parameters that define the model's length, time, and surface‑tension scales; (2) the steady‑state psychrometric relative temperature difference z_inf in the limit of large droplet radius, for two fixed ambient humidity values; (3) the complete evaporation lifetime theta over a logarithmically spaced set of initial radii. All necessary formulas are described in the workflow steps; no external derivation is required beyond what is stated there.

## Reproduction target
Compute and save the following three numerical artifacts for water:
1. `characteristic_params.json` – the dimensionless parameter a, the characteristic length b (nm), the characteristic time tau (µs), and the surface‑tension parameter beta, as defined by the diffusion–heat coupled model.
2. `psychrometric_temperature.csv` – the psychrometric relative temperature difference z_inf for ambient relative humidities f0 = 0.9 and 0.99, with T0 = 300 K.
3. `droplet_lifetime.csv` – the complete evaporation lifetime theta (seconds) for initial droplet radii from 0.01 to 100 µm (at least 20 logarithmically spaced points), using T0 = 300 K, f0 = 0.5, and condensation coefficient α_c = 0.04.
All outputs must follow the schema and units declared in the corresponding workflow steps.

## Assets
No external datasets, model weights, or other files are required. All physical constants and water property values needed for the computations (saturated vapor pressure, latent heat, liquid density, diffusion coefficient, condensation coefficient, surface tension, etc.) are given directly in the workflow steps. The solving agent only needs a Python environment with standard scientific libraries (numpy, scipy).

## Workflow steps

### Step 1: Compute characteristic dimensionless parameters
- Role: scored
- Action: |
  Compute the dimensionless parameters a, b, τ, β for water using the following definitions.

  Physical constants for water at T0 = 300 K:
  - Saturated vapor pressure P_s = 3.6 × 10^3 Pa
  - Latent heat L0 = 43.8 kJ/mol = 43800 J/mol
  - Liquid density ρ = 997 kg/m³
  - Diffusion coefficient of water vapor in air D = 0.25 cm²/s = 2.5e-5 m²/s
  - Condensation coefficient α_c = 0.04
  - Surface tension σ = 71 × 10⁻³ N/m
  - Thermal conductivity of air λ = 0.026 W m⁻¹ K⁻¹
  - Temperature accommodation coefficient α_t = 1
  - Boltzmann constant k = 1.380649 × 10⁻²³ J/K
  - Avogadro's number N_A = 6.02214076 × 10²³ mol⁻¹
  - Molecular weight of water M_w = 18.015 × 10⁻³ kg/mol
  - Mass of one water molecule M = M_w / N_A

  Derived quantities:
  L0_per_molecule = L0 / N_A
  ω = L0_per_molecule / (k T0) - 1

  Saturated vapor flux at the surface (Hertz–Knudsen expression):
    w_s(T0) = α_c P_s / sqrt(2 π M k T0)

  Dimensionless parameter a:
    a = (α_t λ T0) / [ D P_s ω (ω + 1) ]

  Characteristic length b:
    b = (α_t λ) / [ k w_s(T0) ω (ω + 1) (a + 1) ]   (units: m)
    Convert b to nm.

  Characteristic time τ:
    τ = b² ρ k (ω + 1) / (α_t λ M)   (units: s)
    Convert τ to microseconds.

  Surface tension parameter β:
    Kelvin radius: R_σ = 2 σ M / (ρ k T0)   (m)
    β = R_σ / (b ω (a + 1))

  Compute a, b (in nm), τ (in µs), β and save them as a JSON object with keys "a", "b", "tau", "beta".
  Output file: /app/outputs/characteristic_params.json
- Output file: `/app/outputs/characteristic_params.json`
- Format: json
- Contract: JSON object with keys: a (dimensionless), b (nm), tau (microseconds), beta (dimensionless).
- Scoring: scored by hidden verifier

### Step 2: Compute psychrometric temperature
- Role: scored
- Action: |
  For water, compute the psychrometric relative temperature difference in the limit of a very large droplet (R → ∞).
  In this limit, the relative temperature difference z_inf = (T0 - T_R)/T_R is given by:
    ω = L0_per_molecule / (k T0) - 1   (same as Step 1)
    φ0 = (1 - f0) / (ω (a + 1))
    z_inf = φ0
  Use the same physical constants and the value of a computed in Step 1.
  Compute z_inf for f0 = 0.9 and f0 = 0.99. Write a CSV file with columns "f0", "z_inf" and two data rows.
  Output file: /app/outputs/psychrometric_temperature.csv
- Output file: `/app/outputs/psychrometric_temperature.csv`
- Format: csv
- Contract: CSV with columns: f0 (float), z_inf (float). Two rows: f0=0.9 and 0.99.
- Scoring: scored by hidden verifier

### Step 3: Compute droplet lifetime table
- Role: scored
- Action: |
  Compute the complete evaporation time (lifetime) for a water droplet as a function of initial radius using the analytical formulas from the diffusion-heat model.

  Conditions: T0 = 300 K, ambient relative humidity f0 = 0.5, condensation coefficient α_c = 0.04.
  Use the same physical constants and the values of a, b (nm), τ (µs), β computed in Step 1.
  Convert the time scale τ to seconds: τ_s = τ × 1e-6 s.
  Convert the length scale b to meters: b_m = b × 1e-9 m.

  Define:
  ω = L0_per_molecule/(k T0) - 1
  φ0 = (1 - f0) / (ω (a + 1))

  For a given initial droplet radius R_initial (in meters), compute the dimensionless radius R = R_initial / b_m.
  Then compute the dimensionless relative temperature difference z using:
    z = 0.5 * ( sqrt(R^2 + 2 R (1 - β + 2 φ0) + (1 + β)^2 ) - R - 1 + β )

  The dimensionless lifetime θ is given by:
    θ = (1/(2 φ0^2)) * ((z - β)/(φ0 - z)^2) * 
        [ φ0 * ( 2 φ0 z^2 - z (3 φ0^2 + 1) + 2 φ0 (φ0^2 + φ0 + 1) )
          - β * ( φ0 (φ0^2 + 4 φ0 + 3) - 2 z (φ0 + 1) ) ]
        - ( (φ0 + 1)(φ0^2 + β)(φ0 - β) / φ0^3 ) * ln( (φ0 - β) / (φ0 - z) )
        - ( β ( β (φ0 + 1) - φ0 ) / φ0^3 ) * ln( β / z )

    (For the evaporating droplet, z is positive and φ0 > β, so all log arguments are positive.)

  The physical lifetime in seconds is lifetime_s = θ × τ_s.

  Compute lifetime_s for a set of R_initial values logarithmically spaced from 0.01 µm to 100 µm (at least 20 points).
  Convert R_initial to meters: R_initial_m = R_initial_um × 1e-6.
  For each point, compute z(R) and then θ(R), then lifetime_s.
  Write a CSV file with columns "R_initial_um", "lifetime_s".
  Output file: /app/outputs/droplet_lifetime.csv
- Output file: `/app/outputs/droplet_lifetime.csv`
- Format: csv
- Contract: CSV with columns: R_initial_um (float, micrometers), lifetime_s (float, seconds). At least 20 rows covering the range 0.01 to 100 µm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/characteristic_params.json`
- `/app/outputs/psychrometric_temperature.csv`
- `/app/outputs/droplet_lifetime.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### characteristic_params.json
- path: `/app/outputs/characteristic_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Characteristic model parameters for water computed from analytical definitions using given physical properties.
- schema:
  - `type`: object
  - `required`:
    - `a`: number
    - `b`: number
    - `tau`: number
    - `beta`: number
  - `units`:
    - `a`: dimensionless
    - `b`: nm
    - `tau`: microseconds
    - `beta`: dimensionless
  - `description`: Characteristic dimensionless parameters a and beta, length scale b in nm, time scale tau in microseconds.

### psychrometric_temperature.csv
- path: `/app/outputs/psychrometric_temperature.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Psychrometric temperature difference for two near-saturation ambient humidity values.
- schema:
  - `type`: table
  - `required_columns`: `f0`, `z_inf`
  - `units`:
    - `f0`: dimensionless
    - `z_inf`: dimensionless
  - `description`: Relative humidity f0 and corresponding psychrometric relative temperature difference z_inf.

### droplet_lifetime.csv
- path: `/app/outputs/droplet_lifetime.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Droplet lifetime as a function of initial radius computed from the analytical model.
- schema:
  - `type`: table
  - `required_columns`: `R_initial_um`, `lifetime_s`
  - `units`:
    - `R_initial_um`: micrometers
    - `lifetime_s`: seconds
  - `description`: Initial droplet radius in micrometers and complete evaporation lifetime in seconds.

Notes: All outputs are deterministic functions of the given physical constants and input conditions; they are scored by exact_match against the paper's reported values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "characteristic_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a": "number",
          "b": "number",
          "tau": "number",
          "beta": "number"
        },
        "units": {
          "a": "dimensionless",
          "b": "nm",
          "tau": "microseconds",
          "beta": "dimensionless"
        },
        "description": "Characteristic dimensionless parameters a and beta, length scale b in nm, time scale tau in microseconds."
      },
      "description": "Characteristic model parameters for water computed from analytical definitions using given physical properties."
    },
    {
      "file": "psychrometric_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "f0",
          "z_inf"
        ],
        "units": {
          "f0": "dimensionless",
          "z_inf": "dimensionless"
        },
        "description": "Relative humidity f0 and corresponding psychrometric relative temperature difference z_inf."
      },
      "description": "Psychrometric temperature difference for two near-saturation ambient humidity values."
    },
    {
      "file": "droplet_lifetime.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R_initial_um",
          "lifetime_s"
        ],
        "units": {
          "R_initial_um": "micrometers",
          "lifetime_s": "seconds"
        },
        "description": "Initial droplet radius in micrometers and complete evaporation lifetime in seconds."
      },
      "description": "Droplet lifetime as a function of initial radius computed from the analytical model."
    }
  ],
  "notes": "All outputs are deterministic functions of the given physical constants and input conditions; they are scored by exact_match against the paper's reported values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently evaluates each scored output artifact. For each artifact the verifier checks that the file format and required columns/keys match the contract, then compares your computed numerical values to reference values obtained from the same model equations with the same inputs. The final reward is a weighted combination of the per‑step scores; simply reporting a plausible number is not sufficient – the verifier recomputes or cross‑checks the values to ensure they correctly follow from the evaporation model. Tolerances and exact weights are not disclosed.
