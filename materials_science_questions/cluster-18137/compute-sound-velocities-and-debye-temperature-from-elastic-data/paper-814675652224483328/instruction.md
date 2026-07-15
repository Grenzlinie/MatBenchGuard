# Compute Debye Model Ratios for Thermal and Vibrational Pressure at T/θ=1.0

## Problem background
In a widely used approximation for the thermal pressure of solids (Hildebrand's approximation), the thermal pressure is taken as \(T (\partial S/\partial V)_T\). Using the Mie‑Grüneisen equation and Debye theory, the ratio of this approximate pressure to the true pressure is \(\rho = T C_v / E_{\text{vib}}\), where \(C_v\) is the heat capacity at constant volume and \(E_{\text{vib}}\) is the vibrational energy.

There are two natural interpretations of \(E_{\text{vib}}\), corresponding to two different definitions of the pressure:

- **Thermal pressure:** \(E_{\text{vib}}\) includes only the energy of thermal vibrations (zero‑point energy is treated as part of the static lattice). The pressure vanishes at \(T=0\).
- **Vibrational pressure:** \(E_{\text{vib}}\) includes the total vibrational energy, i.e. thermal excitations plus zero‑point energy. The pressure remains finite at \(T=0\).

For a Debye solid the ratio \(\rho\) depends only on the reduced temperature \(T/\theta\) (where \(\theta\) is the Debye temperature). The task is to compute these ratios at a fixed reduced temperature under both interpretations.

## Approach
The Debye model provides expressions for the vibrational energy and heat capacity in terms of the Debye functions \(D_n(x)\). For a solid with \(N\) atoms and Debye temperature \(\theta\), the energy at temperature \(T\) is

\[
E_{\text{vib,total}} = \frac{9}{8} N k_B \theta \;+\; 9 N k_B T \left(\frac{T}{\theta}\right)^3 \int_0^{\theta/T} \frac{x^3}{e^x-1}\,dx
\]
\[
E_{\text{vib,thermal}} = 9 N k_B T \left(\frac{T}{\theta}\right)^3 \int_0^{\theta/T} \frac{x^3}{e^x-1}\,dx
\]

The heat capacity is obtained from the temperature derivative of the energy; equivalently one may use the standard Debye formula

\[
C_v = 9 N k_B \left(\frac{T}{\theta}\right)^3 \int_0^{\theta/T} \frac{x^4 e^x}{(e^x-1)^2}\,dx .
\]

At the chosen reduced temperature \(T/\theta = 1.0\) these integrals must be evaluated numerically (e.g. using SciPy’s `quad`). Compute the two ratios

\[
\rho_{\text{thermal}} = \frac{T \; C_v}{E_{\text{vib,thermal}}}, \qquad
\rho_{\text{vibrational}} = \frac{T \; C_v}{E_{\text{vib,total}}}
\]

and write them to the output JSON file. No pre‑tabulated values may be used; the solver must perform the integration itself.

## Reproduction target
Produce a JSON file `/app/outputs/rho_results.json` with the following structure:

```json
{
  "rho_thermal": <number>,
  "rho_vibrational": <number>
}
```

Both values must be evaluated at the reduced temperature \(T/\theta = 1.0\) and rounded to three decimal places.

## Assets

- SciPy: scipy
- NumPy: numpy

## Workflow steps

### Step 1: Compute Debye model ratio at T/θ = 1.0
- Role: scored (load-bearing)
- Action: Implement the Debye model to compute the vibrational energy (with and without zero-point energy) and heat capacity at constant volume as functions of reduced temperature T/θ using standard Debye integrals. Evaluate these quantities at T/θ = 1.0. Compute ρ_thermal = T * C_v / E_vib_thermal (where E_vib_thermal excludes zero-point energy) and ρ_vibrational = T * C_v / E_vib_total (where E_vib_total includes zero-point energy). Write the two ratios, rounded to three decimal places, as a JSON object with keys 'rho_thermal' and 'rho_vibrational'.
- Output file: `/app/outputs/rho_results.json`
- Format: json
- Contract: {"rho_thermal": number, "rho_vibrational": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rho_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rho_results.json
- path: `/app/outputs/rho_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The two ratios computed at T/θ=1.0 from the Debye model.
- schema:
  - `type`: object
  - `properties`:
    - `rho_thermal`:
      - `type`: number
      - `description`: Ratio T*C_v / E_vib_thermal (thermal pressure interpretation)
    - `rho_vibrational`:
      - `type`: number
      - `description`: Ratio T*C_v / E_vib_total (vibrational pressure interpretation)
  - `required`: `rho_thermal`, `rho_vibrational`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rho_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "rho_thermal": {
            "type": "number",
            "description": "Ratio T*C_v / E_vib_thermal (thermal pressure interpretation)"
          },
          "rho_vibrational": {
            "type": "number",
            "description": "Ratio T*C_v / E_vib_total (vibrational pressure interpretation)"
          }
        },
        "required": [
          "rho_thermal",
          "rho_vibrational"
        ]
      },
      "description": "The two ratios computed at T/θ=1.0 from the Debye model."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently implements the Debye model using the same definitions and the same reduced temperature. It loads your `rho_results.json`, extracts `rho_thermal` and `rho_vibrational`, and compares each to its own independently computed reference value.

Each ratio is scored separately: a value that agrees with the verifier’s reference within a small tolerance (which accounts for minor numerical differences from integration method and precision) receives full credit for that ratio. If a value falls outside the tolerance, that ratio receives no credit. The final reward is the average of the two ratio scores.

Because the verifier computes the reference values itself from the Debye integrals, you must genuinely implement the model; hard‑coded numbers will not match the recomputed reference.
