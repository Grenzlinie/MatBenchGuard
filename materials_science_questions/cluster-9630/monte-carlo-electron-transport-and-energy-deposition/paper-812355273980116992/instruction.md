# Auroral proton beam spreading Monte Carlo simulation

## Problem background
Auroral protons precipitating into the Earth's upper atmosphere undergo charge exchange and electron stripping collisions with ambient neutral species (O, N₂, O₂). These processes convert the initially field-aligned proton beam into fast hydrogen atoms that can travel across magnetic field lines, causing the beam to spread transversely. The spreading effect is important for interpreting auroral images, radar observations, and energy deposition patterns. This task reproduces a three-dimensional Monte Carlo simulation that quantifies the transverse spreading of a monoenergetic proton beam in a vertical magnetic field. The main goal is to compute the spatial dispersion of particle fluxes and determine how the beam width evolves with altitude.

## Approach
The simulation follows individual protons and hydrogen atoms through a collision-by-collision random walk in a plane-parallel, multispecies atmosphere given by the MSIS-90 empirical model. Particles are injected at 700 km with an isotropic downward angular distribution and a fixed energy, and tracked until their energy falls below 20 eV or they leave the domain. The magnetic field is uniform and vertical. The collision model includes charge exchange, electron stripping, ionization, excitation (treated as forward scattering with discrete energy loss), and elastic scattering (angular deflection and energy partitioning according to published cross-section data). The gyrophase of charged particles is updated explicitly between collisions. From the recorded particle positions, velocities, and species, one computes downwards fluxes in horizontal spatial bins at specific altitudes. Two derived quantities are then extracted: (1) the 80% effective beam radius of the combined downward H⁺+H flux at several altitudes, and (2) the azimuthally averaged radial profile of the downward H⁺ flux at a chosen altitude.

## Reproduction target
Implement the described Monte Carlo transport model for a 10 keV monoenergetic proton beam injected at 700 km in a vertical magnetic field, using the MSIS-90 atmosphere for the date, location, and geophysical conditions specified in the first workflow step and the collision cross sections referenced in the assets. After running 2 million test particles, post-process the simulation output to produce two CSV files under /app/outputs:

1. `beam_radii.csv` – the 80% effective beam radius (the radial distance from the central field line that encloses 80% of the total downward particle flux) of the combined downward H⁺ and H flux at altitudes 400, 350, 300, and 250 km, normalized to an incident total energy flux of 1 erg cm⁻² s⁻¹.
2. `flux_profile_350km.csv` – the azimuthally averaged, hemispherically averaged downward H⁺ flux as a function of radial distance at 350 km altitude (same incident flux normalization), for distances up to about 500 km.

The required column names and formats are defined in the workflow steps and output contract.

## Assets

- MSIS-90 neutral atmosphere model (msise00): https://pypi.org/project/msise00/
- Inelastic cross sections (Basu et al. 1987, 1993): 10.1029/JA092iA06p05920
- Elastic scattering cross sections (Kallio & Barabash, 2001) and energy partitioning (Galand et al., 1997): 10.1029/2000JA001388

## Workflow steps

### Step 1: Compute MSIS-90 atmosphere profiles
- Role: process
- Action: Run the MSIS-90 model (using the msise00 package or equivalent) for UT=0, 21 March 1999, geographic coordinates 65°N, 0°E, with Ap=15 and F10.7=150 to obtain vertical number density profiles n_i(z) for O, N₂, and O₂ from 700 km down to ~100 km on a sufficiently fine altitude grid.
- Evidence: none

### Step 2: Run 3D Monte Carlo proton transport simulation
- Role: process
- Action: Implement the collision-by-collision Monte Carlo simulation as described in the paper: inject 2×10⁶ protons with an isotropic downward hemispheric angular distribution at 700 km altitude, monoenergetic energy 10 keV, vertical magnetic field. For each particle, propagate through the atmosphere using optical depth sampling, handle collisions (charge exchange, electron stripping, ionization, excitation, elastic) using cross sections from Basu et al. (1987) and Kallio & Barabash (2001), forward scattering for inelastic collisions, angular deflection and energy partitioning for elastic collisions, explicit gyrophase update for charged segments. Track particles until energy <20 eV or escape. Record particle positions, species, and velocity directions to allow computation of downward fluxes in spatial bins.
- Evidence: none

### Step 3: Compute effective beam radii of downward H⁺+H fluxes
- Role: scored (load-bearing)
- Action: From the simulation outputs, compute the 80% effective beam radius for the combined downward H⁺ and H fluxes at altitudes 400, 350, 300, and 250 km. The beam radius is defined as the radial distance from the incident magnetic field line that encloses 80% of the total downward particle flux at that altitude. Normalize fluxes to an incident total energy flux of 1 erg cm⁻² s⁻¹.
- Output file: `/app/outputs/beam_radii.csv`
- Format: csv
- Contract: columns: altitude_km (float), beam_radius_km (float)
- Scoring: scored by hidden verifier

### Step 4: Compute downward H⁺ flux radial profile at 350 km
- Role: scored
- Action: From the simulation outputs, extract the azimuthally averaged hemispherically averaged downward H⁺ flux as a function of radial distance from the central field line at altitude 350 km. Use the same incident flux normalization (1 erg cm⁻² s⁻¹). Provide flux values for radial distances spanning the spreading region (e.g., from 0 to ~500 km).
- Output file: `/app/outputs/flux_profile_350km.csv`
- Format: csv
- Contract: columns: radial_distance_km (float), downward_Hplus_flux (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/beam_radii.csv`
- `/app/outputs/flux_profile_350km.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### beam_radii.csv
- path: `/app/outputs/beam_radii.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective beam radius (80% radius) of downward H⁺+H fluxes at altitudes 400, 350, 300, and 250 km.
- schema:
  - `type`: table
  - `required_columns`: `altitude_km`, `beam_radius_km`
  - `units`:
    - `altitude_km`: km
    - `beam_radius_km`: km

### flux_profile_350km.csv
- path: `/app/outputs/flux_profile_350km.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Azimuthally averaged downward H⁺ flux as a function of radial distance at 350 km altitude.
- schema:
  - `type`: table
  - `required_columns`: `radial_distance_km`, `downward_Hplus_flux`
  - `units`:
    - `radial_distance_km`: km
    - `downward_Hplus_flux`: arbitrary units normalized to 1 erg/cm²/s total flux

Notes: The checker will compare the submitted beam radii to paper-reported reference values with an appropriate tolerance, and will verify the flux profile shape and values against the published profile using a tolerance that accounts for statistical and implementation differences. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "beam_radii.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "altitude_km",
          "beam_radius_km"
        ],
        "units": {
          "altitude_km": "km",
          "beam_radius_km": "km"
        }
      },
      "description": "Effective beam radius (80% radius) of downward H⁺+H fluxes at altitudes 400, 350, 300, and 250 km."
    },
    {
      "file": "flux_profile_350km.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "radial_distance_km",
          "downward_Hplus_flux"
        ],
        "units": {
          "radial_distance_km": "km",
          "downward_Hplus_flux": "arbitrary units normalized to 1 erg/cm²/s total flux"
        }
      },
      "description": "Azimuthally averaged downward H⁺ flux as a function of radial distance at 350 km altitude."
    }
  ],
  "notes": "The checker will compare the submitted beam radii to paper-reported reference values with an appropriate tolerance, and will verify the flux profile shape and values against the published profile using a tolerance that accounts for statistical and implementation differences. No gold values or tolerances are disclosed here."
}
```

## How you are scored
Your solution is evaluated by a hidden verifier that has access to reference values but cannot be seen by you. The verifier independently reads the two scored output files and compares them to the reference, checking quantitative agreement, monotonic behaviour, and shape. Each artifact carries a weight (the beam radii carry a higher weight), and the final reward is a weighted sum in the range [0, 1]. You must produce the artifacts by genuinely executing the simulation and analysis; simply writing down guessed numbers or copying from the original paper is unlikely to pass, because the tolerance and reference values are unknown to you. No tolerance is disclosed – aim to reproduce the physics as faithfully as possible.
