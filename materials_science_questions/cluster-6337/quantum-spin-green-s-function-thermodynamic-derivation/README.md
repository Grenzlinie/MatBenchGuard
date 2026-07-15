# Quantum Spin Green's Function Thermodynamic Derivation

## Overview
This workflow family contains **138 papers** that derive closed self-consistent equations for thermodynamic quantities (critical temperature \(T_c\), magnetization, correlations, susceptibility, specific heat, etc.) of quantum spin models. The common method employs **Green's function equations of motion** with **decoupling approximations**, followed by application of the **spectral theorem** and **numerical solution** of the resulting nonlinear self-consistency equations. Verification is numerical: computed values are compared against known exact solutions or Monte Carlo results within a prescribed tolerance.

## Core Computational Pattern

The work follows a sequence that is remarkably consistent across the family:

1. **Model definition** – Specify a spin Hamiltonian (Heisenberg, Ising, XY, Blume–Capel, transverse‑field Ising, etc.) with nearest‑neighbor and possibly next‑nearest‑neighbor interactions, single‑ion anisotropy, external magnetic field, and site‑dependent parameters.
2. **Green’s function selection** – Introduce retarded double‑time commutator Green’s functions, typically of the form \(\langle\langle S_i^+; S_j^-\rangle\rangle\) or combinations with products of \(S^z\) to handle higher‑order anisotropy terms. Multisublattice ordering (ferro‑ or antiferromagnetic) is accounted for by defining separate Green’s functions for each sublattice.
3. **Equation of motion** – Write the Heisenberg equations for the chosen Green’s functions using the Hamiltonian. This generates a hierarchy of higher‑order Green’s functions (e.g., \(\langle\langle S_i^z S_j^+; S_k^-\rangle\rangle\)).
4. **Decoupling approximation** – Truncate the infinite hierarchy by factorizing higher‑order Green’s functions into products of lower‑order ones and thermal averages. Common schemes include:
   - **Tyablikov decoupling (RPA)**: \(\langle\langle S_i^z S_j^+; S_k^-\rangle\rangle \to \langle S^z\rangle\langle\langle S_j^+; S_k^-\rangle\rangle\) for \(i\neq j\).
   - **Callen–Anderson decoupling**: accounts for kinematic constraints via a factor \(\Gamma\) depending on \(\langle (S^z)^2\rangle\).
   - **Random Phase Approximation (RPA)** with additional parameters to preserve rotational symmetry.
   - **Effective‑field decoupling** (e.g., in EFT) using Van der Waerden identities.
   - **Static fluctuation approximation (SFA)**: replaces squared fluctuations by their averages.
5. **Fourier transform** – Convert the decoupled equations into algebraic \(\omega\)-dependent equations for the momentum‑space Green’s functions. The poles of these Green’s functions yield the **spin‑wave dispersion** \(\omega_q\).
6. **Spectral theorem** – Express thermal averages (magnetization, correlations, quadrupolar moments) as integrals over the spectral density using Bose distribution functions. This step provides closed relations between the Green’s functions and the order parameters.
7. **Self‑consistent equations** – Combine the dispersion and the spectral relations to obtain a finite set of coupled nonlinear integral equations for the order parameters (e.g., magnetization \(\langle S^z\rangle\), quadrupolar moment \(\langle (S^z)^2\rangle\), etc.). The number of equations equals \(2S\times N_{\text{sublattices}}\) or more depending on anisotropy.
8. **Numerical solution** – Iterate the self‑consistency equations (often with Newton‑Raphson or Picard iteration) over a temperature or field range until convergence. From the converged order parameters, compute thermodynamic functions such as specific heat, susceptibility, internal energy, and critical temperatures.
9. **Comparison** – Validate against known exact solutions (e.g., 1D Ising, Bethe ansatz), series expansions, or high‑precision Quantum Monte Carlo data.

## Resources

### Models and Parameters
- **Hamiltonians**: Heisenberg, XXZ, XY, Ising, transverse‑field Ising, Blume–Capel, Falicov–Kimball, compass‑model, dipolar‑coupled systems, cluster spin models, ladders, frustrated lattices (triangular, Villain), mixed‑spin ferrimagnets.
- **Physical parameters**: Exchange couplings \(J\), anisotropy constants \(\Delta, D\), transverse fields \(\Omega\), external magnetic fields \(h\), single‑ion crystal field \(D\), coordination number \(z\), lattice dimension \(d\).
- **Lattice types**: Square, honeycomb, cubic, linear chains, ladders, layered systems, amorphous structures (via disorder distribution).

### Tools & Computational Aids
- **Symbolic algebra**: One paper (UEG) explicitly uses computer‑algebra software to evaluate closed‑form integrals for spin‑scaling functions. Otherwise the derivations are performed manually, while the resulting self‑consistency equations are solved numerically.
- **Numerical methods**: Gaussian quadrature for momentum integrals, Fourier‑space convolution, non‑linear equation solvers, eigen‑solver methods for the matrix Green’s function approach, occasional Monte Carlo (for validation only).

## Verification Style

The family is entirely **theoretical (dry)** and **numeric verification**. The computed physical quantities—critical temperatures \(T_c\), magnetizations, gaps, correlation lengths, susceptibilities, and specific heats—are compared with:
- Exact solutions where available (1D Ising, 1D XY, Bethe ansatz results, exact dimer/Trotter limits).
- High‑temperature or low‑temperature series expansions.
- Quantum Monte Carlo (QMC) simulations (e.g., for frustrated Heisenberg model, spin ladders).
- Lanczos exact diagonalization on small clusters.
- Other published effective‑field or mean‑field results.

Tolerance is not explicitly specified but the papers typically claim “good agreement,” “quantitative agreement,” or “results consistent with” implying relative errors on the order of a few percent for \(T_c\) and within statistical noise for correlation functions. In some cases the method is shown to improve over simple mean‑field approximations.

## Paper Organization

Each paper in the family is stored as a standalone directory named `paper-<paper_id>`. The public entry point for any solver is `instruction.md`, which contains the detailed task definition, including the specific Hamiltonian, parameters, and target quantities. All necessary equations, codes, and validation data are provided within that directory. This README describes the overarching methodology common to all tasks.
