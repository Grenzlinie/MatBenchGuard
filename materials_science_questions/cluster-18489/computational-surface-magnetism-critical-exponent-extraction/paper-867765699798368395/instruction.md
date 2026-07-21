# Computational Surface Magnetism Critical Exponent Extraction

## Problem background
Aperiodic quantum Ising chains, where couplings follow a deterministic substitution rule, display a variety of surface critical behaviors. The surface magnetization in such systems can be expressed as an infinite sum that depends on the coupling sequence. This task reproduces a method to compute the surface magnetization exactly for two aperiodic sequences—Thue-Morse and period-doubling—and to extract the surface critical exponent β_s from the scaling of the magnetization near the critical point. The two sequences are predicted to belong to different universality classes according to a relevance–irrelevance criterion.

## Approach
The surface magnetization m_s is given by m_s = [S(λ,r)]^{-1/2}, where S(λ,r) = Σ_{j=0}^∞ λ^{-2j} r^{-2 n_j} and n_j is the number of "strong" couplings among the first j bonds. The coupling ratio r and the binary sequence f_k ∈ {0,1} determine n_j = Σ_{k=1}^j f_k. For the Thue-Morse sequence, a recursion relation f_{2p}=1−f_p, f_{2p+1}=f_{p+1} allows S(λ,r) to be expressed as a series that can be evaluated by iteration. For the period-doubling sequence, the substitution rule f_{2p}=1−f_p, f_{2p+1}=1 leads to a functional equation that converts S(λ,r) into an infinite product. The critical coupling λ_c is obtained from the asymptotic density ρ_∞ of strong couplings: λ_c = r^{-ρ_∞}. You will compute S(λ,r) for r=2, evaluate m_s at several ratios λ/λ_c, and then determine β_s by fitting m_s(t) ∼ A t^{β_s} for small reduced temperature t>0.

## Reproduction target
For the Thue-Morse and period-doubling sequences with coupling ratio r=2, compute the surface magnetization m_s at the following λ/λ_c values: 0.9, 0.95, 0.99, 0.999, 1.0, 1.001, 1.01, 1.05, 1.1. Output the results to a CSV file with columns: sequence, r, lambda_over_lambda_c, ms. Then, using the computed m_s data, fit the form m_s(t) = A t^{β_s} for small t>0 (e.g., the three smallest t values) and report the fitted β_s for each sequence in a JSON file.

## Assets

- Python 3 with NumPy and SciPy: python3, numpy, scipy

## Workflow steps

### Step 1: Compute surface magnetization data
- Role: scored (load-bearing)
- Action: For the Thue-Morse and period-doubling sequences with coupling ratio r=2, generate the binary sequences, compute S(λ,r) using the appropriate series representation (Thue-Morse: series derived from functional equations; period-doubling: infinite product) with high precision, determine the critical coupling λ_c, and evaluate the surface magnetization m_s at λ/λ_c values of 0.9, 0.95, 0.99, 0.999, 1.0, 1.001, 1.01, 1.05, 1.1. Write the results to /app/outputs/surface_magnetization_data.csv.
- Output file: `/app/outputs/surface_magnetization_data.csv`
- Format: csv
- Contract: Columns: sequence (string: 'thue_morse' or 'period_doubling'), r (float), lambda_over_lambda_c (float), ms (float).
- Scoring: scored by hidden verifier

### Step 2: Compute critical exponents
- Role: scored
- Action: Use the surface magnetization data from surface_magnetization_data.csv to fit the form m_s(t) = A * t^{β_s} for small t>0 (e.g., using the three smallest t values). Report the fitted β_s for each sequence in /app/outputs/critical_exponents.json.
- Output file: `/app/outputs/critical_exponents.json`
- Format: json
- Contract: JSON object with keys 'thue_morse_beta_s' and 'period_doubling_beta_s', each a float.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_magnetization_data.csv`
- `/app/outputs/critical_exponents.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_magnetization_data.csv
- path: `/app/outputs/surface_magnetization_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Surface magnetization values for Thue-Morse and period-doubling sequences at given λ/λ_c ratios.
- schema:
  - `type`: table
  - `required_columns`: `sequence`, `r`, `lambda_over_lambda_c`, `ms`

### critical_exponents.json
- path: `/app/outputs/critical_exponents.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted surface magnetization critical exponents for Thue-Morse and period-doubling sequences.
- schema:
  - `type`: object
  - `required`:
    - `thue_morse_beta_s`: number
    - `period_doubling_beta_s`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_magnetization_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "sequence",
          "r",
          "lambda_over_lambda_c",
          "ms"
        ]
      },
      "description": "Surface magnetization values for Thue-Morse and period-doubling sequences at given λ/λ_c ratios."
    },
    {
      "file": "critical_exponents.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "thue_morse_beta_s": "number",
          "period_doubling_beta_s": "number"
        }
      },
      "description": "Fitted surface magnetization critical exponents for Thue-Morse and period-doubling sequences."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently recompute the surface magnetization from the analytic series/product with high precision and compare your CSV values. It will also check your fitted critical exponents against the exact theoretical values derived from the analytic expressions. Your final reward is a weighted combination: 50% on the accuracy of the surface magnetization values (relative error) and 50% on the accuracy of the β_s exponents (absolute deviation). Simply reporting the paper's numbers is not sufficient; the verifier recomputes everything from the formulas.
