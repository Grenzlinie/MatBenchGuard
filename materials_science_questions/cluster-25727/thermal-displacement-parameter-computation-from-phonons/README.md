# Thermal displacement parameter computation from phonons

This workflow family computes temperature-dependent atomic mean-square displacement
(and related Debye-Waller factors) for solids using various phonon models.
Common applications include the Mössbauer fraction, anisotropic temperature parameters,
isotropic and anisotropic hyperfine constants, thermal expansion, and Debye temperature.

## Main computational pattern

1. **Obtain phonon data**: For a given crystal, obtain the phonon dispersion
   (frequencies $\omega_{q,\lambda}$ and polarization vectors $\mathbf{e}_{q,\lambda}$)
   either from a dynamical matrix, elastic constants, a Debye continuum, or an
   empirical force-field.
2. **Select a vibrational model**: The same base quantity (mean-square displacement)
   can be computed within:
   - the harmonic lattice-dynamics Green’s function formalism (e.g., for impurity
     nuclei)
   - a Debye model with isotropic or anisotropic elastic constants
   - an Einstein model for local modes
   - the Mori projection‑operator formalism for reduced heatbaths
   - the Morse‑oscillator model for multiphonon processes
   - empirical pseudopotential methods with Debye–Waller attenuation.
3. **Evaluate the mode sum**: The mean-square displacement of an atom $r$ (or
   related quantity) is expressed as a sum/integral over phonon modes weighted by
   the Bose‑Einstein occupation,
   $$ \langle u_r^2 \rangle = \frac{\hbar}{2 m_r} \sum_{\mathbf{q},\lambda}
   \frac{|\mathbf{e}_{r}(\mathbf{q},\lambda)|^2}{\omega_{\mathbf{q},\lambda}}
   \coth\!\Bigl(\frac{\hbar\omega_{\mathbf{q},\lambda}}{2k_{\!B}T}\Bigr). $$
   In approximate models the sum is replaced by an integral over a model density of
   states or by an analytical closed form.
4. **Derive temperature‑dependent properties**:
   - **Debye‑Waller factors** $B_k$ or $f = e^{-2W}$
   - **Hyperfine constants** $A(T)$ and axial splitting $b_2^0(T)$ via orbit‑lattice coupling
   - **Thermal expansion / lattice constant shifts** from anharmonic coupling or
     electronic level rearrangement
   - **Debye or Einstein temperatures** $\Theta(T)$
   - **Soft‑mode potential parameters** from electronic‑structure calculations
     with Debye–Waller attenuation.

### Typical resources

- **Numerical inputs**: phonon dispersion curves, elastic constants $C_{ij}$,
  atomic form factors, Debye temperatures, tetrahedral radii.
- **Codes**: custom scripts implementing the formulas; often a mix of
  symbolic algebra and numerical integration is required.
- **Reference data**: experimental structural data, sublimation enthalpies,
  monatomic vapour entropies, etc.

## Verification

The results are verified **numerically**: the computed mean-square displacement,
Debye‑Waller factor, or derived property is compared with published experimental
or theoretical data, using percentage deviation or RMS error as the figure of
merit.

## Task organization

Each paper in the family lives in a subdirectory named `paper-<paper_id>`.  The
entry point is `instruction.md` (the Harbor task definition), which contains the
specific calculation to be implemented and verified.
