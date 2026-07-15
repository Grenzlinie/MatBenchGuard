# Thermoelectric Transport Modeling Workflow Family

## Overview

This workflow family contains computational studies that model thermoelectric transport properties—Seebeck coefficient, electrical conductivity, power factor, and figure of merit (ZT)—of various materials. The primary goal is to interpret experimental data, predict optimal doping, and extract effective masses by combining electronic structure calculations with semiclassical or quantum transport theory. The workflows are entirely computational (dry lab), validated by numeric comparison with experimental measurements.

## Main Computational Pattern

The common computational pipeline across papers consists of three stages:

1.  **Electronic structure calculation**:
    - Density Functional Theory (DFT) using functionals such as PBE‑GGA, PBEsol, mBJ, HSE06, or LDA. Codes employed include VASP, Quantum ESPRESSO, WIEN2k, SIESTA, and CASTEP.
    - Some studies use tight‑binding models or analytical dispersions (parabolic/Kane bands).
    - Outputs include band structures, density of states, effective masses, and sometimes electron‑phonon matrix elements (via DFPT) for phonon‑limited transport.

2.  **Transport coefficient computation**:
    - Semiclassical Boltzmann transport equation (BTE), most commonly within the constant relaxation‑time approximation (CSTA), implemented via BoltzTraP or custom solvers.
    - Energy‑dependent scattering models (acoustic deformation potential, polar optical phonon, ionized impurity) are introduced when extracting absolute conductivities.
    - For nanoscale systems, non‑equilibrium Green’s function (NEGF) methods (e.g., GOLLUM) are used to compute ballistic transport.
    - Single‑parabolic‑band (SPB), two‑band Kane, or Mott‑relation models are applied to experimental data to extract effective mass or Fermi level.

3.  **Comparison with experiment**:
    - The computed Seebeck coefficient, electrical conductivity, and power factor are compared to experimental data (often from published literature) using numerical agreement metrics such as R², mean absolute error, or relative deviation. This serves as the primary verification.

## Key Resources

- **DFT / Electronic structure codes**: VASP, Quantum ESPRESSO, WIEN2k, SIESTA, CASTEP  
- **Transport codes**: BoltzTraP, ShengBTE (for lattice thermal conductivity), GOLLUM (NEGF), custom BTE solvers  
- **Analytical models**: Single‑parabolic‑band, two‑band Kane model, Mott formula, Heikes formula  
- **Data**: Experimental thermoelectric data (Seebeck coefficient, resistivity, Hall coefficient) drawn from various publications; no single named dataset is common to all papers.

## Verification Style

**Numeric verification**: Calculated transport coefficients are directly compared with experimental measurements. Agreement is quantified using statistical measures (e.g., R², mean absolute error). This aligns with the dry‑lab nature of the family.

## Task Structure

Each subdirectory `paper‑*` corresponds to a standalone Harbor task. The public entry point for a task is `instruction.md`, which details the required resources and steps needed to reproduce the study’s results. This family aggregates 202 papers, each with one or more reasoning chains that codify the specific computational workflow.
