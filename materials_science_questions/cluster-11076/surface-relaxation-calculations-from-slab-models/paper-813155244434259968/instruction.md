# Compute size-dependent elastic properties of Au (110) thin films from MD simulations

## Problem background
Understanding size-dependent elastic properties of thin films is critical for nanomechanics. At nanoscale thicknesses, surface effects dominate, causing the nominal Young's modulus to deviate from bulk behavior. A nonlinear scaling law relates the nominal Young's modulus of a thin film to its thickness through core elastic constants, surface elastic constants, and surface eigenstress. This task focuses on determining the core and surface elastic parameters for Au (110) thin films via molecular dynamics (MD) simulations and testing the scaling law's prediction against a direct MD tension test.

## Approach
The analysis treats a thin film as a composite of a 3D core (bulk‑like) and two 2D surfaces. The core's second‑order and third‑order elastic constants (SOEC and TOEC) for FCC Au are first determined in crystal coordinates by applying six distinct strain modes to a bulk crystal in MD and fitting the energy‑strain curves. These tensors are then rotated to the sample coordinate system of a (110)‑oriented film (x along [1‑10], y along [001], z along [110]) to obtain core pseudo‑uniaxial Young's moduli. Slab models with (110) free surfaces are constructed and relaxed through a three‑step procedure: dimension‑conserved normal relaxation, dimension‑changed normal relaxation, and parallel relaxation. From the relaxed films at several thicknesses, in‑plane strain modes are applied and the force‑balance condition between core stress and surface stress is used to extract the surface eigenstress and surface first‑ and second‑order Young's moduli. Finally, the scaling law is applied to predict the nominal Young's modulus at a film thickness of 3 nm (with y dimension fixed), and a direct pseudo‑uniaxial MD tension test on the relaxed 3 nm film provides an independent value for comparison.

## Reproduction target
Using MD simulations with the Au EAM potential (Daw & Baskes, 1984) in LAMMPS, produce a single JSON artifact, `/app/outputs/extracted_parameters.json`, containing:
- Bulk Au second‑order elastic constants (c11, c12, c44) and third‑order elastic constants (c111, c112, c144, c155, c123, c456) in crystal coordinates.
- Core pseudo‑uniaxial Young's modulus and second‑order modulus for the x‑direction of a (110) film.
- Surface eigenstress, surface Young's modulus, and second‑order surface Young's modulus for the (110) surface along x.
- The nominal Young's modulus at a film thickness of 3 nm computed from the scaling law (using the above parameters) and from a direct MD pseudo‑uniaxial tension test (with y dimension fixed) on a relaxed 3 nm film.
All values must be reported in the specified units.

## Assets
- LAMMPS: https://lammps.sandia.gov
- Au EAM potential (Daw & Baskes, 1984)

## Required equations

### Rotation matrix for (110) films
The sample coordinates $(x,y,z)$ of a (110) film are oriented along $[1\overline{1}0]$, $[001]$, and $[110]$ in the crystal coordinate system. The rotation matrix that transforms tensors from crystal coordinates to sample coordinates is

$$
\mathbf{T} = \begin{pmatrix}
-1/\sqrt{2} & 1/\sqrt{2} & 0 \\
0 & 0 & 1 \\
1/\sqrt{2} & 1/\sqrt{2} & 0
\end{pmatrix}.
$$

Apply this rotation to the bulk SOEC and TOEC tensors using

$$
c'_{ijkl} = T_{ia} T_{jb} c_{abcd} T_{kc} T_{ld}, \qquad
\tilde{c}'_{ijklmn} = T_{ia} T_{jb} T_{kc} \tilde{c}_{abcdef} T_{ld} T_{me} T_{nf}.
$$

### Core pseudo‑uniaxial Young's moduli for (110) films
After rotating the bulk elastic constants to the sample coordinate system (indicated by a prime), the first‑order and second‑order core Young's moduli for loading along the $x$ direction with the $y$ dimension fixed are

$$
Y_x^c = c'_{11} - \frac{(c'_{13})^2}{c'_{33}}, \qquad
\tilde{Y}_x^c = \frac{1}{2}\left[ \tilde{c}'_{111} + \tilde{c}'_{133}\left(\frac{c'_{13}}{c'_{33}}\right)^2 - \tilde{c}'_{113}\frac{c'_{13}}{c'_{33}} \right].
$$

### Nonlinear scaling law for the nominal Young's modulus
For a (110) thin film of thickness $h$ loaded along $x$ with the $y$ dimension fixed, the nominal Young's modulus $\bar{Y}_x^n$ is given by

$$
\bar{Y}_x^n = Y_x^c + \frac{2 Y_x^s}{h} + 2\left( \tilde{Y}_x^c + \frac{2 \tilde{Y}_x^s}{h} \right) \varepsilon_x^{\text{ini}},
$$

where the relaxation‑induced initial in‑plane strain $\varepsilon_x^{\text{ini}}$ is

$$
\varepsilon_x^{\text{ini}} =
\frac{ - (h Y_x^c + 2 Y_x^s) + \sqrt{ (h Y_x^c + 2 Y_x^s)^2 - 8 \sigma_x^{s0} (h \tilde{Y}_x^c + 2 \tilde{Y}_x^s) } }
     { 2 (h \tilde{Y}_x^c + 2 \tilde{Y}_x^s) }.
$$

### Bulk elastic constant fitting via strain modes
The bulk second‑ and third‑order elastic constants are extracted by applying a series of specific finite strain modes to an FCC Au crystal and fitting the energy density versus strain.

**FCC Au lattice constant:**  
Use the equilibrium FCC lattice constant $a_0 = 4.078\,\text{Å}$ for the Au EAM potential. Define the primitive‑cell volume $V_0 = a_0^3/4$ (or use the volume of your simulation supercell).

**Strain modes**  
Apply the following six independent Lagrangian strain modes in Voigt notation, $\boldsymbol{\eta} = (\eta_1,\eta_2,\eta_3,\eta_4,\eta_5,\eta_6)$, with a scalar amplitude $\xi$:

1. $\boldsymbol{\eta}^{(1)} = (\xi, 0, 0, 0, 0, 0)$  
2. $\boldsymbol{\eta}^{(2)} = (\xi, \xi, 0, 0, 0, 0)$  
3. $\boldsymbol{\eta}^{(3)} = (\xi, \xi, \xi, 0, 0, 0)$  
4. $\boldsymbol{\eta}^{(4)} = (0, 0, 0, \xi, 0, 0)$  
5. $\boldsymbol{\eta}^{(5)} = (0, 0, 0, \xi, \xi, 0)$  
6. $\boldsymbol{\eta}^{(6)} = (\xi, 0, 0, \xi, 0, 0)$  

**Strain amplitudes**  
For each mode, use a set of $\xi$ values that cover both positive and negative deformations, e.g.  
$\xi \in \{-0.04,\, -0.03,\, -0.02,\, -0.01,\, 0.00,\, 0.01,\, 0.02,\, 0.03,\, 0.04\}$.

**Energy‑strain fitting**  
For each mode and each $\xi$, deform the simulation box accordingly (keeping fractional atomic positions fixed), perform an energy minimisation at 0 K, and compute the energy density $u = U / V_0$ (where $U$ is the total potential energy and $V_0$ the undeformed volume).  
Fit the data for each mode to the cubic polynomial

$$
u(\xi) = u_0 + A \xi^2 + B \xi^3 + C \xi^4
$$

(including the $\xi^4$ term can improve the quality of the fit, but only $A$ and $B$ are needed for the elastic constants).  

The elastic constants are then obtained from the coefficients $A$ and $B$ of the six modes using the following relations (derived from the strain energy function of a cubic crystal):

- Mode 1: $A_1 = c_{11}/2$, $B_1 = c_{111}/6$  
- Mode 2: $A_2 = c_{11} + c_{12}$, $B_2 = c_{111}/3 + c_{112}$  
- Mode 3: $A_3 = 3c_{11}/2 + 3c_{12}$, $B_3 = c_{111}/2 + 3c_{112} + c_{123}$  
- Mode 4: $A_4 = c_{44}/2$, $B_4 = c_{155}/6$  
- Mode 5: $A_5 = c_{44}$, $B_5 = c_{155}/3 + c_{456}$  
- Mode 6: $A_6 = c_{11}/2 + c_{44}/2$, $B_6 = c_{111}/6 + c_{144}/2$  

Solve this system of equations for the independent constants: $c_{11}, c_{12}, c_{44}$ (SOEC) and $c_{111}, c_{112}, c_{123}, c_{144}, c_{155}, c_{456}$ (TOEC). (The formulas assume the energy density is used; if you fit the total energy $U$ instead, multiply each $A$ and $B$ by $V_0$ before solving.)  

## Workflow steps

### Step 1: Bulk Au elastic constant determination in crystal coordinates
- Role: process
- Action: Run LAMMPS MD simulations on a bulk FCC Au crystal with $a_0 = 4.078\,\text{Å}$. Use the EAM potential, 0 K energy minimisation (e.g. `min_style cg`, `minimize 1e-12 1e-12 100000`). Apply the six strain modes with the strain amplitudes listed above. For each state, record the final total energy and the supercell volume. Fit the energy‑strain curves as described in Required equations to obtain the second‑order elastic constants (c11, c12, c44) and third‑order elastic constants (c111, c112, c144, c155, c123, c456) in crystal coordinates. Convert all constants to GPa.

### Step 2: Coordinate transformation to (110) sample coordinates and core moduli calculation
- Role: process
- Action: Rotate the bulk SOEC and TOEC tensors from the crystal coordinate system to the sample coordinate system of a (110)‑oriented film using the rotation matrix given in the Required equations section. Compute the core first‑order pseudo‑uniaxial Young's modulus $Y_x^c$ and second‑order modulus $\tilde{Y}_x^c$ using the formulas in the same section.

### Step 3: Au (110) thin film construction and normal/parallel relaxation
- Role: process
- Action: Build atomistic slab models with (110) free surfaces at five different thicknesses: 2 nm, 3 nm, 4 nm, 5 nm, and 6 nm. Ensure the in‑plane dimensions are sufficiently large (e.g. ~15 nm × 15 nm) to minimise edge effects. Use periodic boundary conditions in the $x$ and $y$ directions and a free surface in $z$. Perform the three‑step relaxation at 0 K using energy minimisation (conjugate gradient):
  1. *Dimension‑conserved normal relaxation* — allow atoms to move only in the $z$ direction while keeping the $z$ box dimension fixed.
  2. *Dimension‑changed normal relaxation* — allow the $z$ box dimension to change, giving the film its equilibrium free‑standing thickness.
  3. *Parallel relaxation* — allow all in‑plane degrees of freedom to relax (atoms and in‑plane box dimensions) while keeping the $z$ box dimension fixed at the value obtained in step 2.  
  After parallel relaxation, record the equilibrium in‑plane strain $\varepsilon_x^{\text{ini}}$ for each thickness (computed from the change of the box length along $x$ relative to the ideal bulk‑derived dimensions).

### Step 4: Surface property extraction via force balance
- Role: process
- Action: For each relaxed film thickness, perform a series of small pseudo‑uniaxial tensile tests along the $x$ direction with the $y$ dimension fixed. Apply small engineering strains $\Delta\varepsilon_x$ (both positive and negative, in the range approx. –0.01 to 0.01) by incrementally changing the $x$ box length, re‑relaxing in $z$ and $y$ after each step. Determine the nominal Young's modulus $\bar{Y}_x^n(h)$ from the slope of the stress‑strain curve (stress computed from the virial or per‑atom stress divided by the total volume).  
  Use the multi‑thickness data $(h,\, \varepsilon_x^{\text{ini}},\, \bar{Y}_x^n)$ to extract the surface parameters $\sigma_x^{s0}$, $Y_x^s$, and $\tilde{Y}_x^s$ via least‑squares fitting with equations (4a) and (4b).  Specifically, minimise the objective function

  $$
  \sum_i \left[ \left( \bar{Y}_x^{n,\text{MD}}(h_i) - \bar{Y}_x^{n,\text{model}}(h_i;\text{params}) \right)^2 + \lambda \left( \varepsilon_x^{\text{ini,MD}}(h_i) - \varepsilon_x^{\text{ini,model}}(h_i;\text{params}) \right)^2 \right],
  $$

  where the model predictions are given by (4a) and (4b) using the known core moduli $Y_x^c$, $\tilde{Y}_x^c$ and the three unknown surface parameters. A weighting factor $\lambda$ of order unity works well.  Report the fitted $\sigma_x^{s0}$ in N/m, and $Y_x^s$, $\tilde{Y}_x^s$ in N/m.

### Step 5: Compile extracted parameters, compute scaling‑law modulus, and perform direct tension test
- Role: scored (load‑bearing)
- Action: Using the core moduli from Step 2 and the surface parameters from Step 4, compute the nominal Young's modulus at $h = 3\,\text{nm}$ via the nonlinear scaling law given in the Required equations section. Separately, perform a direct pseudo‑uniaxial MD tension test (fixed $y$ dimension) on the relaxed 3 nm (110) film to obtain the nominal Young's modulus. Assemble all results — bulk SOEC/TOEC, core moduli, surface parameters, the scaling‑law modulus, and the direct test modulus — into the JSON output file.
- Output file: `/app/outputs/extracted_parameters.json`
- Format: json
- Contract: {
  "bulk_soec": [c11, c12, c44] (GPa),
  "bulk_toec": [c111, c112, c144, c155, c123, c456] (GPa),
  "core_young_modulus_x": Y_x_c (GPa),
  "core_young_modulus_2nd_x": \tilde{Y}_x_c (GPa),
  "surface_young_modulus_x": Y_x_s (N/m),
  "surface_young_modulus_2nd_x": \tilde{Y}_x_s (N/m),
  "surface_eigenstress_x": σ_x_s0 (N/m),
  "Y_n_direct_3nm": nominal Young's modulus from direct MD tension test at 3 nm (GPa),
  "Y_n_scaling_3nm": nominal Young's modulus from scaling law at 3 nm (GPa)
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/extracted_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### extracted_parameters.json
- path: `/app/outputs/extracted_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The scored artifact containing MD