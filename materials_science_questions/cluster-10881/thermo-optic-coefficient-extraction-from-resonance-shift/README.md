# Thermo-Optic Coefficient Extraction from Resonance Shift

## Common Computational Pattern

The workflow family derives the thermo‑optic coefficient \( dn/dT \) of optical materials (bulk or waveguide) by analyzing the temperature‑dependent shift of a resonance wavelength (e.g., Bragg, whispering‑gallery mode, or interferometer fringe). The core computational pipeline is:

1. **Data acquisition:** Obtain the resonance wavelength \( \lambda_{\mathrm{res}} \) as a function of temperature from experimental measurements or simulations.
2. **Extract group/effective index:** For guided‑wave configurations, calculate the group index \( n_g \) from the fringe period \( \Delta\lambda \) or known waveguide dispersion. For bulk resonators, use the mode volume and known dispersion.
3. **Convert shift to effective index change:** Apply the relation  
   \[
   \frac{dn_{\mathrm{eff}}}{dT} = \frac{n_g}{\lambda}\frac{d\lambda}{dT}
   \]
   (common for interferometric and grating‑based methods) or the analogous formula  
   \[
   \Delta\lambda = \frac{\lambda_0}{n_0}\frac{dn}{dT}\Delta T
   \]
   for cavity‑based measurements.
4. **Relate effective to material \( dn/dT \):** Use an electromagnetic mode solver (e.g., finite‑element method, transfer matrix, analytical eigenmode expansion) to compute the mode effective index \( n_{\mathrm{eff}} \) as a function of the material refractive index \( n_{\mathrm{mat}} \). From this, derive the sensitivity \( dn_{\mathrm{eff}}/dn_{\mathrm{mat}} \) to map the extracted \( dn_{\mathrm{eff}}/dT \) to the intrinsic \( dn_{\mathrm{mat}}/dT \).
5. **Verification:** Compare the final \( dn/dT \) value(s) with literature data or temperature‑dependent refractive‑index models (Sellmeier, Drude) to confirm reproducibility within a specified tolerance.

## Typical Resources

- **Input data:** Temperature‑resolved spectral scans (wavelength vs. temperature), waveguide/device geometry (core size, cladding parameters), material dispersion curves (Sellmeier coefficients, Drude parameters).
- **Numerical tools:** Python, MATLAB, or Jupyter notebooks for data processing and fitting; COMSOL Multiphysics or custom FEM codes for modal analysis and heat‑flow simulations; semi‑analytical eigenmode calculators (scalar/vector).
- **Material models:** Temperature‑dependent Sellmeier equations, Drude models for metals, thermal expansion coefficients, photo‑elastic constants.

## Verification Style

The workflow is **dry‑lab and numeric**. Verification consists of comparing the extracted \( dn/dT \) against established reference values (from handbooks, prior peer‑reviewed measurements) or against predictions from accepted temperature‑dependent refractive‑index models. A tolerance band (e.g., < 2 % for steady‑state cases, within experimental uncertainty) determines successful reproducibility.

## Repository Layout

Each subdirectory (`paper‑*`) corresponds to a self‑contained Harbor task. The entry point is `instruction.md`, which describes the specific steps, required inputs, and expected outputs for that paper’s extraction.
