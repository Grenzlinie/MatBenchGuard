# Velocity-coefficient threshold and worst-case reduction in gamma radiometry

## Problem background
In gamma radiometry nondestructive testing, a collimated radiation beam passes through a moving object onto a stationary scintillation counter, whose output is integrated with an RC time constant τ. Detection of a flaw (a cylindrical aperture or a rectangular groove) relies on the relative increase in recorded pulses [ΔN/N]max. This increase depends on kinetic factors: the velocity v of the object, the beam radius R, the integrator time constant τ, and the flaw dimensions (aperture radius r or groove width a). The paper derives analytic expressions that capture how these parameters combine into a dimensionless coefficient of velocity (2R/(vτ)) and a coefficient of dimension (r/R for apertures, a/(2R) for grooves). The task is to study, by numerical evaluation of those expressions, at what coefficient of velocity further changes no longer meaningfully affect [ΔN/N]max, and how much the relative pulse increase at that threshold is reduced compared to the ideal stationary case.

## Approach
Implement the analytic formulas for the maximal relative pulse increase $[\Delta N/N]_{\max}$ for two geometries: cylindrical apertures and rectangular grooves. The formulas are expressed in terms of a dimensionless coefficient of velocity $k = 2R/(v\tau)$ and a coefficient of dimension $d$ ($r/R$ for apertures, $a/(2R)$ for grooves). Fixed physical parameters $R=1$, $v=1$, $\mu=0.05$, $x=0.1$, $F=\pi R^2=\pi$ are used. The stationary limit ($v\to 0$, $k\to\infty$) defines a baseline.

### Cylindrical aperture
For $d = r/R \le 1$, the maximum relative increase follows from Eq. 4 with
$t_1 = 2r/v$, $t_2 = 2R/v$ and the constant $\alpha$ fixed by the stationary limit:
\[
[\Delta N/N]_{\max} = (e^{\mu x} - 1) \frac{v r}{2 R^2}
\Bigl[ \frac{2r}{v} + \frac{2R}{v} - \tau \ln\!\bigl( e^{2R/(v\tau)} + e^{2r/(v\tau)} - 1 \bigr) \Bigr].
\]
The stationary limit ($v\to 0$) is $[\Delta N/N]_{\max}^{v=0} = (e^{\mu x} - 1) d^2$.
Introducing $k = 2R/(v\tau)$ and $d = r/R$, the ratio becomes
\[
R_{\text{ratio}} = \frac{1}{d}\Bigl[ 1 + d - \frac{1}{k} \ln\!\bigl( e^{k} + e^{d k} - 1 \bigr) \Bigr].
\]
This expression reproduces the paper’s reported worst‑case reduction
$\approx 0.85$ at $k=4$, $d=1$.

### Rectangular groove
Let $d = a/(2R)$. The maximum and entry-area fractions are
\[
\frac{f_m}{F} = \frac{2}{\pi}\Bigl(d\sqrt{1-d^2} + \arcsin d\Bigr), \qquad
\frac{f_a}{F} = \frac{1}{\pi}\Bigl(\arcsin(2d-1) + (2d-1)\sqrt{1-(2d-1)^2} + \frac{\pi}{2}\Bigr).
\]
With $k = 2R/(v\tau)$, the maximal relative increase is
\[
[\Delta N/N]_{\max} = \frac{e^{\mu x} - 1}{F}\,
\frac{f_a}{F}
\biggl[1 + \frac{1}{d} + \frac{1}{d\,k}\,
\ln\!\Bigl(e^{k(1+d)} + \frac{f_m}{f_a}\,d\,k + e^{(f_m/f_a)\,d\,k} - 1\Bigr)\biggr].
\]
Stationary limit: $[\Delta N/N]_{\max}^{v=0} = (e^{\mu x} - 1)\,f_m/F$.  
$R_{\text{ratio}} = \dfrac{[\Delta N/N]_{\max}}{[\Delta N/N]_{\max}^{v=0}}$.

### Grid and analysis
Compute the grid for cylindrical apertures (the aperture case is simpler and sufficient for the threshold analysis). Use a fine grid of $k$ from 0.1 to 10 and $d$ from {0.1, 0.2, 0.5, 0.75, 1.0}. For each $(k,d)$ compute $[\Delta N/N]_{\max}$ and $R_{\text{ratio}}$. Write to CSV. Then identify the smallest $k$ beyond which the maximum relative change in $[\Delta N/N]_{\max}$ for all larger $k$ is less than 1% of the value at that $k$ – this is the threshold velocity coefficient. At that threshold, find the minimum $R_{\text{ratio}}$ across all $d$ and record it as the worst-case reduction.

## Reproduction target
Produce a CSV file (computed_results.csv) containing the computed grid: for each (coefficient_of_velocity, coefficient_of_dimension) pair, report the δN/N max and the ratio to the stationary case. Then, using that grid, determine the velocity coefficient threshold — the value beyond which the influence on δN/N max effectively vanishes — and the worst‑case reduction: the minimum ratio_v_to_v0 among all dimension coefficients at that threshold. Write the threshold and the worst‑case reduction (as a ratio) to threshold_and_worstcase.txt. Both outputs must be placed in /app/outputs. The task is self‑contained; you do not need to retrieve the source paper.

## Assets

- Python 3: python3
- NumPy: numpy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Compute grid of maximal relative pulse increase and velocity ratio
- Role: scored (load-bearing)
- Action: Implement the analytic formulas for the maximal relative pulse increase (ΔN/N)max for a cylindrical aperture (d≤1) and a rectangular groove geometry, expressed as functions of the dimensionless coefficient of velocity k = 2R/(vτ) and the coefficient of dimension d (r/R for apertures, a/(2R) for grooves). Use a fine grid of k from 0.1 to 10 and d taken from the set {0.1, 0.2, 0.5, 0.75, 1.0}. For each combination compute (ΔN/N)max and the ratio R_ratio = (ΔN/N)max(v) / (ΔN/N)max(v=0). Write the results to a CSV file with columns: coefficient_of_velocity, coefficient_of_dimension, delta_N_N_max, ratio_v_to_v0. Ensure the grid is fine enough to reliably locate the threshold and capture the worst‑case reduction (expected at d=1).
- Output file: `/app/outputs/computed_results.csv`
- Format: csv
- Contract: Columns: coefficient_of_velocity (float, 2R/(vτ)), coefficient_of_dimension (float, r/R or a/(2R)), delta_N_N_max (float, the computed maximal relative increase), ratio_v_to_v0 (float, ratio of delta_N_N_max at finite velocity to that at v=0). One row per unique (coefficient_of_velocity, coefficient_of_dimension) combination.
- Scoring: scored by hidden verifier

### Step 2: Determine velocity-coefficient threshold and worst-case reduction from the grid
- Role: scored
- Action: Read the computed grid (computed_results.csv). Identify the velocity coefficient threshold beyond which the influence on (ΔN/N)max effectively vanishes (i.e., the point where further increases produce only marginal changes). At that threshold, find the minimum ratio_v_to_v0 across all dimension coefficients and record its value and the corresponding dimension coefficient. Write the findings to a text file: first line 'threshold = <value>' and second line 'worst_case_reduction = <value>' (the ratio at the worst case).
- Output file: `/app/outputs/threshold_and_worstcase.txt`
- Format: txt
- Contract: Two lines: first line starts with 'threshold = ' followed by the numerical value (float); second line starts with 'worst_case_reduction = ' followed by the numerical value (float, ratio). No extra text.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.csv`
- `/app/outputs/threshold_and_worstcase.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.csv
- path: `/app/outputs/computed_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Grid of computed (ΔN/N)max and ratio values for a range of velocity and dimension coefficients (d≤1). The checker will recompute each row using the same analytic formulas and fixed underlying parameters, comparing within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `coefficient_of_velocity`, `coefficient_of_dimension`, `delta_N_N_max`, `ratio_v_to_v0`
  - `units`:
    - `coefficient_of_velocity`: dimensionless
    - `coefficient_of_dimension`: dimensionless
    - `delta_N_N_max`: dimensionless
    - `ratio_v_to_v0`: dimensionless

### threshold_and_worstcase.txt
- path: `/app/outputs/threshold_and_worstcase.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Text file containing the empirically determined velocity coefficient threshold and the worst‑case reduction ratio derived from the grid data.
- schema:
  - `type`: text
  - `description`: Two lines: threshold = <float>, worst_case_reduction = <float>. The checker will parse these values and compare against the expected threshold and reduction within a tolerance.

Notes: The task reproduces the kinetic factor analysis from the paper. The cylindrical aperture formula has been corrected to include the logarithmic term and restricted to d≤1, avoiding the singularity at d=1. The rectangular groove formula remains as given.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "coefficient_of_velocity",
          "coefficient_of_dimension",
          "delta_N_N_max",
          "ratio_v_to_v0"
        ],
        "units": {
          "coefficient_of_velocity": "dimensionless",
          "coefficient_of_dimension": "dimensionless",
          "delta_N_N_max": "dimensionless",
          "ratio_v_to_v0": "dimensionless"
        }
      },
      "description": "Grid of computed (ΔN/N)max and ratio values for a range of velocity and dimension coefficients (d≤1). The checker will recompute each row using the same analytic formulas and fixed underlying parameters, comparing within a tolerance."
    },
    {
      "file": "threshold_and_worstcase.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Two lines: threshold = <float>, worst_case_reduction = <float>. The checker will parse these values and compare against the expected threshold and reduction within a tolerance."
      },
      "description": "Text file containing the empirically determined velocity coefficient threshold and the worst‑case reduction ratio derived from the grid data."
    }
  ],
  "notes": "The task reproduces the kinetic factor analysis from the paper. The cylindrical aperture formula has been corrected to include the logarithmic term and restricted to d≤1, avoiding the singularity at d=1. The rectangular groove formula remains as given."
}
```

## How you are scored
A hidden verifier independently checks each stage's output. For computed_results.csv, the verifier recomputes the δN/N max and ratio for every row using the same analytic formulas and fixed parameters, comparing within a numerical tolerance. For threshold_and_worstcase.txt, the verifier reads the submitted threshold and worst‑case reduction and compares them to the expected values (derived from the paper's physical data) within a tolerance. Your final reward is a weighted combination of the scores from both stages. Simply reporting a number without running the computation will not suffice — the verifier recomputes the grid from scratch.
