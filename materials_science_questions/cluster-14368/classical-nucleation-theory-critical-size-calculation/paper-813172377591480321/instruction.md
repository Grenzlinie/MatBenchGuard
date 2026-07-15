# Comparison of Ion-Induced Nucleation Theories

## Problem background
Ion-induced nucleation influences many atmospheric phenomena and technological processes. Two classical thermodynamic frameworks coexist: nucleation **on** ions, where a single ion sits at the center of a growing cluster, and nucleation **in the presence of** ions, where the ion can be located anywhere relative to the cluster. Published measurements of critical supersaturations for six organic vapors (tetrachloromethane, trichloromethane, o-xylene, methanol, ethanol, water) at a fixed ion concentration allow a direct comparison. This task determines, through computational reproduction, which of the two theories better predicts the experimentally observed critical supersaturations.

## Approach
Two independent theoretical models are implemented and compared. The equations below are the core mathematical definitions; all symbols are standard and defined in the text.

**Common notation**
- μ_old − μ_new = kT ln S, where S = P / P_eq is the supersaturation.
- v: molecular volume in the new phase.
- σ: surface tension.
- ε_old, ε_new: dielectric permittivities of old and new phases.
- Z e: ion charge; ε_0: vacuum permittivity.
- R_ion: ion radius (if needed, can be set to a small constant or derived from ion associate).
- T: temperature, k: Boltzmann constant.
- n: ion concentration (5.5×10^5 cm⁻³ for the experimental data).
- N_1 = S P_eq / (k T): number density of single molecules.
- j = α S P_eq / sqrt(2π m k T): molecular flux, α condensation coeff ≈ 1.
- R_0 = 2 σ v / (k T ln S): critical radius of homogeneous nucleation.

### 1. Nucleation on ions (central‑ion model)
The work of formation of a spherical cluster with the ion at its centre (radius R ≥ R_ion) is:

$$
W(R) = -(\mu_{\text {old }}-\mu_{\text {new}}) \frac{4 \pi}{3 v}\left(R^{3}-R_{\text {ion }}^{3}\right)+4 \pi \sigma\left(R^{2}-R_{\text {ion }}^{2}\right) 
-\frac{(Z e)^{2}}{8 \pi \varepsilon_{0}}\left(\varepsilon_{\text {old }}^{-1}-\varepsilon_{\text {new }}^{-1}\right)\left(R_{\text {ion }}^{-1}-R^{-1}\right). \tag{1}
$$

Setting dW/dR = 0 gives the equation for the stationary points R_min and R_max:

$$
(\mu_{\text{old}} - \mu_{\text{new}}) R^{4} - 2\sigma v R^{3} + \frac{(Ze)^{2} v}{32\pi^{2} \varepsilon_{0}} \big(\varepsilon_{\text{old}}^{-1} - \varepsilon_{\text{new}}^{-1}\big) = 0. \tag{2}
$$

This quartic has two positive real roots R_min and R_max (R_min < R_max) when ε_new > ε_old (vapor–liquid). The work barrier W* = W(R_max) − W(R_min) can be expressed as

$$
W^{*} = \frac{4\pi\sigma}{3} \big(R_{\text{max}}^{2} - R_{\text{min}}^{2}\big) - \frac{(Ze)^{2}}{6\pi\varepsilon_{0}} \big(\varepsilon_{\text{old}}^{-1} - \varepsilon_{\text{new}}^{-1}\big) \big(R_{\text{min}}^{-1} - R_{\text{max}}^{-1}\big). \tag{3}
$$

The nucleation rate (ions per cm³ per second) is

$$
J = \frac{n j A}{3 N_{\text{nuc}}} \sqrt{ \frac{4\pi\sigma R_{\text{max}}^{2} - \frac{(Ze)^{2}}{4\pi\varepsilon_{0} R_{\text{max}}} (\varepsilon_{\text{old}}^{-1} - \varepsilon_{\text{new}}^{-1})}{\pi kT} } \exp\left( -\frac{W^{*}}{kT} \right), \tag{4}
$$

where
- N_nuc = (4π/3v)(R_max³ − R_ion³),
- A = 4π (R_max + (3v/(4π))^{1/3})².

For a given S, solve Eq. (2) → R_min, R_max, compute W* from (3), then J from (4). The critical supersaturation S_cr^on is the value of S that yields J = 1 s⁻¹ cm⁻³.

### 2. Nucleation in the presence of ions (variable‑ion‑position model)
When the ion can move relative to the centre of the cluster, the work of formation depends on the cluster radius R and the ion–cluster centre distance r. Introduce dimensionless variables with respect to R_0:
- y = R / R_0,  z = r / R_0,  u = R_ion / R_0.
- E_s = 4π σ R_0²,
- p = (Z e)² / (32 π² ε_0 σ R_0³) (ε_old⁻¹ − ε_new⁻¹),
- q_0 = W_add / E_s.

The ion is modelled as a stable ion associate of radius R_min (the minimum of Eq. 1), so u = R_min / R_0 and the ion–molecule binding energy is set to zero (E_i-m = 0). In that case W_add takes the form:

$$
W_{\text{add}} = \frac{4\pi}{3v} (\mu_{\text{old}} - \mu_{\text{new}}) R_{\text{min}}^3 - 4\pi\sigma R_{\text{min}}^2 - \frac{(Ze)^2}{8\pi\varepsilon_0 R_{\text{min}}} \left( \varepsilon_{\text{old}}^{-1} - \varepsilon_{\text{new}}^{-1} \right). \tag{5}
$$

The formation work in three regions is given by:

- **Ion outside** (z > y + u):
$$
W_{\text{out}} = E_{\text{s}} \left[ -\frac{2}{3} y^{3}+y^{2}-\frac{p}{y} \sum_{l=0}^{\infty} \frac{\varepsilon_{\text {new}} l}{\varepsilon_{\text {new}} l+\varepsilon_{\text {old}}(l+1)}\left(\frac{y}{z}\right)^{2(l+1)} \right]. \tag{6}
$$

- **Ion inside** (z < y − u):
$$
W_{\text{in}} = E_{\text{s}} \left[ -\frac{2}{3} y^{3}+y^{2}+\frac{p}{y} \sum_{l=0}^{\infty} \frac{\varepsilon_{\text {old }}(l+1)}{\varepsilon_{\text {new }} l+\varepsilon_{\text {old }}(l+1)}\left(\frac{z}{y}\right)^{2 l}+q_{0} \right]. \tag{7}
$$

- **Ion on the boundary** (y − u ≤ z ≤ y + u):
A cubic polynomial interpolation ensures continuity of W and its y-derivative:
$$
W_{\text {inter }}=a_{0}+a_{1} y+a_{2} y^{2}+a_{3} y^{3}, \tag{8}
$$
where the coefficients are determined by matching W_in and W_out at y = z + u and y = z − u:
$$
\begin{aligned}
a_{3}=& \frac{1}{4 u^{2}}\left(\left.\partial W_{\text {in }} / \partial y\right|_{y=z+u}+\left.\partial W_{\text {out }} / \partial y\right|_{y=z-u}\right. \\
&\left.+\left.\frac{1}{u} W_{\text {out }}\right|_{y=z-u}-\left.\frac{1}{u} W_{\text {in }}\right|_{y=z+u}\right), \\
a_{2}=&\frac{1}{4 u}\left(\left.\partial W_{\text {in }} / \partial y\right|_{y=z+u}-\left.\partial W_{\text {out }} / \partial y\right|_{y=z-u}\right)-3 z a_{3}, \\
a_{1}=&\left.\partial W_{\text {out }} / \partial y\right|_{y=z-u}-2(z-u) a_{2}-3(z-u)^{2} a_{3}, \\
a_{0}=&\left.W_{\text {out }}\right|_{y=z-u}-(z-u) a_{1}-(z-u)^{2} a_{2}-(z-u)^{3} a_{3}.
\end{aligned}
$$

The nucleation rate is a double integral over cluster size y and ion position z:

$$
J = N_{1} n v R_{0}^{2} j \int_{0}^{z_{\max }}\left(\int_{\delta}^{\infty} \exp \left(\frac{W(y, z)}{k T}\right) d y\right)^{-1} 4 \pi z^{2} d z, \tag{9}
$$
with z_max = (1/R_0)(3/(4π n))^{1/3}, δ = (1/R_0)(3v/(4π))^{1/3}.

For each compound and temperature, compute R_min and R_0 from the current trial S, evaluate the integrals in (9) numerically (e.g., using the saddle‑point method), then adjust S until J = 1 s⁻¹ cm⁻³. That S is S_cr^pres.

Both theories require publicly available thermodynamic parameters (surface tension, vapour pressure, molar volume, dielectric constants, molecular mass, condensation coefficient) and the experimental critical supersaturations reported in the literature (Rabeony & Mirabel, 1987). The final step compares the predicted S_cr values with the experimental ones by computing absolute relative percent errors.

## Reproduction target
Compute, for every combination of compound and temperature listed in the published measurement set, the critical supersaturations predicted by the nucleation‑on‑ions and nucleation‑in‑the‑presence‑of‑ions theories. Combine these with the experimental critical supersaturations from Rabeony & Mirabel (1987) and calculate the absolute relative percent error for each theory. Write the result as a CSV table with columns: compound, temperature_K, S_cr_experimental, S_cr_on, S_cr_pres, error_on_percent, error_pres_percent. The table must cover all six compounds at all temperatures for which experimental data exist.

## Assets

- Experimental critical supersaturation data from Rabeony & Mirabel (1987): https://doi.org/10.1021/j100292a042
- Thermodynamic parameters for six organic vapors

## Workflow steps

### Step 1: Prepare input data
- Role: process
- Action: Obtain experimental critical supersaturations for six vapors (tetrachloromethane, trichloromethane, o-xylene, methanol, ethanol, water) from Rabeony & Mirabel (1987, doi:10.1021/j100292a042) at the temperatures listed in the paper's comparison table. Gather thermodynamic parameters (surface tension, vapor pressure, molar volume, dielectric constants, molecular mass, condensation coefficient) for each compound from standard references (NIST Chemistry WebBook or physical chemistry handbooks). Write the combined data to a CSV file.
- Evidence: `/app/outputs/input_parameters.csv`

### Step 2: Calculate nucleation-on-ions predictions
- Role: process
- Action: For each compound and temperature, solve the equation for R_min and R_max, compute the work of formation W* and nucleation rate J from the central-ion rate formula, then iteratively find the supersaturation S that gives J = 1 s⁻¹ cm⁻³ (S_cr^on). Write intermediate results.
- Evidence: `/app/outputs/on_ions_intermediate.csv`

### Step 3: Calculate nucleation-in-presence-of-ions predictions
- Role: process
- Action: Using the stable ion associate assumption (E_i-m=0, u=R_min/R_0), evaluate the formation work W(y,z) from the regional expressions with cubic polynomial interpolation for the ion-on-boundary case, then compute the nucleation rate integral via saddle-point/numerical integration. Solve for S such that J = 1 s⁻¹ cm⁻³ (S_cr^pres) for each compound and temperature. Write intermediate results.
- Evidence: `/app/outputs/pres_ions_intermediate.csv`

### Step 4: Compute final error table
- Role: scored (load-bearing)
- Action: Combine the computed S_cr_on and S_cr_pres with the experimental S_cr values, calculate the absolute relative percentage errors, and write the final comparison table.
- Output file: `/app/outputs/critical_supersaturation_and_errors.csv`
- Format: csv
- Contract: CSV with columns: compound (str), temperature_K (float), S_cr_experimental (float), S_cr_on (float), S_cr_pres (float), error_on_percent (float), error_pres_percent (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_supersaturation_and_errors.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_supersaturation_and_errors.csv
- path: `/app/outputs/critical_supersaturation_and_errors.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of predicted critical supersaturations by the 'on ions' and 'in presence of ions' theories, experimental values, and absolute relative percent errors for each compound and temperature.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `temperature_K`, `S_cr_experimental`, `S_cr_on`, `S_cr_pres`, `error_on_percent`, `error_pres_percent`

Notes: The checker compares the agent's reported S_cr_on, S_cr_pres, error_on_percent, and error_pres_percent against hidden reference values from the paper's table using appropriate tolerances. Homogeneous nucleation predictions are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_supersaturation_and_errors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "temperature_K",
          "S_cr_experimental",
          "S_cr_on",
          "S_cr_pres",
          "error_on_percent",
          "error_pres_percent"
        ]
      },
      "description": "Table of predicted critical supersaturations by the 'on ions' and 'in presence of ions' theories, experimental values, and absolute relative percent errors for each compound and temperature."
    }
  ],
  "notes": "The checker compares the agent's reported S_cr_on, S_cr_pres, error_on_percent, and error_pres_percent against hidden reference values from the paper's table using appropriate tolerances. Homogeneous nucleation predictions are not required."
}
```

## How you are scored
A hidden verifier receives your submitted CSV file. It independently compares the predicted S_cr values and error percentages against reference values using appropriate tolerances. The final reward is a weighted combination of the accuracies across all entries; producing the correct numerical results earns full credit, while deviations reduce the score. Merely reporting the paper’s published numbers is not sufficient—the verifier expects your own computed values to agree with the hidden reference within the specified tolerances.
