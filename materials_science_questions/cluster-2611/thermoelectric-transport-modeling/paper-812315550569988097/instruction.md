# Modeling the Thomson Effect on Thermoelectric Cooler Performance

## Problem background
Thermoelectric coolers pump heat from a cold side to a hot side via the Peltier effect when an electric current is applied. Their performance is limited by Joule heating within the semiconductors and by Fourier heat conduction from the hot to the cold side. The Thomson effect — heat absorbed or released by charge carriers moving through a temperature gradient — is often neglected but can redistribute internal heat generation and alter the temperature profile. This work analytically models a thermoelectric cooler including Fourier conduction, Joule heating, the Thomson effect, and linearized radiation/convection losses, and then numerically evaluates its performance. The problem is to compute how the Thomson effect influences the maximum attainable temperature difference and the maximum allowable heat load, and to compute the temperature difference versus operating current for a specific exemplar thermocouple.

## Approach
A one-dimensional steady‑state thermal model of a thermoelement (p‑ or n‑type) is used. The energy balance includes axial conduction, Joule heating, Thomson heat, and lateral radiation/convection losses (linearized). Assuming constant material properties (thermal conductivity λ, electrical conductivity σ, Thomson coefficient β), constant cross‑sectional area A and perimeter P, and a constant current I, the governing equation is a linear second‑order ODE.

For the limiting case where lateral losses are negligible (γ = 0), the temperature distribution simplifies significantly. The cooling power at the cold end (qc) can be expressed as:
qc = αₚₙ(Tc) I Tc − K̃ ΔT − I² R̃
where ΔT = Th − Tc, and the modified thermal conductance K̃ and modified electrical resistance R̃ are functions of the dimensionless operating current ξ = β I / K (with K = λA/L, R = L/(σA)). For identical p‑ and n‑type materials (except αₚ = −αₙ = α, βₚ = −βₙ = β > 0), the renormalisation functions are:
ηK(ξ) = ξ / (e^ξ − 1),
ηR(ξ) = 1 / (1 − e^ξ) + 1/ξ,
with K̃ = K ηK(ξ) + K ηK(−ξ) and R̃ = R ηR(ξ) + R ηR(−ξ).

**Maximum attainable temperature difference** – The optimum dimensionless current (ξₒₚₜ,T) that maximises ΔT under zero heat load (qc = 0) is found by solving an implicit equation. Once ξₒₚₜ,T is known, the corresponding Z ΔT_max (where Z = σ α² / λ is the figure‑of‑merit evaluated at Tc) is computed from a closed‑form relation.

**Maximum allowable heat load** – Similarly, the optimum current (ξₒₚₜ,N) that maximises the cooling power under the constraint ΔT = 0 is determined from another implicit equation, and the dimensionless maximum heat load N_max* = Z N_max / K is then obtained.

**Exemplar thermocouple** – For a specific set of material properties and geometry (σ = 0.1 (μΩ·m)⁻¹, λ = 1.6 W/(m·K), α(Tc=250 K) = 185 μV/K, β = 200 μV/K, L = 1 mm, A = 0.01 mm², P = 0.4 mm), with a linearised radiation/convection coefficient γ = 50 W/(m²·K), ambient T∞ = 300 K, cold‑side temperature Tc = 250 K, and no external heat load, the temperature difference ΔT is computed as a function of operating current I by solving qc(I, ΔT) = 0.

All implicit equations are solved numerically (root‑finding).

## Reproduction target
Reproduce three analytical predictions and one specific peak value:

1. **Maximum attainable temperature‑difference curves** – For each of six values of the material parameter α/β (0.2, 0.32, 0.512, 0.8192, 1.31072, 2.097152) and for a grid of ZTc values in [0.1, 1.0] (at least 10 points), compute the maximum attainable Z ΔT_max and save the results.

2. **Maximum allowable heat‑load curve** – For a grid of ZTh·β/α values in [0.1, 2.0] (at least 20 points), compute the dimensionless maximum allowable heat load Nmax* = (β²/α²)·(Z Nmax / K) and save the results.

3. **Example ΔT vs. I curve** – Using the exemplar thermocouple parameters given in the Approach, compute the temperature difference ΔT as a function of operating current I (from 0 to 0.1 A, at least 50 points) under zero external heat load, and save the (I, ΔT) pairs.

4. **Example maximum ΔT** – From the curve obtained in step 3, extract the maximum value of ΔT and save it as a JSON key‑value pair.

## Assets

- Python 3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement analytical model
- Role: process
- Action: Implement the one-dimensional steady-state thermal model of a thermoelectric cooler including Fourier conduction, Joule heating, Thomson effect, and linearized radiation/convection. Implement the derived closed-form temperature distribution, cooling power expression, and the formulas for modified thermal conductance and electrical resistance. This includes the auxiliary functions f, g, h and the simplified renormalization functions η_K, η_R for the γ=0 case, as well as the equations that determine the maximum attainable temperature difference and maximum allowable heat load.
- Evidence: none

### Step 2: Maximum attainable temperature difference curves
- Role: scored (load-bearing)
- Action: Using the implemented model, solve the implicit equation for the optimum dimensionless operating current that maximizes temperature difference. For each α/β ratio in {0.2, 0.32, 0.512, 0.8192, 1.31072, 2.097152} and for a grid of ZTc values between 0.1 and 1.0 (at least 10 points), compute the corresponding maximum attainable temperature difference ZΔT_max. Write the results to results_maxdeltaT.csv.
- Output file: `/app/outputs/results_maxdeltaT.csv`
- Format: csv
- Contract: Columns: ZTc (float, dimensionless), alpha_over_beta (float, dimensionless), ZDeltaT_max (float, dimensionless). ZTc in [0.1, 1.0], alpha_over_beta one of the specified values, ZDeltaT_max >= 0.
- Scoring: scored by hidden verifier

### Step 3: Maximum allowable heat load curve
- Role: scored (load-bearing)
- Action: Solve the implicit equations that give the optimal dimensionless operating current for maximum heat load. For ZTh_beta_over_alpha values from 0.1 to 2.0 (at least 20 points), compute the dimensionless maximum allowable heat load Nmax_star. Write the results to results_maxheatload.csv.
- Output file: `/app/outputs/results_maxheatload.csv`
- Format: csv
- Contract: Columns: ZTh_beta_over_alpha (float, dimensionless), Nmax_star (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 4: Temperature difference vs current for example
- Role: scored
- Action: Using the specific material properties and geometry (σ=0.1 (μΩm)⁻¹, λ=1.6 W/mK, α=185 μV/K at Tc=250K, β=200 μV/K, L=1 mm, A=0.01 mm², P=0.4 mm, γ=50 W/m²K, T∞=300 K, Tc=250 K, with no external heat load), compute the net cooling power as a function of operating current I. For each I, find the temperature difference ΔT that yields q_c=0 (self‑sustaining operation). Sample at least 50 currents between 0 and 0.1 A. Write the (I, ΔT) pairs to example_F7_curve.csv.
- Output file: `/app/outputs/example_F7_curve.csv`
- Format: csv
- Contract: Columns: I_A (float, A), DeltaT_K (float, K).
- Scoring: scored by hidden verifier

### Step 5: Maximum ΔT from example
- Role: scored
- Action: From the curve generated in the previous step (or by direct numerical optimization of ΔT with respect to I), determine the maximum attainable temperature difference and write it to example_max_delta_T.json.
- Output file: `/app/outputs/example_max_delta_T.json`
- Format: json
- Contract: JSON object with key 'beta_200_max_delta_T_K' and a float value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_maxdeltaT.csv`
- `/app/outputs/results_maxheatload.csv`
- `/app/outputs/example_F7_curve.csv`
- `/app/outputs/example_max_delta_T.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_maxdeltaT.csv
- path: `/app/outputs/results_maxdeltaT.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Maximum attainable temperature difference ZΔT_max as a function of ZTc for several α/β ratios.
- schema:
  - `type`: table
  - `required_columns`: `ZTc`, `alpha_over_beta`, `ZDeltaT_max`

### results_maxheatload.csv
- path: `/app/outputs/results_maxheatload.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Dimensionless maximum allowable heat load Nmax_star as a function of ZThβ/α.
- schema:
  - `type`: table
  - `required_columns`: `ZTh_beta_over_alpha`, `Nmax_star`

### example_F7_curve.csv
- path: `/app/outputs/example_F7_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature difference ΔT vs operating current I for the exemplar thermocouple.
- schema:
  - `type`: table
  - `required_columns`: `I_A`, `DeltaT_K`

### example_max_delta_T.json
- path: `/app/outputs/example_max_delta_T.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Maximum temperature difference from the exemplar curve.
- schema:
  - `type`: object
  - `required`:
    - `beta_200_max_delta_T_K`: number

Notes: The hidden checker will recompute the analytical expressions using the same input grids and material parameters to generate gold values, and compare the agent's submitted quantities within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_maxdeltaT.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ZTc",
          "alpha_over_beta",
          "ZDeltaT_max"
        ]
      },
      "description": "Maximum attainable temperature difference ZΔT_max as a function of ZTc for several α/β ratios."
    },
    {
      "file": "results_maxheatload.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ZTh_beta_over_alpha",
          "Nmax_star"
        ]
      },
      "description": "Dimensionless maximum allowable heat load Nmax_star as a function of ZThβ/α."
    },
    {
      "file": "example_F7_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "I_A",
          "DeltaT_K"
        ]
      },
      "description": "Temperature difference ΔT vs operating current I for the exemplar thermocouple."
    },
    {
      "file": "example_max_delta_T.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "beta_200_max_delta_T_K": "number"
        }
      },
      "description": "Maximum temperature difference from the exemplar curve."
    }
  ],
  "notes": "The hidden checker will recompute the analytical expressions using the same input grids and material parameters to generate gold values, and compare the agent's submitted quantities within tolerance."
}
```

## How you are scored
A hidden verifier independently solves the same analytical equations using the same material parameters and input grids to generate a reference gold. For each scored artifact, the verifier compares your submitted values against the gold within a prescribed tolerance. The overall reward is a weighted sum of the scores from the individual stages. Merely reporting the paper's final numbers is not sufficient; you must generate the required output files so the verifier can inspect the computed quantities. The tolerances and exact weighting are not disclosed.
