# Two-Carrier Debye-Hückel Transport Exponents for CoO

## Problem background
Undoped CoO is a p‑type semiconductor where doubly ionized cobalt vacancies and electron holes dominate the defect chemistry. The oxygen‑partial‑pressure exponents of electrical conductivity (n_σ) and thermopower (n_α) are key quantities that test defect models and probe the role of minority‑carrier electrons. Experimental data often show a discrepancy between n_σ and n_α, motivating the use of more complex transport descriptions that account for defect interactions. In this work, a two‑carrier model with Debye–Hückel activity corrections is employed to compute the exponents and to understand the observed differences between the conductivity and thermopower responses. The computation targets the exponents n_σ, n_α, and the corresponding hole‑concentration exponent n_h at three elevated temperatures.

## Approach
The core idea is to implement the two‑carrier transport model for undoped CoO. The defect equilibrium is described by a Debye–Hückel‑corrected mass‑action law, which relates the hole concentration [h·] to the oxygen partial pressure p(O₂) through the equilibrium constant K₁* and a mean activity coefficient f. The intrinsic electronic equilibrium constant K_i and the mobility ratio b appear in the expressions for the normalized conductivity S and normalized thermopower A.

### Model equations
The Debye–Hückel corrected mass‑action law (Eq. 25 in the paper) is:

$$K_1^* = \frac{[h^\cdot]^3 f^6}{2\,p(\mathrm{O}_2)^{1/2}}$$

The mean activity coefficient f is calculated from the Debye–Hückel theory, here represented by:

$$\log_{10} f = -G\,\sqrt{[h^\cdot]}$$

where G is an empirical constant (given below) that depends on temperature.

Solving the mass‑action law for [h·] yields the hole concentration at any p(O₂). Once [h·] is known, the normalized conductivity S and normalized thermopower A are obtained from the two‑carrier transport expressions (Eqs. 26 and 27):

$$S = [h^\cdot] + \frac{b\,K_i}{[h^\cdot]}$$

$$A = \frac{-[h^\cdot]^2\ln[h^\cdot] - b K_i\ln[h^\cdot] + b K_i\ln K_i}{[h^\cdot]^2 + b K_i}$$

Finally, the oxygen‑pressure exponents are defined as the reciprocal logarithmic derivatives (Eqs. 28, 29 and the analogue for n_h):

$$n_\sigma = \left(\frac{\partial\ln S}{\partial\ln p(\mathrm{O}_2)}\right)^{-1},\quad
n_\alpha = \left(\frac{\partial\ln A}{\partial\ln p(\mathrm{O}_2)}\right)^{-1},\quad
n_h   = \left(\frac{\partial\ln [h^\cdot]}{\partial\ln p(\mathrm{O}_2)}\right)^{-1}.$$

### Model parameters
The numerical values of the constants K₁*, K_i, b, and G for each temperature are taken from Nowotny & Rekas, J. Amer. Ceram. Soc. 72 (1989) 1199 and 1207. They are listed in the table below (the hole concentration [h·] is expressed in mole fraction, and p(O₂) in Pa):

| T (K) | K₁* (Pa⁻¹ ²) | K_i (mole fraction) | b  | G (mole fraction⁻¹ ²) |
|-------|--------------|----------------------|----|-------------------------|
| 1273  | 1.20 × 10⁻⁴ | 1.0 × 10⁻⁸            | 1.0| 0.15                    |
| 1473  | 1.20 × 10⁻⁴ | 1.0 × 10⁻⁸            | 1.0| 0.15                    |
| 1673  | 8.00 × 10⁻⁵ | 1.0 × 10⁻⁶            | 1.0| 0.12                    |

The workflow consists of two stages:

1.  **Forward evaluation of the model curves.** Using the parameters, compute [h·], S, and A across a sufficiently dense logarithmic p(O₂) grid. Write all curves to a CSV file.

2.  **Exponent extraction.** From the computed curves, extract the logarithmic slopes in the experimentally relevant p(O₂) range (approximately 10–10⁵ Pa) by linear regression of log ₁₀ vs log ₁₀. Store the resulting exponents in a JSON file.

The purpose of this exercise is to reproduce the model‑derived exponents and examine the relationship between n_σ and n_α as a function of temperature.

## Reproduction target
Compute the oxygen‑partial‑pressure exponents n_σ, n_α, and n_h for undoped CoO at the three temperatures 1273 K, 1473 K, and 1673 K, using the two‑carrier Debye–Hückel model described in the approach. The exponents must be evaluated from the computed normalized conductivity, thermopower, and hole‑concentration curves over the p(O₂) range of roughly 10 Pa to 10⁵ Pa. The final output is a JSON file (`exponents.json`) containing one entry per temperature, each reporting the three exponent values.

## Assets

- Debye-Hückel model parameters (K1*, Ki, b, f)
- Python scientific stack (numpy, scipy): numpy, scipy

## Workflow steps

### Step 1: Compute full p(O2) curves
- Role: process
- Action: Implement the two-carrier transport model with Debye-Hückel activity correction for undoped CoO. Using the provided equilibrium constants K1*, Ki, mobility ratio b, and activity coefficient f at each temperature (1273, 1473, 1673 K), compute the hole concentration [h·], normalized conductivity S, and normalized thermopower A as functions of oxygen partial pressure p(O2) over a suitable logarithmic grid. Write all computed data to curves.csv with columns: T_K, pO2_Pa, hole_concentration, S, A.
- Evidence: `/app/outputs/curves.csv`

### Step 2: Extract exponents
- Role: scored (load-bearing)
- Action: From curves.csv, extract the oxygen-pressure exponents in the experimental range p(O2) ≈ 10–10^5 Pa. Compute n_σ = ∂(ln S)/∂(ln pO2), n_α = ∂(ln A)/∂(ln pO2), and n_h = ∂(ln [h·])/∂(ln pO2) at each temperature (1273, 1473, 1673 K) using finite differences or linear regression on log-log data. Write the results to exponents.json as a JSON array of objects, each with keys temperature (int), n_sigma (float), n_alpha (float), n_h (float).
- Output file: `/app/outputs/exponents.json`
- Format: json
- Contract: JSON array of objects; each object must have integer key 'temperature' and float keys 'n_sigma', 'n_alpha', 'n_h'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/exponents.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### exponents.json
- path: `/app/outputs/exponents.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Oxygen-partial-pressure exponents n_σ, n_α, n_h for undoped CoO at 1273 K, 1473 K, and 1673 K, computed from the two-carrier Debye-Hückel model.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `temperature`, `n_sigma`, `n_alpha`, `n_h`
    - `properties`:
      - `temperature`:
        - `type`: integer
        - `unit`: K
      - `n_sigma`:
        - `type`: float
        - `unit`: dimensionless
      - `n_alpha`:
        - `type`: float
        - `unit`: dimensionless
      - `n_h`:
        - `type`: float
        - `unit`: dimensionless

Notes: The exponent values are determined from the computed S, A, and hole concentration curves within the experimental p(O2) range.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "exponents.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "temperature",
            "n_sigma",
            "n_alpha",
            "n_h"
          ],
          "properties": {
            "temperature": {
              "type": "integer",
              "unit": "K"
            },
            "n_sigma": {
              "type": "float",
              "unit": "dimensionless"
            },
            "n_alpha": {
              "type": "float",
              "unit": "dimensionless"
            },
            "n_h": {
              "type": "float",
              "unit": "dimensionless"
            }
          }
        }
      },
      "description": "Oxygen-partial-pressure exponents n_σ, n_α, n_h for undoped CoO at 1273 K, 1473 K, and 1673 K, computed from the two-carrier Debye-Hückel model."
    }
  ],
  "notes": "The exponent values are determined from the computed S, A, and hole concentration curves within the experimental p(O2) range."
}
```

## How you are scored
Your submission will be scored by an automated verifier. The scored artifact is `exponents.json` (Step 2).

- The verifier may independently re‑compute the exponents from your raw `curves.csv` to verify internal consistency.
- It then compares the `n_sigma`, `n_alpha`, and `n_h` values in `exponents.json` against the correct model‑derived exponents for each temperature.
- Your overall reward reflects how accurately your computed exponents match the correct values. Reporting numbers that have not been obtained by running the pipeline will not earn a high reward because the verifier can detect discrepancies between the reported exponents and the underlying curves.
