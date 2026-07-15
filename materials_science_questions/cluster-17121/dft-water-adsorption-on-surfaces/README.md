# DFT Water Adsorption on Surfaces

## Overview
This workflow family encompasses computational studies of water (H₂O) adsorption on various mineral and metal surfaces using electronic structure methods, primarily density functional theory (DFT), and often complemented by molecular dynamics (MD) simulations. The typical research objectives include:
- Determination of the most stable adsorption configuration (molecular vs. dissociative)
- Calculation of adsorption energies (ΔE_ads)
- Analysis of geometric and electronic structure changes upon adsorption
- Investigation of coverage effects, hydrogen‑bonding networks, and water layer ordering
- Comparison with experimental data (adsorption energies, vibrational frequencies, bond lengths, surface energies) to validate the computational model

## Common Computational Pattern
Although individual studies vary in method and detail, a typical workflow follows these steps:

1. **Slab/Cluster Model Preparation**  
   - Obtain bulk crystal structure from experiment or literature  
   - Cut a suitable surface termination (e.g., (0001), (001), (110))  
   - Create a periodic slab or finite cluster model with a vacuum gap  
   - Passivate dangling bonds or fix bottom layers to mimic the bulk  

2. **Water Adsorption**  
   - Place one or several H₂O molecules at various initial positions (top, bridge, hollow sites)  
   - Consider both molecular (intact H₂O) and dissociative (OH⁻ + H⁺) adsorption  

3. **Geometry Optimization / Molecular Dynamics**  
   - Relax the adsorbate and surface atoms (static DFT optimization or MD)  
   - In MD studies, run dynamics to sample hydrogen‑bond networks, water layer formation, and thermal fluctuations  

4. **Property Calculation**  
   - Adsorption energy:  
     \(\Delta E_{\text{ads}} = E_{\text{slab+water}} - (E_{\text{slab}} + n E_{\text{H₂O}})\)  
   - Geometric parameters: adsorbate‑surface distances, bond lengths, angles  
   - Electronic properties: charge transfer, density of states, vibrational spectra  
   - Interfacial structure: density profiles, hydrogen‑bond statistics, radial/angular distribution functions  

5. **Verification and Publication**  
   - Compare computed adsorption energies, bond lengths, or vibrational frequencies against experimental data or high‑level reference calculations  
   - Quantify agreement within a tolerance (e.g., energy differences in kcal/mol, distances in Å, frequency shifts in cm⁻¹)

## Typical Resources
Required computational tools and datasets are described in each task’s `instruction.md`. Common categories include:
- **DFT codes**: VASP, Gaussian, Dmol³, FHI‑aims, Quantum ESPRESSO  
- **Classical MD / Force‑Field codes**: Gromacs, LAMMPS, METADISE, in‑house programs  
- **Water models**: SPC, SPC/E, TIP3P, TIP4P, flexible variants  
- **Force fields**: AMBER, OPLS‑AA, CLAYFF, special metal‑water potentials  
- **Analysis methods**: Basin‑hopping global optimization, Steele summation for graphite, hydrogen‑bond criteria, vibrational DOS from velocity autocorrelation  

All specific dependencies are bundled per paper; the solving agent will retrieve them.

## Verification Style
This family uses **numeric** verification. The computed results (adsorption energies, bond lengths, adsorption heights, vibrational frequencies) are compared against experimental measurements or higher‑accuracy reference values. Agreement is typically considered successful when the deviation falls within a stated tolerance (e.g., a few kcal/mol for ΔE_ads, ±0.1 Å for distances, or within a few cm⁻¹ for IR peaks). The `verify_note` explicitly states that alignment is done by “computing adsorption energies, geometric parameters, and other numerical values with tolerance alignment to experiments or high‑precision reference data.”

## Task Structure
Each paper in the workflow family corresponds to a standalone Harbor task located in a subdirectory `paper‑<paper_id>`. The public entry point is `instruction.md`, which specifies the required computation, the expected output, and the verification criteria. No additional top‑level configuration is needed.
