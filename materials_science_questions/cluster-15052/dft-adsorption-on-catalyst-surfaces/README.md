# DFT Adsorption on Catalyst Surfaces

This workflow family uses density functional theory (DFT) to compute adsorption energies, geometries, charge transfer, and electronic structure for small molecules on catalyst surfaces. It evaluates binding strength, activation, and site specificity. The workflow is a dry‑lab simulation and its results are verified by numeric comparison of computed quantities (e.g., adsorption energies, bond lengths, activation barriers) with experimental data or high‑level benchmarks.

## Common Computational Pattern

The papers in this family typically follow these steps:

1. **Model construction** – Build a periodic slab model (e.g., metal, oxide, carbide, 2D material) or a finite cluster model representing the catalyst surface. Introduce defects (vacancies, dopants) or adsorbed promoters as required.
2. **DFT calculations** – Perform spin‑polarized or non‑spin‑polarized DFT calculations using the Vienna Ab initio Simulation Package (VASP), DMol³, or similar codes. Commonly employed functionals are PBE (GGA), often with dispersion corrections (DFT‑D2, DFT‑D3) and, when needed, on‑site Hubbard U corrections (DFT+U). Basis sets include plane‑wave (with PAW pseudopotentials) and double‑numerical plus polarization (DNP) for localized‑basis codes.
3. **Geometry optimization** – Relax the atomic positions of the surface and any adsorbed species until forces fall below a threshold (e.g., 0.01–0.05 eV/Å). For reaction pathways, locate transition states using the nudged elastic band (NEB) or climbing‑image NEB method and confirm them by vibrational frequency analysis.
4. **Adsorption and reaction energies** – Calculate adsorption energy as:
   ```
   E_ads = E(slab+adsorbate) – E(slab) – E(adsorbate)
   ```
   (or analogous definitions; negative values indicate exothermic binding). For reactions, compute activation barriers and reaction energies from the energy profile.
5. **Electronic structure analysis** – Extract Bader, Mulliken, or Hirshfeld charges to quantify charge transfer. Compute projected density of states (PDOS), charge density differences, Mayer bond orders, or electrostatic potentials to rationalize binding and activation.
6. **Comparison with experiment / benchmarks** – Validate the computational model by comparing the calculated adsorption energies, bond lengths, and barriers with experimental data (e.g., temperature‑programmed desorption, kinetic measurements, X‑ray photoelectron spectroscopy) or with higher‑level theoretical references.

## Typical Verification Style

The workflow family is verified numerically: computed values (adsorption energies, activation barriers, bond lengths, charge transfers) are compared to experimental measurements or high‑level benchmark calculations, often with an acceptable tolerance range (e.g., a few tenths of an eV). This verification is performed without experimental lab work; the entire process is computational.

## Resources Commonly Referenced

- **Models** – periodic slab models of metal (e.g., Pd, Rh, Ni, Cu, Fe, Ir) and oxide (e.g., CeO₂, TiO₂, ZnO, MnO₂) surfaces, 2D materials (graphene, h‑BN, phosphorene, MXenes, graphitic carbon nitride), cluster models (zeolite‑type, metal particles).
- **Tools** – VASP, DMol³, ICON8 (Extended Hückel), B3LYP‑level cluster calculations (Gaussian).
- **Functionals** – PBE (GGA), PW91, B3LYP, PBE‑D3, PBE+U.
- **Analysis** – Bader charge, Mulliken population, Hirshfeld charge, projected density of states (PDOS), crystal orbital Hamilton population (COHP), Mayer bond orders, electron localization function (ELF).

## Workflow File Structure

Each paper’s implementation task lives in a subdirectory named `paper-<paper_id>`. The entry point is `instruction.md`, which contains the detailed computational protocol derived from the paper. The solving agent retrieves that file and any required input structures, then executes the DFT workflow.
