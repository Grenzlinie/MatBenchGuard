# Thermodynamic Boron Distribution during Silicon Codeposition from Chlorosilanes

## Problem background
During chemical vapor deposition (CVD) of silicon from trichlorosilane (SiHCl3) and hydrogen, boron doping occurs via halide species. A thermodynamic model based on surface reactions and quasi-regular solution theory describes the distribution of boron between the gas phase and the solid silicon. The model yields two key quantities: the boron activity coefficient γ_B, which captures non-ideality in the solid solution, and the distribution ratio α°, which relates the gas-phase and solid-phase boron concentrations. Computing these quantities from fundamental thermochemical data is central to understanding doping control in semiconductor processing.

## Approach
The approach uses a set of six surface reactions that describe the removal of silicon and boron atoms from the solid by HCl and H2, forming chlorosilanes and boron halides. Equilibrium constants for these reactions are obtained from publicly available JANAF thermochemical tables. The silicon deposition equilibrium is solved as a small nonlinear system to obtain the gas-phase partial pressures of HCl and H2 and the conversion fraction x at each temperature and initial H2/SiHCl3 ratio. The boron activity coefficient γ_B is estimated from a quasi-regular solution model that uses the experimentally known saturation solubility of boron in silicon and an estimated free energy of formation of the coexisting boride phase. Finally, the boron distribution ratio α° is calculated by combining γ_B, the partial pressures, and the equilibrium constants for the boron-containing reactions. The work culminates in a grid of α° values over a range of temperatures and inlet gas compositions.

## Reproduction target
The goal is to compute the boron activity coefficient γ_B at temperatures of 1200, 1300, 1400, and 1500 K using the thermodynamic model, and to compute the boron distribution ratio α° for the same four temperatures and initial H2/SiHCl3 partial pressure ratios of 1, 5, and 10 at a total pressure of 1 atm. The results must be written to the two specified CSV files with the exact column schemas described in the output contract. The intermediate equilibrium constants and the solved silicon deposition equilibrium are required steps to produce the final α° values.

## Assets

- JANAF Thermochemical Tables: https://janaf.nist.gov/
- Python environment

## Workflow steps

### Step 1: Retrieve equilibrium constants from JANAF
- Role: process
- Action: Obtain standard thermodynamic properties (ΔG_f°, ΔH_f°, S°) from JANAF for all gaseous species: SiHCl₃, SiCl₄, SiCl₂, BCl₃, BHCl₂, BH₂Cl, HCl, H₂. For each temperature in the range 1100–1600 K, compute the equilibrium constants K1–K6 for the six surface reactions using K = exp(-ΔG_rxn/(RT)). Save the temperature-dependent constants for later use.
- Evidence: `/app/outputs/K_values.json`

### Step 2: Compute boron activity coefficient γ_B
- Role: scored
- Action: Compute the boron activity coefficient γ_B at T = 1200, 1300, 1400, 1500 K using the quasi-regular solution approximation with given saturation solubility (log10 N_B^sat = -2852/T - 0.214), N_B^C = 0.8, estimated ΔG_f0(SiB₃₋₄) = 4.5 kcal/mol, and R = 1.987 cal/(mol·K). Write the result to gamma_B_values.csv.
- Output file: `/app/outputs/gamma_B_values.csv`
- Format: csv
- Contract: CSV with columns: T_K (int), gamma_B (float). Rows for T=1200,1300,1400,1500.
- Scoring: scored by hidden verifier

### Step 3: Solve silicon deposition equilibrium
- Role: process
- Action: Using the equilibrium constants K1–K3 from step00, solve the nonlinear system for the silicon deposition reactions at each temperature (1200,1300,1400,1500 K) and each initial H₂/SiHCl₃ partial pressure ratio (1, 5, 10) with total pressure 1 atm. Determine the gas-phase partial pressures p_HCl, p_H₂ and the degree of conversion x = n_Si / n_SiHCl₃ initial. Save the results.
- Evidence: `/app/outputs/Si_equilibrium.csv`

### Step 4: Compute boron distribution ratio α°
- Role: scored (load-bearing)
- Action: For each temperature (1200,1300,1400,1500 K) and each ratio (1,5,10), compute α° using the thermodynamic expression α° ≈ x + (1-x) * (γ_B * Σ_{n=4}^{6} K_n p_HCl^{l_n} p_H₂^{m_n}) / (Σ_{n=1}^{3} K_n p_HCl^{l_n} p_H₂^{m_n}), with γ_B from step01 and p_HCl, p_H₂, x from step02; use γ_Si ≈ 1. Output the results to alpha_conditions.csv.
- Output file: `/app/outputs/alpha_conditions.csv`
- Format: csv
- Contract: CSV with columns: T_K (int), ratio_H2_SiHCl3 (float), alpha (float). Rows for T=1200,1300,1400,1500 and ratio=1,5,10.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gamma_B_values.csv`
- `/app/outputs/alpha_conditions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gamma_B_values.csv
- path: `/app/outputs/gamma_B_values.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Boron activity coefficient at 1200, 1300, 1400, 1500 K computed from the quasi-regular solution model.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `gamma_B`
  - `units`:
    - `T_K`: K
    - `gamma_B`: dimensionless

### alpha_conditions.csv
- path: `/app/outputs/alpha_conditions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Boron distribution ratio α° for specified temperatures and initial H₂/SiHCl₃ ratios.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `ratio_H2_SiHCl3`, `alpha`
  - `units`:
    - `T_K`: K
    - `ratio_H2_SiHCl3`: dimensionless
    - `alpha`: dimensionless

Notes: The intermediate equilibrium constants and Si equilibrium results (K_values.json, Si_equilibrium.csv) are not directly scored but are required to compute the final α° artifact. The checker will recompute α° from the submitted gamma_B and Si_equilibrium artifacts and verify both numerical agreement and monotonic trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gamma_B_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "gamma_B"
        ],
        "units": {
          "T_K": "K",
          "gamma_B": "dimensionless"
        }
      },
      "description": "Boron activity coefficient at 1200, 1300, 1400, 1500 K computed from the quasi-regular solution model."
    },
    {
      "file": "alpha_conditions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "ratio_H2_SiHCl3",
          "alpha"
        ],
        "units": {
          "T_K": "K",
          "ratio_H2_SiHCl3": "dimensionless",
          "alpha": "dimensionless"
        }
      },
      "description": "Boron distribution ratio α° for specified temperatures and initial H₂/SiHCl₃ ratios."
    }
  ],
  "notes": "The intermediate equilibrium constants and Si equilibrium results (K_values.json, Si_equilibrium.csv) are not directly scored but are required to compute the final α° artifact. The checker will recompute α° from the submitted gamma_B and Si_equilibrium artifacts and verify both numerical agreement and monotonic trends."
}
```

## How you are scored
A hidden verifier independently examines your output files. For γ_B it recomputes the values using the same quasi-regular solution model and checks that your numbers fall within an acceptable tolerance. For α° it recomputes the quantity from your raw artifacts (or from independently derived values) and verifies that the computed results satisfy the expected physical trends between the different temperature and ratio conditions. Each scored artifact contributes a portion to the final reward. Simply reporting the paper's published numbers without executing the required thermodynamic calculations will not pass the verification.
