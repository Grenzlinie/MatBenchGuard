# Molecular Dynamics Simulation of Elium Polymerization: Prediction of Physical, Mechanical, and Thermal Property Evolution

## Problem background
Elium-based thermoplastic composites offer recyclability and in‑situ polymerisation, but optimising processing and minimising residual stresses requires accurate predictions of physical, thermal, and mechanical properties as a function of the extent of polymerisation. Molecular dynamics (MD) can provide these property‑vs‑conversion curves, yet no such dataset exists for the Elium/PMMA system. This task challenges you to computationally reproduce the complete set of property‑evolution curves using an MD protocol with a reactive force field.

## Approach
You will build atomistic models of a 1:1 mixture of methyl methacrylate (MMA) monomers and dimers (total 15 435 atoms), described by the IFF‑R reactive force field. Using LAMMPS, you will simulate a free‑radical‑like polymerisation via the 'fix bond/react' command, generating snapshots at increasing extents of reaction. After annealing and equilibration, you will compute mass density and volumetric shrinkage from box volumes; bulk modulus from pressure‑volume response; shear modulus, Young's modulus, Poisson's ratio, and yield strength from shear deformation simulations; and the glass transition temperature (Tg) and coefficients of thermal expansion from a heating ramp. All properties will be computed for multiple independent replicates to estimate uncertainty.

## Reproduction target
Run the complete MD workflow (model construction, polymerisation, post‑processing, property simulations) for the Elium surrogate system and produce three scored CSV files: `physical_properties.csv` (mass density and volumetric shrinkage vs. extent), `mechanical_properties.csv` (bulk, shear, Young's moduli, Poisson's ratio, yield strength vs. extent), and `thermal_properties.csv` (Tg and CTE above/below Tg vs. extent). For each property, report the mean and standard error over at least three replicate models. The verifier will compare your computed mean values and trends against hidden reference values derived from independent measurements.

## Assets

- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://lammps.sandia.gov/
- IFF‑R (Reactive Interface Force Field) parameters: https://github.com/HeinzLab/interface-force-field
- Python scientific stack: numpy scipy pandas matplotlib
- OVITO visualization software: https://www.ovito.org/

## Workflow steps

### Step 1: Initial model construction and equilibration
- Role: process
- Action: Build a periodic simulation box containing 343 MMA monomers and 343 MMA dimers (15435 atoms). Perform energy minimization, densification to 1.01 g/cc at 300 K (NVT), an annealing cycle (300→500 K, hold 500 ps, cool to 300 K at 50 K/ns), and NPT equilibration. Create at least 3 replicate models with different initial velocities.
- Evidence: `/app/outputs/equilibration.log`

### Step 2: Reactive polymerisation simulation
- Role: process
- Action: Using the 'fix bond/react' command in LAMMPS, simulate polymerisation with the specified monomer‑dimer and dimer‑dimer reaction templates. Heat from 300 K to 800 K at 62.5 K/ns (timestep 0.1 fs), stabilise reaction sites every 5000 steps. Output trajectory snapshots at extents of reaction 0.0, 0.1, 0.2, …, up to 0.915 for each replicate.
- Evidence: `/app/outputs/polymerization.log`

### Step 3: Post‑polymerisation annealing and equilibration
- Role: process
- Action: For each snapshot at each extent, cool to 300 K (NPT isotropic), then anneal at 500 K, cool to 300 K at 50 K/ns, and finally equilibrate anisotropically at 300 K for 1 ns. This relaxes residual stresses and yields the final models for property analysis.
- Evidence: `/app/outputs/post_anneal.log`

### Step 4: Physical property analysis
- Role: scored
- Action: From the equilibrated volumes of the initial and annealed models, compute mass density and volumetric shrinkage at each extent of reaction. Compute the mean and standard error across replicates and write the results to physical_properties.csv.
- Output file: `/app/outputs/physical_properties.csv`
- Format: csv
- Contract: Columns: extent (float, 0.0 to 0.915 in steps of 0.1 plus 0.915), density_g_per_cc (float), density_std (float), volumetric_shrinkage_pct (float), shrinkage_std (float). All values are mean ± standard error over replicates.
- Scoring: scored by hidden verifier

### Step 5: Mechanical property simulations
- Role: process
- Action: For each equilibrated model at each extent, run two types of simulations: (a) NPT at 1 atm and 5000 atm to obtain average volumes for bulk modulus; (b) shear deformation at 20% strain in three principal planes at a rate of 2×10⁸ s⁻¹ in NPT. Record volumes and stress‑strain data.
- Evidence: `/app/outputs/mech_sim.log`

### Step 6: Mechanical property analysis
- Role: scored
- Action: From the pressure‑volume data compute the bulk modulus. From shear stress‑strain curves, determine shear modulus via bilinear fit, then calculate Young's modulus, Poisson's ratio, and yield strength (von Mises stress at the breakpoint). Aggregate across replicates and write mechanical_properties.csv with mean and standard error.
- Output file: `/app/outputs/mechanical_properties.csv`
- Format: csv
- Contract: Columns: extent (float), bulk_modulus_GPa (float), bulk_std (float), shear_modulus_GPa (float), shear_std (float), Youngs_modulus_GPa (float), Youngs_std (float), Poisson_ratio (float), Poisson_std (float), yield_strength_MPa (float), yield_std (float). All values are mean ± standard error over replicates.
- Scoring: scored by hidden verifier

### Step 7: Thermal property simulation
- Role: process
- Action: For each equilibrated model at extents ≥0.4, perform an NPT heating ramp from 250 K to 550 K at 50 K/ns (timestep 1 fs) and record volume vs. temperature.
- Evidence: `/app/outputs/thermal_sim.log`

### Step 8: Thermal property analysis
- Role: scored
- Action: Apply a bilinear breakpoint analysis to each volume‑temperature curve to determine Tg. Compute the slopes below and above Tg to obtain the coefficients of thermal expansion. Output the mean and standard error to thermal_properties.csv.
- Output file: `/app/outputs/thermal_properties.csv`
- Format: csv
- Contract: Columns: extent (float, 0.4 to 0.915), Tg_C (float), Tg_std (float), CTE_below_Tg_per_C (float, ×10⁻⁵), CTE_below_std (float), CTE_above_Tg_per_C (float, ×10⁻⁵), CTE_above_std (float). All values are mean ± standard error over replicates.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/physical_properties.csv`
- `/app/outputs/mechanical_properties.csv`
- `/app/outputs/thermal_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### physical_properties.csv
- path: `/app/outputs/physical_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mean and standard error of mass density and volumetric shrinkage across replicates, as a function of extent of reaction.
- schema:
  - `type`: table
  - `required_columns`: `extent`, `density_g_per_cc`, `density_std`, `volumetric_shrinkage_pct`, `shrinkage_std`
  - `units`:
    - `density_g_per_cc`: g/cm³
    - `volumetric_shrinkage_pct`: %

### mechanical_properties.csv
- path: `/app/outputs/mechanical_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mean and standard error of bulk modulus, shear modulus, Young's modulus, Poisson's ratio, and yield strength across replicates, as a function of extent of reaction. For extents <0.4 (liquid state) shear modulus and yield strength are negligible; Poisson's ratio ~0.5.
- schema:
  - `type`: table
  - `required_columns`: `extent`, `bulk_modulus_GPa`, `bulk_std`, `shear_modulus_GPa`, `shear_std`, `Youngs_modulus_GPa`, `Youngs_std`, `Poisson_ratio`, `Poisson_std`, `yield_strength_MPa`, `yield_std`
  - `units`:
    - `bulk_modulus_GPa`: GPa
    - `shear_modulus_GPa`: GPa
    - `Youngs_modulus_GPa`: GPa
    - `yield_strength_MPa`: MPa

### thermal_properties.csv
- path: `/app/outputs/thermal_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mean and standard error of glass transition temperature and coefficient of thermal expansion (below and above Tg) across replicates, for extents ≥0.4.
- schema:
  - `type`: table
  - `required_columns`: `extent`, `Tg_C`, `Tg_std`, `CTE_below_Tg_per_C`, `CTE_below_std`, `CTE_above_Tg_per_C`, `CTE_above_std`
  - `units`:
    - `Tg_C`: °C
    - `CTE_below_Tg_per_C`: 10⁻⁵/°C
    - `CTE_above_Tg_per_C`: 10⁻⁵/°C

Notes: The scored artifacts are compared to hidden reference values extracted from the paper's reported curves. Tolerances account for force‑field, implementation, and sampling differences. The checker expects monotonic trends: density, moduli, yield strength, and Tg increase with extent; CTE decreases; Poisson's ratio decreases from ~0.5. Liquid‑state behavior (shear modulus/yield strength ~0 for extents ≤0.3) is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "physical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "extent",
          "density_g_per_cc",
          "density_std",
          "volumetric_shrinkage_pct",
          "shrinkage_std"
        ],
        "units": {
          "density_g_per_cc": "g/cm³",
          "volumetric_shrinkage_pct": "%"
        }
      },
      "description": "Mean and standard error of mass density and volumetric shrinkage across replicates, as a function of extent of reaction."
    },
    {
      "file": "mechanical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "extent",
          "bulk_modulus_GPa",
          "bulk_std",
          "shear_modulus_GPa",
          "shear_std",
          "Youngs_modulus_GPa",
          "Youngs_std",
          "Poisson_ratio",
          "Poisson_std",
          "yield_strength_MPa",
          "yield_std"
        ],
        "units": {
          "bulk_modulus_GPa": "GPa",
          "shear_modulus_GPa": "GPa",
          "Youngs_modulus_GPa": "GPa",
          "yield_strength_MPa": "MPa"
        }
      },
      "description": "Mean and standard error of bulk modulus, shear modulus, Young's modulus, Poisson's ratio, and yield strength across replicates, as a function of extent of reaction. For extents <0.4 (liquid state) shear modulus and yield strength are negligible; Poisson's ratio ~0.5."
    },
    {
      "file": "thermal_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "extent",
          "Tg_C",
          "Tg_std",
          "CTE_below_Tg_per_C",
          "CTE_below_std",
          "CTE_above_Tg_per_C",
          "CTE_above_std"
        ],
        "units": {
          "Tg_C": "°C",
          "CTE_below_Tg_per_C": "10⁻⁵/°C",
          "CTE_above_Tg_per_C": "10⁻⁵/°C"
        }
      },
      "description": "Mean and standard error of glass transition temperature and coefficient of thermal expansion (below and above Tg) across replicates, for extents ≥0.4."
    }
  ],
  "notes": "The scored artifacts are compared to hidden reference values extracted from the paper's reported curves. Tolerances account for force‑field, implementation, and sampling differences. The checker expects monotonic trends: density, moduli, yield strength, and Tg increase with extent; CTE decreases; Poisson's ratio decreases from ~0.5. Liquid‑state behavior (shear modulus/yield strength ~0 for extents ≤0.3) is required."
}
```

## How you are scored
A hidden verifier will read your three CSV files from `/app/outputs` and compute a weighted score across the three property classes (physical, mechanical, thermal). For each property, the verifier compares your reported mean values against reference values, checks that the trends as a function of extent are physically reasonable (e.g., mass density and moduli increase, CTE decreases, Poisson’s ratio evolves from liquid‑like toward solid‑like), and verifies that your results are consistent with the required output schema. The final reward is a number between 0 and 1. Simply copying known reference values is not sufficient—the verifier is designed to reward honestly computed quantities that match expected physical behavior.
