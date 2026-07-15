# Porosity-Dependent Elastic Property and Energy Harvesting Performance Simulation

## Problem background
Piezoelectric energy harvesters convert ambient vibrations into electrical power, enabling self-powered low-power electronics. Lead-free BCZT ceramics have high piezoelectric coefficients, but their bulk dense form is limited. Introducing controlled porosity can tune the effective elastic, dielectric, and piezoelectric properties, potentially enhancing energy harvesting output. This task investigates, through numerical simulation, how porosity (0% to 25% by volume) affects the open-circuit voltage and harvested power of a porous BCZT unimorph cantilever harvester operating in both d31 and d33 modes. The goal is to determine whether an optimal porosity exists that maximizes performance compared to the non-porous baseline.

## Approach
The pipeline has two main computational stages. First, finite-element (FE) homogenization is performed on a representative volume element (RVE) — a unit cube containing randomly distributed spherical voids — to compute the effective transversely isotropic elastic stiffness coefficients of porous BCZT at each porosity level. Homogenization uses periodic boundary conditions and six independent pure-strain load cases; volume-averaged stresses and strains yield the coefficients C11, C12, C13, C33, C44, and C66. Second, a unimorph cantilever energy harvester is modeled: a steel beam (300×10×5 mm) with an attached BCZT patch (150×10×5 mm). Harvester simulations use the effective stiffnesses from the first stage, publicly available piezoelectric coefficients and relative permittivity, and densities computed via the rule of mixtures. For each porosity (0,5,10,15,20,25%) and both d31 (top-bottom electrodes) and d33 (interdigitated electrodes, with width and gap optimized for maximum power at 0% porosity), the harvester is excited by a base acceleration of 1g. Open-circuit voltage and power (with optimal load resistance matched to the structure's natural frequency) are computed over a frequency sweep. The maximal voltage and power, and the corresponding frequency, are extracted for every condition.

## Reproduction target
Produce two scored CSV files under /app/outputs: (1) effective_stiffness_coefficients.csv containing the six elastic stiffness coefficients (GPa) for each porosity; (2) harvester_results.csv containing the maximum open-circuit voltage (V), maximum harvested power (W), and the frequency at which the maximum occurs (Hz) for each porosity and mode (d31, d33). The required column schemas are given in the output contract. The results should be computed entirely by re-implementing the described RVE homogenization and harvester FE simulations using any open-source FE package (e.g., FEniCS or SfePy). The public material inputs are the dense BCZT elastic constants (Liu & Ren 2009) and the porous BCZT piezoelectric/dielectric properties (Zhang et al. 2019); all geometry and loading parameters are provided in the workflow steps.

## Assets

- Dense BCZT elastic stiffness constants: 10.1103/PhysRevLett.103.257602
- Porous BCZT piezoelectric and dielectric properties: 10.1016/j.materresbull.2018.12.036
- Cantilever beam and patch geometry and steel material
- Open-source finite element library: FEniCS or SfePy

## Workflow steps

### Step 1: Electrode parameter optimization for d33 mode
- Role: process
- Action: Simulate the harvester at 0% porosity with varying interdigital electrode width and gap to find the combination that maximizes harvested power. The resulting optimal width=22.5 mm and gap=20 mm are used in all subsequent d33 simulations.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 2: Density calculation by mixture rule
- Role: process
- Action: Compute the mass density of porous BCZT at each porosity using the rule of mixtures (ρ = ρ_m·v_m, neglecting air).
- Evidence: none

### Step 3: RVE homogenization of elastic stiffness coefficients
- Role: scored
- Action: Perform finite-element analysis on a unit cube RVE containing spherical voids. Apply periodic boundary conditions and six load cases (pure strain states) to compute volume-averaged stress and strain, then extract effective stiffnesses C11, C12, C13, C33, C44, C66 for porosities 0%,5%,10%,15%,20%,25%.
- Output file: `/app/outputs/effective_stiffness_coefficients.csv`
- Format: csv
- Contract: columns: porosity (%), C11 (GPa), C12 (GPa), C13 (GPa), C33 (GPa), C44 (GPa), C66 (GPa)
- Scoring: scored by hidden verifier

### Step 4: Unimorph cantilever energy harvester simulation
- Role: scored (load-bearing)
- Action: Build a finite-element model of a steel cantilever beam (300×10×5 mm) with an attached BCZT patch (150×10×5 mm). Use the stiffness coefficients from step2, piezoelectric/dielectric data from public resource, and densities from step1. Apply base harmonic acceleration 1g. For each porosity (0-25%) and both d31 (top-bottom) and d33 (optimized IDE) modes, compute open-circuit voltage and harvested power vs frequency with optimal load resistance. Extract maximum voltage, maximum power and the corresponding frequency.
- Output file: `/app/outputs/harvester_results.csv`
- Format: csv
- Contract: columns: porosity (%), mode (string: d31 or d33), max_voltage (V), max_power (W), frequency_at_max (Hz)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_stiffness_coefficients.csv`
- `/app/outputs/harvester_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_stiffness_coefficients.csv
- path: `/app/outputs/effective_stiffness_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed effective transversely isotropic elastic stiffness coefficients of porous BCZT at each porosity. The checker compares each coefficient to hidden paper-reported values and verifies monotonic decrease with porosity.
- schema:
  - `type`: table
  - `required_columns`: `porosity`, `C11`, `C12`, `C13`, `C33`, `C44`, `C66`
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C33`: GPa
    - `C44`: GPa
    - `C66`: GPa

### harvester_results.csv
- path: `/app/outputs/harvester_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Maximum open-circuit voltage and harvested power at each porosity for d31 and d33 modes. The checker computes relative increases from 0% to 10% porosity for voltage and from 0% to 5% porosity for power, and compares them to hidden paper-reported percentages; also checks that voltage peaks at 10% and power at 5%.
- schema:
  - `type`: table
  - `required_columns`: `porosity`, `mode`, `max_voltage`, `max_power`, `frequency_at_max`
  - `units`:
    - `max_voltage`: V
    - `max_power`: W
    - `frequency_at_max`: Hz

Notes: All scored outputs will be validated against hidden reference values derived from the paper. Tolerances absorb legitimate differences due to discretisation and solver choices.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_stiffness_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "porosity",
          "C11",
          "C12",
          "C13",
          "C33",
          "C44",
          "C66"
        ],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C33": "GPa",
          "C44": "GPa",
          "C66": "GPa"
        }
      },
      "description": "Computed effective transversely isotropic elastic stiffness coefficients of porous BCZT at each porosity. The checker compares each coefficient to hidden paper-reported values and verifies monotonic decrease with porosity."
    },
    {
      "file": "harvester_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "porosity",
          "mode",
          "max_voltage",
          "max_power",
          "frequency_at_max"
        ],
        "units": {
          "max_voltage": "V",
          "max_power": "W",
          "frequency_at_max": "Hz"
        }
      },
      "description": "Maximum open-circuit voltage and harvested power at each porosity for d31 and d33 modes. The checker computes relative increases from 0% to 10% porosity for voltage and from 0% to 5% porosity for power, and compares them to hidden paper-reported percentages; also checks that voltage peaks at 10% and power at 5%."
    }
  ],
  "notes": "All scored outputs will be validated against hidden reference values derived from the paper. Tolerances absorb legitimate differences due to discretisation and solver choices."
}
```

## How you are scored
A hidden checker reads the submitted CSV files and independently evaluates them against paper-derived reference values. The stiffness coefficients are checked for monotonic decrease with increasing porosity and for approximate agreement with reference values. The harvester output is checked for structural trends: voltage should peak at an intermediate porosity, while power should peak at a lower porosity. The checker also computes relative changes (e.g., the increase in voltage and power relative to the non-porous case) from the submitted values and compares them to hidden reference percentages using generous tolerances. The final reward (0 to 1) is a weighted combination of the stiffness checks and the harvester checks, with the harvester performance carrying the majority of the weight. Simply copying numbers from the paper without running the actual simulations will not yield a passing score.
