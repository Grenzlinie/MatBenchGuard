# Reproduce Critical Concentration Ratio (CCR) Correlation for Solar Thermoelectric Generators

## Problem background
Solar concentrated thermoelectric generators (SCTEGs) use concentrated solar radiation to induce a temperature difference across thermoelectric modules, producing electricity. A critical design constraint is the maximum temperature that the hot side of a module can safely withstand; exceeding this limit damages the material. The critical concentration ratio (CCR) is the highest concentration ratio a given SCTEG can tolerate without violating that limit. The CCR depends on many coupled factors: thermoelectric material properties, module geometry, receiver surface characteristics, site ambient conditions, and thermal and electrical operating settings. A general method to estimate the CCR from these factors would greatly assist in preliminary SCTEG design and optimisation. In this task you will construct such an estimating relationship by performing dimensional analysis, generating a design‑of‑experiments dataset, numerically solving a thermodynamic model, and fitting a power‑law correlation.

## Approach
A steady‑state one‑dimensional thermodynamic model describes the energy flows in a SCTEG through the following equations (symbols: \(T_h\) – hot‑side temperature, \(T_c\) – cold‑side temperature, \(G\) – incident solar flux, \(C\) – concentration ratio; others as defined above).

\[
\begin{aligned}
Q_h &= A_r \bigl( G C \alpha_r - \varepsilon_r \sigma (T_h^4 - T_a^4) - h_h (T_h - T_a) \bigr) \tag{2} \\
Q_h &= S T_h I + K (T_h - T_c) - \tfrac{1}{2} I^2 R \tag{3} \\
S   &= n \alpha \tag{4} \\
K   &= n \lambda G_f \tag{5} \\
R   &= n \rho / G_f \tag{6} \\
Z   &= \frac{\alpha^2}{\rho \lambda} \tag{7} \\
M   &= R_L / R \tag{8} \\
P   &= \frac{[S (T_h - T_c)]^2}{R} \frac{M}{(M+1)^2} \tag{9} \\
I   &= \frac{S (T_h - T_c)}{R (M+1)} \tag{10} \\
Q_c &= Q_h - P \tag{11} \\
Q_c &= h_c A_r (T_c - T_a) \tag{12} \\
A_r &= L^2 \tag{13}
\end{aligned}
\]

At the critical design point the system operates with the maximum allowed hot‑side temperature and the maximum expected solar flux, and the unknown concentration ratio is the critical concentration ratio:

\[
C = \mathrm{CCR},\quad G = G_{\mathrm{max}},\quad T_h = T_{\mathrm{max}} \tag{14-16}
\]

The model therefore involves 13 independent factors: Seebeck coefficient \(\alpha\), electrical resistivity \(\rho\), thermal conductivity \(\lambda\), geometric factor \(G_f\), number of thermocouples \(n\), module side length \(L\), maximum allowed temperature \(T_{\max}\), receiver emissivity \(\varepsilon_r\), receiver absorptivity \(\alpha_r\), ambient temperature \(T_a\), maximum solar flux \(G_{\max}\), hot‑side convection coefficient \(h_h\), cold‑side convection coefficient \(h_c\), and electrical matching load \(M\).

To obtain a compact correlation the Buckingham Pi theorem is applied. Using \(\alpha, \rho, \lambda, G_f\) as repeating variables yields ten dimensionless Pi groups:

\[
\pi_2 = n,\quad \pi_3 = \frac{L}{G_f},\quad \pi_4 = Z T_{\max},\quad \pi_5 = \varepsilon_r,\quad \pi_6 = \alpha_r,\quad \pi_7 = Z T_a,\quad \pi_8 = \frac{Z G_{\max}}{\lambda/G_f},\quad \pi_9 = \frac{h_h}{\lambda/G_f},\quad \pi_{10} = \frac{h_c}{\lambda/G_f},\quad \pi_{11} = M,
\]

with \(\pi_1 = \mathrm{CCR}\).

A power‑law model \(\pi_1 = a \cdot \pi_2^b \cdot \pi_3^c \cdots \pi_{11}^k\) is proposed to relate the groups. The coefficients a, b–k are determined by fitting this model to a dataset built from numerical experiments. For a given set of factor values, the CCR is obtained by solving the system of Eqs. (2)–(13) together with (14–16) for the unknowns \(C\) and \(T_c\); this can be done with a nonlinear root‑finder (e.g., `scipy.optimize.fsolve`). The dataset is created by Latin hypercube sampling (LHS): 500 combinations of the 13 factors are drawn uniformly over the following realistic ranges (same as Table I of the paper): α 200–300 µV/K, ρ 0.5×10⁻³–1.5×10⁻³ Ω cm, λ 0.5×10⁻²–1.5×10⁻² W/cm‑K, Gf 0.04–0.4 cm, n 90–300, L 30–60 mm, Tmax 373–873 K, εr 0.01–0.3, αr 0.7–1.0, Ta 298–323 K, Gmax 300–1000 W/m², hh 5–50 W/m²‑K, hc 500–1500 W/m²‑K, M 0.5–1.5. For each sample the thermodynamic model is solved with the constraints Th = Tmax and G = Gmax to compute the corresponding CCR, giving a full dataset of ten Pi‑group values and the response. Nonlinear regression then fits the power‑law model, producing the correlation coefficient a, exponents b–k, and goodness‑of‑fit statistics (R² and median relative error). The dataset is then standardized (zero mean, unit variance per column) and the model refitted to obtain standardized exponents that indicate the relative sensitivity of the CCR to each Pi group.

## Reproduction target
Produce a correlation model and an associated dataset by completing the workflow steps below. The final correlation must achieve a coefficient of determination R² ≥ 0.95 and a median relative error ≤ 25 % on the 500‑point LHS dataset. Using the fitted coefficients, predict the CCR for 10 hidden test input conditions (provided as /app/inputs/hidden_inputs.csv). Each prediction must have an absolute relative error ≤ 30 % compared with the true CCR computed independently by the verifier. Deliver two scored artifacts: (i) a JSON file containing the fitted coefficient a, exponents b–k, R², median relative error, and standardized exponents; (ii) a CSV file with the predicted CCR for each hidden input.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Latin hypercube sampling of factor ranges
- Role: process
- Action: Generate exactly 500 Latin hypercube samples for the 13 independent factors (alpha, rho, lambda, Gf, n, L, Tmax, epsilon_r, alpha_r, Ta, Gmax, hh, hc, M) using the uniform ranges specified in the paper (Table I). The sampling must cover the multidimensional space uniformly.
- Evidence: `/app/outputs/samples.csv`

### Step 2: Thermodynamic model simulation and Pi-group computation
- Role: process
- Action: For each sample, compute the ten dimensionless Pi groups (pi2 to pi11) as defined using the repeating variables and factor values. Solve the steady-state thermodynamic model (energy balance equations (2)–(16) with constraints Th = Tmax, G = Gmax) to obtain the critical concentration ratio CCR. Save the computed Pi groups and CCR for all samples.
- Evidence: `/app/outputs/dataset.csv`

### Step 3: Correlation fitting and standardized sensitivity analysis
- Role: scored
- Action: Fit the power-law correlation model (pi1 = a * pi2^b * ... * pi11^k) to the dataset using nonlinear regression. Compute coefficient of determination R² and median relative error. Standardize the dataset (zero mean, unit variance per column) and refit to obtain standardized exponents for sensitivity analysis. Write the fitted coefficient a, exponents b–k, R², median relative error, and standardized exponents (all as floats) to correlation_coefficients.json.
- Output file: `/app/outputs/correlation_coefficients.json`
- Format: json
- Contract: Object with keys: coefficient (object with keys a, b, c, d, e, f, g, h, i, j, k, all float), R2 (float), median_relative_error (float), standardized_exponents (object with keys b, c, d, e, f, g, h, i, j, k, all float).
- Scoring: scored by hidden verifier

### Step 4: Predict CCR for hidden test inputs
- Role: scored (load-bearing)
- Action: Read the fitted coefficients from correlation_coefficients.json. Read 10 hidden test input conditions from /app/inputs/hidden_inputs.csv (each row contains the 13 factor values in the same order as Table I). For each, compute the Pi groups, apply the power-law correlation to predict the CCR, and write the results to hidden_predictions.csv with columns input_index (integer 1..10) and CCR_predicted (float).
- Output file: `/app/outputs/hidden_predictions.csv`
- Format: csv
- Contract: Two columns: input_index (int, 1..10), CCR_predicted (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/correlation_coefficients.json`
- `/app/outputs/hidden_predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### correlation_coefficients.json
- path: `/app/outputs/correlation_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted correlation coefficient and exponents, R², median relative error, and standardized exponents for sensitivity analysis. Checked against the paper's reported values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `coefficient`:
      - `a`: float
      - `b`: float
      - `c`: float
      - `d`: float
      - `e`: float
      - `f`: float
      - `g`: float
      - `h`: float
      - `i`: float
      - `j`: float
      - `k`: float
    - `R2`: float
    - `median_relative_error`: float
    - `standardized_exponents`:
      - `b`: float
      - `c`: float
      - `d`: float
      - `e`: float
      - `f`: float
      - `g`: float
      - `h`: float
      - `i`: float
      - `j`: float
      - `k`: float

### hidden_predictions.csv
- path: `/app/outputs/hidden_predictions.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Predicted CCR values for 10 hidden test conditions; each absolute relative error must be ≤ 30% compared to the checker's true values.
- schema:
  - `type`: table
  - `required_columns`: `input_index`, `CCR_predicted`

Notes: All scored outputs are compared against hidden gold values: the correlation coefficients against the paper's reported values (with relative tolerance for exponents, threshold for R² and median error), and the predictions against the checker's own thermodynamic model solutions (error threshold). The process steps (sampling and model solving) are forced by the load-bearing prediction step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "correlation_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "coefficient": {
            "a": "float",
            "b": "float",
            "c": "float",
            "d": "float",
            "e": "float",
            "f": "float",
            "g": "float",
            "h": "float",
            "i": "float",
            "j": "float",
            "k": "float"
          },
          "R2": "float",
          "median_relative_error": "float",
          "standardized_exponents": {
            "b": "float",
            "c": "float",
            "d": "float",
            "e": "float",
            "f": "float",
            "g": "float",
            "h": "float",
            "i": "float",
            "j": "float",
            "k": "float"
          }
        }
      },
      "description": "Fitted correlation coefficient and exponents, R², median relative error, and standardized exponents for sensitivity analysis. Checked against the paper's reported values with tolerances."
    },
    {
      "file": "hidden_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "input_index",
          "CCR_predicted"
        ]
      },
      "description": "Predicted CCR values for 10 hidden test conditions; each absolute relative error must be ≤ 30% compared to the checker's true values."
    }
  ],
  "notes": "All scored outputs are compared against hidden gold values: the correlation coefficients against the paper's reported values (with relative tolerance for exponents, threshold for R² and median error), and the predictions against the checker's own thermodynamic model solutions (error threshold). The process steps (sampling and model solving) are forced by the load-bearing prediction step."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. For Step 3 (correlation_coefficients.json) the verifier compares your reported coefficient a, exponents b–k, R², and median relative error against hidden reference values; the correlation must meet the stated thresholds (R² ≥ 0.95, median relative error ≤ 25 %). The standardized exponents are checked for consistency. For Step 4 (hidden_predictions.csv) the verifier compares each of your 10 predicted CCRs against the true CCR values it computes from its own hidden implementation of the thermodynamic model. Each prediction must have an absolute relative error ≤ 30 %. The two stages are combined into a single reward in [0,1]; meeting or exceeding the required performance yields full credit for each stage. Simply reporting the paper’s numbers is insufficient—the verifier checks the outputs produced by your implemented workflow.
