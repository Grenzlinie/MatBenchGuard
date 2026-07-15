# Analytical steady-state thermoelectric generator performance evaluation

## Problem background
Thermoelectric generators (TEGs) convert waste heat into electricity via the Seebeck effect. Their efficiency is limited by material properties and geometric design. This work investigates a novel asymmetrical and segmented TEG: the p-type leg has a uniform flat-plate cross-section, while the n-type leg has an exponentially varying area \(A(x)=A_a e^{-a x/L}\), controlled by a geometric parameter \(a\). Both legs are segmented with two different thermoelectric materials—material‑1 on the hot side and material‑2 on the cold side—to improve performance over a wide temperature range. The goal is to quantify how the geometric parameter \(a\), temperature ratio \(\theta = T_{\text{low}}/T_{\text{high}}\), and load resistance ratio \(R_L/R_0\) influence the device’s efficiency, output power, output current, and work ratios.

## Approach
The analysis uses a steady-state analytical model with temperature-dependent material properties. The n‑leg cross‑sectional area follows \(A(x) = \frac{a A_0}{1-e^{-a}} e^{-a x/L}\) with constant total volume. Applying Fourier’s law yields effective thermal conductances \(k_{n,\text{eff}}\) and \(k_{p,\text{eff}}\) for the n‑ and p‑legs, respectively, which depend on the segment lengths (dimensionless ratios \(\mu_n, \mu_p\)) and material conductivities. Effective Seebeck coefficients are defined as

\(\alpha_{p,\text{eff}} = \alpha_{p,1}\frac{k_{p,\text{eff}}}{k_{p,1}}\mu_p + \alpha_{p,2}\frac{k_{p,\text{eff}}}{k_{p,2}}(1-\mu_p)\)

\(\alpha_{n,\text{eff}} = \alpha_{n,1}\frac{k_{n,\text{eff}}}{k_{n,1}}\frac{(1-e^{-a})(e^{a\mu_n}-1)}{a^2} + \alpha_{n,2}\frac{k_{n,\text{eff}}}{k_{n,2}}\frac{(1-e^{-a})(e^{a}-e^{a\mu_n})}{a^2}\)

The electrical resistances of the n‑ and p‑legs are similarly obtained by integrating \(1/(\sigma A)\):

\(R_n = \frac{(1-e^{-a})L}{a^2 A_o}\left[\frac{e^{a\mu_n}-1}{\sigma_{n,1}} + \frac{e^{a}-e^{a\mu_n}}{\sigma_{n,2}}\right],\qquad R_p = \frac{1}{A_p}\left(\frac{L_{p,1}}{\sigma_{p,1}} + \frac{L_{p,2}}{\sigma_{p,2}}\right)\)

The total electrical resistance is \(R_{\text{TEG}} = R_p + R_n\). Reference values \(K_0\) and \(R_0\) are computed from material‑1 n‑type properties at 273 K with \(A_0 = 16\ \text{mm}^2\) and \(L = 4\ \text{mm}\). The overall effective thermal conductance is \(K_{\text{eff}} = \frac{k_{n,\text{eff}} A_n}{L} + \frac{k_{p,\text{eff}} A_p}{L}\).

The average figure of merit is \(ZT_{\text{avg}} = \frac{\alpha_{\text{eff}}^2 T_{\text{high}}(1+\theta)}{2 R_{\text{TEG}} K_{\text{eff}}}\) with \(\alpha_{\text{eff}} = \alpha_{p,\text{eff}} - \alpha_{n,\text{eff}}\).

Device efficiency (η) is given by

\(\eta = \frac{2 Z T_{\text{avg}}(1-\theta)(R_L/R_0)(R_{\text{TEG}}/R_0)}{2 (\alpha_{\text{eff},1}/\alpha_{\text{eff}}) (R_{\text{TEG}}/R_0 + R_L/R_0) (R_{\text{TEG}}/R_0) + (1+\theta) (R_{\text{TEG}}/R_0 + R_L/R_0)^2 - 2 Z T_{\text{avg}}(1-\theta) + (R_{\text{TEG}}/R_0) ( (R_{n,1}+R_{p,1})/R_0 ) }\)

where \(\alpha_{\text{eff},1}\) uses only material‑1 properties. Output power \(W = I^2 R_L\) is expressed in dimensionless form as

\(\frac{W}{K_0 T_{\text{low}}} = \frac{2 Z T_{\text{avg}}(1-\theta)^2 (K_{\text{eff}}/K_0)(R_{\text{TEG}}/R_0)(R_L/R_0)}{\theta (1+\theta) (R_{\text{TEG}}/R_0 + R_L/R_0)^2}\)

with \(I = \alpha_{\text{eff}}(T_{\text{high}}-T_{\text{low}})/(R_{\text{TEG}}+R_L)\). The work ratios compare the power of unsegmented material‑1 and material‑2 legs to the maximum power of the segmented device:

\(\xi_1 = \frac{W_1}{W_{\max}},\qquad \xi_2 = \frac{W_2}{W_{\max}}\)

where \(W_1\) is the power when both legs are made of material‑1, \(W_2\) when both are made of material‑2, and \(W_{\max}\) is the maximum power of the segmented configuration.

The temperature-dependent properties for the four semiconductor types are:

**n‑type material‑1**
- κ = 0.6586 + (329.63/T) + (22145/T²)
- α = 173.26 – 3.8229 T + 0.011679 T² – 1.5584e‑5 T³ + 7.6695e‑9 T⁴
- σ = 1462 – 10.419 T + 0.031315 T² – 4.029e‑5 T³ + 1.9034e‑8 T⁴

**p‑type material‑1**
- κ = 0.56959 + (550.66/T) – (47483/T²)
- α = 1450 – 10.36 T + 0.03123 T² – 4.038e‑5 T³ + 1.903e‑8 T⁴
- σ = 179.02 + 12.336 T – 0.042167 T² + 5.129e‑5 T³ – 2.1435e‑8 T⁴

**n‑type material‑2**
- κ = –4.6205 + 9.9277e‑3 T + (833.7/T) + (235636/T²)
- α = 443.49 – 4.5121 T + 9.4424e‑3 T² – 5.8362e‑6 T³
- σ = –2139.4 + 2.5778 T + exp(12.795 – 0.89098 ln(T))

**p‑type material‑2**
- κ = –1.8067 + 5.729e‑3 T – (64.639/T) + (1.3395e5/T²)
- α = –188.2 + 2.2411 T – 3.0075e‑3 T² + 2.4914e‑7 T³
- σ = –473.1 + 0.86507 T + exp(16.637 – 1.6942 ln(T))

All units: T in K, κ in W/m·K, α in V/K (absolute values; appropriate signs for n‑/p‑type must be used), σ in S/m. The model assumes equal leg lengths L = 4 mm, \(A_p = A_0 = 16\ \text{mm}^2\), and equal segment length ratios \(\mu_p = \mu_n = 0.5\). The cold-side temperature is fixed at 300 K; the hot-side temperature is determined from the chosen temperature ratio \(\theta\).

## Reproduction target
Implement the analytical model described above using any open‑source computing environment (e.g., Python with numpy). Then, for every combination of the geometric parameter \(a \in \{-3.0, -2.5, -2.0, \dots, 2.5, 3.0\}\) (step 0.5), temperature ratio \(\theta \in \{0.45, 0.55\}\), and load resistance ratio \(R_L/R_0 \in \{2, 4, 6, 8\}\), compute and save the following quantities as CSV files:

1. **Efficiency**: \(\eta\) (in %). File `efficiency_vs_a.csv` — columns: `theta`, `RL_R0`, `a`, `efficiency_percent`.
2. **Output power**: \(W\) (in W). File `power_vs_a.csv` — columns: `theta`, `RL_R0`, `a`, `power_W`.
3. **Output current**: \(I\) (in A). File `current_vs_a.csv` — columns: `theta`, `RL_R0`, `a`, `current_A`.
4. **Work ratios**: \(\xi_1\) and \(\xi_2\) (dimensionless). File `work_ratio_vs_a.csv` — columns: `theta`, `RL_R0`, `a`, `xi1`, `xi2`.

All output files must be written to `/app/outputs` and must contain every requested combination of the parameters (no missing rows).

## Assets
- Python 3 with standard scientific libraries (`numpy`, optionally `scipy`). Install as needed using the Tsinghua PyPI mirror.
- No external datasets or pre‑trained models are required; all material property correlations are embedded in the approach section.

## Workflow steps

### Step 1: Material property and reference constants setup
- Role: process
- Action: Implement temperature-dependent functions for thermal conductivity, Seebeck coefficient, and electrical conductivity for the four semiconductor types (n-type material-1, p-type material-1, n-type material-2, p-type material-2) using the polynomial and exponential correlations given in the paper's Table 1. Compute reference thermal conductance K₀ and electrical resistance R₀ from material-1 properties at 273 K using geometric parameters A₀ = 16 mm² and L = 4 mm. Save these implementations in a reusable module (e.g., material_properties.py) to be imported by later steps.
- Evidence: `/app/outputs/material_properties.py`

### Step 2: Compute efficiency sweep
- Role: scored (load-bearing)
- Action: Using the material properties from step_01, evaluate the analytically derived efficiency (η) for every combination of geometric parameter a from -3.0 to 3.0 in steps of 0.5, temperature ratio θ in {0.45, 0.55}, and load resistance ratio R_L/R₀ in {2, 4, 6, 8}. Write the results as a CSV file.
- Output file: `/app/outputs/efficiency_vs_a.csv`
- Format: csv
- Contract: CSV with columns: theta (float), RL_R0 (int), a (float), efficiency_percent (float)
- Scoring: scored by hidden verifier

### Step 3: Compute output power sweep
- Role: scored (load-bearing)
- Action: Using the material properties from step_01, evaluate the analytically derived output power (W) for the same grid of a, θ, and R_L/R₀. Write the results as a CSV file.
- Output file: `/app/outputs/power_vs_a.csv`
- Format: csv
- Contract: CSV with columns: theta (float), RL_R0 (int), a (float), power_W (float)
- Scoring: scored by hidden verifier

### Step 4: Compute output current sweep
- Role: scored (load-bearing)
- Action: Using the material properties from step_01, evaluate the analytically derived output current (I) for the same grid of a, θ, and R_L/R₀. Write the results as a CSV file.
- Output file: `/app/outputs/current_vs_a.csv`
- Format: csv
- Contract: CSV with columns: theta (float), RL_R0 (int), a (float), current_A (float)
- Scoring: scored by hidden verifier

### Step 5: Compute work ratios sweep
- Role: scored (load-bearing)
- Action: Using the material properties from step_01, evaluate the analytically derived work ratios ξ₁ (material-1) and ξ₂ (material-2) for the same grid of a, θ, and R_L/R₀. Write the results as a CSV file.
- Output file: `/app/outputs/work_ratio_vs_a.csv`
- Format: csv
- Contract: CSV with columns: theta (float), RL_R0 (int), a (float), xi1 (float), xi2 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/efficiency_vs_a.csv`
- `/app/outputs/power_vs_a.csv`
- `/app/outputs/current_vs_a.csv`
- `/app/outputs/work_ratio_vs_a.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### efficiency_vs_a.csv
- path: `/app/outputs/efficiency_vs_a.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Device efficiency for every combination of temperature ratio, load resistance ratio, and geometric parameter.
- schema:
  - `type`: table
  - `required_columns`: `theta`, `RL_R0`, `a`, `efficiency_percent`
  - `units`:
    - `theta`: dimensionless
    - `RL_R0`: dimensionless
    - `a`: dimensionless
    - `efficiency_percent`: percent

### power_vs_a.csv
- path: `/app/outputs/power_vs_a.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Output power for every combination of temperature ratio, load resistance ratio, and geometric parameter.
- schema:
  - `type`: table
  - `required_columns`: `theta`, `RL_R0`, `a`, `power_W`
  - `units`:
    - `theta`: dimensionless
    - `RL_R0`: dimensionless
    - `a`: dimensionless
    - `power_W`: W

### current_vs_a.csv
- path: `/app/outputs/current_vs_a.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Output current for every combination of temperature ratio, load resistance ratio, and geometric parameter.
- schema:
  - `type`: table
  - `required_columns`: `theta`, `RL_R0`, `a`, `current_A`
  - `units`:
    - `theta`: dimensionless
    - `RL_R0`: dimensionless
    - `a`: dimensionless
    - `current_A`: A

### work_ratio_vs_a.csv
- path: `/app/outputs/work_ratio_vs_a.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Work ratios for material-1 and material-2 over the parameter grid; checked for trend consistency (peak location, sign, monotonicity).
- schema:
  - `type`: table
  - `required_columns`: `theta`, `RL_R0`, `a`, `xi1`, `xi2`
  - `units`:
    - `theta`: dimensionless
    - `RL_R0`: dimensionless
    - `a`: dimensionless
    - `xi1`: dimensionless
    - `xi2`: dimensionless

Notes: The analytical model uses temperature-dependent material properties from Table 1 of the paper. No external datasets are required. The solver must implement the closed-form expressions for effective Seebeck coefficients, resistances, thermal conductance, and efficiency/power/current/work ratios as derived in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "efficiency_vs_a.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta",
          "RL_R0",
          "a",
          "efficiency_percent"
        ],
        "units": {
          "theta": "dimensionless",
          "RL_R0": "dimensionless",
          "a": "dimensionless",
          "efficiency_percent": "percent"
        }
      },
      "description": "Device efficiency for every combination of temperature ratio, load resistance ratio, and geometric parameter."
    },
    {
      "file": "power_vs_a.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta",
          "RL_R0",
          "a",
          "power_W"
        ],
        "units": {
          "theta": "dimensionless",
          "RL_R0": "dimensionless",
          "a": "dimensionless",
          "power_W": "W"
        }
      },
      "description": "Output power for every combination of temperature ratio, load resistance ratio, and geometric parameter."
    },
    {
      "file": "current_vs_a.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta",
          "RL_R0",
          "a",
          "current_A"
        ],
        "units": {
          "theta": "dimensionless",
          "RL_R0": "dimensionless",
          "a": "dimensionless",
          "current_A": "A"
        }
      },
      "description": "Output current for every combination of temperature ratio, load resistance ratio, and geometric parameter."
    },
    {
      "file": "work_ratio_vs_a.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta",
          "RL_R0",
          "a",
          "xi1",
          "xi2"
        ],
        "units": {
          "theta": "dimensionless",
          "RL_R0": "dimensionless",
          "a": "dimensionless",
          "xi1": "dimensionless",
          "xi2": "dimensionless"
        }
      },
      "description": "Work ratios for material-1 and material-2 over the parameter grid; checked for trend consistency (peak location, sign, monotonicity)."
    }
  ],
  "notes": "The analytical model uses temperature-dependent material properties from Table 1 of the paper. No external datasets are required. The solver must implement the closed-form expressions for effective Seebeck coefficients, resistances, thermal conductance, and efficiency/power/current/work ratios as derived in the paper."
}
```

## How you are scored
Your output CSV files will be checked by a hidden automated verifier. The verifier reads your files and extracts the values at a set of pre‑defined hidden parameter points. It compares your efficiency and power/current values against reference results digitised from the original paper’s figures, using appropriate relative tolerances. The work ratio file is checked for trend consistency: the verifier examines whether the reported \(\xi_1\) and \(\xi_2\) exhibit the correct peak location, sign, and monotonic behaviour across the parameter sweep. The final reward is the fraction of checked points that meet the criteria. Simply reporting numbers that match the published curves is not enough; your code must correctly compute them from the model and material properties.
