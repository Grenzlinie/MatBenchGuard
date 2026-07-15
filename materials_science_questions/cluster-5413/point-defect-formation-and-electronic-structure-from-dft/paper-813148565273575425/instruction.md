# Oxygen vacancy concentration and depth distribution in HfO₂ gate dielectric: dependence on process parameters from stochastic placement model

## Problem background
Oxygen vacancy (OV) defects are generated during deposition of a metal gate on high-κ HfO₂. These positively charged defects create dipoles that locally shift the effective gate workfunction and, because of device‑to‑device fluctuations in OV count and position, induce significant variability in threshold voltage. A statistical understanding of how many OVs form and where they are located—as a function of oxygen partial pressure, gate‑stack formation temperature, and metal workfunction—is essential for predicting variability in advanced transistors.

## Approach
We model OV generation using the law of mass action. Surplus electrons released during OV formation fall into the metal electrode, lowering the effective formation energy. The probability of placing an OV at a given site depends on the oxygen partial pressure, the formation temperature, the metal Fermi level, and the local electrostatic potential from already‑placed OVs. Each OV, together with its mirror charge in the metal, forms a dipole whose field is computed via the method of mirror charges. A 3‑D mesh of the HfO₂ film (2 nm thick, node density ∼55 nm⁻³) is created. A randomized‑node‑order placement algorithm visits each site and decides whether to create an OV based on the site probability. For each process condition we generate an ensemble of many independent samples. From the raw per‑sample OV lists we compute the mean sheet concentration N_OV (cm⁻²), the sample‑to‑sample standard deviation, and fit the depth distribution (distance from the metal/HfO₂ interface) to a truncated exponential to obtain the skewness parameter λ (nm). The parameter sweeps cover: (a) oxygen partial pressure pO₂ from 1×10⁻⁸ to 1×10⁻⁶ atm, (b) formation temperature T_G_form at 750 K and 1300 K, (c) metal workfunction WF from 4.5 to 5.0 eV, and (d) a gate‑last process (T_G_form = 750 K) with varying WF.

## Reproduction target
For each combination of process parameters listed in the workflow, run the stochastic placement algorithm and produce an ensemble of 100 independent samples. From these samples compute: (1) the mean OV sheet concentration N_OV (cm⁻²), (2) the within‑condition standard deviation of N_OV, and (3) fit the histogram of OV depths (distance from the metal/HfO₂ interface) to a truncated exponential distribution to obtain the skewness parameter λ (nm). Then report how N_OV varies with pO₂, T_G_form, and WF, and how λ varies with the mean N_OV. The goal is to reproduce the dependence of N_OV and λ on the process parameters as established by the model.

## Assets
No external datasets, pre‑trained models, or proprietary software are required. The simulation is self‑contained and uses only the numerical parameters supplied in the workflow steps. The agent is free to use any open‑source scientific Python stack (e.g., NumPy, SciPy) to implement the computation.

## Workflow steps

### Step 1: Stochastic OV placement and raw data generation
- Role: scored (load-bearing)
- Action: Implement the oxygen vacancy (OV) generation probability model $P_{\mathrm{OV}}(r)$ given by the law of mass action (Equation 5): $$P_{\mathrm{OV}}(r)=\frac{1}{p_{O_2}^{1/2}}\exp\!\Big(-\frac{\Delta G_1^0}{k T_{\mathrm{G,form}}}+2\frac{E_{\mathrm{OV}}(r)-\sum_i \Delta V_i(r)-E_{F,m}}{k T_{\mathrm{G,form}}}\Big)$$ using the provided parameters: standard free energy of OV formation ΔG1^0 = 3 eV, electron affinity = 2.45 eV, energy difference between conduction band and OV level Δ(E_C − E_OV) = 1.2 eV, TiN vacuum work function = 4.7 eV. Create a 3‑D mesh of an HfO₂ film (thickness 2 nm, area representative of a transistor gate) with node density ≈ 55 nm⁻³. For each combination of process parameters — (a) varying pO₂ from 1×10⁻⁸ to 1×10⁻⁶ atm at T_G_form = 1300 K, WF = 4.7 eV; (b) T_G_form = 750 K and 1300 K at pO₂ = 5×10⁻⁸ atm, WF = 4.7 eV; (c) WF varying from 4.5 to 5.0 eV at pO₂ = 5×10⁻⁸ atm, T_G_form = 1300 K; (d) gate‑last process (T_G_form = 750 K) with varying WF — run a randomized‑node‑order stochastic placement algorithm that places OVs based on the per‑site probability, accounting for the dipole potential of already placed OVs. For each condition generate 100 independent samples. For every sample record the OV count and the depth positions (distance from the metal/HfO₂ interface in nm) of every placed OV. Output as JSON.
- Output file: `/app/outputs/ov_per_sample.json`
- Format: json
- Contract: JSON array of objects: { condition_id: int, sample_id: int, ov_count: int, ov_depth_positions: [float, ...] } where ov_depth_positions are distances from the metal/HfO₂ interface in nm.
- Scoring: scored by hidden verifier

### Step 2: OV concentration statistics and depth distribution fitting
- Role: scored
- Action: From the per‑sample OV placement data (step_01), compute for each condition the mean OV sheet concentration N_OV (cm⁻²), the sample‑to‑sample standard deviation of the OV count, and fit the histogram of OV depth positions to the truncated exponential distribution E(λ) to obtain the skewness parameter λ (in nm). Write the aggregated results as CSV.
- Output file: `/app/outputs/ov_statistics.csv`
- Format: csv
- Contract: CSV with columns: condition_id (int), pO2 (float, atm), T_G_form (float, K), WF (float, eV), mean_N_OV (float, cm^-2), std_N_OV (float, cm^-2), lambda (float, nm). One row per simulated condition.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ov_per_sample.json`
- `/app/outputs/ov_statistics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ov_per_sample.json
- path: `/app/outputs/ov_per_sample.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw per‑sample OV placement data: for every (condition, sample) the OV count and a list of depth positions. The checker recomputes ensemble statistics (mean N_OV, standard deviation, λ) from this file and compares them to the paper’s reported trends and ranges; the ov_statistics.csv is also checked for consistency.
- schema:
  - `type`: array
  - `items`:
    - `condition_id`: int
    - `sample_id`: int
    - `ov_count`: int
    - `ov_depth_positions`: `float`
  - `units`:
    - `ov_depth_positions`: nm

### ov_statistics.csv
- path: `/app/outputs/ov_statistics.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per‑condition summary of OV statistics: mean sheet concentration, its standard deviation, and the skewness parameter λ of the truncated exponential depth distribution.
- schema:
  - `type`: table
  - `required_columns`: `condition_id`, `pO2`, `T_G_form`, `WF`, `mean_N_OV`, `std_N_OV`, `lambda`
  - `units`:
    - `pO2`: atm
    - `T_G_form`: K
    - `WF`: eV
    - `mean_N_OV`: cm^-2
    - `std_N_OV`: cm^-2
    - `lambda`: nm

Notes: The checker recomputes mean_N_OV, std_N_OV and λ directly from ov_per_sample.json. The ov_statistics.csv is verified against those recomputed values with small tolerance. Additionally, monotonic trends (N_OV with respect to pO₂, T_G_form, WF) are verified, and the GF (T=1300 K) N_OV range is checked for consistency with published experimental data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ov_per_sample.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "condition_id": "int",
          "sample_id": "int",
          "ov_count": "int",
          "ov_depth_positions": [
            "float"
          ]
        },
        "units": {
          "ov_depth_positions": "nm"
        }
      },
      "description": "Raw per‑sample OV placement data: for every (condition, sample) the OV count and a list of depth positions. The checker recomputes ensemble statistics (mean N_OV, standard deviation, λ) from this file and compares them to the paper’s reported trends and ranges; the ov_statistics.csv is also checked for consistency."
    },
    {
      "file": "ov_statistics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition_id",
          "pO2",
          "T_G_form",
          "WF",
          "mean_N_OV",
          "std_N_OV",
          "lambda"
        ],
        "units": {
          "pO2": "atm",
          "T_G_form": "K",
          "WF": "eV",
          "mean_N_OV": "cm^-2",
          "std_N_OV": "cm^-2",
          "lambda": "nm"
        }
      },
      "description": "Per‑condition summary of OV statistics: mean sheet concentration, its standard deviation, and the skewness parameter λ of the truncated exponential depth distribution."
    }
  ],
  "notes": "The checker recomputes mean_N_OV, std_N_OV and λ directly from ov_per_sample.json. The ov_statistics.csv is verified against those recomputed values with small tolerance. Additionally, monotonic trends (N_OV with respect to pO₂, T_G_form, WF) are verified, and the GF (T=1300 K) N_OV range is checked for consistency with published experimental data."
}
```

## How you are scored
A hidden verifier will read your `ov_per_sample.json`, recompute from that raw data the per‑condition mean N_OV, standard deviation, and λ (by fitting the depth histogram to a truncated exponential). It will then compare these recomputed values against independent reference expectations and verify that the required monotonic trends (N_OV versus pO₂, T_G_form, and WF) hold. Your `ov_statistics.csv` is also checked for internal consistency with the raw JSON. The final reward is a weighted sum over these checks; simply reporting any particular number is not enough, the underlying raw data and derived statistics must be faithful and self‑consistent.
