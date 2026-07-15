# Magnetoelastic Coupling Analysis via Crystal Field Theory

## Overview

This workflow family encompasses computational models that investigate the interplay between magnetic degrees of freedom (rare‑earth ions, spin structures) and lattice strains in magnetic materials. The core methodology relies on **crystal‑field theory** combined with **statistical mechanics** to compute temperature‑dependent properties such as elastic constants, specific heat anomalies, magnetization, lattice distortions, and sound velocities. The models are frequently applied to rare‑earth intermetallics, Heusler alloys, actinide compounds, and transition‑metal systems, providing insight into magnetoelastic coupling constants, phase transitions, and magnetostrictive effects.

## Common Computational Pattern

Despite the diversity of materials, the underlying computational workflow across papers follows a consistent sequence:

1. **Model System Definition**  
   - Define the local magnetic moment (total angular momentum $J$, spin $S$, or effective spin).  
   - Choose an appropriate crystal‑field Hamiltonian (e.g., Stevens operators $O_l^m$ with parameters $B_l$, $A_l\langle r^l\rangle$).  
   - Include additional interactions: bilinear exchange ($J_{ij}$), quadrupolar exchange, and magnetoelastic couplings (strain–spin or strain–quadrupole terms).  
   - Incorporate elastic energy contributions (background elastic constants, strain fields).

2. **Eigenvalue Problem or Perturbation Treatment**  
   - Diagonalize the crystal‑field part of the Hamiltonian to obtain single‑ion energy levels and wavefunctions.  
   - Treat strain or magnetic field as perturbations to extract strain derivatives or field‑induced level shifts.

3. **Thermodynamic Averaging**  
   - Construct the partition function $Z = \sum_i e^{-E_i/k_\mathrm{B}T}$ (or a free energy functional).  
   - Compute quantities such as magnetization, quadrupolar moments, and elastic constants via derivatives of the free energy.  
   - For mean‑field treatments, solve self‑consistent equations for order parameters (magnetization, strain, quadrupolar order).

4. **Observable Calculations**  
   - Derive field‑ and temperature‑dependent elastic moduli (e.g., $C_{11}$, $C_{44}$, $(C_{11}-C_{12})/2$) using quadrupole susceptibilities or strain derivatives of the free energy.  
   - Compute specific heat, magnetic susceptibility, or lattice distortions from the same thermodynamic framework.  
   - Compare results with experimental data (ultrasound measurements, neutron scattering, magnetization curves, etc.).

5. **Parameter Extraction and Analysis**  
   - Fit model parameters (crystal‑field parameters, exchange constants, magnetoelastic coefficients) to reproduce experimental observables.  
   - Determine the temperature evolution of order parameters and phase boundaries.

## Typical Resources

A workflow task (contained in a `paper‑*` subdirectory) usually requires the following resource categories, which are specified in its `instruction.md` file:

- **Crystal‑field parameters** ($B_4$, $B_6$, $A_4\langle r^4\rangle$, etc.) obtained from prior neutron scattering or optical spectroscopy.
- **Stevens operator tables** for the relevant angular momentum $J$.
- **Experimental data** for verification (elastic constants $C_{ij}(T)$, specific heat $C_m(T)$, magnetization curves, lattice parameter temperature dependence). These are often supplied as CSV/TSV files or numerical tables.
- **Background physical constants** (Boltzmann constant, Bohr magneton, etc.).

The solving agent receives the instruction file with exact inputs and required outputs, so no additional bundling is needed.

## Verification

The typical verification strategy is **numeric**: the computed observables (elastic constants, phase transition temperatures, order‑parameter temperature dependence) are compared against experimental data using quantitative metrics such as root‑mean‑square deviation (RMSD) or correlation coefficients. A successful reproduction is declared when the model results fall within the tolerance specified in the task instruction (e.g.,<10% deviation in elastic constant values, or a high $R^2$ for a $C_{ij}(T)$ curve).

## Task Structure

Each paper in the family is a standalone Harbor task located in its own directory (`paper‑<id>`). The public interface is the `instruction.md` file, which details the objective, input data, required calculations, and verification criteria. The README here serves as an overview of the shared methodological approach across the family.
