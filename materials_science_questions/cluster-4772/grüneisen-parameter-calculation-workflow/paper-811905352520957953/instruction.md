# Computation of elastic constants and anharmonic properties of Cu–Al–Ni β-phase shape memory alloy

## Problem background
Cu–Al–Ni is a technologically important shape memory alloy that undergoes a martensitic transformation from a high-temperature austenite phase (β-phase, bcc structure with space group Fm-3m). The elastic and anharmonic properties of the austenite phase govern its mechanical behaviour and the tendency towards transformation. Key quantities include the complete set of second-order elastic constants (SOECs) and third-order elastic constants (TOECs), aggregate properties (bulk modulus, shear modulus, Cauchy pressure, elastic anisotropy), pressure derivatives of the SOECs, mode Grüneisen parameters of long-wavelength acoustic phonons, and the low-temperature limit of lattice thermal expansion. This task requires computing all of these quantities for the β-phase of a Cu–Al–Ni alloy from an atomistic model, using only the crystal structure and experimentally reported elastic constants as input.

## Approach
The calculation uses Keating’s approach for interatomic potentials in a bcc crystal. Two-body interactions are considered up to second-nearest neighbours and three-body interactions among nearest neighbours. The potential energy is expressed in terms of six parameters: second-order parameters α, λ, σ (GPa) and third-order parameters β, ζ, ν (TPa). Analytical expressions relate the elastic constants (SOECs C11, C12, C44 and TOECs C111, C112, C123, C144, C155, C456) to these parameters and the lattice parameter a. First, a least-squares fit is performed using the provided experimental SOEC and TOEC values to determine the six potential parameters. Then, from the fitted parameters, the SOECs and TOECs are re-evaluated, and aggregate properties—longitudinal modulus CL, shear modulus C′, bulk modulus K, Cauchy pressure P, and Zener anisotropy factor A—are derived. Using the resulting SOECs and TOECs, the pressure derivatives dC11/dp, dC12/dp, dC44/dp are computed via finite strain theory. Next, the Christoffel equation is solved for the acoustic wave velocities v_j(θ,φ), and the mode Grüneisen parameters γ_j(θ,φ) for the three acoustic branches are obtained within the quasi-harmonic approximation. These are evaluated at the high-symmetry directions [001], [110], [111] and in the (010) plane from 0° to 90° in 5° steps. Finally, the low-temperature limit of thermal expansion γ_L is computed by numerical integration of the inverse cube of the sound velocities weighted by the mode Grüneisen parameters over the solid angle. The Anderson–Grüneisen parameter δ is obtained from the bulk modulus pressure derivative using the calculated SOECs and TOECs.

## Reproduction target
Implement the Keating model for a bcc crystal as described. Use the lattice parameter a = 5.84 Å and the following experimental elastic constants: SOECs C11 = 142.38 GPa, C12 = 124.10 GPa, C44 = 95.24 GPa; TOECs C111 = −1.65 TPa, C112 = −0.62 TPa, C123 = −0.48 TPa, C144 = −0.60 TPa, C155 = −0.69 TPa, C456 = −0.56 TPa. Perform a least-squares fit to obtain the six potential parameters and write them to fitted_potential_params.json. Then, using the fitted parameters, compute and output: the SOECs and aggregate properties (soecs_and_aggregates.csv); the six TOECs (toecs.csv); the pressure derivatives (pressure_derivatives.csv); the mode Grüneisen parameters for the specified directions and angles (mode_gruneisen_params.csv); and the values of γ_L and δ (gamma_L_and_delta.json). Each output must follow the format and schema defined in the Output contract.

## Assets

- Lattice parameter for Cu-14.3%Al-4.1%Ni β-phase: Standard crystallographic reference (obtainable from ICSD or literature); approximate value a ≈ 5.84 Å
- Experimental second-order and third-order elastic constants: Provided in the task instruction (values from Sedlak et al. 2005 and Landa et al. 2004)

## Workflow steps

### Step 1: Fit potential parameters
- Role: scored (load-bearing)
- Action: Using the provided experimental SOECs (C11, C12, C44) and TOECs (C111, C112, C123, C144, C155, C456), the lattice parameter, and the Keating-derived analytical expressions linking elastic constants to potential parameters for a bcc crystal with two-body interactions up to second neighbours and three-body interactions among nearest neighbours, perform a least-squares fit to determine the six potential parameters α, λ, σ (in GPa) and β, ζ, ν (in TPa). Output the fitted parameters.
- Output file: `/app/outputs/fitted_potential_params.json`
- Format: json
- Contract: {"alpha_GPa": numeric, "lambda_GPa": numeric, "sigma_GPa": numeric, "beta_TPa": numeric, "zeta_TPa": numeric, "nu_TPa": numeric}
- Scoring: scored by hidden verifier

### Step 2: Compute second-order elastic constants and aggregate properties
- Role: scored
- Action: From the fitted potential parameters and lattice parameter, compute the second-order elastic constants C11, C12, C44 using the Keating model expressions. Then derive the longitudinal modulus C_L, shear modulus C', bulk modulus K, Cauchy pressure P, and anisotropy factor A. Save all values.
- Output file: `/app/outputs/soecs_and_aggregates.csv`
- Format: csv
- Contract: required columns: property (string), value_GPa_or_dimensionless (numeric). Properties include C11, C12, C44, C_L, C_prime, K, P, A.
- Scoring: scored by hidden verifier

### Step 3: Compute third-order elastic constants
- Role: scored
- Action: From the fitted potential parameters and lattice parameter, compute the six third-order elastic constants C111, C112, C123, C144, C155, C456 using the Keating model expressions. Save the values in TPa.
- Output file: `/app/outputs/toecs.csv`
- Format: csv
- Contract: required columns: constant (string), value_TPa (numeric). Constants: C111, C112, C123, C144, C155, C456.
- Scoring: scored by hidden verifier

### Step 4: Compute pressure derivatives of SOECs
- Role: scored
- Action: Using the computed SOECs and TOECs, calculate the pressure derivatives dC11/dp, dC12/dp, dC44/dp from finite strain theory. Output the derivatives.
- Output file: `/app/outputs/pressure_derivatives.csv`
- Format: csv
- Contract: required columns: derivative (string), value (numeric). Derivatives: dC11_dp, dC12_dp, dC44_dp.
- Scoring: scored by hidden verifier

### Step 5: Compute mode Grüneisen parameters
- Role: scored
- Action: Solve the Christoffel equation for acoustic wave velocities using the SOECs. Compute the mode Grüneisen parameters γ_j(θ,φ) for the three acoustic branches using the quasi-harmonic approximation. Evaluate and output γ_j at the high-symmetry directions [001], [110], [111] and for the (010) plane from 0° to 90° in steps of 5°.
- Output file: `/app/outputs/mode_gruneisen_params.csv`
- Format: csv
- Contract: required columns: direction (string, e.g. [001], [110], [111], (010)), angle_deg (number, 0 for fixed directions), mode (string: qT1, qT2, qL), gamma (numeric).
- Scoring: scored by hidden verifier

### Step 6: Compute low-temperature limit and Anderson–Grüneisen parameter
- Role: scored
- Action: From the mode Grüneisen parameters and acoustic wave velocities, compute the low-temperature limit of thermal expansion γ_L by numerical integration over solid angle. Compute the Anderson–Grüneisen parameter δ from the bulk modulus pressure derivative using the SOECs and TOECs. Output both values.
- Output file: `/app/outputs/gamma_L_and_delta.json`
- Format: json
- Contract: {"gamma_L": numeric, "delta": numeric}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_potential_params.json`
- `/app/outputs/soecs_and_aggregates.csv`
- `/app/outputs/toecs.csv`
- `/app/outputs/pressure_derivatives.csv`
- `/app/outputs/mode_gruneisen_params.csv`
- `/app/outputs/gamma_L_and_delta.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_potential_params.json
- path: `/app/outputs/fitted_potential_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted second-order and third-order potential parameters.
- schema:
  - `type`: object
  - `required`: `alpha_GPa`, `lambda_GPa`, `sigma_GPa`, `beta_TPa`, `zeta_TPa`, `nu_TPa`
  - `units`:
    - `alpha_GPa`: GPa
    - `lambda_GPa`: GPa
    - `sigma_GPa`: GPa
    - `beta_TPa`: TPa
    - `zeta_TPa`: TPa
    - `nu_TPa`: TPa

### soecs_and_aggregates.csv
- path: `/app/outputs/soecs_and_aggregates.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Second-order elastic constants C11, C12, C44 and aggregate properties (C_L, C_prime, bulk modulus K, Cauchy pressure P, anisotropy factor A).
- schema:
  - `type`: table
  - `required_columns`: `property`, `value_GPa_or_dimensionless`
  - `units`:
    - `value_GPa_or_dimensionless`: GPa for moduli; dimensionless for anisotropy factor A

### toecs.csv
- path: `/app/outputs/toecs.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Third-order elastic constants C111, C112, C123, C144, C155, C456.
- schema:
  - `type`: table
  - `required_columns`: `constant`, `value_TPa`
  - `units`:
    - `value_TPa`: TPa

### pressure_derivatives.csv
- path: `/app/outputs/pressure_derivatives.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Pressure derivatives of second-order elastic constants: dC11/dp, dC12/dp, dC44/dp.
- schema:
  - `type`: table
  - `required_columns`: `derivative`, `value`
  - `units`: object

### mode_gruneisen_params.csv
- path: `/app/outputs/mode_gruneisen_params.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mode Grüneisen parameters for acoustic branches at high-symmetry directions and in the (010) plane.
- schema:
  - `type`: table
  - `required_columns`: `direction`, `angle_deg`, `mode`, `gamma`
  - `units`:
    - `gamma`: dimensionless
    - `angle_deg`: degrees

### gamma_L_and_delta.json
- path: `/app/outputs/gamma_L_and_delta.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Low-temperature limit of thermal expansion and Anderson–Grüneisen parameter.
- schema:
  - `type`: object
  - `required`: `gamma_L`, `delta`
  - `units`:
    - `gamma_L`: dimensionless
    - `delta`: dimensionless

Notes: All quantities are compared to hidden paper-reported reference values with appropriate tolerances. The agent must produce every listed file; missing files score zero for that step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_potential_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "alpha_GPa",
          "lambda_GPa",
          "sigma_GPa",
          "beta_TPa",
          "zeta_TPa",
          "nu_TPa"
        ],
        "units": {
          "alpha_GPa": "GPa",
          "lambda_GPa": "GPa",
          "sigma_GPa": "GPa",
          "beta_TPa": "TPa",
          "zeta_TPa": "TPa",
          "nu_TPa": "TPa"
        }
      },
      "description": "Fitted second-order and third-order potential parameters."
    },
    {
      "file": "soecs_and_aggregates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "value_GPa_or_dimensionless"
        ],
        "units": {
          "value_GPa_or_dimensionless": "GPa for moduli; dimensionless for anisotropy factor A"
        }
      },
      "description": "Second-order elastic constants C11, C12, C44 and aggregate properties (C_L, C_prime, bulk modulus K, Cauchy pressure P, anisotropy factor A)."
    },
    {
      "file": "toecs.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "constant",
          "value_TPa"
        ],
        "units": {
          "value_TPa": "TPa"
        }
      },
      "description": "Third-order elastic constants C111, C112, C123, C144, C155, C456."
    },
    {
      "file": "pressure_derivatives.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "derivative",
          "value"
        ],
        "units": {}
      },
      "description": "Pressure derivatives of second-order elastic constants: dC11/dp, dC12/dp, dC44/dp."
    },
    {
      "file": "mode_gruneisen_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "direction",
          "angle_deg",
          "mode",
          "gamma"
        ],
        "units": {
          "gamma": "dimensionless",
          "angle_deg": "degrees"
        }
      },
      "description": "Mode Grüneisen parameters for acoustic branches at high-symmetry directions and in the (010) plane."
    },
    {
      "file": "gamma_L_and_delta.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "gamma_L",
          "delta"
        ],
        "units": {
          "gamma_L": "dimensionless",
          "delta": "dimensionless"
        }
      },
      "description": "Low-temperature limit of thermal expansion and Anderson–Grüneisen parameter."
    }
  ],
  "notes": "All quantities are compared to hidden paper-reported reference values with appropriate tolerances. The agent must produce every listed file; missing files score zero for that step."
}
```

## How you are scored
A hidden verifier independently inspects each output file. It compares the numerical values you submit to reference results (derived from the published literature) using appropriate tolerances. Each workflow step carries a preassigned weight, and your final reward is the weighted combination of the per-step scores. A step that produces a missing or unparseable file receives zero weight. The comparison policy is monotonic: results within tolerance earn full credit; deviations beyond tolerance reduce credit gradually. You are not required to guess any tolerance or reference value—just execute the described workflow and produce the requested artifacts.
