# Reflection Spectra Simulation of Digital Concatenated Gratings

## Problem background
Widely tunable semiconductor lasers for optical networks require comb reflectors with a flat top‑hat reflection envelope to maintain uniform feedback across all wavelength channels. Existing approaches, such as superstructure gratings or phase‑modulated gratings, demand extremely fine control of the grating pitch and phase, making fabrication difficult. An alternative design, the digital concatenated grating (DCG), consists of several sampled subgratings with different Bragg periods but identical sampling parameters. When concatenated, the subgrating reflection envelopes are predicted to merge into a nearly flat comb response, ideally suited for tunable lasers. This task implements such a DCG reflector and simulates its reflection spectrum to determine whether the envelope is flat and the comb peaks are uniform.

## Approach
A DCG is built from M concatenated sampled grating sections (subgratings). Each subgrating has its own Bragg period, while the sampling period, duty cycle, and segment length are shared by all subgratings. The Bragg period Λ(i) of the i‑th subgrating (i=1,2,3) is given by:
Λ(i) = λc/(2 neff) + (H / Z0) * (λc/(2 neff))^2,   where
H = m * (i - (M+1)/2),
with central wavelength λc=1550 nm, effective index neff=3.2, number of subgratings M=3, integer m=2, and sampling period Z0 (front=38.304 μm, rear=46.512 μm). This rule guarantees that the concatenated reflection envelope becomes flat. Two DCG reflectors are designed: a front reflector and a rear reflector, differing only in their sampling periods and the resulting Bragg period sets. After computing the grating parameters, the full reflector structures are simulated using the transfer‑matrix method (TMM) to obtain the wavelength‑dependent reflectivity over the 1500–1600 nm range.

## Reproduction target
Implement the DCG design rule to compute the Bragg periods, grating segment lengths, and number of Bragg periods for each subgrating of the front and rear reflectors using the parameters provided in the workflow steps. Construct the full front and rear grating structures by concatenating the three subgratings. Simulate the reflection spectra via the transfer‑matrix method from 1500 nm to 1600 nm in steps no larger than 0.1 nm. Output the wavelength (nm) and the front and rear reflectivities in a CSV file. The spectrum should exhibit a comb of reflection peaks whose envelopes are flat and whose peak reflectivities are nearly uniform.

## Assets

- Python scientific libraries: numpy scipy matplotlib

## Workflow steps

### Step 1: DCG design parameter calculation
- Role: process
- Action: Using the design rule for digital concatenated gratings (Bragg period formula with auxiliary parameter H) and the provided front/rear parameters (central wavelength 1550 nm, effective refractive index 3.2, front sampling period 38.304 μm, rear sampling period 46.512 μm, number of subgratings M=3, integer m=2), compute the Bragg periods, grating segment lengths, and Bragg period counts for each subgrating of the front and rear DCG reflectors. Store the results in a JSON file.
- Evidence: `/app/outputs/design_parameters.json`

### Step 2: Reflection spectrum simulation
- Role: scored (load-bearing)
- Action: Construct the full front and rear DCG structures by concatenating the three subgratings. Simulate the reflection spectra using the transfer-matrix method over the wavelength range 1500–1600 nm in steps ≤0.1 nm. Output a CSV with columns wavelength_nm, front_reflectivity, rear_reflectivity.
- Output file: `/app/outputs/reflection_spectra.csv`
- Format: csv
- Contract: columns: wavelength_nm (float), front_reflectivity (float), rear_reflectivity (float); rows: evenly spaced wavelength points.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reflection_spectra.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reflection_spectra.csv
- path: `/app/outputs/reflection_spectra.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Simulated reflection spectra. The checker verifies that the comb peaks have uniform amplitude and the envelope is flat, with peak wavelengths matching the design targets within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `front_reflectivity`, `rear_reflectivity`
  - `units`:
    - `wavelength_nm`: nm
    - `front_reflectivity`: dimensionless
    - `rear_reflectivity`: dimensionless

Notes: The checker uses structural analysis (peak finding, uniformity, envelope flatness) with generous tolerances to accommodate numerical differences in the transfer-matrix implementation. No specific gold wavelengths or reflectivities are exposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reflection_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "front_reflectivity",
          "rear_reflectivity"
        ],
        "units": {
          "wavelength_nm": "nm",
          "front_reflectivity": "dimensionless",
          "rear_reflectivity": "dimensionless"
        }
      },
      "description": "Simulated reflection spectra. The checker verifies that the comb peaks have uniform amplitude and the envelope is flat, with peak wavelengths matching the design targets within tolerance."
    }
  ],
  "notes": "The checker uses structural analysis (peak finding, uniformity, envelope flatness) with generous tolerances to accommodate numerical differences in the transfer-matrix implementation. No specific gold wavelengths or reflectivities are exposed."
}
```

## How you are scored
A hidden verifier reads your `reflection_spectra.csv`, extracts the comb peaks (local maxima), and checks three properties: (1) the standard deviation of the peak reflectivities (a measure of uniformity), (2) the flatness of the envelope (the deviation of the mean reflectivity between peaks from the overall mean), and (3) the peak wavelength positions relative to the design targets. The verifier uses tolerance thresholds that absorb typical numeric differences from independent transfer‑matrix implementations. Full credit requires all metrics to meet their respective targets; partial credit may be awarded if only some do. You do not need to guess the thresholds – just produce a faithful simulation from the given design rule and parameters.
