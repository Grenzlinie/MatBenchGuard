# DFT+U Hubbard U Variation Analysis

## Overview

This workflow family encompasses systematic computational studies that investigate the effect of the on-site Hubbard U parameter in DFT+U (density functional theory with Hubbard correction) calculations. By varying the effective on-site Coulomb interaction parameter U applied to correlated orbitals (typically transition-metal 3d or actinide 5f states), researchers analyze how electronic structure properties—such as band gaps, density of states, magnetic moments, and orbital ordering—respond to correlation strength. The goal is to reproduce experimental observables, gain insight into the degree of electron localization, and establish optimal U values for materials modeling.

## Common Computational Pattern

### Core Method

All papers employ **spin‑polarized density functional theory (DFT) augmented with a Hubbard‑like on‑site correction** (often denoted LSDA+U, GGA+U, or DFT+U). The Hubbard U parameter is either treated as an empirical parameter scanned over a range or determined self‑consistently (e.g., via linear response or constrained DFT). Calculations are performed with standard periodic codes:

- **VASP** – plane‑wave projector‑augmented wave (PAW) method
- **Wien2k** – full‑potential linearized augmented plane‑wave (FP‑LAPW) method
- **Quantum ESPRESSO** – plane‑wave pseudopotential method
- **FPLO** – full‑potential local‑orbital method
- **OpenMX** – numerical pseudo‑atomic orbital basis

Exchange‑correlation functionals used include LDA, PBE‑GGA, and occasionally hybrids (e.g., HSE06) for validation. Spin‑orbit coupling (SOC) is included when relevant for heavy elements.

### Typical Workflow Steps

1.  **Structure Preparation** – Obtain experimental crystal structure or perform full geometry relaxation (lattice parameters and atomic positions) under a chosen DFT+U setting.
2.  **U Parameter Exploration** – Run a series of self‑consistent DFT+U calculations with different U values (or use self‑consistent U methods). Some papers fit U to reproduce experimental band gaps or magnetic moments.
3.  **Property Calculation** – Extract electronic band structure, density of states (DOS), partial DOS, magnetic moments (spin and orbital), band gaps, and formation energies.
4.  **Magnetic Configuration Search** – Compare total energies of ferromagnetic, antiferromagnetic, and non‑collinear (e.g., spiral) spin arrangements to identify the magnetic ground state.
5.  **Verification** – Compare computed band gaps, magnetic moments, lattice parameters, and DOS features with experimental measurements (optical gaps, neutron diffraction, photoemission, magnetic susceptibility).
6.  **Analysis and Interpretation** – Correlate the U‑dependence of electronic structure with material‑specific physics (e.g., Mott transition, orbital ordering, half‑metallicity).

## Resources and Tools

- **DFT codes**: VASP, Wien2k, FPLO, OpenMX, Quantum ESPRESSO (as indicated by individual papers)
- **Postprocessing**: density‑of‑states analysis, band‑structure plotting, Bader charge analysis, Wannier orbital construction
- **Hubbard U determination**: constrained DFT, linear‑response method, empirical fitting to experimental references
- **Magnetic models**: Heisenberg model mapping, Monte Carlo simulations (e.g., VAMPIRE)

## Verification & Validation

The primary validation is **comparison with experimental data**. This family is designated with `verify_type = experiment`. Typical benchmark quantities:

- Electronic band gap (optical absorption, photoemission)
- Magnetic moments (neutron diffraction, SQUID magnetometry)
- Density of states (photoemission, inverse photoemission)
- Lattice constants (X‑ray/neutron diffraction)
- Magnetic transition temperatures (susceptibility, specific heat)

The workflow is “dry” (`lab_type = dry`) – entirely computational, no new experimental measurements are performed within the tasks.

## Task Structure

Each paper in this family is packaged as a standalone Harbor task under a `paper‑<id>` directory. The public interface for each task is the `instruction.md` file, which specifies:

- The target material and Hubbard U range to explore
- Required DFT settings and computational parameters
- The properties to extract and validation criteria

## Domains

- Materials Science
- Computational Physics
- Solid State Physics
- Magnetic Materials

---
*Automatically generated summary from the DFT+U Hubbard U Variation Analysis workflow family.*
