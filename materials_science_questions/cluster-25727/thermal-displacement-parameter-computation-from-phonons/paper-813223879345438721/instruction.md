# Temperature dependence of multiphonon absorption from independent Morse oscillators

## Problem background
Solid insulators absorb infrared light at frequencies far above their maximum lattice frequency through multiphonon processes, where several vibrational quanta combine to absorb a single photon. Simple harmonic-oscillator models predict a temperature dependence α ∝ T^{n-1} (with n the number of phonons needed), i.e., a strong increase with temperature. However, experimental measurements on alkali halides show a much weaker temperature dependence, indicating that anharmonicity of the lattice vibrations is essential. The Morse potential, which is exactly solvable in quantum mechanics and intrinsically anharmonic, offers a way to model such absorption. This task implements a model in which the solid is treated as an assembly of independent, non-rotating Morse oscillators whose fundamental frequencies follow a Debye spectrum, and it computes the temperature-dependent absorption coefficient for KCl at a fixed photon energy.

## Approach
The solid is approximated by a gas of diatomic Morse oscillators. Each oscillator has energy levels given by the Morse spectrum and transition probabilities between any two levels m and m+Δ are obtained from the exact dipole matrix elements. Absorption of a photon of energy E_l is possible if there exists a pair of levels whose energy difference equals E_l and the oscillator frequency ω satisfies the energy conservation condition. The model then averages over the Boltzmann-weighted initial states and integrates over a Debye frequency distribution g(ω) ∝ ω² from 0 to ω_max, with the dissociation energy D held constant across frequencies.

In the high-temperature regime (temperatures well above the ground state but far below dissociation), the partition function and the population difference factor simplify considerably, leading to a closed-form double sum over the level separation Δ (from 1 upward) and the initial level m. Energy conservation selects a specific oscillator frequency ω* for each (m,Δ) pair, and contributions from unphysical frequencies (outside the band or complex) are discarded. The total absorption coefficient α_tot for a given temperature T and photon energy E_l is obtained by performing this double sum, using the KCl material parameters (ω_max, D, reduced mass μ, derived Morse parameter k_min) and the normalized photon energy y = E_l/(ℏ ω_max).

For the specific case of KCl at a photon wavelength of 10.6 μm (y = 3.36), α_tot is computed numerically for a grid of at least 10 temperatures spanning 300–1000 K. The results are written to a CSV file. The power-law exponent j in α ∝ T^j is then determined by fitting log₁₀(α) = j log₁₀(T) + constant to the 400–800 K portion of the data.

## Reproduction target
Implement the model described in the approach. Compute the total absorption coefficient α_tot for KCl at a normalized photon energy y = 3.36 (corresponding to a wavelength of 10.6 μm) for at least 10 temperatures in the range 300–1000 K. Write the results to the file `/app/outputs/absorption_vs_temperature.csv` with columns `T_K` (temperature in Kelvin) and `alpha` (absorption in arbitrary units). The CSV will be used to extract the power-law exponent j that describes the temperature dependence of absorption in the 400–800 K interval.

## Assets
No external datasets, models, or pre-built software are required. All necessary physical constants and the KCl-specific parameters (ω_max = 0.0342 eV, D = 4.35 eV, μ = 18.4 amu, k_min = 505) are provided in the workflow steps. The implementation can be completed using standard scientific Python libraries (numpy, scipy).

## Workflow steps

### Step 1: Implement the model and prepare KCl parameters
- Role: process
- Action: Implement the numerical evaluation of the closed-form total absorption formula for a system of independent Morse oscillators with a Debye frequency distribution, using the high-temperature approximation. Set the KCl material parameters: maximum lattice frequency ω_max=0.0342 eV, dissociation energy D=4.35 eV, reduced mass μ=18.4 amu, and the derived Morse parameter k_min=505.
- Evidence: none

### Step 2: Generate absorption vs temperature for KCl at 10.6 μm
- Role: scored (load-bearing)
- Action: Using the model from step_01, compute the total absorption α_tot for KCl at a normalized photon energy y=3.36 (corresponding to 10.6 μm) over a grid of temperatures covering at least 10 points from 300 K to 1000 K. Write the results to absorption_vs_temperature.csv.
- Output file: `/app/outputs/absorption_vs_temperature.csv`
- Format: csv
- Contract: Header: T_K,alpha (T_K in Kelvin, alpha in arbitrary units).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/absorption_vs_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### absorption_vs_temperature.csv
- path: `/app/outputs/absorption_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Absorption coefficient for KCl at 10.6 μm vs temperature, to be used by the checker to fit a power-law exponent and compare to the paper's reported value.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `alpha`
  - `units`:
    - `T_K`: Kelvin
    - `alpha`: arbitrary units

Notes: The checker will perform a log-log linear regression on the 400-800 K portion of the CSV to extract the exponent, and compare it to the hidden gold with a linear tolerance. No alternative scoring artifacts are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "absorption_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "alpha"
        ],
        "units": {
          "T_K": "Kelvin",
          "alpha": "arbitrary units"
        }
      },
      "description": "Absorption coefficient for KCl at 10.6 μm vs temperature, to be used by the checker to fit a power-law exponent and compare to the paper's reported value."
    }
  ],
  "notes": "The checker will perform a log-log linear regression on the 400-800 K portion of the CSV to extract the exponent, and compare it to the hidden gold with a linear tolerance. No alternative scoring artifacts are required."
}
```

## How you are scored
Your submission is evaluated solely on the quality of the artifact `/app/outputs/absorption_vs_temperature.csv`. A hidden verifier reads this file, validates that it contains valid `T_K` and `alpha` columns with at least 10 rows covering 300–1000 K, then performs a linear regression on log10(alpha) vs log10(T) for points with T_K between 400 and 800 K. The slope of this regression is the exponent j. The verifier compares the extracted j to a hidden reference value and assigns a reward of 1.0 if |j − j_ref| is within a tolerance, decreasing linearly to 0 outside that tolerance. If fewer than three data points fall in the fitting range, the reward is 0. No other artifacts or intermediate steps contribute to the score. You must perform a genuine numerical computation; reporting a number without producing the corresponding CSV will not earn credit.
