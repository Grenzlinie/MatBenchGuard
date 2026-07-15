# Anharmonic Phonon Property Analysis

## Overview

This workflow family addresses the separation of harmonic and anharmonic contributions to temperature-dependent phonon-related physical quantities (e.g., heat capacity, phonon frequencies, second-order Doppler shift, spin‑Hamiltonian parameters). It focuses on modeling anharmonic effects using perturbative or phenomenological approaches to extract anharmonic parameters and evaluate their impact on material properties.

The tasks in this family reconstruct computational protocols that typically start from experimental data (heat capacity vs temperature, Raman/INS phonon energies vs temperature, thermal conductivity, etc.) and apply a decomposition into static (lattice‑expansion) and dynamic (vibrational) parts. Anharmonic corrections are often introduced via higher‑order terms in the crystal potential, effective potentials, or empirical models, and their parameters are determined by fitting to experiment or by first‑principles simulations.

## Common Computational Pattern

1. **Data Acquisition** – Obtain experimental temperature‑dependent data for a phonon‑related observable (e.g., $C_p$ vs $T$, phonon frequency $\omega(T)$, linewidth $\Gamma(T)$, spin‑Hamiltonian parameter $A(T)$, INS scattering intensity).

2. **Model Formulation** – Construct a theoretical expression that separates the observable into a harmonic (or static) part and an anharmonic part. Typical approaches include:
   * Expressing the observable as a sum of Debye and/or Einstein oscillator terms plus an anharmonic correction term (e.g., $C_V = C_V^{\text{harm}} + \delta C_V^{\text{anh}}$).
   * Writing $E(T) = E_s^0(1+\alpha T^x) + \beta \bigl[ \theta_1 \coth(\theta_1/2T) + \theta_2 \coth(\theta_2/2T) \bigr]$ to simultaneously capture lattice‑expansion ($\alpha T^x$) and vibrational contributions (Bose‑like occupancy factors).
   * Using an effective anharmonic potential $W(x,y)$ whose thermal‑average curvature gives the temperature‑dependent phonon frequency $\omega^2(T) = \langle \phi(T) \rangle / \mu$.
   * Applying the Bogolyubov variational method to an interacting rotator/librator Hamiltonian to obtain a self‑consistent order parameter and excitation energies that include anharmonicity.
   * Computing the temperature‑dependent effective potential (TDEP) from *ab initio* molecular dynamics to obtain renormalized phonon frequencies and self‑energies.

3. **Parameter Extraction** – The model parameters (e.g., Debye temperature $\Theta_D$, Einstein temperature $\Theta_E$, anharmonic coupling constants, effective potential parameters) are determined by fitting the model to the experimental data, usually via least‑squares minimization or a grid‑scan procedure. When first‑principles calculations are employed, the IFCs are derived directly from DFT forces and the temperature dependencies emerge from the TDEP or from the thermal average over vibrational states.

4. **Validation / Verification** – The fidelity of the model is assessed by comparing predicted and measured temperature dependencies of the observable and, when possible, by extracting physically meaningful quantities (e.g., anharmonic energy shifts, phonon lifetimes, pure‑volume vs pure‑temperature components). The verification style is **numeric**: the accept/reject decision is based on quantitative metrics such as residual sums, relative deviation percentages, or agreement within experimental uncertainty.

**Illustrative examples from the family:**
- *Rutile heat capacity*: The molar heat capacity $C_p$ (80–1100 K) was decomposed into one Debye and one Einstein term plus a negative anharmonic term $\propto -T$, with the anharmonic coefficient obtained by fitting the $C_V$ data.
- *Temperature‑dependent Raman shifts in anatase TiO$_2$*: The isobaric logarithmic derivative $(\partial\ln\omega/\partial T)_P$ was split into a pure‑volume (lattice‑expansion) part and a pure‑temperature (anharmonic self‑energy) part using measured pressure derivatives, thermal expansion $\beta$, and compressibility $\kappa$.
- *Phonon spectra of PbTe*: The TDEP technique extracted temperature‑dependent IFCs from AIMD; the resulting phonon frequencies and self‑energies were used to compute INS cross sections that quantitatively reproduced experimental double‑peak TO features and the lifting of the LA–TO crossing with increasing temperature.

## Resource Categories

### Datasets
- Temperature‑dependent heat capacity curves ($C_p$ or $C_V$)
- Phonon frequencies and linewidths from Raman, infrared, or inelastic neutron scattering
- Spin‑Hamiltonian parameters (hyperfine splitting $A$, crystal‑field splitting $D$) as a function of temperature
- Volumetric data (thermal expansion coefficients, isothermal compressibilities) to separate anharmonic contributions
- INS scattering intensities to validate frequency shifts and lifetimes

### Models & Methods
- **Debye / Einstein models** for harmonic lattice heat capacity
- **Empirical decomposition formulas** with adjustable exponents and characteristic temperatures (e.g., $E(T) = E_s^0(1+\alpha T^x) + \beta \sum_i \theta_i \coth(\theta_i/2T)$)
- **Effective anharmonic potentials** (e.g., symmetry‑adapted polynomials, exponentials) that capture soft‑mode behavior and anomalous temperature dependencies
- **Bogolyubov variational method** for interacting rotators/librators
- **Temperature‑Dependent Effective Potential (TDEP)** to obtain renormalized harmonic and anharmonic IFCs from *ab initio* molecular dynamics
- **Classical thermal‑average approaches** (sampling the effective potential) for evaluating temperature‑dependent frequencies
- **Phonon gas model** based analyses to assess thermal interface conductance

### Tools & Codes
- **DFT packages**: Quantum ESPRESSO (with PBEsol/AM05, PAW), ABINIT (LDA, DFPT)
- **Molecular dynamics**: LAMMPS (LJ solids), AIMD (VASP or Quantum ESPRESSO via TDEP)
- **Fitting / optimization**: custom scripts (grid‑scan least‑squares)
- **Group‑theoretic analysis**: for Raman mode assignment (polarization‑dependent intensity calculations)

## Verification Style

This family uses **numeric** verification. The primary acceptance criterion is how closely the model reproduces the experimental temperature‑dependent data. Typical metrics include:
- Least‑squares residuals or $\chi^2$ values from the fit.
- Relative percentage deviations between computed and measured observables (e.g., “reproduces the $T^{3}$ law with correct order of magnitude”, “agrees within ±0.7 % up to 700 K”).
- Direct comparison of predicted frequency shifts, linewidths, or cross sections with experimental spectra (e.g., “the TDEP model reproduces the double‑peak structure of the TO mode at $\Gamma$”).

Tolerances are set relative to the experimental uncertainty or the expected accuracy of the computational method. For example, a claim that an anharmonic potential reproduces the temperature dependence of a TO mode is validated by overlaying the computed $\widetilde{\nu}(T)$ curve onto the measured data.

## Repository Structure

Each task in this workflow family resides in a separate subdirectory named `paper-{paper_id}`. The entry point for a task is the file `instruction.md`, which contains:
- The specific conclusion to be reproduced.
- A step‑by‑step computational protocol derived from the reasoning chain.
- Required datasets (often referenced but not bundled; the solving agent obtains them from the source paper or public repositories).
- Model parameter ranges and fitting instructions.
- The verification criteria (numeric tolerance, expected outputs).

This `README.md` serves as the high‑level guide to the common pattern shared by all tasks in the **Anharmonic Phonon Property Analysis** family.
