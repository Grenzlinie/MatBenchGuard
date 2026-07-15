# Monte Carlo Simulation of Temperature-Dependent Carrier Dynamics in THz Quantum Cascade Lasers

## Problem background
Terahertz quantum cascade lasers (QCLs) suffer from performance degradation as the lattice temperature increases. Understanding the microscopic carrier dynamics is essential for improving high-temperature operation. This task investigates a resonant-phonon THz QCL with a vertical radiative transition design using an ensemble Monte Carlo simulation that includes electron–LO-phonon and electron–electron scattering. The goal is to compute the temperature-dependent intersubband scattering rates and subband lifetimes to determine the dominant carrier relaxation channels.

## Approach
Simulate the electron transport through the active region of a THz QCL. First, solve the one-dimensional Schrödinger–Poisson equations self-consistently for the given vertical-design layer sequence under an applied bias to obtain the lowest four subband energies and wavefunctions. Second, precompute energy-dependent transition rates for electron–LO-phonon and electron–electron scattering among these subbands, using a maximum-scattering-probability approximation for electron–electron interactions where the maximum of the transition matrix element is employed so that the scattering probability depends only on the partner electron distribution. Third, run an ensemble Monte Carlo simulation with periodic boundary conditions and the Pauli exclusion principle at several fixed lattice temperatures and a constant electric field, evolving the electron system to steady state. Finally, extract from the steady-state statistics the intersubband scattering rates (τ₄₃)⁻¹ and (τ₄₂)⁻¹, the upper and lower laser level lifetimes τ₄ and τ₃, and the fraction of the 4→3 transition that is mediated by electron–LO-phonon scattering.

## Reproduction target
Produce a CSV file with temperature-dependent intersubband scattering rates (τ₄₃)⁻¹, (τ₄₂)⁻¹, the upper laser level lifetime τ₄, the lower laser level lifetime τ₃, and the fraction of the 4→3 transition mediated by electron–LO-phonon scattering, for lattice temperatures of 25 K, 100 K, and 200 K. This data must be written to the file `/app/outputs/scattering_rates_lifetimes.csv` following the output contract specification.

## Assets

- GaAs/Al0.15Ga0.85As material parameters
- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Electronic structure calculation
- Role: process
- Action: Implement a one-dimensional self-consistent Schrödinger-Poisson solver for the vertical design THz QCL active region (layer sequence: 48/96/20/74/42/161 Å, Al0.15Ga0.85As barriers in bold, GaAs wells; doping 3.0×10¹⁰ cm⁻² in the depopulation well). Apply a bias of 60 mV per module. Compute the lowest four subband energies and wavefunctions.
- Evidence: none

### Step 2: Scattering table preparation
- Role: process
- Action: Using the wavefunctions and energies from Step 1, compute electron-LO-phonon and electron-electron scattering matrix elements. Construct a scattering table of rates for all transitions among the four subbands. For electron-electron scattering, implement the maximum-scattering-probability approximation where the rate Γ_{im,max}^{ee}(k₁) = (m* N_sub) / (2 ħ³ A) M_{im,max}² Σ_{j,k₂} f_j(k₂).
- Evidence: none

### Step 3: Monte Carlo simulation of electron transport
- Role: process
- Action: Implement an ensemble Monte Carlo simulator with 5000 electrons, periodic boundary conditions, and the Pauli exclusion principle. Use the scattering table from Step 2. Run steady-state simulations at lattice temperatures of 25 K, 100 K, and 200 K under the constant electric field corresponding to 60 mV/module. Run until steady state is reached and record subband occupations and scattering event statistics.
- Evidence: none

### Step 4: Extraction of scattering rates and lifetimes
- Role: scored (load-bearing)
- Action: From the steady-state Monte Carlo outputs, calculate (i) the intersubband scattering rate from subband 4 to subband 3, (τ₄₃)⁻¹; (ii) the intersubband scattering rate from subband 4 to subband 2, (τ₄₂)⁻¹; (iii) the upper laser level lifetime τ₄; (iv) the lower laser level lifetime τ₃; and (v) the fraction of the 4→3 transition mediated by electron-LO-phonon scattering. Report the results for lattice temperatures of 25 K, 100 K, and 200 K. Write the data to `/app/outputs/scattering_rates_lifetimes.csv`.
- Output file: `/app/outputs/scattering_rates_lifetimes.csv`
- Format: csv
- Contract: CSV with header: T_lattice,tau43_inv,tau42_inv,tau4,tau3,fraction_eLO_43. All columns numeric. Units: T_lattice (K), tau43_inv (ps⁻¹), tau42_inv (ps⁻¹), tau4 (ps), tau3 (ps), fraction_eLO_43 (dimensionless, range 0–1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/scattering_rates_lifetimes.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### scattering_rates_lifetimes.csv
- path: `/app/outputs/scattering_rates_lifetimes.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CSV with temperature-dependent scattering rates and lifetimes extracted from Monte Carlo simulation. Each row corresponds to a lattice temperature. The values are compared to paper's results with a relative tolerance.
- schema:
  - `columns`:
    - `T_lattice`: numeric (K)
    - `tau43_inv`: numeric (ps⁻¹)
    - `tau42_inv`: numeric (ps⁻¹)
    - `tau4`: numeric (ps)
    - `tau3`: numeric (ps)
    - `fraction_eLO_43`: numeric (0-1)

Notes: The verifier will compare these values against the paper's reported values with an appropriate tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "scattering_rates_lifetimes.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "columns": {
          "T_lattice": "numeric (K)",
          "tau43_inv": "numeric (ps⁻¹)",
          "tau42_inv": "numeric (ps⁻¹)",
          "tau4": "numeric (ps)",
          "tau3": "numeric (ps)",
          "fraction_eLO_43": "numeric (0-1)"
        }
      },
      "description": "CSV with temperature-dependent scattering rates and lifetimes extracted from Monte Carlo simulation. Each row corresponds to a lattice temperature. The values are compared to paper's results with a relative tolerance."
    }
  ],
  "notes": "The verifier will compare these values against the paper's reported values with an appropriate tolerance."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's artifact and combines them by weight into the final reward. The verifier compares the submitted CSV values against expected numerical targets with appropriate tolerances and also checks that the results satisfy expected physical trends (for example, a monotonic increase of (τ₄₃)⁻¹ with lattice temperature, and the dominance of electron–LO-phonon over electron–electron scattering in the 4→3 channel). Your score reflects both the numerical accuracy of the extracted rates/lifetimes and the consistency of the trends you report.
