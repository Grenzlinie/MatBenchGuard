# DFT study of vacancy-induced magnetism

## Overview
This workflow family investigates magnetism induced by point defects—primarily vacancies—in various materials using spin-polarized density functional theory (DFT). It involves constructing a supercell of the host material, introducing one or more defects, relaxing the atomic structure, and performing spin-polarized electronic structure calculations to extract magnetic moments, band topology, spin densities, and formation energies. The goal is to understand the origin of magnetism via projected densities of states, spin density analysis, and exchange coupling strengths.

## Common Computational Pattern
1. **Model construction**  
   - Create a supercell of the pristine host (e.g., wurtzite, zinc-blende, perovskite, 2D materials).  
   - Introduce point defects: single or multiple vacancies (cation/anion), substitutional dopants, or defect complexes.  
   - Ensure periodic images do not interact (vacuum spacing for 2D/surfaces).

2. **Electronic structure method**  
   - Spin-polarized DFT using plane-wave pseudopotential codes (VASP, CASTEP, Quantum ESPRESSO, SIESTA, etc.).  
   - Common exchange-correlation functionals: GGA-PBE, LDA, DFT+U (Hubbard correction), sometimes with semi-empirical dispersion corrections (D2, vdW-DF) for layered materials.  
   - Projector-augmented wave (PAW) or ultrasoft pseudopotentials.  
   - Plane-wave cutoff energies typically 350–600 eV.  
   - Brillouin-zone integration with Monkhorst-Pack k-point grids.

3. **Geometry optimization**  
   - Fully relax atomic positions (and sometimes cell parameters) until forces fall below 0.01–0.05 eV/Å.  
   - Consider different initial magnetic configurations (non-spin-polarized, ferromagnetic, antiferromagnetic) to locate the ground state.

4. **Electronic and magnetic analysis**  
   - Compute band structures (spin-resolved) and density of states (total, partial).  
   - Extract total magnetic moments, atomic magnetic moments (via projection or Bader analysis), and spin density distributions.  
   - Calculate spin-polarization energy  \( \epsilon = E_{\text{NSP}} - E_{\text{SP}} \).  
   - Evaluate exchange coupling by comparing total energies of FM and AFM alignments in supercells with multiple defects.  
   - Determine defect formation energies under different charge states using chemical potentials.

5. **Additional analyses** (optional)  
   - Ab initio molecular dynamics (AIMD) at elevated temperatures to assess structural stability.  
   - Wannier function construction for tight-binding models.  
   - Bader charge analysis for charge transfer.

## Verification Style
**Numeric verification** – The primary means of confirming reproducibility is by comparing computed numerical quantities against reference values (convergence tests or literature data) within specified tolerances. Key checkpoints include:
- Magnetic moments (total, per atom)  
- Energy gaps (band gaps)  
- Total energy differences between magnetic states  
- Defect formation energies  
- Lattice constants after relaxation  
- Spin-polarization energies  

When an experimental reference is available, the comparison is made directly; otherwise, convergence against computational parameters (e.g., increasing k-point density, cutoff energy) serves as verification.

## Typical Resources
- **DFT codes:** VASP, CASTEP, Quantum ESPRESSO, SIESTA, DMol³  
- **Pseudopotentials:** PAW, ultrasoft  
- **Functionals:** GGA-PBE, LDA, PBE+U, LDA+U, vdW-DF, D2 dispersion  
- **Analysis tools:** Bader charge analysis, WANNIER90, VESTA, CALYPSO

## Domains
- Computational materials science
- Condensed matter physics
- Magnetic materials
- Density functional theory

## Task Structure
Each `paper-*` subdirectory corresponds to a standalone Harbor task. Its public interface is `instruction.md`, which details the specific computational setup and verification targets for that paper.

---

*This README provides a high-level guide to the workflow family. Refer to individual task instructions for exact parameters and validation criteria.*
