# Computation of Size-Dependent Shear Moduli in Amorphous Nano-Samples

## Problem background
Nano-sized amorphous solids, such as metallic glasses at sub-micron scales, often exhibit mechanical properties that differ from their bulk counterparts. This task investigates the system-size dependence of the shear modulus in free-standing cuboid samples of a binary glass. The goal is to quantify how the computed shear moduli vary with the sample's aspect ratio (width over height) when all boundaries except the two loading faces are free surfaces. The result reveals the magnitude and character of surface-induced softening.

## Approach
Amorphous glass samples are created from a binary mixture of 'small' and 'large' particles interacting through a modified Lennard-Jones potential with interaction lengths σₛₛ=1, σₗₗ=1.4, σₛₗ=1.18. Cuboid samples with a fixed height and a square cross‑section of varying edge length are prepared by quenching from the melt to zero temperature at zero pressure. The shear moduli μₓₓ and μₓᵧ are measured by clamping opposite faces (top/bottom for μₓₓ, opposite side walls for μₓᵧ) and applying an infinitesimal affine shear strain. Because the system is amorphous, particles must undergo additional non‑affine displacements to restore mechanical equilibrium. The exact shear modulus is therefore given by μ = (1/V)[∂²U/∂γ² − Ξ·H⁻¹·Ξ], where the first term is the Born contribution and the second, negative‑definite, term is the non‑affine correction computed from the Hessian H and the force‑strain coupling Ξ. The moduli are evaluated for at least three aspect ratios spanning roughly 3.5 down to 1, allowing the relative decrease to be quantified.

## Reproduction target
Construct glassy cuboid samples of a binary Lennard‑Jones mixture at three or more aspect ratios Lx/Lz (approximately 3.5, 2, and 1) with free surfaces except for the clamped loading faces. For each sample, compute the shear moduli μₓₓ and μₓᵧ using the full amorphous‑solid expression that includes the non‑affine correction. Report the edge length Lx, height Lz, aspect ratio, and both moduli in a CSV file. The core objective is to establish the system‑size trend: as the aspect ratio decreases, the moduli are expected to change by a substantial relative amount, and the change should be monotonic (each successive ratio should give a lower modulus). The exact magnitude of the change is not prescribed; the task is to compute it from the underlying physics.

## Assets

- LAMMPS: https://www.lammps.org/

## Workflow steps

### Step 1: Generate amorphous glass samples
- Role: process
- Action: Create glassy amorphous cuboid samples from a binary mixture of point particles interacting via a modified Lennard-Jones potential with interaction lengths σ_ss=1, σ_ℓℓ=1.4, σ_sℓ=1.18. Prepare cuboids with fixed height Lz≈15 particles and square cross-sections with edges Lx varying to achieve ratios Lx/Lz from about 3.5 to 1 (e.g., Lx=50, 25, 15). Quench from the melt to T=0 at zero pressure using a gradient energy method.
- Evidence: `/app/outputs/amorphous_configs.npy`

### Step 2: Compute size-dependent shear moduli
- Role: scored (load-bearing)
- Action: For each amorphous sample, impose strain by clamping specific faces: clamp top and bottom to measure μ_xz, clamp two opposite side walls to measure μ_xy. Compute the shear modulus from the exact expression μ = (1/V)[∂²U/∂γ² − Ξ·H⁻¹·Ξ] by evaluating the Born term and the non-affine correction (via Hessian construction and inversion). Report the edge length Lx, height Lz, ratio Lx/Lz, and the computed μ_xz and μ_xy for at least three different aspect ratios covering the range from ~3.5 to 1.
- Output file: `/app/outputs/shear_moduli.csv`
- Format: csv
- Contract: Columns: Lx (int), Lz (int), ratio_Lx_Lz (float), mu_xz (float), mu_xy (float). Units: lengths in particle diameters, moduli in energy/volume.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/shear_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### shear_moduli.csv
- path: `/app/outputs/shear_moduli.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Table of shear moduli for each cuboid sample at different aspect ratios.
- schema:
  - `type`: table
  - `required_columns`: `Lx`, `Lz`, `ratio_Lx_Lz`, `mu_xz`, `mu_xy`
  - `units`:
    - `Lx`: particle diameters
    - `Lz`: particle diameters
    - `ratio_Lx_Lz`: dimensionless
    - `mu_xz`: energy/volume
    - `mu_xy`: energy/volume

Notes: Agent must produce at least three rows covering ratios from ~3.5 to 1. The checker will recompute the fractional decrease in μ_xz and μ_xy from the row with largest ratio to smallest and verify monotonic decrease.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "shear_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Lx",
          "Lz",
          "ratio_Lx_Lz",
          "mu_xz",
          "mu_xy"
        ],
        "units": {
          "Lx": "particle diameters",
          "Lz": "particle diameters",
          "ratio_Lx_Lz": "dimensionless",
          "mu_xz": "energy/volume",
          "mu_xy": "energy/volume"
        }
      },
      "description": "Table of shear moduli for each cuboid sample at different aspect ratios."
    }
  ],
  "notes": "Agent must produce at least three rows covering ratios from ~3.5 to 1. The checker will recompute the fractional decrease in μ_xz and μ_xy from the row with largest ratio to smallest and verify monotonic decrease."
}
```

## How you are scored
A hidden verifier reads your shearmoduli.csv and independently checks your results. It will compute the fractional decrease of μₓₓ and μₓᵧ from the row with the largest aspect ratio to the row with the smallest, and verify that both moduli decrease monotonically with decreasing ratio. The verifier compares the observed fractional decreases against reference values derived from the original study (with generous tolerance margins to account for differences in implementation details, sample preparation, and numerical methods). Additional checks may assess the CSV format, column presence, and unit consistency. The final reward is a weighted combination of these validation scores, with the main weight on the fractional decreases for μₓₓ and μₓᵧ. Simply reporting the expected numbers without executing the actual computation will not pass the verifier.
