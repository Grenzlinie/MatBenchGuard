# Surface relaxation calculations from slab models

## Overview
This workflow family encompasses computational studies that quantify atomic-scale surface relaxations by constructing periodic slab models, relaxing atomic positions using electronic structure methods, and reporting geometric changes such as interlayer spacings, rumpling, and bond lengths. The family includes 185 tasks derived from 116 papers, primarily in the domains of surface science, computational materials science, and condensed matter physics. All tasks are dry‑lab (purely computational) and use numeric verification against experimental data or high‑accuracy calculations.

## Common computational pattern
The core methodology across these tasks involves:
1. **Slab construction** – Build a periodic slab model with a vacuum layer to represent a semi‑infinite surface, typically using bulk‑derived lattice parameters.
2. **Electronic‑structure relaxation** – Minimise the total energy with respect to atomic coordinates (and sometimes the in‑plane lattice constant or cell shape) using a chosen electronic structure method. The relaxation focuses on interlayer distances, rumpling (differential displacement of anions and cations in the same layer), and bond‑length changes near the surface.
3. **Quantification of geometric changes** – Extract percentage changes in interlayer spacings (Δd₁₂, Δd₂₃, …), rumpling amplitudes, and bond‑length variations from the relaxed slab. These are the primary outputs compared to reference data.

## Methods and tools
The tasks employ a variety of electronic structure and atomistic simulation approaches:
- **Density functional theory (DFT)** – Most common, using plane‑wave pseudopotential codes such as VASP, Quantum ESPRESSO (PWscf), OpenMX, and GPAW. Functionals include LDA, GGA (PBE, PW91), and DFT+U. Pseudopotential types include ultra‑soft and PAW.
- **Tight‑binding models** – Non‑orthogonal Sp³ or d‑band parametrisations, sometimes combined with a Born–Mayer repulsive term or a second‑moment approximation (e.g., for surface phonons or cluster studies).
- **Empirical potentials** – Modified Embedded Atom Method (MEAM), Tersoff bond‑order potential, and Coulomb plus Born–Mayer pair potentials have been used for large‑scale or classical relaxation studies.
- **Monte Carlo and force‑field methods** – Used in contexts such as surface tension or adsorption energetics.

Slab models typically contain 5‑15 atomic layers, with vacuum thicknesses of 10–15 Å. Relaxation is often restricted to the top few layers, with the central layers fixed at bulk positions. Force and energy convergence thresholds are clearly reported (e.g., 0.01 eV/Å, 10⁻⁶ eV/atom).

## Verification style
Verification is **numeric**, meaning the computed relaxation percentages, interlayer spacings, and rumpling are compared to experimental measurements (LEED, ion scattering, X‑ray diffraction) or to high‑accuracy computational benchmarks. A tolerance‑based approach is used, often via root‑mean‑square deviations (RMSD) or within‑range checks. For example, a Δd₁₂ value of −2.5 % may be accepted if it falls within a few percent of the experimental LEED value. The `verify_note` in the family metadata explicitly states: “通过计算得到的弛豫百分比、层间距变化等数值与实验数据或高精度计算结果进行数值容差对比（如RMSD）.”

## Directory structure
Each task lives in a separate `paper-*` subdirectory. The public entry point is `instruction.md`, which contains all necessary resources and steps to reproduce the surface relaxation calculation.

## Notes
- All tasks are dry‑lab (no wet‑lab experiments).
- Typical substrates include metals (Al, Cu, Rh, W, …), oxides (MgO, TiO₂, Al₂O₃, …), and compound semiconductors.
- The family covers both clean‑surface relaxation and the effect of adsorbates or point defects on relaxation.
