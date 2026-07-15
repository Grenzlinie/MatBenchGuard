# Partial Molal Volume Coefficient Fitting for Aqueous Ions

## Problem background
Understanding how partial molal volumes of aqueous ions at infinite dilution depend on ion charge \(z\) and crystal radius \(r\) is central to the thermodynamics of electrolyte solutions. A simple physical model leads to an equation of the form \( \bar{V}_{\text{ion}} = A r^{3} - B z^{2}/r \), where the first term represents the volume of the ion cavity and the second term accounts for volume decrease due to electrostriction of the solvent. The coefficients \(A\) and \(B\) are not known a priori; they must be determined from experimental data and their values may differ between cations and anions. This task investigates the partial molal volume systematics by empirically estimating \(A\) and \(B\) for each ion type using published ion data.

## Approach
The model \( \bar{V}_{\text{ion}} = A r^{3} - B z^{2}/r \) can be linearized for regression. Dividing both sides by \(r^{3}\) yields
\[
\frac{\bar{V}_{\text{ion}}}{r^{3}} = A - B \frac{z^{2}}{r^{4}}.
\]
For a set of ions with known charge \(z\), crystal radius \(r\) (in Å), and absolute partial molal volume \(\bar{V}_{\text{ion}}\) (in cm³/mol), one can treat \(x = z^{2}/r^{4}\) and \(y = \bar{V}_{\text{ion}}/r^{3}\), and fit a straight line \(y = A - B x\). The slope gives \(-B\) and the intercept gives \(A\). The fit must be performed separately for cations and anions because the physical contributions may differ. The necessary ion data (a digital transcription of the published compilation) is provided as a bundled CSV.

## Reproduction target
Using the provided ion data CSV (bundled at `/app/resources/hepler_ion_data.csv`), perform the linear regression of \( \bar{V}_{\text{ion}}/r^{3} \) against \( z^{2}/r^{4} \) separately for cations and anions. Extract the intercept \(A\) and slope \(-B\) for each ion type. Save the four fitted constants as a JSON object at `/app/outputs/constants.json` with the exact keys `cation_A`, `cation_B`, `anion_A`, `anion_B`, each a floating‑point number.

## Assets

- Ion data CSV (Hepler 1957)

## Workflow steps

### Step 1: Load ion data
- Role: process
- Action: Read the bundled CSV file containing ion data (name, charge z, crystal radius r in Å, partial molal volume V in cc/mol, and ion type). Load the data into memory for further processing.
- Evidence: none

### Step 2: Fit constants A and B for cations and anions
- Role: scored (load-bearing)
- Action: Separate the data into cations and anions. For each group, compute the transformed variables: x = z²/r⁴ and y = V/r³. Perform linear regression (y = A - B * x) to obtain the intercept A and slope -B, so that B = -slope. Write the four fitted constants to /app/outputs/constants.json as a JSON object with keys cation_A, cation_B, anion_A, anion_B, each a float.
- Output file: `/app/outputs/constants.json`
- Format: json
- Contract: {"cation_A": float, "cation_B": float, "anion_A": float, "anion_B": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### constants.json
- path: `/app/outputs/constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Coefficients A and B of the partial molal volume equation (V = A·r³ − B·z²/r) for cations and anions, obtained by linear regression of V/r³ against z²/r⁴ on the provided ion data.
- schema:
  - `type`: object
  - `required`:
    - `cation_A`: number
    - `cation_B`: number
    - `anion_A`: number
    - `anion_B`: number

Notes: The ion data table is provided as a resource; the agent does not need to compile it from the literature. The fitted constants are compared against hidden reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "cation_A": "number",
          "cation_B": "number",
          "anion_A": "number",
          "anion_B": "number"
        }
      },
      "description": "Coefficients A and B of the partial molal volume equation (V = A·r³ − B·z²/r) for cations and anions, obtained by linear regression of V/r³ against z²/r⁴ on the provided ion data."
    }
  ],
  "notes": "The ion data table is provided as a resource; the agent does not need to compile it from the literature. The fitted constants are compared against hidden reference values with appropriate tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your `constants.json` and compares each of the four constants (cation_A, cation_B, anion_A, anion_B) against a hidden reference gold derived from the original analysis. Each constant is checked against a tolerance that accounts for minor numerical differences between independent implementations; the exact tolerance is not disclosed but is set to distinguish a genuine regression from a random guess. The final reward is the fraction of the four constants that fall within the tolerance. No qualitative interpretation or fit diagnostics are required; the score depends solely on the numerical accuracy of the four coefficients.
