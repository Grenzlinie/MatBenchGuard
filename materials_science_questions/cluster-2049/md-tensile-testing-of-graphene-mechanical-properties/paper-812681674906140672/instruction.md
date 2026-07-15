# Validation of a nanoindentation protocol for extracting elastic modulus from slack nanoribbons

## Problem background
Suspended microbridge nanoindentation is a common technique to measure the elastic modulus of ultrathin films. However, when the tested bridge has initial slack or wrinkles, the early stage of the indentation curve is dominated by straightening deformation rather than pure stretching. This slack-induced displacement drift produces an apparent softening of the load–displacement response, biasing the modulus extraction if a standard membrane model is used. A refined analysis addresses this by treating the raw data with a full cubic polynomial fit and systematically varying the starting point (SP) and fitting range (FR) to identify a plateau region where the extracted modulus is stable and the fitting residual (RMSE) is low.

## Approach
The reproduction workflow has two stages. First, synthetic load–displacement data is generated for a doubly-clamped slack Pd nanoribbon under line loading. A known input elastic modulus (103 GPa) is used, and the ribbon geometry (length, width, thickness, initial slack height) as well as the preload are fixed. The data is produced by an analytical model: the ribbon remains slack until the indentation exceeds a threshold displacement h1 = h0 + h_pre (where h0 is the slack height and h_pre is the pretension displacement caused by the preload). Beyond that point the ribbon is taut, and the true load P_true follows a cubic relation P_true = α (h_act)³ with α = 8 A E / L³, where A = w·t is the cross‑sectional area and L is the span length. Bending contributions are neglected in this regime. The synthetic noisy‑free P–h curve is then P_meas = P_true + P_pre. The result is a continuous P–h dataset that carries the characteristic flat‑then‑cubic shape induced by the slack.

In the second stage, the cubic polynomial P = f₁ h³ + f₂ h² + f₃ h + f₄ is fitted to subsets of the generated data. The fitting starting point SP is swept from 0 to 1.5 µm and the fitting range FR from 1.0 to 3.0 µm. For each (SP, FR) pair the least‑squares fit yields the four coefficients and the RMSE. The effective elastic modulus is extracted from the dominant cubic coefficient as E = f₁ L³ / (8 A), assuming negligible residual stress and bending. The 2D grid of computed moduli and RMSE values is then inspected to localize a plateau region where the modulus is stable (low variance across neighboring SP/FR) and the RMSE is low; points outside this plateau are rejected as they likely contain contributions from slack straightening or plasticity. The mean modulus from the plateau region is taken as the measured modulus of the ribbon.

## Reproduction target
Generate synthetic P–h data for a slack Pd nanoribbon with the following fixed parameters: ribbon length L = 110 µm, width w = 4 µm, thickness t = 66 nm, initial slack height h0 = 0.8 µm, preload P_pre = 2 µN, input modulus E_in = 103 GPa, and Poisson's ratio ν = 0.3 (used only for possible plane‑strain conversion, not required if thin‑film approximation is employed). Apply the cubic polynomial fitting protocol described above with SP from 0.0 µm to 1.5 µm and FR from 1.0 µm to 3.0 µm; use a grid step no larger than 0.05 µm. Identify the plateau region of stable modulus and low RMSE, compute the mean extracted modulus (in GPa), and calculate the percentage error as 100 * |mean_modulus − 103| / 103. Write these two values into `/app/outputs/summary.json` under the keys `extracted_modulus` (float, GPa) and `percentage_error` (float, percent).

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Generate synthetic P–h data
- Role: process
- Action: Generate synthetic load–displacement data for a doubly-clamped slack nanoribbon under line loading using the analytical model for slack-to-taut stretching deformation. Use the following parameters: ribbon length 110 μm, width 4 μm, thickness 66 nm, initial slack height 0.8 μm, preload 2 μN, input elastic modulus 103 GPa, Poisson's ratio 0.3. Compute the cross-sectional area and effective geometric lengths, then calculate the true load as a function of indentation displacement h, incorporating slack and preload offsets to obtain measurable P–h pairs. Output a CSV file with columns 'h' (μm) and 'P' (μN) for a range of h values covering the indentation depth.
- Evidence: `/app/outputs/generated_ph_data.csv`

### Step 2: Fit cubic polynomial with SP/FR sweep and extract modulus
- Role: scored (load-bearing)
- Action: Load the generated P–h data. For each combination of fitting starting point SP (from 0.0 μm to 1.5 μm) and fitting range FR (from 1.0 μm to 3.0 μm), extract the data subset, fit a cubic polynomial P = f1*h^3 + f2*h^2 + f3*h + f4 using least squares, compute the RMSE, and derive the effective elastic modulus from the cubic coefficient f1 according to the analytical model without bending contribution. Identify a plateau region where the extracted modulus is stable (low variance across neighboring SP/FR) and RMSE is low. Compute the mean modulus across points in that plateau. Write the mean modulus (in GPa) and the percentage error (computed as 100 * |mean_modulus - 103| / 103) into summary.json.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: JSON object with keys: 'extracted_modulus' (float, units: GPa), 'percentage_error' (float, units: percent). The extracted_modulus is the mean fitted modulus from the plateau region; percentage_error = 100 * |extracted_modulus - 103| / 103.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Validated extracted elastic modulus and its error against the known input modulus of the COMSOL simulation.
- schema:
  - `type`: object
  - `required`:
    - `extracted_modulus`: float, units: GPa
    - `percentage_error`: float, units: percent
  - `description`: Scored artifact with extracted modulus from plateau fitting and percentage error relative to 103 GPa.

Notes: The checker will compare the agent's reported extracted_modulus and percentage_error against hidden reference values and tolerances derived from the paper's COMSOL validation outcome. The exact gold values and tolerances are not disclosed in this public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "extracted_modulus": "float, units: GPa",
          "percentage_error": "float, units: percent"
        },
        "description": "Scored artifact with extracted modulus from plateau fitting and percentage error relative to 103 GPa."
      },
      "description": "Validated extracted elastic modulus and its error against the known input modulus of the COMSOL simulation."
    }
  ],
  "notes": "The checker will compare the agent's reported extracted_modulus and percentage_error against hidden reference values and tolerances derived from the paper's COMSOL validation outcome. The exact gold values and tolerances are not disclosed in this public contract."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/summary.json`. It compares your reported `extracted_modulus` to a hidden reference value (derived from the paper’s COMSOL validation) with a tolerance that allows for implementation differences. It also checks that `percentage_error` is below a hidden threshold and that it is numerically consistent with `extracted_modulus` (i.e., equals 100 * |extracted_modulus − 103| / 103 to within rounding). All conditions must be met simultaneously to obtain the full reward (1.0); partial credit is not awarded. You do not need to provide any other files.
