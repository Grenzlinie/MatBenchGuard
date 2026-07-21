# Piezoelectric bending actuator modeling

## Problem background
Adhesively bonded composite pipe joints under axial tensile load suffer from high peel and shear stress concentrations near the adhesive layer edges, which can limit joint strength. To actively alleviate these stresses, a smart joint design incorporates piezoelectric layers inside the connection coupler. When a voltage is applied across these piezoelectric layers, they act as actuators and generate additional forces and moments that modify the stress distribution in the adhesive.

The task considers an axisymmetric composite pipe joint consisting of an inner main pipe, an outer coupler sleeve, and a thin adhesive layer bonding them together. The coupler is a symmetric laminate with stacking sequence [Comp/PZT1/Comp/Comp/PZT2/Comp], where each layer (composite or piezoelectric) has equal thickness (coupler wall thickness divided by 6). The pipe and coupler are made of the same composite material. The joint is subjected to a 25 kN axial tensile load, and the electric field is applied equally to both piezoelectric layers, with two cases: E₃ = 0 V/mm and E₃ = -500 V/mm.

The material properties and geometry are as follows:

**Composite lamina** (E-glass/vinyl ester, orthotropic):
- E₁ = 25.2 GPa, E₂ = 7.5 GPa, G₁₂ = 2.4 GPa, ν₁₂ = 0.32

**Epoxy adhesive**:
- Eₐ = 0.96 GPa, Gₐ = 0.34 GPa

**Piezoelectric material** (poling direction along the radial z-axis):
- E_PZT = 84 GPa, ν = 0.22, d₃₁ = d₃₂ = -310 × 10⁻¹² m/V

**Geometry**:
- Pipe inner radius R_pi = 50.8 mm
- Pipe wall thickness hₚ = 2.54 mm
- Coupler wall thickness h_c = 2.54 mm
- Adhesive layer thickness hₐ = 0.0127 mm
- Overlap length l₁ = 25.4 mm
- Bare pipe length l₂ = 127 mm
- Mid-plane radii: Rₚ = R_pi + hₚ/2; R_c = R_pi + hₚ + hₐ + h_c/2
- Outer radius of pipe R_po = R_pi + hₚ; inner radius of coupler R_ci = R_pi + hₚ + hₐ

The adhesive layer stresses (peel q and shear τ) are to be computed along the overlap length and the maximum absolute values extracted. These maxima depend on the applied electric field and indicate the effectiveness of the piezoelectric actuation.

## Approach
You must implement an electro-mechanical analytical model based on first-order shear deformation theory (FOST) to predict the peel and shear stress distributions in the adhesive layer of the smart joint.

**Displacement fields and strains**
For each section (coupler, overlapping pipe, bare pipe) the displacements are expanded as
- u(x,z) = u₀(x) + z φ(x)
- w(x,z) = w(x)
with no tangential displacement (axi-symmetric assumption). The in-plane strain components are
- εₓ = ∂u₀/∂x + z ∂φ/∂x
- ε_θ = w / (R + z)
- γ_xz = φ + ∂w/∂x

**Constitutive relations and resultant forces/moments**
For each layer k, the stress-strain relations for a generally orthotropic lamina (with plane-stress assumptions) are
- σₓ = Q̄₁₁ εₓ + Q̄₁₂ ε_θ – ē₃₁ E₃
- σ_θ = Q̄₁₂ εₓ + Q̄₂₂ ε_θ – ē₃₂ E₃
- τ_xz = K Q̄₅₅ γ_xz
where Q̄_ij are the transformed stiffnesses (computed from the given engineering constants), ē_₃₁, ē_₃₂ the piezoelectric stress coefficients (zero for composite layers), and E₃ the applied electric field (positive along +z). K is the shear correction factor (commonly 5/6).

Integrating through the thickness of each section yields the force and moment resultants:
- N_x = A₁₁ ∂u₀/∂x + B₁₁ ∂φ/∂x + E₁₂ w – N_x^PZT
- M_x = B₁₁ ∂u₀/∂x + D₁₁ ∂φ/∂x + F₁₂ w – M_x^PZT
- N_θ = A₂₁ ∂u₀/∂x + B₂₁ ∂φ/∂x + E₂₂ w – N_θ^PZT
- Q_x = A₅₅ (φ + ∂w/∂x)

The stiffness coefficients (A_ij, B_ij, D_ij, E_ij, F_ij) are defined by sums over layers of ∫ (R+z)/R · (Q̄_ij) · (1, z, z²) dz. The piezoelectric contributions are
- N_x^PZT = Σ ∫ (R+z)/R · ē₃₁ · E₃ dz
- M_x^PZT = Σ ∫ (R+z)/R · z · ē₃₁ · E₃ dz
- N_θ^PZT = Σ ∫ (R+z)/R · ē₃₂ · E₃ dz
For uniform E₃ over a layer, these become constant.

**Adhesive stresses**
The shear and peel stresses are expressed in terms of the displacement variables:
- τ = (Gₐ/hₐ) [ (u₀ₚ – u₀_c) + (hₚ/2 φₚ + h_c/2 φ_c) ] – (Gₐ/2) (∂wₚ/∂x + ∂w_c/∂x)
- q = (Eₐ/hₐ) (w_c – wₚ)

**Equilibrium equations**
Consider the free-body diagrams of the coupler, adhesive, and pipe. The equilibrium of forces and moments leads to the following set of ODEs:

For the coupler (0 < x < l₁):
∂N_xc/∂x = –(R_ci/R_c) τ
∂M_xc/∂x – Q_xc = (h_c/2)(R_ci/R_c) τ
∂Q_xc/∂x – N_θc/R_c = (R_ci/R_c) q

For the overlapping pipe (0 < x < l₁):
∂N_xp/∂x = (R_po/R_p) τ
∂M_xp/∂x – Q_xp = (hₚ/2)(R_po/R_p) τ
∂Q_xp/∂x – N_θp/R_p = –(R_po/R_p) q

For the bare pipe (0 < x₂ < l₂): all adhesive terms vanish, giving homogeneous equations.

**State-space formulation**
Introduce the state vector for the overlapping region:
Z = [ u₀_c,  u₀_c',  φ_c,  φ_c',  w_c,  w_c',  u₀ₚ,  u₀ₚ',  φₚ,  φₚ',  wₚ,  wₚ' ]^T
and for the bare pipe:
X = [ u₀_b,  u₀_b',  φ_b,  φ_b',  w_b,  w_b' ]^T

The displacement-based governing equations reduce to
 Z' = [A] Z + Λ   (overlapping region)
 X' = [B] X       (bare pipe)

The non-zero entries of [A] (12×12) and [B] (6×6) are listed below. In these expressions, A_c11, B_c11, D_c11, E_c12, F_c12, A_c55, A_c21, B_c21, E_c22 refer to the coupler’s stiffness coefficients; A_p11, … are the pipe coefficients.

**Matrix [A]**:
A[1,2] = A[3,4] = A[5,6] = A[7,8] = A[9,10] = A[11,12] = 1

A[2,1] = ( D_c11·(R_ci Gₐ)/(R_c hₐ) + (h_c B_c11·R_ci Gₐ)/(2 R_c hₐ) ) / (A_c11 D_c11 – B_c11²)
A[2,3] = ( –D_c11·(h_c R_ci Gₐ)/(2 R_c hₐ) – B_c11·(A_c55 + h_c² R_ci Gₐ/(4 R_c hₐ)) ) / (A_c11 D_c11 – B_c11²)
A[2,6] = ( D_c11·(R_ci Gₐ/(2 R_c) – E_c12) – B_c11·(A_c55 – h_c R_ci Gₐ/(4 R_c) – F_c12) ) / (A_c11 D_c11 – B_c11²)
A[2,7] = ( –D_c11·(R_ci Gₐ)/(R_c hₐ) – B_c11·(h_c R_ci Gₐ)/(2 R_c hₐ) ) / (A_c11 D_c11 – B_c11²)
A[2,9] = ( –D_c11·(hₚ R_ci Gₐ)/(2 R_c hₐ) – B_c11·(h_c hₚ R_ci Gₐ)/(4 R_c hₐ) ) / (A_c11 D_c11 – B_c11²)
A[2,12] = ( D_c11·(R_ci Gₐ)/(2 R_c) + B_c11·(h_c R_ci Gₐ)/(4 R_c) ) / (A_c11 D_c11 – B_c11²)

A[4,1] = ( –A_c11·(h_c R_ci Gₐ)/(2 R_c hₐ) – B_c11·(R_ci Gₐ)/(R_c hₐ) ) / (A_c11 D_c11 – B_c11²)
A[4,3] = ( A_c11·(A_c55 + h_c² R_ci Gₐ/(4 R_c hₐ)) + B_c11·(h_c R_ci Gₐ)/(2 R_c hₐ) ) / (A_c11 D_c11 – B_c11²)
A[4,6] = ( A_c11·(A_c55 – h_c R_ci Gₐ/(4 R_c) – F_c12) – B_c11·(R_ci Gₐ/(2 R_c) – E_c12) ) / (A_c11 D_c11 – B_c11²)
A[4,7] = ( A_c11·(h_c R_ci Gₐ)/(2 R_c hₐ) + B_c11·(R_ci Gₐ)/(R_c hₐ) ) / (A_c11 D_c11 – B_c11²)
A[4,9] = ( A_c11·(h_c hₚ R_ci Gₐ)/(4 R_c hₐ) + B_c11·(hₚ R_ci Gₐ)/(2 R_c hₐ) ) / (A_c11 D_c11 – B_c11²)
A[4,12] = ( –A_c11·(h_c R_ci Gₐ)/(4 R_c) – B_c11·(R_ci Gₐ)/(2 R_c) ) / (A_c11 D_c11 – B_c11²)

A[6,2] = A_c21 / (R_c A_c55)
A[6,4] = (B_c21 / R_c – A_c55) / A_c55
A[6,5] = (E_c22 / R_c + (R_ci Eₐ)/(R_c hₐ)) / A_c55
A[6,11] = – (R_ci Eₐ) / (R_c hₐ A_c55)

A[8,1] = ( –D_p11·(R_po Gₐ)/(R_p hₐ) + B_p11·(hₚ R_po Gₐ)/(2 R_p hₐ) ) / (A_p11 D_p11 – B_p11²)
A[8,3] = ( D_p11·(h_c R_po Gₐ)/(2 R_p hₐ) – B_p11·(h_c hₚ R_po Gₐ)/(4 R_p hₐ) ) / (A_p11 D_p11 – B_p11²)
A[8,6] = ( –D_p11·(R_po Gₐ)/(2 R_p) + B_p11·(hₚ R_po Gₐ)/(4 R_p) ) / (A_p11 D_p11 – B_p11²)
A[8,7] = ( D_p11·(R_po Gₐ)/(R_p hₐ) – B_p11·(hₚ R_po Gₐ)/(2 R_p hₐ) ) / (A_p11 D_p11 – B_p11²)
A[8,9] = ( D_p11·(hₚ R_po Gₐ)/(2 R_p hₐ) – B_p11·(A_p55 + hₚ² R_po Gₐ/(4 R_p hₐ)) ) / (A_p11 D_p11 – B_p11²)
A[8,12] = ( –D_p11·(E_p12 + R_po Gₐ/(2 R_p)) – B_p11·(A_p55 – F_p12 – hₚ R_po Gₐ/(4 R_p)) ) / (A_p11 D_p11 – B_p11²)

A[10,1] = ( –A_p11·(hₚ R_po Gₐ)/(2 R_p hₐ) + B_p11·(R_po Gₐ)/(R_p hₐ) ) / (A_p11 D_p11 – B_p11²)
A[10,3] = ( A_p11·(h_c hₚ R_po Gₐ)/(4 R_p hₐ) – B_p11·(h_c R_po Gₐ)/(2 R_p hₐ) ) / (A_p11 D_p11 – B_p11²)
A[10,6] = ( –A_p11·(hₚ R_po Gₐ)/(4 R_p) + B_p11·(R_po Gₐ)/(2 R_p) ) / (A_p11 D_p11 – B_p11²)
A[10,7] = ( A_p11·(hₚ R_po Gₐ)/(2 R_p hₐ) – B_p11·(R_po Gₐ)/(R_p hₐ) ) / (A_p11 D_p11 – B_p11²)
A[10,9] = ( A_p11·(A_p55 + hₚ² R_po Gₐ/(4 R_p hₐ)) – B_p11·(hₚ R_po Gₐ)/(2 R_p hₐ) ) / (A_p11 D_p11 – B_p11²)
A[10,12] = ( A_p11·(A_p55 – F_p12 – hₚ R_po Gₐ/(4 R_p)) + B_p11·(E_p12 + R_po Gₐ/(2 R_p)) ) / (A_p11 D_p11 – B_p11²)

A[12,5] = – (R_po Eₐ) / (R_p hₐ A_p55)
A[12,8] = A_p21 / (R_p A_p55)
A[12,10] = (B_p21 / R_p – A_p55) / A_p55
A[12,11] = (R_po Eₐ) / (R_p hₐ A_p55)
A[12,12] = E_p22 / (R_p A_p55)

**Matrix [B]** (bare pipe):
B[1,2] = B[3,4] = B[5,6] = 1
B[2,3] = –B_p11 A_p55 / (A_p11 D_p11 – B_p11²)
B[2,6] = ( –D_p11 E_p12 – B_p11 (A_p55 – F_p12) ) / (A_p11 D_p11 – B_p11²)
B[4,3] = A_p11 A_p55 / (A_p11 D_p11 – B_p11²)
B[4,6] = ( A_p11 (A_p55 – F_p12) + B_p11 E_p12 ) / (A_p11 D_p11 – B_p11²)
B[6,2] = A_p21 / (R_p A_p55)
B[6,4] = (B_p21 / R_p – A_p55) / A_p55
B[6,5] = E_p22 / (R_p A_p55)

**Piezoelectric forcing**
The uniform electric field E₃ induces constant resultant forces and moments N_xc^PZT, M_xc^PZT, N_θc^PZT in the coupler. For the present analysis, these effectively modify the natural force boundary conditions at the free end of the coupler (x = l₁):
- N_xc(l₁) = N_xc^PZT
- M_xc(l₁) = M_xc^PZT
- Q_xc(l₁) = 0
All other boundary and continuity conditions remain as given below.

**Boundary and continuity conditions**
- At x = 0 (coupler symmetry plane): u₀_c(0) = 0, w_c'(0) = 0, Q_xc(0) = 0
- At x = 0 (overlapping pipe free end): N_xp(0) = 0, M_xp(0) = 0, Q_xp(0) = 0
- At x = l₁ (coupler free end, with piezoelectric contributions): N_xc(l₁) = N_xc^PZT, M_xc(l₁) = M_xc^PZT, Q_xc(l₁) = 0
- At x = l₁ (continuity between overlapping pipe and bare pipe):
  u₀ₚ(l₁) = u₀_b(0), φₚ(l₁) = φ_b(0), wₚ(l₁) = w_b(0),
  and all first derivatives are continuous.
- At x₂ = l₂ (loaded pipe end): N_xb(l₂) = 25 kN (the total axial force, applied uniformly over the pipe cross-section), M_xb(l₂) = 0, Q_xb(l₂) = 0.

**Solution and stress extraction**
Solve the ODE systems for Z(x) and X(x) consistent with the above boundary conditions. A convenient method is to use a numerical ODE integrator combined with a shooting method, or to propagate the state transition matrix. Once the state variables are obtained, the peel and shear stresses at any x in the overlap are computed via
- q(x) = (Eₐ/hₐ) (Z₅ – Z₁₁)
- τ(x) = –(Gₐ/hₐ) Z₁ + (Gₐ h_c/(2 hₐ)) Z₃ – (Gₐ/2) Z₆ + (Gₐ/hₐ) Z₇ + (Gₐ hₚ/(2 hₐ)) Z₉ – (Gₐ/2) Z₁₂
where Z₁ = u₀_c, Z₃ = φ_c, Z₅ = w_c, Z₆ = w_c', Z₇ = u₀ₚ, Z₉ = φₚ, Z₁₁ = wₚ, Z₁₂ = wₚ'. (Note the sign in the last term: the expression above matches the standard definition; any sign discrepancy should be resolved by ensuring satisfaction of the equilibrium equations.)

For each electric-field case, compute the stress distributions over the overlap length and extract the maximum absolute values of q and τ.

## Reproduction target
For the described composite pipe joint with the given materials and geometry, compute the maximum absolute peel stress and the maximum absolute shear stress in the adhesive layer for the two electric-field conditions applied to both piezoelectric layers simultaneously:
1. E₃ = 0 V/mm
2. E₃ = –500 V/mm

Produce a CSV file `/app/outputs/peak_stresses.csv` with these columns (case, e3_V_per_mm, peel_stress_max_Pa, shear_stress_max_Pa). The "case" column should contain the same identifier for both rows (e.g., "Case 1"); the two rows correspond to the two electric-field levels. Stresses must be in Pa.

Note that the reference solution is independently obtained from the same FOST state‑space model; your job is to faithfully execute the analysis and report the peak values.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Assemble material and geometric parameters
- Role: process
- Action: Define the composite lamina, adhesive, and piezoelectric material constants and the geometric dimensions of the pipe joint as given in the task description.
- Evidence: none

### Step 2: Compute stress distributions via state-space method
- Role: process
- Action: Implement the displacement-based governing equations in state-space form, set up boundary and continuity conditions, solve the ODE system to obtain displacement fields, then compute the peel stress q(x) and shear stress τ(x) along the adhesive layer for both electric-field cases (E3=0 and E3=-500 V/mm).
- Evidence: `/app/outputs/stress_profiles.npz`

### Step 3: Extract maximum peel and shear stresses
- Role: scored (load-bearing)
- Action: From the computed stress profiles, determine the maximum absolute peel stress and maximum absolute shear stress for each case. Write a CSV file with columns: case, e3_V_per_mm, peel_stress_max_Pa, shear_stress_max_Pa.
- Output file: `/app/outputs/peak_stresses.csv`
- Format: csv
- Contract: columns: case (string), e3_V_per_mm (float), peel_stress_max_Pa (float), shear_stress_max_Pa (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/peak_stresses.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### peak_stresses.csv
- path: `/app/outputs/peak_stresses.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Maximum peel and shear stresses in the adhesive layer for Case 1 under two electric-field conditions (0 and -500 V/mm).
- schema:
  - `type`: table
  - `required_columns`: `case`, `e3_V_per_mm`, `peel_stress_max_Pa`, `shear_stress_max_Pa`
  - `units`:
    - `e3_V_per_mm`: V/mm
    - `peel_stress_max_Pa`: Pa
    - `shear_stress_max_Pa`: Pa

Notes: The solver must implement the FOST state-space model as described; the scoring reference is computed independently by the checker using the same material and geometric parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "peak_stresses.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "e3_V_per_mm",
          "peel_stress_max_Pa",
          "shear_stress_max_Pa"
        ],
        "units": {
          "e3_V_per_mm": "V/mm",
          "peel_stress_max_Pa": "Pa",
          "shear_stress_max_Pa": "Pa"
        }
      },
      "description": "Maximum peel and shear stresses in the adhesive layer for Case 1 under two electric-field conditions (0 and -500 V/mm)."
    }
  ],
  "notes": "The solver must implement the FOST state-space model as described; the scoring reference is computed independently by the checker using the same material and geometric parameters."
}
```

## How you are scored
Your submission will be scored by a hidden verifier that independently implements the same FOST state‑space model using the identical input parameters. The verifier computes reference maximum peel and shear stresses for both electric‑field cases. It then reads your `peak_stresses.csv` and compares each entry to the hidden reference. The reward reflects how closely your reported values match the reference (relative error tolerated), with each case contributing to the final score. You do not need to know the exact tolerance; simply produce the correct stress maxima from a rigorous solution of the model.
