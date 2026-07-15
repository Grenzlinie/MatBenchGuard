# Compute Storage and Loss Moduli from Fractional Viscoelastic Constitutive Model

## Problem background
Carbon black-filled elastomers show a pronounced dependence of dynamic moduli on strain amplitude and a weaker dependence on frequency, a behaviour known as the Payne effect. This task implements a finite viscoelastic constitutive model that uses fractional derivatives and an intrinsic time scale to describe the combined amplitude‑frequency response. You will compute the storage modulus G' and loss modulus G'' predicted by the model over a specified grid of frequencies and amplitudes, and store the results in a structured file for verification.

## Approach
The model consists of an equilibrium elastic contribution and a viscoelastic overstress described by a fractional Maxwell element. For uniaxial harmonic loading \(\varepsilon(t) = \Delta\varepsilon \sin(\omega t)\) the storage and loss moduli are given by algebraic expressions involving a shift function \(a(\omega,\Delta\varepsilon)\) that captures the amplitude‑frequency coupling:

\(a(\omega,\Delta\varepsilon) = 1 + \frac{2b}{\pi}\,\Delta\varepsilon\,(\omega\tau)^{\alpha}\)

\(G' = \mu_{\mathrm{eq}}\left(\lambda_0^2 + \frac{2}{\lambda_0}\right) + 3\,\mu_{\mathrm{ov}}\frac{\left(\frac{\omega\zeta}{a}\right)^{2\beta} + \left(\frac{\omega\zeta}{a}\right)^\beta \cos(\beta\pi/2)}
{1 + 2\left(\frac{\omega\zeta}{a}\right)^\beta \cos(\beta\pi/2) + \left(\frac{\omega\zeta}{a}\right)^{2\beta}}\)

\(G'' = 3\,\mu_{\mathrm{ov}}\frac{\left(\frac{\omega\zeta}{a}\right)^\beta \sin(\beta\pi/2)}
{1 + 2\left(\frac{\omega\zeta}{a}\right)^\beta \cos(\beta\pi/2) + \left(\frac{\omega\zeta}{a}\right)^{2\beta}}\)

Here \(\omega = 2\pi f\), \(f\) is the frequency, \(\Delta\varepsilon\) the strain amplitude, and \(\lambda_0\) is the pre‑stretch corresponding to a given compressive pre‑strain. The material parameters \(\mu_{\mathrm{eq}}, \mu_{\mathrm{ov}}, \zeta, \tau, \alpha, \beta, b\) are constants provided below.

## Reproduction target
Compute the storage modulus \(G'\) (in MPa) and loss modulus \(G''\) (in MPa) for every combination of frequency \(f\) from the list \[10, 20, 30, 40, 50, 60\] Hz and strain amplitude \(\Delta\varepsilon\) from the list \[0.001, 0.0025, 0.005, 0.01, 0.02, 0.03, 0.04, 0.05\]. Use the pre‑stretch \(\lambda_0 = 1 / (1 - \varepsilon_0)\) corresponding to a compressive pre‑strain \(\varepsilon_0 = -0.11\). The model parameters are:

\(\mu_{\mathrm{eq}} = 1.86\) MPa, \(\mu_{\mathrm{ov}} = 10.24\) MPa, \(\zeta = 421\) s, \(\tau = 1.0\) s, \(\alpha = 0.449\), \(\beta = 0.494\), \(b = 51078\).

Produce a CSV file `moduli_table.csv` with the columns `frequency_Hz`, `strain_amplitude`, `G_prime_MPa`, `G_double_prime_MPa` containing all 48 data rows.

## Assets
No external datasets, pre‑trained models, or specialised tools are needed. Every required model equation, parameter value, and the target frequency/amplitude grid are given in this instruction. A standard Python environment with basic scientific libraries (e.g., `numpy`, `math`) is sufficient.

## Workflow steps

### Step 1: Compute storage and loss moduli
- Role: scored (load-bearing)
- Action: Implement the one-dimensional linearized fractional viscoelastic model. Using the closed-form expressions for the storage modulus G' and loss modulus G'' that involve a shift function capturing the amplitude-frequency coupling, compute the moduli for every combination of frequency f in [10,20,30,40,50,60] Hz and strain amplitude Δε in [0.001,0.0025,0.005,0.01,0.02,0.03,0.04,0.05]. Use the pre-stretch λ₀ corresponding to a compressive pre-strain ε₀ = −0.11 (λ₀ = 1/(1−ε₀)), and the parameter values μ_eq=1.86 MPa, μ_ov=10.24 MPa, ζ=421 s, τ=1.0 s, α=0.449, β=0.494, b=51078. Write the results to moduli_table.csv.
- Output file: `/app/outputs/moduli_table.csv`
- Format: csv
- Contract: CSV with header: frequency_Hz, strain_amplitude, G_prime_MPa, G_double_prime_MPa. Each row corresponds to one (frequency, amplitude) combination. Columns: frequency_Hz (float), strain_amplitude (float), G_prime_MPa (float), G_double_prime_MPa (float). 48 data rows total.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/moduli_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### moduli_table.csv
- path: `/app/outputs/moduli_table.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Scored CSV of computed storage and loss moduli used to verify that the model reproduces the amplitude and frequency dependence expected from the Payne effect.
- schema:
  - `type`: table
  - `required_columns`: `frequency_Hz`, `strain_amplitude`, `G_prime_MPa`, `G_double_prime_MPa`
  - `units`:
    - `frequency_Hz`: Hz
    - `strain_amplitude`: dimensionless
    - `G_prime_MPa`: MPa
    - `G_double_prime_MPa`: MPa

Notes: The task uses only the closed-form algebraic expressions and the published parameter set from Table 1 of the source paper. No Monte Carlo fitting or experimental data retrieval is required. The hidden checker recomputes the expected G' and G'' using the same formulas and compares the agent's values within a small tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "moduli_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_Hz",
          "strain_amplitude",
          "G_prime_MPa",
          "G_double_prime_MPa"
        ],
        "units": {
          "frequency_Hz": "Hz",
          "strain_amplitude": "dimensionless",
          "G_prime_MPa": "MPa",
          "G_double_prime_MPa": "MPa"
        }
      },
      "description": "Scored CSV of computed storage and loss moduli used to verify that the model reproduces the amplitude and frequency dependence expected from the Payne effect."
    }
  ],
  "notes": "The task uses only the closed-form algebraic expressions and the published parameter set from Table 1 of the source paper. No Monte Carlo fitting or experimental data retrieval is required. The hidden checker recomputes the expected G' and G'' using the same formulas and compares the agent's values within a small tolerance."
}
```

## How you are scored
A hidden verifier reads your `moduli_table.csv`. For each (frequency, amplitude) row the verifier recomputes the expected \(G'\) and \(G''\) independently using the same model and parameters. It compares your submitted values to those expected values within strict tolerances. Your total reward is the fraction of the 48 rows for which both \(G'\) and \(G''\) agree with the expected values. There is no partial credit within a row; both moduli must match for that row to count.
