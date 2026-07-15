# Thermodynamic modeling of a nonstoichiometric L1₀ intermetallic phase using antistructure defect model

## Problem background
Nonstoichiometric intermetallic phases with the L1₀ structure exhibit thermodynamic properties that are strongly influenced by constitutional lattice disorder. At nonstoichiometric compositions, atoms occupy wrong sublattice sites, and the resulting defect concentrations affect activities, partial enthalpies, and integral Gibbs energies. The antistructure defect model for L1₀ phases describes these composition-dependent properties in terms of a stoichiometric disorder parameter and a ratio of second‑ to first‑neighbor interaction enthalpies. This task reproduces the thermodynamic analysis of a specific L1₀ phase at elevated temperature by fitting the model to experimental Zn activity data and computing derived integral thermodynamic quantities.

## Approach

The thermodynamic properties of nonstoichiometric L1₀ phases are described by an antistructure defect model. The model expresses the activities and partial molar enthalpies as functions of composition, the stoichiometric disorder parameter α, and the interaction enthalpy ratio η.

### Model equations

The activity of component i (Zn: i=2, Pt: i=1) relative to its stoichiometric value is:

$$\ln \frac{a_i}{a_{i,0}} = \varepsilon_i \ln \frac{z(1-2\alpha)}{\alpha(1-2z)} \;+\; \frac{\frac12 \eta}{1 - \frac12 \eta} \, (2\ln 2\alpha) \, (2\varepsilon_i + \chi)\,\chi$$

where

- $\chi \equiv x_{\mathrm{Zn}} - 0.5$ (deviation from stoichiometry, $-0.5 \le \chi \le 0.5$),
- $\varepsilon_i = +1/2$ for Pt (component 1) and $-1/2$ for Zn (component 2),
- $z$ is the composition‑dependent disorder parameter, computed from $\chi$ and $\alpha$:

$$z = \frac{-\chi + \sqrt{\chi^2 + 4\alpha^2}}{2},$$

- $\alpha$ is the disorder parameter at stoichiometry ($\chi=0$),
- $\eta = V_{\mathrm{AB}}'/V_{\mathrm{AB}}$ is the ratio of second‑ to first‑neighbor interchange enthalpies,
- $a_{i,0}$ is the activity of component $i$ at the stoichiometric composition ($x_{\mathrm{Zn}} = 0.5$). $a_{\mathrm{Zn},0}$ is a fitting parameter; $a_{\mathrm{Pt},0}$ is determined self‑consistently such that $\ln a_{\mathrm{Pt},0} \approx \ln a_{\mathrm{Zn},0}$.

The partial molar enthalpy of component $i$ (relative to its value at stoichiometry) follows:

$$\frac{\Delta\bar H_i - \Delta\bar H_{i,0}}{RT} = \left[ 2\alpha + \frac{\varepsilon_i \chi - 4\alpha^2}{2z+\chi} \;+\; \frac{\frac12 \eta}{1 - \frac12 \eta}\, 2 (2\varepsilon_i + \chi)\chi \right] \ln 2\alpha.$$

At the stoichiometric composition we take $\Delta\bar H_{\mathrm{Pt},0} = \Delta\bar H_{\mathrm{Zn},0} \equiv \Delta H(0)$ (the formation enthalpy per g‑atom of the equiatomic compound).

Integral thermodynamic quantities are

$$\Delta G = RT \bigl( x_{\mathrm{Pt}} \ln a_{\mathrm{Pt}} + x_{\mathrm{Zn}} \ln a_{\mathrm{Zn}} \bigr), \qquad
\Delta H = x_{\mathrm{Pt}} \Delta\bar H_{\mathrm{Pt}} + x_{\mathrm{Zn}} \Delta\bar H_{\mathrm{Zn}}, \qquad
T\Delta S = \Delta H - \Delta G.$$

### Estimation of the stoichiometric enthalpy $\Delta H(0)$ (Kubaschewski method)

The stoichiometric Gibbs energy for the Zn(l) standard state is
$\Delta G^{l}(0) = RT \ln a_{\mathrm{Zn},0}$ (using the fitted $\ln a_{\mathrm{Zn},0}$).

Convert to the Zn(s) standard state using the Gibbs energy of fusion of fcc‑Zn:
$\Delta G^{\mathrm{s}}(0) = \Delta G^{l}(0) + \Delta G_{\mathrm{fus}}$, with
$\Delta G_{\mathrm{fus}} = 4.3\ \mathrm{kJ/g\text{-}atom}$ (Kaufman–Bernstein value used in the paper).

The excess entropy of formation is taken as
$\Delta S^{\mathrm{xs}} = -15.8\ \mathrm{J/(K\,g\text{-}atom)}$
(result of the Kubaschewski empirical correlation based on the boiling points of Pt ($4100\,^\circ\mathrm{C}$, i.e. $4373\ \mathrm{K}$) and Zn ($907\,^\circ\mathrm{C}$, i.e. $1180\ \mathrm{K}$)).

The enthalpies of formation for the two standard states are then:

$$\Delta H^{\mathrm{s}}(0) = \Delta G^{\mathrm{s}}(0) + T \Delta S^{\mathrm{xs}}, \qquad
\Delta H^{l}(0) = \Delta G^{l}(0) + T \Delta S^{\mathrm{xs}},$$

with $T = 1273\ \mathrm{K}$.

The workflow proceeds in three stages:
1. **Model fitting**: Implement the activity equation for the phase and perform a least‑squares fit to the provided experimental Zn activity data (composition vs. ln a_Zn). This yields the best‑fit values of α, η, and ln a_Zn,0.
2. **Thermodynamic property calculation**: Using the fitted parameters, compute ln a_Zn and ln a_Pt at the required compositions (45, 48, 49, 50, 51, 52 a/o Zn) from the model equations. Compute ΔG, ΔH, and TΔS using the equations given above. The stoichiometric enthalpy ΔH(0) is obtained via the Kubaschewski method detailed above. With the assumption ΔH_Pt,0 = ΔH_Zn,0 = ΔH(0), use the partial molar enthalpy equation to compute ΔH̄_i(x) and then the integral ΔH and TΔS.
3. **ΔH–α relationship**: From the fitted α and the stoichiometric enthalpy ΔH referred to solid elements (Zn(s), Pt(s)), evaluate the theoretical relation ΔH/(RT) = ln 2 + ln α to obtain a single (phase, α, ΔH) point.

## Reproduction target
Using the provided experimental Zn activity data (composition and ln a_Zn for the β₁ phase at 1273 K), fit the antistructure defect model and produce the best‑fit parameters α, η, and ln a_Zn,0. From the fitted model, compute the thermodynamic activities ln a_Zn and ln a_Pt, and the integral properties ΔG, ΔH, and TΔS at compositions 45, 48, 49, 50, 51, and 52 a/o Zn. Finally, derive the point for this phase on the ΔH–α correlation curve using the relation ΔH/(RT) = ln 2 + ln α with ΔH referred to the solid elements.

## Assets

- β₁-PtZn experimental Zn activity data at 1273K
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Fit thermodynamic model to Zn activity data
- Role: scored (load-bearing)
- Action: Implement the activity equation for nonstoichiometric L1₀ phases with parameters α (disorder parameter), η (interaction enthalpy ratio), and ln a_Zn,0 (stoichiometric activity). Using the provided experimental Zn activity data (composition vs. ln a_Zn), perform a least-squares fit to determine the best-fit values. Write the fitted parameters to a JSON file.
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: {"alpha": float, "eta": float, "ln_a_Zn_0": float}
- Scoring: scored by hidden verifier

### Step 2: Compute thermodynamic properties of β₁-PtZn
- Role: scored
- Action: Using the fitted model parameters and the thermodynamic equations for activities and partial molar enthalpies, compute the activities and integral thermodynamic properties for β₁-PtZn at 1273K. Compute ln a_Zn (from the model) and ln a_Pt (using the equation for component Pt) at compositions 45, 48, 49, 50, 51, 52 a/o Zn. Compute ΔG = RT (x_Pt ln a_Pt + x_Zn ln a_Zn) with R=8.314 J/mol·K, T=1273K. Estimate the stoichiometric enthalpy of formation ΔH(0) using the Kubaschewski empirical entropy method: estimate the standard entropy of formation ΔS° from the boiling points of Pt (4100°C) and Zn (907°C) and the empirical relation; then obtain ΔH(0) for Zn(l) and Zn(s) standard states. Assuming ΔH_Pt,0 = ΔH_Zn,0 = ΔH(0) at stoichiometry, compute the partial molar enthalpies and derive integral ΔH and TΔS. Output a CSV table with the required columns.
- Output file: `/app/outputs/thermodynamic_table_beta1.csv`
- Format: csv
- Contract: Columns: a/o_Zn, ln_a_Zn, ln_a_Pt, Delta_G_kJ_per_g_atom, Delta_H_kJ_per_g_atom, T_Delta_S_kJ_per_g_atom; rows for compositions 45, 48, 49, 50, 51, 52 a/o Zn.
- Scoring: scored by hidden verifier

### Step 3: Verify ΔH-α relationship for β₁-PtZn
- Role: scored
- Action: Using the fitted α and the stoichiometric enthalpy ΔH (referred to solid elements Zn(s) and Pt(s)), compute the point for β₁-PtZn from the derived theoretical relation ΔH/(RT) = ln 2 + ln α. Output a CSV with columns phase, alpha, Delta_H_kJ_per_g_atom. Include at least the PtZn row.
- Output file: `/app/outputs/delta_H_alpha_relation.csv`
- Format: csv
- Contract: Columns: phase, alpha, Delta_H_kJ_per_g_atom. One row for PtZn from the current fit.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.json`
- `/app/outputs/thermodynamic_table_beta1.csv`
- `/app/outputs/delta_H_alpha_relation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted model parameters (disorder parameter, interaction enthalpy ratio, stoichiometric Zn activity).
- schema:
  - `type`: object
  - `required`:
    - `alpha`: float
    - `eta`: float
    - `ln_a_Zn_0`: float

### thermodynamic_table_beta1.csv
- path: `/app/outputs/thermodynamic_table_beta1.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Thermodynamic activity and integral property table for β₁-PtZn at selected compositions.
- schema:
  - `type`: table
  - `required_columns`: `a/o_Zn`, `ln_a_Zn`, `ln_a_Pt`, `Delta_G_kJ_per_g_atom`, `Delta_H_kJ_per_g_atom`, `T_Delta_S_kJ_per_g_atom`
  - `units`:
    - `Delta_G_kJ_per_g_atom`: kJ/g-atom
    - `Delta_H_kJ_per_g_atom`: kJ/g-atom
    - `T_Delta_S_kJ_per_g_atom`: kJ/g-atom

### delta_H_alpha_relation.csv
- path: `/app/outputs/delta_H_alpha_relation.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Point for PtZn on the ΔH-α correlation plot derived from the theoretical relation.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `alpha`, `Delta_H_kJ_per_g_atom`

Notes: All output files are scored against the paper's reported values within hidden tolerances. The fitted parameters are the primary reproduction target; the thermodynamic table and ΔH-α point provide additional validation of the model and derived relationships.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha": "float",
          "eta": "float",
          "ln_a_Zn_0": "float"
        }
      },
      "description": "Fitted model parameters (disorder parameter, interaction enthalpy ratio, stoichiometric Zn activity)."
    },
    {
      "file": "thermodynamic_table_beta1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "a/o_Zn",
          "ln_a_Zn",
          "ln_a_Pt",
          "Delta_G_kJ_per_g_atom",
          "Delta_H_kJ_per_g_atom",
          "T_Delta_S_kJ_per_g_atom"
        ],
        "units": {
          "Delta_G_kJ_per_g_atom": "kJ/g-atom",
          "Delta_H_kJ_per_g_atom": "kJ/g-atom",
          "T_Delta_S_kJ_per_g_atom": "kJ/g-atom"
        }
      },
      "description": "Thermodynamic activity and integral property table for β₁-PtZn at selected compositions."
    },
    {
      "file": "delta_H_alpha_relation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "alpha",
          "Delta_H_kJ_per_g_atom"
        ]
      },
      "description": "Point for PtZn on the ΔH-α correlation plot derived from the theoretical relation."
    }
  ],
  "notes": "All output files are scored against the paper's reported values within hidden tolerances. The fitted parameters are the primary reproduction target; the thermodynamic table and ΔH-α point provide additional validation of the model and derived relationships."
}
```

## How you are scored
Each of the three workflow steps produces one file that is checked independently by a hidden verifier. The verifier compares your computed values against reference values (derived from the published results of the work) using tolerances appropriate for computational reproduction, and also checks internal consistency (e.g., the ΔG at stoichiometry must equal RT ln a_Zn,0). The final reward is a weighted sum of the scores from the fitted parameters, the thermodynamic table, and the ΔH‑α point. Simply reporting a number without genuine fitting or correct thermodynamic derivation will not pass; the verifier expects values that result from a correct re‑implementation of the described methods.
