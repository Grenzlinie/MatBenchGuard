# Thermal expansion model for cast iron

## Problem background
Cast iron's thermal expansion is complex because graphite dissolves upon heating, changing the volume fraction of the composite and causing lattice expansion of the surrounding austenite matrix. Traditional models that treat cast iron as a simple composite often fail to capture the measured expansion behavior, particularly at high temperatures and under different thermal histories. The reproduced work proposes a thermomechanical model that accounts for graphite dissolution, the resulting volume changes, and plastic deformation of the matrix, predicting the overall thermal expansion coefficient α as a function of temperature. Reproducing this model and computing α for two scenarios—with and without plastic deformation—provides insight into the dominant mechanisms and serves as a critical input for thermal fatigue analyses of cast iron components such as brake drums.

## Model description

### Variant B – no plastic deformation (matrix behaves as if graphite were pores)
For this variant the thermal expansion is taken as that of the iron matrix alone, ignoring the additional volume change caused by graphite dissolution. The matrix expansion includes the intrinsic thermal expansion and, at high temperature in austenite, a chemical expansion due to carbon uptake.

- **Low temperature** (≤ 727 °C): the matrix is pearlitic steel. Use the thermal expansion of pearlitic steel,
  $$ \alpha_B = \alpha_{\text{Fe}} = 12.0\times 10^{-6}\,\text{K}^{-1}. $$
- **High temperature** (> 727 °C): the matrix is austenite. The austenite expansion coefficient is given by
  $$ \alpha_{\gamma} = \alpha_{\gamma}^T + \alpha_{\gamma}^C \quad\text{(Eq. 1)} $$
  where
  $$ \alpha_{\gamma}^T = 20.0\times 10^{-6}\,\text{K}^{-1} $$
  is the intrinsic thermal expansion of austenite, and
  $$ \alpha_{\gamma}^C = \frac{\delta\varepsilon_\gamma}{\delta C}\,\frac{\mathrm{d}C}{\mathrm{d}T} $$
  accounts for the lattice expansion caused by carbon dissolution.
  $$ \frac{\delta\varepsilon_\gamma}{\delta C} = 9.24\times 10^{-3}\;\text{per wt\% C} $$
  is the lattice expansion per unit carbon content. The derivative \(\mathrm{d}C/\mathrm{d}T\) is obtained from the Fe–C equilibrium solubility (see below). Thus for \(T > 727\,^\circ\text{C}\),
  $$ \alpha_B = \alpha_{\gamma}^T + \frac{\delta\varepsilon_\gamma}{\delta C}\,\frac{\mathrm{d}C}{\mathrm{d}T}. $$

### Variant C – with plastic deformation
When plastic deformation is allowed, the composite expansion includes the volume change due to graphite dissolution, as well as the thermal expansions of the individual phases weighted by their volume fractions. The overall coefficient is given by

$$
\alpha = \frac{\mathrm{d}f_{\mathrm{gr}}}{\mathrm{d}T}\frac{(\rho_{\mathrm{gr}}-\rho_{\mathrm{Fe}})}{3\rho}
       + \alpha_{\mathrm{gr}}\frac{\rho_{\mathrm{gr}}}{\rho}f_{\mathrm{gr}}
       + \alpha_{\mathrm{Fe}}\frac{\rho_{\mathrm{Fe}}}{\rho}f_{\mathrm{Fe}}
       \quad\text{(Eq. 2)}
$$

$$
\rho = f_{\mathrm{gr}}\,\rho_{\mathrm{gr}} + f_{\mathrm{Fe}}\,\rho_{\mathrm{Fe}}
       \quad\text{(Eq. 3)}
$$

The volume fractions \(f_{\mathrm{gr}}\) and \(f_{\mathrm{Fe}}=1-f_{\mathrm{gr}}\) as well as the derivative \(\mathrm{d}f_{\mathrm{gr}}/\mathrm{d}T\) are determined from the Fe–C phase diagram and the alloy composition. The necessary constants are:

| Symbol | Value | Description |
|--------|-------|-------------|
| \(\rho_{\mathrm{gr}}\) | 2.25 g cm⁻³ | Density of graphite |
| \(\rho_{\mathrm{Fe}}\) | 7.87 g cm⁻³ | Density of iron |
| \(\alpha_{\mathrm{gr}}\) | 1.0×10⁻⁶ K⁻¹ | Thermal expansion coefficient of graphite |
| \(\alpha_{\mathrm{Fe}}\) | 12.0×10⁻⁶ K⁻¹ | Thermal expansion coefficient of iron (pearlitic steel) |
| \(\rho\) | – | Composite density, calculated from Eq. (3) |

### Fe–C equilibrium and graphite volume fraction
The alloy is a grey cast iron with total carbon content \(C_{\text{tot}} = 3.08\) wt%. The equilibrium solubility of carbon in austenite (wt%) is modelled by

$$
C_{\gamma}(T_K) =
\begin{cases}
0, & T_K \le 1000.15\ \text{K}\;(727\,^\circ\text{C}) \\[4pt]
23.1\;\exp\!\left(-\dfrac{3400}{T_K}\right), & T_K > 1000.15\ \text{K}
\end{cases}
$$

where \(T_K = T(^\circ\text{C}) + 273.15\) is the absolute temperature in kelvin.

At any temperature the mass fraction of graphite (assuming all non‑dissolved carbon is present as graphite) is

$$
m_{\mathrm{gr}} = \begin{cases}
\dfrac{C_{\text{tot}} - C_{\gamma}}{100 - C_{\gamma}}, & C_{\gamma} < C_{\text{tot}} \\[6pt]
0, & C_{\gamma} \ge C_{\text{tot}}
\end{cases}
$$

and the volume fraction of graphite is

$$
f_{\mathrm{gr}} = \frac{m_{\mathrm{gr}}/\rho_{\mathrm{gr}}}{m_{\mathrm{gr}}/\rho_{\mathrm{gr}} + (1-m_{\mathrm{gr}})/\rho_{\mathrm{Fe}}}.
$$

The derivative \(\mathrm{d}f_{\mathrm{gr}}/\mathrm{d}T\) is computed by evaluating \(f_{\mathrm{gr}}\) at \(T_K+1\) and \(T_K-1\) and applying a central difference:

$$
\frac{\mathrm{d}f_{\mathrm{gr}}}{\mathrm{d}T}(T_K) \approx \frac{f_{\mathrm{gr}}(T_K+1) - f_{\mathrm{gr}}(T_K-1)}{2\ \text{K}}.
$$

The derivative \(\mathrm{d}C/\mathrm{d}T\) required for variant B is obtained from the analytical derivative of the solubility function:

$$
\frac{\mathrm{d}C_{\gamma}}{\mathrm{d}T} = 23.1 \times \frac{3400}{T_K^{2}}\, \exp\!\left(-\frac{3400}{T_K}\right) \quad (\text{wt\% K}^{-1}).
$$

## Reproduction target
Compute the thermal expansion coefficient α (in units of \(10^{-6}\,\text{K}^{-1}\)) of the cast iron defined above at temperatures from 200 °C to 900 °C in 50 °C steps. Use the formulas presented to generate curves for variant B (no plastic deformation) and variant C (with plastic deformation). Produce a CSV file with three columns: `temperature_C` (temperature in degrees Celsius, integer), `alpha_B` (variant B, float), `alpha_C` (variant C, float). The target is to capture the characteristic temperature dependence governed by graphite dissolution, lattice expansion, and matrix plasticity.

## Workflow steps

### Step 1: Compute thermal expansion model
- Role: scored (load-bearing)
- Action: Implement the thermal expansion model described above. For each temperature:
  1. Obtain \(C_{\gamma}\), \(f_{\mathrm{gr}}\), \(\mathrm{d}f_{\mathrm{gr}}/\mathrm{d}T\), \(\mathrm{d}C_{\gamma}/\mathrm{d}T\) from the provided solubility and alloy composition.
  2. Compute \(\alpha_B\) using the matrix‑only rule (Eq. 1 with the pearlitic steel expansion at low temperature; use \(\alpha_{\gamma}^T = 20.0\!\times\!10^{-6}\,\text{K}^{-1}\) and \(\delta\varepsilon_\gamma/\delta C = 9.24\!\times\!10^{-3}\) per wt% C).
  3. Compute \(\alpha_C\) using Eqs. (2) and (3).
  4. Write the results to a CSV file with columns `temperature_C`, `alpha_B`, `alpha_C`.
- Output file: `/app/outputs/step_01_thermal_expansion.csv`
- Format: csv
- Contract: `temperature_C` (integer), `alpha_B` (float, unit: \(10^{-6}\) K⁻¹), `alpha_C` (float, unit: \(10^{-6}\) K⁻¹)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_thermal_expansion.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_thermal_expansion.csv
- path: `/app/outputs/step_01_thermal_expansion.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed thermal expansion coefficient of cast iron for two model variants as a function of temperature.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `alpha_B`, `alpha_C`
  - `description`: temperature_C: temperature in degrees Celsius (integer); alpha_B: thermal expansion coefficient without plastic deformation (10^-6 /K, float); alpha_C: thermal expansion coefficient with plastic deformation (10^-6 /K, float).

Notes: The model uses the Fe–C phase diagram data, lattice expansion coefficients, and standard physical constants provided in the model description. The checker will recompute a metric from this artifact and compare against hidden reference values digitized from the paper's figures.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, and CSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_thermal_expansion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_C",
          "alpha_B",
          "alpha_C"
        ],
        "description": "temperature_C: temperature in degrees Celsius (integer); alpha_B: thermal expansion coefficient without plastic deformation (10^-6 /K, float); alpha_C: thermal expansion coefficient with plastic deformation (10^-6 /K, float)."
      },
      "description": "Computed thermal expansion coefficient of cast iron for two model variants as a function of temperature."
    }
  ],
  "notes": "The model uses publicly available Fe–C phase diagram data, lattice expansion coefficients, and standard physical constants. The checker will recompute a metric from this artifact and compare against hidden reference values digitized from the paper's figures."
}
```

## How you are scored
Each required output file is independently checked by a hidden verifier. For the thermal expansion table, the verifier will compare your computed `alpha_B` and `alpha_C` values against reference values derived from the experimental measurements reported in the original study. The comparison uses a deviation metric across all temperature points; a higher reward is earned when the predicted curves closely match the reference values. Your reward is the weighted combination of all stage scores, so producing accurate curves that follow the expected temperature trend is essential. The exact scoring formula and tolerances are not disclosed.