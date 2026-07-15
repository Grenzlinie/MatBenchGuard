# Analysis of microprocessor cooling with embedded thermoelectric coolers

## Problem background
Localized cooling of microprocessor functional blocks using embedded thermoelectric coolers (eTECs) can potentially reduce overall system power dissipation. Lowering junction temperature reduces leakage power but adds cooling power that must be supplied by the eTEC. The key question is whether an optimal operating temperature exists where the total power (electronic plus cooling) is lower than without cooling, and how much savings can be achieved for different types of blocks. This work develops a system-level model that combines realistic per-block electronic characteristics (power density, leakage ratio) with eTEC performance (figure of merit ZT, coefficient of performance) to find such optimal temperatures and quantify total power savings.

## Approach
Implement a system-level model that integrates electronic power dissipation of individual processor blocks with the thermodynamics of an embedded TEC.

**Electronic power model:** For each functional block, the total electronic power at a given junction temperature T is the sum of active power (constant) and leakage power. Leakage power increases exponentially with temperature: P_leak(T) = P_leak_ref * exp( (Ea/k) * (1/T_ref - 1/T) ), where Ea/k ≈ 3000 K (activation energy), T_ref is a reference temperature (343 K / 70 °C), and P_leak_ref is the leakage power at that reference. Active power is constant across temperature. The reference leakage ratio (leakage/(active+leakage) at T_ref) and total power density at T_ref are given for each block.

**eTEC model:** The coefficient of performance (COP) of an ideal thermoelectric cooler is given by the maximum theoretical COP for a given figure of merit ZT and temperature difference. For a cold-side temperature T_c and hot-side temperature T_h (ambient), COP = (T_c/(T_h – T_c)) * (sqrt(1+ZT) – (T_h/T_c)) / (sqrt(1+ZT) + 1). The cooling power required to remove the electronic heat load P_elec is P_cool = P_elec / COP.

**Optimization:** For each block, sweep T_c over a plausible range below T_h. At each T_c, compute total power P_total = P_elec(T_c) + P_cool(T_c). Find the T_c that minimizes P_total. Compute power saving (%) as 100 * (P_total_no_cool – P_total_opt) / P_total_no_cool, where P_total_no_cool = P_elec(T_h). Cooling effect (°C) is T_h – T_c_opt.

**Given block parameters (at T_ref = 70 °C):** The following table lists the power density (W/mm²), leakage ratio (%), and area (mm²) for the Xeon functional blocks, extracted from the published data.

| Block           | Power density | Leakage ratio | Area    |
|-----------------|---------------|---------------|---------|
| L-3 Cache       | 0.045         | 60            | 47.0    |
| L-2 Cache       | 0.090         | 50            | 19.6    |
| I-Cache         | 0.32          | 25            |  2.0    |
| BRED            | 0.55          | 20            |  1.5    |
| I-Decoder       | 0.70          | 15            |  1.2    |
| Rename          | 0.85          | 10            |  1.0    |
| LdStQ           | 0.95          | 12            |  0.9    |
| ITB             | 1.05          |  8            |  0.8    |
| DTB             | 1.15          |  8            |  0.7    |
| Register File   | 1.25          |  6            |  0.6    |
| I-Scheduler     | 1.35          |  6            |  0.5    |
| Integer ALU     | 1.45          |  5            |  0.4    |

**Ambient temperature:** T_h = 70 °C (343 K).

**Technology scaling (for Step 2):** For the L-2 Cache and L-3 Cache blocks, scale the 65‑nm parameters to 45 nm, 32 nm, and 22 nm using ITRS rules: area scales as (feature size)², i.e., area_factor = (node/65)². Leakage power scales with a node-dependent factor (relative to 65 nm): 1.0 (65 nm), 1.5 (45 nm), 2.5 (32 nm), 4.0 (22 nm). Active power density scaling is neglected (kept constant per area). Apply the same optimization procedure for ZT = 1 and ZT = 2.

## Reproduction target
Compute two result sets:
1. For each of the 12 functional blocks listed above, using ZT = 1, find the optimal power saving (%) and the associated cooling effect (°C) relative to the no‑cooling baseline at 70 °C. Write the results to `power_savings_table_I.csv`.
2. For the L-2 Cache and L-3 Cache blocks, project the power saving (%) across technology nodes 65 nm, 45 nm, 32 nm, and 22 nm, for ZT = 1 and ZT = 2. Write the results to `power_savings_table_II.csv`.

## Assets

- ITRS 2010 edition scaling parameters: http://public.itrs.net/

## Workflow steps

### Step 1: Single-block optimization for Table I
- Role: scored (load-bearing)
- Action: Implement the system-level model: (1) model electronic power as sum of active power (constant) and temperature-dependent leakage power (exponential dependence with given activation energy); (2) compute eTEC coefficient of performance (COP) using the maximum theoretical COP formula for given ZT and temperature difference; (3) For the L-3 Cache and L-2 Cache blocks, sweep junction temperature over a plausible range and find the temperature that minimizes total power; compute the corresponding optimal power saving (%) and cooling effect (°C). For every other block, do NOT sweep to find the optimum; instead, fix the cooling effect at 10°C (i.e., T_junction = T_ambient - 10°C) and evaluate the total power (electronic + cooling) at that point, then compute the power penalty (negative saving) relative to the no-cooling baseline at T_ambient; report cooling_effect_celsius as 10. (4) Write the results to power_savings_table_I.csv.
- Output file: `/app/outputs/power_savings_table_I.csv`
- Format: csv
- Contract: Columns: block_name (string), power_saving_percent (float, %), cooling_effect_celsius (float, °C). One row per block. Units: power_saving_percent in percent (e.g., 7 means 7%), cooling_effect_celsius in degrees Celsius.
- Scoring: scored by hidden verifier

### Step 2: Technology scaling optimization for Table II
- Role: scored
- Action: Using the ITRS scaling rules (area proportional to feature size squared, leakage scaling factor per node), scale the base parameters of L-2 Cache and L-3 Cache at 65nm to 45nm, 32nm, and 22nm technology nodes. For each node and each ZT value (1 and 2), apply the same system-level model as in step_01 to find the optimum junction temperature and compute the power savings (%) relative to the scaled no-cooling baseline. Write the results to power_savings_table_II.csv.
- Output file: `/app/outputs/power_savings_table_II.csv`
- Format: csv
- Contract: Columns: tech_node_nm (int, e.g., 65, 45, 32, 22), cache_level (string, 'L-2 Cache' or 'L-3 Cache'), ZT (int, 1 or 2), power_saving_percent (float, %). One row per combination. Units: power_saving_percent in percent.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/power_savings_table_I.csv`
- `/app/outputs/power_savings_table_II.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### power_savings_table_I.csv
- path: `/app/outputs/power_savings_table_I.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Per-block optimal power savings and cooling effect under ZT=1 eTEC.
- schema:
  - `type`: table
  - `required_columns`: `block_name`, `power_saving_percent`, `cooling_effect_celsius`
  - `units`:
    - `power_saving_percent`: %
    - `cooling_effect_celsius`: °C

### power_savings_table_II.csv
- path: `/app/outputs/power_savings_table_II.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Projected power savings for L2 and L3 caches across technology nodes and ZT values.
- schema:
  - `type`: table
  - `required_columns`: `tech_node_nm`, `cache_level`, `ZT`, `power_saving_percent`
  - `units`:
    - `power_saving_percent`: %

Notes: The agent must implement the temperature-dependent leakage model and theoretical COP formula from the given expressions. Block parameters and scaling rules are provided in the instruction. The checker compares the reported numeric values against hidden reference values derived from the paper; tolerance is applied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "power_savings_table_I.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "block_name",
          "power_saving_percent",
          "cooling_effect_celsius"
        ],
        "units": {
          "power_saving_percent": "%",
          "cooling_effect_celsius": "°C"
        }
      },
      "description": "Per-block optimal power savings and cooling effect under ZT=1 eTEC."
    },
    {
      "file": "power_savings_table_II.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "tech_node_nm",
          "cache_level",
          "ZT",
          "power_saving_percent"
        ],
        "units": {
          "power_saving_percent": "%"
        }
      },
      "description": "Projected power savings for L2 and L3 caches across technology nodes and ZT values."
    }
  ],
  "notes": "The agent must implement the temperature-dependent leakage model and theoretical COP formula from the given expressions. Block parameters and scaling rules are provided in the instruction. The checker compares the reported numeric values against hidden reference values derived from the paper; tolerance is applied."
}
```

## How you are scored
A hidden verifier will independently score the two output CSV files. Each scored artifact carries a pre‑defined weight, and the final reward is the weighted sum. The verifier compares the values you report in the two tables against reference values derived from the original study, applying appropriate tolerances. It also checks that required columns are present and that file formats match the output contract. Simply reporting numbers that happen to match the paper’s findings is not sufficient; the verifier expects that the outputs are consistent with a correct implementation of the system‑level model described above.
