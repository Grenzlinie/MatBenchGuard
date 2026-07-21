# Static and vibrational contributions to thermal line shift

## Problem background
The thermal shift of the R1-line (a component of the ²E₂ → ⁴A₂ transition) of Cr³⁺ in LiAl₅O₈ arises from two physical effects: a static effect due to lattice thermal expansion, and a vibrational effect from electron–phonon interaction. Disentangling these contributions and determining the true electron–phonon coupling parameter (as opposed to an apparent one that neglects the static effect) is important for understanding the temperature behavior of this luminescent material. This task computes the static temperature derivative, the vibrational temperature derivative, their ratio, the true electron–phonon coupling parameter, and the static parameter from prescribed input constants.

## Approach
The static contribution to the temperature derivative is obtained by multiplying the lattice thermal expansion coefficient (dlnR/dT) by the bond-length sensitivity of the R1-line energy (dE/dlnR). The vibrational contribution is then found by subtracting the static part from the known total observed temperature derivative. Compute the ratio t = dE_dT_static / dE_dT_vib. Using the apparent electron–phonon coupling parameter α = 510 cm⁻¹ and the relations (A − α′) = −α and A = −α′ t, solve for the true coupling α′ = α / (1 + t) and the static parameter A = −α′ t. The results are written to a JSON file. All necessary numeric inputs are supplied in the workflow step.

## Reproduction target
Produce a JSON file named computed_values.json containing the following five computed quantities with their units: dE_dT_static (static temperature derivative, cm⁻¹/K), dE_dT_vib (vibrational temperature derivative, cm⁻¹/K), ratio_t (dimensionless ratio of the static to vibrational contribution), alpha_prime (true electron–phonon coupling parameter, cm⁻¹), and A (static parameter, cm⁻¹). Compute all quantities from the given input constants using the described relations.

## Assets
None. All required numeric constants (the linear thermal expansion coefficient, the bond-length dependence, the observed total temperature derivative, and the apparent electron–phonon coupling parameter) are provided directly in the workflow step.

## Workflow steps

### Step 1: Compute thermal shift parameters
- Role: scored (load-bearing)
- Action: Using the provided fixed constants: linear thermal expansion coefficient (6.7e-6 K^-1), bond-length dependence of R1-line (7100 cm^-1), observed total temperature derivative (-21e-2 cm^-1/K), and apparent electron-phonon coupling parameter (510 cm^-1), compute the static temperature derivative, vibrational temperature derivative, their ratio, the true electron-phonon coupling parameter, and the static parameter. Write all five quantities to computed_values.json.
- Output file: `/app/outputs/computed_values.json`
- Format: json
- Contract: {"dE_dT_static": <float, cm^-1/K>, "dE_dT_vib": <float, cm^-1/K>, "ratio_t": <float, dimensionless>, "alpha_prime": <float, cm^-1>, "A": <float, cm^-1>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_values.json
- path: `/app/outputs/computed_values.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed thermal shift parameters, separating static and vibrational contributions and deriving the true electron-phonon coupling parameter.
- schema:
  - `type`: object
  - `required`:
    - `dE_dT_static`: number (cm^-1/K)
    - `dE_dT_vib`: number (cm^-1/K)
    - `ratio_t`: number (dimensionless)
    - `alpha_prime`: number (cm^-1)
    - `A`: number (cm^-1)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `dE_dT_static`: cm^-1/K
    - `dE_dT_vib`: cm^-1/K
    - `alpha_prime`: cm^-1
    - `A`: cm^-1

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "dE_dT_static": "number (cm^-1/K)",
          "dE_dT_vib": "number (cm^-1/K)",
          "ratio_t": "number (dimensionless)",
          "alpha_prime": "number (cm^-1)",
          "A": "number (cm^-1)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "dE_dT_static": "cm^-1/K",
          "dE_dT_vib": "cm^-1/K",
          "alpha_prime": "cm^-1",
          "A": "cm^-1"
        }
      },
      "description": "Computed thermal shift parameters, separating static and vibrational contributions and deriving the true electron-phonon coupling parameter."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your computed_values.json and compares each reported quantity against the correct reference values. Each value must be within an appropriate hidden tolerance. Your score reflects how many of the quantities are computed correctly. You must perform the actual calculation from the given inputs; reporting memorized numbers without genuine computation will not satisfy the verifier.