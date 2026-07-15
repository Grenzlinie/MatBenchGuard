# Monte Carlo Ionization Cluster Distribution Simulation for Alpha Particle Track Nanodosimetry

## Problem background
In radiation biophysics, the biological damage induced by ionising radiation is driven by the stochastic pattern of energy deposition in nanometre‑sized volumes comparable to DNA segments. Track nanodosimetry investigates the number and distribution of ionisations produced by a single charged particle in such small tissue‑equivalent gas cavities. For an alpha particle traversing low‑pressure propane, Monte Carlo simulations can recreate the resulting cluster size distributions and extract key statistical moments: the mean number of ionisations per event (m1), the ratio of the second raw moment to the first (m2/m1), and the conditional mean ionisation for events with at least one ionisation (m1*). These moments, studied as a function of the impact parameter (the distance between the particle track and the centre of the sensitive volume), characterise the ionisation pattern in the track core and the surrounding delta‑ray cloud.

## Approach
The simulation models a 5.486 MeV alpha particle track in propane at 300 Pa and 20 °C. Alpha‑particle ionisation is described by the Rudd et al. proton ionisation cross sections scaled by the square of the projectile atomic number (Z = 2 for alpha). Secondary electrons are transported using public‑database cross sections for elastic scattering, impact excitation, and ionisation in propane. The energy and angular distributions of ejected electrons are sampled from the HKS model (ICRU Report 55). A spherical sensitive volume of 22 nm diameter is defined; for each impact parameter d from 0 to 70 nm a large number of alpha histories are generated to obtain stable event statistics. An electron is counted as an ionisation if its kinetic energy inside the volume is ≤10 eV. From the resulting cluster size histogram the moments m1, m2/m1 and the conditional mean m1* are computed. To enable a direct comparison with experimental efficiencies, a 25 % detection efficiency factor is applied to m1. The final output is a CSV file tabulating these three quantities for every simulated impact parameter.

## Reproduction target
Compute m1 (with 25 % detection efficiency), m2/m1, and m1* for a representative grid of impact parameters d spanning 0 to 70 nm for the 22 nm‑diameter site at 300 Pa propane. Write the results to `/app/outputs/monte_carlo_results.csv`, containing the columns `d_nm`, `m1`, `m2_over_m1`, `m1_star` for each distance.

## Assets

- Rudd et al. proton ionization cross sections (1985): 10.1103/RevModPhys.57.965
- Electron interaction cross sections for propane (elastic, excitation, ionization)
- HKS model for secondary electron energy and angular distributions

## Workflow steps

### Step 1: Monte Carlo simulation and cluster statistics
- Role: scored (load-bearing)
- Action: Implement a Monte Carlo simulation of a 5.486 MeV alpha particle track in propane at 300 Pa and 20°C. Model alpha ionisation using Rudd et al. proton cross sections scaled by the square of the atomic number (Z=2). Transport secondary electrons using electron cross sections from public databases (elastic, excitation, ionisation). Generate ejected electron energy and angular distributions with the HKS model (ICRU Report 55). Define a spherical sensitive volume of 22 nm diameter. For impact parameters d (distance between track and sphere centre) from 0 to 70 nm in adequate steps, simulate a sufficient number of alpha histories to achieve stable cluster size distributions. Count an electron as an ionisation if its kinetic energy is ≤10 eV inside the volume. For each d compute the mean number of ionisations per event (m1, applying a 25 % detection efficiency factor), the ratio of the second raw moment to the first (m2/m1), and the conditional mean ionisation for events with at least one ionisation (m1*). Write a CSV file with columns d_nm, m1, m2_over_m1, m1_star.
- Output file: `/app/outputs/monte_carlo_results.csv`
- Format: csv
- Contract: CSV with header: d_nm, m1, m2_over_m1, m1_star. Each row corresponds to one impact parameter d in nanometres. All fields are floating‑point numbers.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/monte_carlo_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### monte_carlo_results.csv
- path: `/app/outputs/monte_carlo_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The computed mean ionization (m1), ratio m2/m1, and conditional mean (m1*) at each impact parameter d, scored by comparison to hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `d_nm`, `m1`, `m2_over_m1`, `m1_star`

Notes: The 25% detection efficiency factor is applied to m1; the reference values already incorporate this factor.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "monte_carlo_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "d_nm",
          "m1",
          "m2_over_m1",
          "m1_star"
        ]
      },
      "description": "The computed mean ionization (m1), ratio m2/m1, and conditional mean (m1*) at each impact parameter d, scored by comparison to hidden reference values."
    }
  ],
  "notes": "The 25% detection efficiency factor is applied to m1; the reference values already incorporate this factor."
}
```

## How you are scored
Your submitted CSV file will be evaluated by a hidden verifier. The verifier reads the values you report for each impact parameter and compares them against a reference derived from the original study under the same simulation conditions. The reward is based on how well your computed m1, m2/m1, and m1* reproduce the expected dependence on d, with tolerances that account for statistical fluctuations inherent to the stochastic simulation. The output must strictly adhere to the specified CSV schema. Simply reporting memorised or fabricated numbers is not rewarded – only a correct implementation of the described simulation can produce the expected trends.
