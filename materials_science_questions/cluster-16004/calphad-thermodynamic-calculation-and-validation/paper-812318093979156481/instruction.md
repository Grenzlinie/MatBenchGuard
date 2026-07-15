# Clapeyron Equation Pressure-Induced Temperature Shift Calculation

## Problem background
Phase diagrams of alloys are typically established at atmospheric pressure. However, many processing routes involve elevated pressures, where phase stabilities can shift, potentially enabling new metastable phases or extended solubility limits. The Al‑Si system is industrially important, and a thermodynamic framework based on the Clapeyron equation can predict how pressure alters phase boundaries. This task computes the temperature shifts of the Al‑rich solvus and solidus/liquidus boundaries under a moderate pressure increase using enthalpy and volume change data derived from equilibrium properties at atmospheric pressure.

## Approach
The approach uses the integrated form of the Clapeyron equation. For a phase transformation with enthalpy change ΔH and volume change ΔV, the slope of the coexistence curve in P‑T space is dP/dT = ΔH/(T ΔV). Assuming ΔH and ΔV are independent of pressure over the range of interest, integrating from atmospheric pressure (P₁ ≈ 0) to a target pressure P₂ gives (ΔV/ΔH) ΔP = ln(T₂/T₁), where ΔP = P₂ – P₁ = 689 MPa (0.69 GPa), T₁ is the equilibrium temperature at atmospheric pressure, and T₂ is the new equilibrium temperature at pressure P₂. Solving yields T₂ = T₁⋅exp((ΔV/ΔH)ΔP) and the temperature shift ΔT = T₂ – T₁.

Two phase boundaries are considered:
- Line 1 (solvus): ΔH = 60000 J mol⁻¹.
- Line 2 (solidus/liquidus): ΔH = −10550 J mol⁻¹.

For each boundary, input pairs of T₁ and ΔV are provided (extracted from the paper’s appendix). Additionally, as a consistency check, the shift for the pure aluminium solidification transformation is computed using ΔH = 10500 J mol⁻¹, ΔV = 0.77 ml mol⁻¹, and T₁ = 933 K.

For every input row (5 for line 1, 5 for line 2, and the pure‑Al control), T₂ and ΔT are calculated and written to a single CSV file.

## Reproduction target
For every row of the provided input tables (line 1, line 2, and pure‑Al control), compute T₂ and ΔT using the integrated Clapeyron equation given above. Write all results to a CSV file named `temperature_shifts.csv` with one row per data point and the following columns: `line` (integer: 1 for line 1, 2 for line 2, 0 for pure Al), `T1_K` (float, K), `delta_V_ml_per_mol` (float, ml mol⁻¹), `T2_K` (float, K), `delta_T_K` (float, K). The verifier will assess the accuracy of the computed ΔT values against independently determined reference values.

## Assets
The following constants are provided:
- ΔP = 689 MPa (0.69 GPa)
- ΔH (line 1) = 60000 J mol⁻¹
- ΔH (line 2) = −10550 J mol⁻¹

The input data for each phase boundary are listed below. Only T₁ and ΔV are needed; the remaining columns in the original tables (compositions, individual phase volumes, paper‑reported T₂ and ΔT) are omitted.

**Line 1 (solvus) input:**
| T₁ (K) | ΔV (ml mol⁻¹) |
|--------|----------------|
| 673    | −1.778         |
| 758    | −1.719         |
| 795    | −1.679         |
| 813    | −1.647         |
| 850    | −1.598         |

**Line 2 (solidus/liquidus) input:**
| T₁ (K) | ΔV (ml mol⁻¹) |
|--------|----------------|
| 920    | −0.79          |
| 898    | −0.84          |
| 886    | −0.86          |
| 873    | −0.86          |
| 850    | −0.89          |

**Pure Al verification input:**
ΔH = 10500 J mol⁻¹, ΔV = 0.77 ml mol⁻¹, T₁ = 933 K.

## Workflow steps

### Step 1: Compute pressure-induced temperature shifts
- Role: scored (load-bearing)
- Action: Using the integrated Clapeyron equation (ΔV/ΔH)·ΔP = ln(T₂/T₁) with ΔP = 689 MPa (0.69 GPa) and the provided enthalpy changes (ΔH = 60000 J mol⁻¹ for line 1, −10550 J mol⁻¹ for line 2), apply the equation to every row of the attached Table BI (line 1) and Table BII (line 2). Compute T₂ = T₁·exp((ΔV/ΔH)·ΔP) and ΔT = T₂ − T₁. Additionally, compute the pure-Al control using ΔH = 10500 J mol⁻¹, ΔV = 0.77 ml mol⁻¹, T₁ = 933 K. Write all results to temperature_shifts.csv.
- Output file: `/app/outputs/temperature_shifts.csv`
- Format: csv
- Contract: columns: line (int, 1 or 2; 0 for pure Al control), T1_K (float, K), delta_V_ml_per_mol (float, ml mol⁻¹), T2_K (float, K), delta_T_K (float, K). One row per data point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/temperature_shifts.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### temperature_shifts.csv
- path: `/app/outputs/temperature_shifts.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed temperature shifts and final temperatures for each phase boundary data point and pure-Al control, compared against the paper's reported ΔT values
- schema:
  - `type`: table
  - `required_columns`: `line`, `T1_K`, `delta_V_ml_per_mol`, `T2_K`, `delta_T_K`
  - `units`:
    - `T1_K`: K
    - `delta_V_ml_per_mol`: ml mol⁻¹
    - `T2_K`: K
    - `delta_T_K`: K

Notes: The hidden checker reads the agent's CSV, extracts delta_T_K, and compares each value to the paper's reported gold with a tolerance of ±0.5 K. T₂ values are also validated for consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "temperature_shifts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "line",
          "T1_K",
          "delta_V_ml_per_mol",
          "T2_K",
          "delta_T_K"
        ],
        "units": {
          "T1_K": "K",
          "delta_V_ml_per_mol": "ml mol⁻¹",
          "T2_K": "K",
          "delta_T_K": "K"
        }
      },
      "description": "Computed temperature shifts and final temperatures for each phase boundary data point and pure-Al control, compared against the paper's reported ΔT values"
    }
  ],
  "notes": "The hidden checker reads the agent's CSV, extracts delta_T_K, and compares each value to the paper's reported gold with a tolerance of ±0.5 K. T₂ values are also validated for consistency."
}
```

## How you are scored
A hidden verifier reads your `temperature_shifts.csv`, extracts the `delta_T_K` column, and compares each value to independently recomputed expected values obtained from the same input data. The final reward is a weighted combination across all data points; accurate computation of ΔT within an acceptable deviation yields full credit, while larger deviations reduce the score. The pure‑Al control is included to demonstrate internal consistency. Simply reporting numbers from the literature is not sufficient – you must compute the values from the given inputs.
