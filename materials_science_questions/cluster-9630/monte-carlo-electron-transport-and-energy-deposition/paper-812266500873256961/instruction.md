# Monte Carlo energy deposition and ion pair production in a layered atmosphere

## Problem background
Solar energetic particles (SEPs) precipitating into Earth's upper atmosphere ionize the neutral gas, producing NOx and HOx that catalytically destroy ozone. Accurately modeling the altitude-dependent ionization rates is essential for understanding atmospheric chemistry impacts. Traditional continuous-energy-loss models track only primary particles, but secondary electrons and bremsstrahlung photons can transport energy to lower altitudes, altering the ionization profile. This motivates a detailed Monte Carlo simulation that explicitly follows secondaries to refine the spatial distribution of energy deposition and ion pair production.

## Approach
The approach uses the GEANT4 particle transport toolkit to build a Monte Carlo model of particle precipitation in a plane-parallel atmosphere. The atmosphere is divided into 30 layers (29 equidistant from 0–100 km and one thicker top layer) with fixed composition (23.3 wt% O₂, 75.5 wt% N₂, 1.3 wt% Ar). Atmospheric profiles (pressure, density, temperature) are loaded from a publicly available standard atmosphere model for equatorial June conditions. The simulation tracks electromagnetic interactions for protons, electrons, positrons, alpha particles, and photons, including multiple scattering, ionization, bremsstrahlung, Compton scattering, pair production, and photoelectric effect. Mono‑energetic pencil beams (100 primary particles each) are run for a grid of proton energies (1–500 MeV, logarithmic steps) and electron energies (1–50 MeV) at incidence angles from 0° to 80°. The energy deposited per layer is recorded, and after dividing by layer thickness, linear energy transfer (LET) tables are built as a function of altitude, particle type, initial kinetic energy, and angle. These LET tables are the core intermediate product. For power-law studies, the tables are folded with isotropic differential intensity spectra I(E) ∝ E⁻ᵞ for γ = 0,1,2,3, yielding altitude profiles of energy deposition. For event-specific ion pair production, observed particle spectra from the October 22, 1989 and June 14, 1989 SEP events (protons from GOES or IMP‑8, electrons from IMP‑8 CPME) are fitted to broken power laws and then convolved with the LET tables, assuming 35 eV per ion pair and isotropic incidence. This produces separate proton, electron, and total ion pair production rate profiles.

## Reproduction target
The reproduction target consists of three scored artifacts produced by the pipeline: (1) an energy deposition profile table (`energy_deposition_powerlaw.csv`) that gives altitude‑resolved energy deposition (MeV/km) for proton and electron beams with power-law spectral indices 0, 1, 2, and 3; (2) an ion pair production rate profile for the October 22, 1989 SEP event (`ion_production_oct1989.csv`) that reports proton‑only, electron‑only, and total ion pair production rates (ion pairs cm⁻³ s⁻¹) as a function of altitude; (3) the corresponding profile for the June 14, 1989 event (`ion_production_jun1989.csv`). All CSV files must contain exactly 30 rows corresponding to the atmospheric layers and adhere to the specified column names and units. The October 1989 profile is the primary, load‑bearing objective; the other two artifacts are supporting but also carry weight.

## Assets

- GEANT4 Simulation Toolkit: https://geant4.web.cern.ch/
- Atmosphere model (NRLMSISE-00 or SLIMCAT/TOMCAT): https://ccmc.gsfc.nasa.gov/modelweb/models/nrlmsise00.php
- IMP-8 CPME electron data: https://cdaweb.gsfc.nasa.gov/
- GOES proton data: https://www.ngdc.noaa.gov/stp/satellite/goes/

## Workflow steps

### Step 1: Atmosphere model setup
- Role: process
- Action: Define a plane-parallel atmosphere with 30 layers: 29 equidistant layers from 0–100 km and one 10‑km layer containing the remaining mass above 100 km. Composition: 23.3 wt% O₂, 75.5 wt% N₂, 1.3 wt% Ar. Load pressure, density, and temperature height profiles from a publicly available standard atmosphere model (e.g., NRLMSISE-00) for equatorial June conditions. Set up GEANT4 geometry and material definitions.
- Evidence: `/app/outputs/atmosphere_setup.log`

### Step 2: Monte Carlo particle transport simulation
- Role: process
- Action: Run GEANT4 with the atmosphere model. Particle types: protons, electrons, positrons, α particles, photons. Physics list: multiple scattering, Compton scattering, ionization, photoelectric effect, gamma conversion, annihilation, pair production, bremsstrahlung. For protons: mono‑energetic pencil beams of 100 primaries each, energies 1–500 MeV in 109 logarithmic steps. For electrons: 1–50 MeV in 340 logarithmic steps. Incidence angles: 0°,10°,…,80°. Track secondaries down to a 1 m propagation cut‑off; switch to continuous energy loss at lower energies. Record energy deposited per atmospheric layer for each beam.
- Evidence: `/app/outputs/geant4_output.log`

### Step 3: LET table computation
- Role: process
- Action: Aggregate raw energy deposition per layer from step 02 for each particle type, kinetic energy, and angle. Divide by layer thickness to obtain linear energy transfer (LET = dE/dx) as a function of altitude, initial kinetic energy, and incidence angle. Store results as structured tables (e.g., HDF5 or a set of CSV files).
- Evidence: `/app/outputs/LET_tables.h5`

### Step 4: SEP spectral fitting
- Role: process
- Action: For the October 22, 1989 and June 14, 1989 SEP events, retrieve observed differential intensity spectra: protons from GOES (or IMP-8 for June) and electrons from IMP-8 CPME. Fit broken power-law functions I(E)=I₀·(E/E₀)^{−γ} with up to three segments, determining best-fit spectral indices and break energies. Output the fitted spectral parameters for each event and particle type.
- Evidence: `/app/outputs/fitted_spectra.json`

### Step 5: Power-law energy deposition profiles
- Role: scored
- Action: Using the LET tables from step 03, fold with isotropic power-law differential intensity spectra I(E) ∝ E^{−γ} for γ = 0, 1, 2, 3, separately for protons and electrons. For each γ, sum energy deposition over all energies and angles to obtain an altitude profile of deposited energy (MeV/km). Output a CSV with one row per atmospheric layer.
- Output file: `/app/outputs/energy_deposition_powerlaw.csv`
- Format: csv
- Contract: CSV; columns: altitude_km (float), p_gamma0 (float), p_gamma1 (float), p_gamma2 (float), p_gamma3 (float), e_gamma0 (float), e_gamma1 (float), e_gamma2 (float), e_gamma3 (float). Values in MeV/km per layer. One row per layer (30 layers).
- Scoring: scored by hidden verifier

### Step 6: Ion pair production rate for October 22, 1989 event
- Role: scored (load-bearing)
- Action: Fold the LET tables with the fitted proton and electron spectra (from step 04) for the October 1989 event, assuming isotropic angular distribution. Convert deposited energy to ion pair production rates using a mean ionization energy of 35 eV per ion pair. Compute separate contributions from protons and electrons, and the total.
- Output file: `/app/outputs/ion_production_oct1989.csv`
- Format: csv
- Contract: CSV; columns: altitude_km (float), proton_rate (float), electron_rate (float), total_rate (float). Rates in ion pairs cm⁻³ s⁻¹. One row per atmospheric layer (30 layers).
- Scoring: scored by hidden verifier

### Step 7: Ion pair production rate for June 14, 1989 event
- Role: scored
- Action: Fold LET tables with fitted spectra for the June 1989 event (from step 04) to produce ion pair production profiles, as in step 06.
- Output file: `/app/outputs/ion_production_jun1989.csv`
- Format: csv
- Contract: CSV; columns: altitude_km (float), proton_rate (float), electron_rate (float), total_rate (float). Rates in ion pairs cm⁻³ s⁻¹. One row per atmospheric layer (30 layers).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_deposition_powerlaw.csv`
- `/app/outputs/ion_production_oct1989.csv`
- `/app/outputs/ion_production_jun1989.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_deposition_powerlaw.csv
- path: `/app/outputs/energy_deposition_powerlaw.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Energy deposition altitude profiles for power-law SEP spectra (gamma=0..3) for protons and electrons.
- schema:
  - `type`: table
  - `required_columns`: `altitude_km`, `p_gamma0`, `p_gamma1`, `p_gamma2`, `p_gamma3`, `e_gamma0`, `e_gamma1`, `e_gamma2`, `e_gamma3`
  - `units`:
    - `altitude_km`: km
    - `p_gamma0`: MeV/km
    - `p_gamma1`: MeV/km
    - `p_gamma2`: MeV/km
    - `p_gamma3`: MeV/km
    - `e_gamma0`: MeV/km
    - `e_gamma1`: MeV/km
    - `e_gamma2`: MeV/km
    - `e_gamma3`: MeV/km

### ion_production_oct1989.csv
- path: `/app/outputs/ion_production_oct1989.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Ion pair production rate profile for the October 22, 1989 SEP event, split by particle type.
- schema:
  - `type`: table
  - `required_columns`: `altitude_km`, `proton_rate`, `electron_rate`, `total_rate`
  - `units`:
    - `altitude_km`: km
    - `proton_rate`: ion pairs cm⁻³ s⁻¹
    - `electron_rate`: ion pairs cm⁻³ s⁻¹
    - `total_rate`: ion pairs cm⁻³ s⁻¹

### ion_production_jun1989.csv
- path: `/app/outputs/ion_production_jun1989.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Ion pair production rate profile for the June 14, 1989 SEP event, split by particle type.
- schema:
  - `type`: table
  - `required_columns`: `altitude_km`, `proton_rate`, `electron_rate`, `total_rate`
  - `units`:
    - `altitude_km`: km
    - `proton_rate`: ion pairs cm⁻³ s⁻¹
    - `electron_rate`: ion pairs cm⁻³ s⁻¹
    - `total_rate`: ion pairs cm⁻³ s⁻¹

Notes: The ion_production_oct1989.csv is the mandatory load-bearing scored artifact; the other scored artifacts are supporting but also carry weight. All CSV files are expected to contain exactly 30 rows corresponding to the atmospheric layers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_deposition_powerlaw.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "altitude_km",
          "p_gamma0",
          "p_gamma1",
          "p_gamma2",
          "p_gamma3",
          "e_gamma0",
          "e_gamma1",
          "e_gamma2",
          "e_gamma3"
        ],
        "units": {
          "altitude_km": "km",
          "p_gamma0": "MeV/km",
          "p_gamma1": "MeV/km",
          "p_gamma2": "MeV/km",
          "p_gamma3": "MeV/km",
          "e_gamma0": "MeV/km",
          "e_gamma1": "MeV/km",
          "e_gamma2": "MeV/km",
          "e_gamma3": "MeV/km"
        }
      },
      "description": "Energy deposition altitude profiles for power-law SEP spectra (gamma=0..3) for protons and electrons."
    },
    {
      "file": "ion_production_oct1989.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "altitude_km",
          "proton_rate",
          "electron_rate",
          "total_rate"
        ],
        "units": {
          "altitude_km": "km",
          "proton_rate": "ion pairs cm⁻³ s⁻¹",
          "electron_rate": "ion pairs cm⁻³ s⁻¹",
          "total_rate": "ion pairs cm⁻³ s⁻¹"
        }
      },
      "description": "Ion pair production rate profile for the October 22, 1989 SEP event, split by particle type."
    },
    {
      "file": "ion_production_jun1989.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "altitude_km",
          "proton_rate",
          "electron_rate",
          "total_rate"
        ],
        "units": {
          "altitude_km": "km",
          "proton_rate": "ion pairs cm⁻³ s⁻¹",
          "electron_rate": "ion pairs cm⁻³ s⁻¹",
          "total_rate": "ion pairs cm⁻³ s⁻¹"
        }
      },
      "description": "Ion pair production rate profile for the June 14, 1989 SEP event, split by particle type."
    }
  ],
  "notes": "The ion_production_oct1989.csv is the mandatory load-bearing scored artifact; the other scored artifacts are supporting but also carry weight. All CSV files are expected to contain exactly 30 rows corresponding to the atmospheric layers."
}
```

## How you are scored
A hidden verifier inspects each scored output artifact. It first checks that every required file exists, has the correct format, and contains the expected columns and number of rows. Then it recomputes internal consistency checks and compares the submitted profiles against reference values (obtained from an independent re‑run of the same protocol or from digitized literature curves). Scoring for the energy deposition profiles rewards correct ordering across spectral indices and the characteristic altitude dependence of proton vs. electron deposition. For the ion pair production profiles, the verifier evaluates the shape (e.g., normalized correlation) and the integrated rate magnitude and splits the reward across the separate particle contributions. Simply reporting textbook numbers is not sufficient — the artifacts must be the genuine output of the simulation and analysis pipeline described in the workflow steps.
