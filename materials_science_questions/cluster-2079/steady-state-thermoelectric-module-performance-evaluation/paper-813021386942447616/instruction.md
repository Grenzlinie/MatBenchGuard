# Steady-state hybrid solar still performance model

## Problem background
A single-basin solar still is modified by immersing photovoltaic (PV) cells in the saline water and installing thermoelectric generators (TEMs) at the basin bottom. An external finned condensing chamber is added. The system harvests solar energy to simultaneously produce distilled water and electricity. A steady-state mathematical model couples the thermal and electrical behaviour of the water+PV subsystem, the glass/condenser assembly, and the TEM cold side. The model yields surface temperatures from which performance metrics — distillation rate, still efficiency, system efficiency, and total power output — can be derived.

## Approach

The system is divided into three control volumes:
1. Water basin + PV cells (subsystem 1)
2. Transparent glass cover / condensing chamber assembly (subsystem 2)
3. Cold side of thermoelectric generators (subsystem 3)

The unknown temperatures are:
- T_w : water (and PV) temperature (°C)
- T_g : glass cover temperature (°C)
- T_c : TEM cold‑side temperature (°C)

A fourth intermediate temperature, the effective glass/condenser temperature T_g,e, is defined as:
T_g,e = (T_g A_g + T_a A_c)/(A_g + A_c)   (24)
and the effective area:
A_g,e = A_g + A_c   (25)

### Subsystem 1 (water + PV)
Energy balance:  \dot{E}_{in,1} - \dot{E}_{out,1} - \dot{E}_{gen,1} = 0   (1)

\dot{E}_{in,1} = Q_{S,pv} + Q_{S,w}
Q_{S,pv} = τ_g τ_w G A_{pv}   (3)
Q_{S,w} = τ_g α_w G A_w   (4)

\dot{E}_{out,1} = Q_{c,wg} + Q_{r,wg} + Q_{ev,wg} + Q_h   (5)
\dot{E}_{gen,1} = η_{pv} Q_{S,pv}   (6)

Convective heat transfer from water to glass:
Q_{c,wg} = h_{c,wg} A_w (T_w - T_{g,e})   (7)
with Dunkle's coefficient:
h_{c,wg} = 0.884 [ T_w - T_{g,e} + (P_w - P_{g,e})(T_w+273)/(268.9×10³ - P_w) ]^{1/3}   (8)
where saturation pressures (N/m²):
P_w = exp( 25.317 - 5144/(273+T_w) )   (9)
P_{g,e} = exp( 25.317 - 5144/(273+T_{g,e}) )   (10)

Radiative heat transfer:
Q_{r,wg} = h_{r,wg} A_w (T_w - T_g)   (11)
h_{r,wg} = ε_{eff} σ [ (T_w+273)² + (T_g+273)² ] [ (T_w+273) + (T_g+273) ]   (12)
ε_{eff} = 1 / (1/ε_g + 1/ε_w - 1)   (13)
with σ = 5.67 × 10⁻⁸ W/m²K⁴.

Evaporative heat transfer:
Q_{ev,wg} = h_{ev,wg} A_w (T_w - T_{g,e})   (14)
h_{ev,wg} = 16.273 × 10⁻³ × h_{c,wg} × (P_w - P_{g,e})/(T_w - T_{g,e})   (15)

### Subsystem 2 (glass/condenser)
Energy balance:  \dot{E}_{in,2} - \dot{E}_{out,2} = 0   (16)
\dot{E}_{in,2} = α_g G A_g + Q_{c,wg} + Q_{r,wg} + Q_{ev,wg}   (17)
\dot{E}_{out,2} = Q_{c,ga} + Q_{r,ga}   (18)

Convection to ambient:
Q_{c,ga} = h_{c,ga} A_{g,e} (T_{g,e} - T_a)   (19)
h_{c,ga} = 2.8 + 3.0 V   (20)

Radiation to ambient:
Q_{r,ga} = h_{r,ga} A_g (T_{g,e} - T_a)   (21)
h_{r,ga} = ε_g σ [ (T_{g,e}+273)⁴ - (T_{sky}+273)⁴ ] / (T_{g,e} - T_a)   (22)
Sky temperature (Eq. 23):
T_{sky} = 0.0552 × (T_a + 273)^{1.5} - 273

### Subsystem 3 (TEM cold side)
Energy balance:  \dot{E}_{in,3} - \dot{E}_{out,3} = 0   (26)
\dot{E}_{in,3} = Q_c   (27)
\dot{E}_{out,3} = Q_{t,ca}   (28)

Heat loss from cold side:
Q_{t,ca} = h_{tt,ca} A_{cf} (T_c - T_a)   (29)
h_{tt,ca} = ( L_b/K_b + 1/h_{t,ca} )^{-1}   (30)

### Thermoelectric module equations
Total electrical resistance of n pairs (series):
R = n [ (σ_p A_p / L_p)⁻¹ + (σ_N A_N / L_N)⁻¹ ]   (31)

Total thermal conductance of n pairs (parallel):
K = n [ λ_p A_p / L_p + λ_N A_N / L_N ]   (32)

Heat absorbed by hot side (T_h = T_b):
Q_h = n ᾱ T_h I + K (T_h - T_c) - 0.5 I² R   (33)
Heat rejected at cold side:
Q_c = n ᾱ T_c I + K (T_h - T_c) + 0.5 I² R   (34)

The TEMs operate at matched load (R_L = R). The generated direct current is:
I = ᾱ (T_h - T_c) / (2 R)   (obtained from circuit relations)

The power output of the TEMs:
P_L = I² R_L = I² R = Q_h - Q_c   (35)

### Coupling between basin and TEM hot side
The heat leaving the water to the basin, Q_h, also obeys the convective transport from water to the basin bottom:
Q_h = h_{c,bw} A_b (T_w - T_b)   (un‑numbered relation, with T_b = T_h)

### Output metrics
Distillation rate (kg/s):
ṁ = Q_{ev,wg} / i_{fg,w}   (36)

Still efficiency:
η_still = Q_{ev,wg} / ( G A_w - (P_L + \dot{E}_{gen,1}) )   (37)

System efficiency:
η_system = Q_{ev,wg} / (G A_w) + P_L / (G A_b) + \dot{E}_{gen,1} / (G A_{pv})   (38)

Total electrical power output:
P_output = \dot{E}_{gen,1} + P_L   (39)

### Fixed parameters and constants
The design parameters are as listed in the first part, together with the additional values:
- Latent heat of vaporization of water i_fg,w = 5.42 × 10⁶ J/kg  (value used in the paper’s simulation)
- PV module efficiency η_pv = 0.12
- All areas: A_w = A_b = A_pv = 1.2 m², A_g = 1.3 m², A_c = 1.8 m², A_cf = 1.2 m²
- The remaining design and thermoelectric parameters are unchanged from the initial description.

For a given ambient temperature T_a, solar irradiance G, and wind speed V, the three coupled equations are solved numerically (e.g., using a nonlinear solver) to obtain T_w, T_g,e, and T_c. From these temperatures, the distillation rate (ṁ), still efficiency (η_still), system efficiency (η_system), and total electrical power output (P_output) are computed using the heat transfer and thermoelectric relationships.

## Reproduction target
Using the provided design and thermoelectric parameters, solve the steady‑state model for two ambient conditions, both with G = 1000 W/m² and V = 5 m/s:
1. T_a = 10 °C
2. T_a = 35 °C

For each condition, compute and report the following four metrics:
- Distillation rate ṁ (kg/day)
- Still efficiency η_still (%)
- System efficiency η_system (%)
- Total electrical power output P_output (W)

Additionally, calculate the relative increase in distillation rate from the 10 °C case to the 35 °C case. Write all results to the specified JSON file (model_results.json) with the required structure.

## Assets

- scipy: scipy
- numpy: numpy

## Workflow steps

### Step 1: Solve the coupled energy balance equations
- Role: process
- Action: Implement the steady-state energy balance equations for the water+PV subsystem, effective glass/condenser subsystem, and TEM cold side using the correlations given in the paper (Dunkle convection, radiative, evaporative, ambient convective/radiative, thermoelectric heat flows). Use the fixed design parameters from Tables 1 and 2. Solve the nonlinear system numerically to obtain water temperature, glass temperature, and TEM cold-side temperature for two ambient conditions: Ta=10°C and Ta=35°C, each at G=1000 W/m² and wind speed 5 m/s. Record the solved temperatures as evidence in temperatures.json.
- Evidence: `/app/outputs/temperatures.json`

### Step 2: Compute performance metrics
- Role: scored (load-bearing)
- Action: From the solved temperatures and model parameters, calculate distillation rate (kg/day), still efficiency (%), system efficiency (%), and total power output (W) for both ambient temperatures. Write the results to model_results.json.
- Output file: `/app/outputs/model_results.json`
- Format: json
- Contract: JSON object with keys 'Ta10' and 'Ta35'. Each value is an object with numeric fields: 'mdot_kg_per_day' (float), 'eta_still_pct' (float), 'eta_system_pct' (float), 'P_output_W' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### model_results.json
- path: `/app/outputs/model_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Headline metrics (distillation rate, still efficiency, system efficiency, total power output) for two ambient temperature conditions.
- schema:
  - `type`: object
  - `required`:
    - `Ta10`:
      - `mdot_kg_per_day`: float
      - `eta_still_pct`: float
      - `eta_system_pct`: float
      - `P_output_W`: float
    - `Ta35`:
      - `mdot_kg_per_day`: float
      - `eta_still_pct`: float
      - `eta_system_pct`: float
      - `P_output_W`: float

Notes: The checker reads model_results.json and compares each metric for Ta35 to the paper’s reported values with appropriate tolerances, and verifies the relative increase in distillation from Ta10 to Ta35 is consistent with the claimed trend. This is a result-level comparison (T0).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "model_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Ta10": {
            "mdot_kg_per_day": "float",
            "eta_still_pct": "float",
            "eta_system_pct": "float",
            "P_output_W": "float"
          },
          "Ta35": {
            "mdot_kg_per_day": "float",
            "eta_still_pct": "float",
            "eta_system_pct": "float",
            "P_output_W": "float"
          }
        }
      },
      "description": "Headline metrics (distillation rate, still efficiency, system efficiency, total power output) for two ambient temperature conditions."
    }
  ],
  "notes": "The checker reads model_results.json and compares each metric for Ta35 to the paper’s reported values with appropriate tolerances, and verifies the relative increase in distillation from Ta10 to Ta35 is consistent with the claimed trend. This is a result-level comparison (T0)."
}
```

## How you are scored
A hidden verifier reads your model_results.json and extracts the four metrics for both temperature conditions. The metrics for T_a = 35 °C are compared to hidden reference values with appropriate tolerances (relative or absolute, depending on the metric). The relative increase in distillation rate between the two ambient temperatures is checked against an allowed range that reflects the expected behaviour of the system. The T_a = 10 °C metrics also contribute to the final score. Your reward is a weighted combination of these checks. You do not need to know the reference values; simply implement the model faithfully using the given parameters and report the computed results.
