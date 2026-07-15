# Compton Profile Analysis for Electron Momentum Density

This workflow family covers the computation, correction, and interpretation of Compton profiles—one-dimensional projections of the electron momentum density—for materials ranging from metals and semiconductors to molecular crystals and liquid solutions. The profiles are obtained either via theoretical electronic structure calculations or from experimental measurements (gamma‑ray or synchrotron Compton scattering). The family includes 155 tasks across 57 papers, all of which are **dry‑lab** (computationally reproducible) and are verified using **numeric** comparisons against reference data or experimental results.

## Common Computational Pattern

A typical task in this family follows a sequence:

1. **Obtain electronic structure** – Compute the ground‑state wavefunctions and energies using a chosen method (DFT, Hartree–Fock, SAPW, FP‑LAPW, SPR‑KKR, LCAO, or quantum Monte Carlo).
2. **Construct momentum‑space density** – Transform real‑space orbitals to momentum space to obtain the electron momentum distribution $n(\mathbf{p})$.
3. **Calculate Compton profiles** – Integrate $n(\mathbf{p})$ over planes perpendicular to a direction $\hat{\mathbf{q}}$ to produce the directional Compton profile $J(p_z)$ within the impulse approximation:
   $$
   J(\hat{\mathbf{q}},p_z) = \iint n(\mathbf{p})\,\mathrm{d}p_x\,\mathrm{d}p_y
   $$
4. **Apply corrections** – Incorporate physical effects that refine the profile:
   - **Pauli exclusion corrections** for metals and semiconductors (band‑occupancy factors).
   - **Finite‑size and k‑point convergence** using reference‑based smoothing (LDA‑scaled QMC).
   - **Angular and energy resolution** convolutions (Gaussian broadening) for direct comparison with experiment.
   - **Geometrical deconvolution** from experimental photon‑beam apertures.
5. **Extract properties** – Derive quantities such as directional anisotropies, $J(0)$ surfaces, bond‑oscillation signatures, hydration structure, and charge‑transfer effects.

## Key Resources and Methods

The tasks draw on a variety of computational approaches. The following are explicitly named in the provided context:

- **Electronic‑structure codes**: CRYSTAL (linear combination of atomic orbitals), Wien2k (FP‑LAPW), SPR‑KKR.
- **Theoretical frameworks**: Density functional theory with LDA and GGA functionals (PBE, Perdew–Burke–Ernzerhof), Hartree–Fock, hybrid B3LYP, symmetrised augmented plane wave (SAPW), quantum Monte Carlo (QMC).
- **Correction models**: Free‑electron sphere overlap for Pauli exclusion in semiconductors, linear‑tetrahedron integration for QMC Compton profiles, Monte‑Carlo simulation for beam‑aperture response functions.
- **Data tools**: Scipy (minimization of cost functions), GEANT3 (detector‑response simulation).

Each individual task is packaged as a self‑contained Harbor task inside a `paper‑*` subdirectory; the required resources and dependencies are specified in its `instruction.md` file.

## Verification Style

The family uses **numeric verification** with a tolerance‑based alignment. Theoretical and experimental Compton profiles are compared via metrics such as:

- Mean percentage deviation.
- $\chi^2$ (sum of squared differences weighted by variances).
- Normalization errors.
- Agreement after resolution convolution (Gaussian FWHM).

For tasks that involve corrections to the impulse approximation, the corrected profile must reproduce reference data (e.g., experimental Compton profiles from synchrotron measurements) within a pre‑defined tolerance. In all cases, the verification note in the cluster metadata explicitly states that numeric metrics are used, which guarantees that each tasks solution can be assessed automatically by comparing computed profiles with reference datasets.

## Representative Outcomes

- Band‑occupancy corrections for intrinsic semiconductors (Si) that eliminate low‑angle discrepancies.
- Size‑converged QMC Compton profiles of solid Li using an $\alpha$‑scaled LDA reference and tetrahedron integration.
- Good agreement between SAPW Ni$_3$Ga profiles and experiment after resolution convolution; remaining differences indicate the need for non‑muffin‑tin corrections.
- Bond‑oscillation principle applied to ion hydration, linking Compton profile modulations to hydration‑shell geometry and ion pairing.
- The $J(\mathbf{0})$ surface as a compact directional representation of momentum density in molecular crystals.
- Detector‑response correction for Compton line profiles using a Monte‑Carlo‑derived angular distribution function.
- Exact antisymmetric corrections to the impulse approximation via initial‑state operator expansions.
