# SH-wave reflection and transmission at austenitic weld interface

## Problem background
Ultrasonic inspection of austenitic welds in pressure components is complicated by the columnar grain structure, which causes reflection, refraction, and scattering of conventional wave modes (longitudinal and shear-vertical waves). Shear horizontal (SH) waves have phase velocities that are much less sensitive to the propagation direction in such anisotropic structures. This task investigates the reflection and transmission behavior of SH-waves at the interface between an isotropic austenitic base metal and a transversely isotropic austenitic weld metal. The weld metal is modeled with its columnar grains parallel to the interface and its symmetry axis perpendicular to the interface. You will compute the reflection coefficient R and transmission coefficient T as functions of the incidence angle and evaluate under what conditions nearly total transmission occurs.

## Approach
You will implement a plane-wave SH-wave transmission model for a planar interface between two elastic half-spaces. The base metal is treated as isotropic; the weld metal is transversely isotropic with the symmetry axis normal to the interface. Using the elastic constants and densities provided in the assets, you will derive the effective SH-wave impedances for both media as functions of incidence angle. By enforcing continuity of stress and displacement across the interface, you can obtain expressions for the reflection coefficient R and transmission coefficient T. You will compute these coefficients for incidence angles from 0° to 90° in 1° increments and write the results to a CSV file. No external software beyond a standard scientific Python environment is required.

## Reproduction target
Produce a CSV file `sh_wave_transmission.csv` containing the incidence angle (angle_deg) from 0° to 90° in 1° steps, and the corresponding reflection coefficient R and transmission coefficient T for an SH-wave at the interface between the specified isotropic base metal and transversely isotropic weld metal. The checker will evaluate the angular dependence and magnitude of R and T against the physical behavior predicted by the model.

## Assets

- Elastic constants and densities for austenitic base metal and weld metal

## Workflow steps

### Step 1: Compute SH-wave reflection and transmission coefficients
- Role: scored (load-bearing)
- Action: Using the provided material properties for austenitic base metal (isotropic) and austenitic weld metal (transversely isotropic with symmetry axis perpendicular to the interface), compute the SH-wave impedances for the two media. Apply the boundary conditions for an SH-wave at a planar interface between two elastic half-spaces to derive the reflection coefficient R and transmission coefficient T as functions of the incidence angle. Compute R and T for incidence angles from 0° to 90° in increments of 1° and write the results to a CSV.
- Output file: `/app/outputs/sh_wave_transmission.csv`
- Format: csv
- Contract: angle_deg (float, 0 to 90), R (float, reflection coefficient), T (float, transmission coefficient)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sh_wave_transmission.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sh_wave_transmission.csv
- path: `/app/outputs/sh_wave_transmission.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed SH-wave reflection coefficient R and transmission coefficient T as functions of incidence angle. The checker will verify that for angles in [45°, 90°] R < 0.1 and T > 0.9.
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `R`, `T`
  - `units`:
    - `angle_deg`: degree
    - `R`: dimensionless
    - `T`: dimensionless

Notes: Only the weld interface calculation is included; the cladding interface computation is omitted per taskability scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sh_wave_transmission.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "R",
          "T"
        ],
        "units": {
          "angle_deg": "degree",
          "R": "dimensionless",
          "T": "dimensionless"
        }
      },
      "description": "Computed SH-wave reflection coefficient R and transmission coefficient T as functions of incidence angle. The checker will verify that for angles in [45°, 90°] R < 0.1 and T > 0.9."
    }
  ],
  "notes": "Only the weld interface calculation is included; the cladding interface computation is omitted per taskability scope."
}
```

## How you are scored
A hidden verifier reads your `sh_wave_transmission.csv` and evaluates its correctness. It does not simply check whether you reported particular numbers; it may recompute derived quantities, compare your coefficients against hidden reference values, and verify that they satisfy expected physical relationships (such as trends, energy conservation, and magnitude ranges) for this material system. The verifier's score is a float between 0 and 1. Full credit requires that your computed R and T match the correct angular behavior within hidden tolerances. There is only one scored stage, so its score is your final reward.
