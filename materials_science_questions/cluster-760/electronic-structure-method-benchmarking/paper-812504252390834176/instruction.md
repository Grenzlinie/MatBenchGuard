# Molar enthalpy change of n-butanol–gasoline–ethanol blends from DFT thermochemistry

## Problem background
Biofuels, such as butanol, are being investigated as renewable substitutes for ethanol and gasoline in internal combustion engines. A key parameter during fuel injection is the molar enthalpy change ΔH = H(600 K) − H(298.15 K) at 1 atm, as it reflects the heat absorbed by the fuel before combustion. This task reproduces density functional theory (DFT) thermochemical calculations that compare the enthalpy change of n‑butanol with gasoline‑ethanol mixtures and examine whether blending n‑butanol into those mixtures can alter the blend’s enthalpy change. The gasoline component is represented by a multicomponent surrogate whose composition is taken from a published experimental analysis.

## Approach
The enthalpy change of each fuel component is obtained from first‑principles DFT calculations at the B3LYP/6‑311++G(d,p) level. For each molecule, a geometry optimization is performed, followed by a vibrational frequency analysis, which provides the molar enthalpy H(T) and the constant‑pressure heat capacity Cp at the required temperatures. The per‑molecule ΔH is simply H(600 K) − H(298.15 K). Mixture properties are then computed by mole‑weighted averaging of the pure‑component ΔH values, using the known molar masses and the published weight fractions of the gasoline surrogate. The workflow is organized as three sequential stages: (1) DFT thermochemistry for all fuel molecules, yielding a table of pure‑component enthalpies; (2) validation of the DFT level by comparing the computed Cp of n‑butanol at 298.15 K against the experimental value from the NIST Chemistry WebBook; (3) mole‑weighted mixture analysis to obtain ΔH and the percentage difference relative to n‑butanol for the required blends. Any open‑source DFT package (e.g., ORCA or PySCF) capable of B3LYP/6‑311++G(d,p) calculations and thermochemistry analysis is acceptable; the proprietary software used in the original study is not required.

## Reproduction target
Produce the two CSV files described in the Workflow steps:

- `cp_validation.csv` – At least one row at T = 298.15 K containing the DFT‑computed Cp of n‑butanol (Cp_theoretical_JmolK), the NIST experimental Cp value (Cp_experimental_JmolK), and the relative error (RelativeError_percent).
- `enthalpy_analysis.csv` – Molar enthalpy change ΔH = H(600 K) − H(298.15 K) and the percentage difference ΔH% relative to pure n‑butanol for the following blends:
  - n‑butanol (pure)
  - G100 (gasoline surrogate blend defined by the published composition)
  - G10E (90 mol% G100 + 10 mol% ethanol)
  - G20E (80 mol% G100 + 20 mol% ethanol)
  - G10E blended with 60 mol% n‑butanol (i.e., 0.4 G10E + 0.6 n‑butanol)
  - G100 blended with 40 mol% n‑butanol (i.e., 0.6 G100 + 0.4 n‑butanol)

## Assets

- Molecular structures of n-butanol, ethanol, and gasoline surrogate components: https://pubchem.ncbi.nlm.nih.gov/
- Gasoline surrogate composition (Burri et al. 2004): 10.1016/j.fuel.2003.09.013
- NIST experimental Cp for gas-phase n-butanol at 298.15 K: https://webbook.nist.gov/cgi/cbook.cgi?ID=C71363&Units=SI&Mask=1#Thermo-Gas
- Open-source DFT software (ORCA or PySCF): https://orcaforum.kofo.mpg.de/ or https://pyscf.org/

## Workflow steps

### Step 1: DFT thermochemistry of fuel molecules
- Role: process
- Action: Perform geometry optimization and vibrational frequency analysis for n-butanol, ethanol, and all gasoline surrogate molecules listed in Burri et al. (Fuel 83, 2004, Table 1) at B3LYP/6-311++G(d,p). Extract molar enthalpy H at 298.15 K and 600 K, and for n-butanol also compute Cp at 298.15 K. Save the results as component_enthalpy.csv.
- Evidence: `/app/outputs/component_enthalpy.csv`

### Step 2: Cp validation for n-butanol
- Role: scored
- Action: Using the DFT-calculated Cp for n-butanol at 298.15 K from Step 1 and the experimental Cp value obtained from NIST, compute the relative error. Output cp_validation.csv with at least one row at 298.15 K.
- Output file: `/app/outputs/cp_validation.csv`
- Format: csv
- Contract: Columns: Temperature_K (float), Cp_theoretical_JmolK (float), Cp_experimental_JmolK (float), RelativeError_percent (float).
- Scoring: scored by hidden verifier

### Step 3: Mixture enthalpy change analysis
- Role: scored
- Action: From the component_enthalpy.csv, compute per-molecule ΔH = H(600 K) - H(298.15 K). Determine mole fractions for the G100 gasoline surrogate blend using the weight percentages from Burri et al. (2004) and known molecular weights. Then compute mole-weighted ΔH for the following blends: pure n-butanol; G100; G10E (0.9 G100 + 0.1 ethanol); G20E (0.8 G100 + 0.2 ethanol); G10E blended with 60 mol% n-butanol (i.e., 0.4 G10E + 0.6 n-butanol); G100 blended with 40 mol% n-butanol (0.6 G100 + 0.4 n-butanol). Output enthalpy_analysis.csv with the indicated rows. **IMPORTANT:** The Blend column must contain exactly the following strings (case-sensitive): `n-butanol`, `G100`, `G10E`, `G20E`, `G10E_plus_60pct_nbutanol`, `G100_plus_40pct_nbutanol`. Other names will cause the verifier to miss the row and score zero.
- Output file: `/app/outputs/enthalpy_analysis.csv`
- Format: csv
- Contract: Columns: Blend (string), Delta_H_kJ_per_mol (float), Delta_H_percent_vs_n_butanol (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cp_validation.csv`
- `/app/outputs/enthalpy_analysis.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cp_validation.csv
- path: `/app/outputs/cp_validation.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Validation of DFT computed Cp for n-butanol against experimental NIST value. At least one row at T=298.15 K. The checker will extract RelativeError_percent and score it against a ≤4% threshold.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `Cp_theoretical_JmolK`, `Cp_experimental_JmolK`, `RelativeError_percent`
  - `units`:
    - `Temperature_K`: K
    - `Cp_theoretical_JmolK`: J/(mol K)
    - `Cp_experimental_JmolK`: J/(mol K)
    - `RelativeError_percent`: %

### enthalpy_analysis.csv
- path: `/app/outputs/enthalpy_analysis.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Molar enthalpy change and percentage difference relative to pure n-butanol for the listed fuel blends. The verifier will check the required rows exist and verify structural properties: the relative ordering of ΔH values among G100, G10E, G20E, n-butanol, and the compensation effects (G10E+60% n-butanol ≈ G20E; G100+40% n-butanol ≈ G10E).
- schema:
  - `type`: table
  - `required_columns`: `Blend`, `Delta_H_kJ_per_mol`, `Delta_H_percent_vs_n_butanol`
  - `units`:
    - `Delta_H_kJ_per_mol`: kJ/mol
    - `Delta_H_percent_vs_n_butanol`: %
  - `required_blend_values`: `n-butanol`, `G100`, `G10E`, `G20E`, `G10E_plus_60pct_nbutanol`, `G100_plus_40pct_nbutanol`

Notes: All files are placed under /app/outputs. The Cp validation uses the NIST experimental value (the agent must fetch it from the provided NIST URL). The mixture analysis uses the component enthalpies computed by the agent in step_1; the verifier will validate the reported enthalpy_analysis.csv against structural constraints and may check that the intermediate component_enthalpy.csv contains the required columns as evidence of the process step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cp_validation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "Cp_theoretical_JmolK",
          "Cp_experimental_JmolK",
          "RelativeError_percent"
        ],
        "units": {
          "Temperature_K": "K",
          "Cp_theoretical_JmolK": "J/(mol K)",
          "Cp_experimental_JmolK": "J/(mol K)",
          "RelativeError_percent": "%"
        }
      },
      "description": "Validation of DFT computed Cp for n-butanol against experimental NIST value. At least one row at T=298.15 K. The checker will extract RelativeError_percent and score it against a ≤4% threshold."
    },
    {
      "file": "enthalpy_analysis.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Blend",
          "Delta_H_kJ_per_mol",
          "Delta_H_percent_vs_n_butanol"
        ],
        "units": {
          "Delta_H_kJ_per_mol": "kJ/mol",
          "Delta_H_percent_vs_n_butanol": "%"
        },
        "required_blend_values": [
          "n-butanol",
          "G100",
          "G10E",
          "G20E",
          "G10E_plus_60pct_nbutanol",
          "G100_plus_40pct_nbutanol"
        ]
      },
      "description": "Molar enthalpy change and percentage difference relative to pure n-butanol for the listed fuel blends. The verifier will check the required rows exist and verify structural properties: the relative ordering of ΔH values among G100, G10E, G20E, n-butanol, and the compensation effects (G10E+60% n-butanol ≈ G20E; G100+40% n-butanol ≈ G10E)."
    }
  ],
  "notes": "All files are placed under /app/outputs. The Cp validation uses the NIST experimental value (the agent must fetch it from the provided NIST URL). The mixture analysis uses the component enthalpies computed by the agent in step_1; the verifier will validate the reported enthalpy_analysis.csv against structural constraints and may check that the intermediate component_enthalpy.csv contains the required columns as evidence of the process step."
}
```

## How you are scored
A hidden verifier independently reads your submitted CSV files and scores each scored stage, then combines the stage scores into a final reward between 0 and 1. The verifier compares your computed quantities to hidden reference values (paper‑reported results or derived trends) with appropriate tolerances; you do not know those references or the exact tolerances.

For `cp_validation.csv`, the verifier checks that the relative error meets a hidden threshold. For `enthalpy_analysis.csv`, the verifier may recompute mixture ΔH values from the intermediate `component_enthalpy.csv` (if present) and compare your reported ΔH and percentages to the hidden targets, as well as verify the relative ordering of the ΔH values across the blends.

Simply writing numbers that match the original paper is not sufficient; the numbers must follow from the required DFT calculations and the prescribed averaging procedure.
