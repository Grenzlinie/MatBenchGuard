# FDTD Simulation of Diamond Mirror Reflectivity Spectrum

## Problem background
High-power lasers are widely used in manufacturing, medicine, and defense, but they demand optical mirrors that can withstand extreme optical intensities without damage. Conventional dielectric mirrors rely on multilayer thin-film coatings; at high powers, imperfections and absorption in these layers generate heat, causing thermal stress and permanent failure. Single-crystal diamond is an attractive alternative because of its high refractive index, wide electronic bandgap, and exceptional thermal conductivity. This work proposes a monolithic mirror consisting of a periodic array of "golf-tee"-shaped nanostructures etched directly into a diamond substrate. By engineering the geometry of the columns, the structure supports guided-mode resonances that produce high reflectivity near a chosen operating wavelength. The computational part of the study uses finite-difference time-domain (FDTD) simulations to design the column dimensions and predict the mirror's reflection spectrum. In this task you will reproduce the FDTD simulation and compute the reflectivity spectrum for one of the reported designs, enabling the performance of the mirror to be verified numerically.

## Approach
You will set up and run a three-dimensional FDTD simulation of the golf-tee column array. The simulation models a single unit cell of the hexagonal lattice with Bloch-periodic lateral boundaries and uses a broadband plane-wave source at normal incidence to excite the structure. The reflected flux is recorded as a function of wavelength, and the reflectivity is obtained by normalizing to the incident flux. The diamond material is treated as lossless and non-dispersive with a constant refractive index n = 2.4. The specific geometric parameters (column radii, pitch, height, undercut angle) and the wavelength sweep range are provided in the scored workflow step below. You may implement the simulation with any open‑source FDTD solver; Meep is a capable and readily available option. After obtaining the reflectivity spectrum, you will export it as a CSV file. The computational work is moderately heavy (sub‑micron features in three dimensions spanning a 200 nm wavelength range), so plan for several hours of runtime on a modern multi‑core machine.

## Reproduction target
Simulate the normal‑incidence reflectivity spectrum for the diamond mirror design with the following geometry: hexagonal array of golf‑tee columns with disc radius 250 nm, minimum radius 50 nm, support radius 250 nm, center‑to‑center pitch 1.1 µm, total height 3 µm, and undercut angle 70°. Assume a uniform diamond refractive index of 2.4. Perform the simulation over the wavelength range 1000–1200 nm. Save the resulting spectrum as a CSV file named `step_01_simulated_reflectivity.csv` under `/app/outputs`. The file must contain two columns: `wavelength_nm` (float, in nanometres) and `reflectivity` (float, a dimensionless number between 0 and 1). The hidden verifier will read this spectrum, identify the resonance peak, and extract the peak reflectivity, the corresponding peak wavelength, and the full‑width at half‑maximum (FWHM) of the reflectivity band. The task is considered fully successful if all three extracted metrics meet the design specifications that were reported for this geometry.

## Assets

- Meep FDTD solver: https://meep.readthedocs.io/en/latest/

## Workflow steps

### Step 1: FDTD simulation of diamond mirror reflectivity
- Role: scored (load-bearing)
- Action: Run an FDTD simulation for a hexagonal array of golf-tee columns with the specified geometry (r_disc=250 nm, r_min=50 nm, r_support=250 nm, pitch=1.1 μm, total height h=3 μm, undercut angle α=70°) in a diamond medium (refractive index n=2.4, non-dispersive). Sweep wavelengths from 1000 to 1200 nm at normal incidence. Extract the normal-incidence reflectivity spectrum and save the result as a CSV.
- Output file: `/app/outputs/step_01_simulated_reflectivity.csv`
- Format: csv
- Contract: Columns: wavelength_nm (float), reflectivity (float, between 0 and 1). One row per sampled wavelength.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_simulated_reflectivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_simulated_reflectivity.csv
- path: `/app/outputs/step_01_simulated_reflectivity.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed normal-incidence reflectivity spectrum for the golf-tee diamond mirror design. The checker recomputes peak reflectivity, peak wavelength, and full-width at half-maximum from this spectrum and compares them to hidden paper-reported thresholds.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `reflectivity`
  - `units`:
    - `wavelength_nm`: nm
    - `reflectivity`: dimensionless (0-1)

Notes: The agent must ensure the CSV covers the 1000–1200 nm range with sufficient wavelength sampling to resolve the resonance. The checker will derive scalar metrics from the spectrum, not trust any self-reported summary.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_simulated_reflectivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "reflectivity"
        ],
        "units": {
          "wavelength_nm": "nm",
          "reflectivity": "dimensionless (0-1)"
        }
      },
      "description": "Computed normal-incidence reflectivity spectrum for the golf-tee diamond mirror design. The checker recomputes peak reflectivity, peak wavelength, and full-width at half-maximum from this spectrum and compares them to hidden paper-reported thresholds."
    }
  ],
  "notes": "The agent must ensure the CSV covers the 1000–1200 nm range with sufficient wavelength sampling to resolve the resonance. The checker will derive scalar metrics from the spectrum, not trust any self-reported summary."
}
```

## How you are scored
An automated checker will read your `step_01_simulated_reflectivity.csv`. It first validates that the file contains at least two columns named `wavelength_nm` and `reflectivity` and that all reflectivity values lie in the range [0, 1]. It then computes three quantities from the spectrum: (1) the maximum reflectivity value anywhere in the trace, (2) the wavelength at which that maximum occurs, and (3) the full‑width at half‑maximum (FWHM) of the reflectivity peak, defined as the wavelength span where the reflectivity is at least half of the peak value. Each of these three numbers is compared against pre‑established performance thresholds (the paper’s published design targets). A partial reward is assigned for each metric that meets or exceeds its threshold; the three rewards are then averaged into a single overall score between 0 and 1. The thresholds are chosen to require a physically correct simulation – merely reporting plausible numbers without running a genuine FDTD calculation will not produce a spectrum that passes these checks. You must therefore implement and execute the simulation faithfully.
