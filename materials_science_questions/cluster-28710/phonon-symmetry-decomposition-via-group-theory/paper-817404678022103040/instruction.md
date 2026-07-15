# Beam inhibition in a triangular metallic photonic crystal at K-point

## Problem background
Triangular metallic photonic structures, formed by a periodic array of perfect-conductor cylinders in air, support Dirac cones in the transverse-magnetic (TM) band structure. For frequencies departing from the Dirac point, the isofrequency contours become trigonally warped, leading to directionally anisotropic group velocities. When an incident beam is launched from an armchair edge along the Γ-K direction, three beams are expected: a self-collimated center beam and two side beams at ±π/3. However, due to the symmetry of local resonance modes confined in the metallic cavities, the coupling between the incident beam and the photonic structure can be highly asymmetric. This task quantifies how the transmitted power is distributed among these beam directions across the Dirac cone, exposing an abnormal beam inhibition that depends on whether the excitation is at the lower or upper cone branch.

## Approach
Simulate the system using the finite-difference time-domain (FDTD) method. Model a two-dimensional triangular lattice of infinite perfect-electric-conductor cylinders (radius 0.25a) in a dielectric background of air. Build a rectangular sample of 18×15 periods terminated by an armchair edge parallel to the cylinder rows. A TM-polarized beam of width 4a is injected through a metallic waveguide placed at the armchair edge and directed along Γ-K. For a set of frequencies spanning the Dirac cone (0.85–1.0 in units ωa/2πc), run FDTD simulations until the electromagnetic field reaches a steady state. After steady state is achieved, record the transmitted flux, normalized by the incident flux, in two detection regions: one region lying directly in front of the waveguide exit (center direction) and one region located at an angle of π/3 from the incident axis (side direction). The simulations are executed with an open-source FDTD solver (e.g., MEEP). The output is a table of frequency versus normalized transmission, which reveals where the most efficient beam steering occurs.

## Reproduction target
Produce a CSV file, `transmission_spectra.csv`, with three numeric columns: `frequency` (in normalized units ωa/2πc), `transmission_center` (dimensionless, normalized to the incident flux), and `transmission_side` (dimensionless). The file must contain at least 100 frequency points uniformly covering the interval from 0.85 to 1.0. The spectra should be physically plausible—smooth and exhibiting distinct peaks near the Dirac cone branches—and the transmission values must be obtained from FDTD flux measurements after the fields have converged.

## Assets

- MEEP: https://meep.readthedocs.io

## Workflow steps

### Step 1: FDTD transmission spectra simulation
- Role: scored (load-bearing)
- Action: Set up the triangular lattice of infinite perfect-electric-conductor cylinders (radius r=0.25a, lattice constant a) in an air background. Construct a sample with 18×15 periods having an armchair edge. Inject a TM-polarized beam of width 4a along the Γ-K direction using a metallic waveguide. For many frequencies in the interval [0.85, 1.0] (ωa/2πc), run FDTD simulations to reach steady state. At each frequency, record the transmitted flux, normalized by the incident flux, in two detection regions: one directly in front of the incident beam (center direction) and one at an angle of π/3 from the beam axis (side direction). Store the results as a CSV.
- Output file: `/app/outputs/transmission_spectra.csv`
- Format: csv
- Contract: Header: frequency,transmission_center,transmission_side. All columns numeric. frequency in units of ωa/2πc; transmission values dimensionless. At least 100 rows spanning [0.85, 1.0].
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transmission_spectra.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transmission_spectra.csv
- path: `/app/outputs/transmission_spectra.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Normalized transmission spectra in center and side beam directions as a function of frequency around the Dirac cone.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `transmission_center`, `transmission_side`
  - `units`:
    - `frequency`: omega*a/(2*pi*c)
    - `transmission_center`: dimensionless
    - `transmission_side`: dimensionless

Notes: The checker will recompute inhibition ratios from this CSV at specific hidden frequencies and check that the center-to-side ratio and side-to-center ratio each exceed an order-of-magnitude threshold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transmission_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "transmission_center",
          "transmission_side"
        ],
        "units": {
          "frequency": "omega*a/(2*pi*c)",
          "transmission_center": "dimensionless",
          "transmission_side": "dimensionless"
        }
      },
      "description": "Normalized transmission spectra in center and side beam directions as a function of frequency around the Dirac cone."
    }
  ],
  "notes": "The checker will recompute inhibition ratios from this CSV at specific hidden frequencies and check that the center-to-side ratio and side-to-center ratio each exceed an order-of-magnitude threshold."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `transmission_spectra.csv` and computes two ratios from the data: one ratio at a frequency near the lower Dirac cone peak and another at a frequency near the upper cone peak. The verifier checks that each ratio exceeds an order-of-magnitude threshold, consistent with the beam inhibition reported in the literature, and that the overall spectral shape shows the expected number of transmission maxima. Credit is awarded when both ratios meet the threshold and when the file contains the required number of rows; partial credit may be given if only one ratio is sufficient or if the ratios are weaker but still show a substantial asymmetry. The exact threshold values are not disclosed; you must reproduce the physical effect that one beam direction is overwhelmingly stronger than the other at each cone frequency. No manual or post‑processed values from an outside source are accepted—only the raw CSV.
