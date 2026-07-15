# Compute size-dependent elastic properties of Au (110) thin films from MD simulations

## Problem background
Understanding size-dependent elastic properties of thin films is critical for nanomechanics. At nanoscale thicknesses, surface effects dominate, causing the nominal Young's modulus to deviate from bulk behavior. A nonlinear scaling law relates the nominal Young's modulus of a thin film to its thickness through core elastic constants, surface elastic constants, and surface eigenstress. This task focuses on determining the core and surface elastic parameters for Au (110) thin films via molecular dynamics simulations and testing the scaling law's prediction against a direct MD tension test.

## Approach
The analysis treats a thin film as a composite of a 3D core (bulk-like) and two 2D surfaces. The core's second-order and third-order elastic constants (SOEC and TOEC) for FCC Au are first determined in crystal coordinates by applying six distinct strain modes to a bulk crystal in MD and fitting the energy-strain curves. These tensors are then rotated to the sample coordinate system of a (110)-oriented film (x along [1-10], y along [001], z along [110]) to obtain core pseudo-uniaxial Young's moduli. Slab models with (110) free surfaces are constructed and relaxed through a three-step procedure: dimension-conserved normal relaxation, dimension-changed normal relaxation, and parallel relaxation. From the relaxed films at several thicknesses, in-plane strain modes are applied and the force-balance condition between core stress and surface stress is used to extract the surface eigenstress and surface first- and second-order Young's moduli. Finally, the scaling law is applied to predict the nominal Young's modulus at a film thickness of 3 nm (with y dimension fixed), and a direct pseudo-uniaxial MD tension test on the relaxed 3 nm film provides an independent value for comparison.

## Reproduction target
Using MD simulations with the Au EAM potential (Daw & Baskes, 1984) in LAMMPS, produce a single JSON artifact, `/app/outputs/extracted_parameters.json`, containing:
- Bulk Au second-order elastic constants (c11, c12, c44) and third-order elastic constants (c111, c112, c144, c155, c123, c456) in crystal coordinates.
- Core pseudo-uniaxial Young's modulus and second-order modulus for the x-direction of a (110) film.
- Surface eigenstress, surface Young's modulus, and second-order surface Young's modulus for the (110) surface along x.
- The nominal Young's modulus at a film thickness of 3 nm computed from the scaling law (using the above parameters) and from a direct MD pseudo-uniaxial tension test (with y dimension fixed) on a relaxed 3 nm film.
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

## Workflow steps

### Step 1: Bulk Au elastic constant determination in crystal coordinates
- Role: process
- Action: Run LAMMPS MD simulations (conjugate gradient minimization) on a bulk FCC Au crystal. Apply the six strain modes and fit the energy‑strain curves to obtain the second‑order elastic constants (c11, c12, c44) and third‑order elastic constants (c111, c112, c144, c155, c123, c456) in the crystal coordinate system.
- Evidence: `/app/outputs/bulk_elastic_fit_results.json`

### Step 2: Coordinate transformation to (110) sample coordinates and core moduli calculation
- Role: process
- Action: Rotate the bulk SOEC and TOEC tensors from the crystal coordinate system to the sample coordinate system of a (110)-oriented film using the rotation matrix given in the Required equations section. Compute the core first‑order pseudo‑uniaxial Young's modulus Y_x^c and second‑order modulus \tilde{Y}_x^c using the formulas in the same section.
- Evidence: none

### Step 3: Au (110) thin film construction and normal/parallel relaxation
- Role: process
- Action: Build slab models with (110) surfaces at several thicknesses, including a reference thickness of 3 nm. Perform dimension‑conserved normal relaxation, dimension‑changed normal relaxation, and parallel relaxation to obtain the relaxed configurations and the relaxation‑induced initial in‑plane strains.
- Evidence: `/app/outputs/relaxed_film_data.csv`

### Step 4: Surface property extraction via force balance
- Role: process
- Action: Apply in‑plane strain modes to the relaxed films of different thicknesses. For each mode and thickness, compute the core force from bulk elastic constants and measured in‑plane strains, then fit the force‑balance equations to extract the surface eigenstress σ_x^s0, surface first‑order Young's modulus Y_x^s, and second‑order modulus \tilde{Y}_x^s for the (110) surface.
- Evidence: `/app/outputs/surface_fit_report.txt`

### Step 5: Compile extracted parameters, compute scaling‑law modulus, and perform direct tension test
- Role: scored (load-bearing)
- Action: Using the core moduli from step s2 and the surface parameters from step s4, compute the nominal Young's modulus at h = 3 nm via the nonlinear scaling law given in the Required equations section. Separately, perform a direct pseudo‑uniaxial MD tension test (fixed y dimension) on the relaxed 3 nm (110) film to obtain the nominal Young's modulus. Assemble all results — bulk SOEC/TOEC, core moduli, surface parameters, the scaling‑law modulus, and the direct test modulus — into the JSON output file.
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
- description: The scored artifact containing MD-derived bulk and surface elastic constants, and the nominal Young's moduli from the scaling law and direct tension test.
- schema:
  - `type`: object
  - `required`:
    - `bulk_soec`: array of 3 floats (GPa)
    - `bulk_toec`: array of 6 floats (GPa)
    - `core_young_modulus_x`: float (GPa)
    - `core_young_modulus_2nd_x`: float (GPa)
    - `surface_young_modulus_x`: float (N/m)
    - `surface_young_modulus_2nd_x`: float (N/m)
    - `surface_eigenstress_x`: float (N/m)
    - `Y_n_direct_3nm`: float (GPa)
    - `Y_n_scaling_3nm`: float (GPa)

Notes: The checker recomputes the scaling-law modulus from the submitted core and surface parameters and verifies self-consistency; it compares all submitted values against hidden paper-reported references.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "/app/outputs/extracted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "bulk_soec": "array of 3 floats (GPa)",
          "bulk_toec": "array of 6 floats (GPa)",
          "core_young_modulus_x": "float (GPa)",
          "core_young_modulus_2nd_x": "float (GPa)",
          "surface_young_modulus_x": "float (N/m)",
          "surface_young_modulus_2nd_x": "float (N/m)",
          "surface_eigenstress_x": "float (N/m)",
          "Y_n_direct_3nm": "float (GPa)",
          "Y_n_scaling_3nm": "float (GPa)"
        }
      },
      "description": "The scored artifact containing MD-derived bulk and surface elastic constants, and the nominal Young's moduli from the scaling law and direct tension test."
    }
  ],
  "notes": "The checker recomputes the scaling-law modulus from the submitted core and surface parameters and verifies self-consistency; it compares all submitted values against hidden paper-reported references."
}
```

## How you are scored
An automated verifier reads `/app/outputs/extracted_parameters.json` and scores your submission as follows:
- Each reported elastic constant and modulus is compared to reference values obtained from the same simulation protocol with appropriate numerical tolerances.
- The verifier recomputes the nominal Young's modulus at 3 nm from the submitted core and surface parameters via the scaling-law equation and checks that it matches your submitted `Y_n_scaling_3nm` within a very small tolerance (self-consistency).
- Additional sanity checks may be applied to ensure the reported values are physically plausible.
The final reward is a weighted sum of these checks, with the bulk elastic constants, surface parameters, and the direct tension modulus receiving the highest weight. Reporting the expected numbers without genuine execution of the MD workflow will not produce correct submissions because the tolerances require physically consistent values.
