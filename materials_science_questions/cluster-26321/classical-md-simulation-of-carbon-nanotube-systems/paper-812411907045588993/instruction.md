# Hydrogen Physisorption in Chemically Modified Single-Wall Carbon Nanotubes

## Problem background
Hydrogen storage in carbon nanotubes is a critical challenge for renewable energy technologies. This task computationally investigates how surface chemistry—specifically chemisorbed atomic hydrogen and oxidative cavity formation—alters the physisorption capacity of molecular hydrogen (H2) in matrices of single-wall carbon nanotubes (SWNTs). The goal is to quantify the adsorbed H2 density as a function of surface modifications and to compare the storage performance of clean, hydrogenated, and oxidized nanotube systems under practical temperature and pressure conditions.

## Approach
The workflow combines structure relaxation with grand-canonical Monte Carlo (GCMC) simulations. Atomic geometries of clean, hydrogenated, and oxidized SWNTs are first relaxed to their equilibrium configurations at T = 0 K. The relaxed tubes are then assembled into square-lattice matrices with a fixed intertube wall-to-wall distance D = 7 Å. GCMC simulations are performed to compute H2 adsorption: first, a free-gas calibration determines the chemical potential versus density/pressure relationship; then production runs are carried out at specified temperatures and pressures. Intermolecular interactions are modeled with Lennard-Jones potentials: standard C–C and H2–H2 parameters are taken from public literature, and a specialized H–H2 interaction is implemented as a generalized Lennard-Jones form (parameterized as given in the assets). The results are aggregated into an output JSON containing the coverage scan (density versus chemisorbed hydrogen coverage) and the full adsorption isotherms (gravimetric and volumetric capacities) for the relevant tube types and conditions.

## Reproduction target
Compute and report the following quantities, all obtained from GCMC simulations using the Lennard-Jones potentials and the derived H–H2 interaction:

- **Coverage scan:** For (15,0) and (6,6) SWNTs at T = 293 K, P = 10 MPa, D = 7 Å, compute the average adsorbed H2 density ⟨ρ⟩ (in Å⁻³) for fractional coverages of chemisorbed atomic hydrogen c_H = 0.0, 0.1, 0.2, 0.3, 0.4, 0.5.

- **Isotherms, clean (15,0):** For the clean (15,0) nanotube, compute gravimetric capacity (wt%) and volumetric capacity (kg/m³) over a pressure range from 0 to 40 MPa at T = 77, 150, 293 K.

- **Isotherms, hydrogenated (15,0):** For the (15,0) nanotube with c_H = 0.1, compute gravimetric and volumetric capacities over the same (P,T) range.

- **Isotherms, oxidized (6,6):** For the (6,6) nanotube with a ~40% surface oxidation cavity (H-saturated dangling bonds), compute gravimetric and volumetric capacities over the same (P,T) range.

All results must be written to `/app/outputs/adsorption_results.json` following the output contract.

## Assets

- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://lammps.sandia.gov
- Lennard-Jones parameters for C, H2, and cross-interactions (Stan et al. 2000): 10.1103/PhysRevB.62.2173
- Effective H-H2 interaction potential (generalized Lennard-Jones, Eq. 1 of paper)

## Workflow steps

### Step 1: Derive effective H-H2 interaction potential
- Role: process
- Action: Implement the generalized Lennard-Jones potential for the H-H2 interaction using the parameters provided in the task instruction (ε=7.2435 K and the specified coefficients in Eq. 1). The potential must be usable in subsequent GCMC simulations.
- Evidence: none

### Step 2: Relax clean SWNT structures
- Role: process
- Action: Using a structure relaxation method (tight-binding molecular dynamics, density-functional based tight-binding, or classical force field minimization), relax the atomic geometries of (15,0) and (6,6) single-wall carbon nanotubes at T=0 K. Output the final atomic coordinates for each nanotube.
- Evidence: `/app/outputs/clean_geometries_15_0.xyz and clean_geometries_6_6.xyz`

### Step 3: Generate and relax hydrogenated SWNTs
- Role: process
- Action: For each nanotube chirality ((15,0) and (6,6)), place H atoms on the outer surface to achieve fractional coverages c_H = 0.0, 0.1, 0.2, 0.3, 0.4, 0.5. Relax each configuration at T=0 K using the same relaxation method as in Step 2. Save the relaxed coordinates for all coverages.
- Evidence: `/app/outputs/ directory containing relaxed structures for each coverage and tube`

### Step 4: Generate and relax oxidized SWNT
- Role: process
- Action: For the (6,6) nanotube, remove approximately 19 carbon atoms from the sidewall to create an ellipsoidal cavity (~40% surface oxidation) and saturate the dangling bonds with H atoms. Relax the structure at T=0 K and save the relaxed atomic geometry.
- Evidence: `/app/outputs/oxidized_geometry_6_6.xyz`

### Step 5: Build matrices and calibrate free-gas GCMC
- Role: process
- Action: For each relaxed nanotube structure, build a square-lattice supercell with the tube axis along z and an intertube wall-to-wall distance D=7 Å. Run GCMC simulations of pure H2 gas in a periodic box at T=77, 150, 293 K to determine the relation between chemical potential μ and density (or pressure), which will be used to set μ for the desired pressures in adsorption runs.
- Evidence: `/app/outputs/free_gas_calibration.json`

### Step 6: Run GCMC adsorption simulations and collect results
- Role: scored (load-bearing)
- Action: For all prepared matrices (clean (15,0) and (6,6); hydrogenated (15,0) and (6,6) at each coverage; oxidized (6,6)), run GCMC adsorption simulations using the Lennard-Jones parameters for C, H2, and the effective H-H2 potential. Coverage scan: T=293 K, P=10 MPa, compute average H2 density ⟨ρ⟩ for each c_H. Isotherms: for clean (15,0), hydrogenated (15,0) at c_H=0.1, and oxidized (6,6), run GCMC at T=77, 150, 293 K over a pressure range from 0 to 40 MPa, computing gravimetric capacity (wt%) and volumetric capacity (kg/m³). Aggregate all results into a single JSON file.
- Output file: `/app/outputs/adsorption_results.json`
- Format: json
- Contract: JSON object with keys: coverage_scan (array of {tube, coverage, density}); isotherms_clean (array of {tube, temperature, pressure, gravimetric_capacity, volumetric_capacity}); isotherms_hydrogenated (same shape, coverage=0.1); isotherms_oxidized (tube '6,6'). Density in Å^-3, gravimetric in wt%, volumetric in kg/m^3, pressure in MPa.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_results.json
- path: `/app/outputs/adsorption_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated H2 adsorption simulation results for all chemically modified SWNT matrices.
- schema:
  - `type`: object
  - `required`: `coverage_scan`, `isotherms_clean`, `isotherms_hydrogenated`, `isotherms_oxidized`
  - `properties`:
    - `coverage_scan`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `tube`, `coverage`, `density`
        - `properties`:
          - `tube`:
            - `type`: string
            - `enum`: `15,0`, `6,6`
          - `coverage`:
            - `type`: number
            - `minimum`: 0.0
            - `maximum`: 0.5
          - `density`:
            - `type`: number
            - `units`: angstrom^-3
    - `isotherms_clean`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `tube`, `temperature`, `pressure`, `gravimetric_capacity`, `volumetric_capacity`
        - `properties`:
          - `tube`:
            - `type`: string
            - `enum`: `15,0`
          - `temperature`:
            - `type`: number
            - `enum`: `77`, `150`, `293`
          - `pressure`:
            - `type`: number
            - `minimum`: 0.0
            - `maximum`: 40.0
            - `units`: MPa
          - `gravimetric_capacity`:
            - `type`: number
            - `units`: wt%
          - `volumetric_capacity`:
            - `type`: number
            - `units`: kg/m^3
    - `isotherms_hydrogenated`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `tube`, `coverage`, `temperature`, `pressure`, `gravimetric_capacity`, `volumetric_capacity`
        - `properties`:
          - `tube`:
            - `type`: string
            - `enum`: `15,0`
          - `coverage`:
            - `type`: number
            - `const`: 0.1
          - `temperature`:
            - `type`: number
            - `enum`: `77`, `150`, `293`
          - `pressure`:
            - `type`: number
            - `minimum`: 0.0
            - `maximum`: 40.0
            - `units`: MPa
          - `gravimetric_capacity`:
            - `type`: number
            - `units`: wt%
          - `volumetric_capacity`:
            - `type`: number
            - `units`: kg/m^3
    - `isotherms_oxidized`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `tube`, `temperature`, `pressure`, `gravimetric_capacity`, `volumetric_capacity`
        - `properties`:
          - `tube`:
            - `type`: string
            - `enum`: `6,6`
          - `temperature`:
            - `type`: number
            - `enum`: `77`, `150`, `293`
          - `pressure`:
            - `type`: number
            - `minimum`: 0.0
            - `maximum`: 40.0
            - `units`: MPa
          - `gravimetric_capacity`:
            - `type`: number
            - `units`: wt%
          - `volumetric_capacity`:
            - `type`: number
            - `units`: kg/m^3

Notes: All capacity values must be positive and densities within physically reasonable ranges. The file must contain exactly the specified keys and arrays.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "coverage_scan",
          "isotherms_clean",
          "isotherms_hydrogenated",
          "isotherms_oxidized"
        ],
        "properties": {
          "coverage_scan": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "tube",
                "coverage",
                "density"
              ],
              "properties": {
                "tube": {
                  "type": "string",
                  "enum": [
                    "15,0",
                    "6,6"
                  ]
                },
                "coverage": {
                  "type": "number",
                  "minimum": 0.0,
                  "maximum": 0.5
                },
                "density": {
                  "type": "number",
                  "units": "angstrom^-3"
                }
              }
            }
          },
          "isotherms_clean": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "tube",
                "temperature",
                "pressure",
                "gravimetric_capacity",
                "volumetric_capacity"
              ],
              "properties": {
                "tube": {
                  "type": "string",
                  "enum": [
                    "15,0"
                  ]
                },
                "temperature": {
                  "type": "number",
                  "enum": [
                    77,
                    150,
                    293
                  ]
                },
                "pressure": {
                  "type": "number",
                  "minimum": 0.0,
                  "maximum": 40.0,
                  "units": "MPa"
                },
                "gravimetric_capacity": {
                  "type": "number",
                  "units": "wt%"
                },
                "volumetric_capacity": {
                  "type": "number",
                  "units": "kg/m^3"
                }
              }
            }
          },
          "isotherms_hydrogenated": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "tube",
                "coverage",
                "temperature",
                "pressure",
                "gravimetric_capacity",
                "volumetric_capacity"
              ],
              "properties": {
                "tube": {
                  "type": "string",
                  "enum": [
                    "15,0"
                  ]
                },
                "coverage": {
                  "type": "number",
                  "const": 0.1
                },
                "temperature": {
                  "type": "number",
                  "enum": [
                    77,
                    150,
                    293
                  ]
                },
                "pressure": {
                  "type": "number",
                  "minimum": 0.0,
                  "maximum": 40.0,
                  "units": "MPa"
                },
                "gravimetric_capacity": {
                  "type": "number",
                  "units": "wt%"
                },
                "volumetric_capacity": {
                  "type": "number",
                  "units": "kg/m^3"
                }
              }
            }
          },
          "isotherms_oxidized": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "tube",
                "temperature",
                "pressure",
                "gravimetric_capacity",
                "volumetric_capacity"
              ],
              "properties": {
                "tube": {
                  "type": "string",
                  "enum": [
                    "6,6"
                  ]
                },
                "temperature": {
                  "type": "number",
                  "enum": [
                    77,
                    150,
                    293
                  ]
                },
                "pressure": {
                  "type": "number",
                  "minimum": 0.0,
                  "maximum": 40.0,
                  "units": "MPa"
                },
                "gravimetric_capacity": {
                  "type": "number",
                  "units": "wt%"
                },
                "volumetric_capacity": {
                  "type": "number",
                  "units": "kg/m^3"
                }
              }
            }
          }
        }
      },
      "description": "Aggregated H2 adsorption simulation results for all chemically modified SWNT matrices."
    }
  ],
  "notes": "All capacity values must be positive and densities within physically reasonable ranges. The file must contain exactly the specified keys and arrays."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads `/app/outputs/adsorption_results.json` and performs two types of checks:

1. **Quantitative comparison:** Your computed densities and capacities are compared against hidden reference values derived from the paper’s reported data. The comparison uses appropriate tolerances that account for legitimate run-to-run and implementation differences.

2. **Structural consistency:** The verifier also examines whether your results obey physically expected relationships among the different tube types, coverages, and thermodynamic conditions (e.g., how the adsorption changes with coverage and between clean and chemically modified matrices).

The final reward is a weighted sum over the different sections of the output file. Reporting numbers is not enough—the verifier checks that your data follow the correct trends and lie within the allowed tolerance bands.
