# Elliptic Mohr-Coulomb Failure Predictions for Metallic Glass

## Problem background
Metallic glasses are brittle high-strength materials for which classical failure criteria (linear Mohr–Coulomb, von Mises) often give inaccurate equivalent stress predictions. An elliptical Mohr–Coulomb failure envelope, formulated directly in principal-stress space, has been proposed to better capture the material’s fracture behaviour. The task is to implement this elliptic criterion and evaluate it against classical criteria on a set of 11 experimental test cases for a metallic glass. The central computation involves transforming provided tangent-point data to principal stresses, then computing the predicted equivalent stresses under the elliptic model, the linear Mohr–Coulomb model, and the von Mises criterion, along with the corresponding failure angle and the relative errors of each equivalent stress compared to the material's uniaxial tensile yield strength.

## Approach
The core method is a closed-form transformation that takes each experimental tangent point (σ₀, τ₀) and the dimensionless material constants kST_A (the ratio of semi-axes of the concentric ellipse that contains that point) and K (the ratio of tensile to compressive limit stress). From these, the principal stresses σ₁ and σ₃ are obtained via:

σ₁ = σ₀·[1 - kST_A² + sqrt(kST_A⁴ + (τ₀/σ₀)²)]
σ₃ = σ₀·[1 - kST_A² - sqrt(kST_A⁴ + (τ₀/σ₀)²)]

The classical Mohr–Coulomb equivalent stress is then σ_eq_MC = σ₁ - K·σ₃.

The elliptic-modified Mohr–Coulomb equivalent stress uses the principal-stress form of the elliptical envelope:
σ_eq_MC_mod = (1/(2·(1 - kST_A²)))·[σ₁+σ₃ + sqrt((σ₁+σ₃)² - 4(1 - kST_A²)(σ₁σ₃ + kST_A²·σ_y²))]
where σ_y is the uniaxial tensile yield strength.

The von Mises equivalent stress is the standard:
σ_eq_vM = sqrt(σ₁² - σ₁σ₃ + σ₃²).

The predicted failure angle θ_T is derived from the Mohr’s circle geometry:
tan(2θ_T) = -τ₀ / (σ₀ - a)   with   a = σ₀·(1 - kST_A²),
giving θ_T = 0.5·arctan(-τ₀/(σ₀ - a)).

Finally, for each criterion the relative error versus σ_y is computed as:
e = (σ_y − σ_eq)/σ_y · 100%.

The workflow applies these formulas to all 11 provided test cases, producing a single CSV with all computed quantities. By comparing the errors across the three criteria, one can assess how well the elliptic model describes the experimental data relative to the classical approaches.

## Reproduction target
For each of the 11 experimental test cases supplied in `input_data.csv`, compute the principal stresses (σ₁, σ₃), the failure angle θ_T, the equivalent stresses under the three criteria (classical Mohr–Coulomb, elliptic-modified Mohr–Coulomb, and von Mises), and the relative errors of each equivalent stress versus the material's yield strength σ_y. Write all results to a single CSV file `/app/outputs/computed_results.csv` with one row per test case and columns in the order: sigma1, sigma3, theta_T, sigma_eq_MC, sigma_eq_MC_mod, sigma_eq_vM, eMC, eMC_mod, eMvM. All stress values are in GPa, angles in degrees, and errors in percent.

## Assets

- Zr65Fe5Al10Cu20 experimental tangent-point data
- numpy: numpy

## Workflow steps

### Step 1: Compute principal stresses, equivalent stresses, failure angles, and relative errors
- Role: scored (load-bearing)
- Action: Load the provided input_data.csv. For each of the 11 test cases, transform the tangent-point coordinates (tau0, sigma0) to principal stresses sigma1 and sigma3 using the closed-form relations that involve kST_A. Compute the classical Mohr-Coulomb equivalent stress (sigma1 - K*sigma3), the elliptical-modified Mohr-Coulomb equivalent stress using the principal-stress form of the elliptic envelope, and the von Mises equivalent stress. Compute the predicted failure angle theta_T from the tangent-point geometry and the principal stresses. Compute the relative error of each equivalent stress against the experimental failure stress (uniaxial tensile yield sigma_y), expressed as a percentage. Write all results to a single CSV file.
- Output file: `/app/outputs/computed_results.csv`
- Format: csv
- Contract: 11 rows; columns: sigma1 (float, GPa), sigma3 (float, GPa), theta_T (float, deg), sigma_eq_MC (float, GPa), sigma_eq_MC_mod (float, GPa), sigma_eq_vM (float, GPa), eMC (float, %), eMC_mod (float, %), eMvM (float, %).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.csv
- path: `/app/outputs/computed_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: All computed quantities for the 11 test cases: principal stresses, failure angle, equivalent stresses under three criteria, and their relative errors.
- schema:
  - `type`: table
  - `required_columns`: `sigma1`, `sigma3`, `theta_T`, `sigma_eq_MC`, `sigma_eq_MC_mod`, `sigma_eq_vM`, `eMC`, `eMC_mod`, `eMvM`
  - `units`:
    - `sigma1`: GPa
    - `sigma3`: GPa
    - `theta_T`: deg
    - `sigma_eq_MC`: GPa
    - `sigma_eq_MC_mod`: GPa
    - `sigma_eq_vM`: GPa
    - `eMC`: %
    - `eMC_mod`: %
    - `eMvM`: %

Notes: The file must contain exactly 11 rows, one for each test case, in the same order as the input data. Values must be numeric floats.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sigma1",
          "sigma3",
          "theta_T",
          "sigma_eq_MC",
          "sigma_eq_MC_mod",
          "sigma_eq_vM",
          "eMC",
          "eMC_mod",
          "eMvM"
        ],
        "units": {
          "sigma1": "GPa",
          "sigma3": "GPa",
          "theta_T": "deg",
          "sigma_eq_MC": "GPa",
          "sigma_eq_MC_mod": "GPa",
          "sigma_eq_vM": "GPa",
          "eMC": "%",
          "eMC_mod": "%",
          "eMvM": "%"
        }
      },
      "description": "All computed quantities for the 11 test cases: principal stresses, failure angle, equivalent stresses under three criteria, and their relative errors."
    }
  ],
  "notes": "The file must contain exactly 11 rows, one for each test case, in the same order as the input data. Values must be numeric floats."
}
```

## How you are scored
A hidden verifier independently checks each scored output artifact. For the main computational step, the verifier reads your `computed_results.csv` and compares its numeric contents against hidden reference values. Simply reporting the paper’s published numbers is not sufficient; the output must be the result of actually executing the prescribed computation using the provided input data and formulas. The final reward is a weighted combination of the per‑artifact scores, reflecting correctness of the computed quantities.
