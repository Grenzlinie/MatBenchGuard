# Lattice Energy Calculation for Crystal Stability

This workflow family focuses on computing lattice energies of molecular and ionic crystals to evaluate relative stability, ranking of polymorphs, cocrystals, and other solid-state forms. The computations span a range of methods, from periodic density functional theory (DFT) to classical force fields, and typically include geometry optimization and energy decomposition.

## Common Computational Pattern

1. **Input Crystal Structure**  
   Start from an experimentally determined crystal structure (e.g., from X‑ray diffraction) or a predicted structure obtained from molecular modeling.
2. **Method Selection**  
   Choose a computational method appropriate for the system:
   - **Periodic DFT** (e.g., B3LYP‑D3, PBE‑D3) with plane‑wave or localized basis sets, optionally including basis‑set superposition error (BSSE) corrections.
   - **Classical force fields** using atom–atom potentials (Buckingham, Lennard‑Jones, hydrogen‑bond terms) and point‑charge electrostatics.
3. **Geometry Relaxation**  
   Relax atomic positions and possibly unit cell parameters to a minimum energy configuration while preserving the space group symmetry. For rigid‑molecule models, only molecular positions and orientations are optimized.
4. **Lattice Energy Computation**  
   Compute the total lattice energy as the difference between the optimized crystal energy and the sum of isolated molecule (or ion) energies. For periodic DFT, this includes all intermolecular interactions within the unit cell and long‑range corrections. For force fields, the energy is typically decomposed into van der Waals and electrostatic contributions.
5. **Verification and Stability Analysis**  
   Compare computed lattice energies or derived properties (sublimation enthalpy, density, melting point) with experimental data. Rank different crystal forms (polymorphs, cocrystals) by energy; the most stable form corresponds to the lowest (most negative) lattice energy.

## Key Resources

**Datasets**  
- Experimentally determined crystal structures from the Cambridge Structural Database (CSD) or other crystallographic databases.  
- Reference experimental thermodynamic data: sublimation enthalpies, melting points, heats of formation, densities.

**Models**  
- DFT functionals with dispersion corrections (B3LYP‑D3, PBE‑D3, B2PLYP) and basis sets (pob‑TZVP, TZVP, 6‑311G(d,p)).  
- Atom–atom potential parameter sets: Williams, Gavezzotti–Filippini (GVF), Mirsky (MRK), Kihara core potentials, Stillinger–Rahman (ST2).  
- Force fields: PCK6, OPEC, AIREBO, OPLS3.

**Tools**  
- Periodic DFT codes: CRYSTAL, VASP, DMAREL.  
- Molecular DFT codes: Gaussian, ORCA.  
- Lattice dynamics and relaxation: GULP, LAMMPS, MOPAC.  
- Custom lattice energy minimizers and cluster programs.

## Verification Style

**Numeric verification**: The primary validation method is quantitative comparison of computed lattice energies, sublimation enthalpies, or unit cell parameters against experimental measurements. Acceptable agreement is usually within a few kJ mol⁻¹ for energies and within a few percent for cell dimensions. When experimental lattice energies are unavailable, derived properties (density, melting temperature, detonation performance) are used for indirect validation.
