# Optimization of Diffractive Grating Performance via RCWA

This workflow family covers the design, optimization, and tolerance analysis of diffractive optical grating structures using rigorous electromagnetic simulations. The core objective is to achieve a specific numerical performance metric—such as high diffraction efficiency, broadband reflectivity, narrow linewidth, or phase control—by systematically adjusting grating geometry (period, depth, duty cycle, slant angle, etc.) and material parameters.

## Core Computational Pattern

Across all papers in the family, the workflow follows a consistent pattern:

1. **Define grating geometry and material** – The grating is parameterized: period (Λ), groove/fill depth (d, h), duty cycle (f), slant angle (α), multi-layer stack composition, etc. Refractive indices are taken from literature or standard models.
2. **Solve Maxwell’s equations** – The electromagnetic response is computed using a rigorous numerical method. The most common method is **Rigorous Coupled-Wave Analysis (RCWA)**, which decomposes the periodic structure into Fourier harmonics and solves the eigenmode problem. Several papers also use **Finite-Difference Time-Domain (FDTD)**, **Finite-Element Method (FEM)**, **mode-matching**, or analytic models (e.g., leaky-mode propagation, impedance models). Some papers combine analytic and numerical approaches for rapid scanning.
3. **Extract performance metrics** – From the simulated fields, the relevant optical quantities are derived:
   - Diffraction efficiency (reflectance/transmittance per order)
   - Total reflectance, transmittance, absorptance
   - Phase shift / phase response
   - Resonance linewidth (FWHM), Q-factor
   - Coupling efficiency, spectral selectivity, angle dependence
4. **Optimize and verify** – Geometrical parameters are swept (often using global optimization like simulated annealing, differential evolution, or brute-force grids) to find the combination that best meets the design target. The final optimized performance is compared to a reference value or tolerance band to verify success.

## Typical Simulation Tools and Dependencies

Based on the provided paper excerpts, the following tools and data sources are used:

- **RCWA implementations**: Custom codes, or standard packages (MATLAB, Python). Some papers reference the Fourier modal method, scattering-matrix algorithms, or efficient eigenvalue formulations.
- **FDTD solvers**: Commercial tools (Lumerical FDTD, MEEP) or in-house codes.
- **FEM solvers**: COMSOL Multiphysics.
- **Analytic methods**: Transfer-matrix method, effective‑medium theory, coupled‑mode equations, Green’s function expansions.
- **Material data**: Wavelength‑dependent complex refractive indices (n+ik) from published compilations; Drude/Lorentz models for metals.

Exact dependencies for each paper are listed in the corresponding `instruction.md` file within its subdirectory. The solving agent is responsible for obtaining and configuring the required software environment.

## Task Structure

Each paper in this family is a standalone Harbor task, located in its own `paper-*` subdirectory. The public entry point for a task is:

- `instruction.md` – Describes the design objective, target performance metrics, allowed variations, and any required resource references (e.g., refractive index data).

The task expects the solver to:
1. Implement or use the necessary simulation code.
2. Perform parameter sweeps and/or optimization.
3. Output the resulting geometry parameters and the achieved performance values.

## Verification Style

The family uses a **numeric** verification approach:

- The computed performance metrics (e.g., diffraction efficiency, reflectivity, phase, linewidth) are compared against the reference values provided in the paper’s conclusions.
- Success is declared when the simulated metrics fall within a specified tolerance or exceed a required threshold (e.g., reflectivity >99.5%, coupling efficiency > 70%, linewidth within a few percent).
- No experimental validation or physical lab work is required; simulations alone suffice to reproduce the conclusions.

## Domain Coverage

The family spans a wide range of grating applications, all unified by the RCWA/EM‑simulation optimization paradigm:

- Broadband high‑reflectivity mirrors (polarization‑insensitive, curved, diamond)
- Narrow‑band filters and sensors (guided‑mode resonance, EIT, SPR)
- Beam splitters, polarizers, and waveplates
- Solar cell light‑trapping and antireflection
- Grating couplers for waveguides
- Terahertz emitters and backward‑wave oscillators
- Metasurfaces for nonlinear optics (SHG, thermal emission)

The common thread is the deliberate tuning of grating geometry to optimize a numerically defined optical response.
