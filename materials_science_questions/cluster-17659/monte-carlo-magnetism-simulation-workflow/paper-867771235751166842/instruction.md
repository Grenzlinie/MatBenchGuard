# Monte Carlo Spin Precession in Disordered Systems

## Problem background
In many experimental probes of condensed matter — such as muon spin relaxation (μSR), nuclear magnetic resonance, and quantum optical measurements — an initially polarized spin precesses in a local magnetic field created by randomly distributed magnetic clusters. The field of each cluster falls off as a power law with distance, h ∝ r⁻μ, and clusters undergo thermally activated reorientations between allowed easy‑axis directions at a rate ν. Because of the random spatial configuration, the total field at the probe site follows a Lévy‑type distribution whose second moment diverges for μ > d/2, where d is the spatial dimension. This situation leads to anomalous relaxation of the ensemble‑averaged spin polarization ⟨S_z(t)⟩, which cannot be described by standard Gaussian theories. The task is to simulate this spin precession numerically and compute ⟨S_z(t)⟩ for several combinations of reorientation symmetry (uniaxial vs. multiaxial) and fluctuation rate (slow vs. fast), thereby testing the predicted relaxation laws.

## Approach
The core of the reproduction is a Monte Carlo simulation of a spin S = (0,0,1) precessing at the origin, surrounded by a system of N randomly placed point‑like magnetic clusters in d = 3 dimensions with number density n = 0.01 and fixed moment magnitude m = 1. Each cluster at position r contributes a field h = m / r^μ (with μ = 3), so the total field H is the vector sum of all cluster contributions. Cluster orientations are drawn from either two directions (uniaxial, ±z) or six cubic directions (multiaxial, ±x,±y,±z) and flip according to a Poisson process with rate ν. The characteristic width of the field distribution is W = C_W m n^{μ/d}, where C_W = (1/μ) S_d ∫_0^∞ du u^{-1-d/μ}(1 − sin u / u) and S_d = 2π^{d/2}/Γ(d/2) is the surface area of the unit sphere in d dimensions. The spin evolution follows dS/dt = S × H and is integrated for many independent realizations of cluster positions and stochastic reorientation histories. The ensemble‑averaged polarization ⟨S_z(t)⟩ is recorded as a function of the dimensionless time ν t for three representative regimes: (A) uniaxial clusters with ν/W = 10⁻³ (slow fluctuations), (B) multiaxial clusters with ν/W = 10⁻³ (slow fluctuations), and (C) multiaxial clusters with ν/W = 10 (fast fluctuations). The output contains the raw curves; the hidden verifier later fits the expected functional forms (power law, exponential, stretched exponential) to the tails of these curves.

## Reproduction target
Produce a CSV file named polarization_curves.csv containing the ensemble‑averaged spin polarization ⟨S_z(t)⟩ for the three regimes (A) uniaxial slow (ν/W = 10⁻³), (B) multiaxial slow (ν/W = 10⁻³), and (C) multiaxial fast (ν/W = 10). The time axis ν t must cover approximately 10⁻² to 10³ in at least 50 logarithmically spaced points. The file should have four columns: nu_t, S_z_uniaxial_slow, S_z_multiaxial_slow, and S_z_fast. The checker will independently fit a power law, an exponential, and a stretched exponential to the tails of the respective curves and compare the fitted exponents to the theoretical predictions that follow from the model parameters (d=3, μ=3, with the appropriate ν/W ratios). Your goal is to produce simulation data whose tail‑extracted exponents match the theoretical expectations for each regime.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Monte Carlo spin precession simulations
- Role: scored (load-bearing)
- Action: Implement a Monte Carlo simulation of spin precession in a system of randomly placed magnetic clusters with power-law field decay h = m / r^μ. Use d=3, μ=3, number density n=0.01, moment m=1. Generate random cluster positions and allow orientations to flip according to a Poisson process with rate ν. For the uniaxial case only ±z orientations, for multiaxial the six cubic directions ±x,±y,±z. Compute the characteristic field width W using the given integral expression for C_W. Run three sets of simulations: (A) uniaxial, ν/W = 1e-3; (B) multiaxial, ν/W = 1e-3; (C) multiaxial, ν/W = 10. For each, evolve the spin equation dS/dt = S × H, average over many cluster configurations and reorientation histories, and record the ensemble-averaged S_z(t) at logarithmically spaced νt values from 1e-2 to 1e3 (at least 50 points). Write the results to polarization_curves.csv.
- Output file: `/app/outputs/polarization_curves.csv`
- Format: csv
- Contract: Columns: nu_t (float, dimensionless time νt), S_z_uniaxial_slow (float, ensemble polarization for regime A), S_z_multiaxial_slow (float, regime B), S_z_fast (float, regime C). All columns fully populated, increasing nu_t, at least 50 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/polarization_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### polarization_curves.csv
- path: `/app/outputs/polarization_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Ensemble-averaged spin polarization curves for three regimes: (A) uniaxial slow (ν/W=1e-3), (B) multiaxial slow (ν/W=1e-3), (C) multiaxial fast (ν/W=10). The checker will fit the functional forms (power law, exponential, stretched exponential) to the tail of the data and compare the extracted exponents to the theoretical predictions.
- schema:
  - `type`: table
  - `required_columns`: `nu_t`, `S_z_uniaxial_slow`, `S_z_multiaxial_slow`, `S_z_fast`
  - `units`:
    - `nu_t`: dimensionless
    - `S_z_uniaxial_slow`: polarization (dimensionless)
    - `S_z_multiaxial_slow`: polarization (dimensionless)
    - `S_z_fast`: polarization (dimensionless)

Notes: The solving agent must produce this CSV from its own Monte Carlo simulation; no other output is scored. The hidden checker recomputes fitted exponents and compares them to the paper's theoretical values (d/(2μ)=0.5 for the power law and stretched exponential). The agent need not compute the analytical curves explicitly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "polarization_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "nu_t",
          "S_z_uniaxial_slow",
          "S_z_multiaxial_slow",
          "S_z_fast"
        ],
        "units": {
          "nu_t": "dimensionless",
          "S_z_uniaxial_slow": "polarization (dimensionless)",
          "S_z_multiaxial_slow": "polarization (dimensionless)",
          "S_z_fast": "polarization (dimensionless)"
        }
      },
      "description": "Ensemble-averaged spin polarization curves for three regimes: (A) uniaxial slow (ν/W=1e-3), (B) multiaxial slow (ν/W=1e-3), (C) multiaxial fast (ν/W=10). The checker will fit the functional forms (power law, exponential, stretched exponential) to the tail of the data and compare the extracted exponents to the theoretical predictions."
    }
  ],
  "notes": "The solving agent must produce this CSV from its own Monte Carlo simulation; no other output is scored. The hidden checker recomputes fitted exponents and compares them to the paper's theoretical values (d/(2μ)=0.5 for the power law and stretched exponential). The agent need not compute the analytical curves explicitly."
}
```

## How you are scored
A hidden verifier reads your polarization_curves.csv and evaluates the three regimes independently. For the uniaxial‑slow column it fits a power law S_z(t) = a (ν t)^{-p} to the tail (ν t > 10) and checks that the fitted exponent p is consistent with the theoretical value derived from the model. For the multiaxial‑slow column it fits an exponential and verifies that the decay is free of systematic curvature. For the fast column it fits a stretched exponential S_z(t) = a exp(-(c ν t)^β) to the tail and checks that β is consistent with the predicted exponent. Each regime that passes its test earns an equal share of the reward; the final reward is the fraction of regimes that pass. Reporting the paper’s numbers without running the simulation is insufficient, because the verifier recomputes the fits from your raw data and compares the extracted parameters against hidden theoretical references that are not disclosed in these instructions.
