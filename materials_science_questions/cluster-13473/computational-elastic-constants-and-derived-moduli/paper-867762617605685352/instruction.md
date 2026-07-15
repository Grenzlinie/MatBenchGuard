## Problem background

Fused silica glass exhibits unusual plastic deformation characteristics: under sufficiently high volumetric compression it undergoes an irreversible densification transition, resulting in permanent density increase upon unloading. When subjected to combined pressure-shear loading, the glass evolves toward a critical state of constant volume, with a strongly non-convex critical-state line in the pressure–shear-stress plane. Understanding this behaviour is key to modelling deformation patterning and failure in amorphous silica.

## Approach

Molecular dynamics (MD) simulations are performed for a representative volume element of amorphous SiO₂ containing 1536 atoms at 300 K, using the open-source LAMMPS code and a modified BKS interatomic potential. The workflow is:

1. **Sample generation:** An amorphous starting configuration is prepared by melt-quench: β‑cristobalite is melted at 5000 K and cooled to 300 K over 470 ps in the NVT ensemble, yielding the initial amorphous structure.
2. **Volumetric loading–unloading:** The sample is compressed to a series of maximum pressures (spanning below and above the expected densification threshold) and then unloaded back to ambient conditions. Pressure and normalized volume are recorded throughout each cycle.
3. **Pressure‑shear and critical state:** The sample is first over‑consolidated by compressing to a high pressure and then unloading to a target confining pressure. Shear deformation is applied at constant pressure until a steady plateau in shear stress is reached. The confining pressure and the plateau (critical) shear stress are recorded.

The resulting pressure–volume data and (confining pressure, critical shear stress) data form the basis for extracting the irreversible densification threshold and the two‑branch (tensile linear, compressive power‑law) critical‑state line.

## Reproduction target

Produce the raw MD data required to determine two headline quantities:
1. The irreversible densification threshold pressure—identified as the lowest maximum pressure at which unloading leaves a non‑negligible residual volume change.
2. The critical‑state line parameters—the coefficients of the linear tensile branch and the power‑law compressive branch that describe the relation between confining pressure and critical shear stress.

The verifier will independently process your submitted CSV files, compute the threshold and fit the critical‑state line model, and compare against reference values. You do **not** need to report a single numerical answer; the verifier re‑derives all comparisons from your raw data.

## Assets

- **LAMMPS** – open‑source molecular dynamics code (https://lammps.sandia.gov/download.html).
- **Modified BKS interatomic potential parameters for SiO₂** – parameters (A, C, D, ρ) documented in Malavasi et al., *J. Non‑Cryst. Solids* 352, 285 (2006), Table 4. DOI: `10.1016/j.jnoncrysol.2005.11.022`.

## Workflow steps

### Step 1: Generate amorphous SiO₂ sample via melt-quench
- **Role:** process
- **Action:** Using LAMMPS and the modified BKS potential, create an initial amorphous SiO₂ configuration of 1536 atoms at 300 K. Start from a β‑cristobalite crystal, melt at 5000 K, and cool to 300 K over 470 ps in the NVT ensemble.
- **Evidence:** `/app/outputs/amorphous.lmp` (a LAMMPS data file or equivalent snapshot of the final simulation box)

### Step 2: Volumetric loading–unloading MD and densification threshold data
- **Role:** scored (load‑bearing)
- **Action:** Using the amorphous configuration from Step 1, perform volumetric compression–unloading cycles at 300 K. Choose at least 4 distinct maximum pressures between 0 and 15 GPa that bracket the densification transition. For each cycle, compress the sample isotropically to the chosen maximum pressure and then unload back to ambient pressure. Record pressure (in GPa) and the volume normalised to the initial (undeformed) value at every sampled point. Output one continuous record per cycle.
- **Output file:** `/app/outputs/volumetric_loading_unloading.csv`
- **Format:** csv
- **Contract:** Columns must be `cycle_id` (integer), `loading_phase` (string, either `"load"` or `"unload"`), `volume_norm` (float, dimensionless, normalised to initial volume), `pressure` (float, in GPa). Each row corresponds to one sampled state. A cycle must contain both load and unload phases.
- **Scoring:** scored by hidden verifier

### Step 3: Pressure‑shear MD and critical‑state line data
- **Role:** scored (load‑bearing)
- **Action:** Using the amorphous configuration from Step 1, for each of at least 6 confining pressures (covering both tensile and compressive regimes, e.g. from −1 GPa to +12 GPa) prepare the sample by first compressing to a pressure well above the confining value (e.g. 50 GPa) and then unloading to the target confining pressure. While holding the confining pressure constant, apply shear deformation until a steady plateau in shear stress is observed. Record the confining pressure (the constant pressure held during shear) and the plateau (critical) shear stress 𝑞c.
- **Output file:** `/app/outputs/critical_state_data.csv`
- **Format:** csv
- **Contract:** Columns must be `confining_pressure` (float, in GPa) and `critical_shear_stress_qc` (float, in GPa). Each row represents one confining‑pressure condition. At least 6 rows spanning both negative (tensile) and positive (compressive) pressures are required.
- **Scoring:** scored by hidden verifier

## Output files

All artefacts must be placed under `/app/outputs`:
- `amorphous.lmp` (process evidence)
- `volumetric_loading_unloading.csv` (scored)
- `critical_state_data.csv` (scored)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### volumetric_loading_unloading.csv
- path: `/app/outputs/volumetric_loading_unloading.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Volumetric loading-unloading data for multiple cycles. The verifier recomputes the residual volume change after unloading, determines the densification threshold, and compares it to the hidden paper gold.
- schema:
  - `type`: table
  - `required_columns`: `cycle_id`, `loading_phase`, `volume_norm`, `pressure`
  - `units`:
    - `cycle_id`: integer
    - `loading_phase`: string (load/unload)
    - `volume_norm`: dimensionless
    - `pressure`: GPa

### critical_state_data.csv
- path: `/app/outputs/critical_state_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Critical state data points. The verifier fits a two-branch model (linear tensile, power-law compressive) to these points, extracts the critical-state line parameters, solves the rank-2 envelope equations for the relaxed critical-state line parameters (r, s, p_min, p_max), and compares all parameters against the hidden paper gold.
- schema:
  - `type`: table
  - `required_columns`: `confining_pressure`, `critical_shear_stress_qc`
  - `units`:
    - `confining_pressure`: GPa
    - `critical_shear_stress_qc`: GPa

Notes: All files must be placed under /app/outputs. The verifier works exclusively from the submitted artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "volumetric_loading_unloading.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "cycle_id",
          "loading_phase",
          "volume_norm",
          "pressure"
        ],
        "units": {
          "cycle_id": "integer",
          "loading_phase": "string (load/unload)",
          "volume_norm": "dimensionless",
          "pressure": "GPa"
        }
      },
      "description": "Volumetric loading-unloading data for multiple cycles. The verifier recomputes the residual volume change after unloading, determines the densification threshold, and compares it to the hidden paper gold."
    },
    {
      "file": "critical_state_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "confining_pressure",
          "critical_shear_stress_qc"
        ],
        "units": {
          "confining_pressure": "GPa",
          "critical_shear_stress_qc": "GPa"
        }
      },
      "description": "Critical state data points. The verifier fits a two-branch model (linear tensile, power-law compressive) to these points, extracts the critical-state line parameters, solves the rank-2 envelope equations for the relaxed critical-state line parameters (r, s, p_min, p_max), and compares all parameters against the hidden paper gold."
    }
  ],
  "notes": "All files must be placed under /app/outputs. The verifier works exclusively from the submitted artifacts."
}
```
