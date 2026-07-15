# Condensate fraction of liquid 4He from paired-phonon diagrammatic analysis

## Problem background
The condensate fraction n(T) is the fraction of atoms in the zero-momentum single-particle state in superfluid ⁴He. It is a fundamental quantity that characterizes the superfluid phase and is closely tied to off-diagonal long-range order. First-principles evaluation of n(T) from the interatomic potential and the phonon spectrum provides insight into many-body correlations at low temperatures. This task computes n(T) and the number of excitations per particle ν(T) for liquid ⁴He at density ρ = 0.0218 Å⁻³ within Feenberg's paired-phonon model, using a diagrammatic cluster expansion extended to finite temperatures. By comparing three different modelling choices for the elementary-excitation dispersion — the Bijl-Feynman (paired-phonon) form, the hydrodynamic linear limit, and an empirical curve from experiment — one can assess the role of roton effects and the regime where the simple model is adequate. The work also outputs the thermal correlation function w(r,T) at a representative temperature, which visualizes how the thermal dressing of the ground‑state correlations changes with the chosen phonon model.

## Approach
The calculation starts from a zero‑temperature Jastrow wave function, Ψ₀ = ∏_{i<j} f(r_{ij}), whose optimal pair factor f(r) and static structure function S(k) are obtained by a self‑consistent paired‑phonon analysis with the hypernetted‑chain (HNC) closure. The interatomic interaction is the Lennard‑Jones (6‑12) potential with standard ⁴He parameters (ε = 10.22 K, σ = 2.556 Å).

Finite‑temperature effects enter through a thermal factor f_th(r,T) that is expressed via a correlation function w(r,T). This quantity is constructed from the ground‑state structure factor S(k), a chosen dispersion relation ε(k) for the elementary excitations, and the Bose‑Einstein occupancy at temperature T. Three different choices for ε(k) are used:
- Paired‑phonon (Bijl–Feynman): ε(k) = ħ²k²/(2m S(k)).
- Hydrodynamic limit: ε(k) = ħ s k, with the speed of sound s ≈ 238.3 m/s.
- Empirical: the experimental phonon‑roton dispersion of Cowley & Woods (1971), digitized and interpolated.

The resulting finite‑temperature pair factor f(r,T) = f(r) exp(½ w(r,T)) defines a temperature‑dependent trial function of Jastrow form, allowing the application of the diagrammatic cluster expansion for the one‑body density matrix developed by Ristig and Clark. The condensate fraction n(T) is given by n(T) = exp[−⅛ (T/T₀)² + Q(T)], where T₀ is a phonon temperature scale derived from the density and sound speed, and Q(T) is a sum of three terms: a configurational integral over the correlation functions ξ = f(r,T)−1 and η = f²(r,T)−1, a term involving the finite‑temperature structure factor S(k,T) = S(k) coth(ε(k)/(2k_B T)), and a convolution approximation for the three‑body contribution. The number of excitations per particle ν(T) is computed for the empirical dispersion by integrating the Bose‑Einstein distribution over k‑space.

The pipeline thus requires (i) a ground‑state HNC/paired‑phonon calculation, (ii) digitization of the empirical dispersion, (iii) evaluation of ν(T), (iv) evaluation of w(r,T) at T = 1.4 K for the three models, and (v) evaluation of n(T) for all ten temperatures and all three models.

## Reproduction target
Carry out the full computational pipeline for liquid ⁴He at density ρ = 0.0218 Å⁻³ and produce the following three CSV files under `/app/outputs`:

1. **excitation_number_table.csv** – A table of the number of excitations per particle ν(T) computed with the empirical dispersion relation (Cowley & Woods 1971) at the ten temperatures T = 0.2, 0.6, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.4, 3.0 K. Columns: `T`, `nu_empirical`.

2. **thermal_correlation_function_data.csv** – The thermal correlation function w(r,T) at T = 1.4 K for all three dispersion models: paired‑phonon, hydrodynamic, and empirical. Provide w on a uniform r‑grid spanning the interatomic separation range used in the HNC calculation. Columns: `r`, `w_paired_phonon`, `w_hydrodynamic`, `w_empirical`.

3. **condensate_fraction_table.csv** – The condensate fraction n(T) for all three dispersion models at each of the ten temperatures listed above. Columns: `T`, `n_paired_phonon`, `n_hydrodynamic`, `n_empirical`.

All numerical results must be dimensionless where indicated. Reproduce the results by faithfully implementing the described theory and numerical integrations; do not rely on tabulated values from the paper.

## Assets

- Lennard-Jones (6-12) potential parameters for 4He
- Experimental phonon-roton dispersion relation ε(k) for liquid 4He from Cowley & Woods (1971): 10.1139/p71-023

## Workflow steps

### Step 1: Self-consistent paired-phonon HNC ground-state calculation
- Role: process
- Action: Perform self-consistent paired-phonon analysis with hypernetted-chain (HNC) closure to obtain the optimal Jastrow factor f(r) and the static structure factor S(k) for liquid 4He at density ρ=0.0218 Å⁻³ using the Lennard-Jones (6-12) potential.
- Evidence: `/app/outputs/hinc_results_log.txt`

### Step 2: Load experimental dispersion relation
- Role: process
- Action: Retrieve the experimental phonon-roton dispersion relation ε_e(k) from Cowley & Woods (1971). Digitize the published table and interpolate to obtain ε_e(k) on a suitable k‑grid.
- Evidence: none

### Step 3: Compute excitation number ν(T) for empirical approximation
- Role: scored
- Action: Using the Bose-Einstein occupation factor integrated over k with the empirical dispersion, compute the number of excitations per particle ν(T) at the ten temperatures T = 0.2, 0.6, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.4, 3.0 K. Output the table.
- Output file: `/app/outputs/excitation_number_table.csv`
- Format: csv
- Contract: CSV with header: T,nu_empirical
- Scoring: scored by hidden verifier

### Step 4: Compute thermal correlation w(r,T) at T=1.4 K for three models
- Role: scored
- Action: For each of the three dispersion models (paired-phonon / Bijl-Feynman from S(k), hydrodynamic linear, empirical), compute the thermal correlation function w(r,T) at T=1.4 K using the paired-phonon model formulas for the thermal factor. Output the r‑grid and the three curves.
- Output file: `/app/outputs/thermal_correlation_function_data.csv`
- Format: csv
- Contract: CSV with header: r,w_paired_phonon,w_hydrodynamic,w_empirical
- Scoring: scored by hidden verifier

### Step 5: Compute condensate fraction n(T) for all temperatures and models
- Role: scored (load-bearing)
- Action: Construct the finite-temperature pair factor f(r,T) from the optimal f(r) and the thermal correlation w(r,T), the finite-temperature structure factor, and the correlation functions ξ and η. Compute the condensate fraction n(T) using the diagrammatic cluster expression Q(T) with the three-term approximation (Q1, Q2, Q3), where Q3 uses the convolution approximation for the three-body term. Compute n(T) for each of the three dispersion models at the ten temperatures.
- Output file: `/app/outputs/condensate_fraction_table.csv`
- Format: csv
- Contract: CSV with header: T,n_paired_phonon,n_hydrodynamic,n_empirical
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/excitation_number_table.csv`
- `/app/outputs/thermal_correlation_function_data.csv`
- `/app/outputs/condensate_fraction_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### excitation_number_table.csv
- path: `/app/outputs/excitation_number_table.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: ν(T) for the empirical dispersion approximation; compared to the paper's Table 1 with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T`, `nu_empirical`
  - `units`:
    - `T`: K
    - `nu_empirical`: dimensionless

### thermal_correlation_function_data.csv
- path: `/app/outputs/thermal_correlation_function_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Thermal correlation curves at T=1.4 K; structural check verifies that w_paired_phonon is largest at small r and that w_empirical shows a roton-related peak.
- schema:
  - `type`: table
  - `required_columns`: `r`, `w_paired_phonon`, `w_hydrodynamic`, `w_empirical`
  - `units`:
    - `r`: Å
    - `w_paired_phonon`: dimensionless
    - `w_hydrodynamic`: dimensionless
    - `w_empirical`: dimensionless

### condensate_fraction_table.csv
- path: `/app/outputs/condensate_fraction_table.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Condensate fraction n(T) for the three dispersion models; compared to the paper's Table 2 with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T`, `n_paired_phonon`, `n_hydrodynamic`, `n_empirical`
  - `units`:
    - `T`: K
    - `n_paired_phonon`: dimensionless
    - `n_hydrodynamic`: dimensionless
    - `n_empirical`: dimensionless

Notes: The ground-state HNC/paired-phonon calculation is a required process step; its output is used in downstream steps. Standard constants (ℏ, k_B, He mass, sound speed) are assumed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "excitation_number_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "nu_empirical"
        ],
        "units": {
          "T": "K",
          "nu_empirical": "dimensionless"
        }
      },
      "description": "ν(T) for the empirical dispersion approximation; compared to the paper's Table 1 with tolerance."
    },
    {
      "file": "thermal_correlation_function_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "w_paired_phonon",
          "w_hydrodynamic",
          "w_empirical"
        ],
        "units": {
          "r": "Å",
          "w_paired_phonon": "dimensionless",
          "w_hydrodynamic": "dimensionless",
          "w_empirical": "dimensionless"
        }
      },
      "description": "Thermal correlation curves at T=1.4 K; structural check verifies that w_paired_phonon is largest at small r and that w_empirical shows a roton-related peak."
    },
    {
      "file": "condensate_fraction_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "n_paired_phonon",
          "n_hydrodynamic",
          "n_empirical"
        ],
        "units": {
          "T": "K",
          "n_paired_phonon": "dimensionless",
          "n_hydrodynamic": "dimensionless",
          "n_empirical": "dimensionless"
        }
      },
      "description": "Condensate fraction n(T) for the three dispersion models; compared to the paper's Table 2 with tolerance."
    }
  ],
  "notes": "The ground-state HNC/paired-phonon calculation is a required process step; its output is used in downstream steps. Standard constants (ℏ, k_B, He mass, sound speed) are assumed."
}
```

## How you are scored
A hidden verifier will independently score each of the three output files against the expected output contract. The verifier does not look at intermediate console output; it only reads the submitted CSV files. The scoring weights are distributed across the stages, with the **condensate fraction table** carrying the largest share because it represents the main headline result. The **excitation number table** and the **thermal correlation curves** each carry a smaller but meaningful weight.

For each scored file the verifier checks that the file is present, correctly formatted, and contains the required columns and data types. It then compares the submitted values (or derived properties) against a predefined reference, applying appropriate tolerances for numerical discrepancies that arise from legitimate differences in implementation, integration grids, or discretization. The thermal correlation curves are additionally subjected to a lightweight structural audit: the verifier checks that the curves exhibit the physically expected relative magnitudes and features (e.g., which model gives the largest correlation at short distance, and whether the empirical curve shows a roton‑related structure).

Simply reporting a number that matches a known published value, without performing the actual HNC calculation and numerical integrations, will not satisfy the verifier because the scoring depends on the correct execution of the full pipeline as specified in the workflow steps. The final reward is a number between 0 and 1 that reflects how well the submitted artifacts fulfill the contract.
