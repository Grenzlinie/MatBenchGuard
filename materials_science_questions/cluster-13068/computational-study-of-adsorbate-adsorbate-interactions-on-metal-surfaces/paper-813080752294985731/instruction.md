# Adsorption isotherms with coverage-dependent repulsive interactions on a square lattice

## Problem background
The adsorption of ions on metal electrodes is often accompanied by lateral repulsive interactions that may weaken with coverage due to mutual depolarization (progressive discharge). While this idea has been invoked qualitatively in many studies, there has been no theoretical computation of the resulting adsorption isotherms that incorporates this effect directly. In this task, you will compute equilibrium adsorption isotherms for a lattice-gas model with coverage-dependent pair interactions, using both a mean-field approximation and exact Monte Carlo simulations. The model describes ions on a square lattice, with repulsive interactions that decrease quadratically with coverage up to a critical coverage, after which the electrostatic contribution vanishes. The isotherms will be evaluated for three distinct parameter sets, allowing you to explore how the interaction strength and discharge threshold affect the coverage vs. electrochemical potential relationship.

## Model definition

### Lattice and interactions
- The lattice is a square (100) surface of size L×L with periodic boundary conditions.
- Each site can be either empty (ci = 0) or occupied by an ion (ci = 1).
- The coverage θ is the fraction of occupied sites: θ = (1/L²) Σ_i c_i.
- The total interaction energy between two ions at sites i and j separated by a distance R_ij (in units of the lattice constant a, taken as a=1) is

  E_ij(θ) = ε_elec(θ) · f(R_ij) + ε_nn · δ_nn(i,j)

  where
  - ε_elec(θ) is the coverage‑dependent electrostatic energy scale (see below),
  - f(R) = 1 / R³  (for κ=0; the full screened form is given in the literature but we use κ=0 throughout this task),
  - ε_nn is the nearest‑neighbor interaction energy,
  - δ_nn(i,j) = 1 if i and j are nearest neighbours (distance = 1), and 0 otherwise.

  The elastic contribution ε_elas is zero for all cases in this task.

- The electrostatic energy scale ε_elec(θ) depends on the **global instantaneous coverage θ** and is given by

  ε_elec(θ) = ε_elec⁰ (1 − θ/θ_c)²   for θ < θ_c,
  ε_elec(θ) = 0                      for θ ≥ θ_c,

  where ε_elec⁰ is the value at zero coverage and θ_c is the critical coverage at which complete discharge occurs.

### System parameters and constants
- Temperature: T = 300 K.
- Boltzmann constant: k_B = 8.617333262145 × 10⁻⁵ eV/K.
- Thermal energy: k_B T = (k_B × 300) eV; you must calculate it from the above numbers.
- Zucker sum for a square lattice with κ=0: Σ_e = Σ = 8.977.
- Number of nearest neighbours on a square lattice: Z = 4.
- Monte Carlo lattice size: L = 30 (900 sites), with periodic boundary conditions.
- MC sampling: 200 Monte Carlo steps per site for equilibration, followed by 200 steps per site for averaging. One MC step per site consists of L² attempted insertions/deletions (one per site on average).

### Parameter sets to study
You will compute isotherms for three parameter sets:

| param_set | ε_elec⁰ (eV) | ε_nn (eV) | θ_c |
|-----------|--------------|-----------|-----|
| 1         | 0.1          | 0.02      | 0.4 |
| 2         | 0.3          | 0.02      | 0.4 |
| 3         | 0.1          | 0.02      | 0.2 |

For all sets: ε_elas = 0, κ = 0, T = 300 K.

## Mean‑field isotherm (Step 1)

In the mean‑field approximation (MFA), the equilibrium coverage θ satisfies

  Δμ = k_B T ln( θ / (1−θ) ) − g(θ) θ ,                                     (1)

or equivalently

  Δμ / (k_B T) = ln( θ / (1−θ) ) − [g(θ) / (k_B T)] θ .                    (2)

The function g(θ) (with units of energy) is obtained from the interaction parameters:

  g(θ) = Σ_e ε_elec(θ) + (1/2) Σ_e θ dε_elec/dθ + Z ε_nn .                 (3)

Substituting the explicit form of ε_elec(θ) and using ε_elas=0 gives:

  For θ < θ_c:
    g(θ) = Σ_e ε_elec⁰ (1 − θ/θ_c)(1 − 2θ/θ_c) + Z ε_nn .

  For θ ≥ θ_c:
    g(θ) = Z ε_nn .

The numerical values Σ_e, Z, ε_elec⁰, ε_nn, θ_c are given above.

### Step 1 task
For each of the three parameter sets, solve Eq. (2) over a range of θ from very small to very large (e.g., 0.001 to 0.999) to obtain the corresponding Δμ/(k_B T). You may also solve the equation the other way round: for a range of Δμ values, find the corresponding θ (this may require a root‑finding algorithm if hysteresis is present). Ensure that the sampling covers the full coverage range and captures any steep parts of the isotherm.

Save the results as a CSV file with the columns specified in the output contract.

## Monte Carlo simulation (Step 2)

### Grand‑canonical Monte Carlo with coverage‑dependent interactions and a finite-range cutoff
The simulation is performed on a 30×30 square lattice with periodic boundary conditions. The energy of a configuration {c_i} is

  E({c_i}) = (1/2) Σ_i Σ_{j≠i} c_i c_j E_ij(θ) ,

where E_ij(θ) is defined above and θ = (1/L²) Σ_i c_i is the **instantaneous** global coverage. Because the coupling strength depends on the current coverage, the interaction is effectively many‑body.

**Cutoff**: Following the literature on which this model is based, only pairs of sites whose distance R_ij is less than or equal to a cutoff radius R_cut are included in the energy sum; pairs with R_ij > R_cut are ignored. For the 30×30 lattice we use

  R_cut = 15  (half the box length).

This means you consider all distinct pairs within the minimum-image convention whose distance satisfies R_ij ≤ 15. Using the same cutoff as in the reference simulations ensures that your results can be meaningfully compared to published data.

**Update rule**: at every attempted move (insertion or deletion of a particle at a randomly chosen site), compute the current global coverage θ_curr, then evaluate the energy difference ΔE = E_after − E_before using that θ_curr. Accept the move with probability min(1, exp[−(ΔE − Δμ ΔN)/(k_B T)]), where ΔN = ±1. After accepting or rejecting the move, update the lattice and recompute the new global coverage.

**Distance convention**: use the minimum‑image convention with the 30×30 periodic box. Compute the Euclidean distance R_ij between sites i and j (in units of a), take f(R) = 1 / R³ for pairs with R_ij ≤ R_cut, and ignore the interaction (treat as zero) for R_ij > R_cut.

### Step 2 task
For each of the three parameter sets, run grand‑canonical MC at a series of Δμ/(k_B T) values. Choose a range that spans coverages from near 0 to near 1 (e.g., Δμ/(k_B T) from −3 to +2) with a step size small enough to resolve the isotherm shape.

**Scan protocol**: Perform a single scan for each parameter set. Start from an empty lattice at the most negative (lowest) Δμ. After the equilibration and averaging phases at that Δμ, use the final configuration as the initial state for the next, slightly higher Δμ. Continue this way through all chosen Δμ values. Label all rows with `scan = 'single'`.

At each Δμ, run 200 MC steps per site for equilibration, then 200 steps per site for averaging. One MC step per site consists of L² = 900 attempted insertions/deletions. Average the coverage over the averaging phase and record it in the output CSV.

Save the results as a CSV file with columns: `param_set`, `coverage`, `delta_mu`, `scan`.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_mfa_isotherms.csv`
- `/app/outputs/step_02_mc_isotherms.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_mfa_isotherms.csv
- path: `/app/outputs/step_01_mfa_isotherms.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Mean-field isotherm data used to verify self-consistency of the coverage-dependent lattice-gas model by recomputing the MFA equation from the reported values.
- schema:
  - `type`: table
  - `required_columns`: `param_set`, `coverage`, `delta_mu`, `epsilon_elec0`, `epsilon_nn`, `theta_c`, `T`
  - `units`:
    - `coverage`: dimensionless
    - `delta_mu`: kT (i.e., Δμ/(k_B T))
    - `epsilon_elec0`: eV
    - `epsilon_nn`: eV
    - `theta_c`: dimensionless
    - `T`: K

### step_02_mc_isotherms.csv
- path: `/app/outputs/step_02_mc_isotherms.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Monte Carlo simulation results of adsorption isotherms, checked against digitized reference data from the literature to validate the exact statistical-mechanical prediction.
- schema:
  - `type`: table
  - `required_columns`: `param_set`, `coverage`, `delta_mu`, `scan`
  - `units`:
    - `coverage`: dimensionless
    - `delta_mu`: kT
    - `scan`: string (one of 'forward', 'backward', 'single')

Notes: The MFA isotherm is verified by recomputing the mean-field equation from the submitted coverage and delta_mu values; the MC isotherm is verified by comparing coverage values to a hidden digitised reference under a tolerance that accounts for stochastic simulation spread. For the MC output, the scan protocol discussed above naturally produces the value `'single'` in the scan column; the reference data are not separated by scan direction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_mfa_isotherms.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "param_set",
          "coverage",
          "delta_mu",
          "epsilon_elec0",
          "epsilon_nn",
          "theta_c",
          "T"
        ],
        "units": {
          "coverage": "dimensionless",
          "delta_mu": "kT",
          "epsilon_elec0": "eV",
          "epsilon_nn": "eV",
          "theta_c": "dimensionless",
          "T": "K"
        }
      },
      "description": "Mean-field isotherm data used to verify self-consistency of the coverage-dependent lattice-gas model by recomputing the MFA equation from the reported values."
    },
    {
      "file": "step_02_mc_isotherms.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "param_set",
          "coverage",
          "delta_mu",
          "scan"
        ],
        "units": {
          "coverage": "dimensionless",
          "delta_mu": "kT",
          "scan": "string"
        }
      },
      "description": "Monte Carlo simulation results of adsorption isotherms, checked against digitized reference data from the literature to validate the exact statistical-mechanical prediction."
    }
  ],
  "notes": "The MFA isotherm is verified by recomputing the mean-field equation from the submitted coverage and delta_mu values; the MC isotherm is verified by comparing coverage values to a hidden digitised reference under a tolerance that accounts for stochastic simulation spread."
}
```

## How you are scored
The hidden verifier will score each output independently and combine them into a final reward between 0 and 1. For the mean-field isotherm (step_01), the verifier will recompute the mean-field condition from your reported (θ, Δμ) pairs: it will calculate the left-hand side of the implicit equation and compare it to the reported Δμ; a correct solution must satisfy the equation within the numerical tolerance expected for this problem. For the Monte Carlo isotherm (step_02), the verifier possesses a high-quality reference dataset digitized from the published results; your coverage values will be compared to this reference, tolerating small deviations due to finite sampling. The two artifacts are weighted, and the final score reflects the combined accuracy of both computations.