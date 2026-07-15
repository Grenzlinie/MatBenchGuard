# Computational NEMD thermal conductivity of twisted double-walled nanotubes

## Problem background
Double-walled carbon nanotubes (DWCNTs) are promising for nanoelectronic thermal management, but the effect of the interlayer twist angle on their heat-conduction ability is not well understood. This reproduction task aims to quantify how the chirality of the inner tube—characterized by the interlayer twist angle (ITCA)—influences thermal transport in such nanotubes, while also probing the separate roles of tube length and temperature. You will compute the thermal conductivity of several DWCNT configurations using non-equilibrium molecular dynamics and determine the underlying dependencies.

## Approach
The thermal conductivity is studied using non-equilibrium molecular dynamics (NEMD). Double-walled carbon nanotubes are built with a fixed outer tube chirality (15,15) and inner tubes of chiralities (17,0), (16,2), (14,5), (12,8), and (10,10), yielding five different interlayer twist angles. Intralayer C–C bonds are described with an optimized Tersoff potential; the interlayer van der Waals interactions between inner and outer carbon layers are modeled with a Lennard-Jones potential (ε = 0.002844 eV, σ = 3.4 Å). For each tube, a heat source and a heat sink are applied to create a temperature gradient. After equilibration, the steady-state temperature profile along the tube is recorded and the heat flux is measured from the energy added/removed. The temperature gradient is extracted from the linear region of the profile, and the cross-sectional area of the double-walled tube is computed assuming each wall has a thickness of 3.4 Å (A = π × wall thickness × (inner diameter + outer diameter)). Thermal conductivity follows from Fourier’s law. The procedure is repeated for different tube lengths, temperatures, and twist angles to map out the conductivity behavior.

## Reproduction target
You must produce a CSV file, `/app/outputs/thermal_conductivity_results.csv`, containing the computed thermal conductivity for the following series:

- **DWCNT length series:** system `DWCNT`, ITCA = 0°, tube lengths 5 nm, 10 nm, and 20 nm, all at 200 K.
- **DWCNT temperature series:** system `DWCNT`, ITCA = 0°, tube length 10 nm, at temperatures 200 K, 300 K, and 400 K.
- **DWCNT twist-angle series:** system `DWCNT`, all five ITCAs (0.00°, 5.82°, 14.70°, 23.41°, 30.00°) at tube length 10 nm, temperature 200 K. This yields 5 rows.

For each condition, report the mean thermal conductivity and its uncertainty (standard deviation from at least five independent simulation replicates). The file must follow the required schema: columns `system`, `length_nm`, `temperature_K`, `ITCA_deg`, `thermal_conductivity_W_mK`, `uncertainty_W_mK`. The `system` column is `DWCNT` for all rows. The exact set of rows that must appear is specified in the workflow steps; do not omit any required condition.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/
- Optimized Tersoff potential for C–C (opt-Tersoff): LAMMPS pair_style tersoff with Lindsay parameter set
- Lennard-Jones parameters for interlayer C–C interactions

## Workflow steps

### Step 1: Generate atomic configurations for DWCNT
- Role: process
- Action: Create LAMMPS input data files for double-walled carbon nanotubes (DWCNT) with outer tube chirality (15,15) and inner tubes (17,0), (16,2), (14,5), (12,8), (10,10) corresponding to ITCAs 0.00°, 5.82°, 14.70°, 23.41°, 30.00°. For the length series, generate configurations with ITCA = 0.00° at lengths 5 nm, 10 nm, and 20 nm. For the temperature series, generate ITCA = 0.00° at length 10 nm. For the twist-angle series, generate all five ITCAs at length 10 nm. The interlayer distance must be in the range 3.4–3.57 Å. Use optimized Tersoff potential for intralayer C–C bonds, and a Lennard-Jones potential (ε_CC=0.002844 eV, σ_CC=3.4 Å) for interlayer C–C interactions only.
- Evidence: `/app/outputs/structure_generation_log.txt`

### Step 2: Run NEMD simulations for DWCNT
- Role: process
- Action: For each DWCNT configuration from step01 and for each target temperature (200 K for the length and twist-angle series; 200 K, 300 K, and 400 K for the temperature series), perform a NEMD simulation in LAMMPS. Each simulation consists of: energy minimization, 1 ns NVE relaxation, 1 ns Langevin thermostatting of heat source (set temperature + 100 K) and sink (set temperature − 100 K) to establish a gradient, and a 5 ns NVE production run. Use a timestep of 0.001 ps, shrink-wrapped (non-periodic) boundary conditions. Record the segmented temperature profile along the nanotube and the time series of energy added/removed at the source and sink. Run at least 5 independent replicates per condition to estimate uncertainty.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 3: Compute thermal conductivity and compile results
- Role: scored (load-bearing)
- Action: For each simulation output, extract the steady-state linear region of the temperature profile; compute the temperature gradient dT/dx by linear fitting. Calculate the heat flux q from the rate of energy added/subtracted at the source/sink. Calculate the cross-sectional area A using A = π * b * (d_inner + d_outer) with single-wall thickness b = 3.4 Å. Obtain thermal conductivity k from Fourier's law q = -k A dT/dx. Aggregate results over replicates (mean and standard deviation). Output a CSV file.
- Output file: `/app/outputs/thermal_conductivity_results.csv`
- Format: csv
- Contract: Required columns: system (string, must be 'DWCNT'), length_nm (float), temperature_K (float), ITCA_deg (float), thermal_conductivity_W_mK (float), uncertainty_W_mK (float; standard deviation of replicates, may be NaN if only one run). The CSV must include rows for: (a) DWCNT, ITCA=0°, lengths 5, 10, 20 nm at 200 K; (b) DWCNT, ITCA=0°, length 10 nm at 200, 300, 400 K; (c) DWCNT twist-angle series: all five ITCAs (0.00, 5.82, 14.70, 23.41, 30.00) at length 10 nm, 200 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity_results.csv
- path: `/app/outputs/thermal_conductivity_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Tabulated thermal conductivity of double-walled carbon nanotubes (DWCNT) under varying length, temperature, and interlayer twist angle. The hidden checker compares each row's thermal_conductivity_W_mK value against paper-reported gold values within a hidden tolerance, and also verifies required monotonic trends for DWCNT (k increases with ITCA, increases with length, decreases with temperature).
- schema:
  - `type`: table
  - `required_columns`: `system`, `length_nm`, `temperature_K`, `ITCA_deg`, `thermal_conductivity_W_mK`, `uncertainty_W_mK`

Notes: The scored CSV contains only DWCNT rows: length series, temperature series, and twist-angle series. The hidden verifier checks all DWCNT conditions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "length_nm",
          "temperature_K",
          "ITCA_deg",
          "thermal_conductivity_W_mK",
          "uncertainty_W_mK"
        ]
      },
      "description": "Tabulated thermal conductivity of double-walled carbon nanotubes (DWCNT) under varying length, temperature, and interlayer twist angle. The hidden checker compares each row's thermal_conductivity_W_mK value against paper-reported gold values within a hidden tolerance, and also verifies required monotonic trends for DWCNT (k increases with ITCA, increases with length, decreases with temperature)."
    }
  ],
  "notes": "The scored CSV contains only DWCNT rows: length series, temperature series, and twist-angle series. The hidden verifier checks all DWCNT conditions."
}
```

## How you are scored
An automated verifier will examine your CSV file and compare the reported thermal conductivity values against hidden reference data for DWCNT. The scoring is based on two aspects:

- The accuracy of the absolute conductivity values under each condition.
- Whether the data exhibit physically consistent trends with respect to the twist angle, tube length, and temperature.

The twist-angle series carries the greatest weight in the overall score, followed by the length and temperature series. The verifier does not require exact numerical matches; instead, it checks that your computed values fall within a generous tolerance that accounts for stochastic variation and implementation differences. Submitting only the expected trends without genuine simulation output will not satisfy the scoring criteria.
