# Phonon-based Dynamical Stability Analysis

## Overview
This workflow family performs first‑principles phonon calculations to assess the dynamical stability of crystalline materials. Starting from a relaxed DFT structure, it computes the full phonon dispersion relation and the phonon density of states. The primary stability criterion is the absence of imaginary (negative‑squared) phonon frequencies across the Brillouin zone; such imaginary modes indicate a lattice instability. The analysis is purely computational (dry lab) and covers a broad range of materials, including 2D monolayers, bulk oxides, hydrides, MXenes, and topological systems.

## Typical Computational Pattern
Every paper in this family follows a common sequence, with variations only in the DFT setup and the phonon‑calculation implementation:

1. **Structure preparation** – Build or obtain the initial crystal structure (often from previous DFT relaxations or experimental data).
2. **DFT relaxation** – Optimise lattice parameters and atomic positions using a plane‑wave DFT code. The most frequently used codes are **VASP**, **Quantum ESPRESSO**, and **CASTEP**. Common exchange‑correlation functionals include **PBE‑GGA**, **LDA**, and **HSE06** for band‑gap sensitive materials.
3. **Force‑constant calculation** – Determine harmonic interatomic force constants. Two approaches appear:
   - **Finite‑displacement (direct) method**: atoms are slightly displaced in a supercell, and Hellmann‑Feynman forces are collected. Tools: **Phonopy** (most common), **MedeA‑Phonon**.
   - **Density‑functional perturbation theory (DFPT)**: linear‑response calculations directly on the primitive cell. Tools: **Quantum ESPRESSO** DFPT, **VASP** DFPT (with **Phonopy** post‑processing).
4. **Phonon dispersion & DOS** – Build the dynamical matrix from the force constants and diagonalise to obtain phonon frequencies $\omega(\mathbf{q})$ and eigenvectors. Generate the phonon band structure and density of states.
5. **Stability assessment** – Look for **imaginary (negative) phonon modes**. If no mode shows $\omega^2 < 0$ (or the imaginary part falls below a tolerance, e.g., $\sim 1-10\,\mathrm{cm}^{-1}$), the structure is deemed *dynamically stable*. When imaginary modes exist, they are often analysed to predict possible structural transitions (e.g., by freezing in the soft‑mode eigenvector).

Some papers supplement the phonon analysis with elastic‑constant checks (Born stability criteria) or *ab‑initio* molecular dynamics (AIMD) to confirm thermal stability.

## Verification Style
Stability is verified **numerically** using the computed phonon spectrum:
- **Primary criterion**: No imaginary phonon frequencies anywhere in the Brillouin zone. The presence of any imaginary mode renders the structure dynamically unstable.
- **Tolerance**: Experimentally, very small imaginary modes ($<10\,\mathrm{cm}^{-1}$) are sometimes tolerated as numerical artefacts. The family’s `verify_note` explicitly mentions checking the imaginary part of phonon frequencies against a tolerance threshold (e.g., $1$–$10\,\mathrm{cm}^{-1}$).
- In some cases, the analysis includes **elastic stability** (positive eigenvalues of the stiffness tensor) to cross‑validate the phonon results.

This numeric verification is purely computational; no experimental data are required.

## Resources / Dependencies
All resources are obtained from the context provided in each paper’s `instruction.md`. The workflow does **not** bundle any software or models; the solving agent must provision them. Commonly referenced tools and models in this family include:

- **DFT codes**: VASP (most frequent), Quantum ESPRESSO, CASTEP.
- **Phonon codes**: Phonopy (finite‑displacement or DFPT post‑processing), MedeA‑Phonon, Quantum ESPRESSO DFPT.
- **Exchange‑correlation functionals**: PBE (GGA), LDA, PBEsol, HSE06, HSE06+SOC.
- **Additional packages**: BoltzTraP2 (transport), CALYPSO (structure search), GULP (empirical potentials).
- **Input data**: Optimised crystal structures (lattice constants, atomic coordinates) are always required. For finite‑displacement methods, supercell sizes (e.g., $2\times2\times1$, $4\times4\times1$) are specified in the original papers.

No custom datasets are required beyond what the individual paper tasks already provide.

## How Tasks Are Organised
Each `paper-*` subdirectory corresponds to a single published study and is a **standalone Harbor task**. Inside, the public entry point is an **`instruction.md`** file that describes the objective, the required input structures, the expected outputs (phonon dispersion, stability verdict), and any specific parameters (k‑point grids, cutoff, supercell size). The solving agent can complete the task by following the instructions and using its own DFT/phonon resources; no additional files from this repository are needed.

## Output Highlights
The typical deliverables of a successful run are:
- Phonon dispersion plots (`.png`, `.pdf`).
- List of phonon frequencies, including detection of imaginary modes.
- A stability verdict (stable / unstable) with the size of the largest imaginary frequency if any.
- (Optional) Elastic constant checks and AIMD snapshots when required by the paper.

## Further Notes
- This workflow family originates from the domain of **computational condensed‑matter physics**, with applications in materials science and computational chemistry.
- For papers that report soft‑mode driven phase transitions, the post‑processing often involves **mode following** – displacing the structure along the unstable eigenvector and relaxing it to find lower‑energy polymorphs. Such workflows are built on top of the basic phonon stability check.
