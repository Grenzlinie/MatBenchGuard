# Step velocity curves for impurity adsorption models in crystal growth

## Problem background
During solution-grown crystal growth, impurities can adsorb at growth steps and reduce the advance velocity. Several models describe this effect. Sears proposed a qualitative model in which step velocity remains insensitive to impurity coverage until a critical "monostep coverage" is reached, after which velocity drops sharply. Two quantitative models were later derived: the Albon-Dunning model computes step velocity from the probability of finding free step lengths, while the Cabrera-Vermilyea model considers step pinning by impurities on ledges ahead of the step. The aim is to evaluate whether the Albon-Dunning and Cabrera-Vermilyea models can produce a plateau-like velocity curve consistent with the Sears picture.

## Approach
We compute step velocity versus impurity coverage directly from the published formulas. For the Albon-Dunning model, the step velocity V as a function of adsorbed step coverage c (number per molecular spacing) is given by V = V₀ * (d - (1-c)*d + (1-c)) * (1-c)^d, where V₀ = 5.8×10⁻⁷ m/s is the pure-solution velocity and d is the critical nucleus diameter in molecular spacings. For the Cabrera-Vermilyea model, we use three expressions relating V to the ledge impurity density x (number per molecular spacing²): a squeezing-only formula V = V₀ * √(1 - d·√x); a surface-flux-reduction formula V = V₀·(1 - x); and a combined formula V = V₀·(1 - x)·√(1 - d·√x). Velocities are computed on fine grids of c and x for several values of d. The resulting curves are then analyzed to assess whether any exhibits a plateau region—a range of non-zero impurity coverage over which the step velocity remains constant at V₀.

## Reproduction target
Compute the steady-state step velocity V as a function of impurity coverage for the Albon-Dunning model (c from 0 to 1, d = 2, 6, 10) and for the Cabrera-Vermilyea models (x from 0 to 1, d = 2, 5, 10, using the squeezing-only, flux-reduction, and combined expressions). Output the computed curves as CSV files. Examine the resulting V vs. coverage curves and produce a one‑line text file stating whether any curve exhibits a plateau region where velocity remains constant at the pure-solution value V₀ over a range of non‑zero coverage. The task assesses the structural consistency of these quantitative models with the Sears qualitative picture.

## Assets
This task requires no external datasets, models, or pre‑trained weights. All necessary formulas, physical constants (V₀ = 5.8×10⁻⁷ m/s), and the values of d are provided in this instruction. Standard Python scientific packages (e.g., numpy, pandas) may be used for the calculations and file writing.

## Workflow steps

### Step 1: Compute Albon-Dunning step velocity curves
- Role: scored (load-bearing)
- Action: Implement the Albon-Dunning step velocity formula: V = V0 * (d - (1-c)*d + (1-c)) * (1-c)^d. Use a pure-solution step velocity V0 = 5.8e-7 m/s. Compute the step velocity V as a function of adsorbed step coverage c for c ranging from 0.0 to 1.0 in steps of 0.01, for three critical nucleus diameters: d = 2, 6, and 10 molecular spacings. Write the results to a CSV file with columns c, V_d2, V_d6, V_d10.
- Output file: `/app/outputs/step_01_albon_dunning_curve.csv`
- Format: csv
- Contract: Columns: c (float, coverage number per molecular spacing), V_d2 (float, m/s), V_d6 (float, m/s), V_d10 (float, m/s). Rows for c from 0.0 to 1.0 in increments of 0.01.
- Scoring: scored by hidden verifier

### Step 2: Compute Cabrera-Vermilyea step velocity curves
- Role: scored (load-bearing)
- Action: Implement the three Cabrera-Vermilyea step velocity formulas: squeezing-only V = V0 * sqrt(1 - d * sqrt(x)), surface-flux-reduction V = V0 * (1 - x), and combined V = V0 * (1 - x) * sqrt(1 - d * sqrt(x)). Use V0 = 5.8e-7 m/s. Compute V as a function of ledge adsorbate density x for x from 0.0 to 1.0 in steps of 0.001, for d = 2, 5, 10 (for the squeezing-only formula) and d = 2, 5, 10 for the other two formulas (as per the paper's analysis). If the term inside a square root becomes negative, output 0.0 for that velocity. Write a CSV file with columns x, V_squeezing_d2, V_squeezing_d5, V_squeezing_d10, V_flux_d2, V_flux_d5, V_flux_d10, V_combined_d2, V_combined_d5, V_combined_d10.
- Output file: `/app/outputs/step_02_cabrera_vermilyea_curve.csv`
- Format: csv
- Contract: Columns: x (float, impurity density per molecular spacing^2), V_squeezing_d2 (m/s), V_squeezing_d5 (m/s), V_squeezing_d10 (m/s), V_flux_d2 (m/s), V_flux_d5 (m/s), V_flux_d10 (m/s), V_combined_d2 (m/s), V_combined_d5 (m/s), V_combined_d10 (m/s). Rows for x from 0.0 to 1.0 in 0.001 steps. When the argument to sqrt becomes negative, the corresponding V value must be 0.0.
- Scoring: scored by hidden verifier

### Step 3: Conclude on absence of plateau
- Role: scored
- Action: Examine the computed velocity-coverage curves from the preceding two steps. Assess whether any of the curves exhibits a plateau region (a range of non-zero coverage over which the step velocity remains constant at its pure-solution value V0, or any other constant non-zero value). Write a one-line ASCII text file stating explicitly whether a plateau is observed. 
- Output file: `/app/outputs/step_03_conclusion.txt`
- Format: txt
- Contract: Exactly one line of ASCII text, e.g., 'No plateau region observed in any of the calculated curves.' or equivalent.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_albon_dunning_curve.csv`
- `/app/outputs/step_02_cabrera_vermilyea_curve.csv`
- `/app/outputs/step_03_conclusion.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_albon_dunning_curve.csv
- path: `/app/outputs/step_01_albon_dunning_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Velocity vs. coverage curves for Albon-Dunning model, d=2,6,10.

### step_02_cabrera_vermilyea_curve.csv
- path: `/app/outputs/step_02_cabrera_vermilyea_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Velocity vs. coverage curves for Cabrera-Vermilyea models (squeezing-only, flux-reduction, combined).

### step_03_conclusion.txt
- path: `/app/outputs/step_03_conclusion.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: One-line conclusion about plateau presence.

Notes: All outputs are scored by a hidden verifier that recomputes the curves and checks the plateau conclusion.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_albon_dunning_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {},
      "description": "Velocity vs. coverage curves for Albon-Dunning model, d=2,6,10."
    },
    {
      "file": "step_02_cabrera_vermilyea_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {},
      "description": "Velocity vs. coverage curves for Cabrera-Vermilyea models (squeezing-only, flux-reduction, combined)."
    },
    {
      "file": "step_03_conclusion.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {},
      "description": "One-line conclusion about plateau presence."
    }
  ],
  "notes": "All outputs are scored by a hidden verifier that recomputes the curves and checks the plateau conclusion."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage. For the CSV outputs, the verifier recomputes the expected velocity values from the same formulas and parameters, comparing the submitted numbers within a tight numerical tolerance. For the conclusion text, the verifier inspects whether the statement correctly reflects the computed data. The final reward is a weighted combination of these stage scores; simply reporting textbook or expected numbers is not sufficient—the actual computed values in your output files are what is checked.
