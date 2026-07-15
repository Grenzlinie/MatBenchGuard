# Angular-tolerance enhancement of bi-atomic grating guided-mode resonance filters via RCWA simulation

## Problem background
Guided-mode resonance filters that use metallic gratings on dielectric waveguides can produce narrowband transmission, but they typically suffer from poor angular tolerance — the transmission peak shifts and broadens rapidly as the incidence angle deviates from normal. A bi-atomic grating design, where each unit cell contains two slits of different widths, can open a frequency gap at the Brillouin-zone centre and flatten the dispersion band, which is expected to increase the angular tolerance. This reproduction task evaluates the angular bandwidth enhancement of such bi-atomic structures compared to a simply periodic grating (SPG) using numerical electromagnetic simulations.

## Approach
Use rigorous coupled-wave analysis (RCWA) to simulate the one-dimensional metallic/dielectric gratings under transverse-magnetic (TM) polarization. Model the gold layer with a Drude dielectric function (plasma wavelength 159 nm, damping 0.0077) and the dielectric layer with a constant refractive index n=2. For each structure, first compute the normal-incidence transmission spectrum to locate the resonance wavelength (\(\lambda_R\)). Then sweep the incidence angle from 0° to at least 30° in steps ≤2° at that fixed \(\lambda_R\) and record the transmitted power. Two structures are compared:
- SPG: period 2.48 µm, single slit width 350 nm, metal thickness 100 nm, dielectric thickness 700 nm.
- Bi-atomic grating: period 3 µm, slit widths 200 nm and 700 nm (i.e., two slits per period), same layer thicknesses.
From the angle-resolved transmission curves, the angular tolerance is quantified by the half-width at half-maximum (HWHM) of the transmission peak. The key metric is the ratio of the bi-atomic HWHM to the SPG HWHM.

## Reproduction target
Produce two CSV files containing the angle-resolved transmission data at the resonance wavelength for each structure: `angular_transmission_SPG.csv` and `angular_transmission_bi-atomic.csv`. The verifier will derive the HWHM of each transmission peak from these curves and compute the ratio (bi-atomic HWHM divided by SPG HWHM) to quantify the angular tolerance enhancement.

## Assets

- Rigorous Coupled-Wave Analysis (RCWA) solver: https://github.com/victorliu/S4
- Python scientific stack: numpy scipy matplotlib

## Workflow steps

### Step 1: Simulate SPG angle-resolved transmission
- Role: scored (load-bearing)
- Action: Using the RCWA solver, simulate the simply periodic grating (SPG) structure: period d=2.48 µm, slit width a=350 nm, metal thickness 100 nm, dielectric thickness 700 nm. Use a Drude model for gold with plasma wavelength 159 nm and damping 0.0077, and SiNx index n=2. Compute the normal-incidence transmission spectrum; determine the resonance wavelength λ_R from this spectrum. Then sweep the incidence angle θ from 0° to at least 30° in steps ≤2° at the fixed λ_R, recording the transmitted power. Normalise transmission to the maximum at 0° if needed. Output the angle (degrees) and transmission (fraction in [0,1]) as a CSV file.
- Output file: `/app/outputs/angular_transmission_SPG.csv`
- Format: csv
- Contract: Columns: angle_deg, transmission. Header must be 'angle_deg,transmission'. At least 15 rows covering 0–30°. Transmission at 0° should be near 1.
- Scoring: scored by hidden verifier

### Step 2: Simulate bi-atomic angle-resolved transmission
- Role: scored (load-bearing)
- Action: Repeat the simulation for the bi-atomic grating structure: period d=3 µm, slit widths a=200 nm and a+l=700 nm (i.e., additional slit width l=500 nm), metal thickness 100 nm, dielectric thickness 700 nm, same materials as before. Determine the resonance wavelength λ_R from the normal-incidence transmission spectrum, then compute transmission vs. incidence angle θ (0–30°, ≤2° steps) at that λ_R. Normalise to the maximum at 0° if needed. Output the angle-resolved transmission as a CSV file.
- Output file: `/app/outputs/angular_transmission_bi-atomic.csv`
- Format: csv
- Contract: Columns: angle_deg, transmission. Same format as angular_transmission_SPG.csv.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/angular_transmission_SPG.csv`
- `/app/outputs/angular_transmission_bi-atomic.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### angular_transmission_SPG.csv
- path: `/app/outputs/angular_transmission_SPG.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Angle-resolved transmission curve for the SPG structure. The checker will recompute the half-width at half-maximum (HWHM) of the transmission peak from this data and compare it to the hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `transmission`
  - `units`:
    - `angle_deg`: degree
    - `transmission`: fraction (0-1)

### angular_transmission_bi-atomic.csv
- path: `/app/outputs/angular_transmission_bi-atomic.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Angle-resolved transmission curve for the bi-atomic structure. The checker will recompute its HWHM and compute the ratio to the SPG HWHM, verifying the claimed angular tolerance enhancement.
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `transmission`
  - `units`:
    - `angle_deg`: degree
    - `transmission`: fraction (0-1)

Notes: The checker will recompute the half-width at half-maximum (HWHM) from the submitted data and assess whether the bi-atomic HWHM is at least 1.5 times the SPG HWHM. Both CSVs must contain at least 15 rows covering 0–30°. The resonance wavelength λ_R is determined by the agent as part of the simulation; the exact value is not prescribed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "angular_transmission_SPG.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "transmission"
        ],
        "units": {
          "angle_deg": "degree",
          "transmission": "fraction (0-1)"
        }
      },
      "description": "Angle-resolved transmission curve for the SPG structure. The checker will recompute the half-width at half-maximum (HWHM) of the transmission peak from this data and compare it to the hidden reference."
    },
    {
      "file": "angular_transmission_bi-atomic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "transmission"
        ],
        "units": {
          "angle_deg": "degree",
          "transmission": "fraction (0-1)"
        }
      },
      "description": "Angle-resolved transmission curve for the bi-atomic structure. The checker will recompute its HWHM and compute the ratio to the SPG HWHM, verifying the claimed angular tolerance enhancement."
    }
  ],
  "notes": "The checker will recompute the half-width at half-maximum (HWHM) from the submitted data and assess whether the bi-atomic HWHM is at least 1.5 times the SPG HWHM. Both CSVs must contain at least 15 rows covering 0–30°. The resonance wavelength λ_R is determined by the agent as part of the simulation; the exact value is not prescribed."
}
```

## How you are scored
A hidden verifier reads your submitted CSV files independently. For each file, it interpolates the angle–transmission data and extracts the half-width at half-maximum (HWHM). It then computes the ratio of the bi-atomic HWHM to the SPG HWHM. Your reward is based on whether the computed HWHM values and the ratio meet the expected physical behavior within reasonable numerical tolerances. The scoring does not require exact numbers; it rewards results that are consistent with the anticipated angular tolerance enhancement. Both artifacts contribute to the final score.
