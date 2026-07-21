# Multi-Scale Modeling of Elastic Properties of Nanoparticle/Polymer Composites

## Problem background
Nanoparticle‑reinforced polyimide composites are candidates for lightweight structural materials. Their bulk elastic stiffness depends on nanoscale features, particularly the molecular structure and density of the polymer region adjacent to the nanoparticle surface. Capturing how interfacial treatments and particle size influence the overall mechanical response, and whether a continuum model with an effective interface can bridge molecular simulations and macroscopic predictions, is a challenging multi‑scale problem. This work implements a quantitative pipeline that combines molecular modeling and continuum micromechanics to investigate this size‑ and interface‑dependent behaviour of silica nanoparticle/polyimide composites.

## MD elastic constants (input data)
The table below lists the Young’s and shear moduli obtained from atomistic molecular dynamics simulations on six material systems. These values serve as the primary input for all subsequent micromechanics models. **You must use these exact numbers exactly as given.**

| system                     | E (GPa) | G (GPa) |
|----------------------------|---------|---------|
| silica                     | 88.7    | 41.0    |
| polyimide                  | 4.2     | 1.5     |
| silica_composite           | 3.4     | 1.2     |
| hydroxylated_composite     | 3.3     | 1.2     |
| phenoxybenzene_composite   | 2.2     | 0.8     |
| functionalized_composite   | 4.0     | 1.5     |

The MD simulations were performed on atomistic RVEs with the following protocol (for reference only):
- **Force field:** CVFF (ffcvff2.cff), as distributed with LAMMPS.
- **Molecular system:** BPDA/APB polyimide, 7 chains each containing 10 repeat units; silica nanoparticle with an α‑quartz core of radius 6 Å.
- **Box size:** originally cubic ∼42 Å, refined to 37.6–39.9 Å by constant‑pressure MD.
- **Equilibration:** 200 ps NPT MD at 300 K and 1 atm, time step 1 fs, Nosé–Hoover thermostat and barostat.
- **Elastic constants:** calculated via the static‑deformation energy‑difference method; small uniaxial (ε = ±0.003) and pure shear (γ = ±0.003) deformations were applied and the system was energy‑minimised after each deformation; C₁₁ and C₁₂ were extracted from the quadratic energy profiles and isotropic E and G were derived.

## Micromechanics models (complete description)

All calculations assume linear‑elastic isotropic behaviour. Stiffness matrices are expressed in standard Voigt notation (6‑component).

### Mori–Tanaka two‑phase model
For a matrix with stiffness **C**ₘ, spherical inclusions with stiffness **C**ₚ, and particle volume fraction cₚ, the effective stiffness **C**ₑ is given by

\[
\begin{aligned}
\mathbf{C}_{\text{eff}} &= (c_m\mathbf{C}_m + c_p\mathbf{C}_p\mathbf{T}_p)\,(c_m\mathbf{I} + c_p\mathbf{T}_p)^{-1}, \\
\mathbf{T}_p &= [\mathbf{I} + \mathbf{S}\,\mathbf{C}_m^{-1}(\mathbf{C}_p - \mathbf{C}_m)]^{-1},
\end{aligned}
\tag{1}
\]

where \(c_m = 1 - c_p\) and **S** is the Eshelby tensor for a spherical inclusion in an isotropic matrix with Poisson’s ratio νₘ:

\[
S_{1111} = \frac{7-5\nu_m}{15(1-\nu_m)},\quad
S_{1122} = \frac{5\nu_m-1}{15(1-\nu_m)},\quad
S_{1212} = \frac{4-5\nu_m}{15(1-\nu_m)}.
\tag{2}
\]

### Effective‑interface three‑phase model
The composite consists of three concentric spheres: a particle of radius \(r_p\) (stiffness **C**ₚ), an effective interface of uniform thickness \(t\) (stiffness **C**ᵢ), and the matrix (stiffness **C**ₘ). The total volume is determined by a prescribed particle volume fraction \(v_f^{\text{(given)}}\):

\[
V_{\text{particle}} = \frac{4}{3}\pi r_p^3,\qquad
V_{\text{total}} = \frac{V_{\text{particle}}}{v_f^{\text{(given)}}},\qquad
R = r_p + t.
\]

The volume fractions are

\[
v_f^p = v_f^{\text{(given)}},\qquad
v_f^i = \frac{\frac{4}{3}\pi(R^3 - r_p^3)}{V_{\text{total}}},\qquad
v_f^m = 1 - v_f^p - v_f^i \ (\ge 0).
\tag{3}
\]

The effective stiffness **C**ₑ is obtained through a two‑step homogenisation that combines the particle and the interface into an equivalent inclusion before embedding it in the matrix:

\[
\begin{aligned}
\mathbf{C}_{\text{eff}} &= \mathbf{C}_m + \bigl[(v_f^p+v_f^i)(\mathbf{C}_i-\mathbf{C}_m)\mathbf{T}_{pi} + v_f^p(\mathbf{C}_p-\mathbf{C}_i)\mathbf{T}_p\bigr]\,
\bigl[v_f^m\mathbf{I} + (v_f^p+v_f^i)\mathbf{T}_{pi}\bigr]^{-1}, \\
\mathbf{T}_{pi} &= \mathbf{I} - \mathbf{S}\Bigl(\frac{v_f^p}{v_f^p+v_f^i}[\mathbf{S}+(\mathbf{C}_p-\mathbf{C}_m)^{-1}\mathbf{C}_m]^{-1} +
\frac{v_f^i}{v_f^p+v_f^i}[\mathbf{S}+(\mathbf{C}_i-\mathbf{C}_m)^{-1}\mathbf{C}_m]^{-1}\Bigr), \\
\mathbf{T}_p &= \mathbf{I} - \mathbf{S}\,[\mathbf{S}+(\mathbf{C}_p-\mathbf{C}_m)^{-1}\mathbf{C}_m]^{-1}.
\end{aligned}
\tag{4}
\]

Here **S** is the same Eshelby tensor (Eq. 2), computed with the matrix Poisson’s ratio νₘ. After evaluating **C**ₑ, the effective Young’s modulus \(E\) and shear modulus \(G\) are extracted in the usual way:

\[
K = \frac{C_{11}+2C_{12}}{3},\qquad
G = C_{44},\qquad
E = \frac{9KG}{3K+G}.
\tag{5}
\]

### Solving for the interface properties
Given **C**ₚ, **C**ₘ, and the MD composite stiffness **C**_{MD}, together with the geometry \((r_p, t, v_f^{\text{(given)}})\) and an assumed interface Poisson’s ratio νᵢ = 0.4, the two unknown interface constants \(E_i\) and \(G_i\) are determined by requiring that the effective‑interface model predicts exactly **C**_{MD}. In practice, this is a two‑variable root‑finding problem:

\[
\min_{E_i,G_i} \bigl\| \mathbf{C}_{\text{eff}}(E_i,G_i) - \mathbf{C}_{MD} \bigr\|,
\tag{6}
\]

where the norm is evaluated on the independent stiffness components (e.g. \(C_{11}\) and \(C_{12}\)). The solution must satisfy \(E_i>0,\ G_i>0\). For the RVE geometry used in the paper, \(r_p = 6\) Å, \(t = 12\) Å, and \(v_f^{\text{(given)}} = 0.017\). You must solve this problem numerically for each of the four composite types.

### Radius‑dependent predictions
To study the size effect, the particle inner radius \(r_p\) is varied while keeping the interface thickness fixed at \(t = 12\) Å and the particle volume fraction fixed at \(v_f^{\text{(given)}} = 0.05\). For each chosen \(r_p\), the interface volume fraction \(v_f^i\) is recomputed according to Eq. 3. The effective‑interface model (Eq. 4) then yields the composite moduli using the interface properties obtained at the RVE scale. The Mori–Tanaka prediction is also evaluated at the same 5 % volume fraction (it is independent of particle radius). These calculations should be performed for a set of at least 10 logarithmically spaced radii between 10 Å and 10 000 Å (for example, generated by `np.logspace(1,4, 15)`).

## Workflow steps

### Step 1: Output the MD elastic constants
- Role: scored
- Action: Write the elastic constants from the table above to a CSV file.
- Output file: `/app/outputs/elastic_constants_systems.csv`
- Format: csv
- Contract: columns: system, E, G (one row per system, exactly six rows, values in GPa). The six systems are: `silica`, `polyimide`, `silica_composite`, `hydroxylated_composite`, `phenoxybenzene_composite`, `functionalized_composite`. Use the exact numeric values shown in the table.

### Step 2: Mori–Tanaka predictions at the RVE volume fraction
- Role: scored
- Action: Using the pure silica and polyimide elastic constants, apply the Mori–Tanaka two‑phase model (Eq. 1) with \(c_p = 0.017\) and the Eshelby tensor for spherical inclusions (Eq. 2) to compute the composite Young’s and shear moduli. Save the results.
- Output file: `/app/outputs/mori_tanaka_rve.csv`
- Format: csv
- Contract: columns: composite, E_MT, G_MT (four rows, `composite` identical to the names: `silica_composite`, `hydroxylated_composite`, `phenoxybenzene_composite`, `functionalized_composite`).

### Step 3: Determine effective interface elastic properties
- Role: scored
- Action: For each composite, take the MD composite moduli (from the table in Step 1) and the pure silica and polyimide constants. With \(r_p = 6\) Å, \(t = 12\) Å, \(v_f^{\text{(given)}}=0.017\), and νᵢ = 0.4, solve Eq. 6 to find the isotropic interface Young’s modulus \(E_i\) and shear modulus \(G_i\). Store the results.
- Output file: `/app/outputs/effective_interface_properties.csv`
- Format: csv
- Contract: columns: composite_type, E_interface, G_interface (four rows, `composite_type` naming as above).

### Step 4: Radius‑dependent composite moduli (effective‑interface and Mori–Tanaka)
- Role: scored (load‑bearing)
- Action: For each composite type, compute the composite Young’s modulus \(E\) and shear modulus \(G\) at a fixed particle volume fraction of 5 % for at least 10 logarithmically spaced radii between 10 Å and 10 000 Å. Use the effective‑interface model (Eq. 4) with \(t = 12\) Å and the interface properties determined in Step 3. Also compute the constant Mori–Tanaka predictions (Eq. 1) at each radius using the pure phase constants. Combine both model types in a single CSV.
- Output file: `/app/outputs/moduli_vs_radius.csv`
- Format: csv
- Contract: columns: composite_type, radius_A, model_type, E, G. `model_type` is either `Mori-Tanaka` or `Effective-Interface`. Each composite must have at least 20 rows (10 radii × 2 models). Radii must be logarithmically spaced.

All moduli are in GPa; radii in Å.

## How you are scored
A hidden verifier independently examines each scored output file. For Step 1 it compares your submitted values against the reference table above. For all subsequent steps it performs a **self-consistency** check:
- It recomputes the Mori–Tanaka predictions from the pure silica and polyimide constants you submitted.
- It verifies that the interface properties you report, when inserted into the effective‑interface model, reproduce the MD composite moduli you listed in Step 1.
- It recomputes the radius‑dependent effective‑interface curves using the pure phase constants and the interface properties you submitted, and checks that they match your submitted curves (within 1 %).
- It also verifies that Mori–Tanaka curves are correct relative to the pure phase constants, and that physical trends (monotonic increase, convergence at large radii, expected ordering among composites) are satisfied.

There is no reliance on pre‑loaded hidden gold data; the verifier only uses the reference table for Step 1 and the physical models described in this instruction.

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, and CSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness.

```json
{
  "outputs": [
    {
      "file": "elastic_constants_systems.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": ["system", "E", "G"],
        "units": {"E": "GPa", "G": "GPa"}
      },
      "description": "MD-derived Young's (E) and shear (G) moduli for the six material systems."
    },
    {
      "file": "mori_tanaka_rve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": ["composite", "E_MT", "G_MT"],
        "units": {"E_MT": "GPa", "G_MT": "GPa"}
      },
      "description": "Mori–Tanaka predicted composite moduli at the RVE volume fraction."
    },
    {
      "file": "effective_interface_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": ["composite_type", "E_interface", "G_interface"],
        "units": {"E_interface": "GPa", "G_interface": "GPa"}
      },
      "description": "Effective interface Young's and shear moduli for each composite."
    },
    {
      "file": "moduli_vs_radius.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": ["composite_type", "radius_A", "model_type", "E", "G"],
        "units": {"radius_A": "Å", "E": "GPa", "G": "GPa"}
      },
      "description": "Radius-dependent composite moduli from both effective-interface and Mori–Tanaka models; checker recomputes effective-interface curves for consistency."
    }
  ],
  "notes": "All moduli are in GPa. Radii in Å. The effective-interface model curves will be recomputed from the submitted interface properties and pure phase constants; internal consistency (within 1%) is required."
}
```