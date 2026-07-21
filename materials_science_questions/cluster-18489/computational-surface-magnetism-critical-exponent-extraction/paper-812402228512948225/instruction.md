# Monte Carlo Simulation of Surface Magnetism in Spinel Nanoparticles

## Problem background
Magnetic nanoparticles of maghemite (γ-Fe2O3) often consist of a core and a surface shell. Spins on the surface have reduced coordination and may experience strong surface anisotropy, causing their magnetic response to differ from the core as temperature changes. Understanding the thermal variation of core and surface magnetisation, the resulting specific heat, and the spatial magnetisation profile within the particle is important for interpreting experimental measurements such as Mössbauer spectroscopy and high-field magnetisation data. This task reproduces a classical Monte Carlo simulation of a small maghemite nanoparticle (~4 nm) and requires the computation of these quantities from the simulated spin configurations.

## Approach
The particle is modelled using the spinel crystal structure of γ-Fe2O3 with two sublattices (A and B) and 1/3 randomly distributed vacancies on B sites. Spins are classified as core or surface based on their coordination number; the surface shell thickness is kept constant at ~0.35 nm, yielding a surface fraction of 53% for a total of N_t = 909 spins. The magnetic energy is described by a classical Dirac–Heisenberg Hamiltonian that includes:
- Nearest-neighbour exchange interactions (different couplings between A‑A, A‑B, and B‑B pairs).
- Core uniaxial anisotropy with the easy axis along the particle z‑direction.
- Surface single‑site anisotropy with easy axes pointing outward along the local surface normal.
- Shape anisotropy for a prolate spheroidal particle, modelled through effective demagnetising factors.

Simulations are performed using the Metropolis Monte Carlo algorithm at zero applied field. The system is equilibrated and averaged over a temperature range from about 10 K to above the core ordering temperature (~900 K). From the trajectories, per‑site core and surface magnetisation (root‑mean‑square of the vector sum) and specific heat per spin (from energy variance) are calculated. At the lowest temperature, the radial profile of the local magnetisation—the average projection of each spin onto its local easy axis—is extracted.

## Reproduction target
Produce two scored output files from the Monte Carlo simulation:

1. **step_01_thermal.csv** – columns: `temperature` (K), `core_mag` (dimensionless), `surf_mag` (dimensionless), `specific_heat` (kB per spin).
2. **step_02_profile.csv** – columns: `radial_bin` (nm), `local_mag` (dimensionless).

The simulation must be carried out according to the workflow steps, and the resulting curves should reflect the physical differences between core and surface magnetisation as well as the spatial variation of magnetism inside the nanoparticle.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Generate nanoparticle spinel structure
- Role: process
- Action: Construct the spinel lattice for a maghemite nanoparticle with N_t=909 spins, two sublattices A and B, randomly assign 1/3 vacancies on B sites. Cut a sphere/ellipsoid, classify each site as core (full coordination) or surface (reduced coordination) to achieve N_st=53%, assign anisotropy axes: core along +z, surface along outward normal. Save site list to structure.json.
- Evidence: `/app/outputs/structure.json`

### Step 2: Perform Monte Carlo simulation across temperature range
- Role: process
- Action: Using the site list from step_01, implement classical Metropolis Monte Carlo with Dirac-Heisenberg Hamiltonian (exchange constants J_AB/k_B=-28.1 K, J_BB/k_B=-8.6 K, J_AA/k_B=-21.0 K), core uniaxial anisotropy (K_c/k_B=8.13e-3 K along z), surface single-site anisotropy (K_s/k_B=0.5 K along local normal), and shape anisotropy for a prolate spheroid. Run at H=0 for temperatures from ~10 K to ~900 K, at least 3000 MC steps per spin for equilibration and averaging. Accumulate mean spin components and mean squared magnetisation per temperature; save raw data to mc_data.pkl.
- Evidence: `/app/outputs/mc_data.pkl`

### Step 3: Compute thermal magnetisation and specific heat
- Role: scored (load-bearing)
- Action: From mc_data.pkl, compute per-temperature quantities: core magnetisation per site M_core = sqrt(<(Σ_{i∈core} S_i)^2> / N_c²), surface magnetisation M_surface similarly, and specific heat per spin C = var(E) / (k_B T² N_t). Write a CSV with columns: temperature, core_mag, surf_mag, specific_heat.
- Output file: `/app/outputs/step_01_thermal.csv`
- Format: csv
- Contract: Columns: temperature (float, K), core_mag (float, dimensionless), surf_mag (float, dimensionless), specific_heat (float, k_B per spin).
- Scoring: scored by hidden verifier

### Step 4: Extract magnetisation radial profile at low temperature
- Role: scored
- Action: From mc_data.pkl at the lowest temperature (~10 K), compute the projection of each spin's average orientation onto its local easy axis. Bin spins by radial distance from the particle centre and compute the mean normalised projection (local_mag) per bin. Output a CSV with radial_bin (nm) and local_mag.
- Output file: `/app/outputs/step_02_profile.csv`
- Format: csv
- Contract: Columns: radial_bin (float, nm), local_mag (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_thermal.csv`
- `/app/outputs/step_02_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_thermal.csv
- path: `/app/outputs/step_01_thermal.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Thermal variation of core and surface magnetisation per site and specific heat per spin.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `core_mag`, `surf_mag`, `specific_heat`
  - `units`:
    - `temperature`: K
    - `core_mag`: dimensionless
    - `surf_mag`: dimensionless
    - `specific_heat`: k_B per spin

### step_02_profile.csv
- path: `/app/outputs/step_02_profile.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Radial profile of local magnetisation at low temperature.
- schema:
  - `type`: table
  - `required_columns`: `radial_bin`, `local_mag`
  - `units`:
    - `radial_bin`: nm
    - `local_mag`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_thermal.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "core_mag",
          "surf_mag",
          "specific_heat"
        ],
        "units": {
          "temperature": "K",
          "core_mag": "dimensionless",
          "surf_mag": "dimensionless",
          "specific_heat": "k_B per spin"
        }
      },
      "description": "Thermal variation of core and surface magnetisation per site and specific heat per spin."
    },
    {
      "file": "step_02_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "radial_bin",
          "local_mag"
        ],
        "units": {
          "radial_bin": "nm",
          "local_mag": "dimensionless"
        }
      },
      "description": "Radial profile of local magnetisation at low temperature."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact. It does not simply compare numbers to a target value; instead it checks that the computed curves satisfy expected structural relationships—such as relative ordering between core and surface magnetisation, the temperature dependence of the specific heat, and the radial decay of the local magnetisation—consistent with the physics of a nanoparticle with surface spin disorder. The verifier combines these checks into a final reward between 0 and 1. Simply reporting a set of numbers is not sufficient; the simulation must genuinely produce the correct physical trends.
