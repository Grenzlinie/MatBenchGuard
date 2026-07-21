# Dipole-dipole interaction coefficients and stiffness dispersion for cubic perovskite

## Problem background
In perovskite crystals such as PbZrO₃, dipole-dipole (DD) interactions between A-site and oxygen sublattices can shape the stiffness landscape, potentially flattening the phonon dispersion along the Γ–M direction and favoring incommensurate ordering. The work uses a point-dipole model and Ewald summation to compute the Coulomb coefficient C_A-ORot and then constructs a phenomenological Hamiltonian to study the total stiffness dispersion. The key open question is whether DD coupling persists at the zone center and whether it can produce a stiffness minimum at a finite wave vector under realistic polarizability parameters.

## Approach
The approach employs a point-dipole model with Ewald summation to compute the Coulomb coefficient matrix for the cubic perovskite ABO₃ lattice (A at (0,0,0), B at (0.5,0.5,0.5), O1 at (0.5,0.5,0), O2 at (0.5,0,0.5), O3 at (0,0.5,0.5)). The dipole patterns are restricted to the Σ₃ irreducible representation, which describes transverse modes along the Γ–M direction. For wave vectors q = (ξ,ξ,0) with ξ from 0 to 0.5, the Coulomb matrix is computed in a Cartesian basis and then transformed to the Σ₃ basis, yielding coefficients like C_A-ORot. The total stiffness matrix is obtained by adding a diagonal stabilization term with given site polarizabilities α_A, α_B, α_O-A, α_O-B (in Å³). The lowest eigenvalue of the total stiffness matrix is then computed to map the stiffness dispersion. All computations are performed using standard numerical libraries and the Ewald summation formulas given in the next section.

## Cartesian basis and Σ₃ transformation
The Cartesian dipole vector is a 15‑component list organised by atoms **A, B, O1, O2, O3** in that order, each with components **(x, y, z)**:

0: A_x,  1: A_y,  2: A_z  
3: B_x,  4: B_y,  5: B_z  
6: O1_x, 7: O1_y, 8: O1_z  
9: O2_x, 10: O2_y, 11: O2_z  
12: O3_x, 13: O3_y, 14: O3_z  

The Σ₃ basis comprises five amplitudes: **p_A, p_B, p_O1, p_ORot, p_ODist**. They are related to the Cartesian components by the following relations (from Eq.(1) of the paper):

p_A    → A_x =  p_A/√2,   A_y = -p_A/√2  
p_B    → B_x =  p_B/√2,   B_y = -p_B/√2  
p_O1   → O1_x =  p_O1/√2, O1_y = -p_O1/√2  
p_ORot → O2_x =  p_ORot/√2,  O3_y = -p_ORot/√2  
p_ODist→ O3_x =  p_ODist/√2, O2_y = -p_ODist/√2  

All other Cartesian components are zero.  
This defines a **5×15 transformation matrix T** such that  

**p_Σ₃ = T · p_Cartesian**

with the 15‑vector ordered as above. You can construct T explicitly: for each Σ₃ amplitude, place +1/√2 or –1/√2 at the corresponding Cartesian indices (index 0 for A_x, 1 for A_y, etc.) and set all other entries to zero.

## Ewald summation – required formulas and parameters
The Coulomb coefficient matrix **C(q)** in the Cartesian basis is a 15×15 symmetric matrix. For a wave vector **q** (in reduced units **q = 2π (ξ, ξ, 0)**) it is given by

```
C_{k,k',γ,γ'}(q) =  (4π/v_a) * (q_γ q_γ' / q²)  -  Q_{k,k',γ,γ'}(q)
```

with the auxiliary matrix **Q** defined as

```
Q_{k,k',γ,γ'}(q) =  (4π/v_a) * (q_γ q_γ' / q²) * exp(-q²/(4Y))
                   + (4π/v_a) * Σ_{τ≠-q}  ( (τ+q)_γ (τ+q)_γ' / |τ+q|² ) * exp(-|τ+q|²/(4Y)) * exp(i τ·Δx)
                   - Y^{3/2} * Σ_{R}  H_{γ,γ'}( √Y (x_k - R - x_{k'}) ) * exp(-i q·(x_k - R - x_{k'}))
```

where:
- **a = 1** (lattice constant), **v_a = a³ = 1**
- **Y = 2.1** (Ewald splitting parameter, dimensionless)
- **τ** are reciprocal lattice vectors **τ = 2π (h,k,l)** with integers h,k,l
- **Δx = x_k - x_{k'}** (difference of equilibrium positions in the unit cell)
- **x_k, x_{k'}** are Cartesian vectors for atoms k, k' (positions given above)
- **R** are direct lattice vectors **R = (m, n, p)** (a=1)
- The function **H_{γ,γ'}(x)** (Hessian) is

```
H_{γ,γ'}(x) = (x_γ x_γ'/r²) * [ (3/r³) erfc(r) + (2/√π) (3/r² + 2) exp(-r²) ]
              - δ_{γ,γ'} [ (1/r³) erfc(r) + (2/√π) (1/r²) exp(-r²) ]
```
  with **r = |x|**, and for **r→0** the self‑term becomes **H_{γ,γ'}(0) = (4/(3√π)) δ_{γ,γ'}**.

- The reciprocal‑space sum runs over all integer triplets **(h,k,l)** with **-5 ≤ h,k,l ≤ 5** (excluding τ = -q).
- The real‑space sum runs over all integer triplets **(m,n,p)** with **-5 ≤ m,n,p ≤ 5**.

**Important:** Because the term `(4π/v_a)*(q_γ q_γ'/q²)` diverges at q=0, treat the limit ξ→0 by using a small but non‑zero ξ (e.g. 0.0001) or by the standard analytic limit for the Σ₃ subspace where the macroscopic field vanishes.

After computing the Cartesian **C(q)**, transform it to the Σ₃ basis:

**M(q) = T · C(q) · Tᵀ**

The coefficient **C_A-ORot** is the element **(0,3)** of **M** (row 0: p_A, column 3: p_ORot).

All quantities are dimensionless in these units.

## Reproduction target
Compute the C_A-ORot Coulomb coefficient and the lowest eigenvalue S_min of the total stiffness matrix for the cubic perovskite along the Γ–M direction (q = (ξ,ξ,0), ξ = 0 to 0.5, step 0.02). Use the Ewald summation to obtain the Coulomb matrix, transform to the Σ₃ basis, and build the total stiffness matrix for the given site polarizabilities: α_A = 4.9 Å³, α_B = 0.37 Å³, α_O-A = 4.38 Å³, α_O-B = 2.9 Å³. Produce two CSV files: coulomb_coefficients.csv with ξ and C_A_ORot, and stiffness_dispersion.csv with ξ and S_min. These tables allow the verification of whether C_A_ORot remains non-zero at the zone center and whether the stiffness minimum for this polarizability set occurs at a finite wave vector rather than at Γ.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute Coulomb coefficient C_A-ORot
- Role: scored (load-bearing)
- Action: Implement the Ewald summation method for the cubic perovskite ABO₃ lattice following the formulas and parameters in the “Ewald summation” section above. Compute the Coulomb coefficient matrix in the Cartesian basis for wave vectors q=(ξ,ξ,0) with ξ from 0 to 0.5 (step 0.02). Transform to the Σ₃ irreducible representation basis using the explicit 5×15 matrix T defined in the “Cartesian basis and Σ₃ transformation” section. Extract the C_A-ORot coefficient (the (0,3) element of M). Write a CSV file named coulomb_coefficients.csv with columns xi and C_A_ORot.
- Output file: `/app/outputs/coulomb_coefficients.csv`
- Format: csv
- Contract: columns: xi (float, dimensionless fractional coordinate), C_A_ORot (float, same dimensionless units as paper). Rows for xi = 0.00, 0.02, ..., 0.50.
- Scoring: scored by hidden verifier

### Step 2: Compute stiffness dispersion
- Role: scored (load-bearing)
- Action: Construct the total stiffness matrix S = M + diag(α_A⁻¹, α_B⁻¹, α_O-A⁻¹, α_O-A⁻¹, α_O-B⁻¹) using the Coulomb coefficient matrix M in the Σ₃ basis (computed via the same Ewald implementation as step 1) and the given polarizabilities: α_A=4.9, α_B=0.37, α_O-A=4.38, α_O-B=2.9 (units Å³). Compute the lowest eigenvalue of S for each q along Γ-M (same q-grid). Write a CSV file named stiffness_dispersion.csv with columns xi and S_min.
- Output file: `/app/outputs/stiffness_dispersion.csv`
- Format: csv
- Contract: columns: xi (float), S_min (float, same energy scale as paper). Rows for xi = 0.00, 0.02, ..., 0.50.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/coulomb_coefficients.csv`
- `/app/outputs/stiffness_dispersion.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### coulomb_coefficients.csv
- path: `/app/outputs/coulomb_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: C_A-ORot Coulomb coefficient along Γ-M. Checked by recomputing via Ewald summation and comparing to agent values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `xi`, `C_A_ORot`
  - `units`:
    - `xi`: dimensionless fractional coordinate
    - `C_A_ORot`: dimensionless (Coulomb coefficient units)

### stiffness_dispersion.csv
- path: `/app/outputs/stiffness_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Lowest stiffness eigenvalue along Γ-M for the given polarizability set. Checked by recomputing S from Ewald matrix and polarizabilities, comparing S_min values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `xi`, `S_min`
  - `units`:
    - `xi`: dimensionless fractional coordinate
    - `S_min`: same energy scale as paper (arbitrary units)

Notes: Polarizability values (α_A=4.9, α_B=0.37, α_O-A=4.38, α_O-B=2.9 Å³) are the only non-default inputs; they define the parameter set for Trend 3 in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "coulomb_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "xi",
          "C_A_ORot"
        ],
        "units": {
          "xi": "dimensionless fractional coordinate",
          "C_A_ORot": "dimensionless (Coulomb coefficient units)"
        }
      },
      "description": "C_A-ORot Coulomb coefficient along Γ-M. Checked by recomputing via Ewald summation and comparing to agent values with tolerance."
    },
    {
      "file": "stiffness_dispersion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "xi",
          "S_min"
        ],
        "units": {
          "xi": "dimensionless fractional coordinate",
          "S_min": "same energy scale as paper (arbitrary units)"
        }
      },
      "description": "Lowest stiffness eigenvalue along Γ-M for the given polarizability set. Checked by recomputing S from Ewald matrix and polarizabilities, comparing S_min values with tolerance."
    }
  ],
  "notes": "Polarizability values (α_A=4.9, α_B=0.37, α_O-A=4.38, α_O-B=2.9 Å³) are the only non-default inputs; they define the parameter set for Trend 3 in the paper."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each scored output file. The verifier recomputes quantities from your CSV tables and compares against reference values. Simply quoting literature numbers is not sufficient – your computed values must match the hidden references within tolerances that account for legitimate implementation differences.