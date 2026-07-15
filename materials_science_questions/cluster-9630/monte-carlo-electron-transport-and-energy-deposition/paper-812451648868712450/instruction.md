# Monte Carlo electron transport simulation for TEM-EDX Si substrate noise analysis

## Problem background
Transmission electron microscope (TEM) specimens prepared by focused ion beam (FIB) can produce contaminating X-rays that degrade quantitative elemental analysis. When the electron beam is positioned on a thin film, electrons scattered forward or backward can strike the underlying Si substrate sidewalls, generating a strong Si K X-ray signal that adds to the spectrum of the analysed region. The magnitude of this substrate noise depends on the geometry of the FIB-cut specimen. This task reproduces a Monte Carlo simulation that models electron scattering and X-ray generation in such specimens, allowing the Si noise and true signal intensities to be computed for different specimen shapes and thin-film materials.

## Approach
The core idea is to use a Monte Carlo method to simulate electron transport and then compute the resulting X-ray intensities.

**Electron transport simulation.** A 200 keV electron beam impinges on the thin film (which may be a Ti or W layer) above a Si substrate with sidewalls defined by the specimen geometry. Elastic scattering is modelled with the Rutherford cross section, and the continuous energy loss between scattering events follows Bethe's stopping power approach. A large number of electron trajectories are tracked; each time an electron hits a Si sidewall surface, it is counted to obtain the probability of electron collision with the sidewall.

**X-ray intensity calculation.** The generated Si K noise intensity as well as the Ti or W signal intensity are calculated using the Philibert–Tixier method, which includes absorption correction and the energy attenuation of electrons. The required ionization cross sections and fluorescence yields are taken from the tabulation of Zaluzec (1979).

**Specimen geometry.** The specimens are characterised by the parameters T (bulk thickness), U (upper length), L (lower length), D (depth of removed area), W (width of removed area), and α (tangential angle between D and L). The following dimensions are used:

| Specimen | T (μm) | U (μm) | L (μm) | D (μm) | W (μm) | α (°) |
|----------|--------|--------|--------|--------|--------|-------|
| A        | 49     | 19.5   | 29.0   | 12.5   | 18.0   | 67    |
| B        | 26     | 16.5   | 9.5    | 16.0   | 15.0   | 31    |
| C        | 34     | 18.0   | 15.5   | 51.5   | 16.0   | 17    |
| U        | 26     | 26.0   | 0.0    | 20.0   | 17.0   | 0     |

Material properties:
- Si substrate: Z=14, density 2.33 g/cm³
- Ti thin film: Z=22, density 4.51 g/cm³
- W thin film: Z=74, density 19.3 g/cm³

The simulation is run for each of the four specimens (A, B, C, U) and for both a Ti and a W thin film region (8 combinations in total), yielding the electron–sidewall collision probabilities that are then converted into X-ray intensities.

## Reproduction target
Run the Monte Carlo simulation as described and compute the X-ray intensities for all eight specimen–region combinations. Output a single CSV file containing, for each case, the specimen label, the thin-film material (W or Ti), the signal intensity in cps, and the Si noise intensity in cps. This output is the primary scored artifact. The computed intensities should reflect the physics of electron scattering and X-ray generation described in the approach; the scoring will compare them against reference values obtained from a correct implementation.

## Assets

- Zaluzec ionization cross section and fluorescence yield data

## Workflow steps

### Step 1: Prepare specimen geometry and materials
- Role: process
- Action: Define geometric parameters (T, U, L, D, W, alpha) for specimens A, B, C, and U as given in the specimen dimensions table. Set up material properties: Si substrate (Z=14, density 2.33 g/cm3), Ti thin film (Z=22, density 4.51 g/cm3), W thin film (Z=74, density 19.3 g/cm3).
- Evidence: none

### Step 2: Monte Carlo electron transport simulation
- Role: process
- Action: Implement a Monte Carlo simulation of electron scattering. Use Rutherford scattering cross section for elastic scattering and Bethe continuous energy loss for inelastic losses. Simulate 200 keV electron beam incident on the thin film (Ti or W region) positioned above a Si bulk with sidewalls defined by the geometry. Track many electron trajectories; for each specimen and thin-film material, compute the probability of a scattered electron hitting the Si sidewall surface.
- Evidence: `/app/outputs/electron_collision_probability.csv`

### Step 3: Compute X-ray intensities
- Role: scored (load-bearing)
- Action: Using the collision probabilities from the previous step, compute the generated X-ray intensities using the Philibert-Tixier method: apply absorption correction, Zaluzec ionization cross sections, and fluorescence yields. Calculate the Si K noise intensity (cps) and the W or Ti signal intensity (cps) for each specimen and region (Ti or W). Output a CSV file.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: CSV with columns: specimen (string: A/B/C/U), region (string: W/Ti), signal_cps (float), noise_Si_cps (float). Exactly 8 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed X-ray signal and noise intensities for each specimen (A, B, C, U) and each thin-film region (W, Ti).
- schema:
  - `type`: table
  - `required_columns`: `specimen`, `region`, `signal_cps`, `noise_Si_cps`
  - `items`:
    - `specimen`:
      - `type`: string
    - `region`:
      - `type`: string
    - `signal_cps`:
      - `type`: float
      - `unit`: cps
    - `noise_Si_cps`:
      - `type`: float
      - `unit`: cps

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "specimen",
          "region",
          "signal_cps",
          "noise_Si_cps"
        ],
        "items": {
          "specimen": {
            "type": "string"
          },
          "region": {
            "type": "string"
          },
          "signal_cps": {
            "type": "float",
            "unit": "cps"
          },
          "noise_Si_cps": {
            "type": "float",
            "unit": "cps"
          }
        }
      },
      "description": "Computed X-ray signal and noise intensities for each specimen (A, B, C, U) and each thin-film region (W, Ti)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier examines your "/app/outputs/simulation_results.csv" file. It compares the eight reported Si noise and signal intensities against reference values (derived from a faithful implementation of the model) using an appropriate tolerance, and it also checks whether the intensities follow expected structural relationships (e.g., ordering across specimens and materials). The overall reward is the weighted sum of these checks; no single approximate guess passes, and you must implement the full simulation pipeline to earn a high score. All other steps are required for the workflow but are not individually scored.
