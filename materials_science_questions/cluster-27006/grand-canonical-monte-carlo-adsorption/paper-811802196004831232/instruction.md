# CO2 Solvation Pressure and Deformation Isotherms in Slit Carbon Pores

## Problem background
Microporous carbons (activated carbons, coals) expand or contract when used to sequester carbon dioxide at high pressures, which affects reservoir permeability and storage capacity. Understanding the microscopic mechanism of this adsorption-induced deformation is essential for safe geosequestration. The key quantity is the solvation pressure (adsorption stress) that adsorbed CO₂ exerts inside individual slit-shaped pores. This task reproduces the computational study that computes pore-resolved solvation pressure and then predicts macroscopic volumetric strain and total CO₂ adsorption isotherms for a specific carbide-derived activated carbon sample.

## Approach
The method is based on grand canonical Monte Carlo (GCMC) simulations of rigid linear CO₂ molecules in slit-shaped carbon pores. The intermolecular interactions follow the Nguyen force field, and the solid–fluid interaction uses the Steele 10‑4‑3 potential with standard carbon parameters (σₛₛ=0.34 nm, εₛₛ/k_b=28 K, ρₛ=114 nm⁻³, Δ=0.335 nm). Simulations run at 333 K across a wide range of pore widths and bulk pressures. From each adsorption isotherm, the grand potential per unit surface area is obtained by thermodynamic integration from an ideal-gas reference; the solvation pressure is then computed as the negative derivative of the grand potential with respect to pore width.

These microscopic solvation pressures are averaged over a pore‑size distribution (PSD) that characterizes the activated carbon, using a linear elastic model with bulk modulus K = 12 GPa. The macroscopic volumetric strain ε(p) is given by the surface-area-weighted average of the solvation pressure minus the external pressure, divided by the bulk modulus. The total CO₂ loading (cm³ STP per gram of carbon) is obtained by integrating the pore‑resolved adsorbed amounts over the PSD. The PSD is provided as a bundled CSV file. The workflow requires you to run all GCMC simulations, perform the thermodynamic integration, and compute the three output files listed below.

## Reproduction target
Compute, from GCMC simulations and the provided PSD, three quantities:

1.  **Solvation pressure** of CO₂ in individual slit carbon pores at 333 K and 27 MPa, for at least 15 effective pore widths spanning 0.2–2.0 nm, including the key widths 0.23, 0.31, 0.36, 0.54, 1.0, and 1.3 nm. Write to `solvation_pressure.csv`.
2.  **Macroscopic volumetric strain isotherm** ε(p) (dimensionless) for pressures 0.1–27 MPa, with at least 20 monotonically increasing points, using the PSD and bulk modulus K = 12 GPa. Write to `strain_isotherm.csv`.
3.  **Total CO₂ adsorption isotherm** (loading in cm³ STP/g) for pressures 0.1–27 MPa, obtained by integrating the pore‑resolved isotherms over the PSD. Write to `adsorption_isotherm.csv`.

All files must follow the output contract (columns, units, and ranges) specified in the Workflow steps and the Output contract section.

## Assets

- Pore size distribution of carbide-derived activated carbon
- GCMC simulation software: https://github.com/NASA-Planetary-Science/RASPA2
- CO2 Nguyen force field parameters

## Workflow steps

### Step 1: Run GCMC simulations for CO2 adsorption in slit carbon pores
- Role: process
- Action: Simulate CO2 adsorption in slit-shaped carbon pores with Steele 10‑4‑3 solid-fluid potential using the Nguyen force field at 333 K for effective pore widths covering 0.19 to 4.7 nm and pressures from 1e‑6 to 27 MPa. Produce arrays of adsorbed amount N(H,μ) (molecules per unit surface area) for each pore width.
- Evidence: `/app/outputs/gcmc_log.txt`

### Step 2: Compute solvation pressure from adsorption isotherms
- Role: scored (load-bearing)
- Action: Perform thermodynamic integration of the GCMC isotherms to obtain the grand potential per unit surface area Ωp(H,μ) using an ideal-gas reference state. Compute solvation pressure σs = −∂Ωp/∂H via numerical differentiation. Write a CSV with effective pore width and solvation pressure at a bulk pressure of 27 MPa.
- Output file: `/app/outputs/solvation_pressure.csv`
- Format: csv
- Contract: Columns: effective_pore_width_nm (float), solvation_pressure_GPa (float). Pore widths must cover at least 15 points from 0.2 to 2.0 nm, including the key widths 0.23, 0.31, 0.36, 0.54, 1.0, 1.3 nm.
- Scoring: scored by hidden verifier

### Step 3: Compute strain isotherm from solvation pressure and pore size distribution
- Role: scored
- Action: Using the provided PSD (psd.csv) and bulk modulus K=12 GPa, compute the average adsorption stress via surface‑area‑weighted averaging over the pore‑size distribution. Then compute the volumetric strain ε(p) = (1/K)[σ̅_s − p]. Write the strain isotherm for pressures from 0.1 to 27 MPa.
- Output file: `/app/outputs/strain_isotherm.csv`
- Format: csv
- Contract: Columns: pressure_MPa (float), volumetric_strain (float). At least 20 pressure points monotonically increasing from 0.1 to 27 MPa.
- Scoring: scored by hidden verifier

### Step 4: Compute total adsorption isotherm from pore-resolved isotherms and PSD
- Role: scored
- Action: Integrate the pore-specific adsorbed amounts N(H,μ) over the PSD (psd.csv) to obtain total adsorbed quantity per unit mass. Convert to cm³(STP)/g. Write the adsorption isotherm for pressures from 0.1 to 27 MPa.
- Output file: `/app/outputs/adsorption_isotherm.csv`
- Format: csv
- Contract: Columns: pressure_MPa (float), loading_cm3_g (float). Same pressure range as strain isotherm, at least 20 points.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/solvation_pressure.csv`
- `/app/outputs/strain_isotherm.csv`
- `/app/outputs/adsorption_isotherm.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### solvation_pressure.csv
- path: `/app/outputs/solvation_pressure.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Solvation pressure (adsorption stress) versus effective pore width at 333 K and 27 MPa. Scored at key pore widths against paper‑reported values with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `effective_pore_width_nm`, `solvation_pressure_GPa`
  - `units`:
    - `effective_pore_width_nm`: nm
    - `solvation_pressure_GPa`: GPa

### strain_isotherm.csv
- path: `/app/outputs/strain_isotherm.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Macroscopic volumetric strain isotherm from 0.1 to 27 MPa. Scored at 2.9 MPa and 27 MPa against paper‑reported expansion with absolute tolerances; monotonic increase is also checked.
- schema:
  - `type`: table
  - `required_columns`: `pressure_MPa`, `volumetric_strain`
  - `units`:
    - `pressure_MPa`: MPa
    - `volumetric_strain`: dimensionless

### adsorption_isotherm.csv
- path: `/app/outputs/adsorption_isotherm.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Total CO2 adsorption isotherm in cm³(STP)/g from 0.1 to 27 MPa. Scored at 2.9 MPa and 27 MPa against paper‑reported loading with relative tolerances.
- schema:
  - `type`: table
  - `required_columns`: `pressure_MPa`, `loading_cm3_g`
  - `units`:
    - `pressure_MPa`: MPa
    - `loading_cm3_g`: cm3(STP)/g

Notes: The workflow uses a bundled pore size distribution (digitized from the original paper) to bypass the model‑fitting step, focusing reproduction on the GCMC simulation pipeline and the resulting solvation pressure and macroscopic isotherms. The macroscopic strain is computed assuming a linear stress–strain relation with bulk modulus K=12 GPa.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "solvation_pressure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "effective_pore_width_nm",
          "solvation_pressure_GPa"
        ],
        "units": {
          "effective_pore_width_nm": "nm",
          "solvation_pressure_GPa": "GPa"
        }
      },
      "description": "Solvation pressure (adsorption stress) versus effective pore width at 333 K and 27 MPa. Scored at key pore widths against paper‑reported values with tolerances."
    },
    {
      "file": "strain_isotherm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_MPa",
          "volumetric_strain"
        ],
        "units": {
          "pressure_MPa": "MPa",
          "volumetric_strain": "dimensionless"
        }
      },
      "description": "Macroscopic volumetric strain isotherm from 0.1 to 27 MPa. Scored at 2.9 MPa and 27 MPa against paper‑reported expansion with absolute tolerances; monotonic increase is also checked."
    },
    {
      "file": "adsorption_isotherm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_MPa",
          "loading_cm3_g"
        ],
        "units": {
          "pressure_MPa": "MPa",
          "loading_cm3_g": "cm3(STP)/g"
        }
      },
      "description": "Total CO2 adsorption isotherm in cm³(STP)/g from 0.1 to 27 MPa. Scored at 2.9 MPa and 27 MPa against paper‑reported loading with relative tolerances."
    }
  ],
  "notes": "The workflow uses a bundled pore size distribution (digitized from the original paper) to bypass the model‑fitting step, focusing reproduction on the GCMC simulation pipeline and the resulting solvation pressure and macroscopic isotherms. The macroscopic strain is computed assuming a linear stress–strain relation with bulk modulus K=12 GPa."
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier. For each of the three CSV files, the verifier independently checks your computed values against the corresponding reference values from the source paper, using predetermined tolerances that account for legitimate differences due to simulation code, random seeds, and implementation details.

- **solvation_pressure.csv** is scored on the magnitude and trend of solvation pressure at key pore widths; the verifier checks features such as the high positive value in the smallest pores, the zero crossing around 0.31 nm, and the secondary maximum near 0.54 nm.
- **strain_isotherm.csv** is scored against the paper’s reported expansion at selected pressures (including 2.9 MPa and 27 MPa) and must show a monotonically increasing strain with pressure.
- **adsorption_isotherm.csv** is scored against the paper’s reported total loading at the same pressure points.

The scoring policy is **threshold‑or‑better**: if your computed quantity meets or exceeds the paper’s result within tolerance, you receive full credit for that artifact; you are never penalized for a result that is better than the paper. The verifier also checks that each file has the required columns and data points. The final reward is a weighted sum of the scores from the three artifacts, with the solvation pressure and strain isotherm carrying the largest weight.
