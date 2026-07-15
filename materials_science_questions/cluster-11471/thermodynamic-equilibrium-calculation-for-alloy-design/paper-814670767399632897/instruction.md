# Thermodynamic and kinetic modeling of carbide precipitation in a refractory alloy

## Problem background
The 45Cr26Ni33Si2Nb2 refractory alloy is used in pyrolysis furnaces at operating temperatures between 800 and 1100 °C. During long‑term high‑temperature exposure the alloy's phase composition changes as carbon reacts with alloying elements, forming carbides (Cr23C6, NbC) and, under certain conditions, a complex G‑phase. Predicting the equilibrium phase composition and the time evolution of these precipitates is critical for estimating material aging and the loss of mechanical properties. This task reproduces the thermodynamic‑kinetic model that computes the equilibrium carbide concentrations and the precipitation kinetics of Cr23C6, and determines the time required for the alloy to approach its stable state.

## Approach
First, the thermodynamic equilibrium is solved from the material balance and the equilibrium constants of the carbide‑forming reactions, assuming the G‑phase is absent. This yields equilibrium atomic fractions of carbon, chromium, niobium, and the carbide phases NbC and Cr23C6 at 800 and 1100 °C. Activity coefficients for carbon, chromium, and niobium in austenite are approximated using simple models as described in the resource list.

Next, a kinetic model for Cr23C6 precipitation is set up. The model describes the rate of redistribution of carbon into carbide as a function of the current concentrations, an equilibrium driving force, and a forward reaction rate constant that follows an Arrhenius form with a pre‑exponential factor k₀ and an activation energy Eₙ. Using experimental Cr23C6 mass fractions after 1000 h of aging at 800, 900, and 1000 °C, the unknown kinetic constants are estimated by solving an inverse problem. With the calibrated kinetics, the mass fraction of Cr23C6 is computed as a function of time for the four temperatures (800, 900, 1000, 1100 °C) by numerical integration of the rate equation. Finally, the stabilization time τ∗ is defined as the time needed for the Cr23C6 mass fraction to reach 99 % of its equilibrium value, and is calculated for each temperature.

## Reproduction target
1. **Equilibrium concentrations**: Compute the equilibrium atomic fractions [C]eq, [Cr]eq, [Nb]eq, [NbC]eq, and [Cr23C6]eq at 800 °C and 1100 °C, assuming no G‑phase, and report the intensity ratio i₅/i₁ based on initial concentrations.
2. **Rate constants**: Estimate the forward reaction rate constants k₀ (h⁻¹) and Eₙ (J/mol) for Cr23C6 precipitation by fitting the kinetic model to the experimentally measured Cr23C6 mass fractions after 1000 h at 800, 900, and 1000 °C.
3. **Kinetic curves**: Using the fitted k₀ and Eₙ, numerically integrate the kinetic model to produce the Cr23C6 mass fraction as a function of time at 800, 900, 1000, and 1100 °C, covering at least the time points 1000 h, 3200 h, and 5300 h.
4. **Stabilization time**: For each of the four temperatures, determine τ∗, the time (in hours) required for the Cr23C6 mass fraction to reach 99 % of its equilibrium value.

## Assets

- Alloy composition (45Cr26Ni33Si2Nb2)
- Equilibrium constants K1 and K5 at 800°C and 1100°C
- Activity coefficient models for carbon, chromium, and niobium in austenite
- Experimental EBSD phase composition data (Table 6)

## Workflow steps

### Step 1: Compute thermodynamic equilibrium concentrations
- Role: scored
- Action: Solve the material balance and equilibrium constant relations for reactions forming Cr23C6 and NbC at 800°C and 1100°C, using the given alloy composition, equilibrium constants, and activity coefficients. Assume no G-phase is present. Compute equilibrium atomic fractions of C, Cr, Nb, the molar fraction of NbC and Cr23C6, and the intensity ratio i5/i1 at initial conditions.
- Output file: `/app/outputs/equilibrium_concentrations.json`
- Format: json
- Contract: Array of objects: {temperature_C (number), C_eq (atomic fraction, number), Cr_eq (atomic fraction, number), Nb_eq (atomic fraction, number), NbC_eq (atomic fraction, number), Cr23C6_eq (atomic fraction, number), i5_over_i1 (number)}.
- Scoring: scored by hidden verifier

### Step 2: Estimate kinetic rate constants k0 and En
- Role: scored
- Action: Implement the kinetic model for Cr23C6 precipitation. Using the experimental Cr23C6 mass fractions at 800°C, 900°C, and 1000°C after 1000 h aging, solve the inverse problem to determine the forward rate constant frequency factor k0 (h⁻¹) and activation energy En (J/mol).
- Output file: `/app/outputs/rate_constants.json`
- Format: json
- Contract: Object: {k0 (number, h^-1), En (number, J/mol)}.
- Scoring: scored by hidden verifier

### Step 3: Compute Cr23C6 kinetic curves
- Role: scored (load-bearing)
- Action: Using the fitted k0 and En, numerically integrate the kinetic model to obtain the mass fraction of Cr23C6 as a function of time at 800, 900, 1000, and 1100°C, covering times up to at least 5000 h and including the specific aging times of 1000 h, 5300 h, and 3200 h where experimental data exist.
- Output file: `/app/outputs/kinetic_curve.csv`
- Format: csv
- Contract: CSV with header: temperature_C,time_h,Cr23C6_mass_fraction (numeric columns).
- Scoring: scored by hidden verifier

### Step 4: Calculate stabilization time τ*
- Role: scored
- Action: Define stabilization as the time required for the Cr23C6 mass fraction to reach 99% of its equilibrium value at each temperature. Using the fitted model, compute the stabilization time (hours) for 800, 900, 1000, and 1100°C.
- Output file: `/app/outputs/stabilization_time.csv`
- Format: csv
- Contract: CSV with header: temperature_C,tau_star_h (numeric columns).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_concentrations.json`
- `/app/outputs/rate_constants.json`
- `/app/outputs/kinetic_curve.csv`
- `/app/outputs/stabilization_time.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_concentrations.json
- path: `/app/outputs/equilibrium_concentrations.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium atomic fractions and intensity ratio at 800°C and 1100°C.
- schema:
  - `type`: array
  - `items`:
    - `temperature_C`: number
    - `C_eq`: number
    - `Cr_eq`: number
    - `Nb_eq`: number
    - `NbC_eq`: number
    - `Cr23C6_eq`: number
    - `i5_over_i1`: number

### rate_constants.json
- path: `/app/outputs/rate_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted forward reaction rate constants.
- schema:
  - `type`: object
  - `required`:
    - `k0`: number (h^-1)
    - `En`: number (J/mol)

### kinetic_curve.csv
- path: `/app/outputs/kinetic_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time evolution of Cr23C6 mass fraction at four temperatures.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `time_h`, `Cr23C6_mass_fraction`
  - `units`:
    - `temperature_C`: °C
    - `time_h`: hours
    - `Cr23C6_mass_fraction`: mass fraction (dimensionless)

### stabilization_time.csv
- path: `/app/outputs/stabilization_time.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Stabilization time (τ*) defined as time to reach 99% equilibrium Cr23C6.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `tau_star_h`
  - `units`:
    - `temperature_C`: °C
    - `tau_star_h`: hours

Notes: Activity coefficients may be approximated as described. The kinetic model may use numerical integration or the analytical approximation from the paper. The equilibrium calculation ignores the G-phase. Results are compared to paper-reported values within tolerances appropriate for different implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_concentrations.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "temperature_C": "number",
          "C_eq": "number",
          "Cr_eq": "number",
          "Nb_eq": "number",
          "NbC_eq": "number",
          "Cr23C6_eq": "number",
          "i5_over_i1": "number"
        }
      },
      "description": "Equilibrium atomic fractions and intensity ratio at 800°C and 1100°C."
    },
    {
      "file": "rate_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "k0": "number (h^-1)",
          "En": "number (J/mol)"
        }
      },
      "description": "Fitted forward reaction rate constants."
    },
    {
      "file": "kinetic_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_C",
          "time_h",
          "Cr23C6_mass_fraction"
        ],
        "units": {
          "temperature_C": "°C",
          "time_h": "hours",
          "Cr23C6_mass_fraction": "mass fraction (dimensionless)"
        }
      },
      "description": "Time evolution of Cr23C6 mass fraction at four temperatures."
    },
    {
      "file": "stabilization_time.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_C",
          "tau_star_h"
        ],
        "units": {
          "temperature_C": "°C",
          "tau_star_h": "hours"
        }
      },
      "description": "Stabilization time (τ*) defined as time to reach 99% equilibrium Cr23C6."
    }
  ],
  "notes": "Activity coefficients may be approximated as described. The kinetic model may use numerical integration or the analytical approximation from the paper. The equilibrium calculation ignores the G-phase. Results are compared to paper-reported values within tolerances appropriate for different implementations."
}
```

## How you are scored
A hidden verifier independently evaluates each of the four required output artifacts. For the equilibrium concentrations, the verifier compares your computed atomic fractions and the intensity ratio to reference values. The kinetic rate constants are compared against expected magnitudes derived from the model. The kinetic curves are checked at selected time points (including 1000 h and longer aging times) for consistency with experimentally observed mass fractions, and the stabilization times are compared to the time ranges predicted by the model. Each artifact carries a weight; the individual scores are combined into the final reward. Artifacts that are missing, incorrectly formatted, or contain values far from the physically plausible range will receive low or zero credit. Simply reporting the reference numbers without running the required computations will not pass the hidden checks.
