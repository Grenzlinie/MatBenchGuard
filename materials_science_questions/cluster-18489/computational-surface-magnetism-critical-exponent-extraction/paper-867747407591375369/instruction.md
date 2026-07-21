# Surface-disorder magnetisation profile and thermal magnetization in maghemite nanoparticles

## Problem background
Magnetic nanoparticles exhibit surface disorder that reduces the local magnetisation near the surface and alters the overall magnetic properties. Understanding the spatial profile of magnetisation from the particle centre to the surface, and its evolution with temperature, is key to explaining experimental observations such as non-saturation at low temperatures and size-dependent magnetisation enhancement. This task requires computing the radial magnetisation profile and thermal magnetisation curves for spherical maghemite (γ-Fe₂O₃) nanoparticles.

## Approach
The magnetic state of the nanoparticle is described by a classical anisotropic Dirac–Heisenberg model that includes exchange interactions between nearest-neighbour spins, uniaxial anisotropy in the core, and single-site surface anisotropy with axes along the outward normal. The particle is built by cutting a sphere from the cubic spinel crystal structure of maghemite (space group P4₃32, lattice parameter ~0.834 nm, Fe³⁺ spins of magnitude 5/2 with 1/3 vacancy on octahedral B sites). Spins are classified as core (full coordination) or surface (incomplete), and the exchange constants on the surface are reduced relative to the core. Metropolis Monte Carlo simulations are run for particles of different total spin counts, at several reduced core temperatures, to compute the ensemble-averaged magnetisation. Two types of output are produced: (1) the radial profile of the local magnetisation (projection onto the local easy axis) binned by normalised distance from the centre, and (2) the temperature-dependent site-averaged magnetisation computed separately for core and surface spins, together with the weighted mean magnetisation per site.

## Reproduction target
Produce two scored artifacts from independent Monte Carlo runs, using the same Hamiltonian and parameter set.

1. **Radial magnetisation profile** (`step_01_radial_profile.csv`): For a spherical nanoparticle containing exactly 3140 spins, compute the local magnetisation (projection of the spin onto its easy axis) binned by normalised radial distance from the centre (0) to the surface (1), at three reduced core temperatures: very low (τ_core ≪ 1, e.g. 0.05), intermediate (τ_core = 0.5), and near the core critical temperature (τ_core ≈ 0.95). The CSV must contain one row per bin per temperature, with columns: reduced_temperature (string label), radial_bin (float), local_magnetization (float).

2. **Thermal magnetisation curves** (`step_02_thermal_magnetization.csv`): For two particle sizes, Nt = 909 and Nt = 3766 spins, compute the site-averaged core magnetisation, surface magnetisation, and mean magnetisation per site over at least ten reduced core temperatures spanning approximately τ_core from 0.05 to 1.2. The CSV must contain columns: particle_size (integer), reduced_temperature (float), core_magnetization (float), surface_magnetization (float), mean_magnetization (float).

The required physical trends that must emerge from the simulations are: the local magnetisation decreases continuously from centre to surface at all temperatures, with a temperature-dependent drop near the surface; the surface magnetisation decays more rapidly with temperature than the core magnetisation; the surface 'critical region' lies at a lower reduced temperature than the core; and the mean magnetisation at low temperatures is larger for the smaller particle (Nt=909) than for the larger one (Nt=3766).

## Assets

- Spinel crystal structure of γ-Fe2O3 (maghemite)

## Workflow steps

### Step 1: Nanoparticle lattice generation
- Role: process
- Action: Generate spherical nanoparticle lattices from the spinel structure of maghemite for particle sizes of 3140, 909, and 3766 spins. Classify each spin as core (full coordination) or surface (incomplete coordination). Assign easy axes: core spins have uniaxial anisotropy along the global z-axis; surface spins have outward-normal single-site anisotropy. Build nearest-neighbor lists for exchange interactions. Write a log recording the number of core and surface spins and the radial bin boundaries.
- Evidence: `/app/outputs/step_00_lattice_log.txt`

### Step 2: Radial magnetisation profile
- Role: scored (load-bearing)
- Action: For a 3140-spin spherical nanoparticle, use classical Metropolis Monte Carlo simulations of the anisotropic Dirac-Heisenberg Hamiltonian (exchange + core uniaxial anisotropy + surface single-site anisotropy) to compute the local magnetisation profile at three reduced core temperatures: very low (τ_core ≪ 1, e.g. 0.05), intermediate (τ_core = 0.5), and near critical (τ_core ≈ 0.95). Use the exchange constants J_AB/k_B = −28.1 K, J_BB/k_B = −8.6 K, J_AA/k_B = −21.0 K; surface exchange is 0.1 times the core values. Core anisotropy constant K_c/k_B = 8.13×10⁻³ K; surface anisotropy K_s/k_B = 0.5 K. Compute the local magnetisation as the ensemble-averaged projection of each spin onto its local easy axis. Bin spins by normalised radial distance (from 0 at the centre to 1 at the surface) and average the magnetisation per bin. Write the result to step_01_radial_profile.csv.
- Output file: `/app/outputs/step_01_radial_profile.csv`
- Format: csv
- Contract: columns: reduced_temperature (string, one of 'very_low','intermediate','near_critical'), radial_bin (float, normalised distance from centre, 0 to 1), local_magnetization (float, dimensionless projection of spin onto easy axis).
- Scoring: scored by hidden verifier

### Step 3: Thermal magnetisation curves
- Role: scored
- Action: For spherical nanoparticles of total spin count Nt = 909 and Nt = 3766, run classical Metropolis Monte Carlo simulations over at least ten reduced core temperatures spanning approximately τ_core from 0.05 to 1.2. Use the same Hamiltonian, exchange constants, and anisotropy values as in step_01. At each temperature compute the site-averaged magnetisation separately for core and surface spins using M = sqrt( ⟨ ( (1/N) Σ_i S_i )² ⟩ ), and the mean magnetisation per site as M_mean = (N_s M_surface + N_c M_core) / N_t. Write the results to step_02_thermal_magnetization.csv.
- Output file: `/app/outputs/step_02_thermal_magnetization.csv`
- Format: csv
- Contract: columns: particle_size (integer, total number of spins Nt), reduced_temperature (float, τ_core = T/T_c_core), core_magnetization (float, M_core per site), surface_magnetization (float, M_surface per site), mean_magnetization (float, M_mean per site).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_radial_profile.csv`
- `/app/outputs/step_02_thermal_magnetization.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_radial_profile.csv
- path: `/app/outputs/step_01_radial_profile.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Radial profile of local magnetisation for the 3140-spin nanoparticle. The checker will compute derived quantities (centre-to-surface decrease, temperature-dependent drop) from the submitted data and compare against hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `reduced_temperature`, `radial_bin`, `local_magnetization`
  - `units`:
    - `radial_bin`: normalised distance (unitless)
    - `local_magnetization`: dimensionless

### step_02_thermal_magnetization.csv
- path: `/app/outputs/step_02_thermal_magnetization.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Thermal magnetisation curves for two particle sizes. The checker will evaluate the relative ordering (surface decays faster than core, surface critical region at lower τ_core) and the size dependence from the submitted data, comparing derived ratios and inflection points to hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `particle_size`, `reduced_temperature`, `core_magnetization`, `surface_magnetization`, `mean_magnetization`
  - `units`:
    - `reduced_temperature`: unitless
    - `core_magnetization`: per-site dimensionless
    - `surface_magnetization`: per-site dimensionless
    - `mean_magnetization`: per-site dimensionless

Notes: Both scored artifacts are produced from independent Monte Carlo runs. The agent must implement the full Hamiltonian and simulation protocol. The hidden checker performs structural audits on the submitted tables (computing summary metrics from the data) and compares them to paper-derived gold thresholds; the target policies are structural_audit to reflect this honest structural scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_radial_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "reduced_temperature",
          "radial_bin",
          "local_magnetization"
        ],
        "units": {
          "radial_bin": "normalised distance (unitless)",
          "local_magnetization": "dimensionless"
        }
      },
      "description": "Radial profile of local magnetisation for the 3140-spin nanoparticle. The checker will compute derived quantities (centre-to-surface decrease, temperature-dependent drop) from the submitted data and compare against hidden reference values."
    },
    {
      "file": "step_02_thermal_magnetization.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "particle_size",
          "reduced_temperature",
          "core_magnetization",
          "surface_magnetization",
          "mean_magnetization"
        ],
        "units": {
          "reduced_temperature": "unitless",
          "core_magnetization": "per-site dimensionless",
          "surface_magnetization": "per-site dimensionless",
          "mean_magnetization": "per-site dimensionless"
        }
      },
      "description": "Thermal magnetisation curves for two particle sizes. The checker will evaluate the relative ordering (surface decays faster than core, surface critical region at lower τ_core) and the size dependence from the submitted data, comparing derived ratios and inflection points to hidden reference values."
    }
  ],
  "notes": "Both scored artifacts are produced from independent Monte Carlo runs. The agent must implement the full Hamiltonian and simulation protocol. The hidden checker performs structural audits on the submitted tables (computing summary metrics from the data) and compares them to paper-derived gold thresholds; the target policies are structural_audit to reflect this honest structural scoring."
}
```

## How you are scored
A hidden verifier independently scores each of the two scored output files and combines them by weight into a final reward in [0,1]. For `step_01_radial_profile.csv`, the verifier checks structural features: the centre-to-surface decrease at each temperature and the temperature-dependent behaviour near the surface. For `step_02_thermal_magnetization.csv`, it evaluates relative ordering (surface vs. core decay, critical region shift) and the size dependence (low-temperature mean magnetisation ordering), comparing derived quantities against hidden reference values. Merely reporting numbers that match a table is not sufficient; the artifacts must result from a correct implementation of the Hamiltonian and Monte Carlo simulation protocol described in the workflow steps.
