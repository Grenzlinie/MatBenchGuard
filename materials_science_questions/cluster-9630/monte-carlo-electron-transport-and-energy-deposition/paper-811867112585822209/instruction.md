# Specific cellular dose and lineal energy calculation for low-energy electrons

## Problem background
In cellular dosimetry for internally deposited radionuclides, the specific cellular dose — the mean absorbed dose to a subcellular target per emission from a subcellular source — and the lineal energy — the single-event energy deposition per mean chord length — are critical quantities, especially for low-energy electrons where source distributions are often non-uniform and transport effects such as elastic scattering and energy-loss straggling become significant. This task addresses the computation of these quantities for a spherical cell model with several distinct source-target configurations: nucleus (N), cytoplasm (Cy), whole cell (C), and cell surface (CS).

## Approach
Two computational approaches are employed.

**Mixed method**: First, the electron continuous-slowing-down approximation (CSDA) range in liquid water is derived from the dielectric response theory, using published optical constants and extended Drude model parameters for liquid water. With that range-energy relation, specific cellular doses for the given source-target geometries are computed by randomly sampling electron pathlengths through the target region and applying the range-energy relation to determine energy deposition.

**Probabilistic method**: The open-source Penelope Monte Carlo code is used to simulate electron transport in liquid water. Simulations are performed both without and with elastic interactions to isolate the effect of elastic scattering. Single-event energy deposition data from the elastic-interaction simulation are further processed to extract frequency-mean and most probable lineal energies.

## Reproduction target
Your task is to produce the following three output files under `/app/outputs` for a spherical cell of radius 5 µm and nucleus radius 2 µm, with all calculations in liquid water:

1. `mixed_doses.csv` — specific cellular doses (Gy/emission) computed by the mixed method for geometry N←N, N←Cy, C←C, C←CS at electron energies 0.1, 0.5, 1, 5, 10 keV.
2. `penelope_doses.csv` — specific cellular doses (Gy/emission) from Penelope Monte Carlo simulations, including standard deviations, for the same four geometries at electron energies 0.5, 1, 5, 10 keV. Two simulation modes are required: without elastic interactions and with elastic interactions.
3. `lineal_energies.csv` — frequency-mean (ȳ_F) and most probable (y_mp) lineal energies (keV/µm) for geometry N←N, N←Cy, C←C, C←CS, N←CS at electron energies 0.5, 1, 5, 10, 50, 100 keV, obtained from the Penelope simulation that includes elastic interactions.

## Assets

- Penelope Monte Carlo code: https://www.oecd-nea.org/tools/abstract/detail/nea-1525
- Optical constants of liquid water
- Extended Drude model parameters for liquid water: 10.1016/j.nimb.2007.05.008

## Workflow steps

### Step 1: Compute electron CSDA range-energy relation
- Role: process
- Action: Implement the dielectric response theory using the extended Drude model parameters from the literature (DOI:10.1016/j.nimb.2007.05.008) and the optical data of liquid water from Palik's handbook. Compute the differential inverse mean free path (DIMFP) and the continuous-slowing-down approximation (CSDA) range of electrons in liquid water. Produce a table of range versus energy as intermediate evidence.
- Evidence: `/app/outputs/range_energy.csv`

### Step 2: Specific cellular doses via the mixed method
- Role: scored (load-bearing)
- Action: Using the range-energy relation from Step 1 and random sampling of electron pathlengths, compute specific cellular doses D(R_T←R_S) for the four geometries (N←N, N←Cy, C←C, C←CS) in a cell with cell radius 5 μm and nuclear radius 2 μm at electron energies 0.1, 0.5, 1, 5, 10 keV. Output a CSV file with the results.
- Output file: `/app/outputs/mixed_doses.csv`
- Format: csv
- Contract: columns: geometry (string), energy_keV (float), D_mixed (float)
- Scoring: scored by hidden verifier

### Step 3: Penelope Monte Carlo simulation for cellular doses
- Role: scored (load-bearing)
- Action: Run the Penelope code for electron transport in liquid water for the spherical cell (Rc=5 μm, Rn=2 μm) with source-target geometries N←N, N←Cy, C←C, C←CS. Perform two simulation modes: without elastic interactions and with elastic interactions. Use 10^7 electron histories per configuration for energies 0.5, 1, 5, 10 keV. Output the mean specific cellular doses and their standard deviations.
- Output file: `/app/outputs/penelope_doses.csv`
- Format: csv
- Contract: columns: geometry (string), energy_keV (float), D_without_elastic (float), std_without (float), D_with_elastic (float), std_with (float)
- Scoring: scored by hidden verifier

### Step 4: Lineal energy analysis from Penelope simulation
- Role: scored
- Action: From the Penelope simulation with elastic interactions (Step 3), extract single-event energy deposition data. Compute the frequency-mean (ȳ_F) and most probable (y_mp) lineal energies for geometries N←N, N←Cy, C←C, C←CS, N←CS at electron energies 0.5, 1, 5, 10, 50, 100 keV. Output a CSV file.
- Output file: `/app/outputs/lineal_energies.csv`
- Format: csv
- Contract: columns: geometry (string), energy_keV (float), yF (float, keV/µm), ymp (float, keV/µm)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mixed_doses.csv`
- `/app/outputs/penelope_doses.csv`
- `/app/outputs/lineal_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mixed_doses.csv
- path: `/app/outputs/mixed_doses.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Specific cellular doses computed by the mixed method for four source-target geometries at five electron energies.
- schema:
  - `type`: table
  - `required_columns`: `geometry`, `energy_keV`, `D_mixed`
  - `units`:
    - `energy_keV`: keV
    - `D_mixed`: Gy/emission

### penelope_doses.csv
- path: `/app/outputs/penelope_doses.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Specific cellular doses from Penelope simulations without and with elastic interactions, along with their standard deviations.
- schema:
  - `type`: table
  - `required_columns`: `geometry`, `energy_keV`, `D_without_elastic`, `std_without`, `D_with_elastic`, `std_with`
  - `units`:
    - `energy_keV`: keV
    - `D_without_elastic`: Gy/emission
    - `std_without`: Gy/emission
    - `D_with_elastic`: Gy/emission
    - `std_with`: Gy/emission

### lineal_energies.csv
- path: `/app/outputs/lineal_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Frequency-mean (yF) and most probable (ymp) lineal energies for five source-target geometries at six electron energies.
- schema:
  - `type`: table
  - `required_columns`: `geometry`, `energy_keV`, `yF`, `ymp`
  - `units`:
    - `energy_keV`: keV
    - `yF`: keV/µm
    - `ymp`: keV/µm

Notes: The mixed method doses extend to 0.1 keV, while Penelope doses cover 0.5-10 keV. Lineal energies are obtained from the Penelope simulation with elastic interactions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mixed_doses.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "geometry",
          "energy_keV",
          "D_mixed"
        ],
        "units": {
          "energy_keV": "keV",
          "D_mixed": "Gy/emission"
        }
      },
      "description": "Specific cellular doses computed by the mixed method for four source-target geometries at five electron energies."
    },
    {
      "file": "penelope_doses.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "geometry",
          "energy_keV",
          "D_without_elastic",
          "std_without",
          "D_with_elastic",
          "std_with"
        ],
        "units": {
          "energy_keV": "keV",
          "D_without_elastic": "Gy/emission",
          "std_without": "Gy/emission",
          "D_with_elastic": "Gy/emission",
          "std_with": "Gy/emission"
        }
      },
      "description": "Specific cellular doses from Penelope simulations without and with elastic interactions, along with their standard deviations."
    },
    {
      "file": "lineal_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "geometry",
          "energy_keV",
          "yF",
          "ymp"
        ],
        "units": {
          "energy_keV": "keV",
          "yF": "keV/µm",
          "ymp": "keV/µm"
        }
      },
      "description": "Frequency-mean (yF) and most probable (ymp) lineal energies for five source-target geometries at six electron energies."
    }
  ],
  "notes": "The mixed method doses extend to 0.1 keV, while Penelope doses cover 0.5-10 keV. Lineal energies are obtained from the Penelope simulation with elastic interactions."
}
```

## How you are scored
A hidden verifier inspects your output files. For each scored artifact, it compares your computed values to hidden reference values using tolerances appropriate for the stochastic and systematic uncertainties of the methods. It also performs structural consistency checks, e.g., verifying that the inclusion of elastic interactions changes the dose in a physically expected direction for certain configurations. The verifier computes a score for each artifact and combines them by weight into a single final reward. Reporting the paper's numbers without actually executing the workflow will not satisfy these checks.
