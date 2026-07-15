# DFT Mechanistic Analysis of CO₂ Reduction on Copper Surfaces

This workflow family covers density functional theory (DFT)-based computational studies that build atomic-scale models of copper-based catalyst surfaces, calculate reaction energetics (adsorption energies, activation barriers, free energies) for key elementary steps in CO₂ reduction, and analyze electronic structure to explain selectivity or activity trends.

## Common Computational Pattern

The core methodology across all papers in this family is periodic DFT calculations on copper-containing model systems. Typical steps include:

1. **Model construction** – building slab models of Cu single-crystal surfaces (e.g., Cu(111), Cu(100), Cu(110), stepped Cu(211)), Cu nanoparticles (clusters), Cu‑alloys (Cu‑Zn, Cu‑Ru, Cu‑Sb), doped oxides (S‑Cu₂O), metal‑organic frameworks (Cu‑MOF‑143), zeolites (CuY), or molecular complexes (Cu‑porphyrins).
2. **Energetic evaluation** – computing adsorption energies of key intermediates (*CO, *COOH, *CHO, *OCCOH, *H, etc.) and reaction energies for elementary steps using total‑energy differences.
3. **Kinetic barrier calculation** – locating first‑order saddle points (transition states) for bond‑forming/bond‑breaking steps, typically with the nudged elastic band (NEB) method, dimer method, or linear/quadratic synchronous transit (LST/QST) approaches; activation barriers (Eₐ) and zero‑point‑energy‑corrected values (Eₐ^(ZPEC)) are reported.
4. **Electrochemical free‑energy analysis** – applying the computational hydrogen electrode (CHE) model to convert gas‑phase/adsorbate DFT energies into free‑energy diagrams as a function of applied potential (U vs RHE). From these diagrams the potential‑limiting step and the corresponding overpotential are identified.
5. **Electronic‑structure interpretation** – calculating descriptors such as Bader charges, d‑band centres, s‑band centres, electrostatic potentials, or CO vibrational frequencies to rationalise trends in adsorption strength and catalytic activity.

These calculations are carried out with widely used plane‑wave DFT codes (VASP, DMol³) and standard exchange‑correlation functionals (PBE, rPBE, BEEF‑vdw). A typical workflow yields a comprehensive reaction network (e.g., 46 elementary steps for CO₂‑to‑methanol on Cu(111)) and numerical tables of formation/adsorption energies and activation barriers that can be directly compared across different catalysts.

## Verification Style

Verification within this family relies on numeric comparison: computed adsorption energies and reaction barriers are checked against previously published values with an acceptance tolerance of **0.1 eV**. Exact reproduction of literature values within this tolerance confirms that the calculation setup and numerical convergence are correct.

## Dataset / Model / Tool Categories

- **DFT software**: VASP, DMol³
- **Exchange‑correlation functionals**: PBE, rPBE, BEEF‑vdw
- **Surface models**: Cu(111), Cu(100), Cu(110), Cu(211) slabs; Cu clusters (Cun, n = 8–55); Cu alloys (CuₓRu₁₋ₓ, CuₓZn₁₀₋ₓ, Cu‑Sb); S‑doped Cu₂O; CuTCNQ; Cu zeolites; Cu porphyrins
- **Reaction‑path methods**: linear synchronous transit/quadratic synchronous transit (LST/QST), nudged elastic band (NEB), dimer method, minimum‑mode following
- **Electrochemical model**: computational hydrogen electrode (CHE)
- **Key energetic quantities**: adsorption energy ΔE_ads, formation energy E_form, activation barrier Eₐ (including ZPE correction), reaction free energy ΔG, limiting potential U_L
- **Electronic descriptors**: Bader charge, d‑band centre, s‑band centre, electrostatic potential maps, CO vibrational frequency, density of states (DOS)
- **Computational parameters**: plane‑wave cutoffs (400–500 eV), k‑point meshes (e.g., 4×3×1 Monkhorst‑Pack), slab layers (3–4), force convergence (0.01–0.05 eV Å⁻¹), vacuum gaps (~15 Å)

## Task Structure

Each paper in this workflow family is packaged as a standalone Harbor task in a subdirectory named `paper-<paper_id>`. The public instruction file for every task is **`instruction.md`**, which contains the specific objective for that paper’s replication (e.g., “reproduce the CO adsorption energies on strained Cu(100)”, “verify the activation barrier for CO→CHO on Cu(110)”, etc.). The solving agent is expected to read this file, set up and run the required DFT calculations, and return results that match the original study within the prescribed tolerance.
