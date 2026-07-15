# Monte Carlo Electron Transport in Air: Attenuation and Beam Spreading

## Problem background
Understanding how high-energy electron beams propagate and deposit energy in atmospheric air is important for accelerator design, radiation dosimetry, and atmospheric physics. When a beam of relativistic electrons enters air, scattering and energy loss cause the beam to spread and attenuate with distance. The spatial distribution of electron number density and energy density as a function of radial distance from the beam axis determines key beam characteristics such as the axial attenuation factor and effective beam width. This task investigates these properties for monoenergetic electron beams in air through computational simulation.

## Approach
The primary method is Monte Carlo particle transport. Individual electrons are tracked as they interact with standard atmospheric air (1 atm, 20°C), undergoing elastic and inelastic collisions that change their direction and energy. Electrons are launched from a uniform circular beam of 2 cm diameter, incident normally on a planar boundary, with initial kinetic energies of 400 keV and 600 keV. Detection planes perpendicular to the beam axis at chosen distances (10, 20, 40, 60, and 100 cm) record the number of electrons and their total energy in each radial bin. Running a large number of primary electrons (millions) yields radial distributions of electron number density per area (dN/dS, electrons/cm² per emitted electron) and energy density per area (dE/dS, keV/cm² per emitted electron). The simulation should be implemented with an open-source Monte Carlo toolkit (e.g., Geant4, PENELOPE, or EGSnrc) that provides electromagnetic physics models for this energy range.

## Reproduction target
Produce a single CSV file containing the radial profiles from the simulation described above. The file must include columns: `energy_keV` (400 or 600), `distance_cm` (10, 20, 40, 60, 100), `radius_cm`, `dN_dS` (electrons/cm² per emitted electron), and `dE_dS` (keV/cm² per emitted electron). The profiles must be monotonically non‑increasing with radius for each (energy, distance) combination and must cover a radial range sufficient to capture the full spread of the beam. The checker will derive from your CSV the on‑axis density attenuation factor after 100 cm, the beam diameters at which local electron density falls to 1/10 of the on‑axis value at each distance, and the beam half‑width at 100 cm; these derived quantities will be compared against hidden reference values. You do not need to compute or report the derived quantities yourself—only the raw radial profiles are submitted.

## Assets

- Open-source Monte Carlo particle transport toolkit: https://geant4.web.cern.ch/

## Workflow steps

### Step 1: Monte Carlo electron transport simulation
- Role: scored (load-bearing)
- Action: Using a publicly available open-source Monte Carlo particle transport toolkit (e.g., Geant4, PENELOPE, EGSnrc), simulate monoenergetic electrons with kinetic energies 400 keV and 600 keV. The electrons are normally incident on atmospheric air from a uniform circular beam of initial diameter 2 cm. Track the electrons and score their number (dN/dS) and energy (dE/dS) on detection planes perpendicular to the beam axis at propagation distances of 10, 20, 40, 60, and 100 cm. Normalize the results to one emitted primary electron and output the radial profiles in a single CSV file.
- Output file: `/app/outputs/electron_radial_profiles.csv`
- Format: csv
- Contract: CSV with columns: energy_keV (400 or 600), distance_cm (10,20,40,60,100), radius_cm (positive float, radial coordinate from beam axis), dN_dS (electron number density per area per emitted electron, electrons/cm²), dE_dS (energy density per area per emitted electron, keV/cm²). Data should cover a sufficient radial range to capture beam spreading and must be monotonically non-increasing with radius for each (energy,distance) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electron_radial_profiles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electron_radial_profiles.csv
- path: `/app/outputs/electron_radial_profiles.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Radial distributions of electron number density and energy density for 400 keV and 600 keV electrons at propagation distances of 10, 20, 40, 60, and 100 cm in air, normalized to one emitted electron. The checker will recompute on-axis attenuation factors, beam diameters at 1/10 on-axis density, and half-widths from these profiles.
- schema:
  - `type`: table
  - `required_columns`: `energy_keV`, `distance_cm`, `radius_cm`, `dN_dS`, `dE_dS`
  - `units`:
    - `energy_keV`: keV
    - `distance_cm`: cm
    - `radius_cm`: cm
    - `dN_dS`: electrons/cm^2 per emitted electron
    - `dE_dS`: keV/cm^2 per emitted electron

Notes: The checker recomputes the derived quantities (axial density attenuation after 100 cm, beam diameters at factor‑10 reduction, and beam half‑widths) from the submitted radial profiles and compares them against paper‑reported reference values using appropriate tolerances. The simulation step itself is load‑bearing; the radial profiles cannot be guessed without running a genuine Monte Carlo transport code.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electron_radial_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_keV",
          "distance_cm",
          "radius_cm",
          "dN_dS",
          "dE_dS"
        ],
        "units": {
          "energy_keV": "keV",
          "distance_cm": "cm",
          "radius_cm": "cm",
          "dN_dS": "electrons/cm^2 per emitted electron",
          "dE_dS": "keV/cm^2 per emitted electron"
        }
      },
      "description": "Radial distributions of electron number density and energy density for 400 keV and 600 keV electrons at propagation distances of 10, 20, 40, 60, and 100 cm in air, normalized to one emitted electron. The checker will recompute on-axis attenuation factors, beam diameters at 1/10 on-axis density, and half-widths from these profiles."
    }
  ],
  "notes": "The checker recomputes the derived quantities (axial density attenuation after 100 cm, beam diameters at factor‑10 reduction, and beam half‑widths) from the submitted radial profiles and compares them against paper‑reported reference values using appropriate tolerances. The simulation step itself is load‑bearing; the radial profiles cannot be guessed without running a genuine Monte Carlo transport code."
}
```

## How you are scored
Your submission will be scored automatically by a hidden verifier. The verifier first checks that `electron_radial_profiles.csv` is well‑formed (correct columns, data for both energies and all distances, monotonically non‑increasing radial profiles). It then recomputes from your profiles the following quantities: on‑axis density attenuation factor after 100 cm, beam diameters at which the local electron density drops to 1/10 of the on‑axis value for each distance, and the beam half‑width at 100 cm. Each derived quantity is compared to a reference value with a preset tolerance that accounts for statistical noise and implementation‑dependent differences. The final reward is a weighted combination of how many of these checks pass; structural (monotonicity) checks carry low weight, while correct attenuation/diameter/half‑width values carry high weight. To score well, you must run a genuine Monte Carlo simulation with sufficient statistics; simply guessing or fabricating the profiles will not match the reference within tolerance.
