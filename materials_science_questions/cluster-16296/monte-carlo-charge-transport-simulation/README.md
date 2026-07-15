# Monte Carlo Charge Transport Simulation

## Overview

This workflow family encompasses semiclassical Monte Carlo simulations of charge carrier transport in semiconductor bulk materials, heterostructures, quantum wells, nanowires, and devices. The central computational task is to model the dynamics of electrons (and sometimes holes) under an applied electric field, accounting for scattering from phonons, impurities, interfaces, and other carriers. The primary outputs are steady‑state transport properties such as drift velocity, mobility, distribution functions, and subband populations.

## Common Computational Pattern

Despite variations in materials and device geometries, the papers in this family share a coherent computational pipeline:

1.  **Definition of electronic structure**  
    - Choice of band model: parabolic or non‑parabolic valleys (e.g., Kane’s theory), often including several conduction‑band minima (Γ, L, X).  
    - For confined systems: solution of the Schrödinger equation in the growth direction (Numerov method, variational trials, or analytic approximations) to obtain subband energies and envelope functions.  
    - Specification of material parameters: effective masses, band gaps, non‑parabolicity coefficients, dielectric constants, phonon energies, deformation potentials, etc.

2.  **Computation of scattering rates**  
    - Rates are derived from Fermi’s golden rule for each relevant mechanism:  
      - Electron–phonon interactions (polar optical, acoustic deformation, piezoelectric, intervalley).  
      - Ionized‑impurity scattering (Brooks–Herring, Conwell–Weisskopf, or mixed models).  
      - Electron–electron scattering (short‑range, screened, or two‑electron state methods).  
      - Impact ionization (Keldysh‑type formulas, analytic threshold laws).  
    - For low‑dimensional systems, bulk matrix elements are projected onto the confined envelope functions to obtain subband‑dependent 1D or 2D rates.  
    - Rates are tabulated over an energy mesh for efficient Monte Carlo sampling.

3.  **Monte Carlo simulation of carrier dynamics**  
    - Implementation as ensemble Monte Carlo (parallel evolution of many carriers) or single‑particle Monte Carlo.  
    - Free‑flight generation: a random flight time is sampled from an exponential distribution using the total scattering rate; the electron accelerates according to Newton’s law.  
    - Scattering selection: at the end of the flight, a scattering mechanism is chosen based on the relative rates, and the final state (momentum, energy, possibly subband) is determined stochastically, enforcing energy and crystal‑momentum conservation.  
    - Advanced features include:  
      - Time‑dependent nonequilibrium phonon populations (coupled electron–phonon Monte Carlo).  
      - Pauli exclusion (Lugli–Ferry rejection).  
      - Energy broadening (Lorentzian or Gaussian convolution, intra‑collisional field effects).  
      - Two‑electron pair Monte Carlo for exact e‑e scattering.  
    - The simulation is run until a steady state is reached (or transient evolution is tracked).

4.  **Extraction of steady‑state transport properties**  
    - Drift velocity vs. electric field (including velocity overshoot, negative differential mobility, Gunn effect).  
    - Low‑field mobility (from the linear slope).  
    - Carrier distribution functions (energy‑resolved, valley‑resolved, subband‑resolved).  
    - Subband populations, average electron temperatures, and energy‑loss rates.  
    - For device simulations: terminal currents, electric field profiles, and I‑V characteristics are obtained by coupling the Monte Carlo transport with Poisson’s equation.

## Taxonomy of Models, Tools, and Datasets

*Derived from the provided papers only; categories are listed when explicitly mentioned.*

### Models / Physical Ingredients
- **Band structure**: parabolic, non‑parabolic (Kane), empirical pseudopotentials, full‑band models (Δ‑point, L‑point, X‑point valleys).
- **Scattering mechanisms**: Fröhlich polar‑optical phonon, acoustic deformation potential, piezoelectric, intervalley (Γ↔L, Γ↔X), ionized impurity, electron‑electron (short‑range, screened), impact ionization.
- **Confinement / structure**: bulk, quantum wells (infinite square well, triangular well), quasi‑1D quantum wires, resonant‑tunneling double‑barrier diodes, HEMT channels.
- **Screening**: Debye–Hückel, Brooks–Herring.
- **Special treatments**: nonequilibrium LO phonons, collisional broadening (Lorentzian, Gaussian), intra‑collisional field effect, hot‑phonon models, two‑electron state ensembles.

### Tools
- **Numerical solvers**: Poisson solver (FISH1D), Numerov Schrödinger solver, variational methods.
- **Programming environments**: MATLAB (absorption‑spectrum calculation, data analysis).
- **Commercial simulators**: COMSOL Multiphysics (mentioned in one paper for complementary LED simulations).

### Reference Data
- Experimental low‑field mobilities of bulk InAs, InSb, GaN, etc.
- Experimental velocity‑field curves of GaAs, CdTe.
- Experimental I‑V characteristics of double‑barrier resonant tunneling diodes.
- Benchmark Monte Carlo results from earlier publications.

## Verification Style

This family employs **numeric verification**: the simulated quantities (drift velocity, mobility, peak velocity, negative differential mobility, subband populations, photocurrent transients) are compared with
1.  **Experimental measurements** (e.g., mobility vs. temperature, velocity‑field data, peak‑to‑valley ratios) using a numerical tolerance; and/or
2.  **Benchmark Monte Carlo results** from established literature.

Agreement within a factor of order two (or better) is typically reported when physical parameters are tuned; exact numerical convergence is demonstrated by varying ensemble sizes, mesh discretization, and simulated time steps.

## Repository Structure

Each subdirectory `paper-<id>/` constitutes a **standalone Harbor task**. The public entry point for solving is the file `instruction.md` (not `TASK.md`). The task includes all necessary input specifications (material parameters, geometry, field conditions) and requires the solver to implement and execute the Monte Carlo workflow described in the corresponding paper to reproduce the targeted transport observable.

No additional bundling of datasets or pre‑installed software is required beyond what the solving agent obtains from the task files; the instruction.md specifies the resources needed.
