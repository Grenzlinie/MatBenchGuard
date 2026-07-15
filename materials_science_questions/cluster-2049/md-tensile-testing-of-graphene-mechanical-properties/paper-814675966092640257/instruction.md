# Thermal conductivity of polycrystalline graphene under grain size, strain and temperature via MD

## Problem background
Chemical vapor deposition (CVD) can produce large-area graphene, but the resulting films are polycrystalline, containing grain boundaries that are expected to influence thermal transport. Understanding how the thermal conductivity of such realistic polycrystalline graphene sheets depends on grain size, external tensile strain, and temperature is essential for the thermal management of graphene-based electronic and energy devices. This task reproduces a systematic molecular dynamics investigation of these effects using realistic polycrystalline graphene structures.


## Approach
Polycrystalline graphene sheets (30 × 30 nm) with average grain sizes ranging from 2.5 nm to 12.5 nm are constructed using Voronoi tessellation with randomly oriented grains. The atomic configurations are equilibrated through a protocol of high-temperature annealing, cooling, and relaxation to zero stress. All molecular dynamics simulations are performed with the AIREBO potential in LAMMPS. The thermal conductivity is computed using the reverse non-equilibrium molecular dynamics (RNEMD) method: the simulation cell is divided into slabs, a heat flux is imposed between designated hot and cold regions, the steady-state temperature gradient is measured, and the conductivity is obtained via Fourier’s law. A reference single-crystalline graphene sheet of identical dimensions is prepared and its conductivity K₀ is computed in the same manner, so that the polycrystalline conductivities can be expressed as normalized values K/K₀. After the grain-size dependence is established, the effect of uniaxial tensile strain (0 to 0.12) and temperature (200 K to 600 K) is investigated for selected grain sizes, always comparing with the single-crystal case.


## Reproduction target
The objective is to produce three results files under `/app/outputs`:
- `grain_size_results.csv` – normalized thermal conductivity K/K₀ for polycrystalline graphene with grain sizes 2.5, 5, 7.5, 10, and 12.5 nm at 300 K.
- `strain_results.csv` – thermal conductivity (in W/mK) as a function of uniaxial tensile strain (0, 0.03, 0.06, 0.09, 0.12) for single‑crystalline graphene (`SC`) and for polycrystalline graphene with grain sizes 2.5 nm and 7.5 nm.
- `temperature_results.csv` – thermal conductivity (in W/mK) as a function of temperature (200, 300, 400, 500, 600 K) for single‑crystalline graphene and for polycrystalline graphene with grain sizes 2.5 nm and 10 nm.

The exact column schemas are specified in the workflow steps. The results must be obtained by running the full MD workflow described in the steps; no external data files or pre‑computed numbers are provided.


## Assets

- LAMMPS: https://lammps.sandia.gov/

## Workflow steps

### Step 1: Generate polycrystalline graphene structures
- Role: process
- Action: Use Voronoi tessellation with random grain orientations (0 to π/3 rad) to construct polycrystalline graphene sheets of 30×30 nm with average grain sizes 2.5, 5, 7.5, 10, 12.5 nm. Anneal at 3000 K for 50 ps (NVT), cool to 300 K, equilibrate 10 ps (NVT), relax to zero stress 10 ps (NPT). Save the relaxed atomic configurations.
- Evidence: `/app/outputs/structures_generated.txt`

### Step 2: Prepare reference single-crystalline graphene
- Role: process
- Action: Generate a 30×30 nm defect-free single-crystalline graphene sheet and subject it to the same equilibration protocol (300 K NVT 10 ps, NPT relax 10 ps).
- Evidence: `/app/outputs/sc_structure_generated.txt`

### Step 3: Compute reference thermal conductivity K0
- Role: process
- Action: Run reverse non-equilibrium MD (RNEMD) on the single-crystalline graphene at 300 K using LAMMPS with AIREBO, 0.1 fs timestep, 60 slabs, heat flux imposed, steady-state and averaging steps. Compute the thermal conductivity K0 from Fourier's law. Save the computed value.
- Evidence: `/app/outputs/k0_reference.txt`

### Step 4: Compute normalized thermal conductivity vs grain size
- Role: scored (load-bearing)
- Action: For each polycrystalline grain size (2.5,5,7.5,10,12.5 nm), run RNEMD at 300 K with the same protocol as step_03 to obtain thermal conductivity K. Normalize each K by the K0 from step_03. Output the grain size and K/K0 pairs.
- Output file: `/app/outputs/grain_size_results.csv`
- Format: csv
- Contract: Header: grain_size_nm,K_over_K0. Five rows for grain sizes 2.5,5,7.5,10,12.5. K_over_K0 is a dimensionless float.
- Scoring: scored by hidden verifier

### Step 5: Compute thermal conductivity vs tensile strain
- Role: scored
- Action: For single-crystalline graphene and for polycrystalline sheets with grain sizes 2.5 nm and 7.5 nm, apply uniaxial tensile strains of 0, 0.03, 0.06, 0.09, 0.12. Re-equilibrate and run RNEMD to obtain the thermal conductivity K at each strain. Collect results in a CSV.
- Output file: `/app/outputs/strain_results.csv`
- Format: csv
- Contract: Header: sample_type,strain,thermal_conductivity. sample_type is one of 'SC','poly_2.5nm','poly_7.5nm'. strain is a float in [0,0.12]. thermal_conductivity is a float (units W/mK).
- Scoring: scored by hidden verifier

### Step 6: Compute thermal conductivity vs temperature
- Role: scored
- Action: For single-crystalline graphene and for polycrystalline sheets with grain sizes 2.5 nm and 10 nm, run RNEMD at temperatures of 200, 300, 400, 500, 600 K. Compute thermal conductivity K for each case and output the results.
- Output file: `/app/outputs/temperature_results.csv`
- Format: csv
- Contract: Header: sample_type,temperature_K,thermal_conductivity. sample_type is one of 'SC','poly_2.5nm','poly_10nm'. temperature_K is an integer. thermal_conductivity is a float (units W/mK).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/grain_size_results.csv`
- `/app/outputs/strain_results.csv`
- `/app/outputs/temperature_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### grain_size_results.csv
- path: `/app/outputs/grain_size_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized thermal conductivity K/K0 for polycrystalline graphene with grain sizes 2.5, 5, 7.5, 10, 12.5 nm.
- schema:
  - `type`: table
  - `required_columns`: `grain_size_nm`, `K_over_K0`
  - `units`:
    - `K_over_K0`: dimensionless

### strain_results.csv
- path: `/app/outputs/strain_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermal conductivity under uniaxial tensile strain for single-crystalline and polycrystalline graphene (2.5 nm, 7.5 nm).
- schema:
  - `type`: table
  - `required_columns`: `sample_type`, `strain`, `thermal_conductivity`
  - `units`:
    - `thermal_conductivity`: W/mK

### temperature_results.csv
- path: `/app/outputs/temperature_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Thermal conductivity at 200–600 K for single-crystalline and polycrystalline graphene (2.5 nm, 10 nm).
- schema:
  - `type`: table
  - `required_columns`: `sample_type`, `temperature_K`, `thermal_conductivity`
  - `units`:
    - `thermal_conductivity`: W/mK

Notes: All scored outputs are compared to hidden reference values derived from the paper's tables and figures. The agent must run the full RNEMD simulations; no pre-computed results are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "grain_size_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "grain_size_nm",
          "K_over_K0"
        ],
        "units": {
          "K_over_K0": "dimensionless"
        }
      },
      "description": "Normalized thermal conductivity K/K0 for polycrystalline graphene with grain sizes 2.5, 5, 7.5, 10, 12.5 nm."
    },
    {
      "file": "strain_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample_type",
          "strain",
          "thermal_conductivity"
        ],
        "units": {
          "thermal_conductivity": "W/mK"
        }
      },
      "description": "Thermal conductivity under uniaxial tensile strain for single-crystalline and polycrystalline graphene (2.5 nm, 7.5 nm)."
    },
    {
      "file": "temperature_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample_type",
          "temperature_K",
          "thermal_conductivity"
        ],
        "units": {
          "thermal_conductivity": "W/mK"
        }
      },
      "description": "Thermal conductivity at 200–600 K for single-crystalline and polycrystalline graphene (2.5 nm, 10 nm)."
    }
  ],
  "notes": "All scored outputs are compared to hidden reference values derived from the paper's tables and figures. The agent must run the full RNEMD simulations; no pre-computed results are provided."
}
```

## How you are scored
A hidden verifier independently reads each of the three scored CSV files and compares the reported values (and, where applicable, the qualitative trends such as monotonicity and the relative sensitivity of different samples) against reference data derived from the paper’s published tables and figures. The comparisons use tolerances that are appropriate for the reproducibility of MD simulations with the specified potential and protocol. Each scored step contributes a weight to the final reward; the total reward is the weighted sum of the individual scores. Simply reporting numbers that match a known reference without actually executing the simulation workflow will not satisfy the trend and consistency checks that the verifier performs, and will therefore receive little to no credit.
