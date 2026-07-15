# Pressure-dependent elastic and mechanical properties of a hexagonal crystal via REBO potential

## Problem background
A hexagonal polymorph of carbon (space group P6₃/mmc, typical lattice parameters a = 2.53 Å, c = 4.12 Å) is a candidate ultra‑hard material whose mechanical properties are of great interest. While some ground‑state elastic constants have been computed, the pressure‑dependent elastic and polycrystalline mechanical properties remain largely unexplored. This task computes the five independent single‑crystal elastic constants and a suite of derived polycrystalline moduli, wave velocities, and stability indicators over the pressure range 0–500 GPa, enabling a quantitative assessment of the material’s stiffness, brittleness, and anisotropy under compression.

## Approach
The computational approach uses a second‑generation reactive empirical bond‑order (REBO) potential to describe the interatomic interactions. Constant‑pressure geometry optimizations are performed with the open‑source General Utility Lattice Program (GULP) at T = 0 K for a series of applied pressures. After each optimization, the five independent elastic constants (C11, C12, C13, C33, C44) are extracted using the Voigt–Reuss–Hill averaging scheme. From these constants and the optimized density, the polycrystalline bulk modulus B, shear modulus G, Young modulus E, Poisson ratio ν, longitudinal and shear wave velocities Vp and Vs, Kleinman parameter ζ, and elastic anisotropy factor A are computed for each pressure. The same procedure is repeated at several pressures from 0 to 500 GPa, yielding the full pressure‑dependent trends.

## Reproduction target
Produce the following three scored output files by executing the workflow steps below:

1) `elastic_constants_0GPa.csv` – the five independent elastic constants at P = 0 GPa.
2) `derived_properties_0GPa.csv` – the eight derived polycrystalline properties at P = 0 GPa computed from your own elastic constants and density.
3) `pressure_dependence.csv` – a table containing all seven pressure values (0, 100, 200, 300, 400, 500 GPa): the pressure value itself, the five elastic constants, and the eight derived properties, one row per pressure.

The exact column names and units are specified in the output contracts below. The goal is to obtain a self‑consistent set of elastic and mechanical properties that satisfies the known mechanical stability conditions and shows physically sensible trends under increasing pressure.

## Assets

- General Utility Lattice Program (GULP): http://gulp.curtin.edu.au/

## Workflow steps

### Step 1: Geometry optimization under pressure
- Role: process
- Action: Using GULP with the second-generation REBO potential, perform constant-pressure geometry optimization of hexagonal diamond (space group P6₃/mmc, a = 2.53 Å, c = 4.12 Å) at T = 0 K for each pressure P = 0, 100, 200, 300, 400, 500 GPa. Employ the Newton–Raphson method with BFGS Hessian updates. Save the optimized structures for later use.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 2: Single-crystal elastic constants at 0 GPa
- Role: scored
- Action: From the optimized 0 GPa structure, compute the five independent elastic constants (C11, C12, C13, C33, C44) using the Voigt–Reuss–Hill averaging procedure. Write the values (in GPa, one decimal) to the output CSV.
- Output file: `/app/outputs/elastic_constants_0GPa.csv`
- Format: csv
- Contract: columns: C11, C12, C13, C33, C44; one row of numeric values in GPa, at least one decimal place.
- Scoring: scored by hidden verifier

### Step 3: Derived polycrystalline properties at 0 GPa
- Role: scored
- Action: Using the 0 GPa elastic constants and the corresponding density from the optimized structure, compute the bulk modulus B, shear modulus G, Young modulus E, Poisson ratio ν, longitudinal wave velocity Vp, shear wave velocity Vs, Kleinman parameter ζ, and anisotropy factor A via standard VRH relations for a hexagonal crystal. Write all values to the output CSV.
- Output file: `/app/outputs/derived_properties_0GPa.csv`
- Format: csv
- Contract: columns: B, E, G, v, Vp, Vs, zeta, A; B,E,G in GPa; Vp,Vs in km/s; v, zeta, A dimensionless. One row of numeric values.
- Scoring: scored by hidden verifier

### Step 4: Pressure-dependent properties
- Role: scored (load-bearing)
- Action: For each pressure (0, 100, 200, 300, 400, 500 GPa), compute the five elastic constants, density, and all derived properties (B, E, G, ν, Vp, Vs, ζ, A) from the corresponding optimized structure. Write one row per pressure to the output CSV.
- Output file: `/app/outputs/pressure_dependence.csv`
- Format: csv
- Contract: columns: pressure_GPa, C11, C12, C13, C33, C44, B, E, G, v, Vp, Vs, zeta, A. Pressure in GPa; Cij, B, E, G in GPa; Vp, Vs in km/s; v, zeta, A dimensionless. Six rows, one for each pressure.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants_0GPa.csv`
- `/app/outputs/derived_properties_0GPa.csv`
- `/app/outputs/pressure_dependence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants_0GPa.csv
- path: `/app/outputs/elastic_constants_0GPa.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Five single-crystal elastic constants at 0 GPa from the re-optimised structure; compared to the paper’s ground‑state values with allowed tolerances.
- schema:
  - `type`: table
  - `required_columns`: `C11`, `C12`, `C13`, `C33`, `C44`
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C33`: GPa
    - `C44`: GPa

### derived_properties_0GPa.csv
- path: `/app/outputs/derived_properties_0GPa.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Polycrystalline moduli and derived properties at 0 GPa, recomputed from the agent’s own elastic constants and density; the checker recomputes these quantities and compares them to paper‑reported values.
- schema:
  - `type`: table
  - `required_columns`: `B`, `E`, `G`, `v`, `Vp`, `Vs`, `zeta`, `A`
  - `units`:
    - `B`: GPa
    - `E`: GPa
    - `G`: GPa
    - `v`: 
    - `Vp`: km/s
    - `Vs`: km/s
    - `zeta`: 
    - `A`: 

### pressure_dependence.csv
- path: `/app/outputs/pressure_dependence.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Pressure‑dependent elastic constants and derived properties for 0–500 GPa; checked for monotonic trends and Born mechanical stability at every pressure.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `C11`, `C12`, `C13`, `C33`, `C44`, `B`, `E`, `G`, `v`, `Vp`, `Vs`, `zeta`, `A`
  - `units`:
    - `pressure_GPa`: GPa
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C33`: GPa
    - `C44`: GPa
    - `B`: GPa
    - `E`: GPa
    - `G`: GPa
    - `v`: 
    - `Vp`: km/s
    - `Vs`: km/s
    - `zeta`: 
    - `A`: 

Notes: All outputs must be produced by re‑running the GULP/REBO workflow; using pre‑computed numbers or external sources is a violation. The checker compares ground‑state values to the paper’s Table 1 with appropriate tolerances and verifies structural trends for the pressure‑dependent data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants_0GPa.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "C11",
          "C12",
          "C13",
          "C33",
          "C44"
        ],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C33": "GPa",
          "C44": "GPa"
        }
      },
      "description": "Five single-crystal elastic constants at 0 GPa from the re-optimised structure; compared to the paper’s ground‑state values with allowed tolerances."
    },
    {
      "file": "derived_properties_0GPa.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "B",
          "E",
          "G",
          "v",
          "Vp",
          "Vs",
          "zeta",
          "A"
        ],
        "units": {
          "B": "GPa",
          "E": "GPa",
          "G": "GPa",
          "v": "",
          "Vp": "km/s",
          "Vs": "km/s",
          "zeta": "",
          "A": ""
        }
      },
      "description": "Polycrystalline moduli and derived properties at 0 GPa, recomputed from the agent’s own elastic constants and density; the checker recomputes these quantities and compares them to paper‑reported values."
    },
    {
      "file": "pressure_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "C11",
          "C12",
          "C13",
          "C33",
          "C44",
          "B",
          "E",
          "G",
          "v",
          "Vp",
          "Vs",
          "zeta",
          "A"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C33": "GPa",
          "C44": "GPa",
          "B": "GPa",
          "E": "GPa",
          "G": "GPa",
          "v": "",
          "Vp": "km/s",
          "Vs": "km/s",
          "zeta": "",
          "A": ""
        }
      },
      "description": "Pressure‑dependent elastic constants and derived properties for 0–500 GPa; checked for monotonic trends and Born mechanical stability at every pressure."
    }
  ],
  "notes": "All outputs must be produced by re‑running the GULP/REBO workflow; using pre‑computed numbers or external sources is a violation. The checker compares ground‑state values to the paper’s Table 1 with appropriate tolerances and verifies structural trends for the pressure‑dependent data."
}
```

## How you are scored
A hidden verifier reads your output CSV files and scores each on a 0–1 scale. The ground‑state elastic constants at 0 GPa are checked for reasonableness within expected method‑dependent ranges. The derived properties at 0 GPa are recomputed from your own elastic constants and density using the standard Voigt–Reuss–Hill formulas; the checker ensures internal consistency. The pressure‑dependence file is audited for structural correctness: all elastic constants must increase monotonically with pressure, the Born mechanical stability conditions must be satisfied at every pressure, and the derived properties must follow the expected trends. Your final reward is a weighted combination of these stage scores; reporting a single number is not sufficient—you must provide the complete tables as specified.
