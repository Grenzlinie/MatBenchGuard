# Molecular dynamics simulation of thermal transport in polycrystalline graphene

## Problem background
Understanding the thermal conductivity of polycrystalline graphene is crucial for thermal management in graphene-based electronic devices. Chemical vapor deposition (CVD) growth often produces polycrystalline rather than single-crystalline graphene, and the grain boundaries are known to strongly affect thermal transport. Molecular dynamics (MD) simulations can provide quantitative predictions of how grain size, tensile strain, and temperature influence the thermal conductivity, but a systematic computational reproduction is needed to establish reliable reference values. This task asks you to compute the in-plane thermal conductivity of polycrystalline graphene across a range of grain sizes, applied strains, and temperatures, and to report the normalized thermal conductivity relative to that of single-crystalline graphene.

## Approach
The workflow combines structure generation and non-equilibrium MD simulations. Polycrystalline graphene samples with average grain sizes from 2.5 nm to 12.5 nm are created using Voronoi tessellation with random grain orientations; a single-crystalline sample of the same 30 × 30 nm dimensions is prepared as a reference. After high-temperature annealing and equilibration, the reverse non-equilibrium molecular dynamics (RNEMD) method is applied: the simulation box is divided into slabs, a heat flux is imposed by continuously adding and removing kinetic energy at opposite ends, and the resulting temperature gradient is measured. Thermal conductivity K is obtained from Fourier's law using the steady-state heat flux and the time-averaged temperature profile. The Adaptive Intermolecular Reactive Bond Order (AIREBO) potential describes the carbon–carbon interactions. All conductivity values are normalized by the single-crystalline value at 300 K and zero applied strain (K0) to give K/K0. The same procedure is repeated under tensile strains (0 to 0.12) for selected grain sizes and at temperatures from 300 K to 500 K for other selected grain sizes. This approach systematically maps the dependence of thermal conductivity on microstructural features and external conditions.

## Reproduction target
Compute and tabulate the normalized thermal conductivity (K/K0) and the absolute thermal conductivity (W/(m·K)) for the following simulation conditions:

- Grain size series: single-crystalline graphene and polycrystalline graphene with average grain sizes of 2.5, 5, 7.5, 10, and 12.5 nm, all at 300 K and zero strain.
- Strain series: single-crystalline, 2.5 nm, and 7.5 nm samples at 300 K under tensile strains of 0, 0.03, 0.06, 0.09, and 0.12.
- Temperature series: single-crystalline, 2.5 nm, and 10 nm samples at zero strain for temperatures of 300, 400, and 500 K.

The normalization constant K0 is your computed thermal conductivity for single-crystalline graphene at 300 K and zero strain.

Write all results to a CSV file at `/app/outputs/thermal_conductivity_results.csv` containing exactly these columns: `grain_size_nm` (float; use -1 for single-crystalline), `strain` (float, dimensionless), `temperature_K` (float), `absolute_K_W_mK` (float), and `normalized_K` (float). Each row corresponds to one of the conditions listed above.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org

## Workflow steps

### Step 1: Generate polycrystalline graphene structures
- Role: process
- Action: Create atomic configurations of polycrystalline graphene with average grain sizes of 2.5, 5, 7.5, 10, and 12.5 nm and overall dimensions 30×30 nm using Voronoi tessellation with random grain centers and orientations (0 to π/3 rad). Anneal each sample at 3000 K for 50 ps (NVT), cool to 300 K, equilibrate at 300 K for 10 ps, relax to zero stress (NPT) for 10 ps. Also prepare a single-crystalline graphene sample of 30×30 nm for reference.
- Evidence: `/app/outputs/structures.tar.gz`

### Step 2: Compute thermal conductivity via RNEMD
- Role: scored (load-bearing)
- Action: For each grain size sample and the single-crystalline (SC) sample, run reverse non-equilibrium MD (RNEMD) using LAMMPS/AIREBO with a 0.1 fs timestep. Divide simulation box into 60 slabs along x, impose heat flux, run 1e6 steps to steady state and 2e6 steps for averaging. Compute temperature gradient and thermal conductivity K via Fourier's law. Normalize by SC value at 300 K zero strain to obtain K/K0. Repeat for tensile strains 0, 0.03, 0.06, 0.09, 0.12 on SC, 2.5 nm, and 7.5 nm samples. Repeat for temperatures 300, 400, 500 K on SC, 2.5 nm, and 10 nm samples at zero strain. Compile all absolute and normalized thermal conductivities into a CSV file.
- Output file: `/app/outputs/thermal_conductivity_results.csv`
- Format: csv
- Contract: Columns: grain_size_nm (float, -1 for single-crystalline), strain (float), temperature_K (float), absolute_K_W_mK (float), normalized_K (float).
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
- target_policy: reference_match
- description: CSV file containing computed normalized thermal conductivity (K/K0) and absolute thermal conductivity for all simulation conditions: grain size series (5 rows for grain sizes 2.5,5,7.5,10,12.5 nm at strain=0, temp=300 K), strain series (15 rows for SC, 2.5 nm, 7.5 nm at strains 0,0.03,0.06,0.09,0.12, temp=300 K), and temperature series (9 rows for SC, 2.5 nm, 10 nm at temps 300,400,500 K, strain=0).
- schema:
  - `type`: table
  - `required_columns`: `grain_size_nm`, `strain`, `temperature_K`, `absolute_K_W_mK`, `normalized_K`
  - `units`:
    - `grain_size_nm`: nm, -1 for single-crystalline
    - `strain`: dimensionless
    - `temperature_K`: K
    - `absolute_K_W_mK`: W/(m·K)
    - `normalized_K`: dimensionless ratio

Notes: The normalized values use the agent's own computed K0 for single-crystalline graphene at 300 K zero strain. Only the normalized_K values are scored against the paper's reported data.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "grain_size_nm",
          "strain",
          "temperature_K",
          "absolute_K_W_mK",
          "normalized_K"
        ],
        "units": {
          "grain_size_nm": "nm, -1 for single-crystalline",
          "strain": "dimensionless",
          "temperature_K": "K",
          "absolute_K_W_mK": "W/(m·K)",
          "normalized_K": "dimensionless ratio"
        }
      },
      "description": "CSV file containing computed normalized thermal conductivity (K/K0) and absolute thermal conductivity for all simulation conditions: grain size series (5 rows for grain sizes 2.5,5,7.5,10,12.5 nm at strain=0, temp=300 K), strain series (15 rows for SC, 2.5 nm, 7.5 nm at strains 0,0.03,0.06,0.09,0.12, temp=300 K), and temperature series (9 rows for SC, 2.5 nm, 10 nm at temps 300,400,500 K, strain=0)."
    }
  ],
  "notes": "The normalized values use the agent's own computed K0 for single-crystalline graphene at 300 K zero strain. Only the normalized_K values are scored against the paper's reported data."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads `/app/outputs/thermal_conductivity_results.csv`. The verifier compares the `normalized_K` values you report to a set of hidden reference values derived from the paper's published data. Your score is based on how closely your computed values match those references, and on the consistency of the reported trends (e.g., monotonic behavior with grain size, strain, and temperature). Different simulation series contribute with different weights: the grain size series carries the highest weight, while the strain and temperature series each carry a smaller but still significant weight. The verifier does not reveal the exact tolerances or the reference values. Simply copying the paper's numbers without performing the MD simulations will not satisfy the task; the verifier expects the output to be the result of actually running the prescribed MD workflow.
