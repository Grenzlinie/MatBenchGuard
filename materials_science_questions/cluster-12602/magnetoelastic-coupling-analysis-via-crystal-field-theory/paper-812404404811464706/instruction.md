# Magnetostrictive energy‑minimization model for epitaxial Dy films

## Problem background
Bulk hexagonal dysprosium exhibits a helical antiferromagnetic order below \(T_{\mathrm{N}}=176\,\text{K}\) and a helical‑to‑ferromagnetic transition at a Curie temperature \(T_{\mathrm{C}}=89\,\text{K}\), driven by magnetostrictive effects. Epitaxial growth of Dy films on substrates with different lattice parameters introduces a measurable \(c\)‑axis strain \(\varepsilon_{33}\) that can shift the Curie temperature. The goal is to compute the Curie temperature of an epitaxial dysprosium film as a function of the \(c\)‑axis strain \(\varepsilon_{33}\) using a magnetostrictive total‑energy model.

## Model equations (to be implemented)
All energies are expressed as volumetric densities (energy per unit volume).  
The model considers three symmetry‑adapted strains in the basal plane:

\[
\varepsilon_{\alpha 1} = \varepsilon_{11} + \varepsilon_{22},\qquad
\varepsilon_{\alpha 2} = \varepsilon_{11} - \varepsilon_{22},\qquad
\varepsilon_{\gamma}  = \varepsilon_{12},
\]

where \(\varepsilon_{ij}\) are the components of the small‑strain tensor in hexagonal axes.

The total energy of the system includes elastic, magnetoelastic, and exchange contributions.

### 1. Elastic energy density
For a hexagonal crystal the elastic energy density (Voigt notation) is

\[
E_{\mathrm{el}} = \frac{1}{2}C_{11}(\varepsilon_{11}^2+\varepsilon_{22}^2) + C_{12}\varepsilon_{11}\varepsilon_{22}
+ C_{13}(\varepsilon_{11}+\varepsilon_{22})\varepsilon_{33} + \frac{1}{2}C_{33}\varepsilon_{33}^2
+ 2C_{44}(\varepsilon_{13}^2+\varepsilon_{23}^2) + 2C_{66}\varepsilon_{12}^2 .
\]

Using the symmetry‑adapted strains and setting \(\varepsilon_{13}=\varepsilon_{23}=0\) (no out‑of‑plane shears), this becomes

\[
E_{\mathrm{el}} = B_{1}\,\varepsilon_{\alpha 1}^{2} + B_{2}\,\varepsilon_{\alpha 2}^{2}
+ C_{13}\,\varepsilon_{\alpha 1}\varepsilon_{33} + \frac{1}{2}C_{33}\,\varepsilon_{33}^{2}
+ B_{\gamma}\,\varepsilon_{\gamma}^{2},
\]

where the effective constants are

\[
B_{1} = \frac{C_{11}+C_{12}}{4},\qquad
B_{2} = \frac{C_{11}-C_{12}}{4},\qquad
B_{\gamma} = 2C_{66}.
\]

For simplicity, the elastic energy of the clamping layers (Y or Er) is neglected; it can be absorbed into an effective calibration of the magnetostriction constants without affecting the qualitative trend required here.

### 2. Magnetoelastic energy
The coupling between the magnetic order and the symmetry strains is taken to first order in the strains.
*In the ferromagnetic state* the magnetisation is along the easy \(a\)‑axis; the three symmetry strains are all active:

\[
E_{\mathrm{me}}^{\mathrm{FM}} = -\,f(T)\,\bigl[ M_{\alpha 1}\,\varepsilon_{\alpha 1} + M_{\alpha 2}\,\varepsilon_{\alpha 2} + M_{\gamma}\,\varepsilon_{\gamma} \bigr].
\]

*In the helical state* the magnetisation rotates in the basal plane and the average over one pitch eliminates the coupling to \(\varepsilon_{\alpha 2}\) and \(\varepsilon_{\gamma}\):

\[
E_{\mathrm{me}}^{\mathrm{hel}} = -\,f_{\mathrm{hel}}(T)\, M_{\alpha 1}^{\mathrm{hel}}\,\varepsilon_{\alpha 1}.
\]

The coefficients \(M_{\alpha 1}, M_{\alpha 2}, M_{\gamma}\) and \(M_{\alpha 1}^{\mathrm{hel}}\) are the magnetostriction constants that must be calibrated. The temperature factor is approximated by the square of the reduced magnetisation:

\[
f(T) = \bigl[m(T)\bigr]^{2},\qquad
m(T) = \frac{M(T)}{M(0)},
\]

and similarly for \(f_{\mathrm{hel}}(T)\). The reduced magnetisation of Dy can be obtained from published experimental data (e.g., Behrendt et al., Phys. Rev. **109**, 1544 (1958)) or from a simple parameterisation such as

\[
m(T) \approx \bigl[1-(T/T_{\mathrm{N}})^{2}\bigr]^{1/3},\qquad
T_{\mathrm{N}}=176\ \text{K}.
\]

### 3. Exchange energy barrier
The exchange energy difference between the helical and ferromagnetic states, \(\Delta E_{\mathrm{ex}}\), is evaluated with the classical three‑planes model (Enz, J. Appl. Phys. **32**, 225 (1961)). Let \(J_1, J_2, J_3\) be the exchange integrals between nearest, next‑nearest, and third‑nearest basal planes. For a helix of turn angle \(\omega\), the exchange energy per volume (relative to an arbitrary constant) is

\[
E_{\mathrm{ex}}(\omega) = -2S^{2}\bigl[J_1\cos\omega + J_2\cos 2\omega + J_3\cos 3\omega\bigr].
\]

The equilibrium helix angle \(\omega_0(T)\) minimises this expression, satisfying

\[
J_1\sin\omega_0 + 2J_2\sin 2\omega_0 + 3J_3\sin 3\omega_0 = 0 .
\]

The ferromagnetic state corresponds to \(\omega=0\). The exchange barrier that the magnetostrictive energy must overcome is

\[
\Delta E_{\mathrm{ex}}(T) = E_{\mathrm{ex}}\bigl(\omega_0(T)\bigr) - E_{\mathrm{ex}}(0).
\]

The exchange integrals themselves depend on temperature. It is sufficient to assume the scaling

\[
J_i(T) = J_i(0) \; m(T)^{2},
\]

which makes \(\omega_0\) temperature‑independent. The values of \(J_1(0), J_2(0), J_3(0)\) must be taken from the literature (e.g., the Enz reference). Suitable values (in meV) are \(J_1(0) \approx 0.30\), \(J_2(0) \approx 0.18\), \(J_3(0) \approx 0.06\).

### 4. Total energy and minimisation
For a given \(c\)‑axis strain \(\varepsilon_{33}\) and temperature \(T\),

\[
E_{\mathrm{FM}}(\varepsilon_{\alpha 1},\varepsilon_{\alpha 2},\varepsilon_{\gamma}; T) =
E_{\mathrm{el}} + E_{\mathrm{me}}^{\mathrm{FM}} + E_{\mathrm{ex}}(0),
\]

\[
E_{\mathrm{hel}}(\varepsilon_{\alpha 1},\varepsilon_{\alpha 2},\varepsilon_{\gamma}; T) =
E_{\mathrm{el}} + E_{\mathrm{me}}^{\mathrm{hel}} + E_{\mathrm{ex}}\bigl(\omega_0(T)\bigr).
\]

The exchange term shifts both states by the same constant; only the difference \(\Delta E_{\mathrm{ex}}\) matters. Therefore one can work with the relative energies

\[
\mathcal{E}_{\mathrm{FM}} = E_{\mathrm{el}} + E_{\mathrm{me}}^{\mathrm{FM}},\qquad
\mathcal{E}_{\mathrm{hel}} = E_{\mathrm{el}} + E_{\mathrm{me}}^{\mathrm{hel}} + \Delta E_{\mathrm{ex}} .
\]

At each temperature, both \(\mathcal{E}_{\mathrm{FM}}\) and \(\mathcal{E}_{\mathrm{hel}}\) are minimised with respect to the free symmetry strains \(\varepsilon_{\alpha 1}, \varepsilon_{\alpha 2}, \varepsilon_{\gamma}\) (subject to the fixed \(\varepsilon_{33}\)). The minimisation can be performed analytically or numerically. The Curie temperature \(T_{\mathrm{C}}\) for a given \(\varepsilon_{33}\) is the temperature at which the minimum of \(\mathcal{E}_{\mathrm{FM}}\) falls below the minimum of \(\mathcal{E}_{\mathrm{hel}}\).

## Implementation steps

### Step 1: obtain material data
Extract the elastic constants \(C_{11}, C_{12}, C_{13}, C_{33}, C_{66}\) of Dy from the literature (e.g., Behrendt et al., Phys. Rev. **109**, 1544 (1958) and subsequent compilations). Typical values are \(C_{11}\approx 74.6\) GPa, \(C_{12}\approx 27.6\) GPa, \(C_{13}\approx 20.5\) GPa, \(C_{33}\approx 62.6\) GPa, \(C_{66}\approx 23.5\) GPa. Obtain the exchange integrals \(J_1, J_2, J_3\) at zero temperature from Enz, J. Appl. Phys. **32**, 225 (1961) – typical values are given above. Adopt a parameterisation for the reduced magnetisation \(m(T)\) (see Section 2).

### Step 2: calibrate magnetostriction constants
Set \(\varepsilon_{33}=0\) (bulk condition). Using the energy expressions above, treat the magnetostriction constants \(M_{\alpha 1}, M_{\alpha 2}, M_{\gamma}, M_{\alpha 1}^{\mathrm{hel}}\) (in energy‑density units) as adjustable parameters. Adjust them within physically reasonable ranges so that the computed Curie temperature matches the known bulk Curie temperature of dysprosium. Reasonable starting ranges (in GPa) are \(|M_{\alpha 1}| \sim 0.05\)–\(0.5\), \(|M_{\alpha 2}| \sim 0.1\)–\(1\), \(|M_{\gamma}| \sim 0.1\)–\(1\). The sign of the constants is such that the energy is lowered in the ferromagnetic state. The calibration may be done by a simple grid search or a few manual trials.

### Step 3: compute \(T_{\mathrm{C}}\) vs \(\varepsilon_{33}\) – **scored**
With the calibrated magnetostriction constants, for a set of \(c\)‑axis strain values covering at least \(\varepsilon_{33} \in [-0.005, 0.005]\) (corresponding to \(-0.5\%\) to \(+0.5\%\)), perform for each strain the temperature scan and energy minimisation described above. Determine \(T_{\mathrm{C}}\) as the temperature where \(\min\mathcal{E}_{\mathrm{FM}}\) becomes lower than \(\min\mathcal{E}_{\mathrm{hel}}\). Output a list of \((\varepsilon_{33}, T_{\mathrm{C}})\) pairs.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tc_vs_strain.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tc_vs_strain.json
- path: `/app/outputs/tc_vs_strain.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Computed Tc vs ε33 data; verified by structural consistency checks.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `epsilon33`, `Tc`
    - `properties`:
      - `epsilon33`:
        - `type`: number
        - `description`: c‑axis epitaxial strain (dimensionless, e.g. −0.005 to +0.005)
      - `Tc`:
        - `type`: number
        - `units`: K
        - `description`: Calculated Curie temperature

Notes: The model may be run for either Y or Er clamping layers; the trend is independent of the choice.

## Self‑check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tc_vs_strain.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "epsilon33",
            "Tc"
          ],
          "properties": {
            "epsilon33": {
              "type": "number",
              "description": "c‑axis epitaxial strain (dimensionless, e.g. −0.005 to +0.005)"
            },
            "Tc": {
              "type": "number",
              "units": "K",
              "description": "Calculated Curie temperature"
            }
          }
        }
      },
      "description": "Computed Tc vs ε33 data; verified by structural consistency checks."
    }
  ],
  "notes": "The model may be run for either Y or Er clamping layers; the trend is independent of the choice."
}
```

## How you are scored
A hidden verifier inspects the final artifact `tc_vs_strain.json`. It checks the structure of the list (minimum number of points, strain range covered, data types) and evaluates the physical consistency of the computed trend. The exact scoring criteria and thresholds are not disclosed.