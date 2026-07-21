# Computation of Size-Dependent Shear Moduli in Amorphous Nano-Samples

## Problem background
Nano-sized amorphous solids, such as metallic glasses at sub-micron scales, often exhibit mechanical properties that differ from their bulk counterparts. This task investigates the system-size dependence of the shear modulus in free-standing cuboid samples of a binary glass. The goal is to quantify how the computed shear moduli vary with the sample's aspect ratio (width over height) when all boundaries except the two loading faces are free surfaces. The result reveals the magnitude and character of surface-induced softening.

## Approach
Amorphous glass samples are created from a binary mixture of 'small' and 'large' particles interacting through a modified Lennard-Jones potential with interaction lengths σₛₛ=1, σₗₗ=1.4, σₛₗ=1.18. Cuboid samples with a fixed height and a square cross‑section of varying edge length are prepared by quenching from the melt to zero temperature at zero pressure. The shear moduli μₓₓ and μₓᵧ are measured by clamping opposite faces (top/bottom for μₓₓ, opposite side walls for μₓᵧ) and applying an infinitesimal affine shear strain. Because the system is amorphous, particles must undergo additional non‑affine displacements to restore mechanical equilibrium. The exact shear modulus is therefore given by μ = (1/V)[∂²U/∂γ² − Ξ·H⁻¹·Ξ], where the first term is the Born contribution and the second, negative‑definite, term is the non‑affine correction computed from the Hessian H and the force‑strain coupling Ξ. The moduli are evaluated for at least three aspect ratios spanning roughly 3.5 down to 1, allowing the relative decrease to be quantified.

## Model and Methods

### Interparticle potential
All particles interact via a modified Lennard-Jones potential. For particles of types α, β ∈ {s,ℓ}:
U_{αβ}(r) = 4 ε [ (σ_{αβ}/r)^{12} - (σ_{αβ}/r)^6 ] + S_{αβ}(r),   for r < r_cut,
and U_{αβ}(r) = 0 for r ≥ r_cut.

The length parameters are:
σ_{ss} = 1.0,   σ_{ℓℓ} = 1.4,   σ_{sℓ} = 1.18.

Set the energy scale ε = 1.0 for all pairs (energy is measured in units of ε).
Use a cutoff radius r_cut = 2.5 σ_{αβ} and a shift function S_{αβ}(r) that makes the potential and its first derivative continuous at r_cut (e.g., a polynomial shift or the common truncated-and‑shifted Lennard‑Jones form).
All particles have mass m = 1.0.

### Binary composition
The system is a 50:50 (by number) mixture of small (s) and large (ℓ) particles. For a total of N particles, set N/2 of each type. (Small variations in composition are acceptable; the final moduli trends are robust.)

### Geometry and density
Use a target number density ρ = 1.2 (in units of σ_{ss}^{−3}). For a cuboid with dimensions Lx × Lx × Lz (all lengths in units of σ_{ss}), place N = round(ρ · Lx² · Lz) particles, maintaining the 50:50 mixture. All three directions use non‑periodic, free boundaries (i.e., the cuboid has free surfaces on all six faces, except where later clamped for loading). This is essential to create surface effects.

### Quenching protocol (gradient‑energy method)
1. Initialise particle positions (random or on a lattice) inside the box.
2. Equilibrate the melt at high temperature T = 1.0 and zero pressure P = 0 using a short NPT run (e.g., 10⁴ steps, timestep 0.005).
3. Quench to T = 0 by alternating (a) a few hundred conjugate‑gradient energy minimisation steps and (b) an isotropic box relaxation to maintain P = 0, until the potential energy converges and the mean squared force per particle is below 10⁻¹².
The result is an inherent (zero‑temperature, zero‑pressure) glass sample.

Prepare at least three samples with fixed height Lz ≈ 15 and square cross‑section edges Lx chosen to give aspect ratios Lx/Lz ≈ 3.5, 2.0, and 1.0 (for example, Lx = 50, 30, 15). The exact particle numbers follow from the density.

### Shear modulus calculation
For a given inherent configuration, compute the two shear moduli μ_{xz} and μ_{xy} using the exact amorphous‑solid expression:

μ = (1/V) [ B − Ξ·H⁻¹·Ξ ],

where V = Lx · Lx · Lz, and:
- Born term: B = ∂²U/∂γ²,
- Hessian: H_{ij} = ∂²U/∂r_i ∂r_j,
- Force‑strain coupling: Ξ_i = ∂²U/∂r_i ∂γ.

All derivatives are evaluated at the unstrained inherent configuration.

#### Strain application and boundary conditions
- For μ_{xz} (x‑z shear): apply an infinitesimal affine strain γ_{xz} via x → x + γ z, y → y, z → z. The top (z = z_max) and bottom (z = z_min) faces are **clamped**: particles within a thin layer of thickness ~σ near these faces are held fixed. All side faces are free.
- For μ_{xy} (x‑y shear): apply γ_{xy} via x → x + γ y, y → y, z → z. The two opposite side walls at x = x_min and x = x_max are clamped, while top, bottom and the other two sides are free.

#### Computation of H and Ξ
1. Build the 3N×3N Hessian matrix H numerically: displace each particle ±δ (δ ≈ 10⁻⁵) in x, y, z and compute finite differences of forces. Alternatively, use analytical second derivatives if available.
2. Compute the vector Ξ = ∂²U/∂r_i ∂γ. This mixed derivative can be obtained by applying the affine strain transformation with a small δγ (e.g., 10⁻⁵), measuring the induced forces, and taking the finite difference.
3. **Remove clamped degrees of freedom**: identify the coordinates of particles in the clamped layers. Set the corresponding rows and columns of H to zero, and set the corresponding entries of Ξ to zero. Then eliminate those rows and columns from the linear system. (Equivalently, keep only the free degrees of freedom.)
4. Handle zero modes: the reduced Hessian still contains translation zero modes. Project them out or fix three non‑collinear Cartesian coordinates of one particle to remove them before inversion.
5. Invert the reduced, non‑singular Hessian and compute C = Ξ'·H⁻¹·Ξ'.
6. Compute the Born term B = ∂²U/∂γ² by applying the affine strain alone (without relaxation) and numerically differentiating U(γ) twice with respect to γ.
7. The shear modulus is μ = (1/V)(B − C).

**Implementation note:** Since the Hessian is large, use sparse matrices or iterative solvers. The clamped‑face approach is crucial; without it the non‑affine correction would be ill‑defined.

### Expected trend
As the aspect ratio Lx/Lz decreases (sample becomes more cube‑like), both μ_{xz} and μ_{xy} should decrease monotonically. The relative decrease is expected to be substantial for μ_{xz} and moderate for μ_{xy}. The verifier will check that your computed moduli follow this trend and that the fractional decreases are within generous tolerances of the reference values from the original study.

## Reproduction target
Construct glassy cuboid samples of a binary Lennard‑Jones mixture at three or more aspect ratios Lx/Lz (approximately 3.5, 2, and 1) with free surfaces except for the clamped loading faces. For each sample, compute the shear moduli μ_{xz} and μ_{xy} using the full amorphous‑solid expression that includes the non‑affine correction. Report the edge length Lx, height Lz, aspect ratio, and both moduli in a CSV file. The core objective is to establish the system‑size trend: as the aspect ratio decreases, the moduli are expected to change by a substantial relative amount, and the change should be monotonic (each successive ratio should give a lower modulus). The exact magnitude of the change is not prescribed; the task is to compute it from the underlying physics.

## Assets

- LAMMPS: https://www.lammps.org/

## Workflow steps

### Step 1: Generate amorphous glass samples
- Role: process
- Action: Create glassy amorphous cuboid samples from a binary mixture of point particles interacting via the modified Lennard‑Jones potential described above. Use the prescribed density, composition, and protocol. Prepare cuboids with fixed height Lz≈15 and square cross‑sections with edges Lx chosen to achieve ratios Lx/Lz from about 3.5 to 1 (e.g., Lx=50, 30, 15). Quench from the melt to T=0 at zero pressure using the gradient‑energy method.
- Evidence: (no scored output; intermediate configurations are for your own use)

### Step 2: Compute size-dependent shear moduli
- Role: scored (load-bearing)
- Action: For each amorphous sample, impose strain by clamping specific faces: clamp top and bottom to measure μ_{xz}, clamp two opposite side walls to measure μ_{xy}. Compute the shear modulus from the exact expression μ = (1/V)[∂²U/∂γ² − Ξ·H⁻¹·Ξ] by evaluating the Born term and the non‑affine correction (via Hessian construction and inversion) as detailed in the Model and Methods section. Report the edge length Lx, height Lz, ratio Lx/Lz, and the computed μ_{xz} and μ_{xy} for at least three different aspect ratios covering the range from ~3.5 to 1.
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

Notes: Agent must produce at least three rows covering ratios from ~3.5 to 1. The checker will recompute the fractional decrease in μ_{xz} and μ_{xy} from the row with largest ratio to smallest and verify monotonic decrease.

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
A hidden verifier reads your shear_moduli.csv and independently checks your results. It will compute the fractional decrease of μₓₓ and μₓᵧ from the row with the largest aspect ratio to the row with the smallest, and verify that both moduli decrease monotonically with decreasing ratio. The verifier compares the observed fractional decreases against reference values derived from the original study (with generous tolerance margins to account for differences in implementation details, sample preparation, and numerical methods). Additional checks may assess the CSV format, column presence, and unit consistency. The final reward is a weighted combination of these validation scores, with the main weight on the fractional decreases for μₓₓ and μₓᵧ. Simply reporting the expected numbers without executing the actual computation will not pass the verifier.