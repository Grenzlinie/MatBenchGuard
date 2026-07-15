# Finite Vacancy Concentration Effect on Tracer Diffusion Correlation Factor in FCC Crystals

## Problem background
In vacancy‑mediated tracer diffusion, the correlation factor f measures how non‑random successive jumps of a tracer atom are. At very low vacancy concentrations (the infinite‑dilution limit), f is conventionally calculated assuming the vacancy escapes and the correlated jump sequence is infinite. At finite vacancy concentrations, the correlated sequence is truncated because a different vacancy may exchange with the tracer before the original vacancy departs, potentially shifting f towards unity. This computational reproduction task investigates the magnitude of this effect for the face‑centred cubic (f.c.c.) lattice. The goal is to compute the correlation factor using a rigorous finite‑n formula and to determine how much it deviates from the infinite‑dilution value at a range of vacancy concentrations.

## Approach
The reproduction follows the random‑walk matrix method. A 91×91 jump probability matrix for the f.c.c. lattice (sphere size 90, containing 2731 sites) is constructed from the nearest‑neighbour jump frequencies and the site numbering in the crystal. The initial vacancy distribution w(0) places the vacancy at the site it occupies immediately after the first tracer‑vacancy exchange. For each integer n, the finite‑sum W(n) = w(0)·(I + A + A² + … + Aⁿ) is computed, where A is the jump probability matrix, and the probabilities W(0)…W(4) for the nearest neighbouring sites of the tracer are extracted. From these, the average cosine t₁(n) is calculated.  
For a given vacancy concentration C_v, the correlation duration n_c (the mean number of vacancy jumps before the vacancy escapes its associated sphere) is estimated as n_c ≈ 0.33·C_v^{-2/3}. The t₁ value to be used in the correlation factor is taken as t₁(n_c). The finite‑n correlation factor f is evaluated via a rigorous formula that depends on t₁ and n_c. The infinite‑dilution limit f_∞ is obtained from the converged t₁ at large n. The percentage deviation (f − f_∞)/f_∞ × 100% quantifies the effect of the vacancy concentration. The computation is performed for the set of vacancy concentrations derived from the paper’s Table I (spheres of size 5, 11, 39, 48, 67, 80, 90).

## Reproduction target
Produce a CSV file `deviation_table.csv` containing the correlation factor f, its infinite‑dilution limit f∞, and the relative deviation (in percent) for the seven f.c.c. vacancy concentrations: 1.27×10⁻², 4.97×10⁻³, 9.5×10⁻⁴, 7.8×10⁻⁴, 5.0×10⁻⁴, 4.3×10⁻⁴, 3.7×10⁻⁴. The file must have columns C_v, n_c, t1, f, f_inf, deviation_percent. The values must be computed from the rigorous finite‑n formula using the t₁(n) data generated from the random‑walk matrix. The exact numeric results are not prescribed; the hidden verifier will check that the deviations are positive and monotonically decreasing with decreasing C_v, and that the reported t1, f, f_inf, and deviation_percent are internally consistent with the rigorous formula.

## Assets

- NumPy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Construct FCC matrix and compute t₁(n)
- Role: process
- Action: Construct the 91×91 jump probability matrix A for the f.c.c. lattice (sphere size 90, 2731 sites) based on the site numbering in Fig. 1 and nearest‑neighbour jump frequencies. Build the initial vacancy distribution w(0) (site 0 occupied). For n from 1 to 100, compute the finite‑sum W(n) = w(0)·(I + A + A² + … + Aⁿ) and extract the probabilities W(k) for k=0..4. Compute t₁(n) = (1/12)[−W(0) − 2W(1) + 2W(3) + W(4)]. Save the t₁ vs n data as evidence.
- Evidence: `/app/outputs/t1_vs_n.csv`

### Step 2: Evaluate correlation factor deviation at vacancy concentrations
- Role: scored (load-bearing)
- Action: For each target vacancy concentration C_v in {1.27e‑2, 4.97e‑3, 9.5e‑4, 7.8e‑4, 5.0e‑4, 4.3e‑4, 3.7e‑4}, compute n_c = 0.33·C_v^{−2/3}. Obtain t₁ at n=n_c from the computed t₁(n) data. Then calculate the correlation factor f = (1+t₁)/(1−t₁) · [1 − (2 t₁ / n_c) · (1 − t₁^{n_c})/(1−t₁²)]. Determine f∞ using the converged t₁ at large n. Compute deviation_percent = 100·(f − f∞)/f∞. Write a CSV file with columns C_v, n_c, t1, f, f_inf, deviation_percent.
- Output file: `/app/outputs/deviation_table.csv`
- Format: csv
- Contract: CSV with columns: C_v (float), n_c (float), t1 (float), f (float), f_inf (float), deviation_percent (float). Exactly seven rows for the concentrations specified in the action.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/deviation_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### deviation_table.csv
- path: `/app/outputs/deviation_table.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file with correlation factor and its deviation from the infinite‑dilution limit for seven f.c.c. vacancy concentrations.
- schema:
  - `type`: table
  - `required_columns`: `C_v`, `n_c`, `t1`, `f`, `f_inf`, `deviation_percent`
  - `units`:
    - `C_v`: atomic fraction
    - `n_c`: count
    - `t1`: unitless
    - `f`: unitless
    - `f_inf`: unitless
    - `deviation_percent`: percent

Notes: The structural checker will verify that deviation_percent values are positive and monotonically decreasing with decreasing C_v, and that the magnitude is small (a few percent), consistent with a negligible vacancy‑concentration effect.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "deviation_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "C_v",
          "n_c",
          "t1",
          "f",
          "f_inf",
          "deviation_percent"
        ],
        "units": {
          "C_v": "atomic fraction",
          "n_c": "count",
          "t1": "unitless",
          "f": "unitless",
          "f_inf": "unitless",
          "deviation_percent": "percent"
        }
      },
      "description": "CSV file with correlation factor and its deviation from the infinite‑dilution limit for seven f.c.c. vacancy concentrations."
    }
  ],
  "notes": "The structural checker will verify that deviation_percent values are positive and monotonically decreasing with decreasing C_v, and that the magnitude is small (a few percent), consistent with a negligible vacancy‑concentration effect."
}
```

## How you are scored
A hidden verifier will read your `deviation_table.csv` and the optional `t1_vs_n.csv` evidence. The verifier performs structural checks: it verifies that deviation_percent values are positive and that they decrease as C_v decreases. It also verifies that the deviations are below thresholds derived from the paper’s conclusions (these thresholds are hidden). Additionally, the verifier may recompute f from the reported t1 and n_c to ensure self‑consistency. The reward is a real number between 0 and 1, with 1.0 indicating full credit. The task does not require matching any specific published table; your computed values are accepted as long as they pass the structural and tolerance checks.
