# Monte Carlo Simulation of a Sine-Gordon Solid-on-Solid Model for Preroughening and Roughening Transitions

## Problem background
Crystal surfaces can undergo a succession of disordering transitions: preroughening, where the outermost layer disorders while the surface remains macroscopically flat, and roughening, where the surface delocalizes and wanders freely. A modified sine-Gordon solid-on-solid (SOS) model with temperature-dependent pinning potentials provides a framework in which both types of transitions can occur. This task uses Monte Carlo simulations of this SOS Hamiltonian to quantify the finite-size scaling of interface width fluctuations, the behavior of a sublattice order parameter and its susceptibility, and the thermal evolution of roughness parameters that characterize the surface phases.

## Approach
The SOS Hamiltonian consists of a nearest-neighbor Gaussian coupling that penalises height differences, together with a temperature-dependent logarithmic pinning potential that encourages integer or half-integer heights depending on the coefficients. Two parameter sets (Model A and Model B) are investigated, differing in the preroughening temperature. Metropolis Monte Carlo simulations are performed on square lattices with periodic boundary conditions, varying system size and temperature. The observables recorded are: (i) the mean-square height fluctuation δh² = ⟨(h_x − h_bar)²⟩, used to examine the interface width dependence on system size; (ii) the sublattice order parameter P = ⟨(1/N)|∑_x exp(iπ h_x)|⟩ and its susceptibility χ_P, which reflect surface ordering; (iii) the height-height radial correlation function G(r), fitted to a logarithmic form to extract the roughness strength K and correlation parameter X, which characterise surface roughness and critical behavior. Simulations are run with a tuned acceptance ratio and long enough sweeps to ensure equilibrium.

## Reproduction target
Compute the following artifacts and submit them as CSV files:

- Mean-square height fluctuation δh² at the respective preroughening temperatures (t = 0.5 for Model A, t = 0.25 for Model B) for square lattices of size L = 24, 48, 72, 96. Analyse the system-size dependence of δh² (logarithmic growth vs saturation).
- Order parameter P and susceptibility χ_P as functions of temperature for both models on a 72×72 lattice (optionally also L=48) over a temperature range from t=0.3 to 1.2 (at least 10 points). Identify and characterise any prominent features such as dips or peaks.
- For Model A on a 72×72 lattice, extract the roughness strength K and correlation parameter X by fitting the height-height correlation function to the form −(K/2) ln(r^{−2} + X^{−2}) + C at several temperatures across the same range. Determine whether K crosses the universal roughening value 2/π² and describe the temperature dependence of X.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Mean-square height difference δh² at preroughening
- Role: scored (load-bearing)
- Action: Implement the SOS Hamiltonian given in the paper with parameters for Model A (C/k=0.5, kT_PR/J=0.5, y4/J=0.1) and Model B (C/k=0.5, kT_PR/J=0.25, y4/J=0.1). Run Metropolis Monte Carlo simulations on square lattices of sizes L=24, 48, 72, 96 with periodic boundary conditions at the respective PR temperatures (t=0.5 for A, t=0.25 for B). For each (model, L), compute the mean-square height fluctuation δh² = ⟨(h_x - ar{h})²⟩ using the converged equilibrium configurations. The acceptance ratio should be tuned to ~50% and sufficient sweeps (≥10⁶) must be used. Write the final δh² values to the output file.
- Output file: `/app/outputs/delta_h2_data.csv`
- Format: csv
- Contract: Columns: model (string, 'A' or 'B'), L (integer), delta_h2 (float). One row per (model, L).
- Scoring: scored by hidden verifier

### Step 2: Order parameter P and susceptibility χ_P vs temperature
- Role: scored
- Action: For both Model A and Model B, perform MC simulations on square lattices of size L=72 over a temperature range from t=0.3 to 1.2 (at least 10 evenly spaced points). Optionally also run L=48 for finite-size comparison. At each temperature, compute the sublattice order parameter P = ⟨(1/N)|∑_x exp(iπ h_x)|⟩ and the susceptibility χ_P = N (⟨P²⟩ - ⟨P⟩²). Average over at least 10⁶ sweeps after equilibration. Write the results to the output file.
- Output file: `/app/outputs/order_parameter_data.csv`
- Format: csv
- Contract: Columns: model (string, 'A' or 'B'), t (float), L (integer), P (float), chi_P (float). One row per temperature per L.
- Scoring: scored by hidden verifier

### Step 3: Roughness parameters K and X from height-height correlations
- Role: scored
- Action: For Model A on a 72×72 lattice, run MC simulations at multiple temperatures between t=0.3 and 1.2 (at least the same grid as order parameter). For each temperature, compute the radial correlation function G(|x|) = ⟨(h_x − h_0)²⟩ averaged over all sites and directions. Fit the profile to the form G(r) ≃ −(K/2) ln(r^{−2} + X^{−2}) + C using a robust non-linear least-squares procedure. Record the fitted parameters K, X, and C for every temperature.
- Output file: `/app/outputs/K_X_data.csv`
- Format: csv
- Contract: Columns: t (float), L (integer, expected 72), K (float), X (float), C (float). One row per temperature.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_h2_data.csv`
- `/app/outputs/order_parameter_data.csv`
- `/app/outputs/K_X_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_h2_data.csv
- path: `/app/outputs/delta_h2_data.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Finite-size scaling of the mean-square height fluctuation δh² at the preroughening temperature.
- schema:
  - `type`: table
  - `required_columns`: `model`, `L`, `delta_h2`

### order_parameter_data.csv
- path: `/app/outputs/order_parameter_data.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Temperature evolution of the sublattice order parameter P and susceptibility χ_P.
- schema:
  - `type`: table
  - `required_columns`: `model`, `t`, `L`, `P`, `chi_P`

### K_X_data.csv
- path: `/app/outputs/K_X_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fitted roughness strength K and correlation parameter X for Model A on L=72.
- schema:
  - `type`: table
  - `required_columns`: `t`, `L`, `K`, `X`, `C`

Notes: Only the SOS model results are required; the dual Coulomb gas and its dielectric constant are excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_h2_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "L",
          "delta_h2"
        ]
      },
      "description": "Finite-size scaling of the mean-square height fluctuation δh² at the preroughening temperature."
    },
    {
      "file": "order_parameter_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "t",
          "L",
          "P",
          "chi_P"
        ]
      },
      "description": "Temperature evolution of the sublattice order parameter P and susceptibility χ_P."
    },
    {
      "file": "K_X_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "t",
          "L",
          "K",
          "X",
          "C"
        ]
      },
      "description": "Fitted roughness strength K and correlation parameter X for Model A on L=72."
    }
  ],
  "notes": "Only the SOS model results are required; the dual Coulomb gas and its dielectric constant are excluded."
}
```

## How you are scored
A hidden verifier evaluates each scored artifact independently. Your CSV files are read and the reported quantities are compared to expected physical relationships and to benchmark values derived from the reference study, using tolerances that allow for statistical noise and implementation differences. The three workflow stages carry pre‑defined weights that are combined into an overall reward between 0 and 1. A high score requires correctly implemented simulations that produce the right trends and values; simply reporting numbers without the underlying computations will not succeed.
