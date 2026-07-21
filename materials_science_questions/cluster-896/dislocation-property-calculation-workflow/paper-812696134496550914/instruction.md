# Reproduce Homogeneous Dislocation Nucleation in 2D Square Crystal using Landau Energy

## Problem background
Crystalline solids undergo plastic deformation through the nucleation and motion of dislocations. At micro- and nano-scales, homogeneous dislocation nucleation can take place in initially defect-free crystals under applied shear. A Landau-type nonlinear elasticity model that incorporates global lattice invariance and an infinitely periodic energy landscape provides a route to capturing such nucleation without phenomenological rules. In this model, loss of strong ellipticity of the elastic energy signals the onset of instability leading to collective dislocation formation on slip planes. The task is to determine, for a 2D square crystal described by a polynomial Landau energy under simple shear, the critical shear at which strong ellipticity is lost and the accompanying collective nucleation pattern with the orientations of the associated instability modes.

## Approach
The method employs a strain energy density φ(C) for a 2D square crystal built from a volumetric part φ_v(det C) = μ/2 (det C − 1)² and an isochoric part φ_d(C̃) = β Ψ₁(C̃) + Ψ₂(C̃) with β = −1/4, where Ψ₁ and Ψ₂ are polynomials of the hexagon invariants I₁,I₂,I₃ defined in terms of the reduced metric C̃. A Lagrange reduction maps any right Cauchy–Green tensor C to its unique reduced form C̃ inside the fundamental domain using integer matrix transformations, guaranteeing that the energy respects the infinite lattice symmetry.

Two complementary computations are performed. First, a linear stability analysis constructs the Eulerian acoustic tensor for the homogeneous simple shear deformation F_A = I + α (e₁⊗e₂). The smallest α at which the acoustic tensor determinant vanishes identifies the critical shear and yields the wave vector ζ and the eigenvector η for each instability mode. Second, a finite element simulation discretizes a square domain, applies hard‑device boundary conditions corresponding to the same simple shear for a sequence of α values, and minimizes the total elastic energy via L‑BFGS. The Cauchy stress recorded as a function of α produces the stress–strain curve and captures any stress drop associated with dislocation nucleation. The two analyses together provide the critical shear and the dominant instability orientations.

## Reproduction target
Produce a JSON file, results.json, containing the following fields:

- alpha_c_stability: the minimum shear α at which the acoustic tensor’s determinant first becomes zero during the linear stability analysis.
- alpha_c_simulation: the shear α at which a sharp drop in Cauchy stress occurs in the finite element simulation stress–strain curve (e.g., the location of peak stress).
- stability_modes: an array of two objects, each with zeta_angle_deg (the angle in degrees of the unit wave vector ζ that makes the acoustic tensor singular) and eta_angle_deg (the angle in degrees of the corresponding zero eigenvector η, which represents the amplitude/displacement direction of the instability mode). The two modes should be the ones near the loading direction and near the perpendicular direction, respectively.

The finite element simulation should also write a supporting evidence file stress_strain.csv with columns alpha and cauchy_stress, documenting the simulated stress–strain curve. These outputs together verify the connection between loss of strong ellipticity and collective dislocation nucleation.

## Assets

- Python 3: https://www.python.org/
- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Implement strain energy density and Lagrange reduction
- Role: process
- Action: Implement the polynomial strain energy density φ(C) for a 2D square crystal, consisting of volumetric part φ_v(s)=μ/2 (s-1)^2 with s=det C, μ=1, and isochoric part φ_d(C̃)=β Ψ1(C̃)+Ψ2(C̃) with β=-1/4 and the hexagon invariants I1,I2,I3 defined in the model. Implement the Lagrange reduction to map any right Cauchy–Green tensor C to its unique reduced form C̃ inside the fundamental domain, using integer matrix transformations. This provides the energy function and reduction routine used in all subsequent computations.
- Evidence: none

### Step 2: Finite element simulation of simple shear
- Role: process
- Action: Discretize a 2D square domain (e.g., 500x500 elements) with bilinear finite elements. Apply simple shear hard-device boundary conditions F_A = I + α (e1⊗e2) for a sequence of α from 0 to above the expected critical value. Minimize total elastic energy W = ∫ φ dV using L-BFGS for each α, starting from the homogeneous deformation. Record the resulting Cauchy stress (e.g., the relevant shear component or von Mises stress) for each α. Output the stress-strain data as evidence.
- Evidence: `/app/outputs/stress_strain.csv`

### Step 3: Linear stability analysis and compilation of results
- Role: scored (load-bearing)
- Action: Perform linear stability analysis for the simple shear deformation: construct the acoustic tensor Q(ζ) for a grid of α and unit wave vectors ζ=(cosξ, sinξ). Identify the minimum α where det Q(ζ)=0 for some ξ – this is α_c_stability – and record the corresponding ζ and the zero eigenvector η (amplitude vector) for the two instability modes (one near loading direction, one near perpendicular). From the stress-strain data in stress_strain.csv, determine the shear α_c_simulation where a sharp stress drop occurs (e.g., location of peak stress). Output the combined results in results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"alpha_c_stability": float, "alpha_c_simulation": float, "stability_modes": [{"zeta_angle_deg": float, "eta_angle_deg": float}, {"zeta_angle_deg": float, "eta_angle_deg": float}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Combined critical shear values from linear stability analysis and finite element simulation, and orientations of the two instability modes.
- schema:
  - `type`: object
  - `required`:
    - `alpha_c_stability`: float
    - `alpha_c_simulation`: float
    - `stability_modes`: array of objects
  - `items`:
    - `zeta_angle_deg`: float
    - `eta_angle_deg`: float
  - `required_columns`:
  - `units`:
    - `alpha_c_stability`: dimensionless
    - `alpha_c_simulation`: dimensionless
    - `zeta_angle_deg`: degrees
    - `eta_angle_deg`: degrees

Notes: The checker will verify that |alpha_c_stability - alpha_c_simulation| is within a tolerance and that the instability mode direction vectors align with the deformed lattice vectors (loading and perpendicular directions) within an angular tolerance. Optionally, it may check that the stress drop in stress_strain.csv coincides with alpha_c_simulation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "alpha_c_stability": "float",
          "alpha_c_simulation": "float",
          "stability_modes": "array of objects"
        },
        "items": {
          "zeta_angle_deg": "float",
          "eta_angle_deg": "float"
        },
        "required_columns": [],
        "units": {
          "alpha_c_stability": "dimensionless",
          "alpha_c_simulation": "dimensionless",
          "zeta_angle_deg": "degrees",
          "eta_angle_deg": "degrees"
        }
      },
      "description": "Combined critical shear values from linear stability analysis and finite element simulation, and orientations of the two instability modes."
    }
  ],
  "notes": "The checker will verify that |alpha_c_stability - alpha_c_simulation| is within a tolerance and that the instability mode direction vectors align with the deformed lattice vectors (loading and perpendicular directions) within an angular tolerance. Optionally, it may check that the stress drop in stress_strain.csv coincides with alpha_c_simulation."
}
```

## How you are scored
A hidden verifier inspects /app/outputs/results.json and, if present, /app/outputs/stress_strain.csv. It performs the following checks and combines them into a final reward between 0 and 1:

- Consistency check: verifies that |alpha_c_stability − alpha_c_simulation| is below an absolute tolerance, confirming that the stability analysis agrees with the simulation stress drop.
- Orientation check: for each of the two stability modes, computes the deformed lattice vectors a = F_A e₁ and b = F_A e₂ at the shear alpha_c_simulation (with F_A = I + alpha_c_simulation e₁⊗e₂). It then checks that the eta vector of one mode is approximately aligned with a (the loading direction) and the eta vector of the other mode is approximately aligned with b (the perpendicular direction), within an angular tolerance. This ensures the instability modes correspond to the expected slip directions in the deformed state.
- The reward is weighted predominantly on these two checks; additional minor checks on the existence and format of stress_strain.csv may contribute a small fraction.

The verifier does not require that the computed alpha_c values or mode angles match any specific paper‑reported number exactly; it rewards internal consistency and physically expected alignment. A solution that fabricates values without actually performing the stability analysis and simulation will fail the orientation checks because the geometry at the actual critical shear will not satisfy the alignment conditions.
