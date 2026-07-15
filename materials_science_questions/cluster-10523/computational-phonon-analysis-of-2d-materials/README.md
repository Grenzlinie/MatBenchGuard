# Computational Phonon Analysis of 2D Materials

## Overview
This workflow family focuses on the first-principles calculation of vibrational properties of two-dimensional materials and nanostructures. The core objective is to obtain phonon frequencies, mode eigenvectors, and Raman/infrared activity using density-functional theory (DFT) combined with phonon calculation methods (DFPT or finite displacement), and subsequently analyze how these properties change under external perturbations such as strain, doping, or substitution.

## Common Computational Pattern
1. **Structure Relaxation**  
   Full geometry optimization of the target material using DFT with appropriate exchange-correlation functionals (PBE, LDA, HSE06) and pseudopotentials (PAW, norm‑conserving). Periodic boundary conditions model monolayers or bilayers, often with vacuum gaps to simulate free-standing layers.

2. **Phonon Calculation**  
   Harmonic interatomic force constants (IFCs) are obtained via density-functional perturbation theory (DFPT) or the finite‑displacement method. Phonon dispersions and density of states are computed, typically with codes like VASP + Phonopy or ABINIT. Zero‑point motion and thermodynamic quantities may be derived from the harmonic spectrum.

3. **Spectroscopic Intensities**  
   Raman polarizability tensors and infrared oscillator strengths are evaluated from DFPT or finite differences. Orientation‑averaged Raman and IR spectra are generated for comparison with experiment.

4. **Perturbation Handling**  
   External influences are simulated by:
   - Introducing intentional strain (via lattice deformation),
   - Substituting atoms (using supercells, VCA, or doping models),
   - Adding charge carriers (via gating or virtual doping).

5. **Validation**  
   Computed phonon frequencies and intensities are compared with experimental Raman and IR data using numeric metrics (e.g., root‑mean‑square deviation, linear‑regression slope).

## Typical Resources
- **DFT codes**: VASP, ABINIT
- **Phonon tools**: Phonopy, finite‑displacement utilities
- **Post‑processing**: custom scripts for Raman tensors, oscillator strengths, and Boltzmann transport (ShengBTE)
- **Interatomic potentials**: machine‑learning force fields for certain materials (e.g., CHGNet or DeePMD) occasionally employed for large‑scale modeling
- **Experimental baselines**: Raman and infrared spectra from literature

## Verification Style
The family uses **numeric** verification. Key metrics include:
- Direct comparison of calculated and measured Raman/IR peak positions (in cm⁻¹)
- Energy differences between structural phases (in eV)
- Trends in frequency shifts (e.g., slope of softening vs. doping) compared to experimental dependences
- Statistical indicators such as RMSE or linear‑trend slopes when multiple peaks are compared across a series of samples or conditions.

## Task Structure
Each `paper-*` subdirectory is a standalone Harbor task containing an `instruction.md` that defines the specific calculation, the material, the perturbation, and the target observables. All necessary input files (e.g., relaxed structures, scripts) are bundled in the task directory.
