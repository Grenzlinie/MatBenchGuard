# Steady-state thermoelectric module performance evaluation

## Problem background
Thermoelectric generators convert a temperature difference directly into electrical power. Their performance is limited by the trade-off between output power and conversion efficiency. Theory suggests that a boxcar-shaped (bandpass) electronic transmission function optimally balances this trade-off. However, engineering a heterostructure to realize such a transmission function in practice is challenging. One promising approach is to embed a resonant tunneling structure inside an electronic Fabry-Pérot cavity, where the cavity mirrors are rectangular potential barriers. By tuning the width and height of these cavity walls, one can modify the transmission lineshape. This work explores several cavity designs derived from a simple GaAs/AlGaAs heterostructure, and investigates how the resulting transmission function affects the thermoelectric performance metrics—both in the nonlinear (power, efficiency) and linear (power factor, Seebeck coefficient, figure-of-merit) regimes. The goal is to assess whether careful cavity engineering can improve the power-efficiency trade-off compared to a bare resonant tunneling device (RTD).

## Approach
The central device is a double-barrier resonant tunneling structure in a GaAs/AlGaAs heterostructure, modeled using a single-band effective mass approximation. To form the Fabry-Pérot cavity, two additional rectangular barriers are placed symmetrically around the central device; their width and height are varied according to a design guideline that relates the barrier dimensions. Four device configurations are considered: the baseline RTD (no cavity), and three cavity designs labeled FP-I (cavity walls of standard dimensions), FP-II, and FP-III (with progressively narrower and taller cavity walls). For each configuration, a 1D self-consistent NEGF-Poisson solver is implemented to compute the non-equilibrium potential profile and the energy-resolved transmission function T(E) under applied bias. The charge and heat current densities are then calculated using the Landauer formulas, incorporating contributions from all transverse modes via a 2D density of states. From these currents, the output power density P = J·V_app, conversion efficiency η = P/J_H^Q (normalized to Carnot efficiency), and linear-response coefficients (power factor, Seebeck coefficient, electronic figure-of-merit zT) are extracted as functions of applied voltage and contact Fermi level. The analysis yields key performance metrics for each device: maximum power, efficiency at maximum power, maximum efficiency, maximum power-efficiency product, peak power factor, peak zT, and the ranges of zT and Seebeck coefficient within a relevant Fermi level window. The complete workflow is split into two major steps: (1) NEGF-Poisson simulation to obtain the transmission functions, and (2) post-processing to compute and extract the thermoelectric metrics.

## Reproduction target
Your task is to implement the full simulation and analysis pipeline as described in the workflow steps. You must produce a single scored artifact, `/app/outputs/results.json`, containing the extracted thermoelectric performance metrics for all four device configurations. For each device (RTD, FP-I, FP-II, FP-III), the JSON object must include the following fields: maximum power density (P_max_MW_per_m2), efficiency at maximum power (eta_Pmax_percent), maximum efficiency (eta_max_percent), maximum power-efficiency product (PEP_max_MW_per_m2), maximum power factor (PF_max), maximum electronic figure-of-merit (zT_max), and the ranges of zT and Seebeck coefficient (zT_range, S_range_mV_per_K) within the contact Fermi level window E_f ≈ 4–7 k_BT. The ranges should be reported as strings of the form 'min-max' (e.g., '2.5-4.5'). All numerical values must be in the specified units. The checker expects the output to conform to the exact JSON schema described in the output contract; it will be scored based solely on the numbers and structure contained in this file. No other files will be scored.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Self-consistent NEGF-Poisson transmission simulation
- Role: process
- Action: Implement a 1D NEGF-Poisson solver within the effective-mass approximation for GaAs/AlGaAs heterostructures. For each device configuration (RTD, FP-I, FP-II, FP-III), compute the self-consistent potential profile and the non-equilibrium transmission function T(E) over the relevant energy and applied voltage ranges. The used device geometries, barrier heights, effective masses, contact temperatures, and discretization are taken from the paper's device parameters.
- Evidence: none

### Step 2: Compute thermoelectric performance metrics
- Role: scored (load-bearing)
- Action: Using the transmission functions T(E) from step 1, calculate charge current density J, heat current density J_H^Q, output power density P = J * V_app, and conversion efficiency η = P/J_H^Q (normalized to Carnot efficiency) for each device. From these quantities extract maximum power density P_max, efficiency at maximum power η(P_max), maximum efficiency η_max, maximum power-efficiency product PEP_max, power factor PF_max, figure-of-merit zT_max, and the ranges of zT and Seebeck coefficient S within the contact Fermi level window E_f ≈ 4-7 k_BT. Write the results into /app/outputs/results.json according to the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with keys 'RTD','FP-I','FP-II','FP-III'. Each value is an object with keys: 'P_max_MW_per_m2' (number), 'eta_Pmax_percent' (number), 'eta_max_percent' (number), 'PEP_max_MW_per_m2' (number), 'PF_max' (number), 'zT_max' (number), 'zT_range' (string, e.g. '2.5-4.5'), 'S_range_mV_per_K' (string, e.g. '0.2-0.26').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Thermoelectric performance metrics for RTD, FP-I, FP-II, FP-III. Each metric (except range strings) is a numeric value in the specified unit. The checker compares each numeric metric against paper-derived thresholds using a threshold-or-better policy; meeting or exceeding the reference earns full credit. Additionally, the relative device ordering (e.g., P_max: FP-III > FP-II > FP-I > RTD) is checked.
- schema:
  - `type`: object
  - `required`: `RTD`, `FP-I`, `FP-II`, `FP-III`
  - `additionalProperties`: False
  - `properties`:
    - `RTD`:
      - `type`: object
      - `required`: `P_max_MW_per_m2`, `eta_Pmax_percent`, `eta_max_percent`, `PEP_max_MW_per_m2`, `PF_max`, `zT_max`, `zT_range`, `S_range_mV_per_K`
      - `properties`:
        - `P_max_MW_per_m2`:
          - `type`: number
        - `eta_Pmax_percent`:
          - `type`: number
        - `eta_max_percent`:
          - `type`: number
        - `PEP_max_MW_per_m2`:
          - `type`: number
        - `PF_max`:
          - `type`: number
        - `zT_max`:
          - `type`: number
        - `zT_range`:
          - `type`: string
        - `S_range_mV_per_K`:
          - `type`: string
    - `FP-I`:
      - `$ref`: #/properties/RTD
    - `FP-II`:
      - `$ref`: #/properties/RTD
    - `FP-III`:
      - `$ref`: #/properties/RTD

Notes: The agent must compute the transmission functions from scratch using NEGF-Poisson; no pre-computed data is provided. The scoring uses the paper's Table I as the hidden gold with a 5% relative or 0.05 absolute tolerance, whichever is larger, combined with monotonic ordering.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "RTD",
          "FP-I",
          "FP-II",
          "FP-III"
        ],
        "additionalProperties": false,
        "properties": {
          "RTD": {
            "type": "object",
            "required": [
              "P_max_MW_per_m2",
              "eta_Pmax_percent",
              "eta_max_percent",
              "PEP_max_MW_per_m2",
              "PF_max",
              "zT_max",
              "zT_range",
              "S_range_mV_per_K"
            ],
            "properties": {
              "P_max_MW_per_m2": {
                "type": "number"
              },
              "eta_Pmax_percent": {
                "type": "number"
              },
              "eta_max_percent": {
                "type": "number"
              },
              "PEP_max_MW_per_m2": {
                "type": "number"
              },
              "PF_max": {
                "type": "number"
              },
              "zT_max": {
                "type": "number"
              },
              "zT_range": {
                "type": "string"
              },
              "S_range_mV_per_K": {
                "type": "string"
              }
            }
          },
          "FP-I": {
            "$ref": "#/properties/RTD"
          },
          "FP-II": {
            "$ref": "#/properties/RTD"
          },
          "FP-III": {
            "$ref": "#/properties/RTD"
          }
        }
      },
      "description": "Thermoelectric performance metrics for RTD, FP-I, FP-II, FP-III. Each metric (except range strings) is a numeric value in the specified unit. The checker compares each numeric metric against paper-derived thresholds using a threshold-or-better policy; meeting or exceeding the reference earns full credit. Additionally, the relative device ordering (e.g., P_max: FP-III > FP-II > FP-I > RTD) is checked."
    }
  ],
  "notes": "The agent must compute the transmission functions from scratch using NEGF-Poisson; no pre-computed data is provided. The scoring uses the paper's Table I as the hidden gold with a 5% relative or 0.05 absolute tolerance, whichever is larger, combined with monotonic ordering."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.json` and independently scores it. The verifier checks every numeric metric against expected reference values and also checks that the relative ordering of certain metrics across the four devices matches physically expected trends. The final reward is a weighted combination of scores from the individual metrics and the consistency checks. You do not need to match any pre-disclosed numbers; the verifier uses its own hidden evaluation criteria. Simply run the described simulation and report the results honestly.
