# Mechanical properties of h-BN grain boundaries from molecular dynamics

## Problem background
Hexagonal boron nitride (h‑BN) is a two‑dimensional analogue of graphene with exceptional mechanical, thermal and electronic properties. During synthesis, grain boundaries form where crystalline domains meet, introducing topological defects that can alter the material's mechanical response. Understanding how grain boundary linear density, arrangement, and external conditions such as strain rate and temperature affect the stiffness and strength of h‑BN nanosheets is critical for designing robust nanodevices. Molecular dynamics simulations capture the atomistic mechanisms of deformation and failure, providing quantitative predictions of key mechanical properties—Young’s modulus, ultimate tensile strength, and failure strain—for pristine and polycrystalline h‑BN under uniaxial tension.

## Approach
Classical molecular dynamics with an optimized Tersoff potential is used to model B–N interactions. Atomic models of a pristine monolayer h‑BN sheet and several grain‑boundary configurations are built from known lattice constants and boundary‑defining translation vectors. Each model is equilibrated to a stress‑free state at 300 K by energy minimization, NPT, and NVT relaxation. Uniaxial tensile tests are then performed at a constant engineering strain rate while the system stress is recorded. Mechanical properties (Young’s modulus, ultimate tensile strength, failure strain) are extracted from the resulting stress–strain curves. Additional simulations probe the effects of strain rate and temperature by varying the applied strain rate and the simulation temperature for selected grain‑boundary models.

## Reproduction target
Produce four comma‑separated‑value (CSV) files under `/app/outputs/` that report the mechanical properties derived from the MD tensile tests:

- `pristine_mechanical_properties.csv`: for a pristine monolayer h‑BN sheet, report Young’s modulus, ultimate tensile strength, and failure strain along both the zigzag and armchair directions.
- `gb_mechanical_properties.csv`: for at least six grain‑boundary models with known linear densities along zigzag and armchair directions, report the same mechanical properties together with the GB linear density.
- `strain_rate_results.csv`: for two representative GB models, report ultimate tensile strength and Young’s modulus at five strain rates between 1e8 s⁻¹ and 1e10 s⁻¹.
- `temperature_results.csv`: for the same two models, report ultimate tensile strength and Young’s modulus at five temperatures between 1 K and 1100 K.

## Assets

- LAMMPS: https://www.lammps.org

## Workflow steps

### Step 1: Construct atomic models
- Role: process
- Action: Generate atomic coordinates for a pristine monolayer h-BN sheet (lattice constant 2.52 Å, B–N bond 1.45 Å) and at least six grain boundary configurations using the translation vectors (2,1)|(1,2), (3,2)|(2,3), (6,5)|(5,6) along zigzag and (1,9)|(9,1), (1,4)|(4,1), (2,5)|(5,2) along armchair. Models should have approximate dimensions 15 nm × 15 nm with periodic boundary conditions in‑plane and a 100 Å vacuum layer. Output LAMMPS data files.
- Evidence: `/app/outputs/model_generation.log`

### Step 2: MD relaxation
- Role: process
- Action: For each model, perform energy minimization, then equilibration at 300 K using an NPT ensemble for 50 ps followed by an NVT ensemble for 30 ps with a 1 fs timestep, using the Tersoff potential with the parameters optimised by Kinaci et al. for h‑BN:

nnn,3.0,1.0,0.0,17.7959,5.9484,0.00000,0.6184432,0.019251,2.6272721,138.77866,2.0,0.1,2.8293093,128.86866
bb,3.0,1.0,0.0,0.52629,0.001587,0.5,3.9929061,0.0000016,2.0774982,43.132016,2.0,0.1,2.2372578,40.0520156
bn,3.0,1.0,0.0,25000,4.3484,-0.89000,0.72751,0.000000125724,2.199,340.0,1.95,0.05,3.568,1380.0

These rows correspond to N‑N, B‑B, and B‑N (or N‑B) interactions respectively. The columns are: pair, m, γ, λIII (Å⁻¹), c, d, h, n, β, λII (Å⁻¹), B (eV), R (Å), D (Å), λI (Å⁻¹), A (eV).
- Evidence: `/app/outputs/relaxation.log`

### Step 3: Baseline tensile test simulations
- Role: process
- Action: For each relaxed model, perform uniaxial tensile deformation at 300 K and a constant engineering strain rate of 1e8 s⁻¹. Apply load perpendicular to the grain boundary line. For the pristine sheet, test both zigzag and armchair directions. Record stress–strain data.
- Evidence: `/app/outputs/stress_strain_baseline.log`

### Step 4: Pristine mechanical properties
- Role: scored
- Action: From the stress-strain curves of the pristine sheet obtained in step 03, extract Young's modulus (initial linear slope), ultimate tensile strength (peak stress), and critical failure strain (strain at catastrophic stress drop). Report one row for zigzag direction and one for armchair direction.
- Output file: `/app/outputs/pristine_mechanical_properties.csv`
- Format: csv
- Contract: columns: direction (string: zz|am), Youngs_modulus_GPa (float), UTS_GPa (float), failure_strain_percent (float)
- Scoring: scored by hidden verifier

### Step 5: GB mechanical properties
- Role: scored (load-bearing)
- Action: From the stress-strain curves of the grain boundary models obtained in step 03, extract Young's modulus, ultimate tensile strength, and critical failure strain. Write one row per model.
- Output file: `/app/outputs/gb_mechanical_properties.csv`
- Format: csv
- Contract: columns: model_name (string), direction (string: zz|am), GB_linear_density_nm-1 (float), Youngs_modulus_GPa (float), UTS_GPa (float), failure_strain_percent (float)
- Scoring: scored by hidden verifier

### Step 6: Strain‑rate tensile test simulations
- Role: process
- Action: For grain boundary models (2,1)|(1,2) and (1,9)|(9,1), perform tensile simulations at 300 K with strain rates of 1e8, 5e8, 1e9, 5e9, and 1e10 s⁻¹. Record stress–strain data.
- Evidence: `/app/outputs/strain_rate_simulations.log`

### Step 7: Strain‑rate effects
- Role: scored (load-bearing)
- Action: For each strain‑rate simulation, extract ultimate tensile strength and Young's modulus. Report them organized by model and strain rate.
- Output file: `/app/outputs/strain_rate_results.csv`
- Format: csv
- Contract: columns: model_name (string), strain_rate_s-1 (float), UTS_GPa (float), Youngs_modulus_GPa (float)
- Scoring: scored by hidden verifier

### Step 8: Temperature‑dependent tensile test simulations
- Role: process
- Action: For grain boundary models (2,1)|(1,2) and (1,9)|(9,1), perform tensile simulations at a strain rate of 1e8 s⁻¹ and temperatures of 1, 300, 500, 800, and 1100 K. Record stress–strain data.
- Evidence: `/app/outputs/temperature_simulations.log`

### Step 9: Temperature effects
- Role: scored (load-bearing)
- Action: For each temperature‑dependent simulation, extract ultimate tensile strength and Young's modulus. Report them organized by model and temperature.
- Output file: `/app/outputs/temperature_results.csv`
- Format: csv
- Contract: columns: model_name (string), temperature_K (int), UTS_GPa (float), Youngs_modulus_GPa (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pristine_mechanical_properties.csv`
- `/app/outputs/gb_mechanical_properties.csv`
- `/app/outputs/strain_rate_results.csv`
- `/app/outputs/temperature_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pristine_mechanical_properties.csv
- path: `/app/outputs/pristine_mechanical_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Baseline mechanical properties of pristine h-BN along zigzag and armchair directions, extracted from stress-strain curves.
- schema:
  - `type`: table
  - `required_columns`: `direction`, `Youngs_modulus_GPa`, `UTS_GPa`, `failure_strain_percent`
  - `units`:
    - `Youngs_modulus_GPa`: GPa
    - `UTS_GPa`: GPa
    - `failure_strain_percent`: %

### gb_mechanical_properties.csv
- path: `/app/outputs/gb_mechanical_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mechanical properties of grain boundary configurations, including GB linear density and the type of the first broken bond observed during tensile failure.
- schema:
  - `type`: table
  - `required_columns`: `model_name`, `direction`, `GB_linear_density_nm-1`, `Youngs_modulus_GPa`, `UTS_GPa`, `failure_strain_percent`, `first_broken_bond_type`
  - `units`:
    - `GB_linear_density_nm-1`: nm⁻¹
    - `Youngs_modulus_GPa`: GPa
    - `UTS_GPa`: GPa
    - `failure_strain_percent`: %

### strain_rate_results.csv
- path: `/app/outputs/strain_rate_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ultimate tensile strength and Young's modulus for selected GB models at different strain rates.
- schema:
  - `type`: table
  - `required_columns`: `model_name`, `strain_rate_s-1`, `UTS_GPa`, `Youngs_modulus_GPa`
  - `units`:
    - `strain_rate_s-1`: s⁻¹
    - `UTS_GPa`: GPa
    - `Youngs_modulus_GPa`: GPa

### temperature_results.csv
- path: `/app/outputs/temperature_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ultimate tensile strength and Young's modulus for selected GB models at different temperatures.
- schema:
  - `type`: table
  - `required_columns`: `model_name`, `temperature_K`, `UTS_GPa`, `Youngs_modulus_GPa`
  - `units`:
    - `temperature_K`: K
    - `UTS_GPa`: GPa
    - `Youngs_modulus_GPa`: GPa

Notes: The checker compares submitted values to hidden reference values with tolerances and also verifies structural trends: UTS increases with strain rate, UTS and Young's modulus decrease with temperature, and UTS and Young's modulus generally decrease with increasing GB linear density.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pristine_mechanical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "direction",
          "Youngs_modulus_GPa",
          "UTS_GPa",
          "failure_strain_percent"
        ],
        "units": {
          "Youngs_modulus_GPa": "GPa",
          "UTS_GPa": "GPa",
          "failure_strain_percent": "%"
        }
      },
      "description": "Baseline mechanical properties of pristine h-BN along zigzag and armchair directions, extracted from stress-strain curves."
    },
    {
      "file": "gb_mechanical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model_name",
          "direction",
          "GB_linear_density_nm-1",
          "Youngs_modulus_GPa",
          "UTS_GPa",
          "failure_strain_percent",
          "first_broken_bond_type"
        ],
        "units": {
          "GB_linear_density_nm-1": "nm⁻¹",
          "Youngs_modulus_GPa": "GPa",
          "UTS_GPa": "GPa",
          "failure_strain_percent": "%"
        }
      },
      "description": "Mechanical properties of grain boundary configurations, including GB linear density and the type of the first broken bond observed during tensile failure."
    },
    {
      "file": "strain_rate_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model_name",
          "strain_rate_s-1",
          "UTS_GPa",
          "Youngs_modulus_GPa"
        ],
        "units": {
          "strain_rate_s-1": "s⁻¹",
          "UTS_GPa": "GPa",
          "Youngs_modulus_GPa": "GPa"
        }
      },
      "description": "Ultimate tensile strength and Young's modulus for selected GB models at different strain rates."
    },
    {
      "file": "temperature_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model_name",
          "temperature_K",
          "UTS_GPa",
          "Youngs_modulus_GPa"
        ],
        "units": {
          "temperature_K": "K",
          "UTS_GPa": "GPa",
          "Youngs_modulus_GPa": "GPa"
        }
      },
      "description": "Ultimate tensile strength and Young's modulus for selected GB models at different temperatures."
    }
  ],
  "notes": "The checker compares submitted values to hidden reference values with tolerances and also verifies structural trends: UTS increases with strain rate, UTS and Young's modulus decrease with temperature, and UTS and Young's modulus generally decrease with increasing GB linear density."
}
```

## How you are scored
A hidden verifier inspects each scored CSV file. For every numeric quantity, your reported values are compared to a set of hidden reference values (derived from the original study) using relative tolerances; small deviations arising from differences in implementation or simulation details are acceptable. The verifier also performs structural checks: it verifies that your results follow the expected qualitative trends—for example, that ultimate tensile strength increases with strain rate and decreases with temperature, Young’s modulus decreases with temperature, and both strength and modulus generally decrease with increasing grain‑boundary linear density. Each artifact contributes a weighted portion to the final score, which is the combination of how well your numbers agree with the hidden references and whether the correct trends are present.
