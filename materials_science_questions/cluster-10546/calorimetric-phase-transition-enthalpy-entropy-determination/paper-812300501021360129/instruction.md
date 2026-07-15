# Calorimetric Glass Transition and Phase Transition Analysis from Heat Capacity Data

## Problem background
Cyanoadamantane is a plastic crystal that can exist in several solid phases: an ordered crystalline phase, a plastic phase where molecules are orientationally disordered, and a glassy crystalline phase obtained by quenching the plastic phase. The thermodynamics of these phases, especially the first-order transition between ordered and plastic phases and the glass transition of the supercooled plastic phase, provide insight into the nature of orientational disorder and the residual entropy frozen at the glass transition. The present task focuses on extracting these key thermodynamic quantities from a table of molar heat capacity data measured for all relevant phases.

## Approach
The method uses the heat capacity data of stable phases (ordered and plastic) and metastable phases (glassy and supercooled plastic) to derive the transition energetics and the configurational entropy. For the first-order transition, a baseline is constructed by interpolating the heat capacity of the ordered phase below the transition and the plastic phase above it. The excess heat capacity above this baseline is integrated over the transition region to obtain the transition enthalpy and entropy. For the glass transition, the heat capacity step is identified from the metastable data to determine the glass transition temperature and the jump in heat capacity. The configurational entropy of the plastic phase is then computed as a function of temperature using the fundamental relation that sums the transition entropy and corrects for the differences in vibrational heat capacities between the plastic, glassy, and ordered crystal phases. All computations are performed using standard thermodynamic integration formulas applied to the provided Cp(T) data.

## Reproduction target
Using the provided molar heat capacity data for cyanoadamantane (stable ordered/plastic phases and metastable glassy/supercooled plastic phases), perform the following analyses:
1. Determine the first-order transition region from the stable Cp curve, define an appropriate baseline, and integrate the excess heat capacity to compute the transition enthalpy (kJ/mol) and entropy (J/K/mol).
2. From the metastable Cp data, identify the glass transition step and compute the glass transition temperature (K) and the heat capacity jump (J/K/mol).
3. Compute the full configurational entropy curve S_c(T) from near 0 K up to the transition temperature, expressing the result as a CSV file with columns T (K) and S_c (J/K/mol).
4. From the S_c(T) curve, extract the residual configurational entropy at the glass transition temperature.

All intermediate quantities and final answers must be derived from the provided data using clear thermodynamic reasoning; the outputs must be saved to the specified JSON and CSV files in the /app/outputs directory.

## Assets

- Molar heat capacities of cyanoadamantane (stable and metastable phases)
- Python scientific stack (numpy, scipy, pandas, matplotlib): https://pypi.org

## Workflow steps

### Step 1: Load and validate heat capacity data
- Role: process
- Action: Load the provided heat capacity CSV, separate the stable (ordered crystal + plastic) and metastable (glassy crystal + supercooled plastic) phase series, and ensure temperature ranges and data completeness.
- Evidence: none

### Step 2: Determine baselines for excess heat capacity integration
- Role: process
- Action: From the loaded Cp curves, locate the first‑order transition anomaly near 273 K in the stable data and the glass transition jump near 160 K in the metastable data. Define physically motivated baselines (e.g., interpolation of Cp from the ordered phase below the transition and from the plastic phase above) for the transition region, and establish a baseline for the glass transition jump.
- Evidence: none

### Step 3: Compute transition enthalpy and entropy
- Role: scored (load-bearing)
- Action: Integrate the excess heat capacity (Cp − baseline) over the first‑order transition region (e.g., 265–280 K) to obtain the transition enthalpy ΔH_trs (kJ/mol). Compute the transition entropy ΔS_trs (J/K/mol) either as ΔH_trs/T_trs or by integrating (Cp − baseline)/T over the same region.
- Output file: `/app/outputs/transition_enthalpy_entropy.json`
- Format: json
- Contract: {"delta_H_kJ_per_mol": number, "delta_S_J_per_K_per_mol": number}
- Scoring: scored by hidden verifier

### Step 4: Determine glass transition temperature and heat capacity jump
- Role: scored
- Action: From the metastable Cp data, determine the glass transition temperature Tg (K) as the midpoint or inflection point of the Cp step, and compute the heat capacity jump ΔCp (J/K/mol) as the difference in Cp just above and below Tg.
- Output file: `/app/outputs/glass_transition_deltaCp.json`
- Format: json
- Contract: {"T_g_K": number, "delta_Cp_J_per_K_per_mol": number}
- Scoring: scored by hidden verifier

### Step 5: Compute configurational entropy curve
- Role: scored (load-bearing)
- Action: Using the thermodynamic relation S_c(T) = ΔS_trs − ∫_{T}^{T_trs} (Cp_pc − Cp_gc)/T' dT' − ∫_{0}^{T_trs} (Cp_gc − Cp_oc)/T' dT', compute the configurational entropy S_c (J/K/mol) as a function of temperature over the range from near 0 K to T_trs, employing the Cp data for the ordered, glassy, and plastic phases. Produce a complete temperature dependence curve.
- Output file: `/app/outputs/configurational_entropy.csv`
- Format: csv
- Contract: CSV with columns: T (K), S_c (J/K/mol)
- Scoring: scored by hidden verifier

### Step 6: Extract residual configurational entropy at Tg
- Role: scored
- Action: From the computed S_c(T) curve, read the value at the glass transition temperature (where S_c plateaus) to obtain the residual configurational entropy S_c,residual (J/K/mol).
- Output file: `/app/outputs/residual_configurational_entropy.json`
- Format: json
- Contract: {"S_c_residual_J_per_K_per_mol": number, "T_g_K": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_enthalpy_entropy.json`
- `/app/outputs/glass_transition_deltaCp.json`
- `/app/outputs/configurational_entropy.csv`
- `/app/outputs/residual_configurational_entropy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_enthalpy_entropy.json
- path: `/app/outputs/transition_enthalpy_entropy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Transition enthalpy (kJ/mol) and entropy (J/K/mol) for the ordered‑to‑plastic phase transition.
- schema:
  - `type`: object
  - `required`:
    - `delta_H_kJ_per_mol`: number
    - `delta_S_J_per_K_per_mol`: number

### glass_transition_deltaCp.json
- path: `/app/outputs/glass_transition_deltaCp.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Glass transition temperature (K) and heat capacity jump (J/K/mol) of cyanoadamantane.
- schema:
  - `type`: object
  - `required`:
    - `T_g_K`: number
    - `delta_Cp_J_per_K_per_mol`: number

### configurational_entropy.csv
- path: `/app/outputs/configurational_entropy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Temperature dependence of the configurational entropy; must exhibit a monotonic decrease and plateau near Tg.
- schema:
  - `type`: table
  - `required_columns`: `T`, `S_c`
  - `units`:
    - `T`: K
    - `S_c`: J/K/mol

### residual_configurational_entropy.json
- path: `/app/outputs/residual_configurational_entropy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Residual configurational entropy (J/K/mol) at the glass transition temperature.
- schema:
  - `type`: object
  - `required`:
    - `S_c_residual_J_per_K_per_mol`: number
    - `T_g_K`: number

Notes: The target_policy for the S_c curve uses structural audit to verify monotonic decrease and plateau near Tg, while scalar quantities are evaluated by exact match with the paper‑reported values within appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_enthalpy_entropy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_H_kJ_per_mol": "number",
          "delta_S_J_per_K_per_mol": "number"
        }
      },
      "description": "Transition enthalpy (kJ/mol) and entropy (J/K/mol) for the ordered‑to‑plastic phase transition."
    },
    {
      "file": "glass_transition_deltaCp.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "T_g_K": "number",
          "delta_Cp_J_per_K_per_mol": "number"
        }
      },
      "description": "Glass transition temperature (K) and heat capacity jump (J/K/mol) of cyanoadamantane."
    },
    {
      "file": "configurational_entropy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "S_c"
        ],
        "units": {
          "T": "K",
          "S_c": "J/K/mol"
        }
      },
      "description": "Temperature dependence of the configurational entropy; must exhibit a monotonic decrease and plateau near Tg."
    },
    {
      "file": "residual_configurational_entropy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "S_c_residual_J_per_K_per_mol": "number",
          "T_g_K": "number"
        }
      },
      "description": "Residual configurational entropy (J/K/mol) at the glass transition temperature."
    }
  ],
  "notes": "The target_policy for the S_c curve uses structural audit to verify monotonic decrease and plateau near Tg, while scalar quantities are evaluated by exact match with the paper‑reported values within appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently inspects your output artifacts and computes a reward between 0 and 1. The scalar quantities (transition enthalpy, transition entropy, glass transition temperature and jump, residual configurational entropy) are checked against reference values derived from the underlying physical properties; numeric agreement within appropriate tolerances is required. The configurational entropy curve is assessed both by verifying its structural properties (e.g., monotonic decrease with temperature, a clear plateau near the glass transition) and by checking selected point values. Your reward will reflect the accuracy and plausibility of all these artifacts combined. Simply writing down assumed numbers without performing the prescribed analysis will not produce a reward.
