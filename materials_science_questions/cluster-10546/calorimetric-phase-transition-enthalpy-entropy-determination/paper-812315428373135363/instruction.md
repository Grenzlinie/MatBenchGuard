# Calorimetric Phase Transition Enthalpy and Entropy Determination

## Problem background
The spin‑crossover compounds [Fe(phen)<sub>2</sub>(NCS)<sub>2</sub>] and [Fe(phen)<sub>2</sub>(NCSe)<sub>2</sub>] display a cooperative transition between a low‑spin and a high‑spin electronic ground state. Calorimetric measurements reveal a sharp heat‑capacity anomaly at a critical temperature, and the associated thermodynamic quantities (transition enthalpy ΔH and entropy ΔS) are substantially larger than what can be attributed to magnetic effects alone. This task quantifies those thermodynamic changes and explores a phenomenological heterophase‑fluctuation model in which the transition is driven by coupling between the electronic state and the phonon system. The work tests whether a model relying on coexisting spin phases and a single temperature‑independent energy separation can account for the observed cooperative behaviour.

## Approach
The core idea is to separate the measured heat capacity into a 'normal' baseline and an excess contribution due to the spin transition.

The normal baseline is built from three contributions:
- **Lattice vibrations:** described by a Debye model with effective frequency spectra obtained from the experimental data in regions far from the transition.
- **Internal vibrations:** treated with an Einstein model using the provided IR‑active wavenumbers.
- **Magnetic/electronic contribution:** computed from the low‑lying energy‑level scheme (parameters supplied).
Four physically motivated extrapolations (different Debye cut‑off choices) are constructed for both the low‑temperature and high‑temperature phases; their arithmetic mean is taken as the final baseline.

Subtracting this baseline from the experimental C<sub>p</sub> yields the excess heat capacity. Numerical integration gives the transition enthalpy ΔH, and integration of the excess divided by temperature gives the transition entropy ΔS.

The heterophase‑fluctuation model treats the system as a collection of cells, each containing <em>n</em> molecules. The mole fraction <em>x</em> of the high‑spin phase is determined by minimising a Gibbs free energy that includes an ideal mixing entropy term. The model heat capacity is then calculated from <em>x</em> and the normal heat capacities of the two phases. By equating the maximum model heat capacity to the experimental peak value, the number of cells <em>N</em> (and subsequently <em>n</em> = N<sub>A</sub> / <em>N</em>) can be deduced. The full C<sub>p</sub>(<em>T</em>) curve predicted by the model is also generated for comparison.

## Reproduction target
The objective is to compute, for both [Fe(phen)<sub>2</sub>(NCS)<sub>2</sub>] and [Fe(phen)<sub>2</sub>(NCSe)<sub>2</sub>]:

1. The transition enthalpy ΔH (kJ mol<sup>−1</sup>) and entropy ΔS (J K<sup>−1</sup> mol<sup>−1</sup>).
2. The heterophase‑fluctuation model parameters: the number of cells <em>N</em> (mol<sup>−1</sup>) and the number of molecules per cell <em>n</em>.
3. The predicted heat‑capacity anomaly curve (C<sub>p</sub> model vs. temperature) produced by the model over a dense temperature grid covering the transition region.

The calculations must use the provided experimental heat‑capacity tables, the supplied IR wavenumbers, and the electronic energy‑level parameters. All results must be written to the specified output files under `/app/outputs`.

## Assets

- Heat capacity data for [Fe(phen)2(NCS)2] (Table 1)
- Heat capacity data for [Fe(phen)2(NCSe)2] (Table 2)
- IR internal vibration wavenumbers for spin phases
- Electronic energy level parameters
- Python scientific stack: numpy, scipy, matplotlib

## Workflow steps

### Step 1: Determine normal heat capacity baselines and enthalpy/entropy of phases
- Role: process
- Action: For each compound, ingest the experimental Cp(T) data and the provided IR wavenumbers and energy parameters. Compute the normal heat capacity baseline C_p(normal) as the sum of lattice (Debye model with cutoffs 30 and 50 cm⁻¹, using extrapolation to obtain effective frequency spectra), internal vibrations (Einstein model), and magnetic/electronic contributions. Construct four extrapolations (curves A–D) for the low- and high-temperature phases as described in the paper and take their arithmetic mean as the baseline. Integrate the baselines to obtain the enthalpy H_L(T), H_H(T) and entropy S_L(T), S_H(T) of each phase. Identify the transition temperature T_c (peak of experimental Cp) and the maximum heat capacity C_p(max). Save intermediate baseline curves, enthalpy/entropy, T_c, and C_p(max) for subsequent steps.
- Evidence: `/app/outputs/step_00_baseline.json`

### Step 2: Transition enthalpy and entropy for [Fe(phen)2(NCS)2]
- Role: scored
- Action: Subtract the normal heat capacity baseline (from step_00) from the experimental Cp(T) for [Fe(phen)2(NCS)2] to obtain the excess heat capacity ΔC_p_excess. Integrate ΔC_p_excess with respect to temperature from below to above T_c to compute the transition enthalpy ΔH. Divide ΔC_p_excess by T and integrate to obtain the transition entropy ΔS. Write the results along with T_c to /app/outputs/step_01a_thermo_NCS.json.
- Output file: `/app/outputs/step_01a_thermo_NCS.json`
- Format: json
- Contract: {"compound": "[Fe(phen)2(NCS)2]", "Tc_K": 176.29, "Delta_H_kJ_mol": <float>, "Delta_S_J_K_mol": <float>}
- Scoring: scored by hidden verifier

### Step 3: Transition enthalpy and entropy for [Fe(phen)2(NCSe)2]
- Role: scored
- Action: Analogous to step_01a, but for [Fe(phen)2(NCSe)2]. Write to /app/outputs/step_01b_thermo_NCSe.json.
- Output file: `/app/outputs/step_01b_thermo_NCSe.json`
- Format: json
- Contract: {"compound": "[Fe(phen)2(NCSe)2]", "Tc_K": 231.26, "Delta_H_kJ_mol": <float>, "Delta_S_J_K_mol": <float>}
- Scoring: scored by hidden verifier

### Step 4: Model parameters (N, n) for [Fe(phen)2(NCS)2]
- Role: scored
- Action: Using the C_p(max), T_c, and the enthalpy difference H_H(T_c) − H_L(T_c) from step_00, compute the number of cells N and the number of molecules per cell n = N_A / N, where N_A is Avogadro's constant, using the relation derived from the heterophase-fluctuation model's expression for maximum heat capacity. Write the values to /app/outputs/step_02a_model_NCS.json.
- Output file: `/app/outputs/step_02a_model_NCS.json`
- Format: json
- Contract: {"compound": "[Fe(phen)2(NCS)2]", "N_mol-1": <float>, "n": <int>}
- Scoring: scored by hidden verifier

### Step 5: Model parameters (N, n) for [Fe(phen)2(NCSe)2]
- Role: scored
- Action: Analogous to step_02a, but for [Fe(phen)2(NCSe)2]. Write to /app/outputs/step_02b_model_NCSe.json.
- Output file: `/app/outputs/step_02b_model_NCSe.json`
- Format: json
- Contract: {"compound": "[Fe(phen)2(NCSe)2]", "N_mol-1": <float>, "n": <int>}
- Scoring: scored by hidden verifier

### Step 6: Heat capacity anomaly curve for [Fe(phen)2(NCS)2]
- Role: scored (load-bearing)
- Action: For [Fe(phen)2(NCS)2], use the equilibrium mole fraction x(T) from the heterophase-fluctuation model and the normal heat capacities C_p,H(T), C_p,L(T) from step_00 to compute the model heat capacity C_p(T) over a temperature grid covering the transition region (e.g., from well below to well above T_c). Write a CSV file with columns T(K) and Cp_model(J/K/mol) to /app/outputs/step_03a_cp_anomaly_NCS.csv. The grid should be sufficiently dense to capture the peak shape.
- Output file: `/app/outputs/step_03a_cp_anomaly_NCS.csv`
- Format: csv
- Contract: T(K), Cp_model(J/K/mol)
- Scoring: scored by hidden verifier

### Step 7: Heat capacity anomaly curve for [Fe(phen)2(NCSe)2]
- Role: scored (load-bearing)
- Action: Analogous to step_03a, but for [Fe(phen)2(NCSe)2]. Write to /app/outputs/step_03b_cp_anomaly_NCSe.csv.
- Output file: `/app/outputs/step_03b_cp_anomaly_NCSe.csv`
- Format: csv
- Contract: T(K), Cp_model(J/K/mol)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01a_thermo_NCS.json`
- `/app/outputs/step_01b_thermo_NCSe.json`
- `/app/outputs/step_02a_model_NCS.json`
- `/app/outputs/step_02b_model_NCSe.json`
- `/app/outputs/step_03a_cp_anomaly_NCS.csv`
- `/app/outputs/step_03b_cp_anomaly_NCSe.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01a_thermo_NCS.json
- path: `/app/outputs/step_01a_thermo_NCS.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Transition temperature, enthalpy, and entropy for [Fe(phen)2(NCS)2].
- schema:
  - `type`: object
  - `required`:
    - `compound`: string
    - `Tc_K`: number
    - `Delta_H_kJ_mol`: number
    - `Delta_S_J_K_mol`: number
  - `items`: object
  - `required_columns`:
  - `units`:
    - `Tc_K`: K
    - `Delta_H_kJ_mol`: kJ mol⁻¹
    - `Delta_S_J_K_mol`: J K⁻¹ mol⁻¹

### step_01b_thermo_NCSe.json
- path: `/app/outputs/step_01b_thermo_NCSe.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Transition temperature, enthalpy, and entropy for [Fe(phen)2(NCSe)2].
- schema:
  - `type`: object
  - `required`:
    - `compound`: string
    - `Tc_K`: number
    - `Delta_H_kJ_mol`: number
    - `Delta_S_J_K_mol`: number
  - `items`: object
  - `required_columns`:
  - `units`:
    - `Tc_K`: K
    - `Delta_H_kJ_mol`: kJ mol⁻¹
    - `Delta_S_J_K_mol`: J K⁻¹ mol⁻¹

### step_02a_model_NCS.json
- path: `/app/outputs/step_02a_model_NCS.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Number of cells N and molecules per cell n for [Fe(phen)2(NCS)2].
- schema:
  - `type`: object
  - `required`:
    - `compound`: string
    - `N_mol-1`: number
    - `n`: integer
  - `items`: object
  - `required_columns`:
  - `units`:
    - `N_mol-1`: mol⁻¹
    - `n`: molecules per cell

### step_02b_model_NCSe.json
- path: `/app/outputs/step_02b_model_NCSe.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Number of cells N and molecules per cell n for [Fe(phen)2(NCSe)2].
- schema:
  - `type`: object
  - `required`:
    - `compound`: string
    - `N_mol-1`: number
    - `n`: integer
  - `items`: object
  - `required_columns`:
  - `units`:
    - `N_mol-1`: mol⁻¹
    - `n`: molecules per cell

### step_03a_cp_anomaly_NCS.csv
- path: `/app/outputs/step_03a_cp_anomaly_NCS.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Model heat capacity curve for [Fe(phen)2(NCS)2] as a CSV file.
- schema:
  - `type`: table
  - `required`: object
  - `items`:
    - `T(K)`: number
    - `Cp_model(J/K/mol)`: number
  - `required_columns`: `T(K)`, `Cp_model(J/K/mol)`
  - `units`:
    - `T(K)`: K
    - `Cp_model(J/K/mol)`: J K⁻¹ mol⁻¹

### step_03b_cp_anomaly_NCSe.csv
- path: `/app/outputs/step_03b_cp_anomaly_NCSe.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Model heat capacity curve for [Fe(phen)2(NCSe)2] as a CSV file.
- schema:
  - `type`: table
  - `required`: object
  - `items`:
    - `T(K)`: number
    - `Cp_model(J/K/mol)`: number
  - `required_columns`: `T(K)`, `Cp_model(J/K/mol)`
  - `units`:
    - `T(K)`: K
    - `Cp_model(J/K/mol)`: J K⁻¹ mol⁻¹

Notes: The task requires the agent to implement the baseline separation and the heterophase-fluctuation model from the provided equations and data. All necessary numerical values (Tc, energy parameters, wavenumbers) are embedded in the resources or derivable from the procedure.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01a_thermo_NCS.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "compound": "string",
          "Tc_K": "number",
          "Delta_H_kJ_mol": "number",
          "Delta_S_J_K_mol": "number"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "Tc_K": "K",
          "Delta_H_kJ_mol": "kJ mol⁻¹",
          "Delta_S_J_K_mol": "J K⁻¹ mol⁻¹"
        }
      },
      "description": "Transition temperature, enthalpy, and entropy for [Fe(phen)2(NCS)2]."
    },
    {
      "file": "step_01b_thermo_NCSe.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "compound": "string",
          "Tc_K": "number",
          "Delta_H_kJ_mol": "number",
          "Delta_S_J_K_mol": "number"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "Tc_K": "K",
          "Delta_H_kJ_mol": "kJ mol⁻¹",
          "Delta_S_J_K_mol": "J K⁻¹ mol⁻¹"
        }
      },
      "description": "Transition temperature, enthalpy, and entropy for [Fe(phen)2(NCSe)2]."
    },
    {
      "file": "step_02a_model_NCS.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "compound": "string",
          "N_mol-1": "number",
          "n": "integer"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "N_mol-1": "mol⁻¹",
          "n": "molecules per cell"
        }
      },
      "description": "Number of cells N and molecules per cell n for [Fe(phen)2(NCS)2]."
    },
    {
      "file": "step_02b_model_NCSe.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "compound": "string",
          "N_mol-1": "number",
          "n": "integer"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "N_mol-1": "mol⁻¹",
          "n": "molecules per cell"
        }
      },
      "description": "Number of cells N and molecules per cell n for [Fe(phen)2(NCSe)2]."
    },
    {
      "file": "step_03a_cp_anomaly_NCS.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required": {},
        "items": {
          "T(K)": "number",
          "Cp_model(J/K/mol)": "number"
        },
        "required_columns": [
          "T(K)",
          "Cp_model(J/K/mol)"
        ],
        "units": {
          "T(K)": "K",
          "Cp_model(J/K/mol)": "J K⁻¹ mol⁻¹"
        }
      },
      "description": "Model heat capacity curve for [Fe(phen)2(NCS)2] as a CSV file."
    },
    {
      "file": "step_03b_cp_anomaly_NCSe.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required": {},
        "items": {
          "T(K)": "number",
          "Cp_model(J/K/mol)": "number"
        },
        "required_columns": [
          "T(K)",
          "Cp_model(J/K/mol)"
        ],
        "units": {
          "T(K)": "K",
          "Cp_model(J/K/mol)": "J K⁻¹ mol⁻¹"
        }
      },
      "description": "Model heat capacity curve for [Fe(phen)2(NCSe)2] as a CSV file."
    }
  ],
  "notes": "The task requires the agent to implement the baseline separation and the heterophase-fluctuation model from the provided equations and data. All necessary numerical values (Tc, energy parameters, wavenumbers) are embedded in the resources or derivable from the procedure."
}
```

## How you are scored
Each scored workflow stage is independently evaluated by a hidden verifier. The verifier reads the output artifact you produce and compares the computed quantities (ΔH, ΔS, <em>N</em>, <em>n</em>, and the C<sub>p</sub> anomaly curve) to reference values established from the original study. The comparisons use appropriate tolerances that account for legitimate differences in implementation details. For the heat‑capacity curves, structural properties such as peak height and shape are also checked. The individual stage scores are combined with weights that reflect their importance, producing a final reward between 0 and 1. Reaching the published numbers is not sufficient on its own; the artifacts must be derived by executing the described analysis pipeline and must align with the expected behaviour of the model.
