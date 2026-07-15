# Extracting Thermoelectric Transport Parameters with a Single Parabolic Band Model

## Problem background
Thermoelectric materials can directly convert heat into electricity, with their efficiency determined by the power factor P = σ α², where σ is the electrical conductivity and α is the Seebeck coefficient. A major challenge is that σ and α are strongly coupled, making it difficult to independently enhance the power factor. Conducting polymer nanocomposites, in which inorganic nanostructures are embedded in a polymer matrix, have been proposed as a route to improving the thermoelectric performance. The organic–inorganic interfaces can act as energy filters that selectively scatter low‑energy charge carriers, potentially increasing α without severely degrading σ. Understanding how the carrier concentration, carrier mobility, and energy‑dependent scattering evolve at such interfaces is critical. The single parabolic band (SPB) model, which describes charge transport in semiconductors with a single band and energy‑dependent relaxation time, provides a framework for extracting these microscopic transport parameters from macroscopic experimental measurements of electrical conductivity, Seebeck coefficient, and Hall coefficient. This task asks you to compute these SPB‑derived transport parameters for two thermoelectric samples: a pure P3HT matrix and a P3HT–Bi₂Te₃ nanocomposite, utilising the measured experimental inputs that are provided below.

## Approach
For a p‑type single parabolic band, the Seebeck coefficient α can be expressed as α = (k_B/e) [ (r+5/2)F_{r+3/2}(η) / (r+3/2)F_{r+1/2}(η) − η ], where η = E_f/(k_B T) is the reduced Fermi level, e is the elementary charge, k_B is Boltzmann’s constant, and F_j(η) are Fermi–Dirac integrals. The parameter r is related to the energy‑dependent scattering exponent λ by r = λ − 1/2, with the relaxation time assumed to follow τ ∝ E^(r). The Hall coefficient R_H for a single parabolic band yields the hole concentration n directly as n = 1/(e R_H), ignoring a Hall factor of order unity. With n known, the reduced Fermi level η determines the effective density‑of‑states mass m* through n = (2/π^(2)) (2π m* k_B T / h^(2))^(3/2) F_{1/2}(η), but the mass cancels when solving the coupled equations. By numerically solving the system consisting of the Seebeck coefficient equation and the carrier‑concentration relation, one can obtain η and λ simultaneously. Once η and λ are known, the Fermi level relative to the valence band edge is E_f = η k_B T, the carrier mobility is μ = σ/(n e), and the power factor is P = σ α². The calculation must be performed at room temperature (T = 300 K) using standard physical constants. The problem reduces to a two‑variable root‑finding task that can be implemented with numerical libraries or custom code.

## Reproduction target
You are given the room‑temperature experimental measurements for two samples:

- P3HT matrix: σ = 930 S m⁻¹, α = 24 μV K⁻¹, R_H = 1.4×10⁻² m³ C⁻¹.
- P3HT–Bi₂Te₃ nanocomposite: σ = 450 S m⁻¹, α = 118 μV K⁻¹, R_H = 1.8×10⁻² m³ C⁻¹.

Using the single parabolic band model described above, compute for each sample:

- Fermi level E_f (in eV, signed relative to the valence band edge),
- scattering parameter λ (dimensionless),
- carrier concentration n (in cm⁻³),
- carrier mobility μ (in cm² V⁻¹ s⁻¹),
- power factor P (in μW K⁻² m⁻¹).

Write the results to `/app/outputs/transport_parameters.csv` with exactly the following columns: `sample,Ef_eV,lambda,n_cm3,mu_cm2Vs,P_uW_K2m`. The file must contain one row for `P3HT` and one row for `P3HT-Bi2Te3` (the sample strings must match exactly). All numeric values should be given as standard floating-point numbers.

## Assets

- SciPy: scipy

## Workflow steps

### Step 1: Derive transport parameters from experimental measurements
- Role: scored (load-bearing)
- Action: Given the experimental electrical conductivity (σ), Seebeck coefficient (α), and Hall coefficient (R_H) for the P3HT matrix and the P3HT–Bi₂Te₃ nanocomposite, apply a single parabolic band model with Fermi–Dirac statistics to solve for the reduced Fermi level and energy-dependent scattering parameter. Compute the Fermi level relative to the valence band edge, carrier concentration, carrier mobility, and power factor for each sample. Write the results to transport_parameters.csv.
- Output file: `/app/outputs/transport_parameters.csv`
- Format: csv
- Contract: Columns: sample (str), Ef_eV (float, signed, in eV), lambda (float, dimensionless), n_cm3 (float, in cm⁻³), mu_cm2Vs (float, in cm² V⁻¹ s⁻¹), P_uW_K2m (float, in µW K⁻² m⁻¹). Two rows: 'P3HT' and 'P3HT-Bi2Te3'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transport_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transport_parameters.csv
- path: `/app/outputs/transport_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The scored artifact containing the extracted Fermi level, scattering parameter, carrier concentration, carrier mobility, and power factor for both samples.
- schema:
  - `type`: table
  - `required_columns`: `sample`, `Ef_eV`, `lambda`, `n_cm3`, `mu_cm2Vs`, `P_uW_K2m`
  - `units`:
    - `Ef_eV`: eV
    - `lambda`: dimensionless
    - `n_cm3`: cm^-3
    - `mu_cm2Vs`: cm^2 V^-1 s^-1
    - `P_uW_K2m`: muW K^-2 m^-1

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transport_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "Ef_eV",
          "lambda",
          "n_cm3",
          "mu_cm2Vs",
          "P_uW_K2m"
        ],
        "units": {
          "Ef_eV": "eV",
          "lambda": "dimensionless",
          "n_cm3": "cm^-3",
          "mu_cm2Vs": "cm^2 V^-1 s^-1",
          "P_uW_K2m": "muW K^-2 m^-1"
        }
      },
      "description": "The scored artifact containing the extracted Fermi level, scattering parameter, carrier concentration, carrier mobility, and power factor for both samples."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your `transport_parameters.csv` and compare each computed numeric field (Ef_eV, lambda, n_cm3, mu_cm2Vs, P_uW_K2m) against expected reference values. The scoring function aggregates the deviations across the five parameters with appropriate tolerances, producing a single reward between 0.0 (completely wrong or missing) and 1.0 (excellent agreement). The reference values are derived from the same physical model and the given experimental inputs; small numerical differences due to implementation details (e.g., numerical integration error, solver tolerance) are expected and are absorbed by the allowed tolerances. The file must conform exactly to the specified format (column order and header, sample strings) — structural checks account for a small weight of the total score. You do not need to guess the hidden tolerances; simply implement the model as accurately as possible using the supplied experimental data.
