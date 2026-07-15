# RCWA-Based Design Data for Rectangular Groove Grating Polarizers

## Problem background
Reflection gratings with rectangular grooves can be designed to act as polarizers. By choosing the groove depth appropriately, a corrugated conducting surface can backscatter one linear polarization while reflecting the orthogonal polarization with high efficiency. For a TE polarizer, the TM component is completely backscattered (specular reflection negligible) while the TE component is reflected with at least 99% efficiency. The required groove depth depends on the groove width ratio and the incidence angle. The task is to compute these design depths using rigorous electromagnetic simulation.

## Approach
Use Rigorous Coupled-Wave Analysis (RCWA) to solve the scattering of plane waves from a perfectly conducting rectangular groove grating. Set the grating period according to the blaze condition d = λ/(2 sin θ_i) so that only the specular (n=0) and backscatter (n=-1) diffraction orders propagate. Treat the two linear polarisations independently: TE (electric field parallel to the grooves) and TM (magnetic field parallel to the grooves).

For the TE polarizer design, for each prescribed groove width ratio a/d and incidence angle θ_i, scan the groove depth h/λ and compute the specular reflection efficiencies. Record a depth h/λ that gives TM specular reflection below 1% and TE specular reflection at least 99%. For the TM polarizer verification, fix the grating geometry (d, a, θ_i, h) and compute both TE and TM specular reflection efficiencies at that single depth.

An open-source RCWA implementation is available from PyPI (`rcwa`). Any functionally equivalent RCWA solver may be used as long as it correctly models rectangular groove gratings with the required period, width, and depth.

## Reproduction target
Produce two scored artifacts:

1. **`te_polarizer_depths.csv`** – a table of optimal groove depth-to-wavelength ratios h/λ for the TE polarizer design condition. For each combination of groove width ratio a/d (0.00001, 0.001, 0.01, 0.05, 0.1, 0.25, 0.333) and incidence angle θ_i (35°, 45°, 55°, 65°), determine a depth that gives TM specular reflection < 1% and TE specular reflection ≥ 99%. Output only those combinations for which such a depth exists; omit rows where no depth satisfies both criteria.

2. **`tm_polarizer_verification.json`** – computed reflection efficiencies for a specific TM polarizer geometry. At a grating with period d = 0.707λ, groove width a = 0.754d, incidence angle 45°, and groove depth h = 0.96λ, compute and report the TE and TM specular reflection efficiencies.

## Assets

- rcwa (Python RCWA package): https://pypi.org/project/rcwa/

## Workflow steps

### Step 1: TE Polarizer Design Data Generation
- Role: scored (load-bearing)
- Action: For each groove width ratio a/d in {0.00001, 0.001, 0.01, 0.05, 0.1, 0.25, 0.333} and each incidence angle θ_i in {35°, 45°, 55°, 65°}, set grating period d = λ/(2 sin θ_i) with λ=1. Use RCWA to scan groove depth h/λ and find a depth where TM specular reflection efficiency < 1% and TE specular reflection efficiency ≥ 99%. Output the found h/λ for each combination; omit rows where no depth satisfies both criteria.
- Output file: `/app/outputs/te_polarizer_depths.csv`
- Format: csv
- Contract: columns: a_d (float, groove width ratio), theta_i_deg (float, incidence angle in degrees), h_over_lambda (float, groove depth divided by wavelength)
- Scoring: scored by hidden verifier

### Step 2: TM Polarizer Condition Verification
- Role: scored
- Action: For the grating geometry d=0.707λ, a=0.754d, θ_i=45° (λ=1), compute TE and TM specular reflected power at groove depth h=0.96λ using RCWA. Output the reflection efficiencies.
- Output file: `/app/outputs/tm_polarizer_verification.json`
- Format: json
- Contract: keys: theta_i_deg (float), a_over_d (float), d_over_lambda (float), h_over_lambda (float), TE_reflection (float), TM_reflection (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/te_polarizer_depths.csv`
- `/app/outputs/tm_polarizer_verification.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### te_polarizer_depths.csv
- path: `/app/outputs/te_polarizer_depths.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optimal groove depth-to-wavelength ratios for TE polarizer design. Comparison to paper values uses absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `a_d`, `theta_i_deg`, `h_over_lambda`

### tm_polarizer_verification.json
- path: `/app/outputs/tm_polarizer_verification.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Computed reflection efficiencies for the TM polarizer geometry. Requires TE_reflection < 0.01 and TM_reflection > 0.99.
- schema:
  - `type`: object
  - `required`: `theta_i_deg`, `a_over_d`, `d_over_lambda`, `h_over_lambda`, `TE_reflection`, `TM_reflection`

Notes: Only the computational design data (Table I) and the TM polarizer verification are reproduced. Experimental measurements and triangular groove designs are excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "te_polarizer_depths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "a_d",
          "theta_i_deg",
          "h_over_lambda"
        ]
      },
      "description": "Optimal groove depth-to-wavelength ratios for TE polarizer design. Comparison to paper values uses absolute tolerance."
    },
    {
      "file": "tm_polarizer_verification.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "theta_i_deg",
          "a_over_d",
          "d_over_lambda",
          "h_over_lambda",
          "TE_reflection",
          "TM_reflection"
        ]
      },
      "description": "Computed reflection efficiencies for the TM polarizer geometry. Requires TE_reflection < 0.01 and TM_reflection > 0.99."
    }
  ],
  "notes": "Only the computational design data (Table I) and the TM polarizer verification are reproduced. Experimental measurements and triangular groove designs are excluded."
}
```

## How you are scored
A hidden verifier will score your two output artifacts. For `te_polarizer_depths.csv`, the verifier compares your reported h/λ values for each (a/d, θ_i) combination against reference design depths. Accuracy is measured by how close your depths are to the expected values; missing a valid depth or including one where none exists will lower the score. For `tm_polarizer_verification.json`, the verifier checks whether your computed TE reflection is below the required threshold and TM reflection is above the required threshold, confirming the TM polarizer condition. The two scored artifacts are combined into a final reward between 0 and 1.
