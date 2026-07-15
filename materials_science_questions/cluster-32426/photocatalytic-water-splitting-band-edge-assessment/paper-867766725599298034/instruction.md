# Plasmon-Induced Hot-Carrier Generation and Water Splitting in Metallic Nanoparticles

## Problem background
Harnessing hot electrons and holes produced by the decay of localized surface plasmons in metallic nanoparticles is important for photovoltaics, photocatalysis, and optoelectronics. The properties of these hot carriers—generation rates and energy distributions—depend on the nanoparticle material, size, and the dielectric medium surrounding it. In this task, you will implement a theoretical model to compute hot-carrier generation in spherical nanoparticles of six different metals (Na, K, Al, Cu, Ag, Au) and evaluate their potential for water splitting. By varying the material, the nanoparticle radius, and the environment dielectric constant (ε_m = 1, 5, 10), you can explore how these factors influence hot-carrier efficiency and the availability of energetic carriers for the hydrogen evolution reaction (HER) and the oxygen evolution reaction (OER).

## Approach
To model hot-carrier generation, you will solve the electronic structure of a spherical nanoparticle using a finite spherical potential well, with the well depth chosen so that the Fermi energy equals the material’s work function. The optical response is described in the quasistatic approximation, using experimental bulk dielectric functions. Transition rates between electronic states are computed via Fermi’s Golden Rule, with a density of available transitions that includes both resonant and anti-resonant contributions and is broadened by linewidths that arise from electron-phonon (Debye model) and electron-electron (Fermi liquid theory) scattering. From the resulting energy-resolved hot-carrier distributions, you will integrate to obtain two practical quantities: a figure of merit (the fraction of hot carriers with energy above a threshold related to the plasmon energy) and the total number of hot carriers that can drive water-splitting half-reactions under standard AM1.5 solar illumination.

## Reproduction target
Your goal is to implement the described pipeline and produce two scored output files for nanoparticles of radius R = 6 nm, at three dielectric constants (ε_m = 1, 5, 10), for all six materials: Na, K, Al, Cu, Ag, Au.

- **figure_of_merit.csv**: contains the figure of merit (FoM) for hot electrons and hot holes, computed using a threshold δE = 0.3·ħω_LSP, where ω_LSP is the localized surface plasmon energy for that material and environment combination.
- **water_splitting_counts.csv**: contains the total number of hot electrons with energy above -4.44 eV (HER threshold) and hot holes with energy below -5.67 eV (OER threshold) per nanoparticle, integrated over the AM1.5 solar spectrum.

Both files must follow the specified column schemas; see the output contract for details.

## Assets

- Material parameters for Na, K, Al, Cu, Ag, Au
- Complex dielectric functions for Na, K, Al, Cu, Ag, Au
- Standard AM1.5 solar spectral irradiance: https://www.nrel.gov/grid/solar-resource/spectra-astm-e490.html
- Python scientific environment: numpy, scipy, pandas

## Workflow steps

### Step 1: Load material parameters and dielectric functions
- Role: process
- Action: Load the bundled material_parameters.csv and dielectric_functions.csv into memory. Parse conduction electron densities, work functions, Debye temperatures, electron‑phonon coupling constants, and energy‑dependent refractive index/extinction coefficient for each metal.
- Evidence: none

### Step 2: Solve electronic structure: spherical potential well
- Role: process
- Action: For each material and for radius R=6 nm, determine the well depth V0 such that the Fermi energy matches the work function. Solve the radial Schrödinger equation numerically to obtain bound and discretized continuum single‑particle wavefunctions and energy eigenvalues for all relevant angular momenta.
- Evidence: `/app/outputs/eigenstates_info.json`

### Step 3: Compute hot‑carrier linewidths and lifetimes
- Role: process
- Action: Using state energies and material parameters, compute the electron‑phonon contribution (Debye model) and electron‑electron contribution (Fermi‑liquid formula) for each state, then combine via Matthiessen’s rule to obtain transition linewidths γ_if and lifetimes τ_if.
- Evidence: `/app/outputs/linewidths_summary.csv`

### Step 4: Compute optical matrix elements in quasistatic approximation
- Role: process
- Action: Construct the total perturbing potential Φ_tot (external field plus dipolar response) for each photon energy and dielectric environment (ε_m=1,5,10). Compute transition matrix elements ⟨Ψ_f|Φ_tot|Ψ_i⟩ for all initial‑final state pairs using wavefunctions and dielectric functions.
- Evidence: none

### Step 5: Compute energy‑resolved hot‑carrier generation rates
- Role: process
- Action: Apply Fermi’s golden rule with two‑Lorentzian density of available transitions and a Gaussian‑smeared delta function to obtain hot‑electron energy distribution N_e(E,ω) and hot‑hole distribution N_h(E,ω) for relevant photon energies.
- Evidence: none

### Step 6: Compute Figure of Merit (FoM) for hot carriers
- Role: scored (load-bearing)
- Action: Integrate the hot‑carrier distributions over energy to obtain total numbers and absorbed power. Compute the figure of merit N_e^{δE} and N_h^{δE} using δE = 0.3·ħω_LSP, where ω_LSP is the localized surface plasmon energy for each material and environment. Output the FoM for each material, each dielectric constant ε_m (1,5,10) at radius 6 nm.
- Output file: `/app/outputs/figure_of_merit.csv`
- Format: csv
- Contract: Columns: material (string), epsilon_m (float), radius_nm (float), FoM_electrons (float), FoM_holes (float). One row per (material, epsilon_m, 6.0).
- Scoring: scored by hidden verifier

### Step 7: Compute hot‑carrier counts for water splitting under sunlight
- Role: scored
- Action: Using the AM1.5 spectral irradiance S(ω), integrate the hot‑carrier distributions over photon energy and count electrons with energy above E_HER = –4.44 eV and holes with energy below E_OER = –5.67 eV. Output the total counts for each material and ε_m at radius 6 nm.
- Output file: `/app/outputs/water_splitting_counts.csv`
- Format: csv
- Contract: Columns: material (string), epsilon_m (float), radius_nm (float), N_electrons_HER (float), N_holes_OER (float). One row per (material, epsilon_m, 6.0).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/figure_of_merit.csv`
- `/app/outputs/water_splitting_counts.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### figure_of_merit.csv
- path: `/app/outputs/figure_of_merit.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Hot‑carrier Figure of Merit for six materials at three dielectric environments; scored against paper‑reported trends and approximate magnitudes.
- schema:
  - `type`: table
  - `required_columns`: `material`, `epsilon_m`, `radius_nm`, `FoM_electrons`, `FoM_holes`
  - `units`:
    - `FoM_electrons`: dimensionless
    - `FoM_holes`: dimensionless

### water_splitting_counts.csv
- path: `/app/outputs/water_splitting_counts.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total hot carriers available for HER and OER under AM1.5 illumination; scored against paper‑reported ordering and approximate magnitudes.
- schema:
  - `type`: table
  - `required_columns`: `material`, `epsilon_m`, `radius_nm`, `N_electrons_HER`, `N_holes_OER`
  - `units`:
    - `N_electrons_HER`: counts per nanoparticle
    - `N_holes_OER`: counts per nanoparticle

Notes: The checker applies both absolute value comparison (within generous tolerance) and structural audits (trends, ordering, monotonicity) to award partial credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "figure_of_merit.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "epsilon_m",
          "radius_nm",
          "FoM_electrons",
          "FoM_holes"
        ],
        "units": {
          "FoM_electrons": "dimensionless",
          "FoM_holes": "dimensionless"
        }
      },
      "description": "Hot‑carrier Figure of Merit for six materials at three dielectric environments; scored against paper‑reported trends and approximate magnitudes."
    },
    {
      "file": "water_splitting_counts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "epsilon_m",
          "radius_nm",
          "N_electrons_HER",
          "N_holes_OER"
        ],
        "units": {
          "N_electrons_HER": "counts per nanoparticle",
          "N_holes_OER": "counts per nanoparticle"
        }
      },
      "description": "Total hot carriers available for HER and OER under AM1.5 illumination; scored against paper‑reported ordering and approximate magnitudes."
    }
  ],
  "notes": "The checker applies both absolute value comparison (within generous tolerance) and structural audits (trends, ordering, monotonicity) to award partial credit."
}
```

## How you are scored
A hidden verifier will independently examine your submitted outputs and compare them against expected physical relationships and reference values. Each scored artifact is first checked for structural completeness (correct columns and data types). Then the verifier assesses whether the computed quantities follow physically sensible trends (e.g., smooth variation with controlling parameters, reasonable ordering between materials) and whether their magnitudes fall within acceptable numerical ranges. The final reward is a weighted combination of the scores from the individual stages. Simply reporting pre‑determined numbers without running the genuine computational pipeline will not satisfy the structural and trend checks.
