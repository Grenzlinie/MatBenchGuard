# Thermal Conductivity of Strained Hexagonal Boron Nitride Nanoribbon via Molecular Dynamics

## Problem background
Efficient thermal management in nanoscale devices is a critical challenge. Hexagonal boron nitride nanoribbon (h-BNNR) is a wide-bandgap 2D material with potential electronic applications, but its thermal transport properties—especially under mechanical deformation—must be understood to ensure device reliability. This task investigates how uniaxial tensile strain in the zigzag direction affects the thermal conductivity of single-layer h-BNNR, and how this effect varies with temperature and ribbon width. By computing the thermal conductivity from first-principles molecular dynamics, we aim to quantify the strain-dependent thermal response of this material.

## Approach
The thermal conductivity is computed using equilibrium molecular dynamics (EMD) with the Green‑Kubo formulation. Atomic interactions are described by the Tersoff potential with the Lindsay–Broido parameterization, which accurately captures phonon dispersions in h‑BN. The procedure constructs a zigzag h‑BNNR of given dimensions, applies periodic boundary conditions along the zigzag axis, and imposes uniaxial tensile strain along that axis. After energy minimization and equilibration, the system is evolved in the NVE ensemble while recording the heat current. The heat current autocorrelation function (HCACF) is integrated to yield the thermal conductivity along the strained direction. This workflow is repeated for multiple values of strain, temperature, and ribbon width to map out the conductivity landscape.

## Reproduction target
Produce three CSV files containing the thermal conductivity of a 10 nm × 3 nm zigzag h‑BNNR under uniaxial tensile strain in the zigzag direction:
- `thermal_conductivity_vs_strain.csv`: thermal conductivity at 300 K for tensile strains of 0 %, 1 %, 2 %, 3 %, 4 %, and 5 %.
- `thermal_conductivity_vs_temperature.csv`: thermal conductivity for each of those six strain levels evaluated at temperatures 100 K, 200 K, 300 K, 400 K, 500 K, and 600 K.
- `thermal_conductivity_vs_width.csv`: thermal conductivity at 300 K for ribbon widths 1 nm, 2 nm, 3 nm, 4 nm, and 5 nm (length fixed at 10 nm) for each of the six strain levels.
All conductivities must be computed via the Green‑Kubo integral of the HCACF, using the LAMMPS EMD protocol with the Lindsay–Broido Tersoff parameters. The reported values should reflect the zigzag-direction conductivity (Kx).

## Assets

- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://lammps.sandia.gov
- Tersoff potential parameters for h-BN (Lindsay & Broido, 2011): https://www.ctcms.nist.gov/potentials/BN.html

## Workflow steps

### Step 1: Construct h-BNNR atomic structures
- Role: process
- Action: Build a 10 nm × 3 nm zigzag h-BNNR with B-N equilibrium bond length 0.1446 nm. Set up periodic boundary conditions along the zigzag direction. Apply uniaxial tensile strains along that direction for 0%, 1%, 2%, 3%, 4%, 5% (and for other required widths and lengths) to generate strained atomic coordinates. Output one or more LAMMPS data files.
- Evidence: `/app/outputs/structure_data.lmp`

### Step 2: Run equilibrium molecular dynamics simulations
- Role: process
- Action: Using the atomic structures, run LAMMPS EMD simulations with the Tersoff potential (Lindsay & Broido parameters). For each condition (strain, temperature, width) perform energy minimization, NVT equilibration (64 ps at target temperature), then NVE production (80 ps, timestep 0.4 fs), recording heat current every 5 simulation steps. For the strain series at 300 K, run 5 independent NVE ensembles with different initial velocities and average. Save raw heat current data per condition.
- Evidence: `/app/outputs/heat_current_data.log`

### Step 3: Thermal conductivity as a function of tensile strain
- Role: scored (load-bearing)
- Action: From the raw heat current data for strains 0–5% at 300 K, compute thermal conductivity in the zigzag direction using the Green-Kubo formula: K_x = (1 / (V k_B T^2)) * integral of heat current autocorrelation function. System volume V = area × van der Waals thickness (3.3 Å). Average over autocorrelation profiles and, for the strain series, average across the 5 independent NVE ensembles. Write a CSV with columns strain_percent and conductivity_W_mK for strains 0, 1, 2, 3, 4, 5 %.
- Output file: `/app/outputs/thermal_conductivity_vs_strain.csv`
- Format: csv
- Contract: strain_percent (float), conductivity_W_mK (float)
- Scoring: scored by hidden verifier

### Step 4: Thermal conductivity as a function of temperature
- Role: scored
- Action: From simulations at temperatures 100, 200, 300, 400, 500, 600 K for each strain (0–5%), compute thermal conductivity via Green-Kubo. Write a CSV with columns strain_percent, temperature_K, conductivity_W_mK.
- Output file: `/app/outputs/thermal_conductivity_vs_temperature.csv`
- Format: csv
- Contract: strain_percent (float), temperature_K (float), conductivity_W_mK (float)
- Scoring: scored by hidden verifier

### Step 5: Thermal conductivity as a function of ribbon width
- Role: scored
- Action: From simulations for ribbon widths 1, 2, 3, 4, 5 nm (fixed length 10 nm) at 300 K for each strain (0–5%), compute thermal conductivity via Green-Kubo. Write a CSV with columns strain_percent, width_nm, conductivity_W_mK.
- Output file: `/app/outputs/thermal_conductivity_vs_width.csv`
- Format: csv
- Contract: strain_percent (float), width_nm (float), conductivity_W_mK (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity_vs_strain.csv`
- `/app/outputs/thermal_conductivity_vs_temperature.csv`
- `/app/outputs/thermal_conductivity_vs_width.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity_vs_strain.csv
- path: `/app/outputs/thermal_conductivity_vs_strain.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermal conductivity of 10 nm × 3 nm zigzag h-BNNR as a function of uniaxial tensile strain (0-5%) at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `strain_percent`, `conductivity_W_mK`
  - `units`:
    - `strain_percent`: %
    - `conductivity_W_mK`: W/m·K

### thermal_conductivity_vs_temperature.csv
- path: `/app/outputs/thermal_conductivity_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermal conductivity as a function of temperature (100-600 K) for each applied tensile strain (0-5%).
- schema:
  - `type`: table
  - `required_columns`: `strain_percent`, `temperature_K`, `conductivity_W_mK`
  - `units`:
    - `strain_percent`: %
    - `temperature_K`: K
    - `conductivity_W_mK`: W/m·K

### thermal_conductivity_vs_width.csv
- path: `/app/outputs/thermal_conductivity_vs_width.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermal conductivity as a function of ribbon width (1-5 nm) at 300 K for each applied tensile strain (0-5%).
- schema:
  - `type`: table
  - `required_columns`: `strain_percent`, `width_nm`, `conductivity_W_mK`
  - `units`:
    - `strain_percent`: %
    - `width_nm`: nm
    - `conductivity_W_mK`: W/m·K

Notes: The checker compares the submitted thermal conductivity values to expected reference values with appropriate tolerances and verifies the monotonic decrease with strain, decrease with temperature, and increase with width for each strain condition.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity_vs_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_percent",
          "conductivity_W_mK"
        ],
        "units": {
          "strain_percent": "%",
          "conductivity_W_mK": "W/m·K"
        }
      },
      "description": "Thermal conductivity of 10 nm × 3 nm zigzag h-BNNR as a function of uniaxial tensile strain (0-5%) at 300 K."
    },
    {
      "file": "thermal_conductivity_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_percent",
          "temperature_K",
          "conductivity_W_mK"
        ],
        "units": {
          "strain_percent": "%",
          "temperature_K": "K",
          "conductivity_W_mK": "W/m·K"
        }
      },
      "description": "Thermal conductivity as a function of temperature (100-600 K) for each applied tensile strain (0-5%)."
    },
    {
      "file": "thermal_conductivity_vs_width.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_percent",
          "width_nm",
          "conductivity_W_mK"
        ],
        "units": {
          "strain_percent": "%",
          "width_nm": "nm",
          "conductivity_W_mK": "W/m·K"
        }
      },
      "description": "Thermal conductivity as a function of ribbon width (1-5 nm) at 300 K for each applied tensile strain (0-5%)."
    }
  ],
  "notes": "The checker compares the submitted thermal conductivity values to expected reference values with appropriate tolerances and verifies the monotonic decrease with strain, decrease with temperature, and increase with width for each strain condition."
}
```

## How you are scored
A hidden verifier scores each of the three output CSV files independently and combines them into a single reward using these weights: strain dependence 0.6, temperature dependence 0.3, width dependence 0.1. For each file, the verifier compares your reported conductivity values to reference benchmarks (with tolerances to absorb toolchain and seed variation) and checks that the data obey the expected physical trends (e.g., monotonic dependence on strain, temperature, and width). Your score reflects how accurately your computed values match the reference and how well they exhibit the correct qualitative behavior. Merely reporting numbers that look plausible without actually performing the simulations will not yield a passing score.
