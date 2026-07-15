# Semiclassical Magneto-Thermopower in PbTe Quantum Wells

## Problem background
Thermoelectric materials convert heat directly into electricity, and their efficiency is captured by the thermopower (Seebeck coefficient). In thin-film quantum wells of narrow-gap semiconductors, spin-orbit coupling can split the electron bands into spin-up and spin-down branches, leading to spin-dependent transport. This task examines the magneto-thermopower – the thermopower in the presence of a perpendicular magnetic field – for a two-dimensional electron gas with Rashba spin splitting. The goal is to compute the longitudinal and transverse components of the magneto-thermopower tensor and the zero-field power factor, and to observe how these quantities differ between the two spin sub-bands.

## Approach
The magneto-thermopower is derived from the semiclassical Mott formula, which relates thermopower to the energy derivative of the conductivity tensor. In a magnetic field, the conductivity tensor gains off-diagonal components, giving both longitudinal (Qxx) and transverse (Qyx) thermopower. The relaxation time is modeled as τ ∝ εᵚ, where the exponent s is fixed. The two spin branches are described by a Rashba-split parabolic dispersion; the Rashba coefficient is computed from the material's band parameters (band gap, spin-orbit splitting, effective mass) and an out-of-plane electric field. The Fermi energies for spin-up and spin-down carriers are obtained self-consistently from the 2D carrier density. The zero-field power factor is computed as PF = Q²σ, where Q is the Seebeck coefficient and σ the Drude conductivity for each spin branch. The entire workflow is implemented in Python, using standard numerical libraries, and writes the results to CSV files.

## Reproduction target
Compute the spin-resolved magneto-thermopower tensor components and the zero-field power factor for a 6.0 nm PbTe quantum well. For the magneto-thermopower, use a fixed carrier density, temperature, and scattering exponent, and evaluate Qxx and Qyx at a set of magnetic fields for both spin-up and spin-down electrons. For the power factor, compute PF as a function of carrier density for both spin branches at a lower temperature. The numerical results for each case are written to separate CSV files with the columns specified in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute magneto-thermopower tensor components
- Role: scored (load-bearing)
- Action: Implement the semiclassical formulas for longitudinal Qxx and transverse Qyx using a power-law energy-dependent relaxation time. Use the Rashba spin-split Fermi energies for a 6.0 nm PbTe quantum well. Fix carrier density n = 1×10^12 cm⁻², temperature T = 4 K, scattering exponent s = 0.7, relaxation time τ = 0.1 ns, and the PbTe material parameters: effective mass m* = 0.0565 mₑ, band gap Eg = 0.2131 eV, spin-orbit splitting Δ = 0.77 eV, and out-of-plane electric field F = 10⁶ V/m. Compute the Rashba coefficient from the given band parameters. Calculate Qxx and Qyx (in μV/K) for spin-up and spin-down electrons at magnetic fields B from -3.0 T to 3.0 T in steps of 0.5 T. Write the results to magneto_thermopower.csv.
- Output file: `/app/outputs/magneto_thermopower.csv`
- Format: csv
- Contract: Columns: B_field (T), spin (string: 'up' or 'down'), Qxx (uV/K), Qyx (uV/K). Rows for B from -3.0 to 3.0 in steps of 0.5 T, for both spins.
- Scoring: scored by hidden verifier

### Step 2: Compute power factor
- Role: scored
- Action: Compute the zero-field power factor PF = Q^2 σ for both spin branches using the same PbTe QW parameters (effective mass, Rashba coefficient) and scattering exponent s = 0.7, relaxation time τ = 1.0 ns, temperature T = 1 K. Vary the carrier density n over [1e11, 2e11, 5e11, 1e12, 2e12, 5e12, 1e13] cm⁻². Calculate PF in μW/cm·K² for spin-up and spin-down and write to power_factor.csv.
- Output file: `/app/outputs/power_factor.csv`
- Format: csv
- Contract: Columns: carrier_density (cm^-2), spin (string: 'up' or 'down'), power_factor (uW/cmK^2). Rows for densities: [1e11, 2e11, 5e11, 1e12, 2e12, 5e12, 1e13] for both spins.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magneto_thermopower.csv`
- `/app/outputs/power_factor.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magneto_thermopower.csv
- path: `/app/outputs/magneto_thermopower.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Spin-resolved magneto-thermopower components as a function of magnetic field. The checker recomputes the expected values and compares with a relative tolerance of 1% or absolute 1 μV/K.
- schema:
  - `type`: table
  - `required_columns`: `B_field`, `spin`, `Qxx`, `Qyx`
  - `units`:
    - `B_field`: T
    - `spin`: None
    - `Qxx`: uV/K
    - `Qyx`: uV/K

### power_factor.csv
- path: `/app/outputs/power_factor.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Spin-resolved zero-field power factor as a function of carrier density. The checker recomputes the expected values and compares with a relative tolerance of 1% or absolute 0.1 μW/cm·K².
- schema:
  - `type`: table
  - `required_columns`: `carrier_density`, `spin`, `power_factor`
  - `units`:
    - `carrier_density`: cm^-2
    - `spin`: None
    - `power_factor`: uW/cmK^2

Notes: The agent must use the formulas described in the problem. The hidden checker independently recomputes the results from the same fixed input parameters to validate the agent's output.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magneto_thermopower.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "B_field",
          "spin",
          "Qxx",
          "Qyx"
        ],
        "units": {
          "B_field": "T",
          "spin": null,
          "Qxx": "uV/K",
          "Qyx": "uV/K"
        }
      },
      "description": "Spin-resolved magneto-thermopower components as a function of magnetic field. The checker recomputes the expected values and compares with a relative tolerance of 1% or absolute 1 μV/K."
    },
    {
      "file": "power_factor.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "carrier_density",
          "spin",
          "power_factor"
        ],
        "units": {
          "carrier_density": "cm^-2",
          "spin": null,
          "power_factor": "uW/cmK^2"
        }
      },
      "description": "Spin-resolved zero-field power factor as a function of carrier density. The checker recomputes the expected values and compares with a relative tolerance of 1% or absolute 0.1 μW/cm·K²."
    }
  ],
  "notes": "The agent must use the formulas described in the problem. The hidden checker independently recomputes the results from the same fixed input parameters to validate the agent's output."
}
```

## How you are scored
Each workflow stage produces a scored artifact. A hidden verifier independently recomputes the expected values from the same formulas and input parameters and compares your results to the recomputed gold standard using appropriate tolerances. The comparison checks the numerical values and, where applicable, the relative ordering between spin branches. The final reward is a weighted combination of the scores from all scored stages. Simply reporting the paper's numbers is not sufficient; your calculation must agree with the independent recomputation within the allowed margin.
