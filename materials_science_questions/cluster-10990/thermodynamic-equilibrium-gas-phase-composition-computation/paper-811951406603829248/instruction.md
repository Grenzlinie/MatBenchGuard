# Thermodynamic Prediction of Cr₂O₃ Oxidative Vaporization Rate

## Problem background
When Cr₂O₃ is heated in an oxygen-containing environment, it undergoes oxidative vaporization to form CrO₃(g). In the low-pressure regime, where gas-phase mass transport does not limit the reaction, the rate of chromium loss can be predicted solely from equilibrium thermochemical data. Computing this reaction‑controlled rate is essential for understanding the oxidation kinetics of chromium and chromium‑containing alloys at high temperatures. This task implements the thermodynamic description of the Cr₂O₃–O₂ system and computes the predicted chromium mass flux as a function of temperature and oxygen pressure.

## Approach
The equilibrium vapor pressure of CrO₃(g) over Cr₂O₃(s) is given by the thermochemical expression
log₁₀(P_CrO₃/atm) = –1.247×10⁴/T + 3.20 + (3/4) log₁₀(P_O₂/atm),
derived from high‑temperature measurements. Using this expression together with the Hertz–Langmuir equation—which relates the maximum possible vaporization rate to the equilibrium vapor pressure—you can compute the mass flux of chromium atoms leaving the surface. The workflow consists of two parts:

1. **Process step** – Implement the full general rate equation that combines chemical reaction kinetics with boundary‑layer mass transport, and numerically verify that it reduces to the reaction‑controlled expression in the low‑pressure limit and to the diffusion‑controlled expression in the high‑pressure limit. Write a brief evidence file summarizing the verification.

2. **Scored step** – Compute the reaction‑controlled chromium mass flux at a fixed oxygen partial pressure (0.115 Torr, i.e., 1.51×10⁻⁴ atm) for a set of temperatures in the range 1000–1300 °C, and write the results to a CSV file.

## Reproduction target
Produce a CSV file `reaction_controlled_rate.csv` containing the computed chromium mass flux (g cm⁻² s⁻¹) at an oxygen partial pressure P_O₂ = 1.51×10⁻⁴ atm (0.115 Torr) for the temperatures 1273 K, 1373 K, 1473 K, and 1573 K. The file must have columns `temperature_K`, `oxygen_pressure_atm`, and `mass_flux_Cr_g_cm2_s`. Additionally, as a process step, verify that the full general rate equation (combining reaction kinetics and boundary‑layer mass transport) reduces to the reaction‑controlled form at low pressure and to the diffusion‑controlled form at high pressure, and write a short summary to `general_rate_verification.txt`.

## Assets
No external datasets, models, or proprietary tools are required. All necessary thermochemical constants and the vapor‑pressure formula are stated in the workflow description. The agent is expected to use a Python 3 environment with standard scientific libraries (e.g., numpy) for numerical computation.

## Workflow steps

### Step 1: General rate equation and limiting forms
- Role: process
- Action: Implement the full general rate equation that combines chemical reaction kinetics with boundary‑layer mass transport. Write a brief evidence file summarizing the verification that this equation reduces to the reaction‑controlled form in the low‑pressure limit and to the diffusion‑controlled form in the high‑pressure limit.

**General rate equation**

The total chromium mass flux (g cm⁻² s⁻¹) can be approximated by the series‑resistance formula

```
1 / J_total = 1 / J_rxn + 1 / J_diff
```

where
- **J_rxn** is the reaction‑controlled flux given by the Hertz–Langmuir equation:

```
J_rxn = 44.35 * P_CrO3(atm) * M_Cr / ( √(M_CrO3) * √(T) )
```

- **J_diff** is the diffusion‑limited flux across a stagnant boundary layer, described by Bartlett’s boundary‑layer theory:

```
J_diff = ( D * Sh * P_CrO3(atm) * M_Cr ) / ( L * R * T )
```

with

| symbol | meaning | typical units |
|--------|---------|---------------|
| D      | binary diffusion coefficient of CrO₃ in O₂ | cm² s⁻¹ |
| Sh     | Sherwood number | dimensionless |
| L      | characteristic length | cm |
| R      | gas constant | 82.057 cm³ atm mol⁻¹ K⁻¹ |
| T      | absolute temperature | K |

The equilibrium vapor pressure P_CrO3 (atm) is obtained from the thermodynamic expression

```
log10(P_CrO3/atm) = -1.247×10⁴ / T + 3.20 + (3/4) log10(P_O₂/atm)
```

**Constants:**
- M_Cr  = 52.00 g mol⁻¹
- M_CrO3 = 99.99 g mol⁻¹
- R     = 82.057 cm³ atm mol⁻¹ K⁻¹

**Verification of limiting behaviour**

- In the low‑pressure (or large‑diffusion) limit, mass transport is very fast compared to the chemical reaction, i.e. the parameter `D·Sh/L` → ∞. Then J_total → J_rxn.
- In the high‑pressure (or small‑diffusion) limit, the reaction is fast and transport is the bottleneck, i.e. `D·Sh/L` → 0. Then J_total → J_diff.

Write a short text file `general_rate_verification.txt` that reports, for a representative temperature (e.g. 1273 K) and oxygen partial pressure (1.51×10⁻⁴ atm), the values of J_rxn, J_diff, and J_total for two extreme choices of the transport parameter `D·Sh/L` (one very large, one very small), clearly demonstrating the approach to the respective limits. No numerical precision is required; the file should only demonstrate that the general equation behaves as described above.

- Evidence: `/app/outputs/general_rate_verification.txt`

### Step 2: Reaction-controlled oxidative vaporization rate
- Role: scored (load-bearing)
- Action: Using the thermodynamic expression for the equilibrium vapor pressure of CrO₃(g) over Cr₂O₃(s): log10(P_CrO₃/atm) = -1.247e4/T + 3.20 + (3/4) log10(P_O₂/atm), and the Hertz–Langmuir equation: mass_flux_Cr (g cm⁻² s⁻¹) = 44.35 * P_CrO₃(atm) * M_Cr / (M_CrO₃^{1/2} * T^{1/2}), where M_Cr = 52.00 g mol⁻¹ and M_CrO₃ = 99.99 g mol⁻¹, compute the chromium mass flux at oxygen partial pressure P_O₂ = 1.51e-4 atm for the temperatures T = 1273, 1373, 1473, and 1573 K. Write the results to reaction_controlled_rate.csv.
- Output file: `/app/outputs/reaction_controlled_rate.csv`
- Format: csv
- Contract: temperature_K (float), oxygen_pressure_atm (float), mass_flux_Cr_g_cm2_s (float). At least rows for T = 1273, 1373, 1473, 1573 K at P_O₂ = 1.51e-4 atm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reaction_controlled_rate.csv`
- `/app/outputs/general_rate_verification.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reaction_controlled_rate.csv
- path: `/app/outputs/reaction_controlled_rate.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Reaction-controlled chromium mass flux computed from the equilibrium vapor pressure of CrO₃(g) over Cr₂O₃(s) and the Hertz–Langmuir equation.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `oxygen_pressure_atm`, `mass_flux_Cr_g_cm2_s`
  - `units`:
    - `temperature_K`: K
    - `oxygen_pressure_atm`: atm
    - `mass_flux_Cr_g_cm2_s`: g cm^-2 s^-1

### general_rate_verification.txt
- path: `/app/outputs/general_rate_verification.txt`
- format: text
- purpose: process (evidence)
- target_policy: passthrough
- description: Evidence file demonstrating that the general rate equation reduces to the reaction‑controlled limit and to the diffusion‑controlled limit.
- schema: {}

Notes: The checker will read the CSV, recompute the expected mass flux from the given temperature and oxygen pressure using the same thermodynamic formula and constants, and verify that the agent's reported mass_flux is within a relative tolerance for each row. The verification text file is not numerically scored, but its absence may result in a penalty.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reaction_controlled_rate.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "oxygen_pressure_atm",
          "mass_flux_Cr_g_cm2_s"
        ],
        "units": {
          "temperature_K": "K",
          "oxygen_pressure_atm": "atm",
          "mass_flux_Cr_g_cm2_s": "g cm^-2 s^-1"
        }
      },
      "description": "Reaction-controlled chromium mass flux computed from the equilibrium vapor pressure of CrO₃(g) over Cr₂O₃(s) and the Hertz–Langmuir equation."
    },
    {
      "file": "general_rate_verification.txt",
      "format": "text",
      "purpose": "process",
      "target_policy": "passthrough",
      "schema": {},
      "description": "Evidence file showing verification that the general rate equation reduces to reaction-controlled and diffusion-controlled limits."
    }
  ],
  "notes": "The checker will read the CSV, recompute the expected mass flux from the given temperature and oxygen pressure using the same thermodynamic formula and constants, and verify that the agent's reported mass_flux is within a relative tolerance for each row."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage’s artifact. The primary scored artifact is `reaction_controlled_rate.csv`. For every row, the verifier recomputes the expected mass flux from the same thermodynamic formula and constants using the temperature and oxygen pressure you provide in that row, and compares your reported `mass_flux_Cr_g_cm2_s` against the recomputed value. The check passes for a row if the relative difference falls within a tight tolerance. Your overall reward is a weighted combination of the scores across all required rows. Simply writing the correct final numbers without a consistent computation is insufficient—the verifier recomputes from your submitted data, so your numbers must be self‑consistent with the given expressions. The process‑step evidence file (`general_rate_verification.txt`) is not directly scored, but its absence may result in a penalty.