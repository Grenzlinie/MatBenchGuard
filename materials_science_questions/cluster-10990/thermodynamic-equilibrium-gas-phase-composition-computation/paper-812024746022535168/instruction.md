# Thermodynamic Boron Distribution during Silicon Codeposition from Chlorosilanes

## Problem background
During chemical vapor deposition (CVD) of silicon from trichlorosilane (SiHCl3) and hydrogen, boron doping occurs via halide species. A thermodynamic model based on surface reactions and quasi-regular solution theory describes the distribution of boron between the gas phase and the solid silicon. The model yields two key quantities: the boron activity coefficient γ_B, which captures non-ideality in the solid solution, and the distribution ratio α°, which relates the gas-phase and solid-phase boron concentrations. Computing these quantities from fundamental thermochemical data is central to understanding doping control in semiconductor processing.

## Approach
The approach uses a set of six surface reactions that describe the removal of silicon and boron atoms from the solid by HCl and H2, forming chlorosilanes and boron halides:

(1) [Si] + 3 HCl → SiHCl3 + H2
(2) [Si] + 4 HCl → SiCl4 + 2 H2
(3) [Si] + 2 HCl → SiCl2 + H2
(4) [B] + 3 HCl → BCl3 + 1.5 H2
(5) [B] + 2 HCl → BHCl2 + 0.5 H2
(6) [B] + HCl + 0.5 H2 → BH2Cl

The stoichiometric coefficients for HCl and H2 in the α° expression (see below) are denoted l_n and m_n and are defined with the sign convention that **reactant coefficients are positive, product coefficients are negative** for H2 (HCl is always a reactant, so its coefficient is always positive):

| reaction n | l_n (HCl) | m_n (H2) |
|------------|-----------|-----------|
| 1          | 3         | –1        |
| 2          | 4         | –2        |
| 3          | 2         | –1        |
| 4          | 3         | –1.5      |
| 5          | 2         | –0.5      |
| 6          | 1         | +0.5      |

For each reaction n, the equilibrium constant K_n is defined according to the direction written above (i.e. solid + HCl (+ H2) → gaseous products) with solid activities taken as unity. Thus, for example:

K1 = p_SiHCl3 · p_H2 / p_HCl^3
K6 = p_BH2Cl / (p_HCl · p_H2^0.5)

All partial pressures are in atmospheres. The K_n are computed from standard thermodynamic data as K_n = exp(–ΔG_rxn_n / (R T)), where ΔG_rxn_n is the standard Gibbs free energy change of reaction n at temperature T.

Using these definitions, the hypothetical partial pressures required for α° can be written directly as sums of the relevant gaseous species pressures:

p_Si* = p_SiHCl3 + p_SiCl4 + p_SiCl2 = K1 p_HCl^3 p_H2^(–1) + K2 p_HCl^4 p_H2^(–2) + K3 p_HCl^2 p_H2^(–1)

p_B*  = p_BCl3  + p_BHCl2  + p_BH2Cl  = K4 p_HCl^3 p_H2^(–1.5) + K5 p_HCl^2 p_H2^(–0.5) + K6 p_HCl^1 p_H2^(+0.5)

p_Cl* ≈ p_HCl + 3 p_SiHCl3 + 4 p_SiCl4 + 2 p_SiCl2
      = p_HCl + 3 K1 p_HCl^3 p_H2^(–1) + 4 K2 p_HCl^4 p_H2^(–2) + 2 K3 p_HCl^2 p_H2^(–1)

The degree of conversion of trichlorosilane, x, is defined as x = n_Si / n_SiHCl3^0, where n_Si is the number of silicon atoms deposited and n_SiHCl3^0 is the initial amount of SiHCl3. It can be obtained from:

x ≈ 1 – 3 p_Si* / p_Cl*

Equilibrium constants for these reactions are obtained from publicly available JANAF thermochemical tables. The silicon deposition equilibrium is solved as a small nonlinear system to obtain the gas-phase partial pressures of HCl and H2 and the conversion fraction x at each temperature and initial H2/SiHCl3 ratio. The boron activity coefficient γ_B is estimated from a quasi-regular solution model that uses the experimentally known saturation solubility of boron in silicon and an estimated free energy of formation of the coexisting boride phase. Finally, the boron distribution ratio α° is calculated by combining γ_B, the partial pressures, and the equilibrium constants for the boron-containing reactions. The work culminates in a grid of α° values over a range of temperatures and inlet gas compositions.

## Reproduction target
The goal is to compute the boron activity coefficient γ_B at temperatures of 1200, 1300, 1400, and 1500 K using the thermodynamic model, and to compute the boron distribution ratio α° for the same four temperatures and initial H2/SiHCl3 partial pressure ratios of 1, 5, and 10 at a total pressure of 1 atm. The results must be written to the two specified CSV files with the exact column schemas described in the output contract. The intermediate equilibrium constants and the solved silicon deposition equilibrium are required steps to produce the final α° values.

## Assets

- JANAF Thermochemical Tables: https://janaf.nist.gov/
- Python environment

## Workflow steps

### Step 1: Retrieve equilibrium constants from JANAF
- Role: process
- Action: Obtain standard thermodynamic properties (ΔG_f°, ΔH_f°, S°) from JANAF for all gaseous species: SiHCl₃, SiCl₄, SiCl₂, BCl₃, BHCl₂, BH₂Cl, HCl, H₂. For each temperature in the range 1100–1600 K, compute the equilibrium constants K1–K6 for the six surface reactions using K = exp(-ΔG_rxn/(RT)). You may store the temperature-dependent constants locally; they are not directly scored.

### Step 2: Compute boron activity coefficient γ_B
- Role: scored
- Action: Compute the boron activity coefficient γ_B at T = 1200, 1300, 1400, 1500 K using the quasi-regular solution approximation with given saturation solubility (log10 N_B^sat = -2852/T - 0.214), N_B^C = 0.8, estimated ΔG_f0(SiB₃₋₄) = 4.5 kcal/mol, and R = 1.987 cal/(mol·K). Write the result to gamma_B_values.csv.
- Output file: `/app/outputs/gamma_B_values.csv`
- Format: csv
- Contract: CSV with columns: T_K (int), gamma_B (float). Rows for T=1200,1300,1400,1500.
- Scoring: scored by hidden verifier

### Step 3: Solve silicon deposition equilibrium
- Role: process
- Action: For each temperature T ∈ {1200, 1300, 1400, 1500} K and each initial H₂/SiHCl₃ ratio R0 ∈ {1, 5, 10}, solve the silicon deposition equilibrium to obtain the partial pressures p_HCl and p_H₂, and the conversion x. Use the equilibrium constants K1–K3 obtained in Step 1 and the following relations:
  * Total pressure = 1 atm.
  * Initial composition (before reaction): p_SiHCl3^0 = 1/(1 + R0), p_H2^0 = R0/(1 + R0).
  * Express the partial pressures of the silicon-bearing gases in terms of p_HCl and p_H₂:
    p_SiHCl3 = K1 p_HCl^3 / p_H₂
    p_SiCl4  = K2 p_HCl^4 / p_H₂^2
    p_SiCl2  = K3 p_HCl^2 / p_H₂
  * Impose total pressure condition:
    p_HCl + p_H₂ + p_SiHCl3 + p_SiCl4 + p_SiCl2 = 1
  * Impose chlorine atom conservation (initial chlorine atoms come only from SiHCl₃):
    p_HCl + 3 p_SiHCl3 + 4 p_SiCl4 + 2 p_SiCl2 = 3 p_SiHCl3^0
  Solve the two equations for the two unknowns p_HCl, p_H₂ numerically (e.g., using scipy.optimize.fsolve). From the solution compute:
    p_Si* = p_SiHCl3 + p_SiCl4 + p_SiCl2
    p_Cl* = p_HCl + 3 p_SiHCl3 + 4 p_SiCl4 + 2 p_SiCl2
    x = 1 – 3 p_Si* / p_Cl*
  Store the results (T, R0, K1-K3, p_HCl, p_H₂, x) locally; they are not directly scored but must be used in Step 4.

### Step 4: Compute boron distribution ratio α°
- Role: scored (load-bearing)
- Action: For each temperature (1200,1300,1400,1500 K) and each ratio (1,5,10), compute α° using the thermodynamic expression:

  α° ≈ x + (1 – x) · [ γ_B · Σ_{n=4}^{6} K_n p_HCl^{l_n} p_H₂^{m_n} ] / [ γ_Si · Σ_{n=1}^{3} K_n p_HCl^{l_n} p_H₂^{m_n} ]

  with γ_Si ≈ 1, γ_B from Step 2, p_HCl, p_H₂, x from Step 3, and the coefficients (l_n, m_n) given in the table in the Approach section. Equivalently, you may use the simplified gas‑species forms:

  Σ_{n=1}^{3} K_n p_HCl^{l_n} p_H₂^{m_n} = p_SiHCl3 + p_SiCl4 + p_SiCl2
  Σ_{n=4}^{6} K_n p_HCl^{l_n} p_H₂^{m_n} = p_BCl3  + p_BHCl2  + p_BH2Cl

  where p_BCl3 = K4 p_HCl^3 / p_H₂^{1.5}, p_BHCl2 = K5 p_HCl^2 / p_H₂^{0.5}, p_BH2Cl = K6 p_HCl p_H₂^{0.5}.

  Output the results to alpha_conditions.csv.
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
- target_policy: numeric_table
- description: Boron distribution ratio α° for specified temperatures and initial H₂/SiHCl₃ ratios.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `ratio_H2_SiHCl3`, `alpha`
  - `units`:
    - `T_K`: K
    - `ratio_H2_SiHCl3`: dimensionless
    - `alpha`: dimensionless

Notes: The intermediate equilibrium constants and Si equilibrium results are not directly scored but are required to compute the final α° artifact. The checker will compare α° values against the paper's reference data and also verify monotonic trends (α° decreasing with increasing temperature at fixed ratio, and decreasing with increasing ratio at fixed temperature).

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
      "target_policy": "numeric_table",
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
  "notes": "The intermediate equilibrium constants and Si equilibrium results are not directly scored but are required to compute the final α° artifact. The checker will compare α° values against the paper's reference data and verify monotonic trends."
}
```

## How you are scored
A hidden verifier independently examines your output files. For γ_B it recomputes the values using the same quasi-regular solution model and checks that your numbers fall within an acceptable tolerance **and that γ_B decreases monotonically with increasing temperature** (as predicted by the model). For α° it compares your submitted values against the paper's published results and checks that the values satisfy the expected monotonic trends with temperature and H₂/SiHCl₃ ratio. The verifier also checks that α° decreases with increasing temperature and with increasing ratio. Each scored artifact contributes a portion to the final reward. Simply reporting arbitrary numbers without following the thermodynamic workflow will not pass the verification.