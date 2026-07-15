# First-Principles Resonant Raman Calculation

## Overview
This workflow family covers the first‑principles prediction of resonant Raman scattering intensities using density functional theory (DFT) for electronic structure, density functional perturbation theory (DFPT) or electron‑phonon Wannier (EPW) methods for electron‑phonon matrix elements, and sum‑over‑states expressions with resonant denominators and phenomenological broadening. The calculations produce laser‑energy‑dependent Raman excitation profiles (REPs) and full spectra that can be directly compared with experiment.

The family spans materials from molecules to extended solids (semiconductors, 2D crystals, correlated systems, etc.) and handles both resonant and non‑resonant regimes, often including many‑body corrections (GW, Bethe‑Salpeter equation) to capture excitonic effects.

## Main Computational Pattern
The common computational workflow consists of the following steps:

1. **Structural optimisation and electronic structure**  
   A ground‑state DFT calculation (typically LDA or other functionals) provides the electronic band structure, charge density, and Kohn‑Sham eigenvalues. Spin‑orbit coupling and relativistic corrections are included when necessary (e.g., for heavy elements).

2. **Lattice dynamics**  
   Phonon frequencies and eigenvectors at the Γ point are obtained via DFPT. This yields the normal‑mode displacements and the phonon densities needed for Raman‑activity selection rules.

3. **Electron‑phonon matrix elements**  
   The derivative of the Kohn‑Sham Hamiltonian with respect to atomic displacements is computed, either through DFPT, frozen‑phonon finite differences, or the EPW method. These matrix elements describe how the electronic states couple to the lattice vibrations.

4. **Resonant Raman response**  
   The Raman susceptibility tensor $\alpha_{\mu}(\omega)$ for phonon mode $\mu$ is obtained either by:
   - **Finite‑difference approach:** calculating the dielectric susceptibility $\chi(\omega)$ at two displaced geometries along the phonon eigenvector and differentiating,
   - **Perturbative sum‑over‑states approach:** evaluating the Albrecht‑type formula,
     $$
     \alpha_{\rm pert.} \propto \sum_{S,S'} \frac{\langle 0|\mathbf{r}|S'\rangle \langle S'|\partial H|S\rangle \langle S|\mathbf{r}|0\rangle}{(\omega_{S'}-\omega-i\gamma)(\omega_{S}-\omega-i\gamma)},
     $$
     where $|S\rangle, |S'\rangle$ are electronic excitations (single‑particle or excitonic), $\omega$ is the incident laser frequency, $\gamma$ is a phenomenological broadening, and $\partial H$ is the electron‑phonon coupling.

   Many‑body corrections are often applied: a **scissor operator** (or explicit $G_0W_0$ corrections) adjusts the band gap, and the **Bethe‑Salpeter equation (BSE)** is solved to include excitonic effects, replacing the independent‑particle states with exciton eigenstates in the sum‑over‑states formula.

5. **Raman intensity/spectrum**  
   The Stokes Raman intensity for a given excitation energy $\omega_L$, polarization configuration, and phonon mode $\mu$ is computed as
   $$
   I(\omega_L) \propto (\omega_L-\omega_\mu)^4 \big| (\vec{e}_S)^\dagger \alpha_\mu(\omega_L) (\vec{e}_L) \big|^2 \frac{n_\mu+1}{2\omega_\mu},
   $$
   where $\vec{e}_L$ and $\vec{e}_S$ are the incident and scattered polarizations, $\omega_\mu$ is the phonon frequency, and $n_\mu$ the Bose factor.

   Spectra are typically convolved with a broader Gaussian or Lorentzian to mimic experimental resolution.

## Typical Resources
- **Electronic‑structure codes:** DFT implementations such as Quantum ESPRESSO, VASP, SIESTA, or full‑potential LMTO (as used in several provided papers).
- **Phonon & electron‑phonon calculations:** DFPT as implemented in the DFT codes, or the EPW code for Wannier‑interpolated e‑ph coupling.
- **Many‑body corrections:** Yambo, BerkeleyGW, or internal routines for GW and BSE.
- **Raman post‑processing:** Custom scripts that perform the finite‑difference or sum‑over‑states evaluation, often using output databases (e.g., `pwy` files) from DFPT.

*Note:* The exact tools depend on the specific paper; the family leverages standard first‑principles software in the community.

## Verification
Results are validated by **quantitative comparison with experimental resonant Raman spectra**:
- Peak positions, relative intensities, and resonance profiles (Raman excitation profiles) are matched against measured data.
- For systems with multiple electronic resonances, the calculated enhancement patterns (e.g., selective enhancement of certain phonon modes by specific excitons) are directly compared to wavelength‑dependent Raman experiments.
- Discrepancies often highlight the need for improved broadening parameters or missing many‑body effects (e.g., exciton‑phonon coupling).

This verify‑against‑experiment style is consistent across the family, as indicated by the `verify_type: experiment` in the workflow definition.

## Paper Tasks
Each `paper-*` subdirectory in this workflow family is a standalone Harbor task. The public instruction file is `instruction.md` (not TASK.md). These instructions detail the specific inputs, parameters, and expected outputs for reproducing the calculations of that particular paper.
