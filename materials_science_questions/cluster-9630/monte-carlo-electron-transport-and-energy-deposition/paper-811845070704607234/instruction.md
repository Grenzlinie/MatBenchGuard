# Monte Carlo optimum lead thickness for lead-activation detectors

## Problem background
Lead-activation detectors measure pulsed neutron yield by counting gamma rays emitted from radioactive lead nuclides produced by neutron reactions. The detector consists of a cylindrical lead sheath surrounding a central detector volume. Because lead strongly attenuates the gamma rays it produces, the detection efficiency depends on the thickness of the lead wall: if the wall is too thin, fewer neutrons interact; if too thick, the gamma rays are absorbed before reaching the detector. Consequently, for a given detector geometry and neutron energy, there exists an optimum lead thickness that maximizes detection efficiency. The goal of this task is to determine that optimum thickness from a Monte Carlo simulation.

## Approach
The approach is to simulate the neutron and gamma transport through a simplified model of the lead-activation detector using an open‑source Monte Carlo particle transport code (OpenMC recommended). The lead sheath is modelled as a hollow cylinder of length 22 cm and inner diameter 12 cm, with a variable wall thickness. An isotropic point neutron source is placed 15 cm from the front face along the cylinder axis. The simulation tallies the flux of gamma rays at the centre of the detector for the two characteristic lines (0.571 MeV and 1.064 MeV) produced by the decay of Pb‑207m. Detection efficiency at each thickness is obtained by normalising the combined gamma‑ray count rate. By sweeping the thickness over a range and recording the efficiency for each thickness, the thickness that yields the peak efficiency is identified as the optimum. The process is repeated for two incident neutron energies to test whether the optimum thickness depends on energy.

## Reproduction target
Produce a CSV file listing the optimum lead thickness for neutron energies of 2 MeV and 14 MeV. For each energy, run Monte Carlo simulations for lead thicknesses between 0.5 cm and 5.0 cm with sufficient source particles (at least 1e7 NPS per point) to reduce statistical noise. At each thickness compute the normalized detection efficiency from the flux of the 0.571 MeV and 1.064 MeV gamma rays at the detector centre. Determine the thickness that maximises efficiency for each energy and write one row per energy to 'optimum_thicknesses.csv' (columns: energy_MeV, optimum_thickness_cm). The computed optimum thicknesses are expected to show whether the optimum is energy‑independent.

## Assets

- OpenMC Monte Carlo particle transport code: https://docs.openmc.org/en/stable/
- ENDF/B-VIII.0 nuclear data library: https://openmc.org/data/

## Workflow steps

### Step 1: Define detector geometry, materials, and neutron source
- Role: process
- Action: Set up the OpenMC (or alternative Monte Carlo) model: define a cylindrical lead sheath of length 22 cm, inner diameter 12 cm, variable wall thickness; natural lead material; an isotropic point neutron source at 15 cm from the front along the cylinder axis with a Gaussian time distribution (FWHM 20 ns). Ignore back window and electron transport (bremsstrahlung). Prepare the input model that can be executed for different thicknesses and source energies.
- Evidence: `/app/outputs/model_input.txt`

### Step 2: Run efficiency simulations for 14 MeV and 2 MeV neutrons over thickness sweep
- Role: process
- Action: For neutron energies 2 MeV and 14 MeV, run OpenMC simulations for lead thicknesses from 0.5 cm to 5.0 cm in fine steps (e.g., 0.1 cm) with sufficient source particles (≥ 1e7 NPS). At each thickness, tally the gamma-ray flux at the detector centre for the 0.571 MeV and 1.064 MeV lines, normalize to obtain detection efficiency. Save the raw efficiency vs. thickness data for each energy to a JSON file.
- Evidence: `/app/outputs/efficiency_raw_data.json`

### Step 3: Determine optimum lead thicknesses and write scored CSV
- Role: scored (load-bearing)
- Action: From the efficiency vs. thickness data for each energy, find the thickness that maximizes efficiency (optimum thickness). Create a CSV file 'optimum_thicknesses.csv' with columns energy_MeV (float) and optimum_thickness_cm (float), containing one row for 2 MeV and one row for 14 MeV.
- Output file: `/app/outputs/optimum_thicknesses.csv`
- Format: csv
- Contract: CSV with columns: energy_MeV (float), optimum_thickness_cm (float). At least two rows: one for 2 MeV and one for 14 MeV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimum_thicknesses.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimum_thicknesses.csv
- path: `/app/outputs/optimum_thicknesses.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The optimum lead thickness determined from Monte Carlo simulations for 2 MeV and 14 MeV neutrons. Each row gives the energy and the thickness that maximized detection efficiency.
- schema:
  - `type`: table
  - `required_columns`: `energy_MeV`, `optimum_thickness_cm`
  - `units`:
    - `energy_MeV`: MeV
    - `optimum_thickness_cm`: cm
  - `description`: Optimum lead thickness for each neutron energy.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimum_thicknesses.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_MeV",
          "optimum_thickness_cm"
        ],
        "units": {
          "energy_MeV": "MeV",
          "optimum_thickness_cm": "cm"
        },
        "description": "Optimum lead thickness for each neutron energy."
      },
      "description": "The optimum lead thickness determined from Monte Carlo simulations for 2 MeV and 14 MeV neutrons. Each row gives the energy and the thickness that maximized detection efficiency."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your 'optimum_thicknesses.csv' and compares the reported optimum thickness for each energy to a reference expectation, as well as checking that the two energies yield similar optimum thicknesses (consistent with the claimed energy‑independence). The verifier may also inspect the intermediate evidence files to confirm the simulation pipeline was executed. Each workflow stage carries a weight; the final combined reward (a value between 0 and 1) reflects how well the outputs match the expected physical behaviour. Simply reporting numbers without running the full simulation will not succeed.
