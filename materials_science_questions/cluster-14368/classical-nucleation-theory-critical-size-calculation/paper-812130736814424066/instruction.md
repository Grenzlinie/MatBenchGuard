# Supersaturation and Droplet Growth Kinetics for Laser-Induced Clouding of Aqueous Fog

## Problem background
When a pulsed CO₂ laser irradiates a fine‑droplet aqueous fog at energy densities below the total‑clearing threshold, the fog partially evaporates but subsequently undergoes clouding due to heterogeneous recondensation of vapor onto residual particles. To understand this clouding, a theoretical model was developed that describes the diffusive and thermal relaxation of explosion products and predicts the resulting supersaturation, the maximum size that recondensed droplets can reach, and the time required for their growth. This task is to compute these three quantities for a representative experimental scenario using the model's analytical expressions.

## Approach
The model treats the fog as composed of water droplets that after explosive evaporation leave behind final spheres containing a two‑phase mixture of vapor and homogeneously nucleated fine particles. During relaxation, mass and energy transfer between these spheres and the surrounding air leads to a uniform supersaturation δ₀⁰ that depends on the initial water content, ambient temperature, temperature of the explosion products, and thermodynamic and transport properties of water vapor and air. Given this supersaturation, the maximum radius a₀ that a droplet can attain by condensing the available vapor is determined by the initial particle concentration and the saturated vapor density. The growth of a droplet from its initial radius r₀ to a fraction of a₀ is described by a kinetic equation that integrates to an implicit relation between time and radius, which can be inverted to find the time needed to reach, e.g., 0.9 a₀.

The computation uses standard physical constants (diffusion coefficient, thermal conductivity, specific heats, density of air, latent heat of evaporation, gas constant of water vapor) that are publicly available from reference handbooks. The experimental parameters are given: water content 1.9 g/m³, initial temperature 293 K, explosion‑product temperature in the range 373–600 K, fog droplet concentration 3.3×10⁴ cm⁻³, final particle concentration after evaporation 2×10⁹ cm⁻³, initial particle radius 0.24 μm, and evaporation coefficient 0.03. Your task is to implement the analytical formulas, look up the necessary constants, and compute the three quantities.

## Reproduction target
Produce the following three output files under /app/outputs:

- supersaturation.json containing the dimensionless supersaturation δ₀⁰.
- max_radius.json containing the maximum droplet radius a₀ in micrometers.
- growth_time.json containing the time to reach 0.9 a₀ in microseconds.

Each file must be a valid JSON object following the schema specified in the Output contract section (e.g., {"delta0": <number>}, {"a0_microns": <number>}, {"t_90_microsec": <number>}).

## Assets

- Standard physical properties of water vapor and air

## Workflow steps

### Step 1: Compute supersaturation δ₀⁰
- Role: scored
- Action: Using the given experimental parameters (water content q = 1.9 g/m³, initial temperature T = 293 K, explosion product temperature T_V in the range 373–600 K, and the saturated vapor concentration ρ₀ at T) and standard physical constants (isobaric specific heats of vapor and air, air density, latent heat of evaporation, gas constant of water vapor), compute the dimensionless supersaturation δ₀⁰ from the analytical model derived in the paper. The model accounts for diffusive and thermal relaxation of explosion products and expresses supersaturation as a function of the listed parameters.
- Output file: `/app/outputs/supersaturation.json`
- Format: json
- Contract: { "type": "object", "properties": { "delta0": { "type": "number", "description": "dimensionless supersaturation value" } }, "required": ["delta0"] }
- Scoring: scored by hidden verifier

### Step 2: Compute maximum droplet radius a₀
- Role: scored
- Action: Using the supersaturation δ₀⁰ from the previous step, the initial particle radius (r₀ = 0.24 μm), the particle concentration (N = 2 × 10⁹ cm⁻³), and the required physical constants, compute the maximum radius a₀ that droplets can attain under the given supersaturation. Apply the analytical expression derived in the paper that relates a₀ to supersaturation, initial radius, particle concentration, saturated vapor concentration, and thermodynamic parameters. Report the radius in micrometers.
- Output file: `/app/outputs/max_radius.json`
- Format: json
- Contract: { "type": "object", "properties": { "a0_microns": { "type": "number", "description": "maximum droplet radius in micrometers" } }, "required": ["a0_microns"] }
- Scoring: scored by hidden verifier

### Step 3: Compute droplet growth time to 0.9a₀
- Role: scored
- Action: Using the computed supersaturation δ₀⁰, maximum radius a₀, initial radius r₀, particle concentration N, evaporation coefficient α = 0.03, and the necessary transport and thermodynamic constants, solve the droplet growth kinetics equations to find the time required for a droplet to reach 0.9a₀. The growth is described by a coupled system that can be integrated to a relation F(r) – F(r₀) = C t, where F is a known function. Evaluate this relation for r = 0.9 a₀ and report the time in microseconds.
- Output file: `/app/outputs/growth_time.json`
- Format: json
- Contract: { "type": "object", "properties": { "t_90_microsec": { "type": "number", "description": "growth time to 0.9*a0 in microseconds" } }, "required": ["t_90_microsec"] }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/supersaturation.json`
- `/app/outputs/max_radius.json`
- `/app/outputs/growth_time.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### supersaturation.json
- path: `/app/outputs/supersaturation.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed supersaturation δ₀⁰ for the clouding scenario.
- schema:
  - `type`: object
  - `properties`:
    - `delta0`:
      - `type`: number
      - `description`: dimensionless supersaturation value
  - `required`: `delta0`

### max_radius.json
- path: `/app/outputs/max_radius.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Maximum droplet radius a₀ achievable under the given supersaturation.
- schema:
  - `type`: object
  - `properties`:
    - `a0_microns`:
      - `type`: number
      - `description`: maximum droplet radius in micrometers
  - `required`: `a0_microns`

### growth_time.json
- path: `/app/outputs/growth_time.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Droplet growth time to 0.9 of the maximum radius.
- schema:
  - `type`: object
  - `properties`:
    - `t_90_microsec`:
      - `type`: number
      - `description`: time to reach 0.9*a0 in microseconds
  - `required`: `t_90_microsec`

Notes: All three quantities are numerically recomputed by the hidden checker using the paper's analytical expressions with a gold reference set of constants and input parameters. The agent must implement the three formulas and output the numerical results. Scattering cross-section and optical thickness are omitted as they require additional Mie theory parameters not fully specified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "supersaturation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "delta0": {
            "type": "number",
            "description": "dimensionless supersaturation value"
          }
        },
        "required": [
          "delta0"
        ]
      },
      "description": "Computed supersaturation δ₀⁰ for the clouding scenario."
    },
    {
      "file": "max_radius.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "a0_microns": {
            "type": "number",
            "description": "maximum droplet radius in micrometers"
          }
        },
        "required": [
          "a0_microns"
        ]
      },
      "description": "Maximum droplet radius a₀ achievable under the given supersaturation."
    },
    {
      "file": "growth_time.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "t_90_microsec": {
            "type": "number",
            "description": "time to reach 0.9*a0 in microseconds"
          }
        },
        "required": [
          "t_90_microsec"
        ]
      },
      "description": "Droplet growth time to 0.9 of the maximum radius."
    }
  ],
  "notes": "All three quantities are numerically recomputed by the hidden checker using the paper's analytical expressions with a gold reference set of constants and input parameters. The agent must implement the three formulas and output the numerical results. Scattering cross-section and optical thickness are omitted as they require additional Mie theory parameters not fully specified."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently recomputes each quantity using the same physical model and a reference set of inputs and constants. For each of the three output files, the verifier compares your reported value to the reference value and assigns a partial score based on how close they are. The partial scores are then combined (with the three quantities carrying roughly equal weight) into a final reward in [0,1]. You must implement the physics honestly; simply reporting a known number without performing the computation will not yield a high score, because the verifier recomputes from scratch and the tolerances are set to require a correct implementation.
