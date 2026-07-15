# Apparent interfacial free energy from nucleation lag-time data

## Problem background
Understand the influence of citrate on calcium oxalate monohydrate (COM) crystallization is important for urolithiasis. This task focuses on the nucleation step. The goal is to determine the apparent interfacial free energy σ from nucleation lag‑time measurements, applying the Gibbs–Thomson equation.

## Approach
The nucleation rate J is proportional to 1/τ, where τ is the observed lag‑time. For a series of relative supersaturation (RS) values, the measured τ can be used to construct a linearized Gibbs–Thomson plot: ln(1/τ) versus (ln RS)^{-2}. According to classical nucleation theory, the slope of this line is given by

  slope = –16π σ³ v² / (3 k³ T³),

with v = 1.10×10⁻²² cm³ (molecular volume of COM), k = 1.38×10⁻¹⁶ erg/K (Boltzmann constant), and T = 310 K (experimental temperature). Lag‑time data are available for two conditions—control and 3.5 mM citrate—at six RS values. For each condition, linear regression of ln(1/τ) against (ln RS)^{-2} yields a slope, from which σ can be solved.

## Reproduction target
Given the six lag‑time values for the control solution and the six for the citrate solution at the specified RS values, perform the linear regression and compute the apparent interfacial free energy σ for each condition. Report both results in erg/cm², rounded to two decimal places, as a JSON file.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute apparent interfacial free energy from lag-time data
- Role: scored
- Action: Given the lag-time data (in seconds) for control and 3.5 mM citrate solutions at six relative supersaturation values (RS = 20, 22, 24, 28, 33, 37) — control: [400, 250, 170, 130, 70, 30]; citrate: [560, 350, 290, 170, 140, 90] — compute ln(1/τ) for each τ and (ln RS)^{-2} for each RS. Perform separate linear regressions of ln(1/τ) against (ln RS)^{-2} to obtain slopes. For each slope, compute the apparent interfacial free energy σ from the relationship slope = -16π σ³ v² / (3 k³ T³) using v = 1.10×10⁻²² cm³, k = 1.38×10⁻¹⁶ erg/K, T = 310 K. Output the computed σ values in erg/cm² as a JSON file with two decimal places.
- Output file: `/app/outputs/sigma_results.json`
- Format: json
- Contract: {"sigma_control": <float>, "sigma_citrate": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sigma_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sigma_results.json
- path: `/app/outputs/sigma_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Apparent interfacial free energies for control and citrate conditions, derived from Gibbs-Thomson analysis of nucleation lag-time data.
- schema:
  - `type`: object
  - `required_keys`: `sigma_control`, `sigma_citrate`
  - `items`:
    - `sigma_control`:
      - `type`: number
      - `unit`: erg/cm²
    - `sigma_citrate`:
      - `type`: number
      - `unit`: erg/cm²

Notes: The checker will independently recompute sigma from the same input data and constants, and compare the submitted values within an absolute tolerance. No other artifacts are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sigma_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "sigma_control",
          "sigma_citrate"
        ],
        "items": {
          "sigma_control": {
            "type": "number",
            "unit": "erg/cm²"
          },
          "sigma_citrate": {
            "type": "number",
            "unit": "erg/cm²"
          }
        }
      },
      "description": "Apparent interfacial free energies for control and citrate conditions, derived from Gibbs-Thomson analysis of nucleation lag-time data."
    }
  ],
  "notes": "The checker will independently recompute sigma from the same input data and constants, and compare the submitted values within an absolute tolerance. No other artifacts are required."
}
```

## How you are scored
Your submitted sigma_results.json is evaluated by a hidden verifier. The verifier independently recomputes σ from the same input data using the same linear regression and σ‑solving procedure, producing its own sigma_control and sigma_citrate. It then compares your reported values to the recomputed values: full credit is earned when they agree within a set tolerance; credit decreases as the discrepancy grows.
