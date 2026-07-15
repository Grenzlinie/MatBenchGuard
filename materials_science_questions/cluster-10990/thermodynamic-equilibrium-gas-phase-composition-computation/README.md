# Thermodynamic Equilibrium Gas-Phase Composition Computation

## Overview
This workflow family encompasses the computation of equilibrium partial pressures, mole fractions, or yields of gas-phase species in multicomponent chemical systems that may also contain condensed phases (solids, liquids). The underlying methodology is rooted in classical thermodynamics: either by direct minimization of the total Gibbs free energy of the system, or by solving a set of nonlinear mass‑action equations using equilibrium constants obtained from standard thermochemical data.

Typical applications include:
- Prediction of dominant vapor species over ceramic, metal, or oxide substrates at high temperature.
- Phase‑field mapping for chemical vapor deposition (CVD) or chemical vapor infiltration (CVI).
- Speciation in combustion, gasification, or nuclear accident scenarios.
- Volatile degassing from magmas.

## Common Computational Pattern
Despite the diversity of chemical systems, the core computational workflow almost always follows these steps:

1. **Define the system**: Elements present, candidate gaseous and condensed species, temperature range, total pressure, and initial composition (often expressed as elemental amounts or feed ratios).
2. **Select the thermodynamic method**:
   - *Gibbs energy minimization*: The equilibrium composition is the set of species amounts that minimizes the total Gibbs free energy of the system subject to mass‑balance constraints. This is implemented by software packages such as **SOLGASMIX**, **FactSage**, or **TERRA**.
   - *Mass‑action approach*: A set of independent chemical reactions is written, and their equilibrium constants are computed from standard free energies (often from the **JANAF** tables). Together with element‑conservation equations, the partial pressures of all species are solved numerically. This approach is common when only a few species dominate or when explicit algebraic expressions are desired (e.g., for redox‑controlled systems or for surface exchange equilibria).
3. **Include auxiliary models** when needed:
   - Activity coefficients for solid/liquid solutions.
   - Solubility laws for volatile species in melts (e.g., power‑law relations used in D‑Compress).
   - Transport or mass‑transfer coupling (flux equations, boundary‑layer models).
4. **Numerical solution**: Solve the resulting nonlinear algebraic system. Tools range from custom iterative solvers (using high‑precision arithmetic when required) to built‑in algorithms in thermodynamic packages.
5. **Post‑processing**: Generate partial‑pressure curves, phase diagrams, conversion yields, or particle‑size predictions (when combined with agglomeration theory).

## Typical Verification Style

- **Numeric verification**: The computed partial pressures or mole fractions are compared against published experimental measurements or independent benchmark calculations. For major species, agreement within 10 % relative error is accepted as successful. Experimental validation often includes:
  - Knudsen effusion mass‑loss data.
  - X‑ray diffraction (XRD), X‑ray photoelectron spectroscopy (XPS), or energy‑dispersive X‑ray analysis (EDX) of condensed residues.
  - Transmission electron microscopy (TEM) for particle morphology.
  - Gas‑phase analysis by mass spectrometry or ion chromatography in combustion experiments.

## Resources (Tools, Databases, Models)

- **Thermochemical databases**: JANAF, IVTANTERMO, FactSage databases (Thermfact/CRCT, GTT‑Technologies).
- **Equilibrium software**: SOLGASMIX / CHEMSAGE, FactSage, TERRA, D‑Compress (specialized for magmatic volatiles), NASA chemical equilibrium program.
- **Reactor‑scale models**: Custom analytical models coupling mass transfer and interface equilibria (e.g., SiC/CO₂ oxidation).
- **Physical models**: Agglomeration theory for droplet size prediction (boron condensation), Einstein solid models for solid‑vapor equilibria.

## Task Structure

Each `paper-*` subdirectory is a standalone Harbor task. The public file is `instruction.md`, which contains the specific goals, inputs, and expected outputs for that paper’s computation. The solving agent should retrieve any required resources (e.g., thermochemical data, reaction sets) from the provided context and perform the equilibrium calculation using either minimization or mass‑action equations, as appropriate for that paper. Verification will involve comparing calculated partial pressures or compositions with published benchmark values, targeting agreement within 10 % for major species.
