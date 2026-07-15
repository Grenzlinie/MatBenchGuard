# Thermal Conductivity of Ni-Coated 3WCNTs with Vacancies

## Problem background
Carbon nanotubes (CNTs) are promising thermal interface materials because of their high axial thermal conductivity, but growth-induced vacancies can severely degrade heat conduction. Applying a metal coating to CNTs has been proposed as a potential way to modify thermal transport in defective CNTs. This task uses molecular dynamics simulations to compute the axial thermal conductivity of a tri-walled CNT (3WCNT) in pristine, vacancy-defective, and nickel-coated configurations, and to evaluate the effect of the coating.

## Approach
The system is a 57 nm tri-walled armchair CNT composed of coaxial (10,10), (15,15), and (20,20) tubes. Pristine and defective models (0.5% and 1% random carbon vacancies restricted to the middle 20–80% of the length) are constructed, and a conformal 3 nm (18 atomic layers) nickel coating is added to the defective models. Non-equilibrium molecular dynamics (NEMD) is performed with the Two-Temperature Model (TTM) to include electronic heat conduction in the metal. Carbon–carbon interactions use the AIREBO potential, nickel–nickel uses an EAM potential, and nickel–carbon uses a Morse potential. Langevin heat baths at 350 K (hot) and 250 K (cold) are applied at the ends, and the system is equilibrated at 300 K before collecting temperature profiles and heat flux data during NVE production. Axial thermal conductivity is then computed from Fourier's law using the temperature gradient (fitted between grids 20–80) and the heat flux, with the cross-sectional area derived from the van der Waals radii of the outermost and innermost atoms.

## Reproduction target
Build the five atomistic models (pristine, 0.5% vacancies, 1% vacancies, coated 0.5% 3 nm, coated 1% 3 nm), run the NEMD+TTM simulations, and compute the axial thermal conductivity for each configuration. Output the results in a CSV file `thermal_conductivities.csv` with columns `condition` (one of: pristine, vacancy_0.5, vacancy_1.0, coated_0.5_3nm, coated_1.0_3nm) and `thermal_conductivity` (W/mK). The scoring will compare your reported values to a hidden reference and check a required relationship between the coated and uncoated cases for each vacancy concentration.

## Assets

- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://lammps.sandia.gov
- AIREBO potential for carbon-carbon interactions: included in LAMMPS distribution (potentials folder)
- Embedded Atom Method (EAM) potential for nickel (Mishin et al. 1999): https://www.ctcms.nist.gov/potentials/Ni.html
- Morse potential parameters for nickel-carbon interactions (Tang et al. 2013): 10.1039/c3cp51041k

## Workflow steps

### Step 1: Build atomistic models of pristine and defective 3WCNTs
- Role: process
- Action: Generate atomic coordinates for a tri-walled CNT consisting of three coaxial armchair tubes (10,10), (15,15), (20,20) with a length of 57 nm. Then create defective models by randomly removing carbon atoms in the middle 20–80% of the tube length to achieve vacancy concentrations of 0.5% and 1% (relative to the total carbon atoms in that region). Ensure the heat bath regions are free of vacancies.
- Evidence: `/app/outputs/model_coordinates.xyz`

### Step 2: Add nickel coating to defective models
- Role: process
- Action: For each defective 3WCNT model (0.5% and 1% vacancies), deposit a conformal coating of nickel atoms on the outer surface, targeting a thickness of approximately 3 nm (18 atomic layers). The coating should be defect-free.
- Evidence: `/app/outputs/coated_models.xyz`

### Step 3: Run NEMD simulations with TTM
- Role: process
- Action: For each prepared model (pristine, 0.5% and 1% vacancies, coated 0.5% and coated 1%), perform a non-equilibrium molecular dynamics simulation in LAMMPS using the specified potentials: AIREBO for C-C, EAM for Ni-Ni, Morse for Ni-C. Apply Langevin heat baths at 350 K and 250 K on the ends, and enable the two-temperature model (TTM) for the coated models to capture electron heat transfer. Use a 0.5 fs timestep, equilibrate at 300 K for 175 ps in NVT, then collect temperature profiles and heat flux data over 1.25 ns in NVE with the heat baths active.
- Evidence: none

### Step 4: Compute axial thermal conductivity and output results
- Role: scored (load-bearing)
- Action: From the simulation outputs, calculate the axial thermal conductivity for each configuration using Fourier's law: k = -J / (A * dT/dx). The temperature gradient is obtained by linearly fitting the temperature profiles between grids 20 and 80, averaged over the last 250 ps; the heat flux J is averaged over the same interval. Use the cross-sectional area based on the average van der Waals radii of the outermost and innermost atoms. Compile the results into a single CSV file.
- Output file: `/app/outputs/thermal_conductivities.csv`
- Format: csv
- Contract: CSV with columns: condition (string, one of: pristine, vacancy_0.5, vacancy_1.0, coated_0.5_3nm, coated_1.0_3nm) and thermal_conductivity (float, W/mK). Rows correspond to each configuration.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivities.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivities.csv
- path: `/app/outputs/thermal_conductivities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Compiled axial thermal conductivity values for each configuration. The checker will verify that (1) each value matches paper-reported gold values within tolerance, and (2) for each vacancy concentration, the coated conductivity exceeds the defective uncoated conductivity.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `thermal_conductivity`
  - `columns`:
    - `condition`: string, one of: pristine, vacancy_0.5, vacancy_1.0, coated_0.5_3nm, coated_1.0_3nm
    - `thermal_conductivity`: float (W/mK)

Notes: Scoring uses a T0 result-level comparison: the checker compares the reported thermal_conductivity values to hidden paper-reported values with a tolerance (e.g., ±15% relative) and additionally checks the coating-induced increase trend. The agent must produce correct values and positive increase.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "thermal_conductivity"
        ],
        "columns": {
          "condition": "string, one of: pristine, vacancy_0.5, vacancy_1.0, coated_0.5_3nm, coated_1.0_3nm",
          "thermal_conductivity": "float (W/mK)"
        }
      },
      "description": "Compiled axial thermal conductivity values for each configuration. The checker will verify that (1) each value matches paper-reported gold values within tolerance, and (2) for each vacancy concentration, the coated conductivity exceeds the defective uncoated conductivity."
    }
  ],
  "notes": "Scoring uses a T0 result-level comparison: the checker compares the reported thermal_conductivity values to hidden paper-reported values with a tolerance (e.g., ±15% relative) and additionally checks the coating-induced increase trend. The agent must produce correct values and positive increase."
}
```

## How you are scored
A hidden verifier reads your `thermal_conductivities.csv`. It compares each thermal conductivity to a hidden benchmark value with an appropriate tolerance, and verifies that the coated configurations satisfy a predefined relational condition relative to the corresponding defective uncoated configurations for each vacancy concentration. The verifier then combines the checks (with the largest weight on the thermal conductivity values) into a single reward between 0 and 1. Reporting numbers that match the paper is not sufficient; the verifier uses hidden benchmarks not disclosed to you.
