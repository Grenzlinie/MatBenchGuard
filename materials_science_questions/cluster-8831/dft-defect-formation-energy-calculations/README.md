# DFT Defect Formation Energy Calculations

## Overview
This workflow family encompasses first‑principles calculations of point‑defect formation energies in solids, primarily using density functional theory (DFT) supercell approaches. The target is the quantitative prediction of defect concentrations, charge‑state stabilities, and related thermodynamic quantities, often validated against experimental measurements.

## Common Computational Pattern

The core computational pattern across papers is:

1. **Structure construction** – Build a supercell of the host crystal and introduce a point defect (vacancy, interstitial, antisite, or defect complex).
2. **Electronic‑structure calculation** – Perform DFT total‑energy calculations, typically with the *Vienna Ab‑initio Simulation Package* (VASP) or similar plane‑wave pseudopotential codes. Functionals range from GGA (PBE) to hybrid functionals (HSE06) and DFT+U to correct self‑interaction errors. Spin‑orbit coupling may be included for heavy elements.
3. **Formation energy evaluation** – Compute the defect formation energy as a function of Fermi level and atomic chemical potentials. The standard expression is  
   `E^f[D^q] = E_tot[D^q] – E_tot[bulk] – Σ n_i µ_i + q E_F + E_corr`,  
   where `E_corr` accounts for finite‑size electrostatic interactions (e.g., Makov‑Payne or Freysoldt corrections). Chemical potentials are chosen to reflect growth conditions (e.g., O‑rich, metal‑rich).
4. **Post‑processing** – Extract charge‑transition levels, binding energies of complexes, migration barriers (via NEB or climbing‑image methods), and equilibrium defect concentrations using statistical mechanics (Boltzmann distribution or grand‑canonical formalism).

Some papers integrate DFT energetics with statistical‑mechanical models (e.g., quasi‑chemical reactions) or continuum approaches to predict defect populations under varying temperature and pressure.

## Verification Style

Verification is **numeric**: calculated formation energies, charge‑transition levels, activation energies, and defect concentrations are compared against experimental values (e.g., positron annihilation, diffusion measurements, or transport data) or against previous benchmark calculations. Agreement within a few tenths of an eV is typically required, or the computed trend must reproduce the observed dependence on chemical potential, pressure, or temperature.

## Required Resources

- **DFT codes**: VASP, Quantum ESPRESSO, AIMPRO, and occasionally PWscf.
- **Post‑processing tools**: Phonopy (for vibrational stability), BANDUP (for spectral function unfolding), and in‑house scripts for formation‑energy analysis.
- **Reference databases**: C2DB, OQMD, and the Materials Project for chemical potentials and competing phases.
- **Statistical‑mechanics codes**: Custom quasi‑chemical equilibrium solvers.

## Typical Workflow Tasks

Each `paper‑*` subdirectory contains an `instruction.md` specifying:
- The defect type and the host material.
- The computational setup (cell size, k‑point mesh, functional).
- The chemical potential ranges to be explored.
- The output quantities (formation energies, transition levels, binding energies).

No fixed bundling is required; the solver agent obtains all needed resources from the instruction and the provided metadata.
