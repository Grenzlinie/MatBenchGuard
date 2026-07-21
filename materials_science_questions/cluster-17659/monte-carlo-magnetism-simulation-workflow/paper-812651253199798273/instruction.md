# Fitting Magnetization Work Model for Stress-Annealed Nanocrystalline Ribbons

## Problem background
Stress-annealed Fe73.5Cu1Nb3Si13.5B9 (FINEMET) amorphous ribbons can develop a transverse magnetic anisotropy that strongly influences their magnetic properties. One way to characterize this induced anisotropy is to measure the magnetization work W — the area under the magnetization curve between remanence and a fixed magnetization — as a function of an externally applied tensile stress σ. The random anisotropy model provides a theoretical framework that links the W(σ) curve to three key material parameters: the average local anisotropy energy density ⟨K⟩, the magnetostriction λ, and the stress-induced anisotropy Kann. Extracting these parameters from experiment allows one to quantify the annealing-induced magnetic hardening and to evaluate the magnetoelastic coupling in the nanocrystalline alloy.

## Approach
This reproduction uses the zero‑temperature limit of the random anisotropy model, where the magnetization work for a given applied stress can be expressed as an analytic function of a combined variable x = (3λσ/2 − Kann)/⟨K⟩. For x > 0 and for x < 0, the model provides two different closed‑form expressions for W/(V⟨K⟩). These formulas capture the behavior of magnetic domains with isotropically distributed easy axes in the presence of magnetoelastic coupling and an additional uniaxial anisotropy induced during stress annealing.

We treat the three unknown parameters ⟨K⟩, λ, and Kann as fit parameters. Provided experimental W(σ) data for three samples (labeled A, C, and D in the original measurement) is available as a CSV file. For each sample separately, you will implement the analytical W(σ) function and perform a nonlinear least‑squares fit to the experimental data, thereby determining the set of parameters that best reproduces the observed magnetization work curve.

## Reproduction target
Using the supplied experimental CSV file (experimental_W_vs_sigma.csv), which contains columns sample (A/C/D), stress (MPa), and W (J/m³), implement the zero‑temperature magnetization work formulas of the random anisotropy model. For each sample, carry out a nonlinear least‑squares fit to find the values of the average local anisotropy energy density ⟨K⟩ (J/m³), the magnetostriction λ (dimensionless), and the stress‑induced anisotropy Kann (MPa). Write the fitted parameters for samples A, C, and D into a CSV file with header `sample, K_avg, lambda, Kann`.

## Assets

- Experimental magnetization work vs applied stress data

## Workflow steps

### Step 1: Fit magnetization work model parameters
- Role: scored
- Action: Implement the zero-temperature magnetization work function W(σ) from the random anisotropy model using the parameter x = (3λσ/2 − K_ann)/⟨K⟩ and the piecewise analytic formulas for x>0 and x<0. Load the experimental W(σ) data from the bundled CSV file (experimental_W_vs_sigma.csv). For each sample (A, C, D), perform a nonlinear least-squares fit to determine the optimal parameters ⟨K⟩ (K_avg), λ (lambda), and K_ann (Kann). Write the fitted parameters to fitted_parameters.csv.
- Output file: `/app/outputs/fitted_parameters.csv`
- Format: csv
- Contract: CSV file with header: sample, K_avg, lambda, Kann. Columns: sample (string, values A, C, D), K_avg (float, unit J/m^3), lambda (float, dimensionless), Kann (float, unit MPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.csv
- path: `/app/outputs/fitted_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fitted parameters (⟨K⟩, λ, K_ann) from the magnetization work model, compared to the paper's reported values within relative tolerances.
- schema:
  - `type`: table
  - `required_columns`: `sample`, `K_avg`, `lambda`, `Kann`
  - `units`:
    - `K_avg`: J/m^3
    - `lambda`: dimensionless
    - `Kann`: MPa

Notes: Only approach (a) from the paper (adding stress-induced anisotropy K_ann) is reproduced. The hidden gold consists of the paper's Table II values for samples A, C, D under approach (a).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "K_avg",
          "lambda",
          "Kann"
        ],
        "units": {
          "K_avg": "J/m^3",
          "lambda": "dimensionless",
          "Kann": "MPa"
        }
      },
      "description": "Fitted parameters (⟨K⟩, λ, K_ann) from the magnetization work model, compared to the paper's reported values within relative tolerances."
    }
  ],
  "notes": "Only approach (a) from the paper (adding stress-induced anisotropy K_ann) is reproduced. The hidden gold consists of the paper's Table II values for samples A, C, D under approach (a)."
}
```

## How you are scored
A hidden verifier will read your `fitted_parameters.csv` and compare each fitted parameter against reference values derived from the original study. For each sample, the verifier checks whether the reported ⟨K⟩, λ, and Kann fall within hidden tolerance intervals that reflect genuine reproducibility spread in the fitting. The overall reward is the fraction of samples whose parameters pass these checks. Reporting the correct paper values is not sufficient on its own — the verifier expects physically plausible, toleranced values obtained from the actual fitting procedure.
