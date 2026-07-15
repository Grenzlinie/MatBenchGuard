# Ensemble Monte Carlo simulation of nonequilibrium LO-phonon effects on transport in n-type GaAs

## Problem background
In polar semiconductors such as n-type gallium arsenide (GaAs), energetic electrons can emit longitudinal optical (LO) phonons at a rate that exceeds the phonon thermalization rate by the lattice. This creates a nonequilibrium LO-phonon distribution that can feed back on the carrier transport. The central question is whether such hot-phonon effects significantly alter the steady-state drift velocity versus electric field characteristic and the transient velocity overshoot that are critical for high-speed device design. This task investigates that question by simulating the coupled electron–LO-phonon system in n-type GaAs at 300 K under high dc fields.

## Approach
The core idea is to embed a time-evolving, discretized LO-phonon distribution into an ensemble Monte Carlo transport simulation. The GaAs conduction band includes Γ and L valleys with standard scattering mechanisms: polar-optical, intervalley, acoustic deformation potential, and ionized-impurity scattering (with static free-carrier screening). The LO-phonon distribution is discretized in (wave vector magnitude q, cos θ) space and is updated every subhistory: (i) electron-phonon scattering events change the phonon occupancy according to the ensemble's emissions and absorptions, and (ii) a phonon-phonon relaxation term drives the distribution back toward the thermal Planck distribution with a lifetime τ_LO. Two separate simulation sets are run for each electric field: one with phonon equilibrium (i.e., τ_LO^0 = 0, so phonons remain at the thermal Planck distribution) and one with nonequilibrium phonon buildup (using the experimental lifetime τ_LO^0 = 9 ps). By comparing the drift velocity time series from the two sets, the influence of hot LO phonons on steady-state transport and on the initial velocity overshoot is quantified.

## Reproduction target
For n-type GaAs at a lattice temperature of 300 K, with a free-electron density n_e = 3×10^17 cm⁻³ and a donor density n_i = 3×10^12 cm⁻³ (remote impurity scattering), compute the mean drift velocity as a function of electric field for fields 0.5, 1, 2, 4, 6, 8, 10, and 12 kV/cm. Produce two CSV files:
1. Steady-state drift velocity (cm/s) versus field (kV/cm) for both the phonon-equilibrium and the nonequilibrium-phonon cases.
2. The peak velocity during the first 2 ps after field onset at 8 kV/cm (the overshoot peak) for both cases.
From these outputs, the impact of the nonequilibrium LO-phonon disturbances on the velocity-field characteristic and on the overshoot peak can be assessed.

## Assets

- GaAs material parameters (Littlejohn, Hauser, Glisson, J. Appl. Phys. 48, 4587, 1977): https://doi.org/10.1063/1.323585

## Workflow steps

### Step 1: Implement Monte Carlo algorithm with nonequilibrium phonons
- Role: process
- Action: Implement the ensemble Monte Carlo algorithm for n-type GaAs as described in the paper, including discretized LO-phonon distribution in (q,cosθ) space with evolving phonon-electron scattering and phonon-phonon relaxation (τ_LO model). Use material parameters from Littlejohn et al. (1977): Γ and L valleys, polar-optical coupling, intervalley and acoustic deformation potentials, ionized-impurity scattering with static free-carrier screening, and the two-channel LO-phonon lifetime formula with τ_LO^0 = 9 ps.
- Evidence: none

### Step 2: Run ensemble Monte Carlo simulations for all conditions
- Role: process
- Action: Run the implemented Monte Carlo code for electric fields 0.5, 1, 2, 4, 6, 8, 10, 12 kV/cm at lattice temperature 300 K, carrier density n_e = 3×10¹⁷ cm⁻³, donor density n_i = 3×10¹² cm⁻³ (remote impurity). For each field, perform two simulations: with nonequilibrium phonons (τ_LO^0 = 9 ps) and with phonon equilibrium (τ_LO^0 = 0). Use an ensemble of at least 10,000 electrons, subhistory Δt = 2.5×10⁻¹⁴ s, and simulate up to at least 20 ps. Save the time series of mean drift velocity for each run.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 3: Extract steady-state drift velocity and write CSV
- Role: scored (load-bearing)
- Action: For each field, compute the steady-state drift velocity as the time average of v(t) over the interval 10–20 ps after field onset. Produce a CSV file with three columns: electric_field_kVcm, v_equilibrium_cms (phonon equilibrium run), v_nonequilibrium_cms (phonon disturbance run).
- Output file: `/app/outputs/steady_state.csv`
- Format: csv
- Contract: columns: electric_field_kVcm (float), v_equilibrium_cms (float), v_nonequilibrium_cms (float)
- Scoring: scored by hidden verifier

### Step 4: Extract velocity overshoot peak and write CSV
- Role: scored (load-bearing)
- Action: From the 8 kV/cm simulation runs, find the maximum drift velocity within the first 2 ps after field onset. Write a single-row CSV with columns: electric_field_kVcm (set to 8.0), v_equilibrium_peak_cms, v_nonequilibrium_peak_cms.
- Output file: `/app/outputs/overshoot_peak.csv`
- Format: csv
- Contract: columns: electric_field_kVcm (float), v_equilibrium_peak_cms (float), v_nonequilibrium_peak_cms (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/steady_state.csv`
- `/app/outputs/overshoot_peak.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### steady_state.csv
- path: `/app/outputs/steady_state.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Steady-state drift velocity vs electric field for n-type GaAs at 300 K, with and without nonequilibrium LO-phonon disturbances.
- schema:
  - `type`: table
  - `required_columns`: `electric_field_kVcm`, `v_equilibrium_cms`, `v_nonequilibrium_cms`
  - `units`:
    - `electric_field_kVcm`: kV/cm
    - `v_equilibrium_cms`: cm/s
    - `v_nonequilibrium_cms`: cm/s

### overshoot_peak.csv
- path: `/app/outputs/overshoot_peak.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Velocity overshoot peak at 8 kV/cm, showing negligible effect of nonequilibrium phonons.
- schema:
  - `type`: table
  - `required_columns`: `electric_field_kVcm`, `v_equilibrium_peak_cms`, `v_nonequilibrium_peak_cms`
  - `units`:
    - `electric_field_kVcm`: kV/cm
    - `v_equilibrium_peak_cms`: cm/s
    - `v_nonequilibrium_peak_cms`: cm/s

Notes: The checker will compare the agent's reported velocities to hidden reference values and apply checks for relative trends (drag at low fields, heating at high fields) as well as absolute tolerance. The agent does not need to know the gold values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "steady_state.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "electric_field_kVcm",
          "v_equilibrium_cms",
          "v_nonequilibrium_cms"
        ],
        "units": {
          "electric_field_kVcm": "kV/cm",
          "v_equilibrium_cms": "cm/s",
          "v_nonequilibrium_cms": "cm/s"
        }
      },
      "description": "Steady-state drift velocity vs electric field for n-type GaAs at 300 K, with and without nonequilibrium LO-phonon disturbances."
    },
    {
      "file": "overshoot_peak.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "electric_field_kVcm",
          "v_equilibrium_peak_cms",
          "v_nonequilibrium_peak_cms"
        ],
        "units": {
          "electric_field_kVcm": "kV/cm",
          "v_equilibrium_peak_cms": "cm/s",
          "v_nonequilibrium_peak_cms": "cm/s"
        }
      },
      "description": "Velocity overshoot peak at 8 kV/cm, showing negligible effect of nonequilibrium phonons."
    }
  ],
  "notes": "The checker will compare the agent's reported velocities to hidden reference values and apply checks for relative trends (drag at low fields, heating at high fields) as well as absolute tolerance. The agent does not need to know the gold values."
}
```

## How you are scored
A hidden verifier reads your two output CSV files and independently scores them. Each artifact is compared to hidden reference values and checked for specific required relative relationships between the equilibrium and nonequilibrium cases (e.g., whether the nonequilibrium phonons cause a systematic increase or decrease in steady-state velocity at different field ranges, and whether the overshoot peak magnitude is materially changed). The verifier does not simply check whether a single number matches; it validates physical trends and absolute consistency within tolerances. The two scored stages are weighted and combined into a final reward between 0 and 1. Simply reporting numbers from the literature without running the simulation pipeline will not produce the required artifacts and will receive zero reward.
