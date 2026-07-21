# Finite-size scaling amplitudes for the 3D Ising model

## Problem background
Finite‑size scaling theory describes how thermodynamic properties of finite Ising lattices approach the behaviour of an infinite system at the critical point. For a simple‑cubic spin‑¹⁄₂ Ising model, the "pseudo‑ordering" temperature \(T_c(N)\) – usually identified with the maximum of the specific heat – is expected to shift with system size \(N\) according to \(\delta T_c = 1 - T_c(N)/T_c(\infty) \approx a N^{-\lambda}\), where \(\lambda\) is predicted to equal \(1/\nu\) (\(\nu \approx 0.64\) is the correlation‑length exponent). The magnetization \(M\) and susceptibility \(\chi\) should obey finite‑size scaling relations that involve the bulk critical exponents \(\beta \approx 0.312\) and \(\gamma \approx 1.25\). Monte Carlo simulations can test these predictions and determine the amplitude \(a\) of the temperature shift as well as the asymptotic amplitudes \(B\) (magnetization) and \(C_+\) (high‑temperature susceptibility). This task reproduces a minimal version of that study using single‑spin‑flip Metropolis dynamics and simple‑cubic lattices with periodic boundary conditions.

## Approach
The workflow implements a standard Monte Carlo analysis of finite‑size scaling. First, the Ising Hamiltonian \(\mathcal{H} = -J \sum_{\langle ij\rangle} \sigma_i \sigma_j\) (with \(\sigma_i = \pm 1\)) is simulated on \(N\times N\times N\) simple‑cubic lattices with periodic boundary conditions for several values of \(N\) using the Metropolis algorithm. For each \(N\) the temperature is scanned across the critical region around the known infinite‑lattice critical temperature \(T_c(\infty) = 0.221654\, J/k_B\). Time series of the total energy and magnetization are collected, and after thermalisation the mean energy, specific heat, magnetisation and susceptibility are computed as functions of temperature.

From the specific heat curve of each lattice, the finite‑size pseudotransition temperature \(T_c(N)\) is identified as the temperature at which the specific heat attains its maximum. The shift \(\delta T_c(N)\) is then fitted to the form \(\delta T_c = a N^{-\lambda}\) with \(\lambda\) fixed to \(1/\nu\) (\(\nu = 0.64\)) to obtain the amplitude \(a\).

Next, finite‑size scaling plots are constructed for the magnetization and the high‑temperature susceptibility using the scaled variables \(x = t N^{1/\nu}\) and \(t = |1 - T/T_c(\infty)|\). For the magnetisation, \(M N^{\beta/\nu}\) is plotted against \(x\), and in the large‑\(x\) (large \(t N^{1/\nu}\)) region the asymptotic behaviour \(M N^{\beta/\nu} \approx B\, x^{\beta}\) is used to extract \(B\). Similarly, for the susceptibility the quantity \(\chi N^{-\gamma/\nu}\) is plotted against \(x\), and the high‑temperature branch is fitted with \(\chi N^{-\gamma/\nu} \approx C_+\, x^{-\gamma}\) to obtain \(C_+\). All exponent values are taken from the standard 3D Ising model literature: \(\beta = 0.312\), \(\gamma = 1.25\), \(\nu = 0.64\). The implementation details (number of Monte Carlo steps, temperature grid, fitting ranges) are left to the solver, but the final amplitudes must be extracted as described.

## Reproduction target
The goal is to compute, from Monte Carlo simulations of the 3D Ising model with periodic boundary conditions and lattice sizes \(N = 4, 6, 8, 10, 14, 20\), three key quantities that characterise finite‑size scaling:

1. The amplitude \(a\) of the finite‑size shift of the specific‑heat peak temperature, obtained from the power‑law \(\delta T_c = a N^{-1/\nu}\).
2. The bulk finite‑size scaling amplitude \(B\) for the magnetisation, extracted from the large‑\(x\) limit of the scaling plot \(M N^{\beta/\nu}\) vs. \(t N^{1/\nu}\).
3. The high‑temperature susceptibility amplitude \(C_+\) from the corresponding scaling plot of \(\chi N^{-\gamma/\nu}\) vs. \(t N^{1/\nu}\).

All computations must use the known critical temperature \(T_c(\infty) = 0.221654\, J/k_B\) and the exponents \(\nu = 0.64\), \(\beta = 0.312\), \(\gamma = 1.25\). The intermediate pseudotransition temperatures \(T_c(N)\) must be saved as a CSV, and the final amplitudes saved as JSON files according to the exact formats specified in the workflow steps.

## Assets

- Python scientific computing environment

## Workflow steps

### Step 1: Monte Carlo simulation of Ising model
- Role: process
- Action: Implement single-spin-flip Metropolis Monte Carlo simulations for the S=1/2 simple-cubic Ising model with periodic boundary conditions for lattice sizes N = 4, 6, 8, 10, 14, 20. For each N, scan a temperature range covering the critical region around Tc=0.221654 (in units of J/k). Collect time series of energy and magnetization, and compute mean values and fluctuations to obtain specific heat and susceptibility as functions of T.
- Evidence: `/app/outputs/simulation_data.npz`

### Step 2: Extract pseudotransition temperatures
- Role: scored (load-bearing)
- Action: For each N, locate the temperature T at which the specific heat C(T) attains its maximum. Record T as Tc(N). Output a CSV with columns N and Tc.
- Output file: `/app/outputs/step_02_Tc_values.csv`
- Format: csv
- Contract: CSV with header 'N,Tc'. N integer, Tc float (temperature in units of J/k).
- Scoring: scored by hidden verifier

### Step 3: Fit finite-size shift amplitude a
- Role: scored (load-bearing)
- Action: Using the Tc(N) values and the known infinite-lattice critical temperature Tc(∞)=0.221654 and correlation-length exponent ν=0.64, compute δTc = 1 - Tc(N)/Tc(∞). Perform a power-law fit of the form δTc = a N^{-λ} with λ fixed to ν^{-1} (λ=1.5625) over the available N. Extract the amplitude a. Save a JSON object with key 'a' and optionally 'a_error'.
- Output file: `/app/outputs/step_04_fitted_a.json`
- Format: json
- Contract: JSON object with key 'a' (float) and optionally 'a_error' (float).
- Scoring: scored by hidden verifier

### Step 4: Extract bulk finite-size scaling amplitudes
- Role: scored (load-bearing)
- Action: Using the magnetization and susceptibility data from simulations, construct finite-size scaling plots for magnetization (M N^{β/ν} vs t N^{1/ν}) and high-temperature susceptibility (χ N^{-γ/ν} vs t N^{1/ν}), with β=0.312, ν=0.64, γ=1.25, and t = |1 - T/Tc(∞)|. From the large-x (large t N^{1/ν}) region, extract the asymptotic amplitudes B (for magnetization, from M N^{β/ν} ≈ B (t N^{1/ν})^{β}) and C+ (for susceptibility, from χ N^{-γ/ν} ≈ C+ (t N^{1/ν})^{-γ}). Save a JSON object with keys 'B' and 'Cplus'.
- Output file: `/app/outputs/step_06_scaling_amplitudes.json`
- Format: json
- Contract: JSON object with keys 'B' (float) and 'Cplus' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_Tc_values.csv`
- `/app/outputs/step_04_fitted_a.json`
- `/app/outputs/step_06_scaling_amplitudes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_Tc_values.csv
- path: `/app/outputs/step_02_Tc_values.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Pseudotransition temperatures from specific-heat peak positions.
- schema:
  - `type`: table
  - `required_columns`: `N`, `Tc`
  - `units`:
    - `N`: dimensionless
    - `Tc`: J/k (energy per Boltzmann constant)

### step_04_fitted_a.json
- path: `/app/outputs/step_04_fitted_a.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Amplitude a of finite-size shift of Tc.
- schema:
  - `type`: object
  - `required`:
    - `a`: float
  - `optional`:
    - `a_error`: float

### step_06_scaling_amplitudes.json
- path: `/app/outputs/step_06_scaling_amplitudes.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Bulk finite-size scaling amplitudes for magnetization (B) and susceptibility (C+).
- schema:
  - `type`: object
  - `required`:
    - `B`: float
    - `Cplus`: float

Notes: This task covers the minimal reproduction scope: Monte Carlo simulation, shift amplitude a, and bulk scaling amplitudes B and C+. Surface scaling and specific-heat scaling with background subtraction are excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_Tc_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "Tc"
        ],
        "units": {
          "N": "dimensionless",
          "Tc": "J/k (energy per Boltzmann constant)"
        }
      },
      "description": "Pseudotransition temperatures from specific-heat peak positions."
    },
    {
      "file": "step_04_fitted_a.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a": "float"
        },
        "optional": {
          "a_error": "float"
        }
      },
      "description": "Amplitude a of finite-size shift of Tc."
    },
    {
      "file": "step_06_scaling_amplitudes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "B": "float",
          "Cplus": "float"
        }
      },
      "description": "Bulk finite-size scaling amplitudes for magnetization (B) and susceptibility (C+)."
    }
  ],
  "notes": "This task covers the minimal reproduction scope: Monte Carlo simulation, shift amplitude a, and bulk scaling amplitudes B and C+. Surface scaling and specific-heat scaling with background subtraction are excluded."
}
```

## How you are scored
A hidden verifier inspects the artifacts you write for each scored step. It recomputes derived quantities where applicable, compares them against independently established reference values, and checks that intermediate data obey the expected physical trends (e.g., that the pseudotransition temperature decreases monotonically with increasing \(N\)). Each scored step contributes a portion of the total reward, which is the weighted sum of the individual step scores. Simply printing numbers that match the paper's published values is not sufficient; the verifier will assess the consistency of your simulation outputs with the finite‑size scaling predictions.
