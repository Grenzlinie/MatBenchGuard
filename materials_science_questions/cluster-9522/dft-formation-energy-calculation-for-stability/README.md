# Workflow Family: DFT Formation Energy Calculation for Stability

## Overview
This workflow family covers first‑principles density functional theory (DFT) calculations of crystalline compounds to obtain formation energies. The goal is to assess thermodynamic stability relative to elemental (or solid) reference states. It is widely used in computational materials science, condensed‑matter physics, and quantum chemistry to screen new phases, model phase diagrams, and understand bonding.

## Common Computational Pattern
The core of each task is the computation of the formation energy per atom at 0 K (often used as an enthalpy proxy) from DFT total energies. The general procedure is:

1. **Obtain candidate crystal structures**  
   – From experimental databases (e.g., Crystallography Open Database, COD), literature prototypes, or structure‑prediction methods.  
   – Optionally, construct ordered supercells or Special Quasirandom Structures (SQS) to model disordered phases.

2. **Perform DFT total‑energy calculations**  
   – Employ plane‑wave codes (VASP, Quantum ESPRESSO, ABINIT) or all‑electron full‑potential methods (WIEN2k, FPLO).  
   – Common exchange‑correlation functionals are GGA‑PBE, GGA‑PW91, LDA, or PBEsol.  
   – Convergence parameters: plane‑wave cutoff, k‑point density, smearing, and force/stress thresholds are verified.  
   – Spin‑polarized calculations are used when magnetic ordering is relevant.  
   – Full relaxation of atomic positions and cell parameters is performed (zero‑pressure condition).

3. **Compute reference energies**  
   – Elementary phases (e.g., hcp Ti, bcc Nb, diamond Si, etc.) are computed with the same DFT settings.  
   – The average energy per atom of the pure element in its most stable crystal structure is used as the reference.

4. **Calculate formation energy**  
   The formation energy (enthalpy) per atom for a compound \(\mathrm{A}_x\mathrm{B}_y\) is given by:
   \[
   \Delta E_{\rm f} = \frac{E_{\mathrm{A}_x\mathrm{B}_y} - x\,E_{\rm ref}(\mathrm{A}) - y\,E_{\rm ref}(\mathrm{B})}{x+y}
   \]
   where \(E_{\mathrm{A}_x\mathrm{B}_y}\) is the total energy of the fully relaxed compound cell, and \(E_{\rm ref}\) are the per‑atom energies of the pure elements. Negative values indicate thermodynamic favorability.

5. **Stability analysis (optional but common)**  
   – Construct convex hulls (e.g., using AFLOW‑CHULL) to identify the lowest‑energy phases and check if a compound lies on the hull.  
   – Map formation energies onto cluster expansion or Compound Energy Formalism (CEF) parameters to model finite‑temperature phase diagrams.  
   – Compare relative stability of competing polymorphs or defect configurations.

## Typical Tools, Data, and Models
From the provided papers, the most frequently used tools are:
- **DFT packages**: VASP, Quantum ESPRESSO, WIEN2k, ABINIT, FPLO.  
- **Data repositories**: AFLOW.org (over 1.8 million compounds), Crystallography Open Database (COD).  
- **Modeling approaches**: plane‑wave pseudopotential method (PAW or USPP), all‑electron FP‑LAPW, GGA functionals (PBE, PW91).  
- **Advanced thermodynamic modeling**: AFLOW‑CHULL for convex hulls, Compound Energy Formalism (CEF) for sublattice models, cluster expansion (IT‑CVM) for configurational entropy.  

*Note: Other resources mentioned in specific papers (e.g., LAKIMOCA for kinetic Monte Carlo, specific interatomic potentials) may be required for individual tasks but are not part of the core DFT formation‑energy pipeline.*

## Verification
Verification of computed formation energies usually proceeds by:
- **Comparison with experimental calorimetric data** (e.g., measured enthalpies of formation). Agreement within a few kJ mol⁻¹ is typical.  
- **Convergence tests**: ensure that the total energy is converged with respect to plane‑wave cutoff, k‑point grid, and smearing to better than ~1 meV atom⁻¹.  
- **Lattice‑parameter check**: relaxed cell parameters should match experimental values (typically within ~1–2%).  
- **Numerical tolerance**: many studies set a convergence target of ~1 meV atom⁻¹ for total energies, which is considered sufficient for phase‑stability predictions.

## How a Task is Structured
Each `paper‑*` subdirectory is a self‑contained Harbor task. The public interface is `instruction.md`. The solving agent is expected to:
- Retrieve the atomic structures (from COD or other provided sources).
- Set up and run DFT calculations according to the computational parameters described in the paper.
- Compute formation energies using the elemental references specified in the paper.
- Optionally, perform additional analysis such as convex‑hull construction or mapping to thermodynamic models, if required by the conclusion.

## Output
A result summary containing the computed formation enthalpy per atom (with units), the relaxed lattice parameters, and any stability assessment (e.g., whether the phase lies on the convex hull). When experimental data are available, a comparison is provided.
