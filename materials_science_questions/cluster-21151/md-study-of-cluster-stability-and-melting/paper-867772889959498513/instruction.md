# Monopole Oscillation Parameter Extraction for Argon Cluster

## Problem background
Classical molecular dynamics simulation of a 13-atom Argon cluster (Ar13) can be used to study collective shape oscillations, specifically the monopole "breathing" mode. The time evolution of the monopole amplitude may be describable by a damped harmonic oscillator. The equivalent 1D oscillator parameters (damping coefficient, oscillation period, spring constant, and reduced mass) could reveal characteristic behaviors as functions of total energy, potentially indicating different dynamical regimes of the cluster. This task aims to compute those parameters and explore how they change with energy.

## Approach
Perform isoergic molecular dynamics simulations of a 13-particle Argon cluster using the Lennard‑Jones 6‑12 potential with parameters σ=3.4 Å and ε=1.67×10⁻¹⁴ erg. Equilibrate the icosahedral cluster at a series of total energies spanning the solid‑like regime. At each energy, apply a monopole excitation by a sudden, radially uniform expansion that raises the potential energy by δE=0.05×10⁻¹⁴ erg/atom, then run 500 independent trajectories (Verlet algorithm, time step 2 fs, ~100 ps duration). Compute the ensemble-averaged average radius (monopole amplitude) as a function of time. Fit this averaged signal to the damped harmonic oscillator form y(t)=y₀+A·exp(−λt)·cos(ω′t+δ) to obtain damping coefficient λ and reduced frequency ω′. From a selected trajectory, fit the cluster potential energy versus radius to a parabola to extract the spring constant k. Compute natural frequency ω = √(ω′²+λ²) and effective mass m = k/ω², then derive the oscillation period T=2π/ω′ and the reduced‑mass ratio M/m (M is the Ar atomic mass). Finally, compile these parameters as functions of total energy and examine any qualitative trends or transitions.

## Reproduction target
From the MD simulations, produce a CSV table (oscillator_parameters_vs_energy.csv) with columns: total_energy (in 1e-14 erg/atom), damping_coefficient (in 1e10 Hz), period (in ps), spring_constant (in consistent units such as erg/atom/Å²), and reduced_mass_ratio (dimensionless). The table must contain at least 10 rows covering the solid‑like regime (roughly −5.8 to −5.2 ×10⁻¹⁴ erg/atom), including energies on both sides of any observed qualitative change. The goal is to compute these quantities and identify whether a distinct transition exists in their energy dependence, and if so, to characterize how the parameters behave on either side.

## Assets

- Lennard-Jones parameters for Argon (σ=3.4 Å, ε=1.67×10⁻¹⁴ erg)
- Molecular dynamics engine (open-source)
- scipy (curve fitting): scipy

## Workflow steps

### Step 1: MD simulation and oscillator parameter extraction
- Role: process
- Action: Set up the initial icosahedral Ar13 geometry using LJ parameters (σ=3.4 Å, ε=1.67×10⁻¹⁴ erg). For a series of target total energies spanning the solid-like regime (roughly -5.8 to -5.2 ×10⁻¹⁴ erg/atom), equilibrate the cluster, apply a sudden radially uniform expansion (δE=0.05×10⁻¹⁴ erg/atom), and run 500 independent isoergic MD trajectories (Verlet algorithm, time step 2 fs, total duration ~100 ps). Compute the ensemble-averaged monopole amplitude (average radius) as y(t) and fit it to y(t)=y₀+A·e^(-λt)·cos(ω't+δ) to obtain damping coefficient λ and reduced frequency ω'. From a selected trajectory, fit the cluster potential energy vs radius to a parabola to extract the spring constant k. Compute natural frequency ω = √(ω'²+λ²) and effective mass m = k/ω². Compute oscillation period T = 2π/ω' and reduced-mass ratio M/m (where M is the atomic mass of Ar). Produce an intermediate JSON file containing for each energy: λ, ω', k, m, T, and M/m, along with the raw ensemble-averaged y(t) data points for at least one temperature as evidence.
- Evidence: `/app/outputs/fitted_parameters_per_energy.json`

### Step 2: Compile oscillator parameters vs total energy
- Role: scored (load-bearing)
- Action: From the extracted parameters, create a CSV file with columns: total_energy, damping_coefficient, period, spring_constant, reduced_mass_ratio. Total energy in units of 1e-14 erg/atom; damping coefficient in 1e10 Hz; period in ps; spring constant in consistent relative units (e.g., erg/atom/Å²); reduced_mass_ratio dimensionless. The table must cover the solid-like regime with at least 10 rows, including points below and above the transition.
- Output file: `/app/outputs/oscillator_parameters_vs_energy.csv`
- Format: csv
- Contract: Columns: total_energy (float, unit 1e-14 erg/atom), damping_coefficient (float, unit 1e10 Hz), period (float, unit ps), spring_constant (float), reduced_mass_ratio (float). At least 10 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/oscillator_parameters_vs_energy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### oscillator_parameters_vs_energy.csv
- path: `/app/outputs/oscillator_parameters_vs_energy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Oscillator parameters extracted from MD simulations as a function of total energy. Used to verify the structural trends and the transition energy marking the onset of single-particle excitations and damping.
- schema:
  - `type`: table
  - `required_columns`: `total_energy`, `damping_coefficient`, `period`, `spring_constant`, `reduced_mass_ratio`
  - `units`:
    - `total_energy`: 1e-14 erg/atom
    - `damping_coefficient`: 1e10 Hz
    - `period`: ps
    - `spring_constant`: erg/atom/Å² (or consistent relative unit)
    - `reduced_mass_ratio`: dimensionless (M/m)

Notes: The transition total energy is expected around -5.444×10⁻¹⁴ erg/atom. The damping coefficient should be near zero below this energy and increase linearly above; period changes slope; spring constant increases as √E above; reduced mass ratio drops from ~12 to ~1. Tolerances are not disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "oscillator_parameters_vs_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "total_energy",
          "damping_coefficient",
          "period",
          "spring_constant",
          "reduced_mass_ratio"
        ],
        "units": {
          "total_energy": "1e-14 erg/atom",
          "damping_coefficient": "1e10 Hz",
          "period": "ps",
          "spring_constant": "erg/atom/Å² (or consistent relative unit)",
          "reduced_mass_ratio": "dimensionless (M/m)"
        }
      },
      "description": "Oscillator parameters extracted from MD simulations as a function of total energy. Used to verify the structural trends and the transition energy marking the onset of single-particle excitations and damping."
    }
  ],
  "notes": "The transition total energy is expected around -5.444×10⁻¹⁴ erg/atom. The damping coefficient should be near zero below this energy and increase linearly above; period changes slope; spring constant increases as √E above; reduced mass ratio drops from ~12 to ~1. Tolerances are not disclosed."
}
```

## How you are scored
A hidden verifier checks your submitted CSV file. It first validates the file structure (correct columns, at least 10 rows, appropriate units). Then it evaluates whether the reported parameter values exhibit the qualitative trends characteristic of the Ar13 cluster dynamics — for example, whether the damping coefficient, period, spring constant, and reduced‑mass ratio change in a consistent manner across the energy range, and whether any transition can be identified. The verifier may use paper‑derived reference values (not disclosed to you) to assess the correctness of the trends. Reporting numbers is not sufficient; the submitted parameters must be the result of executing the full simulation and analysis pipeline. The final reward is a weighted combination of the structural check and the trend‑based evaluation.
