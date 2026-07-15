# Segmented Thermoelectric Generator Geometry Optimization via Improved Powell Method

## Problem background
Segmented thermoelectric generators (STEGs) are designed to achieve high conversion efficiency over a wide temperature range by joining materials with high thermoelectric figure-of-merit (ZT) in different temperature intervals. This task focuses on a STEG consisting of CoSb3 (hot side) and Bi2Te3 (cold side) in both n- and p-type legs. The performance, measured as specific output power (P_m, W/kg) and conversion efficiency (η, %), strongly depends on the relative lengths of the hot segments (S_nh, S_ph) and the cross-sectional area ratio between n- and p-legs (a = A_n/A_p). Finding the optimal values of these three design variables to maximize either P_m or η is a nonlinear, multi-parameter optimization problem.

## Approach
A discrete numerical model (DNM) is used to compute the temperature distribution and performance of the STEG. Each leg segment is divided into many elements, and steady-state heat balance equations are solved iteratively to obtain the temperature profile, current, and the objective functions P_m and η, taking into account the temperature dependence of the Seebeck coefficient, electrical conductivity, and thermal conductivity. The optimization is performed with an Improved Powell Algorithm, a derivative-free direct search method that can handle multiple variables simultaneously. Design constraints include strictly decreasing temperature from hot to cold junction and interface temperatures within the operational limits of the materials (300 K to 563 K). The optimizer minimizes -P_m or -η separately to find the optimal length ratios S_nh_opt, S_ph_opt and area ratio a_opt.

## Reproduction target
Your goal is to produce a single JSON file `/app/outputs/optimization_results.json` that contains the optimal geometry parameters and resulting performance for both optimization objectives. For the case with total leg length L = 4 mm, p-leg cross-sectional area A_p = 3 × 3 mm², hot-junction temperature T_h = 823 K, cold-junction temperature T_c = 298 K, and electrical contact resistance R_con = 0 Ω, you must determine the optimal (S_nh, S_ph, a) that maximize P_m and separately maximize η, and report the corresponding maximum P_m and the accompanying η (for the max‑power case) and maximum η and accompanying P_m (for the max‑efficiency case). All numeric geometry values should be reported to at least three decimal places, and performance metrics to at least two decimal places.

## Assets
The temperature-dependent thermoelectric properties (Seebeck coefficient α in µV/K, electrical conductivity σ in S/m, thermal conductivity κ in W/(m·K)) for the p- and n-type CoSb3 and Bi2Te3 materials are provided in the table below (digitized from the reference). Use interpolation to obtain property values at any temperature between 300 K and 900 K.

| T (K) | α_p_CoSb3 (µV/K) | σ_p_CoSb3 (S/m) | κ_p_CoSb3 (W/(m·K)) | α_n_CoSb3 (µV/K) | σ_n_CoSb3 (S/m) | κ_n_CoSb3 (W/(m·K)) | α_p_Bi2Te3 (µV/K) | σ_p_Bi2Te3 (S/m) | κ_p_Bi2Te3 (W/(m·K)) | α_n_Bi2Te3 (µV/K) | σ_n_Bi2Te3 (S/m) | κ_n_Bi2Te3 (W/(m·K)) |
|------|-----------------|------------------|---------------------|------------------|------------------|---------------------|--------------------|--------------------|-----------------------|--------------------|--------------------|-----------------------|
| 300  | 180 | 120000 | 2.3 | -170 | 110000 | 2.4 | 190 | 100000 | 1.5 | -195 | 95000 | 1.4 |
| 350  | 185 | 115000 | 2.5 | -175 | 108000 | 2.5 | 195 | 98000 | 1.6 | -200 | 93000 | 1.5 |
| 400  | 190 | 110000 | 2.6 | -180 | 105000 | 2.6 | 200 | 96000 | 1.7 | -205 | 91000 | 1.6 |
| 450  | 195 | 105000 | 2.7 | -185 | 102000 | 2.7 | 205 | 94000 | 1.8 | -210 | 89000 | 1.7 |
| 500  | 200 | 100000 | 2.8 | -190 | 99000 | 2.8 | 210 | 92000 | 1.9 | -215 | 87000 | 1.8 |
| 550  | 205 | 95000 | 2.9 | -195 | 96000 | 2.9 | 215 | 90000 | 2.0 | -220 | 85000 | 1.9 |
| 600  | 210 | 90000 | 3.0 | -200 | 93000 | 3.0 | —  | —   | —   | —   | —   | —   |
| 650  | 215 | 85000 | 3.1 | -205 | 90000 | 3.1 | —  | —   | —   | —   | —   | —   |
| 700  | 220 | 80000 | 3.2 | -210 | 87000 | 3.2 | —  | —   | —   | —   | —   | —   |
| 750  | 225 | 75000 | 3.3 | -215 | 84000 | 3.3 | —  | —   | —   | —   | —   | —   |
| 800  | 230 | 70000 | 3.4 | -220 | 81000 | 3.4 | —  | —   | —   | —   | —   | —   |
| 850  | 235 | 65000 | 3.5 | -225 | 78000 | 3.5 | —  | —   | —   | —   | —   | —   |
| 900  | 240 | 60000 | 3.6 | -230 | 75000 | 3.6 | —  | —   | —   | —   | —   | —   |

(Dashes indicate temperatures outside the material's stable range.)

## Workflow steps

### Step 1: Prepare temperature-dependent thermoelectric material properties
- Role: process
- Action: Read the provided temperature-dependent Seebeck coefficient, electrical conductivity, and thermal conductivity data for p-type and n-type CoSb3 and Bi2Te3. Create interpolation functions α(T), σ(T), κ(T) for each material to be used in the subsequent simulation.
- Evidence: none

### Step 2: Implement the discrete numerical model (DNM) and the Improved Powell optimizer
- Role: process
- Action: Implement the DNM solver that computes the temperature distribution, current, and performance metrics (specific output power P_m and conversion efficiency η) for given geometry. Implement the Improved Powell Algorithm for unconstrained minimization with incorporated constraint handling (objective function returns zero if constraints violated). The optimizer should minimize -P_m or -η.
- Evidence: none

### Step 3: Run optimization for maximum specific output power
- Role: process
- Action: Using the material properties from step 1 and the DNM/optimizer from step 2, perform optimization for maximum specific output power (minimize -P_m). Use input parameters: total leg length L=4 mm, p-leg cross-sectional area A_p=3×3 mm², hot-junction temperature T_h=823 K, cold-junction temperature T_c=298 K, electrical contact resistance R_con=0. Record the optimal design variables (S_nh_opt, S_ph_opt, a_opt), the attained maximum power P_m_max, and the corresponding efficiency η.
- Evidence: `/app/outputs/power_optimization.log`

### Step 4: Run optimization for maximum conversion efficiency
- Role: process
- Action: Similarly, perform optimization for maximum conversion efficiency (minimize -η) using the same input parameters. Record the optimal parameters, the attained maximum efficiency η_max, and the corresponding power P_m.
- Evidence: `/app/outputs/efficiency_optimization.log`

### Step 5: Compile final optimization results
- Role: scored (load-bearing)
- Action: Combine the outcomes from the two optimization runs into a single JSON file with the structure: { "max_power": { "S_nh_opt":..., "S_ph_opt":..., "a_opt":..., "P_m_max":..., "eta_max":... }, "max_efficiency": { ... } }. All numeric values to at least three decimal places for geometry parameters and at least two decimal places for performance metrics.
- Output file: `/app/outputs/optimization_results.json`
- Format: json
- Contract: {"max_power": {"S_nh_opt": float, "S_ph_opt": float, "a_opt": float, "P_m_max": float (W/kg), "eta_max": float (%)}, "max_efficiency": {"S_nh_opt": float, "S_ph_opt": float, "a_opt": float, "P_m_max": float (W/kg), "eta_max": float (%)}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimization_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimization_results.json
- path: `/app/outputs/optimization_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Optimal geometry parameters and resulting performance for the base case.
- schema:
  - `type`: object
  - `required`: `max_power`, `max_efficiency`
  - `properties`:
    - `max_power`:
      - `type`: object
      - `required`: `S_nh_opt`, `S_ph_opt`, `a_opt`, `P_m_max`, `eta_max`
      - `properties`:
        - `S_nh_opt`:
          - `type`: number
        - `S_ph_opt`:
          - `type`: number
        - `a_opt`:
          - `type`: number
        - `P_m_max`:
          - `type`: number
          - `description`: W/kg
        - `eta_max`:
          - `type`: number
          - `description`: %
    - `max_efficiency`:
      - `type`: object
      - `required`: `S_nh_opt`, `S_ph_opt`, `a_opt`, `P_m_max`, `eta_max`
      - `properties`:
        - `S_nh_opt`:
          - `type`: number
        - `S_ph_opt`:
          - `type`: number
        - `a_opt`:
          - `type`: number
        - `P_m_max`:
          - `type`: number
          - `description`: W/kg
        - `eta_max`:
          - `type`: number
          - `description`: %

Notes: The checker compares the base-case geometry parameters against hidden reference values with an absolute tolerance, and performance metrics on a threshold-or-better basis.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimization_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "max_power",
          "max_efficiency"
        ],
        "properties": {
          "max_power": {
            "type": "object",
            "required": [
              "S_nh_opt",
              "S_ph_opt",
              "a_opt",
              "P_m_max",
              "eta_max"
            ],
            "properties": {
              "S_nh_opt": {
                "type": "number"
              },
              "S_ph_opt": {
                "type": "number"
              },
              "a_opt": {
                "type": "number"
              },
              "P_m_max": {
                "type": "number",
                "description": "W/kg"
              },
              "eta_max": {
                "type": "number",
                "description": "%"
              }
            }
          },
          "max_efficiency": {
            "type": "object",
            "required": [
              "S_nh_opt",
              "S_ph_opt",
              "a_opt",
              "P_m_max",
              "eta_max"
            ],
            "properties": {
              "S_nh_opt": {
                "type": "number"
              },
              "S_ph_opt": {
                "type": "number"
              },
              "a_opt": {
                "type": "number"
              },
              "P_m_max": {
                "type": "number",
                "description": "W/kg"
              },
              "eta_max": {
                "type": "number",
                "description": "%"
              }
            }
          }
        }
      },
      "description": "Optimal geometry parameters and resulting performance for the base case."
    }
  ],
  "notes": "The checker compares the base-case geometry parameters against hidden reference values with an absolute tolerance, and performance metrics on a threshold-or-better basis."
}
```

## How you are scored
A hidden verifier will read your output file `/app/outputs/optimization_results.json` and compare both the `max_power` and `max_efficiency` entries against reference values. The geometry parameters (S_nh_opt, S_ph_opt, a_opt) are evaluated with an absolute tolerance; the performance metrics (P_m_max, eta_max) are scored on a threshold-or-better basis: meeting or exceeding the reference yields full credit, with partial credit for results close to the reference. The two optimization objectives are scored independently, and the final reward is the weighted sum of the scores. Reporting the paper's numbers without correctly implementing the model and optimizer will not suffice; the verifier checks that the reported numbers are consistent with a correct reproduction of the optimization procedure.
