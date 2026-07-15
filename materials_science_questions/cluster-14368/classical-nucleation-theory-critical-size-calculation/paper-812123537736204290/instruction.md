# Nucleation Time Scale and Required Mass-Loss Rates for T Tauri Envelopes

## Problem background
T Tauri stars are young pre-main-sequence stars that eject mass into their surroundings, forming expanding circumstellar envelopes. As the ejected gas expands and cools, it may become supersaturated in carbon, potentially forming solid graphite grains. The nucleation of graphite depends on the local density and temperature, which are set by the stellar mass-loss rate and the expansion dynamics. This task uses the classical Becker-Döring theory of homogeneous nucleation to compute the nucleation time scale of graphite, and compares it with the expansion time scale of the stellar wind. By requiring that nucleation occurs somewhere along the expansion (i.e., the nucleation time is shorter than the expansion time), one can determine the minimum mass-loss rate needed for appreciable graphite formation. The goal is to compute this required mass-loss rate for six T Tauri stars with known radii and surface outflow velocities, and to verify the nucleation model by computing the nucleation time at a set of test density-temperature points.

## Approach
The nucleation time scale τ_n(ρ,T) is computed from the Becker-Döring theory for a carbon-rich gas composed only of H, He, and C. The key input parameters are: carbon mass fraction X_C = 0.01, sticking probability α = 1, molecular volume Ω = 9×10⁻²⁴ cm³, surface energy σ = 1×10⁸ erg cm⁻², and the vapor pressure constants γ = 3.71×10⁴ and δ = 14.1 (c.g.s. units). The super-saturation ratio S, the critical cluster size, the nucleation rate J, and finally τ_n = n_C/(g* J) are evaluated following the standard formalism. The expanding envelope is modeled as spherical, steady, and adiabatic, with two limiting velocity laws: (A) constant velocity v = v₀, and (B) velocity proportional to distance v ∝ R. The continuity equation, together with the adiabatic relation d ln T / d ln ρ = 2/3 and a surface temperature T₀ = 4000 K, determines the density and temperature profiles. The expansion time scale τ_exp is derived for each case. For a given star, defined by its radius R₀ and surface velocity v₀, the mass-loss rate A controls the density level. By scanning along the expansion path and checking whether τ_n < τ_exp ever holds, the minimum mass-loss rate A_required that permits nucleation can be found for both velocity cases. The observed mass-loss rate A_obs is provided for each star (extracted from the literature), but it is not used in the computation of A_required; it serves only for context.

## Reproduction target
The task has two scored outputs:
1. Verification of the nucleation model: using your τ_n function, compute the nucleation time for a list of test (T, ρ) points provided in the file `test_points.csv`. Output the results in `tau_n_values.csv` with columns T (K), rho (g cm⁻³), tau_n (seconds). This step confirms that the nucleation physics is correctly implemented.
2. Required mass-loss rates: for each of the six T Tauri stars (RY Tau, T Tau, GW Ori, RU Lup, AS 209, LkHα120) whose stellar parameters are given in `stellar_data.csv`, compute the minimum mass-loss rate A_required (in units of 10⁻⁷ M_⊙ yr⁻¹) under velocity Case A (v = constant) and Case B (v ∝ R). Output the file `required_mass_loss_rates.csv` containing the star name, stellar radius, surface velocity, the observed mass-loss rate (copied from the input), and your computed required rates for both cases. Six data rows are expected.
All intermediate steps (nucleation function, expansion model, search routine) are required process steps that must be executed; their correctness is indirectly verified by the scoring of these two artifacts.

## Assets

- T Tauri star parameters
- Test points for nucleation time scale
- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Implement nucleation rate and time scale
- Role: process
- Action: Implement functions that compute the homogeneous nucleation time scale τ_n(ρ,T) for graphite using Becker–Döring theory. Use the given parameters: carbon mass fraction X_C=0.01, sticking probability α=1, molecular volume Ω=9e-24 cm³, surface energy σ=1e8 erg/cm², vapor pressure law log10 P_v = -γ/T + δ with γ=3.71e4, δ=14.1 (c.g.s. units), and physical constants (Boltzmann constant, carbon atom mass). The implementation should calculate S, P_v, ΔG*, r*, Z, nucleation rate J, and finally τ_n = n_C/(g* J).
- Evidence: none

### Step 2: Verify nucleation time scale at test points
- Role: scored (load-bearing)
- Action: Using the τ_n function from step_01, read the file test_points.csv (columns T, rho) and compute τ_n for each row. Output tau_n_values.csv with columns T, rho, tau_n.
- Output file: `/app/outputs/tau_n_values.csv`
- Format: csv
- Contract: CSV with columns: T (float, K), rho (float, g cm^-3), tau_n (float, seconds). Each row corresponds to one test point.
- Scoring: scored by hidden verifier

### Step 3: Implement expansion model and mass‑loss rate search
- Role: process
- Action: Implement the spherical, steady, adiabatic expansion model. Define the expansion time scales for velocity Case A (v=constant) and Case B (v∝R), the adiabatic relation T=T0 (ρ/ρ0)^(2/3) with T0=4000 K, and the density profile derived from continuity. For a given star (R0, v0) and a trial mass‑loss rate, determine whether τ_n ≤ τ_exp can be satisfied somewhere along the expansion. Write a search routine that finds the minimum A (in 10^{-7} M_sun/yr) for which nucleation becomes possible.
- Evidence: none

### Step 4: Compute required mass‑loss rates for six T Tauri stars
- Role: scored (load-bearing)
- Action: Using the search procedure from step_03 and the stellar parameters from stellar_data.csv, compute the minimum mass‑loss rate A (in 10^{-7} M_sun/yr) for each star under Case A (v=constant) and Case B (v∝R). Output required_mass_loss_rates.csv with columns: Star, R0_Rsun, v0_kms, A_obs_1e-7Msun_per_yr (observed rate, copied from input), A_required_caseA_1e-7Msun_per_yr, A_required_caseB_1e-7Msun_per_yr.
- Output file: `/app/outputs/required_mass_loss_rates.csv`
- Format: csv
- Contract: CSV with columns: Star (string), R0_Rsun (float, solar radii), v0_kms (float, km/s), A_obs_1e-7Msun_per_yr (float), A_required_caseA_1e-7Msun_per_yr (float), A_required_caseB_1e-7Msun_per_yr (float). Six data rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tau_n_values.csv`
- `/app/outputs/required_mass_loss_rates.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tau_n_values.csv
- path: `/app/outputs/tau_n_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Nucleation time scale computed at specified test points; compared to hidden reference values with an appropriate relative/absolute tolerance.
- schema:
  - `required_columns`: `T`, `rho`, `tau_n`
  - `units`:
    - `T`: K
    - `rho`: g cm^-3
    - `tau_n`: seconds

### required_mass_loss_rates.csv
- path: `/app/outputs/required_mass_loss_rates.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Required mass‑loss rates for six T Tauri stars under two velocity laws; compared to hidden reference values with a relative tolerance (e.g., 10%) or absolute tolerance in log10(A).
- schema:
  - `required_columns`: `Star`, `R0_Rsun`, `v0_kms`, `A_obs_1e-7Msun_per_yr`, `A_required_caseA_1e-7Msun_per_yr`, `A_required_caseB_1e-7Msun_per_yr`
  - `units`:
    - `R0_Rsun`: solar radii
    - `v0_kms`: km/s
    - `A_obs_1e-7Msun_per_yr`: 10^{-7} M_sun/yr
    - `A_required_caseA_1e-7Msun_per_yr`: 10^{-7} M_sun/yr
    - `A_required_caseB_1e-7Msun_per_yr`: 10^{-7} M_sun/yr

Notes: Hidden reference values are derived from the paper's published results or independently recomputed. Scoring uses tolerances chosen to absorb legitimate numerical differences while requiring a correct implementation of the physics.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tau_n_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "T",
          "rho",
          "tau_n"
        ],
        "units": {
          "T": "K",
          "rho": "g cm^-3",
          "tau_n": "seconds"
        }
      },
      "description": "Nucleation time scale computed at specified test points; compared to hidden reference values with an appropriate relative/absolute tolerance."
    },
    {
      "file": "required_mass_loss_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "Star",
          "R0_Rsun",
          "v0_kms",
          "A_obs_1e-7Msun_per_yr",
          "A_required_caseA_1e-7Msun_per_yr",
          "A_required_caseB_1e-7Msun_per_yr"
        ],
        "units": {
          "R0_Rsun": "solar radii",
          "v0_kms": "km/s",
          "A_obs_1e-7Msun_per_yr": "10^{-7} M_sun/yr",
          "A_required_caseA_1e-7Msun_per_yr": "10^{-7} M_sun/yr",
          "A_required_caseB_1e-7Msun_per_yr": "10^{-7} M_sun/yr"
        }
      },
      "description": "Required mass‑loss rates for six T Tauri stars under two velocity laws; compared to hidden reference values with a relative tolerance (e.g., 10%) or absolute tolerance in log10(A)."
    }
  ],
  "notes": "Hidden reference values are derived from the paper's published results or independently recomputed. Scoring uses tolerances chosen to absorb legitimate numerical differences while requiring a correct implementation of the physics."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently computes reference values for each scored artifact. For `tau_n_values.csv`, the checker recomputes τ_n for the same test points using a reference implementation of the Becker-Döring model and compares your values within a predetermined tolerance. For `required_mass_loss_rates.csv`, the checker recomputes the expected mass-loss rates from the provided stellar parameters using the paper's derived linear approximations, and checks that your submitted A_required values fall within an allowed margin (typically a relative tolerance or an absolute tolerance in log₁₀ A). The verification step (step 2) and the final mass‑loss table (step 4) each carry a portion of the total reward; the final reward is the weighted sum (weights are specified in the hidden grading specification). To earn full credit, your work must faithfully implement the physical models and search procedure described in the instructions, so that the computed nucleation times and mass‑loss rates match the hidden reference. Simply reporting the paper's published numbers without performing the computations will not pass—the verifier checks the values derived from your implementation.
