# Isentropic Temperature Ratio Calculation for Deuterium Metallization

## Problem background
The insulator-metal transition in dense fluid deuterium is studied experimentally under shock compression. Two major experimental efforts (using NIF and Z facilities) reported different metallization pressures, and a reanalysis of one dataset suggested a temperature correction of approximately -50% along the phase boundary. Such a large temperature drop would imply an anomalously low specific heat for the metallic fluid. This task evaluates the thermodynamic consistency of that proposed correction by computing the isentropic temperature ratio across the insulator-metal coexistence region, using both a simplified constant‑specific‑heat estimate and an exact entropy–temperature analysis based on first‑principles thermodynamic parameters.

## Approach
The analysis uses provided thermodynamic parameters derived from first-principles calculations for the metallic fluid: isothermal bulk modulus B_T = 385 GPa, specific heats C_V = 5.16 kB/atom and C_P = 8.94 kB/atom, Grüneisen parameter γ = -2.3, coexistence‑line slope dP/dT_coex = -0.12 GPa/K, entropy change ΔS = 0.48 kB/atom, and simple constant‑pressure specific heat C_P,simple = 2.6 kB/atom. For the simplified estimate, the temperature ratio is obtained from ΔS ≈ C_P,simple ln(T0/T1), which assumes C_P is nearly constant away from the boundary. For the exact analysis, the entropy–temperature slope along the coexistence line is given by (dS/dT)coex = (C_P / T) [1 - (C_V C_P γ T B_T) / (dP/dT_coex) ]. Evaluate this expression at a representative temperature T = 1350 K to obtain the slope coefficient A (which can be thought of as T·dS/dT). Then, using the integrated form ΔS = A ln(T0/T1), compute the exact temperature ratio T1/T0. Finally, apply that ratio to an isentrope that enters the coexistence region at 1416 K to obtain the exit temperature T1.

## Reproduction target
Given the thermodynamic parameters above, compute and output the following four quantities to a JSON file:
1. simple_T1_T0 (dimensionless) – the simple temperature ratio T1/T0 from the constant‑specific‑heat estimate.
2. exact_dS_dT_coefficient (units kB/atom·K) – the exact entropy–temperature slope coefficient A.
3. exact_T1_T0 (dimensionless) – the exact temperature ratio T1/T0 obtained from the full analysis.
4. exact_T1 (units K) – the exit temperature corresponding to an entry temperature of 1416 K, using the exact ratio.
All intermediate steps must derive from the provided formulas and parameters.

## Assets

- Python 3 standard library (math): python3

## Workflow steps

### Step 1: Compute entropy-temperature slope and temperature ratios
- Role: scored (load-bearing)
- Action: Using the provided thermodynamic parameters (BT=385 GPa, CV=5.16 kB/atom, CP=8.94 kB/atom, gamma=-2.3, dP_dT_coex=-0.12 GPa/K, Delta_S=0.48 kB/atom, CP_simple=2.6 kB/atom, T0_entry=1416 K), compute: (1) the simple temperature ratio T1/T0 via the exponential relation using CP_simple and Delta_S; (2) the exact entropy-temperature slope coefficient along the coexistence line via the exact formula; (3) the exact temperature ratio T1/T0 by integrating that slope with Delta_S; and (4) the exact exit temperature T1 for an isentrope entering at 1416 K using the exact ratio.
- Output file: `/app/outputs/step_01_exact_slope_and_ratios.json`
- Format: json
- Contract: JSON object with keys: exact_dS_dT_coefficient (number, units kB/atom·K), exact_T1_T0 (number, dimensionless), exact_T1 (number, units K), simple_T1_T0 (number, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_exact_slope_and_ratios.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_exact_slope_and_ratios.json
- path: `/app/outputs/step_01_exact_slope_and_ratios.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Headline thermodynamic results reproduced from the paper: exact entropy-temperature slope coefficient, exact and simple temperature ratios, and corresponding exit temperature.
- schema:
  - `type`: object
  - `required_keys`: `exact_dS_dT_coefficient`, `exact_T1_T0`, `exact_T1`, `simple_T1_T0`
  - `properties`:
    - `exact_dS_dT_coefficient`: number (kB/atom·K)
    - `exact_T1_T0`: number (dimensionless)
    - `exact_T1`: number (K)
    - `simple_T1_T0`: number (dimensionless)

Notes: All numbers are computed from publicly available thermodynamic parameters; no hidden gold values or tolerances are exposed. The checker will compare each field to the paper-reported values with a small relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_exact_slope_and_ratios.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "exact_dS_dT_coefficient",
          "exact_T1_T0",
          "exact_T1",
          "simple_T1_T0"
        ],
        "properties": {
          "exact_dS_dT_coefficient": "number (kB/atom·K)",
          "exact_T1_T0": "number (dimensionless)",
          "exact_T1": "number (K)",
          "simple_T1_T0": "number (dimensionless)"
        }
      },
      "description": "Headline thermodynamic results reproduced from the paper: exact entropy-temperature slope coefficient, exact and simple temperature ratios, and corresponding exit temperature."
    }
  ],
  "notes": "All numbers are computed from publicly available thermodynamic parameters; no hidden gold values or tolerances are exposed. The checker will compare each field to the paper-reported values with a small relative tolerance."
}
```

## How you are scored
Your output JSON file will be checked against a hidden verifier that compares each reported number to the paper’s reference values, using a small tolerance to account for numerical differences. The verifier assigns a reward weighting to each field and combines them into a final score. Accurate computation from the provided formulas and parameters is essential; simply reporting plausible numbers is not sufficient.
