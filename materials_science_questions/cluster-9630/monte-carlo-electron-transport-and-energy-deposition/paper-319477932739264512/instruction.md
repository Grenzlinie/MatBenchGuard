# Monte Carlo electron transport through foil and air gap

## Problem background
Beta‑voltaic batteries convert nuclear decay energy into electricity using semiconductor structures. Diamond is a promising material due to its wide bandgap and high radiation resistance. Realistic experimental testing requires a beta source with a broad energy spectrum and near‑isotropic angular distribution, which is difficult to achieve with real isotopes. In one experimental approach, a wide‑aperture electron beam (initially monoenergetic at high energy) was scattered by a thin aluminium foil and an air gap to produce an electron distribution that approximates a real beta source. Monte Carlo simulations were used to characterise the energy and angular distribution of the electrons reaching the converter aperture. This task focuses on reproducing those simulations.

## Approach
The central method is a Monte Carlo simulation of electron transport through matter. Electrons are emitted from a rectangular source, then pass through a thin aluminium foil and an air gap, undergoing scattering. A circular detector aperture records the electrons that reach it. For each recorded electron, the kinetic energy and the incidence angle relative to the foil normal are saved. From these recorded events the average energy and average angle can be computed. The simulation must be performed with an open‑source Monte Carlo toolkit such as Geant4, using the exact geometric and material parameters specified in the workflow steps. The resulting CSV file will be checked by computing mean energy and mean angle and comparing them to reference values.

## Reproduction target
Produce a CSV file (`/app/outputs/electrons.csv`) containing the kinetic energy (keV) and incidence angle (degrees) of every electron that reaches the circular converter aperture (2.6 mm diameter) after scattering. The hidden verifier will compute the arithmetic mean of the energy values and the arithmetic mean of the angle values from this file and compare those means to hidden reference windows derived from the experimental study. Your submission is considered successful if the computed means fall within those windows. The exact reference values and tolerances are not provided; you must obtain stable mean estimates by running a Monte Carlo simulation with adequate statistics.

## Assets

- Geant4: https://geant4.web.cern.ch/

## Workflow steps

### Step 1: Monte Carlo simulation of electron transport
- Role: scored (load-bearing)
- Action: Using a Monte Carlo particle transport toolkit (e.g. Geant4), set up a geometry consisting of: a 12×20 mm planar electron source emitting 110 keV electrons uniformly across its surface; a 14 μm thick aluminum foil immediately after; a 17 mm air gap; and a circular detector of diameter 2.6 mm representing the converter aperture, positioned at the end of the air gap. Track electrons through the foil and air. For each electron that reaches the detector, record its kinetic energy in keV and its angle relative to the foil normal in degrees. Write all recorded events to electrons.csv under /app/outputs.
- Output file: `/app/outputs/electrons.csv`
- Format: csv
- Contract: CSV with two columns: 'energy_kev' (float, kinetic energy in keV) and 'angle_deg' (float, incidence angle in degrees relative to foil normal). Each row corresponds to one electron.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electrons.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electrons.csv
- path: `/app/outputs/electrons.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file containing kinetic energy and incidence angle for each electron that reaches the 2.6 mm diameter converter aperture after passing through a 14 μm Al foil and 17 mm air gap. The checker recomputes the mean energy and mean angle from this file and compares them to hidden reference windows derived from the paper's reported values.
- schema:
  - `type`: table
  - `required_columns`: `energy_kev`, `angle_deg`
  - `units`:
    - `energy_kev`: keV
    - `angle_deg`: degrees
  - `items`: object
  - `required`: object

Notes: The agent must perform a Monte Carlo transport simulation using the publicly described geometry and beam parameters. The exact statistics (number of incident electrons) are not prescribed, but must be sufficient for stable mean values. The simulation may use any open-source MC toolkit (e.g., Geant4).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electrons.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_kev",
          "angle_deg"
        ],
        "units": {
          "energy_kev": "keV",
          "angle_deg": "degrees"
        },
        "items": {},
        "required": {}
      },
      "description": "CSV file containing kinetic energy and incidence angle for each electron that reaches the 2.6 mm diameter converter aperture after passing through a 14 μm Al foil and 17 mm air gap. The checker recomputes the mean energy and mean angle from this file and compares them to hidden reference windows derived from the paper's reported values."
    }
  ],
  "notes": "The agent must perform a Monte Carlo transport simulation using the publicly described geometry and beam parameters. The exact statistics (number of incident electrons) are not prescribed, but must be sufficient for stable mean values. The simulation may use any open-source MC toolkit (e.g., Geant4)."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/electrons.csv` and independently computes the mean of the `energy_kev` column and the mean of the `angle_deg` column. These two means are compared against hidden reference windows. If a computed mean falls within its window, you earn full credit for that metric; credit for a metric decreases the farther the mean is from the window. The final reward is a weighted combination of the energy and angle scores. The verifier’s tolerances are unknown; therefore your simulation must faithfully model the physics according to the specified geometry and produce statistically stable averages. Simply reporting numbers found in the literature is not sufficient.
