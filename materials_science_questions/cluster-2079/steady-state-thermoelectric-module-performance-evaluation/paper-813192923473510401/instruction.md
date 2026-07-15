# Steady-State Thermoelectric Generation Heat Exchanger Performance Simulation

## Problem background
Solid oxide fuel cell (SOFC) systems produce high‑temperature exhaust that still carries usable enthalpy. In a compact 700 W class SOFC system, a bottom water heater recovers part of that enthalpy to heat water for cogeneration. Replacing this water heater with a thermoelectric generation heat exchanger (TEG‑HEX) offers the potential to generate additional electricity while still delivering hot water. This task simulates the steady‑state performance of such a TEG‑HEX and quantifies the resulting improvement in system electrical efficiency.

## Approach
The TEG‑HEX is modelled with a node‑by‑node finite‑difference approach along the flow direction. At each node, coupled enthalpy balances are solved for two aluminium alloy plates, the exhaust gas, and the water stream. A condensation heat transfer model accounts for the extra heat released when water vapour in the exhaust condenses. The thermoelectric effect — Seebeck effect, Joule heating, and thermal conduction — links the hot‑side and cold‑side junction temperatures to the electrical current and generated power at each node. Publicly available thermodynamic data for the exhaust species and liquid water are used to evaluate enthalpies, and averaged (p+n)/2 properties for the TE materials are employed. The TEG‑HEX length is iteratively adjusted until the total heat transferred to the water reaches a prescribed target, simultaneously satisfying the required water outlet temperature. The simulation outputs per‑node temperatures, heat flows, electrical power, and aggregated performance metrics.

## Reproduction target
Run the finite‑difference simulation for the baseline case: TE element height = 0.9 cm, heat‑transfer enhancement rate = 3.0, and total TEG‑HEX physical volume = 2205 cm³. Tune the device length so that the water outlet temperature reaches 348 K and the total heat rejected to water equals 630 W. Output a single JSON file containing per‑node temperatures (hot‑side junction T_hj, cold‑side junction T_cj, exhaust T_ex, water T_water), module current I_TEG, electrical power P_TEG, and heat flows Q_in_TE and Q_out_TE. The file must also include a summary object with the total electrical power, total TEG conversion efficiency, SOFC efficiency improvement, and the final tuned device length. All quantities must be computed from the simulation, not taken from any external source.

## Assets

- Average TE material properties (Seebeck coefficient, electrical resistivity, thermal conductivity)
- Simulation parameters (Tables I–III)
- SOFC system parameters (AC output, efficiency target, S/C, fuel/oxygen utilisation)
- Thermodynamic data for gaseous H₂O, CO₂, O₂, N₂ and liquid water

## Workflow steps

### Step 1: Compute water flow rate
- Role: process
- Action: Using the given exhaust composition, inlet temperature (538 K), and the SOFC system parameters, calculate the water flow rate (mol/s) that absorbs 92% of the exhaust enthalpy to heat liquid water from 298.15 K to about 348 K. Use standard enthalpy functions for the gases and liquid water. Write the resulting flow rate to a simple text file for the next step.
- Evidence: `/app/outputs/water_flow_rate.txt`

### Step 2: Run finite‑difference TEG‑HEX simulation and compute performance metrics
- Role: scored (load-bearing)
- Action: Implement a node‑by‑node finite‑difference model that solves the coupled enthalpy balances (plates, exhaust, water), condensation heat transfer, and thermoelectric equations (Seebeck effect, Joule heating, thermal conduction). Iteratively adjust the TEG‑HEX length until the total heat transferred to water (sum of Q_out_TE) reaches 630 W (which also gives a water outlet temperature of 348 K). Run the simulation for the case: TE element height L_TE = 0.9 cm, heat‑transfer enhancement rate r_hte = 3.0, and total physical volume V_WH = 2205 cm³. Output a single JSON file containing: per‑node temperatures (T_hj, T_cj, T_ex, T_water), TE current I_TEG, generated power P_TEG, and heat flows Q_in_TE and Q_out_TE; plus a summary object with total electrical power, total TEG conversion efficiency, and SOFC efficiency improvement.
- Output file: `/app/outputs/simulation_outputs.json`
- Format: json
- Contract: {
  "summary": {
    "total_P_TEG": float,
    "total_eta_TE": float,
    "delta_eta_SOFC": float,
    "final_length": float
  },
  "nodes": [
    {
      "node_index": int,
      "T_hj": float,
      "T_cj": float,
      "T_ex": float,
      "T_water": float,
      "P_TEG": float,
      "Q_in_TE": float,
      "Q_out_TE": float,
      "I_TEG": float
    }
  ]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_outputs.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_outputs.json
- path: `/app/outputs/simulation_outputs.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Main simulation output: per‑node thermoelectric data and aggregated performance metrics including power densities and cumulative distribution information for the baseline case (L_TE=0.9 cm, r_hte=3.0, V_WH=2205 cm³).
- schema:
  - `type`: object
  - `required`: `summary`, `nodes`
  - `properties`:
    - `summary`:
      - `type`: object
      - `required`: `total_P_TEG`, `total_eta_TE`, `delta_eta_SOFC`, `final_length`, `V_WH`, `V_TE`, `power_density_WH`, `power_density_TE`
      - `properties`:
        - `total_P_TEG`:
          - `type`: number
          - `unit`: W
        - `total_eta_TE`:
          - `type`: number
          - `unit`: dimensionless ratio
        - `delta_eta_SOFC`:
          - `type`: number
          - `unit`: percentage points
        - `final_length`:
          - `type`: number
          - `unit`: m
        - `V_WH`:
          - `type`: number
          - `unit`: m³
          - `description`: Total TEG-HEX physical volume
        - `V_TE`:
          - `type`: number
          - `unit`: m³
          - `description`: Sum of TE elements volume
        - `power_density_WH`:
          - `type`: number
          - `unit`: W/m³
          - `description`: Power density based on TEG-HEX volume (total_P_TEG / V_WH)
        - `power_density_TE`:
          - `type`: number
          - `unit`: W/m³
          - `description`: Power density based on TE elements volume (total_P_TEG / V_TE)
    - `nodes`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `node_index`, `position`, `T_hj`, `T_cj`, `T_ex`, `T_water`, `P_TEG`, `Q_in_TE`, `Q_out_TE`, `I_TEG`
        - `properties`:
          - `node_index`:
            - `type`: integer
          - `position`:
            - `type`: number
            - `unit`: fraction of total TEG-HEX length (0 to 1)
          - `T_hj`:
            - `type`: number
            - `unit`: K
          - `T_cj`:
            - `type`: number
            - `unit`: K
          - `T_ex`:
            - `type`: number
            - `unit`: K
          - `T_water`:
            - `type`: number
            - `unit`: K
          - `P_TEG`:
            - `type`: number
            - `unit`: W
          - `Q_in_TE`:
            - `type`: number
            - `unit`: W
          - `Q_out_TE`:
            - `type`: number
            - `unit`: W
          - `I_TEG`:
            - `type`: number
            - `unit`: A

Notes: The agent must run the full finite‑difference simulation; the summary values are recomputed by the checker from the node data. The per‑node temperatures must reflect the physical monotonicity constraints (exhaust decreasing, water increasing) and the water outlet must satisfy the 348 K target within solver tolerance. The volume and power density fields allow the checker to verify structural and reported quantities.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_outputs.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "summary",
          "nodes"
        ],
        "properties": {
          "summary": {
            "type": "object",
            "required": [
              "total_P_TEG",
              "total_eta_TE",
              "delta_eta_SOFC",
              "final_length",
              "V_WH",
              "V_TE",
              "power_density_WH",
              "power_density_TE"
            ],
            "properties": {
              "total_P_TEG": {
                "type": "number",
                "unit": "W"
              },
              "total_eta_TE": {
                "type": "number",
                "unit": "dimensionless ratio"
              },
              "delta_eta_SOFC": {
                "type": "number",
                "unit": "percentage points"
              },
              "final_length": {
                "type": "number",
                "unit": "m"
              },
              "V_WH": {
                "type": "number",
                "unit": "m³",
                "description": "Total TEG-HEX physical volume"
              },
              "V_TE": {
                "type": "number",
                "unit": "m³",
                "description": "Sum of TE elements volume"
              },
              "power_density_WH": {
                "type": "number",
                "unit": "W/m³",
                "description": "Power density based on TEG-HEX volume (total_P_TEG / V_WH)"
              },
              "power_density_TE": {
                "type": "number",
                "unit": "W/m³",
                "description": "Power density based on TE elements volume (total_P_TEG / V_TE)"
              }
            }
          },
          "nodes": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "node_index",
                "position",
                "T_hj",
                "T_cj",
                "T_ex",
                "T_water",
                "P_TEG",
                "Q_in_TE",
                "Q_out_TE",
                "I_TEG"
              ],
              "properties": {
                "node_index": {
                  "type": "integer"
                },
                "position": {
                  "type": "number",
                  "unit": "fraction of total TEG-HEX length (0 to 1)"
                },
                "T_hj": {
                  "type": "number",
                  "unit": "K"
                },
                "T_cj": {
                  "type": "number",
                  "unit": "K"
                },
                "T_ex": {
                  "type": "number",
                  "unit": "K"
                },
                "T_water": {
                  "type": "number",
                  "unit": "K"
                },
                "P_TEG": {
                  "type": "number",
                  "unit": "W"
                },
                "Q_in_TE": {
                  "type": "number",
                  "unit": "W"
                },
                "Q_out_TE": {
                  "type": "number",
                  "unit": "W"
                },
                "I_TEG": {
                  "type": "number",
                  "unit": "A"
                }
              }
            }
          }
        }
      },
      "description": "Main simulation output: per‑node thermoelectric data and aggregated performance metrics including power densities and cumulative distribution information for the baseline case (L_TE=0.9 cm, r_hte=3.0, V_WH=2205 cm³)."
    }
  ],
  "notes": "The agent must run the full finite‑difference simulation; the summary values are recomputed by the checker from the node data. The per‑node temperatures must reflect the physical monotonicity constraints (exhaust decreasing, water increasing) and the water outlet must satisfy the 348 K target within solver tolerance. The volume and power density fields allow the checker to verify structural and reported quantities."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your simulation_outputs.json. The verifier recomputes the summary aggregates (total power, efficiency, efficiency improvement) directly from the per‑node data you provide. It first checks that the water outlet temperature is within acceptable tolerance of 348 K and that the total heat rejected to water is within tolerance of 630 W. It then compares your recomputed aggregate metrics to a hidden reference. Your overall reward is a weighted combination of these checks; accuracy of the per‑node data and the aggregates they produce determines your score. Simply reporting numbers that match a known result without correct underlying node data will not pass.
