# Simulation of TGF-driven secondary electron beams and magnetospheric transport

## Problem background
Terrestrial Gamma-ray Flashes (TGFs) are millisecond bursts of high-energy photons produced in thunderstorms. As the gamma rays propagate upward through the atmosphere they interact with air atoms via Compton scattering and pair production, generating secondary electrons and positrons. Most of these secondary leptons are absorbed, but above about 40 km a significant fraction can escape the atmosphere and propagate along geomagnetic field lines into the inner magnetosphere. Understanding this mechanism requires simulating the full chain: from the gamma-ray source, through the atmospheric interactions, to the resulting electron beams and their detectable properties in low-Earth orbit. This task aims to computationally reproduce the key signatures of such electron beams – the energy spectrum, the spatial extent, and the time-intensity profile at satellite altitude.

## Approach
Use a Monte Carlo particle transport toolkit (e.g., GEANT4) to simulate a TGF gamma-ray source located at 21 km altitude, emitting vertically upward with a gamma-ray energy spectrum typical of RHESSI TGFs – a power law with index around -1.2 and an exponential cutoff near 40 MeV. The atmosphere is modeled using the US Standard Atmosphere 1976, including density and composition as functions of altitude. Track all photon and electron/positron interactions: Compton scattering, pair production, photoelectric absorption, ionization, Møller scattering, and bremsstrahlung. Record the secondary electrons and positrons that escape above 40 km. Then propagate this escaping population along a geomagnetic field line to a satellite altitude of 500 km, using the IGRF-10 geomagnetic field model for a representative event location and date. Conserve the first adiabatic invariant to account for pitch-angle focusing and magnetic mirroring. From these simulations, extract three quantitative characteristics: (1) the differential energy spectrum of escaping electrons, (2) the radial spatial distribution of electron number per unit area at 500 km, and (3) the time-dependent count rate at the satellite that arises from the propagation and mirroring of the electron beam.

## Reproduction target
Produce the following three scored artifacts:

- `energy_spectrum.csv`: a table of electron energy (MeV) vs differential flux (arbitrary units per MeV) that demonstrates the escaping electron population extends to at least 30 MeV, with non-zero flux at the highest energies.
- `spatial_distribution.csv`: a radial profile (radius in km, flux per area) at 500 km altitude showing that the electron beam is approximately an order of magnitude narrower than the parent gamma-ray beam (which is known to be ~100 km wide). The electron beam’s half-width at half-max must fall within a plausible compact range indicative of field-line confinement.
- `time_profile.csv`: a time series (time in ms, count rate) that exhibits two distinct peaks — a direct pulse followed by a mirrored pulse — consistent with pitch-angle focusing and magnetic mirroring. The separation and relative amplitude of the peaks must reflect the propagation geometry.

All files must follow the formats given in the workflow steps and output contract.

## Assets

- GEANT4 Monte Carlo toolkit: https://geant4.web.cern.ch/
- IGRF-10 Geomagnetic Field Model: https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html
- US Standard Atmosphere 1976: https://www.pdas.com/atmos.html

## Workflow steps

### Step 1: Monte Carlo simulation of TGF gamma-ray interactions and secondary lepton escape
- Role: process
- Action: Set up a TGF gamma-ray source at 21 km altitude beamed vertically upward with a gamma-ray energy spectrum typical of RHESSI TGFs (power-law index ~-1.2, exponential cutoff ~40 MeV). Simulate photon and electron/positron transport through the US Standard Atmosphere using GEANT4, including Compton scattering, pair production, photoelectric absorption, ionization, Møller scattering, and bremsstrahlung. Record escaping secondary electrons and positrons above 40 km altitude.
- Evidence: `/app/outputs/mc_simulation_log.txt`

### Step 2: Magnetospheric propagation of electron beam along geomagnetic field lines
- Role: process
- Action: Propagate the escaping electron distribution from the MC simulation along the geomagnetic field line to a satellite altitude of 500 km using the IGRF-10 geomagnetic field model for a representative event location and date. Conserve the first adiabatic invariant to include pitch angle focusing and magnetic mirroring. Compute the time-dependent electron count rate at the satellite.
- Evidence: `/app/outputs/propagation_log.txt`

### Step 3: Write escaping electron energy spectrum
- Role: scored
- Action: From the atmospheric Monte Carlo simulation results, produce the differential energy spectrum of escaping electrons (energy vs differential flux). Ensure the spectrum extends to at least 30 MeV with non-zero flux.
- Output file: `/app/outputs/energy_spectrum.csv`
- Format: csv
- Contract: columns: energy_MeV (float, MeV), differential_flux (float, arbitrary units per MeV)
- Scoring: scored by hidden verifier

### Step 4: Write spatial distribution of electrons at 500 km
- Role: scored
- Action: From the MC simulation results, produce the radial spatial distribution of escaping electrons at 500 km altitude (radius vs flux per area). The electron beam width should be approximately an order of magnitude smaller than the gamma-ray beam.
- Output file: `/app/outputs/spatial_distribution.csv`
- Format: csv
- Contract: columns: radius_km (float, km), flux_per_area (float, arbitrary units per area)
- Scoring: scored by hidden verifier

### Step 5: Write electron beam time-intensity profile
- Role: scored (load-bearing)
- Action: From the magnetospheric propagation results, produce the simulated time-intensity profile (time vs count rate) showing the characteristic double-peak shape due to magnetic mirroring.
- Output file: `/app/outputs/time_profile.csv`
- Format: csv
- Contract: columns: time_ms (float, milliseconds), count_rate (float, arbitrary units)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_spectrum.csv`
- `/app/outputs/spatial_distribution.csv`
- `/app/outputs/time_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_spectrum.csv
- path: `/app/outputs/energy_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Differential energy spectrum of escaping secondary electrons. Checker verifies that the spectrum contains a data point with energy ≥ 30 MeV and non-zero flux.
- schema:
  - `type`: table
  - `required_columns`: `energy_MeV`, `differential_flux`
  - `units`:
    - `energy_MeV`: MeV
    - `differential_flux`: arbitrary units per MeV

### spatial_distribution.csv
- path: `/app/outputs/spatial_distribution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Radial distribution of electron number per unit area at 500 km altitude. Checker verifies that the electron beam half-width at half-max is between 5 and 20 km, implying a factor ~10 narrower than the gamma-ray beam.
- schema:
  - `type`: table
  - `required_columns`: `radius_km`, `flux_per_area`
  - `units`:
    - `radius_km`: km
    - `flux_per_area`: arbitrary units per area

### time_profile.csv
- path: `/app/outputs/time_profile.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Simulated electron count rate vs time at satellite altitude, showing two distinct peaks separated by 5–15 ms with the second peak amplitude 0.5–2× the first. This artifact carries the highest weight and is load-bearing, requiring the full simulation chain.
- schema:
  - `type`: table
  - `required_columns`: `time_ms`, `count_rate`
  - `units`:
    - `time_ms`: ms
    - `count_rate`: arbitrary units

Notes: All outputs are produced from the Monte Carlo and propagation pipeline. The checker performs structural audits: for energy_spectrum.csv it checks for presence of non-zero flux at >=30 MeV; for spatial_distribution.csv it computes the half-width at half-max and verifies it lies in 5–20 km; for time_profile.csv it identifies two distinct peaks with separation 5–15 ms and second-to-first amplitude ratio between 0.5 and 2.0. No gold numerical values are disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_MeV",
          "differential_flux"
        ],
        "units": {
          "energy_MeV": "MeV",
          "differential_flux": "arbitrary units per MeV"
        }
      },
      "description": "Differential energy spectrum of escaping secondary electrons. Checker verifies that the spectrum contains a data point with energy ≥ 30 MeV and non-zero flux."
    },
    {
      "file": "spatial_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "radius_km",
          "flux_per_area"
        ],
        "units": {
          "radius_km": "km",
          "flux_per_area": "arbitrary units per area"
        }
      },
      "description": "Radial distribution of electron number per unit area at 500 km altitude. Checker verifies that the electron beam half-width at half-max is between 5 and 20 km, implying a factor ~10 narrower than the gamma-ray beam."
    },
    {
      "file": "time_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ms",
          "count_rate"
        ],
        "units": {
          "time_ms": "ms",
          "count_rate": "arbitrary units"
        }
      },
      "description": "Simulated electron count rate vs time at satellite altitude, showing two distinct peaks separated by 5–15 ms with the second peak amplitude 0.5–2× the first. This artifact carries the highest weight and is load-bearing, requiring the full simulation chain."
    }
  ],
  "notes": "All outputs are produced from the Monte Carlo and propagation pipeline. The checker performs structural audits: for energy_spectrum.csv it checks for presence of non-zero flux at >=30 MeV; for spatial_distribution.csv it computes the half-width at half-max and verifies it lies in 5–20 km; for time_profile.csv it identifies two distinct peaks with separation 5–15 ms and second-to-first amplitude ratio between 0.5 and 2.0. No gold numerical values are disclosed."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that examines each scored output file independently. The verifier does not compare your outputs to a single published number; instead it checks structural properties that a correct simulation chain must produce:

- For `energy_spectrum.csv`, it verifies that there is a data point with energy ≥ 30 MeV and that the corresponding flux is non-zero.
- For `spatial_distribution.csv`, it computes the half-width at half-max (HWHM) of the radial electron distribution and confirms that this width lies within a range consistent with an electron beam roughly 10× narrower than the gamma-ray beam.
- For `time_profile.csv`, it identifies two distinct peaks, measures their separation in time, and compares the amplitude of the second peak to the first. The score reflects whether these features match the expected signature of magnetic mirroring.

Each artifact carries a weight, and the total reward is the weighted sum. The `time_profile.csv` is load-bearing and receives the largest weight because it can only be produced by genuinely executing the atmospheric Monte Carlo and magnetospheric propagation steps. Reporting values that look plausible or fabricating files will not succeed; the verifier’s criteria are quantitative and require the outputs to be internally consistent with a physics-based simulation chain.
