# Compute Sound Velocities and Debye Temperature from Elastic Data

## Problem background
Cubic perovskite-type compounds are studied for their mechanical and thermal properties, particularly as candidates for thermal barrier coatings. An important aspect of such studies is the estimation of polycrystalline thermal parameters — sound velocities, Debye temperature, and minimum thermal conductivity — from the material's elastic moduli and structural parameters. This task focuses on computing these derived thermal properties for a series of related compounds, using the provided bulk modulus, shear modulus, density, lattice constant, and mean atomic mass.

## Approach
The calculation proceeds in several stages grounded in solid-state physics. From the bulk modulus B, shear modulus G, and density ρ, the longitudinal sound velocity v_l and transverse sound velocity v_t are obtained. These are combined into an average sound velocity v_m via the averaging formula that weights the inverse cubes of the two velocities. Using the average sound velocity and the volume per atom (derived from the lattice constant a₀ and the number of atoms per unit cell), the Debye temperature θ_D is computed. An analogous expression provides the minimum thermal conductivity k_min, which relates k_B, the average sound velocity, and the mean atomic mass and density. All necessary input data for the four compounds are supplied in a single CSV file; the task is to implement these formulas, compute the six output quantities for each compound, and write the results in a structured CSV.

## Reproduction target
Load the provided input file RBRh3_elastic_data.csv, which contains columns for compound identifier, bulk modulus B (GPa), shear modulus G (GPa), density ρ (g/cm³), lattice constant a₀ (Å), and mean atomic mass M_m (g/mol) for the four compounds ScBRh3, YBRh3, LuBRh3, and LaBRh3. For each compound, compute the longitudinal sound velocity v_l (m/s), transverse sound velocity v_t (m/s), average sound velocity v_m (m/s), Debye temperature θ_D (K), and minimum thermal conductivity k_min (W/m/K). Produce a CSV file thermal_properties.csv with the header compound,v_l,v_t,v_m,theta_D,k_min, containing one row per compound in the order ScBRh3, YBRh3, LuBRh3, LaBRh3, with numeric values expressed as floating-point numbers.

## Assets

- RBRh3_elastic_data.csv

## Workflow steps

### Step 1: Compute thermal properties
- Role: scored (load-bearing)
- Action: Load the bundled CSV RBRh3_elastic_data.csv containing compound, B (GPa), G (GPa), density (g/cm³), a0 (Å), and Mm (g/mol). For each compound, compute longitudinal sound velocity v_l = sqrt((3B+4G)/(3ρ)), transverse sound velocity v_t = sqrt(G/ρ), average sound velocity v_m = [(1/3)(2/v_t^3 + 1/v_l^3)]^{-1/3}, Debye temperature θ_D = (h/kB)*(3/(4π*Va))^{1/3}*v_m with Va = a0^3/5 (h=6.62607e-34 J·s, kB=1.38065e-23 J/K), and minimum thermal conductivity k_min = kB*v_m*(Mm/ρ)^{-2/3}. Ensure unit conversions (B, G in GPa; density in g/cm³; a0 in Å; Mm in g/mol). Write the results to thermal_properties.csv with columns: compound, v_l (m/s), v_t (m/s), v_m (m/s), theta_D (K), k_min (W/m/K). Rows in order: ScBRh3, YBRh3, LuBRh3, LaBRh3.
- Output file: `/app/outputs/thermal_properties.csv`
- Format: csv
- Contract: CSV with header compound, v_l, v_t, v_m, theta_D, k_min. All numeric columns as floats in specified units.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_properties.csv
- path: `/app/outputs/thermal_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV with computed sound velocities, Debye temperature, and minimum thermal conductivity for each compound. Checker compares theta_D and k_min to hidden reference values within tolerances and verifies the decreasing trend in compound order.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `v_l`, `v_t`, `v_m`, `theta_D`, `k_min`
  - `units`:
    - `v_l`: m/s
    - `v_t`: m/s
    - `v_m`: m/s
    - `theta_D`: K
    - `k_min`: W/m/K

Notes: The input data is extracted from the paper's DFT results; the agent only performs the final property calculation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "v_l",
          "v_t",
          "v_m",
          "theta_D",
          "k_min"
        ],
        "units": {
          "v_l": "m/s",
          "v_t": "m/s",
          "v_m": "m/s",
          "theta_D": "K",
          "k_min": "W/m/K"
        }
      },
      "description": "CSV with computed sound velocities, Debye temperature, and minimum thermal conductivity for each compound. Checker compares theta_D and k_min to hidden reference values within tolerances and verifies the decreasing trend in compound order."
    }
  ],
  "notes": "The input data is extracted from the paper's DFT results; the agent only performs the final property calculation."
}
```

## How you are scored
A hidden verifier reads your thermal_properties.csv and independently checks the correctness of the computed Debye temperatures and minimum thermal conductivities. The verifier compares your values for each compound to reference values and also examines whether the results exhibit a physically consistent monotonic trend across the compound series. All compounds contribute equally to the score; the final reward is a single number between 0 and 1. The specific tolerances and reference values are kept hidden — you must compute the quantities honestly from the input data and the standard formulas.
