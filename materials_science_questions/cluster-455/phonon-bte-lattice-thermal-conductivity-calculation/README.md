# Phonon BTE Lattice Thermal Conductivity Calculation

## Overview
This workflow family computes the lattice thermal conductivity of solids from first‑principles or empirical phonon properties using the phonon Boltzmann transport equation (BTE). It models phonon scattering by harmonic/anharmonic force constants, isotopic disorder, grain boundaries, and point defects, and optionally analyzes spectral contributions and mean free path accumulation. The computed conductivity values are compared directly with experimental or literature reference data to validate the predictions.

## Common Computational Pattern
All papers in this family follow a consistent multistep procedure:

1. **Obtain interatomic force constants**  
   - **Harmonic (second‑order) force constants** from density‑functional theory (DFT) via `VASP`, `Quantum ESPRESSO`, or from empirical potentials (e.g., Stillinger–Weber, AIREBO).  
   - **Anharmonic (third‑order) force constants** from finite‑difference or perturbation‑theory methods, typically using `Thirdorder`, `Phono3py`, or direct DFT supercell calculations.  

2. **Compute phonon dispersion and group velocities**  
   - Diagonalize the dynamical matrix constructed from second‑order force constants to obtain phonon frequencies ω(q) and eigenvectors.  
   - Calculate group velocities v_g = dω/dq analytically or by finite differences.  

3. **Construct scattering rates (relaxation times)**  
   - **Three‑phonon scattering** – from third‑order force constants; treated in the relaxation time approximation (RTA) or iteratively.  
   - **Isotopic / mass‑disorder scattering** – using the Klemens or Tamura model (τ⁻¹ ∝ ω⁴).  
   - **Boundary scattering** – via Casimir limit or more detailed surface‑transmission models.  
   - **Point‑defect, impurity, and grain‑boundary scattering** – incorporated through Matthiessen’s rule (τ_total⁻¹ = Σ τ_i⁻¹).  
   - Codes: `ShengBTE`, `almaBTE`, `Phono3py`, custom scripts.  

4. **Solve the phonon Boltzmann transport equation**  
   - Use the RTA or the iterative solution (provided by the BTE solvers).  
   - Compute the thermal conductivity tensor from the modal contributions:
     ```
     κ_αβ = Σ_{q,s} c_{q,s} v_{q,s,α} v_{q,s,β} τ_{q,s}
     ```
     where c is the modal heat capacity.  
   - For spectral analysis, decompose κ into frequency‑ or mean‑free‑path‑resolved contributions.  

5. **Validate against experiment / literature**  
   - Compare temperature‑dependent κ(T) with measured values (tolerance typically within ~20–30% for accurate potentials/functionals).  
   - Check convergence with respect to q‑point grid and cutoff radius.  
   - In some cases, use macroscopic transport models (e.g., Callaway/Dubey models) as a complementary check.  

## Required Resources

### Datasets & Reference Data
- Experimental or ab‑initio‑derived phonon dispersions and group velocity tables.  
- Thermal conductivity measurements for validation (e.g., time‑domain thermoreflectance, 3ω methods).  
- Elastic constants, Grüneisen parameters, and Debye temperatures (often from DFT or literature).  

### Models & Frameworks
- **Scattering rate models**: Three‑phonon (Fermi golden rule), isotopic (mass disorder), point‑defect (Rayleigh‑like), boundary (Casimir, specular/diffuse).  
- **Boltzmann transport solvers**: ShengBTE, almaBTE, Phono3py (iterative or RTA), custom Monte Carlo solvers.  
- **Empirical thermal conductivity formulas**: Callaway model, Dubey model (used in some papers for analytical checks).  

### Tools & Software
- **First‑principles engines**: `VASP`, `Quantum ESPRESSO` (DFT for forces, total energies).  
- **Force‑constant extraction**: `Phonopy` (harmonic), `thirdorder` / `Phono3py` (anharmonic).  
- **Phonon BTE solvers**: `ShengBTE`, `almaBTE`, `Phono3py` (with built‑in relaxation‑time‑approximation or iterative schemes).  
- **Molecular dynamics** (complementary): LAMMPS with potentials like Stillinger–Weber, AIREBO, or machine‑learned potentials, for Green‑Kubo or NEMD conductivity.  
- **Data processing**: Python (NumPy, SciPy), Matminer (for composition‑based machine learning), Jupyter notebooks.  

## Verification Approach

**Type**: Numeric comparison  
The workflow is considered successfully reproduced when:
- The computed thermal conductivity values (temperature dependence, convergence with system size) agree with experimental measurements or previously validated theoretical results within a predefined tolerance.  
- Convergence tests (e.g., q‑point mesh, cutoff radius) confirm numerical stability.  
- (Optional) Spectral decomposition or mean‑free‑path analysis reproduces known trends (e.g., dominant phonon frequencies, grain‑size effects).  

Many papers cross‑check against published data from first‑principles calculations (e.g., CoSi, Si, Ge, half‑Heuslers, clathrates) or against their own MD simulations, ensuring the BTE pipeline is correct.

## Additional Notes
- Each subdirectory `paper‑*` inside this repository contains a self‑contained task; the public entry point is `instruction.md` (not `TASK.md`).  
- This workflow family covers both crystalline bulk materials and nanostructures (nanowires, thin films, superlattices). Scattering by boundaries and interfaces often requires explicit inclusion in the relaxation times.  
- When machine learning is employed, it is used only to rank compositions or predict effective medium conductivities; the core BTE pipeline remains the primary physics‑based tool.
