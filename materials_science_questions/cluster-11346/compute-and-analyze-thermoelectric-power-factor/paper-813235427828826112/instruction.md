# Compute Harris texture coefficients for Bi2Te3 electrodeposited films

## Problem background
Quantifying the degree of preferred crystallographic orientation in thin films is important because texture affects transport and thermoelectric properties. The Harris texture analysis provides a quantitative measure of this preference by computing a texture coefficient for each crystallographic direction and an overall standard deviation that indicates how much the film deviates from a random powder. In this task, we focus on Bi₂Te₃ films grown under four different electrodeposition conditions, and we aim to compute their Harris texture coefficients and standard deviations from experimental X-ray diffraction peak intensities.

## Approach
The Harris texture coefficient for a given (hkl) reflection is defined as the ratio of the normalized experimental intensity (I_{hkl} / I⁰_{hkl}) to the average of all considered normalized intensities. The standard deviation σ is then computed from the spread of the texture coefficients around unity. In this analysis, only two reflections are considered: (1010) and (110). Thus N=2, and the standard (JCPDS) intensities are both 25. The experimental intensities for each film are provided in the step action; the objective is to compute the texture coefficient for the (110) direction, TC(110), and the standard deviation σ, and to report them in a structured table.

## Reproduction target
Given the experimental XRD peak intensities I(1010) and I(110) for each of the four Bi₂Te₃ films (constant potential +0.02 V, pulsed 5/5 s, 0.1/0.1 s, and 0.01/0.01 s), compute the Harris texture coefficient TC(110) and the standard deviation σ for each film. Write the results to a CSV file at /app/outputs/texture_results.csv with columns: film, TC_110, sigma.

## Assets
None. All required input data (the experimental XRD intensities) are provided directly in the workflow step; no external datasets, models, or tools need to be fetched.

## Workflow steps

### Step 1: Compute Harris texture coefficients and standard deviation
- Role: scored (load-bearing)
- Action: Read the experimental XRD intensities I(1010) and I(110) for each film from the table below. Use the standard Harris texture formulae: TC_{(hkl)} = (I_{(hkl)} / I⁰_{(hkl)}) / ((1/N) Σ (I/I⁰)), with N = 2 (only (1010) and (110) reflections considered), I⁰_{(1010)} = 25, I⁰_{(110)} = 25. Compute TC(110) and the standard deviation σ = sqrt( Σ (TC_{(hkl)} - 1)² / N ) for each film. Write the results to /app/outputs/texture_results.csv.

| Film | I(1010) | I(110) |
|------|---------|--------|
| Constant potential +0.02 V | 16 | 2550 |
| Pulsed 5 s / 5 s | 22 | 3864 |
| Pulsed 0.1 s / 0.1 s | 0 | 3926 |
| Pulsed 0.01 s / 0.01 s | 40 | 4246 |

- Output file: `/app/outputs/texture_results.csv`
- Format: csv
- Contract: CSV with columns: film (string film identifier), TC_110 (float texture coefficient), sigma (float standard deviation).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/texture_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### texture_results.csv
- path: `/app/outputs/texture_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Harris texture analysis output: texture coefficient TC(110) and standard deviation sigma for each of the four Bi2Te3 films. Values will be compared with a tolerance of 0.01.
- schema:
  - `type`: table
  - `required_columns`: `film`, `TC_110`, `sigma`
  - `description`: Columns: film (string identifier of the film, must be one of: constant_potential_+0.02V, pulsed_5s_5s, pulsed_0.1s_0.1s, pulsed_0.01s_0.01s), TC_110 (float, texture coefficient), sigma (float, standard deviation). All four films must be present. The hidden verifier checks each film's values against gold references with a tolerance of 0.01; both columns must match within tolerance for that film to pass.

Notes: Scoring uses tolerance 0.01; target_policy updated to threshold_or_better.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "texture_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "film",
          "TC_110",
          "sigma"
        ],
        "description": "Columns: film (string identifier of the film, must be one of: constant_potential_+0.02V, pulsed_5s_5s, pulsed_0.1s_0.1s, pulsed_0.01s_0.01s), TC_110 (float, texture coefficient), sigma (float, standard deviation). All four films must be present. The hidden verifier checks each film's values against gold references with a tolerance of 0.01; both columns must match within tolerance for that film to pass."
      },
      "description": "Harris texture analysis output: texture coefficient TC(110) and standard deviation sigma for each of the four Bi2Te3 films. Values will be compared with a tolerance of 0.01."
    }
  ],
  "notes": "Scoring uses tolerance 0.01; target_policy updated to threshold_or_better."
}
```

## How you are scored
A hidden verifier will read the texture_results.csv file you produce. For each film, it will compare your computed TC(110) and σ values against gold-standard reference values using a hidden tolerance. Both values must fall within the tolerance for that film to be considered correctly reproduced. Your final reward is the fraction of films that pass; reproducing all four films correctly yields the maximum score.
