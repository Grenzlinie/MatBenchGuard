# Phonon Dispersion and Density of States Computation

## Overview
This workflow family encompasses computational protocols that calculate phonon dispersion curves and phonon density of states (DOS) for a given material using first‑principles or empirical atomistic methods. The primary outputs are the material’s vibrational frequencies (as functions of wave‑vector) and the corresponding density of vibrational states, which are then compared with experimental reference data (e.g., inelastic neutron scattering, Raman/IR spectroscopy, inelastic x‑ray scattering) to validate the model or predictions.

**Key characteristics:**
- **Dry‑lab** computational workflow – no experimental measurement is performed within the workflow itself; entire procedure relies on simulations.
- **Numeric verification** – the success of the workflow is judged by comparing computed phonon frequencies, spectra, or derived properties to experiments using quantitative metrics (relative standard error, mean absolute deviation, band‑by‑band differences) within a tolerance.
- **Domains:** Condensed‑matter physics, computational physics, materials science.

## Common Computational Pattern

Despite the diversity of methods employed across the 179 papers, the underlying pattern follows a consistent sequence:

1. **Structural model preparation**
   - Obtain the crystal structure from experimental databases or from a prior geometry optimization using density‑functional theory (DFT).
   - Example from cluster papers: DFT‑relaxed cell parameters for ReB₂, anatase TiO₂, HgSe/HgTe, etc.

2. **Force‑constant evaluation**
   - Compute the interatomic force constants (harmonic – and optionally anharmonic – terms) that describe the potential energy landscape.
   - Techniques observed in this cluster:
     - **Density‑functional perturbation theory (DFPT)** – analytical linear‑response calculation of dynamical matrices (e.g., for MgB₂, BaM₂P₂, TiO₂ anatase).
     - **Direct (finite‑displacement) method** – numerical differentiation of forces obtained from DFT or empirical potentials (e.g., frozen‑phonon calculations for Rh, MgB₂, Ge).
     - **Empirical or semi‑empirical interatomic potentials** – force‑constant models (Born‑von Kármán, shell models, Lennard‑Jones, Morse, etc.) fitted to experimental data (e.g., Au/Ni superlattices, B‑C₃/NbB₂, InP rigid‑ion model).
     - **Machine‑learned potentials** – Gaussian approximation potentials (GAP) or deep neural network potentials trained on DFT data (e.g., Si, Ga₂O₃).

3. **Dynamical matrix construction and diagonalization**
   - Assemble the dynamical matrix $D(\mathbf{q})$ from the force constants and masses.
   - Solve the eigenvalue problem $\det|D(\mathbf{q}) - \omega^2 I| = 0$ to obtain phonon frequencies $\omega(\mathbf{q})$ for each wave‑vector $\mathbf{q}$ in the Brillouin zone.
   - Typical implementations: Phonopy, ALAMODE, ABINIT (DFPT), Quantum‑ESPRESSO, CPMD.

4. **Phonon dispersion and DOS calculation**
   - Evaluate frequencies along high‑symmetry directions to produce dispersion curves.
   - Integrate over the Brillouin zone (e.g., using tetrahedron method or smearing) to obtain the phonon DOS $g(\omega)$.

5. **Derived properties (optional)**
   - Many papers further compute thermodynamic quantities (specific heat, entropy, Debye temperature) or transport coefficients (lattice thermal conductivity) from the phonon spectrum.
   - These are often used as additional validation metrics (e.g., specific heat of indium, andalusite; thermal conductivity of RhSi/RhSn).

6. **Validation against experiment**
   - The workflow is considered successful when the computed phonon frequencies/dispersion curves reproduce the experimental measurements within a stated numerical tolerance.
   - Examples:
     - BaNi₂P₂/BaIr₂P₂/BaRh₂P₂: calculated Allen‑Dynes $T_c$ compared to experimental $T_c$.
     - Rhodium: Kohn anomalies confirmed by neutron scattering; agreement within 3%.
     - BaTiO₃ second‑principles model: phonon dispersion and phase‑diagram compared to reference model.
     - InAsₙSb₁₋ₓ: lattice constants obey Vegard’s law to <1.3%.

## Tools, Models, and Resources

The following categories, names, and examples are extracted directly from the paper chains and metadata in this cluster:

- **DFT codes** (plane‑wave/pseudopotential): VASP, Quantum‑ESPRESSO (PWscf), ABINIT, CPMD, SIESTA.
- **Lattice‑dynamics and phonon post‑processing**: Phonopy, ALAMODE, ShengBTE (for thermal conductivity).
- **Force‑field builders**: Gaussian Approximation Potential (GAP) tools, Deep‑Potential (DeePMD) – used in machine‑learned potentials.
- **Empirical/semi‑empirical potentials**: Lennard–Jones, Morse, shell models (valence shell models for BN), rigid‑ion models (RIM 11), interstitial electron model (IEM), Born‑von Kármán models.
- **Electronic‑structure methods**: Local Density Approximation (LDA), Generalized Gradient Approximation (PBE), hybrid functionals (HSE06), DFPT, full‑potential linearized augmented plane wave (FLAPW).
- **Experimental references** frequently cited: inelastic neutron scattering (INS), Raman spectroscopy, infrared absorption, x‑ray thermal diffuse scattering (TDS), superconducting tunneling spectra.

## Verification Style

This workflow family uses **numeric verification**. The computed phonon dispersion, density of states, or derived physical quantity is directly compared with experimental data using quantitative error metrics:

- Frequencies: mean absolute deviation (MAD), relative errors per mode (typically <5% for harmonic calculations, sometimes larger for anharmonic modes).
- Bulk properties: differences in lattice constants, bulk moduli, and elastic constants are reported as percentages.
- Derived quantities (e.g., specific heat, thermal conductivity): compared to calorimetric or transport experiments with tolerances of a few percent.
- The “reproduction” is deemed successful when the computed results lie within the experimental uncertainty or within a stated tolerance (e.g., ±2% for phonon frequencies in BaS/BaSe, ±50‑100 K for melting curve of sodium).

This explicit comparison to experimental observables ensures that the workflow is self‑contained and its outcomes are reproducible and physically meaningful.
