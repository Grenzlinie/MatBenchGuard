# Isotope diffusion ratio in palladium

## Problem background
The diffusion of hydrogen and deuterium in palladium shows an unusual temperature dependence: the measured ratio D_D/D_H exceeds the classical 1/√2 and is rather isotope‑independent at high temperatures. A lattice‑deformation‑assisted jump model has been proposed to explain this behaviour. In this model a hydrogen atom can only jump between neighbouring octahedral sites when a local deformation of the palladium lattice assists the jump; the diffusion coefficient is then expressed through the partition functions of the hydrogen isotope in the octahedral site and in an anisotropic activated state. The aim is to compute the temperature‑dependent D_D/D_H ratio from that model using harmonic‑oscillator partition functions with specified vibrational frequencies, and to examine whether the computed ratio reproduces the excess over the classical value and its monotonic increase at lower temperatures.

## Approach
The ratio of the diffusion coefficients is given by D_D/D_H = (f_D(i)^‡ / f_D(i)) / (f_H(i)^‡ / f_H(i)), where f denotes a partition function and the superscript ‡ indicates the activated state. Each partition function is evaluated as a sum over energy levels of a three‑dimensional harmonic oscillator. The octahedral‑site oscillator is isotropic; its vibrational energies are ħω_H = 69 meV for hydrogen and ħω_D = 47 meV for deuterium. The activated‑state oscillator is strongly anisotropic: two perpendicular directions have ħω_H^‡ = 1.82 × 69 meV, and the direction parallel to the jump path has ħω_H^‡ = 0.02 × 69 meV. All activated‑state frequencies for deuterium are scaled by 0.68 relative to hydrogen. The energy‑level sums are carried up to a cutoff that ensures convergence for every temperature in the range 773–1373 K. The ratio is then evaluated on a dense, uniform temperature grid spanning that range.

## Reproduction target
Compute the D_D/D_H ratio at a uniform grid of at least 50 temperature points between 773 K and 1373 K using the harmonic‑oscillator partition functions and frequencies described above. Write a CSV file with columns 'temperature_K' (float, in kelvin) and 'ratio_DD_DH' (float, dimensionless). The output should span the full temperature range and be ordered by ascending temperature. The file must be placed at /app/outputs/DD_DH_ratio.csv.

## Assets

- Python 3
- NumPy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Compute D_D/D_H ratio from lattice-deformation model
- Role: scored
- Action: Compute the diffusion coefficient ratio D_D/D_H = (f_D(i)^‡ / f_D(i)) / (f_H(i)^‡ / f_H(i)) using three-dimensional harmonic oscillator partition functions. For the octahedral (O) site use isotropic oscillators with ħω_H = 69 meV and ħω_D = 47 meV. For the activated state use strongly anisotropic oscillators: two perpendicular directions with ħω_H^‡ = 1.82×69 meV, one parallel direction with ħω_H^‡ = 0.02×69 meV; scale all activated-state frequencies for deuterium by 0.68. Evaluate each partition function as a sum over energy levels up to a cutoff that ensures convergence for temperatures from 773 K to 1373 K. Compute the ratio at uniform temperature steps (at least 50 points) within that range. Write a CSV file with columns 'temperature_K' (float, K) and 'ratio_DD_DH' (float, dimensionless).
- Output file: `/app/outputs/DD_DH_ratio.csv`
- Format: csv
- Contract: CSV with columns: temperature_K (float, K), ratio_DD_DH (float, dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/DD_DH_ratio.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### DD_DH_ratio.csv
- path: `/app/outputs/DD_DH_ratio.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-dependent ratio of deuterium to hydrogen diffusion coefficients computed from the lattice-deformation-assisted jump model with harmonic oscillator partition functions.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `ratio_DD_DH`
  - `units`:
    - `temperature_K`: K
    - `ratio_DD_DH`: dimensionless

Notes: The absolute diffusion coefficients D_H and D_D are not reproduced; only their ratio is targeted. The specified vibrational frequencies are taken as given and need not be refit to solubility data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "DD_DH_ratio.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "ratio_DD_DH"
        ],
        "units": {
          "temperature_K": "K",
          "ratio_DD_DH": "dimensionless"
        }
      },
      "description": "Temperature-dependent ratio of deuterium to hydrogen diffusion coefficients computed from the lattice-deformation-assisted jump model with harmonic oscillator partition functions."
    }
  ],
  "notes": "The absolute diffusion coefficients D_H and D_D are not reproduced; only their ratio is targeted. The specified vibrational frequencies are taken as given and need not be refit to solubility data."
}
```

## How you are scored
A hidden verifier inspects your submitted DD_DH_ratio.csv. It independently recomputes the D_D/D_H ratio from the same harmonic‑oscillator model and compares the values in your file with those recomputed values using a fixed absolute tolerance. In addition, the verifier checks that the ratio exceeds 1/√2 at every temperature and increases monotonically as the temperature decreases. Your final reward is a weighted combination of how well your computed ratio matches the expected quantitative behaviour across the temperature range; simply reporting a known literature value without performing the required computation will yield a low score.
